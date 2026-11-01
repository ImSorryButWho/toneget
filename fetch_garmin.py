"""Download the latest not-yet-enriched strength workout from Garmin Connect.

Usage: python fetch_garmin.py [output.fit] [--all-strength]

Saves the original FIT file recorded by the watch, ready to feed to tonal2fit.py.
"""
import io
import os
import sys
import zipfile
from getpass import getpass
from pathlib import Path

from garminconnect import Garmin

TOKEN_DIR = Path(os.environ.get("GARMIN_TOKEN_DIR", Path.home() / ".garminconnect"))


def _prompt_mfa() -> str:
    if not sys.stdin.isatty():
        raise RuntimeError(
            "Garmin requires an MFA code but this is not an interactive session. "
            "Run `python fetch_garmin.py` once interactively (with the same "
            "GARMIN_TOKEN_DIR) to cache login tokens."
        )
    return input("Garmin MFA code: ").strip()


def login() -> Garmin:
    """Log in, reusing cached tokens when available.

    Credentials come from GARMIN_EMAIL / GARMIN_PASSWORD, falling back to prompts
    when run interactively. Tokens are cached in GARMIN_TOKEN_DIR.
    """
    try:
        client = Garmin()
        client.login(str(TOKEN_DIR))
        return client
    except Exception:
        pass  # No/expired tokens: fall back to credentials
    email = os.environ.get("GARMIN_EMAIL")
    password = os.environ.get("GARMIN_PASSWORD")
    if not (email and password):
        if not sys.stdin.isatty():
            raise RuntimeError("No cached Garmin tokens; set GARMIN_EMAIL and GARMIN_PASSWORD.")
        email = input("Garmin email: ").strip()
        password = getpass("Garmin password: ")
    client = Garmin(email, password, prompt_mfa=_prompt_mfa)
    client.login(str(TOKEN_DIR))
    return client


def is_enriched(client: Garmin, activity_id) -> bool:
    """An activity is enriched if it already has exercise sets with reps."""
    sets = client.get_activity_exercise_sets(activity_id).get("exerciseSets") or []
    return any(s.get("repetitionCount") for s in sets)


def unenriched_strength_activities(client: Garmin, scan: int = 30):
    """Yield recent strength activities (newest first) that have no exercise sets yet."""
    # strength_training is a sub-type on Garmin's side, which the server rejects
    # as an activityType filter, so filter the recent activities ourselves.
    for act in client.get_activities(0, scan):
        if act.get("activityType", {}).get("typeKey") != "strength_training":
            continue
        if not is_enriched(client, act["activityId"]):
            yield act


def find_latest_unenriched(client: Garmin, include_enriched: bool = False, scan: int = 30) -> dict:
    if include_enriched:
        for act in client.get_activities(0, scan):
            if act.get("activityType", {}).get("typeKey") == "strength_training":
                return act
    else:
        for act in unenriched_strength_activities(client, scan):
            return act
    raise SystemExit(f"No unenriched strength workouts in your last {scan} activities.")


def download_original_fit(client: Garmin, activity_id) -> bytes:
    data = client.download_activity(str(activity_id), dl_fmt=Garmin.ActivityDownloadFormat.ORIGINAL)
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        name = next(n for n in z.namelist() if n.lower().endswith(".fit"))
        return z.read(name)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    client = login()
    act = find_latest_unenriched(client, include_enriched="--all-strength" in sys.argv)
    out = Path(args[0] if args else f"{act['activityId']}_ACTIVITY.fit")
    out.write_bytes(download_original_fit(client, act["activityId"]))
    print(f"{act.get('activityName')} ({act.get('startTimeLocal')}) -> {out}")


if __name__ == "__main__":
    main()
