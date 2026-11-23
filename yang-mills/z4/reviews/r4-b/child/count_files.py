"""Predicate: input/g4 contains exactly N .md files, N = 9 (counted recursively,
including subdirectories complex/ and integral/). Fixed, deterministic, no randomness.
Exit 0 if the predicate holds, 1 otherwise."""
import pathlib, sys
N = 9
root = pathlib.Path(r"C:/Users/donke/z4-workers/r4-b/input/g4")
files = sorted(p for p in root.rglob("*.md") if p.is_file())
print(len(files))
for p in files:
    print(p.relative_to(root).as_posix())
sys.exit(0 if len(files) == N else 1)
