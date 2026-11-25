"""The Funniest Honest Appliance Error — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt:
the funniest honest error message an appliance could show.
"""

import os

LINE = "ERROR: I lost Wi-Fi. I am a washing machine. I do not know why I needed Wi-Fi either."


def main() -> None:
    # The gate allows 1-200 characters; fail loudly instead of
    # ever writing an over-long or empty line.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars"
    assert LINE.strip() and "\n" not in LINE, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
