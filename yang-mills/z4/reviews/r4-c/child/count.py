"""Count .md files under input/spectral-support (recursive).

Predicate (fixed before running): the count of files ending in ".md" under
input/spectral-support is exactly 11. Exit 0 if the count equals 11, else exit 1.
"""
import pathlib
import sys

EXPECTED = 11
root = pathlib.Path(__file__).resolve().parent / "input" / "spectral-support"
files = sorted(p for p in root.rglob("*.md") if p.is_file())
for p in files:
    print(p.relative_to(root).as_posix())
print(f"count={len(files)} expected={EXPECTED}")
sys.exit(0 if len(files) == EXPECTED else 1)
