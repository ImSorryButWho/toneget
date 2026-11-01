# Tonal to Garmin Sync

Every few minutes this add-on looks for a Garmin strength workout that has no exercise
sets yet, finds the matching Tonal workout, builds a combined FIT file (sets, reps,
weights and rest from Tonal; heart rate and the rest from your watch), uploads it to
Garmin Connect, and then deletes the original. The original is backed up first.
The new activity is named like the Tonal app shows it, e.g. "Modern Muscle - Workout 20".

## Setup

1. Fill in your Tonal and Garmin credentials in the add-on configuration.
2. Leave **Dry run** on for the first run. The add-on then builds the combined file and
   logs what it would do, but uploads and deletes nothing. Check the log, then turn
   Dry run off.
3. Start the add-on and watch the **Log** tab.

### Garmin accounts with two-step verification (MFA)

Garmin asks for a code at login, which an unattended add-on can't type. Either:

- Start the add-on, wait for Garmin to send you a code, put it in **Garmin MFA code**
  and restart within a few minutes. Login tokens are then cached in `/data/garmin`
  and later runs don't need a code until they expire; or
- Open a shell in the container (`docker exec -it addon_<repo>_tonal_garmin_sync sh`)
  and run `python /app/fetch_garmin.py` once, entering the code when prompted.

## Options

| Option | Meaning |
|---|---|
| `interval_minutes` | How often to check (5 to 1440). Each check is one Garmin request when nothing is pending; Tonal is only contacted when a Garmin workout needs enriching. |
| `tonal_lookback` | How many recent Tonal workouts to consider as matches (default 5). |
| `dry_run` | Build files and log, but never upload or delete. |

## Where things are

Everything lives in the add-on's `/data` folder: `backups/` (original Garmin FIT files
and the matching Tonal JSON; keep these as long as you like), `combined/` (generated
files), `garmin/` (login tokens), `state.json`, and `movements_cache.json`.

## If something goes wrong

- If an upload can't be confirmed, the original is **not** deleted and the next cycle retries.
- If a Garmin workout is deleted before its replacement is confirmed, the log names the
  backup file to restore by uploading it in Garmin Connect (Import Data).
- Movements without a Garmin mapping are logged by name. Their sets are still included,
  just without an exercise type.
