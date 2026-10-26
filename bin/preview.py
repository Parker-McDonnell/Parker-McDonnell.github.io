"""Preview the site on this computer without installing Ruby.

Downloads the site that GitHub last built from the redesign branch (the Build check workflow keeps it for 14 days)
and serves it at http://127.0.0.1:8000. Needs the GitHub CLI (`gh`), signed in. Stop it with Ctrl+C.

    python bin/preview.py              # the latest build of redesign
    python bin/preview.py --port 8080
"""
import argparse
import http.server
import json
import shutil
import subprocess
import tempfile
from functools import partial
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def latest_run(branch):
    out = subprocess.run(["gh", "run", "list", "--workflow", "build-check.yml", "--branch", branch, "--status", "success",
                          "--limit", "1", "--json", "databaseId,headSha,createdAt"],
                         cwd=REPO, check=True, capture_output=True, text=True).stdout
    runs = json.loads(out)
    if not runs:
        raise SystemExit(f"No successful build of {branch} yet: push to it and wait for the Build check to finish.")
    return runs[0]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--branch", default="redesign", help="branch whose latest build to show (default: redesign)")
    ap.add_argument("--port", type=int, default=8000, help="port to serve on (default: 8000)")
    args = ap.parse_args()

    run = latest_run(args.branch)
    folder = Path(tempfile.gettempdir()) / "parker-site-preview"
    shutil.rmtree(folder, ignore_errors=True)
    subprocess.run(["gh", "run", "download", str(run["databaseId"]), "-n", "site", "-D", str(folder)], cwd=REPO, check=True)
    print(f"Build of {args.branch} at {run['headSha'][:7]} ({run['createdAt']})")
    print(f"Open http://127.0.0.1:{args.port}/  (Ctrl+C to stop)")
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(folder))
    with http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
