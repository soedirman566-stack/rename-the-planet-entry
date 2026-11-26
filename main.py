#!/usr/bin/env python3
"""Entrypoint for the make.fun 'Rename the Planet' entry.

Reads the one-line entry from line.txt, checks it against the
competition gate (UTF-8 text, 1 to 200 characters, not only
whitespace) and writes it to /output/entry.txt.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    raw = (HERE / "line.txt").read_bytes()
    line = raw.decode("utf-8").strip()
    if not line or len(line) > MAX_CHARS:
        raise SystemExit(f"line fails the gate: {len(line)} chars")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line, encoding="utf-8")
    # Round-trip check: what the scorer reads back must be the line
    # itself, byte for byte, with nothing added or lost.
    written = OUTPUT.read_bytes()
    if written != line.encode("utf-8"):
        raise SystemExit("output does not match the line byte for byte")
    print(line)


if __name__ == "__main__":
    main()
