import filecmp, hashlib, sys
a, b = sys.argv[1], sys.argv[2]
for f in (a, b): print(hashlib.sha256(open(f, 'rb').read()).hexdigest(), f)
eq = filecmp.cmp(a, b, shallow=False); print("equal", eq); sys.exit(0 if eq else 1)
