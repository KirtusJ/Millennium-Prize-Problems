"""Evaluate predicates P1-P6 (defined in main.py docstring) on results.json. Output predicates.txt (mode x). Always exit 0."""
import json,numpy as np
R=json.load(open('results.json')); rows=R['rows']; out=[]
def P(k,ok,msg): out.append(f"{k}: {'MET' if ok else 'FAILED'} - {msg}")
P('P1',R['qualify']==[16,16],f"{R['qualify'][0]}/{R['qualify'][1]} cases have x/m integer")
ab=[r['AB_rel'] for r in rows if 'AB_rel' in r]; P('P2',max(ab)<1e-7,f"max A-vs-B rel diff {max(ab):.2e} over {len(ab)} cases")
by={}
for r in rows: by.setdefault(r['x'],[]).append(r)
for x,L in by.items():
    e=[r['rel'] for r in L]
    P('P3 '+x,all(e[i+1]<e[i] for i in range(3)),"errors "+", ".join("%.3e"%v for v in e))
    rt=[e[i]/e[i+1] for i in range(3)]
    P('P4 '+x,all(3<=v<=5 for v in rt[1:]),"ratios err(m)/err(m/2): "+", ".join("%.2f"%v for v in rt))
a=[r['S_m'] for r in by['(1,0,0,0)']]; b=[r['S_m'] for r in by['(.5,.5,.5,.5)']]; s0=by['(1,0,0,0)'][0]['S']
d=[abs(u-v)/s0 for u,v in zip(a,b)]
P('P5',all(d[i+1]<d[i] for i in range(3)) and d[-1]<1e-2,"rotation diff "+", ".join("%.3e"%v for v in d)+f"; ratios {[round(d[i]/d[i+1],2) for i in range(3)]}")
for x,L in by.items():
    w=[r['wick_rel'] for r in L]; e=[r['rel'] for r in L]
    P('P6 '+x,all(abs(wi-(2*ei))<0.1*2*ei+ei*ei+1e-12 for wi,ei in zip(w[2:],e[2:])) and w[3]<w[0],"wick rel "+", ".join("%.3e"%v for v in w))
open('predicates.txt','x').write("\n".join(out)+"\n"); print("\n".join(out))
