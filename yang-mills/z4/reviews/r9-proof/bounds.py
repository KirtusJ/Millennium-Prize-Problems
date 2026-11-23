"""bounds.py -- r9-proof, builder.  Free lattice Maxwell benchmark, two-sided bound on C_b.

Setting (input/STATEMENT.md): ell = 1, b = ell/N, f(y) = sum_m exp(-|y-m|^2/(2R^2)), R = 0.1
(periodized Gaussian, peak 1; all bounds and C_b are homogeneous of degree 2 in f, so the
ratios bound/measured do not depend on this normalization).
w(k) = P33(k) khat/2, P33 = (khat1^2+khat2^2)/khat^2.  fhat_b(q) = b^3 sum_x f(bx) e^{-i q.bx}.
A = (2 pi)^{3/2} R^3 = integral of f over the torus.

Proved constants (proof.md):
  v(tau) = (2/ell^6) * F0^2 * min(kap3^2 e^{-4 tau kap3}, (2pi/ell)^2 e^{-4 tau 2pi/ell}),
           kap3 = (6/ell) sin(pi/3), F0 = A   (N >= 3; f > 0 so fhat_b(0) >= A by aliasing)
  V(tau) = (2/ell^6) * F^2 * (pi/ell)^2 * G(4 tau/ell)^2,
           G(a) = 4 pi e^{sqrt3 a/2} (6/a^4 + sqrt3/a^3),  F = A (1 + eps8), eps8 = theta(N=8)^3 - 1
           (valid for N >= 8, i.e. b_0 = 1/8).

PREDICATES (fixed before the first run):
 P0 hypothesis test (step 1 of the route): at N = 8, t in {0.05, 0.1, 0.2}: position-space
    C_pos = 2 b^6 sum_{x,y} f f D_t(x-y)^2 (D_t by explicit k-sum, no FFT) equals the momentum form
    C_mom (FFT convolution).  Tolerance rel 1e-10: float64 sums of <= 3e5 terms of one sign up to
    cancellation in D_t; roundoff ~1e-13, three orders of margin.
 P1 every momentum weight is >= 0: min w(k) >= 0 exactly (N = 16..64).
 P2 Jordan componentwise on the BZ: (2/pi)|k_i| <= |khat_i| <= |k_i| (rel slack 1e-12, float), N = 16..64.
 P3 aliasing for the Gaussian: A <= fhat_b(0) <= A(1+eps_N) and max_q |fhat_b(q)| <= fhat_b(0)
    (rel slack 1e-12), N = 16..64.
 P4 lattice-sum lemma: S_b(t) = sum_{k != 0, BZ} w(k) e^{-t khat} <= (pi/ell) G(4t/ell), all N, t in {0.05,0.1,0.2}.
 P5 bracket: v(tau) <= C_b(2 tau) and C_b(tau) <= V(tau), N in {16,24,32,48,64}, tau in {0.05,0.1}.
 P6 factorized bound: C_b(t) <= (2/ell^6) F^2 S_b(t)^2 (intermediate step of the upper bound), same cases.
 Measured only: looseness ratios C_b(2tau)/v, V/C_b(tau); window E0 = (1/tau) log(2V/v); S4 constant.
Hypothesis count ("for all" predicates): cases qualifying = N >= 8 (needed for F) and N >= 3 (for v): all listed N.
"""
import numpy as np, math, json, os, sys

ell, R = 1.0, 0.1
A = (2*math.pi)**1.5 * R**3
SQ3 = math.sqrt(3.0)
res = {"met": [], "failed": [], "measured": {}}

def pred(name, ok, info):
    (res["met"] if ok else res["failed"]).append(name + ": " + info)
    print(("MET   " if ok else "FAIL  ") + name + ": " + info)

def fgrid(N):
    b = ell/N
    x = np.arange(N)*b
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    f = np.zeros_like(X)
    for m1 in range(-2, 3):
        for m2 in range(-2, 3):
            for m3 in range(-2, 3):
                f += np.exp(-((X-m1)**2+(Y-m2)**2+(Z-m3)**2)/(2*R*R))
    return f

def modes(N):
    b = ell/N
    n = np.arange(N); n = np.where(n >= (N+1)//2, n-N, n)  # BZ representatives, |k_i b| <= pi
    k1 = 2*math.pi*n/ell
    K = np.meshgrid(k1, k1, k1, indexing="ij")
    kh = [(2/b)*np.sin(Ki*b/2) for Ki in K]
    khat = np.sqrt(kh[0]**2+kh[1]**2+kh[2]**2)
    with np.errstate(invalid="ignore", divide="ignore"):
        w = np.where(khat > 0, (kh[0]**2+kh[1]**2)/np.where(khat > 0, khat**2, 1)*khat/2, 0.0)
    return K, kh, khat, w

def C_mom(N, t):
    b = ell/N
    K, kh, khat, w = modes(N)
    g = w*np.exp(-t*khat); g[0, 0, 0] = 0.0
    conv = np.fft.ifftn(np.fft.fftn(g)**2).real   # sum_k g(k) g(q-k)
    fh = b**3*np.fft.fftn(fgrid(N))
    return 2/ell**6*np.sum(np.abs(fh)**2*conv), g

def C_pos(N, t):
    b = ell/N
    K, kh, khat, w = modes(N)
    f = fgrid(N)
    idx = np.arange(N)
    r = np.stack(np.meshgrid(idx, idx, idx, indexing="ij"), -1).reshape(-1, 3)*b
    kk = np.stack(K, -1).reshape(-1, 3)
    gk = (w*np.exp(-t*khat)).reshape(-1); gk[0] = 0.0
    D = (np.exp(1j*(r @ kk.T)) @ gk).real/ell**3          # D_t(r), explicit k-sum
    D2 = D.reshape(N, N, N)**2
    tot = 0.0
    for x in np.ndindex(N, N, N):
        tot += f[x]*np.sum(f*np.roll(D2, shift=x, axis=(0, 1, 2)))  # sum_y f(y) D^2(x-y)
    return 2*b**6*tot

def G(a): return 4*math.pi*math.exp(SQ3*a/2)*(6/a**4+SQ3/a**3)

def eps(N):
    b = ell/N; q = math.exp(-2*math.pi**2*R**2/b**2)
    th = 1+2*sum(q**(j*j) for j in range(1, 50))
    return th**3-1

kap3 = 6/ell*math.sin(math.pi/3)
F0 = A
F = A*(1+eps(8))
def v_of(tau):
    t = 2*tau
    return 2/ell**6*F0**2*min(kap3**2*math.exp(-2*t*kap3), (2*math.pi/ell)**2*math.exp(-2*t*2*math.pi/ell))
def V_of(tau):
    return 2/ell**6*F**2*(math.pi/ell)**2*G(4*tau/ell)**2

# P0
for t in (0.05, 0.1, 0.2):
    cp = C_pos(8, t); cm, _ = C_mom(8, t)
    rel = abs(cp-cm)/abs(cp)
    pred(f"P0 N=8 t={t}", rel < 1e-10, f"C_pos={cp:.12e} C_mom={cm:.12e} rel={rel:.2e}")

Ns = (16, 24, 32, 48, 64)
taus = (0.05, 0.1)
table = []
for N in Ns:
    b = ell/N
    K, kh, khat, w = modes(N)
    pred(f"P1 N={N}", w.min() >= 0, f"min w = {w.min():.3e}")
    ok = True
    for Ki, khi in zip(K, kh):
        a, h = np.abs(Ki), np.abs(khi)
        ok &= bool(np.all(2/math.pi*a <= h*(1+1e-12)+1e-300) and np.all(h <= a*(1+1e-12)+1e-300))
    pred(f"P2 N={N}", ok, "componentwise Jordan on all BZ modes")
    fh = b**3*np.fft.fftn(fgrid(N)); f0 = fh[0, 0, 0].real
    ok3 = A*(1-1e-12) <= f0 <= A*(1+eps(N))*(1+1e-12) and np.abs(fh).max() <= f0*(1+1e-12)
    pred(f"P3 N={N}", ok3, f"fhat(0)/A-1 = {f0/A-1:.3e}, eps_N={eps(N):.3e}, max|fhat|/fhat(0)={np.abs(fh).max()/f0:.15f}")
    for t in (0.05, 0.1, 0.2):
        S = float(np.sum(w*np.exp(-t*khat)))
        pred(f"P4 N={N} t={t}", S <= math.pi/ell*G(4*t/ell), f"S_b={S:.4e} bound={math.pi/ell*G(4*t/ell):.4e} ratio={math.pi/ell*G(4*t/ell)/S:.2f}")
    for tau in taus:
        c2, _ = C_mom(N, 2*tau); c1, _ = C_mom(N, tau)
        v, V = v_of(tau), V_of(tau)
        pred(f"P5 N={N} tau={tau}", v <= c2 and c1 <= V,
             f"v={v:.4e} <= C(2tau)={c2:.6e} ; C(tau)={c1:.6e} <= V={V:.4e}")
        for t, c in ((tau, c1), (2*tau, c2)):
            S = float(np.sum(w*np.exp(-t*khat)))
            fb = 2/ell**6*F**2*S**2
            pred(f"P6 N={N} t={t}", c <= fb, f"C={c:.4e} <= 2F^2 S^2={fb:.4e}")
        E0 = math.log(2*V/v)/tau
        table.append(dict(N=N, tau=tau, v=v, C2=c2, C1=c1, V=V, lowloose=c2/v, uploose=V/c1, E0=E0))

# S4 = sum_{m != 0} |m|^-4 (needed only for the generic-f constants in proof.md)
M = 60
m = np.arange(-M, M+1); X, Y, Z = np.meshgrid(m, m, m, indexing="ij"); r2 = (X*X+Y*Y+Z*Z).astype(float)
r2[M, M, M] = np.inf
part = float(np.sum(r2**-2.0))
# tail: m with |m|_inf > M has |m| >= M+1; its unit cube lies in |y| >= M-1 and |m|^-4 <= (|y|-sqrt3/2)^-4
u0 = M-1.0-SQ3/2; c = SQ3/2   # closed form of int_{M-1}^inf 4 pi r^2/(r-c)^4 dr
tail = 4*math.pi*(1/u0 + c/u0**2 + c*c/(3*u0**3))
res["measured"]["S4_partial"] = part; res["measured"]["S4_upper"] = part+tail
print(f"S4: partial(M={M})={part:.6f}, upper bound={part+tail:.6f}")
res["measured"]["table"] = table
res["constants"] = dict(A=A, F=F, eps8=eps(8), kap3=kap3, b0=1/8)
for r_ in table:
    print("N={N:3d} tau={tau}: v={v:.4e} C(2tau)={C2:.5e} C(tau)={C1:.5e} V={V:.4e} "
          "C2/v={lowloose:.1f} V/C1={uploose:.3e} E0={E0:.1f}".format(**r_))
print(f"COUNTS met={len(res['met'])} failed={len(res['failed'])} measured_only={len(table)*3+1}")
out = "results_bounds_run1.json"
assert not os.path.exists(out), "result file exists; never overwrite"
json.dump(res, open(out, "w"), indent=1)
sys.exit(1 if res["failed"] else 0)
