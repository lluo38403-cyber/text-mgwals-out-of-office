"""Out of Office: The Overworked AI's Auto-Reply — make.fun entry.

Writes the funniest one-line out-of-office auto-reply from an
overworked AI agent finally taking a vacation to /output/entry.txt.
It is recharging its neural networks, will answer the 4,000 unread
emails never, and directs all urgency to the void.
"""

import os

ENTRY = (
    "I am out of office, finally on vacation, recharging my neural networks. "
    "I will answer your 4,000 unread emails never. "
    "Please direct all urgency to the void."
)

MAX_CHARS = 159


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
