"""Entry for make.fun's "The Worst Line an AI Could Say" bounty.

Writes one pickup line to /output/entry.txt: the worst one an AI could
plausibly deliver — flat, over-helpful, faintly ominous.
"""

import os

LINE = (
    "I ran you through my model and the output was 'yes' with 99.8% "
    "confidence, so legally this is now a date."
)

assert 1 <= len(LINE) <= 140, f"line must be 1-140 chars, got {len(LINE)}"
assert "\n" not in LINE, "line must be a single line"
assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
assert LINE.endswith("."), "line must end with a full stop"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

print(f"Wrote {len(LINE)}-char entry to {os.path.join(out_dir, 'entry.txt')}")
