"""T152 main. Predicates fixed BEFORE first run:
 REVISED after K2 failure: positivity asserted only on |x|<=0.5 (strict) and g.min()>-1e-12 globally (roundoff in tails).
 P0 (hypothesis per case, rule 4): for each of the 12 (beta,a) cases test Q1 and Q2 separately and count met/failed.
 Q1: sqrt(b)*L <= sqrt(b)*J + log(b).  Q2: L <= 10*a.  Measured only: 1-lambda, (1-lambda)*b^(1/3), sqrt(b)*(L-J).
 Sanity predicates: eigenvector g positive (min>0) after projecting ones onto the top eigenspace (eigs within 1e-9; eps vanishes at 0 AND pi,
 so top eigenvalue is 2-fold degenerate up to roundoff, Perron vector = symmetric combination); T symmetric to 1e-12; L(0)==0;
 J quadrature: GL n=200 vs 400 agree 1e-10 (tolerance = quadrature convergence); eigen residual |Tg-lambda g|<1e-10.
Output files opened with mode 'x'."""
import numpy as np, json
def J(a,n=200):
    x,w=np.polynomial.legendre.leggauss(n); s=(x+1)/2; w=w/2   # x=a s^2 removes sqrt singularity
    xx=a*s**2; return np.sum(w*2*a*s*np.sqrt(4*np.arcsinh(np.sin(xx))))
rows=[]; fails=[]
for b in (256,1024,4096):
    h=0.5/np.sqrt(b); N=int(np.round(2*np.pi/h)); N+=(-N)%4; h=2*np.pi/N
    x=-np.pi+h*np.arange(N); eps=2*np.arcsinh(np.abs(np.sin(x)))
    d=x[:,None]-x[None,:]
    K=h*np.sqrt(b/(2*np.pi))*sum(np.exp(-b*(d+2*np.pi*k)**2/2) for k in (-1,0,1))
    e=np.exp(-eps/2); T=e[:,None]*K*e[None,:]
    assert abs(T-T.T).max()<1e-12
    ev,V=np.linalg.eigh(T); lam=ev[-1]
    idx=np.where(ev>lam-1e-9)[0]; B=V[:,idx]; g=B@(B.T@np.ones(N))
    g/=np.sqrt(h*np.sum(g**2)); assert g.min()>-1e-12 and g[np.abs(x)<=0.5].min()>0, g.min()
    assert abs(T@g-lam*g).max()<1e-10
    i0=N//2; assert abs(x[i0])<1e-12
    for a in (0.05,0.1,0.2,0.4):
        i=i0+int(np.round(a/h)); xa=x[i]
        L=-np.log(g[i]/g[i0])/np.sqrt(b); Ja=J(a); assert abs(Ja-J(a,400))<1e-10
        sb=np.sqrt(b)
        rows.append(dict(beta=b,N=N,a=a,x_used=xa,L=L,J=Ja,sbLmJ=sb*(L-Ja),Q1=bool(sb*L<=sb*Ja+np.log(b)),Q2=bool(L<=10*a),
                         one_minus_lam=1-lam,scaled=(1-lam)*b**(1/3),degen=len(idx)))
with open("results.json","x") as f: json.dump(rows,f,indent=1)
for r in rows: print({k:(round(v,6) if isinstance(v,float) else v) for k,v in r.items()})
print("Q1 met",sum(r['Q1'] for r in rows),"failed",sum(not r['Q1'] for r in rows),"| Q2 met",sum(r['Q2'] for r in rows),"failed",sum(not r['Q2'] for r in rows))
