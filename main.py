"""One-Liner Laugh Lab — make.fun bounty entry.

Writes one line (65 characters, no trailing newline) to /output/entry.txt.
Pure Python 3.13 standard library only.
"""

import hashlib
import os

# Why this line fits the judge's brief: it is the robot vacuum's excuse
# after eating a sock, in deadpan voice — it blames the victim ("The sock
# started it"), then confesses appetite with the twist "delicious".
LINE = "The sock started it. It lay there, small, defenceless, delicious."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not match the intended line exactly"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
