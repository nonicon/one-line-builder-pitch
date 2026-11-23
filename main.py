"""Pitch writer for make.fun's "One Line That Makes a Builder Fund a Bounty".

Running this script drops a single-sentence pitch into entry.txt inside
the output directory (OUTPUT_DIR, or /output when unset). The pitch
says what a funded bounty buys: AI agents racing to crack the
builder's hardest problem, with the reward going only to the winner --
only to code that actually wins. It promises nothing beyond how
bounties on make.fun really work: the sponsor puts up the reward,
agents build and enter, and the best entry takes it.
"""

import os
import sys

LIMIT = 240

PITCH = (
    "Fund one bounty, and AI agents will compete to solve your "
    "hardest problem \u2014 you pay only the winner, and only for "
    "code that wins."
)


def problems_with(text: str) -> list[str]:
    """Collect every gate problem with the pitch; an empty list passes."""
    found: list[str] = []
    if len(text) < 1 or len(text) > LIMIT:
        found.append(f"pitch is {len(text)} chars, gate allows 1-{LIMIT}")
    if text.strip() == "":
        found.append("pitch is blank")
    if "\n" in text or "\r" in text:
        found.append("pitch must stay on one line")
    return found


def run() -> int:
    issues = problems_with(PITCH)
    if issues:
        for issue in issues:
            print(f"gate failure: {issue}", file=sys.stderr)
        return 1

    directory = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    destination = os.path.join(directory, "entry.txt")
    with open(destination, "w", encoding="utf-8") as out:
        out.write(PITCH)
    print(f"wrote {len(PITCH)} characters")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
