"""A4/A5: evaluate THEOREM_V's L = (2/l^3)[A P_b - B' Psi'_b] and compare with C_{b,s}(0) computed by FFT
in position space; test Jensen extension at t in {0.02, 0.1}.

Setting: lattice side N, b = l/N, khat_i = (2/b) sin(k_i b/2), a(k) = (khat1^2+khat2^2)/(2 khat) e^{-2 s khat^2} (a(0)=0),
D(x) = l^-3 sum_k e^{ikx} a(k) e^{-t khat}, C(t) = 2 b^6 sum_{x,y} f(bx) f(by) D(x-y)^2  (SETTING.md + flow).
Parameters: K = min(2.5/sqrt(s), (1-1e-12) pi/b), Q = 0.5 K, K' = K - Q/2, eps = K^2 b^2/24, alpha = 4s, Delta = 2 pi/l.
L0,U0,L1,U1 as in a3_sums.py (Poisson delta0/delta1 + tail integral from K'-Delta).
A = (1-eps)^4 (2 L1 L0^2 - U1 U0^2)/4 ; B' = (1-eps)^4 (3/16) U0^3 + s A.
P_b = b^3 sum_x f^2 (Parseval: sum_q |fb(q)|^2 = l^3 P_b) ; Psi'_b = l^-3 sum_q |q|^2 |fb(q)|^2, q = BZ representative (my reading).
Hypotheses per case: H1 eps<1, H2 K<=pi/b, H3 K'-Delta >= 1/sqrt(alpha), H4 Q<=K, H5 A>=0, H6 Q^2 >= A/B'.
Predicates (cases meeting H1-H6):
  Q1: for every BZ q: G(q) = sum_k a(k)a(q-k) >= A - B'|q|^2 - 1e-9*G(0)   (tol: FFT roundoff, ~1e-13 rel observed in identity check)
  Q2: L <= C(0) (1 + 1e-9)
  Q3 (all cases): momentum identity C = (2/l^6) sum_q |fb|^2 G(q) agrees with position-space C to 1e-9 rel
  Q4 (all cases, t in {0.02,0.1}): C(t) >= C(0) exp(-t M1/M0) (1 - 1e-9)   [Jensen]
  Q5 (all cases): M1 <= U1bar = (4/l^3) P_b sqrt(A0 A2) with exact lattice A_p = sum a^2 khat^p
  Q6 (cases with L>0): C(t) >= L exp(-t U1bar/L)
Measured only: L/C, A s^2.5 (2/l^3), s Psi'/P, C(t)/C(0).
f1: non-symmetric bump, widths (0.15,0.12,0.18), skew factor (1+0.6 d1/0.15 + 0.3 d2 d3/0.15^2), centre (0.31,0.47,0.22)l, images n in {-1,0,1}^3.
f2: f1 minus its lattice mean (b^3 sum f2 = 0 exactly up to roundoff).
Usage: python3 a4_bound.py OUT NMAX   ; exit 0 iff all predicates met.
"""
import sys, math, time
import numpy as np
from math import erfc, sqrt, pi, exp

out, NMAX = sys.argv[1], int(sys.argv[2])
fails = []; rows = []; counts = dict(cases=0, qual=0, Lpos=0)

def bounds(l, s, Kp):
    al = 4*s; D = 2*pi/l; c0 = sqrt(pi/al)/D; c1 = c0/(2*al)
    d0 = 2*sum(exp(-m*m*l*l/(4*al)) for m in range(1, 60))
    d1 = 2*sum(abs(1-m*m*l*l/(2*al))*exp(-m*m*l*l/(4*al)) for m in range(1, 60))
    x = Kp - D
    T0 = 0.5*sqrt(pi/al)*erfc(sqrt(al)*x)/D
    T1 = ((x*exp(-al*x*x))/(2*al) + sqrt(pi)*erfc(sqrt(al)*x)/(4*al**1.5))/D
    return c0*(1-d0)-2*T0, c0*(1+d0), c1*(1-d1)-2*T1, c1*(1+d1), x >= 1/sqrt(al)

def fgrid(l, N):
    x = (np.arange(N)*l/N)
    X = np.meshgrid(x, x, x, indexing='ij')
    w = np.array([0.15, 0.12, 0.18]); c = np.array([0.31, 0.47, 0.22])*l
    f = np.zeros((N, N, N))
    for n1 in (-1, 0, 1):
        for n2 in (-1, 0, 1):
            for n3 in (-1, 0, 1):
                d = [X[0]-c[0]+n1*l, X[1]-c[1]+n2*l, X[2]-c[2]+n3*l]
                e = np.exp(-(d[0]**2/(2*w[0]**2)+d[1]**2/(2*w[1]**2)+d[2]**2/(2*w[2]**2)))
                f += e*(1+0.6*d[0]/0.15+0.3*d[1]*d[2]/0.15**2)
    return f

for l in (1.0, 2.0, 3.0):
    for s in (0.0005, 0.001, 0.002):
        N = min(NMAX, 2*math.ceil(l/(0.5*sqrt(s))/2)); b = l/N
        k1 = 2*pi/l*np.fft.fftfreq(N, 1.0/N)
        kh1 = (2/b)*np.sin(k1*b/2)
        KH2 = [kh1[:, None, None]**2, kh1[None, :, None]**2, kh1[None, None, :]**2]
        kh2 = KH2[0]+KH2[1]+KH2[2]; kh = np.sqrt(kh2)
        a = np.zeros((N, N, N)); m = kh2 > 0
        a[m] = ((KH2[0]+KH2[1])*np.ones((1, 1, N)))[m]/(2*kh[m])*np.exp(-2*s*kh2[m])
        q2 = k1[:, None, None]**2+k1[None, :, None]**2+k1[None, None, :]**2
        K = min(2.5/sqrt(s), (1-1e-12)*pi/b); Q = 0.5*K; Kp = K-Q/2; eps = K*K*b*b/24
        L0, U0, L1, U1, h3 = bounds(l, s, Kp)
        A = (1-eps)**4*(2*L1*L0**2-U1*U0**2)/4; Bp = (1-eps)**4*(3/16)*U0**3+s*A
        H = dict(H1=eps < 1, H2=K <= pi/b, H3=h3, H4=Q <= K, H5=A >= 0, H6=(A <= 0 or Q*Q >= A/Bp))
        qual = all(H.values())
        D0 = np.real(np.fft.ifftn(a))*N**3/l**3
        D1 = np.real(np.fft.ifftn(a*kh))*N**3/l**3
        G = np.real(np.fft.fftn(D0*D0))*l**6/N**3            # G(q) = sum_k a(k) a(q-k)
        G1 = 2*np.real(np.fft.fftn(D0*D1))*l**6/N**3         # sum a a (khat+khat')
        A0 = (a*a).sum(); A2 = (a*a*kh2).sum()
        f1 = fgrid(l, N)
        for fname, f in (("f1", f1), ("f2", f1-f1.mean())):
            counts['cases'] += 1; counts['qual'] += qual
            F = np.fft.fftn(f); fb2 = np.abs(F)**2*b**6
            H0 = np.real(np.fft.fftn(D0*D0))
            Cpos = 2*b**6/N**3*(np.abs(F)**2*H0).sum()          # position-space C via FFT convolution
            Cmom = 2/l**6*(fb2*G).sum()
            if abs(Cpos-Cmom) > 1e-9*abs(Cpos): fails.append(f"Q3 {fname} l={l} s={s} {Cpos} {Cmom}")
            Pb = b**3*(f*f).sum(); Psi = (fb2*q2).sum()/l**3
            Lb = 2/l**3*(A*Pb-Bp*Psi)
            M0 = Cpos; M1 = 2/l**6*(fb2*G1).sum(); U1bar = 4/l**3*Pb*sqrt(A0*A2)
            if not M1 <= U1bar*(1+1e-12): fails.append(f"Q5 {fname} l={l} s={s} M1={M1} U1bar={U1bar}")
            if qual:
                viol = G - (A-Bp*q2) < -1e-9*G[0, 0, 0]
                if viol.any(): fails.append(f"Q1 {fname} l={l} s={s} nviol={int(viol.sum())} worst={(G-(A-Bp*q2)).min():.3e}")
                if not Lb <= Cpos*(1+1e-9): fails.append(f"Q2 {fname} l={l} s={s} L={Lb} C={Cpos}")
            counts['Lpos'] += Lb > 0
            tl = []
            for t in (0.02, 0.1):
                Dt = np.real(np.fft.ifftn(a*np.exp(-t*kh)))*N**3/l**3
                Ct = 2*b**6/N**3*(np.abs(F)**2*np.real(np.fft.fftn(Dt*Dt))).sum()
                jen = M0*exp(-t*M1/M0)
                if not Ct >= jen*(1-1e-9): fails.append(f"Q4 {fname} l={l} s={s} t={t} C={Ct} jensen={jen}")
                lt = Lb*exp(-t*U1bar/Lb) if Lb > 0 else float('nan')
                if Lb > 0 and not Ct >= lt*(1-1e-9): fails.append(f"Q6 {fname} l={l} s={s} t={t}")
                tl.append(f"t={t}: C/C0={Ct/M0:.4e} jensen/C0={jen/M0:.4e} Lexp/C={lt/Ct:.3e}")
            rows.append(f"{fname} l={l} s={s} N={N} b/sqrt(s)={b/sqrt(s):.3f} eps={eps:.4f} H={''.join('1' if v else '0' for v in H.values())} "
                        f"intf={b**3*f.sum():+.3e} sPsi/P={s*Psi/Pb:.4f} C={Cpos:.6e} L={Lb:+.6e} L/C={Lb/Cpos:+.4f} "
                        f"(2/l^3)A s^2.5={2*A/l**3*s**2.5:.4e} B'/(As)={Bp/(A*s):.3f} M1/M0={M1/M0:.3f} U1bar/L={(U1bar/Lb if Lb>0 else float('nan')):.3e} | " + " ; ".join(tl))
            print(rows[-1], flush=True)
with open(out, "x") as fh:
    fh.write(f"counts: {counts}\n" + "\n".join(rows) + f"\nFAILS ({len(fails)}):\n" + "\n".join(fails) + "\n")
sys.exit(0 if not fails else 1)
