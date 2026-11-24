import numpy as np
def qm(a,b):
    a0,a1,a2,a3=[a[...,i] for i in range(4)]; b0,b1,b2,b3=[b[...,i] for i in range(4)]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
                     a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0],-1)
def dotc(a,b):  # Re(a b)
    c=a*np.array([1,-1,-1,-1.]); return (c*b).sum(-1)
E=[np.array(x,float) for x in ([0,1,0,0],[0,0,1,0],[0,0,0,1])]
rng=np.random.default_rng(7)
def ru(*s):
    x=rng.normal(size=s+(4,)); return x/np.linalg.norm(x,axis=-1,keepdims=True)
C,M,N=ru(),ru(),ru()
beta=1.0
def feats(u,v):
    P=qm(C,u); Q=qm(M,v); QN=qm(Q,N)
    Y=dotc(P,QN)
    X=[qm(P,e) for e in E]; W=[qm(qm(Q,e),N) for e in E]
    A=np.stack([np.stack([dotc(X[a],W[b]) for b in range(3)],-1) for a in range(3)],-2)
    s=np.stack([beta*dotc(X[a],QN) for a in range(3)],-1)
    t=np.stack([beta*dotc(P,W[b]) for b in range(3)],-1)
    Z=(Y[:,None,None]*np.ones((1,3,3)) + s[:,:,None]*(-s[:,:,None]/beta) + t[:,None,:]*(-t[:,None,:]/beta)
       + beta*A**2 + s[:,:,None]*t[:,None,:]*A).sum((1,2))
    return Y,(A**2).sum((1,2)),Z
nb,m=20,100000
rows=[];maxerr=0
for _ in range(nb):
    u,v=ru(m),ru(m)
    Y,S,Z=feats(u,v); maxerr=max(maxerr,np.abs(S-(2+Y**2)).max())
    w=np.exp(beta*Y); w/=w.sum(); EY=(w*Y).sum()
    rows.append([(w*S).sum(),(w*(2+Y**2)).sum(),(w*Z).sum(),(w*(Y-EY)*Z).sum(),(w*Z**2).sum(),EY])
R=np.array(rows); mean=R.mean(0); se=R.std(0,ddof=1)/np.sqrt(nb)
# L2 norm: sqrt of mean; SE by delta
l2=np.sqrt(mean[4]); l2se=se[4]/(2*l2)
# finite differences
u,v=ru(),ru(); h=1e-4
ex=lambda e,x: np.cos(x)*np.array([1,0,0,0.])+np.sin(x)*e
f=lambda a,b,s,t: qm(qm(qm(qm(qm(qm(C,u),ex(E[a],s)),M),v),ex(E[b],t)),N)[0]
Ar=np.stack([np.stack([dotc(qm(qm(C,u),E[a]),qm(qm(qm(M,v),E[b]),N)) for b in range(3)]) for a in range(3)])
fd=np.array([[(f(a,b,h,h)-f(a,b,h,-h)-f(a,b,-h,h)+f(a,b,-h,-h))/(4*h*h) for b in range(3)] for a in range(3)])
fderr=np.abs(fd-Ar).max()
diff=mean[3]-mean[1]; sed=np.sqrt(np.var(R[:,3]-R[:,1],ddof=1)/nb)
verdict="YES" if abs(diff)<=3*sed else "NO"
out=f"""# Results (seed 7, beta=1, 2e6 samples = 20 batches x 1e5, self-normalised importance weights)
- pointwise max |sum A^2 - (2+Y^2)| = {maxerr:.3e}
- (a) E[sum A^2] = {mean[0]:.6f} +- {se[0]:.6f}; E[2+Y^2] = {mean[1]:.6f} +- {se[1]:.6f}
- (b) E[Z] = {mean[2]:.6f} +- {se[2]:.6f} (expect 0)
- E[(Y-EY)Z] = {mean[3]:.6f} +- {se[3]:.6f}; E[2+Y^2] = {mean[1]:.6f} +- {se[1]:.6f}
- difference = {diff:.6f}, SE(diff, paired batches) = {sed:.6f}, z = {diff/sed:.2f}
- ||Z||_L2/beta = {l2/beta:.6f} +- {l2se:.6f}
- E[Y] = {mean[5]:.6f}
- finite-difference check of A_ab (h=1e-4): max err = {fderr:.3e}
- Verdict: E[(Y-EY)Z] equals E[2+Y^2] within 3 SE? {verdict}
"""
with open('results.md','x') as fh: fh.write(out)
print(out)
