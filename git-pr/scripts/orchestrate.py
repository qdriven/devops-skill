#!/usr/bin/env python3
"""Git PR helpers — create / merge / status via gh CLI.

Usage:
    python3 orchestrate.py create --title "..." --body "..." [--base main] [--draft]
    python3 orchestrate.py merge [--pr N] [--method squash|merge|rebase] [--delete-branch]
    python3 orchestrate.py status [--pr N]
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

STATE_FILE = Path(".git-pr.state.json")


def run(cmd: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, check=check)


def run_gh(args: list[str], check: bool = True) -> subprocess.CompletedProcess:
    return run(["gh"] + args, check=check)


def die(msg: str, code: int = 1) -> None:
    print(f"Error: {msg}", file=sys.stderr)
    sys.exit(code)


def current_branch() -> str:
    r = run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    return r.stdout.strip()


def detect_base(preferred: str | None) -> str:
    if preferred:
        return preferred
    for name in ("main", "master"):
        r = run(["git", "rev-parse", "--verify", f"origin/{name}"], check=False)
        if r.returncode == 0:
            return name
        r = run(["git", "rev-parse", "--verify", name], check=False)
        if r.returncode == 0:
            return name
    die("Could not detect base branch; pass --base")


def save_state(data: dict) -> None:
    STATE_FILE.write_text(json.dumps(data, indent=2) + "\n")


def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def resolve_pr(pr: int | None) -> int:
    if pr:
        return pr
    state = load_state()
    if state.get("pr"):
        return int(state["pr"])
    r = run_gh(["pr", "view", "--json", "number", "-q", ".number"], check=False)
    if r.returncode == 0 and r.stdout.strip().isdigit():
        return int(r.stdout.strip())
    die("No PR specified; pass --pr or run create first / stand on a PR branch")


def cmd_create(args: argparse.Namespace) -> None:
    branch = current_branch()
    if branch in ("main", "master"):
        die(f"Refusing to open a PR from '{branch}'")

    base = detect_base(args.base)

    # Push current branch
    push = run(["git", "push", "-u", "origin", "HEAD"], check=False)
    if push.returncode != 0:
        die(f"git push failed:\n{push.stderr or push.stdout}")

    # Already has PR?
    existing = run_gh(
        ["pr", "view", "--json", "url,number,state", "-q", ".url + \"|\" + (.number|tostring) + \"|\" + .state"],
        check=False,
    )
    if existing.returncode == 0 and existing.stdout.strip():
        url, number, state = existing.stdout.strip().split("|", 2)
        print(f"PR already exists: {url} (#{number}, {state})")
        save_state({"pr": int(number), "url": url, "branch": branch, "base": base})
        return

    create_args = [
        "pr", "create",
        "--base", base,
        "--title", args.title,
        "--body", args.body,
    ]
    if args.draft:
        create_args.append("--draft")
    if args.repo:
        create_args.extend(["--repo", args.repo])

    result = run_gh(create_args, check=False)
    if result.returncode != 0:
        die(f"gh pr create failed:\n{result.stderr or result.stdout}")

    url = result.stdout.strip().splitlines()[-1]
    # Resolve number
    view = run_gh(["pr", "view", url, "--json", "number", "-q", ".number"])
    number = int(view.stdout.strip())
    save_state({"pr": number, "url": url, "branch": branch, "base": base})
    print(f"PR created: {url}")
    print(f"State saved to: {STATE_FILE}")


def cmd_merge(args: argparse.Namespace) -> None:
    number = resolve_pr(args.pr)
    method = args.method
    if method not in ("squash", "merge", "rebase"):
        die("--method must be squash|merge|rebase")

    # Guardrails
    view = run_gh(
        ["pr", "view", str(number), "--json", "url,state,mergeable,mergeStateStatus,baseRefName,headRefName,title"],
        check=False,
    )
    if view.returncode != 0:
        die(f"gh pr view failed:\n{view.stderr or view.stdout}")
    info = json.loads(view.stdout)
    if info.get("state") != "OPEN":
        die(f"PR #{number} is {info.get('state')}, not OPEN ({info.get('url')})")
    if info.get("mergeable") == "CONFLICTING":
        die(f"PR #{number} has conflicts; resolve before merge")

    delete_branch = not bool(getattr(args, "keep_branch", False))
    merge_args = ["pr", "merge", str(number), f"--{method}"]
    if delete_branch:
        merge_args.append("--delete-branch")
    if args.admin:
        merge_args.append("--admin")

    result = run_gh(merge_args, check=False)
    if result.returncode != 0:
        die(f"gh pr merge failed:\n{result.stderr or result.stdout}")

    # Confirm
    after = run_gh(["pr", "view", str(number), "--json", "url,state,mergedAt"], check=False)
    if after.returncode == 0:
        data = json.loads(after.stdout)
        print(f"PR merged: {data.get('url')} ({data.get('state')}, at {data.get('mergedAt')})")
    else:
        print(f"PR #{number} merge requested.")

    if STATE_FILE.exists():
        state = load_state()
        state["merged"] = True
        save_state(state)


def cmd_status(args: argparse.Namespace) -> None:
    number = resolve_pr(args.pr) if (args.pr or STATE_FILE.exists()) else None
    if number is None:
        # try current branch PR
        r = run_gh(["pr", "view", "--json", "number,url,state,mergeable,mergeStateStatus,title"], check=False)
        if r.returncode != 0:
            die("No PR on current branch; pass --pr")
        info = json.loads(r.stdout)
    else:
        r = run_gh(
            ["pr", "view", str(number), "--json", "number,url,state,mergeable,mergeStateStatus,title"],
            check=False,
        )
        if r.returncode != 0:
            die(r.stderr or r.stdout)
        info = json.loads(r.stdout)

    print(json.dumps(info, indent=2))
    checks = run_gh(["pr", "checks", str(info["number"])], check=False)
    if checks.returncode == 0 and checks.stdout.strip():
        print("\nChecks:")
        print(checks.stdout.rstrip())
    elif checks.stderr.strip():
        print(f"\nChecks: {checks.stderr.strip()}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Git PR orchestrator (create / merge / status)")
    sub = p.add_subparsers(dest="command", required=True)

    c = sub.add_parser("create", help="Push branch and create PR")
    c.add_argument("--title", required=True)
    c.add_argument("--body", required=True)
    c.add_argument("--base", default=None, help="Base branch (default: main/master)")
    c.add_argument("--draft", action="store_true")
    c.add_argument("--repo", default=None)
    c.set_defaults(func=cmd_create)

    m = sub.add_parser("merge", help="Merge an open PR")
    m.add_argument("--pr", type=int, default=None)
    m.add_argument("--method", choices=["squash", "merge", "rebase"], default="squash")
    m.add_argument(
        "--keep-branch",
        action="store_true",
        help="Keep the head branch after merge (default: delete remote head branch)",
    )
    m.add_argument("--admin", action="store_true", help="gh --admin (bypass if permitted)")
    m.set_defaults(func=cmd_merge, delete_branch=True)

    s = sub.add_parser("status", help="Show PR mergeability and checks")
    s.add_argument("--pr", type=int, default=None)
    s.set_defaults(func=cmd_status)

    return p


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
