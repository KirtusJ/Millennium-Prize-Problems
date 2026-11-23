"""
Predicates (declared before first run):
 P1: for every case, |ratio - 4| < 1e-9, where ratio = (lam - (sg)^T T (sg)) / S.
 P2: for every case, |(1/2) sum (s_x-s_y)^2 g_x T_xy g_y - 4*S| < 1e-9 (identity form).
 P3 (hypotheses): every case has T symmetric with all entries > 0.
Tolerance 1e-9 reflects float64 eigensolver accuracy ~1e-12.
Cases: fixed T with A={0}; seeds 1,2 (default_rng, uniform[0.1,2], symmetrised) with A={0} and A={0,1}.
"""
import numpy as np, json
Ts = {"fixed": np.array([[2.0,0.7,0.3],[0.7,1.5,0.5],[0.3,0.5,1.1]])}
for s in (1,2):
    M = np.random.default_rng(s).uniform(0.1,2,(3,3)); Ts["seed%d"%s] = (M+M.T)/2
cases=[]
for name,T in Ts.items():
    for A in ([0],[0,1]):
        w,v = np.linalg.eigh(T); lam=w[-1]; g=v[:,-1]; g=g*np.sign(g.sum())
        sig = np.array([1.0 if i in A else -1.0 for i in range(3)])
        Ac=[i for i in range(3) if i not in A]
        S = sum(g[x]*T[x,y]*g[y] for x in A for y in Ac)
        sg = sig*g
        lhs = lam - sg@T@sg
        half = 0.5*sum((sig[x]-sig[y])**2*g[x]*T[x,y]*g[y] for x in range(3) for y in range(3))
        cases.append(dict(case=name,A=A,lam=lam,S=S,lhs=lhs,half_sum=half,ratio=lhs/S,
            P1=bool(abs(lhs/S-4)<1e-9),P2=bool(abs(half-4*S)<1e-9),
            hyp=bool(np.allclose(T,T.T) and (T>0).all() and (g>0).all())))
out=dict(cases=cases,P1_all=all(c["P1"] for c in cases),P2_all=all(c["P2"] for c in cases),
         hyp_count=sum(c["hyp"] for c in cases),n=len(cases))
with open("result.json","x") as f: json.dump(out,f,indent=1)
for c in cases: print(c["case"],c["A"],c["ratio"],c["P1"],c["P2"],c["hyp"])
print(out["P1_all"],out["P2_all"],out["hyp_count"],out["n"])
