"""Predicates (before running):
P1: control c* in [4.60535,4.60545] (expected 4.6054), stable under refinement.
P2: N multiple of 4, grid index N/2 has x==0 (|x|<1e-12); L(0)==0 exactly.
P3: top eigenvalue>0, g>0 everywhere after sign fix, h*sum g^2==1.
Expected N=204 (2pi*32=201.06->201->204).
"""
import numpy as np
def ctrl(M):
    t=(np.arange(M)+.5)*np.pi/M; a=np.pi/2*(1-np.cos(t))
    return np.sum(np.sqrt(4*np.arcsinh(np.sin(a)))*np.pi/2*np.sin(t))*np.pi/M
c1,c2=ctrl(20000),ctrl(80000)
with open("control.txt","x") as f:
    f.write(f"c*={c2:.6f} (M=20000: {c1:.6f}); expected 4.6054; match={abs(c2-4.6054)<1e-4}\n")
print(open("control.txt").read())
beta=256.; kappa=.5; h=kappa/np.sqrt(beta)
N=int(round(2*np.pi/h)); N+=(-N)%4; h=2*np.pi/N
x=-np.pi+np.arange(N)*h
eps=2*np.arcsinh(np.abs(np.sin(x)))
d=x[:,None]-x[None,:]
K=sum(np.exp(-beta*(d+2*np.pi*k)**2/2) for k in (-1,0,1))*h*np.sqrt(beta/(2*np.pi))
w=np.exp(-eps/2); T=w[:,None]*K*w[None,:]
ev,V=np.linalg.eigh(T); lam=ev[-1]; g=V[:,-1]
g=g*np.sign(g.sum()); g/=np.sqrt(h*np.sum(g**2))

L=lambda i:-np.log(g[i]/g[N//2])/np.sqrt(beta)
i=N//2+int(round(0.1/h))
res=f"N={N} h={h:.8f} idx0={N//2} idx={i} x={x[i]:.8f} sqrtbeta*L(0.1)={np.sqrt(beta)*L(i):.6f} L(0)={L(N//2)!r} lambda={lam:.10f} gap={lam-ev[-2]:.3e} gmin_pos_region={g[N//2-60:N//2+60].min():.3e}\n"
with open("result.txt","x") as f: f.write(res)
print(res)
