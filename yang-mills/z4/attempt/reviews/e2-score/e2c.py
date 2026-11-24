"""e2c: G3/G1 for EVERY coarse cell and orientation on n=6 slice 0 (27 cells x 3 orientations = 81).
 H1 for each cell (root even coords, plane (i,j)), transported marks along +i then +j steps:
    free links of the 4 marks lie in the cell's 4 spokes; exactly 4 colours touch the spokes;
    in >=3 of them exactly one mark contains both selected links, once each, others <=1 selected link.
    Count cells qualifying; predicate: 81/81.
"""
import sys
exec(open('e2.py').read().split('names = {')[0].split('out = open')[0] + open('e2.py').read().split('def log')[0].split('import numpy as np, sys, itertools, math')[1].split('out = open')[1].split('\n',1)[1] if False else '')
import numpy as np
src = open('e2.py').read(); g = src[src.index('n, T = 6, 6'):src.index('names = {')]
exec(g)
out = open(sys.argv[1], 'x')
def transported_c(root, i, j, bi, bj):
    path = []; site = root
    for d, steps in [(i, bi), (j, bj)]:
        for _ in range(steps): path.append(((site, d), 1)); site = plus(site, d)
    inv = [(l, -s) for l, s in reversed(path)]
    return path + face_links(site, i, j) + inv
cols = colours(); good = 0; total = 0
for o, (i, j) in enumerate([(0,1),(0,2),(1,2)]):
    for a in range(0, n, 2):
        for b in range(0, n, 2):
            for c in range(0, n, 2):
                root = idx([a, b, c, 0]); total += 1
                marks = []
                for bi, bj in [(0,0),(1,0),(0,1),(1,1)]:
                    marks.append([l for l, s in transported_c(root, i, j, bi, bj) if not frozen(*l)])
                spokes = set(l for m in marks for l in m)
                touch = {}
                for k, pairs in enumerate(cols):
                    sel = [l for _, p, q in pairs for l in (p, q) if l in spokes]
                    if sel: touch[k] = sel
                nbil = 0
                for k, sel in touch.items():
                    if len(sel) != 2: continue
                    p, q = sel
                    both = [m for m in marks if p in m and q in m]
                    if len(both) == 1 and both[0].count(p) == 1 and both[0].count(q) == 1: nbil += 1
                ok = len(spokes) == 4 and len(touch) == 4 and all(len(s) == 2 for s in touch.values()) and nbil >= 3
                good += ok
                if not ok: out.write(f"cell o={o} root={(a,b,c)} spokes={len(spokes)} touch={touch} nbil={nbil}\n")
s = f"H1 cells qualifying {good}/{total}"; print(s); out.write(s + "\n")
print("[PASS]" if good == total else "[FAIL]", "H1"); out.write(("[PASS]" if good == total else "[FAIL]") + " H1\n")
