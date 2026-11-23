"""Predicate P5' (fixed before run): m(tau) from explicit matrices (results_flow.txt) equals
closed form (1/L^4) sum_{k!=0, p!=0} 2 p^2 exp(-2 tau p^2)/A  (two transverse polarizations; sum_{i<j}|D_i a_j-D_j a_i|^2 = p^2 |a_T|^2),
tol abs 1e-12 (values <=7e-3, float64 sums of 65536 terms).
The earlier P5 failure was my own expectation error (omitted factor 2), not a target defect."""
import numpy as np, itertools, re
L=16; q=4*np.sin(np.pi*np.arange(L)/L)**2
ref={}
for line in open("results_flow.txt"):
    t=re.match(r"tau=(\d+): e=(\S+) m=(\S+)",line)
    if t: ref[int(t[1])]=float(t[3])
out=open("results_m.txt","x")
for tau in (1,4,16):
    m=0.0
    for nv in itertools.product(range(L),repeat=4):
        if not any(nv): continue
        qq=q[list(nv)]; A=qq.sum(); p2=qq[:3].sum()
        if p2>1e-12: m+=2*p2*np.exp(-2*tau*p2)/A
    m/=L**4; s=f"tau={tau} m_closed={m:.10e} m_matrix={ref[tau]:.10e} diff={abs(m-ref[tau]):.1e} {'MET' if abs(m-ref[tau])<1e-12 else 'FAIL'}"
    print(s); out.write(s+"\n")
