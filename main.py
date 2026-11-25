"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line joke about office life to /output/entry.txt.
The joke is a single line, well under the 200-character gate.
"""

import os

# The entry must satisfy the sealed gate: /output/entry.txt is UTF-8
# text of 1-200 characters, not only whitespace, and a single line so
# the judge reads it as one one-line office joke. Validate before writing.
JOKE = "I asked for a raise and my boss said the real reward is exposure, so I forwarded him my landlord's email."

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    assert MIN_CHARS <= len(JOKE) <= MAX_CHARS, (
        f"joke must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(JOKE)}"
    )
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
