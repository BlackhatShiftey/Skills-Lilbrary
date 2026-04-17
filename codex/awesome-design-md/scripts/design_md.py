#!/usr/bin/env python3
"""List and install DESIGN.md inspirations via the getdesign CLI."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys


def resolve_npx() -> str:
    return shutil.which("npx.cmd") or shutil.which("npx") or ""


def safe_write(text: str, is_error: bool = False) -> None:
    stream = sys.stderr if is_error else sys.stdout
    encoding = stream.encoding or "utf-8"
    stream.write(text.encode(encoding, errors="replace").decode(encoding))


def run(cmd: list[str]) -> int:
    proc = subprocess.run(
        cmd,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.stdout:
        safe_write(proc.stdout)
    if proc.stderr:
        safe_write(proc.stderr, is_error=True)
    return proc.returncode


def ensure_npx() -> None:
    if resolve_npx():
        return
    raise SystemExit("npx is required. Install Node.js/npm first.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Work with the getdesign CLI from a Codex skill."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List available design inspirations")

    add_parser = subparsers.add_parser("add", help="Install a DESIGN.md by brand")
    add_parser.add_argument("brand", help="Brand slug, such as vercel or stripe")
    add_parser.add_argument("--out", help="Optional output path for DESIGN.md")
    add_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite the active DESIGN.md when supported by getdesign",
    )

    args = parser.parse_args()
    ensure_npx()

    cmd = [resolve_npx(), "getdesign@latest", args.command]
    if args.command == "add":
        cmd.append(args.brand)
        if args.force:
            cmd.append("--force")
        if args.out:
            cmd.extend(["--out", args.out])

    return run(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
