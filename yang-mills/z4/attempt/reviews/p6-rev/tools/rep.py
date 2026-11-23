"""rep.py FILE EDITS.py -- apply exact (old,new[,count]) replacements; each old must occur exactly `count` times (default 1). Aborts without writing on any mismatch."""
import sys, runpy
f = sys.argv[1]; edits = runpy.run_path(sys.argv[2])['E']
s = open(f).read()
for e in edits:
    old, new = e[0], e[1]; cnt = e[2] if len(e) > 2 else 1
    n = s.count(old)
    if n != cnt:
        sys.exit(f"ABORT: {n} occurrences (expected {cnt}) of: {old[:90]!r}")
    s = s.replace(old, new)
open(f, 'w').write(s); print(f"{f}: {len(edits)} edits applied")
