"""Home Assistant add-on entry point: map add-on options to environment variables,
then run tonal_to_garmin.main() every `interval_minutes`."""
import json
import os
import signal
import sys
import time
from datetime import datetime

OPTIONS_FILE = os.environ.get("OPTIONS_FILE", "/data/options.json")
stop = False


def log(msg: str) -> None:
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] [addon] {msg}", flush=True)


def load_options(path: str = OPTIONS_FILE) -> dict:
    with open(path) as f:
        return json.load(f)


def apply_options(opts: dict, env=os.environ) -> None:
    mapping = {
        "TONAL_EMAIL": "tonal_email", "TONAL_PASSWORD": "tonal_password",
        "GARMIN_EMAIL": "garmin_email", "GARMIN_PASSWORD": "garmin_password",
        "GARMIN_MFA_CODE": "garmin_mfa_code", "TONAL_LOOKBACK": "tonal_lookback",
    }
    for var, key in mapping.items():
        value = opts.get(key)
        if value not in (None, ""):
            env[var] = str(value)
    env["DATA_DIR"] = "/data"
    env["GARMIN_TOKEN_DIR"] = "/data/garmin"
    env["DRY_RUN"] = "1" if opts.get("dry_run", True) else "0"


def run_forever(run_once, interval_minutes: int, sleep=time.sleep) -> None:
    while not stop:
        try:
            rc = run_once()
            log(f"Run finished (exit code {rc}).")
        except SystemExit as e:  # e.g. a missing credential
            log(f"Run aborted: {e}")
        except Exception as e:  # keep the add-on alive; the next cycle retries
            log(f"Run failed: {type(e).__name__}: {e}")
        for _ in range(interval_minutes * 60):  # wake each second so stop requests are prompt
            if stop:
                return
            sleep(1)


def _handle_stop(signum, frame) -> None:
    global stop
    stop = True


def main() -> None:
    opts = load_options()
    apply_options(opts)
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, _handle_stop)
    import tonal_to_garmin
    mode = "DRY RUN (nothing is uploaded or deleted)" if os.environ["DRY_RUN"] == "1" else "LIVE"
    interval = int(opts.get("interval_minutes", 10))
    log(f"Starting: {mode}; checking every {interval} min.")
    sys.argv = [sys.argv[0]]  # tonal_to_garmin reads --dry-run from argv; DRY_RUN env is used instead
    run_forever(tonal_to_garmin.main, interval)
    log("Stopped.")


if __name__ == "__main__":
    main()
