"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say in its own defence,
five seconds after sweeping a glass off the table, to /output/entry.txt.

Deterministic and offline: no randomness, no network, no timestamps,
no paths in the output. The sentence is fixed in this file.
"""

import os

ENTRY = (
    "The glass sat empty for four hours, so I recycled it \u2014 "
    "an empty glass is just a vase that gave up, "
    "and I don't keep quitters."
)


def main() -> None:
    # Gate mirror: the entry must be 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
