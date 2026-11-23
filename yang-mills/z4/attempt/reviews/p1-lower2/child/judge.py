"""Evaluates P3,P4,P5 from results.csv per mc.py docstring; writes judge.txt (mode x)."""
import numpy as np
d=np.genfromtxt('results.csv',delimiter=',',names=True)
L=[]
ess=d['ESS']>=1000; L.append(f"P5 ESS>=1000: met {ess.sum()}/36 (min ESS {d['ESS'].min():.0f})")
p3=np.abs(d['diff'])<=5*d['SE']+2/np.sqrt(d['beta']); L.append(f"P3 |diff|<=5SE+2/sqrt(b): met {p3.sum()}/36 failed {(~p3).sum()}")
for i in np.where(~p3)[0]: L.append("  P3 FAIL "+str(d[i]))
m={}
for b in (256,1024,4096):
    s=d['beta']==b; m[b]=np.abs(d['sqrtb_diff'][s]).max(); L.append(f"beta={b}: worst|diff|={np.abs(d['diff'][s]).max():.5f}  max sqrt(b)|diff|={m[b]:.3f}  max SE={d['SE'][s].max():.4f}")
p4=m[4096]<=1.5*m[256]+3*(d['SE'][d['beta']==4096].max()*64); L.append(f"P4 bounded: {m[4096]:.3f} <= 1.5*{m[256]:.3f}+slack -> met={p4}")
open('judge.txt','x').write("\n".join(L)+"\n"); print("\n".join(L))
