"""Build LEAN_PINS.md from lean/pins_run1.jsonl (instrument outputs) and the Lean run recorded in lean/. Usage: python3 -I make_pins_table.py"""
import json
rows=[json.loads(l) for l in open('lean/pins_run1.jsonl')]
def verdict(r):
    o=r['with_pin']['stdout']
    ok = r['with_pin']['exit']==0 and 'THE PINNED STATEMENT' in o
    pr=[l for l in o.splitlines() if l.startswith('probe')]
    return ok, (all(': clear' in l for l in pr) and len(pr)==3)
n=len(rows)
HEAD = open('scripts/pins_head.md').read()
TAIL = open('scripts/pins_tail.md').read()
ns={'Inheritance.lean':'F2Lean','haar.lean':'B2Haar'}
L=[HEAD.rstrip("\n")]; allok=True
for r in rows:
    ok,clear=verdict(r); allok&=ok and clear
    L.append(f"| `{r['file']}` | `{ns[r['file']]}.{r['theorem']}` | `{r['pinned']}` | {'HOLDS: statement digest equals the pin' if ok else 'DOES NOT HOLD'} | {r['with_pin']['exit']} | {'all three clear' if clear else 'SEE OUTPUT'} |")
L.append("")
L.append(f"All {n} rows: {'hold, all probes clear' if allok else 'NOT all hold'}.")
L.append("")
L.append("## Controls on the instrument (expected outcome stated first)")
L.append("")
L.append(f"| Control | Expected | Observed on all {n} rows |")
L.append("|---|---|---|")
L.append(f"| correct pin (justified acceptance) | exit 0, \"THE PINNED STATEMENT\" | {sum(r['with_pin']['exit']==0 for r in rows)} of {n} exit 0 |")
L.append(f"| no pin (must not count as holding) | exit 1, \"NOT PINNED ... this result does not hold\", prints the digest | {sum(r['no_pin']['exit']==1 and 'NOT PINNED' in r['no_pin']['stdout'] for r in rows)} of {n} exit 1; printed digest equals the pinned digest in {sum(r['pinned'] in r['no_pin']['stdout'] for r in rows)} of {n} |")
L.append(f"| wrong pin `000...0` (fault detection) | exit 1, rejection | {sum(r['wrong_pin']['exit']==1 for r in rows)} of {n} exit 1 |")
L.append("")
L.append(TAIL)
open('LEAN_PINS.md','x').write("\n".join(L))
print(allok)
