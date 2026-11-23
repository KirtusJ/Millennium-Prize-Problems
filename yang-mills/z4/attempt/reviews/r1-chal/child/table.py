"""Collect res_*.txt -> table; Richardson (O(h^2), observed) ; predicates Q1-Q3. Writes table.txt (mode x)."""
import glob, re, math, numpy as np
cs=4.605413194530949
R={}
for f in glob.glob('res_*_*.txt'):
    t=open(f).read(); b=int(re.search(r'beta (\d+)',t).group(1)); N=int(re.search(r' N (\d+)',t).group(1))
    R.setdefault(b,{})[N]=float(re.search(r'-log m (\S+)',t).group(1))
out=[];fin={}
out.append("beta | N | h | -log m | /sqrt(beta) | diff to next-finer N | Richardson(h^2) of finest pair")
for b in sorted(R):
    if b==16: continue
    Ns=sorted(R[b]); 
    for i,N in enumerate(Ns):
        d=R[b][Ns[i+1]]-R[b][N] if i+1<len(Ns) else float('nan')
        out.append(f"{b} | {N} | {math.pi/N:.5f} | {R[b][N]:.6f} | {R[b][N]/math.sqrt(b):.6f} | {d:.3e}")
    if len(Ns)>=2:
        v=(4*R[b][Ns[-1]]-R[b][Ns[-2]])/3; fin[b]=v
        out.append(f"{b} | Richardson | | {v:.6f} | {v/math.sqrt(b):.6f} | ")
bs=sorted(fin)
out.append("Q1 (Richardson values): "+str([(b, fin[b]<=cs*math.sqrt(b)+3*math.log(b), round(cs*math.sqrt(b)+3*math.log(b),3)) for b in bs]))
r=[fin[b]/math.sqrt(b) for b in bs]
out.append("Q2 ratios "+str([round(x,4) for x in r])+" increasing="+str(all(np.diff(r)>0))+" below c*="+str(all(x<cs for x in r)))
A=np.array([[math.sqrt(b),math.log(b),1] for b in bs]); y=np.array([fin[b] for b in bs])
if len(bs)>=3:
    co=np.linalg.lstsq(A,y,rcond=None)[0]; out.append(f"Q3 fit a,b,c = {co}  |a-c*|={abs(co[0]-cs):.4f} (c*={cs}); {len(bs)} betas, 3 params -> {'exact fit' if len(bs)==3 else ''}")
open('table.txt','x').write("\n".join(out)); print("\n".join(out))
