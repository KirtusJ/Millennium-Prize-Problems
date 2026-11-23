"""Predicates fixed before first run:
(a) PASS_a: |kappa_1(100) backward - quadrature| <= 1e-13 (relative).
(b) PASS_b: LHS=1-kappa_M^2 >= RHS=theta*(2*lambda_M)/(2*beta) * (1 - 1e-12);
    tolerance 1e-12 relative covers rounding of ~1e-15 per ratio (50 products) plus
    backward/quadrature disagreement; kappa_n computed by both methods, both must satisfy.
"""
import numpy as np, math
def ratios_back(x, N):
    r = np.zeros(N+2); 
    for nu in range(N, 0, -1):   # r[nu-1] = 1/(2nu/x + r[nu])
        r[nu-1] = 1.0/(2*nu/x + r[nu])
    return r  # r[k]=I_{k+1}/I_k
def I_scaled_quad(nu, x, n=2_000_000):
    t = np.linspace(0, math.pi, n+1)
    f = np.exp(x*(np.cos(t)-1))*np.cos(nu*t)
    return (f.sum() - 0.5*(f[0]+f[-1]))*(math.pi/n)/math.pi
out=[]
rb=ratios_back(100.0, 2000)
k_back=rb[1]
k_quad=I_scaled_quad(2,100.0)/I_scaled_quad(1,100.0)
out.append(f"a backward {k_back:.15f}\na quad     {k_quad:.15f}\na diff {k_back-k_quad:.3e}")
PASS_a = abs(k_back-k_quad)<=1e-13*abs(k_back)
beta=10000.0; m=0.5; M=int(math.floor(m*math.sqrt(beta)))
rb=ratios_back(beta, 30000)
kb=np.prod(rb[1:M+1])  # I_{M+1}/I_1 = prod_{k=1}^{M} r_k
kq=I_scaled_quad(M+1,beta)/I_scaled_quad(1,beta)
theta=(beta/(beta+M+0.5))/(1+m*m+3*m/math.sqrt(beta))
lam=M*(M+2); RHS=theta*(2*lam)/(2*beta)
res=[]
for name,k in (("backward",kb),("quad",kq)):
    L=1-k*k; res.append((name,k,L,L/RHS,L>=RHS*(1-1e-12)))
out.append(f"M={M} theta={theta:.15f} lambda_M={lam} RHS={RHS:.15e}")
for name,k,L,rt,ok in res: out.append(f"b {name}: kappa_M={k:.15f} LHS={L:.15e} ratio={rt:.15f} ok={ok}")
PASS_b=all(r[4] for r in res)
out.append(f"PASS_a={PASS_a} PASS_b={PASS_b}")
open("gc_result.txt","x").write("\n".join(out)+"\n"); print("\n".join(out))
