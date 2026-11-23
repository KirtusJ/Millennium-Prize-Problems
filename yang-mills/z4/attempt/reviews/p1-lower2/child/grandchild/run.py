import numpy as np, math, os
D=os.path.dirname(os.path.abspath(__file__))
x,w=np.polynomial.legendre.leggauss(400)
if not os.path.exists(D+'/control.txt'):
    u=(x+1)/2; ww=w/2
    a=np.pi*u**2*(3-2*u); da=np.pi*(6*u-6*u**2)
    c=np.sum(ww*da*np.sqrt(2*2*np.arcsinh(np.sin(a))))
    with open(D+'/control.txt','x') as f: f.write('%.6g\n'%c)
control=open(D+'/control.txt').read().strip()
beta=256.0
t=np.pi*(x+1)/2; ww=np.pi/2*w
def I(n): return np.sum(ww*np.exp(beta*(np.cos(t)-1))*np.cos(n*t))/np.pi  # scaled by e^-beta
I0,I1,I2=I(0),I(1),I(2)
e1=I0/I1-2/beta; e2=I2/I1
rng=np.random.default_rng(12345)
acc=[];n=0;tot=0
while n<10**6:
    g=rng.gamma(1.5,1/beta,size=1200000); tot+=g.size
    ok=(g<2)&(rng.random(g.size)<np.sqrt(np.clip(1-g/2,0,None)))
    acc.append(g[ok]);n+=ok.sum()
# truncate to 1e6 in order; count draws used up to the 1e6-th acceptance
s=np.concatenate(acc)[:10**6]
cum=0;idx=None
# draws used: recompute precisely not needed; use batch rate (all draws) for acceptance
rate=n/tot
c=1-s; m=c.mean(); se=c.std(ddof=1)/math.sqrt(len(c))
exact_rate=math.pi*I1/beta/(math.gamma(1.5)*beta**-1.5)
met=abs(m-e1)<=4*se
out=f"""control integral = {control}
exact I0/I1-2/beta = {e1:.12f}
exact I2/I1        = {e2:.12f}  (diff {abs(e1-e2):.2e})
sample mean cos    = {m:.8f}  SE={se:.3e}
|mean-exact|       = {abs(m-e1):.3e} = {abs(m-e1)/se:.2f} SE (predicate <=4 SE)
acceptance rate    = {rate:.6f} (all {tot} draws incl. surplus) ; exact = {exact_rate:.6f}
verdict: {'MET' if met else 'FAILED'}
"""
print(out)
with open(D+'/result.md','x') as f:
    f.write("# Result\n\n```\n"+out+"```\n\nRerun (new dir needed since files open with 'x'; remove control.txt/result.md first):\n\n`cd /home/user/z4-workers/p1-lower2/child/grandchild && python3 run.py`\n")
