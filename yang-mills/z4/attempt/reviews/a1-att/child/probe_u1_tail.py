"""Probe: U(1) d=4 order A, long-run tail of c_1(n): is it a fixed point (change ~0) or slow drift?
Predicate (fixed before run): for beta0 in {1,2,4,8}, report c1 at n=100,400,1600,6400; 'fixed point' if
|c1(6400)-c1(1600)| < 1e-6, else 'drifting' (tolerance: 1e-6 >> rounding 1e-15 per step * 5000 steps)."""
import sys; sys.path.insert(0,'.')
import mk_recursion as m, json
out={}
for b0 in (1,2,4,8):
    f=m.u1_wilson(b0,4096); tr=[]
    for n in range(6401):
        tr.append(m.u1_coef(f)[1]); f=m.u1_step(f,4,'A')
    v={n:tr[n] for n in (100,400,1600,6400)}
    drift=abs(tr[6400]-tr[1600]); out[b0]=dict(v=v,drift=drift,verdict='fixed point' if drift<1e-6 else 'drifting')
    print(b0,v,drift,out[b0]['verdict'])
with open('result_tail.json','x') as fh: json.dump(out,fh,indent=1)
