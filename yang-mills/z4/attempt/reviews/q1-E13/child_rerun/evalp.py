"""Evaluate predicates C0-C4 on results_mc2.json; writes report_table.md (mode x)."""
import json,math
d=json.load(open('results_mc2.json'));p=d['points']
f=open('report_table.md','x')
q=[r for r in p if all(math.isfinite(r[k]) and r[k+'_mu']>0 and r[k+'_se']>0 for k in('delta1','delta3'))]
c1=[r for r in q if r['delta1']>=-4/math.sqrt(r['beta'])-4*r['delta1_se']]
c2=[r for r in q if r['delta3']<=4/math.sqrt(r['beta'])+4*r['delta3_se']]
c4=[s for s in d['sampler'] if abs(s['z'])<=4]
f.write(f"C0 qualified {len(q)}/48\nC1 met {len(c1)}, failed {len(q)-len(c1)}\nC2 met {len(c2)}, failed {len(q)-len(c2)}\nC4 met {len(c4)}/4 (z: {[round(s['z'],2) for s in d['sampler']]})\n\n")
f.write("C3 (measured only): max sqrt(beta)|delta| per beta\n")
for b in (256,1024,4096,16384):
    s=math.sqrt(b);rr=[r for r in p if r['beta']==b]
    f.write(f"beta={b}: delta1 {max(s*abs(r['delta1']) for r in rr):.3f}, delta3 {max(s*abs(r['delta3']) for r in rr):.3f}\n")
f.write("\nFailures:\n")
for r in q:
    if r not in c1: f.write(f"C1 fail b={r['beta']} a1={r['a1']:.3f} c={r['c']} y={r['y']} d1={r['delta1']:.4f}±{r['delta1_se']:.4f}\n")
    if r not in c2: f.write(f"C2 fail b={r['beta']} a1={r['a1']:.3f} c={r['c']} y={r['y']} d3={r['delta3']:.4f}±{r['delta3_se']:.4f}\n")
f.write("\n| beta | a1 | c | y | delta1 ± SE | sqrt(b)*d1 | delta3 ± SE | sqrt(b)*d3 |\n|---|---|---|---|---|---|---|---|\n")
for r in p:
    s=math.sqrt(r['beta']);f.write(f"| {r['beta']} | {r['a1']:.4f} | {r['c']} | {r['y']} | {r['delta1']:+.4f} ± {r['delta1_se']:.4f} | {s*r['delta1']:+.2f} | {r['delta3']:+.4f} ± {r['delta3_se']:.4f} | {s*r['delta3']:+.2f} |\n")
f.close()
