"""Enrich Garmin strength workouts with Tonal set data, end to end.

For each recent Garmin strength activity that has no exercise sets yet, find the
matching recent Tonal workout, merge the two into one FIT file, upload it, and
then delete the original Garmin activity (after saving a backup of it).

Configuration comes from environment variables so this can run unattended
(e.g. as a Home Assistant add-on):

  TONAL_EMAIL, TONAL_PASSWORD     Tonal login (required)
  GARMIN_EMAIL, GARMIN_PASSWORD   Garmin login (only needed if no cached tokens)
  GARMIN_TOKEN_DIR                Where Garmin login tokens are cached
                                  (default ~/.garminconnect; use a persistent dir)
  DATA_DIR                        Backups, outputs and state (default ./data)
  TONAL_LOOKBACK                  How many recent Tonal workouts to consider (default 5)
  GARMIN_SCAN                     How many recent Garmin activities to scan (default 30)
  UPLOAD_WAIT                     Seconds to wait for Garmin to process an upload (default 120)

Usage: python tonal_to_garmin.py [--dry-run]

  --dry-run   Do everything except upload to / delete from Garmin Connect.

Safety: the original FIT is saved to DATA_DIR/backups before anything changes, the
new file is parsed back before upload, and the original is only deleted once Garmin
has confirmed the upload. A Tonal workout is never processed twice.
"""
import itertools
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from fit_tool.fit_file import FitFile
from fit_tool.profile.messages.set_message import SetMessage
from fit_tool.profile.profile_type import SetType

import fetch_garmin
import requests

from movement_map import MOVEMENT_MAP
from sync_workouts import API_BASE, authenticate, download_workouts, get_user_info, get_workout_template
from tonal2fit import merge_tonal_and_garmin, TONAL_REST_ID
from update_movements import trim

DATA_DIR = Path(os.environ.get("DATA_DIR", "data"))
BACKUP_DIR = DATA_DIR / "backups"
OUTPUT_DIR = DATA_DIR / "combined"
STATE_FILE = DATA_DIR / "state.json"
CATALOG_CACHE = DATA_DIR / "movements_cache.json"
CATALOG_SNAPSHOT = Path(__file__).parent / "tonal_movements.json"


def log(msg: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}", flush=True)


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise SystemExit(f"Missing required environment variable {name}")
    return value


# --- state -------------------------------------------------------------------

def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"processed": {}}


def save_state(state: dict) -> None:
    tmp = STATE_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2))
    tmp.replace(STATE_FILE)


# --- helpers -----------------------------------------------------------------

def verify_fit(path: Path, tonal: dict) -> int:
    """Parse the generated file back and check its active sets against Tonal's."""
    fit = FitFile.from_file(str(path))
    active = [r.message for r in fit.records
              if isinstance(r.message, SetMessage) and r.message.set_type == SetType.ACTIVE.value]
    expected = sum(1 for b in tonal.get("workoutSetActivity", [])
                   if b.get("movementId") != TONAL_REST_ID and (b.get("repCount") or b.get("movementId")))
    if not active or len(active) != expected:
        raise ValueError(f"generated FIT has {len(active)} active sets, expected {expected}")
    return len(active)


def upload(client, path: Path) -> bool:
    """Upload a FIT file. Returns True if Garmin flagged it as a duplicate.

    Garmin processes uploads asynchronously: a successful upload usually comes back
    with an uploadId but no activity ID yet, so success is confirmed separately by
    wait_for_activity().
    """
    try:
        result = client.upload_activity(str(path))
    except Exception as e:  # the library raises on HTTP 409 (duplicate)
        if "409" in str(e) or "uplicate" in str(e):
            return True
        raise
    detail = (result or {}).get("detailedImportResult", result or {})
    failures = detail.get("failures") or []
    if failures:
        text = json.dumps(failures).lower()
        if "duplicate" in text or '"code": 202' in text:
            return True
        raise RuntimeError(f"Garmin rejected the upload: {failures}")
    return False


def _gmt(text: str) -> datetime:
    dt = datetime.fromisoformat(text.replace("Z", "+00:00").replace(" ", "T"))
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def find_new_activity(client, original_id, tonal: dict):
    """Find an activity other than the original that starts when the Tonal workout did."""
    begin = _gmt(tonal["beginTime"])
    for a in client.get_activities(0, 10):
        if str(a["activityId"]) == str(original_id) or not a.get("startTimeGMT"):
            continue
        if abs((_gmt(a["startTimeGMT"]) - begin).total_seconds()) <= 120:
            return a
    return None


def wait_for_activity(client, original_id, tonal: dict, timeout: int):
    """Poll until the uploaded activity appears and Garmin has parsed its exercise sets."""
    deadline = time.time() + timeout
    found = None
    while True:
        found = find_new_activity(client, original_id, tonal) or found
        if found and fetch_garmin.is_enriched(client, found["activityId"]):
            return found
        if time.time() >= deadline:
            return None if not found else {**found, "_unenriched": True}
        time.sleep(5)


def process_match(client, act: dict, tonal: dict, tonal_json: Path, original: Path,
                  combined: Path, dry_run: bool, state: dict) -> None:
    activity_id = act["activityId"]
    count = verify_fit(combined, tonal)
    log(f"Built {combined.name}: {count} active sets")

    if dry_run:
        log(f"Dry run: not uploading or deleting. Activity would be named: {tonal.get('_title') or act.get('activityName')!r}")
        return

    timeout = int(os.environ.get("UPLOAD_WAIT", 120))
    original_deleted = False

    if upload(client, combined):
        # Either an earlier run already uploaded it, or Garmin rejects it while the
        # original overlaps it.
        new = find_new_activity(client, activity_id, tonal)
        if new:
            log(f"Garmin flagged a duplicate and activity {new['activityId']} already exists.")
        else:
            log(f"Garmin flagged a duplicate; deleting original {activity_id} (backed up) and retrying.")
            client.delete_activity(activity_id)
            original_deleted = True
            if upload(client, combined):
                raise RuntimeError(
                    f"Upload was refused again after deleting the original. Backup: {original}")
    else:
        log("Upload accepted; waiting for Garmin to process it.")

    new = wait_for_activity(client, activity_id, tonal, timeout)
    if not new or new.get("_unenriched"):
        where = "no new activity appeared" if not new else f"activity {new['activityId']} has no exercise sets"
        raise RuntimeError(
            f"Could not confirm the upload ({where} within {timeout}s). "
            f"{'The original was already deleted; restore from ' + str(original) if original_deleted else 'The original was left in place.'}")

    new_id = new["activityId"]
    if not original_deleted:
        log(f"Confirmed new activity {new_id}; deleting original {activity_id}.")
        client.delete_activity(activity_id)

    try:  # name it after the Tonal workout, falling back to the original Garmin name
        name = tonal.get("_title") or act.get("activityName")
        if name:
            client.set_activity_name(str(new_id), name)
    except Exception as e:
        log(f"Could not copy activity name (not critical): {e}")

    state["processed"][tonal["id"]] = {"garmin_original": activity_id, "garmin_new": new_id,
                                       "at": datetime.now().isoformat()}
    save_state(state)
    log("Done.")


# --- movement catalog --------------------------------------------------------

def _load_catalog(path: Path) -> dict:
    return {m["id"]: m for m in json.loads(path.read_text())} if path.exists() else {}


def check_movements(id_token: str, workouts: list) -> frozenset:
    """Log movements we can't map, and find barbell movements new since the last snapshot.

    Tonal's movement catalog is only downloaded when a workout contains an ID that is
    in neither movement_map.py, the shipped tonal_movements.json snapshot, nor the
    local cache from an earlier download, so normal runs make no extra requests.
    Returns the IDs of straight-bar movements missing from BARBELL_MOVEMENTS.
    """
    known = _load_catalog(CATALOG_SNAPSHOT)
    known.update(_load_catalog(CATALOG_CACHE))
    used = {b.get("movementId") for w in workouts for b in w.get("workoutSetActivity", [])}
    used.discard(None)
    if any(i not in MOVEMENT_MAP and i not in known for i in used):
        log("Workout has movement(s) not seen before; downloading Tonal's movement catalog (once).")
        r = requests.get(f"{API_BASE}/v6/movements", headers={"Authorization": f"Bearer {id_token}"}, timeout=60)
        r.raise_for_status()
        fresh = {m["id"]: trim(m) for m in r.json()}
        known.update(fresh)
        CATALOG_CACHE.write_text(json.dumps(list(known.values())))
    for i in sorted(used):
        if i in MOVEMENT_MAP or i == TONAL_REST_ID:
            continue
        m = known.get(i)
        log(f"No Garmin mapping for movement {i} ({m['name'] if m else 'not in Tonal catalog'}); "
            f"its sets will have no exercise type. Add it to movement_map.py.")
    from movement_map import BARBELL_MOVEMENTS
    return frozenset(i for i in used if (known.get(i) or {}).get("accessory") == "StraightBar"
                     and i not in BARBELL_MOVEMENTS)


# --- activity naming ---------------------------------------------------------

_program_cache: dict = {}


def activity_name(id_token: str, tonal: dict):
    """Name the activity the way the Tonal app shows it.

    Program workouts become "<program name> - Workout <n>" (e.g. "Modern Muscle -
    Workout 20"); anything else uses the workout template's title. Returns None if
    nothing is available, so the caller keeps the original Garmin name.
    """
    template = get_workout_template(id_token, tonal["workoutId"]) or {}
    title = template.get("title")
    program_id = tonal.get("programId")
    if program_id:
        if program_id not in _program_cache:
            r = requests.get(f"{API_BASE}/v6/programs/{program_id}",
                             headers={"Authorization": f"Bearer {id_token}"}, timeout=30)
            _program_cache[program_id] = r.json() if r.status_code == 200 else {}
        program = _program_cache[program_id]
        number = next((w.get("workoutNumber") for w in program.get("programWorkouts") or []
                       if w.get("workoutId") == tonal["workoutId"]), None)
        if number is None and title:  # titles end like "... - WO20 (W4D5)"
            m = re.search(r"\bWO(\d+)\b", title)
            number = int(m[1]) if m else None
        if program.get("name") and number is not None:
            return f"{program['name']} - Workout {number}"
    return title


# --- main --------------------------------------------------------------------

def could_match(act: dict, tonal: dict, slack: float = 60) -> bool:
    """Cheap pre-check from the activity list: the same window tonal2fit enforces
    (Garmin starts no later than Tonal + slack, ends no earlier than Tonal - slack)."""
    if not act.get("startTimeGMT"):
        return True  # can't tell; let the real check decide
    start = _gmt(act["startTimeGMT"])
    length = max(act.get("elapsedDuration") or 0, act.get("duration") or 0)
    return ((start - _gmt(tonal["beginTime"])).total_seconds() <= slack and
            (start - _gmt(tonal["endTime"])).total_seconds() + length >= -slack)


def main() -> int:
    dry_run = "--dry-run" in sys.argv or os.environ.get("DRY_RUN") == "1"
    for d in (DATA_DIR, BACKUP_DIR, OUTPUT_DIR):
        d.mkdir(parents=True, exist_ok=True)
    state = load_state()

    # Garmin first: if there is nothing to enrich, don't bother Tonal.
    client = fetch_garmin.login()
    garmin_acts = fetch_garmin.unenriched_strength_activities(  # lazy, newest first
        client, int(os.environ.get("GARMIN_SCAN", 30)))
    first = next(garmin_acts, None)
    if first is None:
        log("No unenriched Garmin strength activities. Nothing to do.")
        return 0

    tokens = authenticate(require_env("TONAL_EMAIL"), require_env("TONAL_PASSWORD"))
    id_token = tokens["id_token"]
    user_id = get_user_info(id_token)["id"]
    workouts = download_workouts(id_token, user_id, int(os.environ.get("TONAL_LOOKBACK", 5)))
    workouts.sort(key=lambda w: w.get("beginTime", ""), reverse=True)
    todo = [w for w in workouts if w["id"] not in state["processed"]]
    if not todo:
        log("All recent Tonal workouts were already processed.")
        return 0
    oldest_begin = min(_gmt(w["beginTime"]) for w in todo)
    extra_barbell = check_movements(id_token, todo)

    failures = 0
    for act in itertools.chain([first], garmin_acts):
        if not todo:
            log("All Tonal workouts handled; done.")
            break
        activity_id = act["activityId"]
        if act.get("startTimeGMT") and (_gmt(act["startTimeGMT"]) - oldest_begin).total_seconds() < -3600:
            log("Remaining Garmin activities are older than the Tonal workouts; done.")
            break
        matches = [t for t in todo if could_match(act, t)]
        if not matches:
            log(f"Garmin activity {activity_id} ({act.get('startTimeLocal')}): no Tonal workout overlaps it; skipping.")
            continue

        log(f"Garmin activity {activity_id} ({act.get('startTimeLocal')}): checking {len(matches)} Tonal workout(s).")
        original = BACKUP_DIR / f"{activity_id}_ACTIVITY.fit"
        # Back up first, before anything else touches this activity.
        original.write_bytes(fetch_garmin.download_original_fit(client, activity_id))

        for tonal in matches:
            tonal_json = BACKUP_DIR / f"{activity_id}_tonal.json"
            tonal_json.write_text(json.dumps(tonal))
            combined = OUTPUT_DIR / f"{activity_id}_ACTIVITY_COMBINED.fit"
            try:
                matched = merge_tonal_and_garmin(str(tonal_json), str(original), str(combined), extra_barbell)
            except Exception as e:
                log(f"Merge error with Tonal workout {tonal['id']}: {e}")
                matched = False
            if not matched:
                continue
            log(f"Matched Tonal workout {tonal['id']} ({tonal.get('beginTime')}).")
            try:
                tonal["_title"] = activity_name(id_token, tonal)
            except Exception as e:
                log(f"Could not look up the Tonal workout name (not critical): {e}")
            try:
                process_match(client, act, tonal, tonal_json, original, combined, dry_run, state)
            except Exception as e:
                failures += 1
                log(f"ERROR processing activity {activity_id}: {e}")
            todo.remove(tonal)  # handled (success or failure): don't try it on other activities
            break
        else:
            log(f"No matching Tonal workout for {activity_id}; leaving it alone.")
            (BACKUP_DIR / f"{activity_id}_tonal.json").unlink(missing_ok=True)
            original.unlink(missing_ok=True)  # nothing was changed, no backup needed

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
