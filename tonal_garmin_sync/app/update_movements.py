"""Refresh the local copy of Tonal's movement catalog and compare it to movement_map.py.

Usage: python update_movements.py [output.json]

Reads TONAL_EMAIL / TONAL_PASSWORD from the environment (or prompts), downloads
GET /v6/movements, and writes a trimmed catalog (default tonal_movements.json).
Then prints which movements have no Garmin mapping yet, grouped by family, and
any disagreement between Tonal's accessory data and BARBELL_MOVEMENTS.
"""
import json
import os
import sys
from collections import defaultdict
from getpass import getpass

import requests

from movement_map import BARBELL_MOVEMENTS, MOVEMENT_MAP
from sync_workouts import API_BASE, authenticate

KEEP = ["id", "name", "shortName", "family", "bodyRegion", "muscleGroups", "pushPull",
        "baseOfSupport", "isBilateral", "isAlternating", "isTwoSided", "inFreeLift",
        "onMachine", "customMovement", "hiddenInMovePicker"]


def fetch_catalog() -> list:
    email = os.environ.get("TONAL_EMAIL") or input("Tonal email: ").strip()
    password = os.environ.get("TONAL_PASSWORD") or getpass("Tonal password: ")
    token = authenticate(email, password)["id_token"]
    r = requests.get(f"{API_BASE}/v6/movements", headers={"Authorization": f"Bearer {token}"}, timeout=60)
    r.raise_for_status()
    return r.json()


def trim(m: dict) -> dict:
    out = {k: m.get(k) for k in KEEP}
    info = m.get("onMachineInfo") or {}
    out["accessory"] = info.get("accessory")
    out["resistanceType"] = info.get("resistanceType")
    return out


def main() -> None:
    if any(a in ("-h", "--help") for a in sys.argv[1:]):
        print(__doc__)
        return
    out_path = sys.argv[1] if len(sys.argv) > 1 else "tonal_movements.json"
    catalog = sorted((trim(m) for m in fetch_catalog()), key=lambda m: m["name"] or "")
    with open(out_path, "w") as f:
        json.dump(catalog, f, indent=1)
    print(f"\nSaved {len(catalog)} movements to {out_path}")

    by_id = {m["id"]: m for m in catalog}
    unmapped = [m for m in catalog if m["id"] not in MOVEMENT_MAP]
    print(f"{len(MOVEMENT_MAP)} mapped, {len(unmapped)} unmapped, "
          f"{sum(1 for k in MOVEMENT_MAP if k not in by_id)} mapped IDs missing from the catalog")

    groups = defaultdict(list)
    for m in unmapped:
        groups[m["family"] or "(none)"].append(m)
    for family, items in sorted(groups.items()):
        print(f"\n== {family} ({len(items)})")
        for m in items:
            flags = "".join(c for c, on in (("B", m["isBilateral"]), ("A", m["isAlternating"]),
                                            ("2", m["isTwoSided"])) if on)
            print(f"  {m['id']}  {m['name']:<45} {m['accessory'] or '-':<12} {flags}")

    print("\n== Barbell check (accessory == StraightBar vs BARBELL_MOVEMENTS)")
    bar_by_accessory = {m["id"] for m in catalog if m["accessory"] == "StraightBar"}
    for i in sorted(bar_by_accessory - BARBELL_MOVEMENTS):
        print(f"  StraightBar but not in BARBELL_MOVEMENTS: {by_id[i]['name']} ({i})")
    for i in sorted(BARBELL_MOVEMENTS - bar_by_accessory):
        print(f"  In BARBELL_MOVEMENTS but accessory is {by_id.get(i, {}).get('accessory')!r}: "
              f"{by_id.get(i, {}).get('name')} ({i})")


if __name__ == "__main__":
    main()
