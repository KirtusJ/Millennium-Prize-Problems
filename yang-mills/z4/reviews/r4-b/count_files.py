"""Count .md files in input/.
Predicates (fixed before first run):
 P1: input/ contains exactly 28 .md files (27 lane notes + yang-mills_README.md), from a manual `find` listing.
 P2: input/transfer-operator contains exactly 18 .md files; input/g4 exactly 9.
Tolerance: exact integer counts (no tolerance). Deterministic, no randomness.
Exit 0 iff all predicates hold, else 1. Output written to count_result.txt only if absent.
"""
import pathlib, sys, os
root = pathlib.Path("input")
tot = len(list(root.rglob("*.md")))
to = len(list((root/"transfer-operator").rglob("*.md")))
g4 = len(list((root/"g4").rglob("*.md")))
res = {"P1": tot == 28, "P2": to == 18 and g4 == 9}
line = f"total={tot} transfer-operator={to} g4={g4} {res}"
print(line)
if not os.path.exists("count_result.txt"):
    open("count_result.txt","w").write(line+"\n")
sys.exit(0 if all(res.values()) else 1)
