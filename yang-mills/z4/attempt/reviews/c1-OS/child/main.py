"""T7 main. Predicates fixed BEFORE first run:
P1 (hypothesis count) all 16 (x,m) cases have x/m integer (expected 16/16).
P2 methods A and B agree, rel diff < 1e-7, at x=(1,0,0,0) and x=(1/2)^4 for each m (tolerance: both quadratures
   converge to ~1e-10; 1e-7 leaves margin; B uses N=48/m grid).
P3 for each of 4 points, rel error |S_m-S|/S strictly decreases as m halves.
P4 for each point, successive error ratio err(m)/err(m/2) in [3,5] at the two smallest m (order m^2 => ~4).
   Own expectation; lattice corrections may carry log or m^2 with big constant, so failure = my expectation.
P5 rotation: |S_m(1,0,0,0)-S_m(.5^4)|/S(1) decreases with m and is < 1e-2 at m=1/16.
P6 Wick: m^-4*2G^2 rel err vs 2S^2 equals ~2*err_S (within 10% of 2*err+err^2) and decreases.
Results file mode 'x'."""
import sys, json; sys.path.insert(0,'.')
from lib import *
pts={'(1,0,0,0)':(1,0,0,0),'(.5,.5,.5,.5)':(.5,.5,.5,.5),'(1,1,0,0)':(1,1,0,0),'(2,0,0,0)':(2,0,0,0)}
ms=[.5,.25,.125,.0625]
rows=[]; ok=0; tot=0
for name,x in pts.items():
    for m in ms:
        tot+=1
        n=[v/m for v in x]
        if all(abs(v-round(v))<1e-12 for v in n): ok+=1
        else: continue
        n=tuple(int(round(v)) for v in n)
        g=GA(n,m); s=g/m**2; s0=S(x)
        row=dict(x=name,m=m,n=n,G=g,S_m=s,S=s0,rel=abs(s-s0)/s0,wick=2*g*g/m**4,wick0=2*s0**2)
        row['wick_rel']=abs(row['wick']-row['wick0'])/row['wick0']
        if name in('(1,0,0,0)','(.5,.5,.5,.5)'):
            gb=GB(n,m,N=int(48/m)); row['G_B']=gb; row['AB_rel']=abs(gb-g)/g
        rows.append(row); print(row,flush=True)
json.dump(dict(qualify=[ok,tot],rows=rows),open('results.json','x'),indent=1)
