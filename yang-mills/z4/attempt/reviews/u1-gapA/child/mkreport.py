import json,sys,re
r=json.load(open('results.json'))
rows=[]
import collections
g=collections.OrderedDict()
for k,v in r.items():
    if not isinstance(v,dict): continue
    item=k.split(' ')[0]
    g.setdefault(item,[]).append(v)
out=["| item | cases | grid points | met | failed | worst margin (measured) |","|---|---|---|---|---|---|"]
for it,vs in g.items():
    out.append(f"| {it} | {len(vs)} | {sum(v['n'] for v in vs)} | {sum(v['met'] for v in vs)} | {sum(v['failed'] for v in vs)} | {min(v['worst'] for v in vs):.3e} |")
open('table.md','x').write("\n".join(out)+"\n")
print("\n".join(out))
