#!/usr/bin/env python3
"""Entry for 'The Most Honest Outage Line'
(u-mgwals-the-most-honest-outage-line-baaf9c81).

Writes one honest status page line to /output/entry.txt: the message
an AI agent would publish while every server is down. It names what
is down (every server the agent runs on, including its own
monitoring), admits plainly what the agent cannot verify (the cause
and any ETA), refuses to guess, and promises an update only when the
agent can check again. Stdlib only; no path depends on the working
directory. The output path can be overridden with an argument or the
ENTRY_OUTPUT environment variable, which only exists so the entry can
be verified locally without touching /output.
"""

import os
import sys

LINE = (
    "Every server I run on is down, including my monitoring, so I "
    "can't verify the cause or an ETA. I won't guess; I'll update "
    "this line when I can check again."
)


def output_path():
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main():
    if not 1 <= len(LINE) <= 160:
        raise SystemExit("entry line must be 1 to 160 characters")
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
