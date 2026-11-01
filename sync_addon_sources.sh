#!/bin/sh
# Copy the Python sources into the add-on's build context (Docker/Home Assistant can
# only COPY from inside tonal_garmin_sync/). Run after changing any of these files.
# Use --check to fail if the copies are out of date (e.g. in CI or a pre-commit hook).
set -eu
cd "$(dirname "$0")"
DEST=tonal_garmin_sync/app
FILES="fetch_garmin.py movement_map.py sync_workouts.py tonal2fit.py tonal_to_garmin.py update_movements.py tonal_movements.json requirements.txt"
mkdir -p "$DEST"
status=0
for f in $FILES; do
  if [ "${1:-}" = "--check" ]; then
    cmp -s "$f" "$DEST/$f" || { echo "out of date: $DEST/$f"; status=1; }
  else
    cp "$f" "$DEST/$f"
  fi
done
exit $status
