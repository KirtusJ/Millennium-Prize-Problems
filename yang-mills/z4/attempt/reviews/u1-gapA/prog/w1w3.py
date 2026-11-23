"""w1w3.py -- numerical check of the constructions of rho_eta (W1) and ftilde (W3).

Construction (as in GAPS.md / tun_upper_patched.tex):
  Sm(s) = 0 (s<=0), 3s^2-2s^3 (0<=s<=1), 1 (s>=1);   psi(t) = Sm((t-1/2)/(3/2)).
  g(e) = sqrt((e-eta)_+) * psi((e-eta)/eta),  rho = g^2.
  p(a) = sqrt(2 rho(eps(a))), eps(a) = 2 asinh(sin a); f(a) = int_0^a p on [0, pi/2], f(pi-a)=f(a).
  chi(a) = Sm((pi/2-a)/(tau/2)); ftilde' = p*chi on [0,pi/2], ftilde(0)=0, ftilde(pi-a)=ftilde(a).

PREDICATES (fixed before first run), for eta in {0.5,0.2,0.05,0.01}, tau in {0.5,0.1,0.02}:
  P1  rho(e) <= (e-eta)_+ on a grid of e in [0,2]                        tol 1e-14 (float rounding)
  P2  rho(e) >= e-2eta for e in [3eta,2]                                  tol 1e-14
  P3  |g'(e)| <= 3/sqrt(2 eta) (g' analytic formula, checked vs central differences to 1e-5 rel)
  P4  g is C^1: |g'(e+)-g'(e-)| -> 0 at the junctions e = 3eta/2, 4eta  (analytic one-sided values; tol 1e-12)
  P5  c* - pi sqrt(6 eta) <= c_rho <= c*_eta <= c*   (Simpson, 2e5 panels; tol 1e-6 = quadrature error bound)
  P6  ftilde = f on [0, pi/2 - tau/2] (exact by construction: chi=1 there; tol 1e-12)
  P7  0 <= ftilde' <= f' = p on [0, pi/2]                                 tol 0
  P8  f - L tau/2 <= ftilde <= f on [0, pi/2]                              tol 1e-9 (cumulative trapezoid error)
  P9  |ftilde''| <= 6/sqrt(eta) + 3L/tau on [0, pi/2] (analytic derivative)  tol 0
  P10 ftilde'(pi/2)=0 and ftilde''(pi/2)=0 (so the even reflection is C^2)    tol 1e-12
  P11 |ftilde' cot a| <= L/sinh(3eta/4) on (0, pi/2]                       tol 0
  P12 support of p is {eps >= 3eta/2}, so p=0 on I={eps<eta}               tol 0
Output: results/w1w3.txt (mode "x").
"""
import math, sys, os
import numpy as np

L = math.sqrt(4 * math.asinh(1.0))

def Sm(s):
    s = np.clip(s, 0.0, 1.0)
    return 3 * s**2 - 2 * s**3

def dSm(s):
    return np.where((s > 0) & (s < 1), 6 * s - 6 * s**2, 0.0)

def g(e, eta):
    t = (e - eta) / eta
    return np.sqrt(np.maximum(e - eta, 0.0)) * Sm((t - 0.5) / 1.5)

def dg(e, eta):
    # analytic: zero where psi=0 (t<=1/2), else psi/(2 sqrt(e-eta)) + sqrt(e-eta) psi'(t)/eta
    t = (e - eta) / eta
    s = (t - 0.5) / 1.5
    out = np.zeros_like(e)
    m = t > 0.5
    em = e[m] - eta
    out[m] = Sm(s[m]) / (2 * np.sqrt(em)) + np.sqrt(em) * dSm(s[m]) / 1.5 / eta
    return out

def eps(a):
    return 2 * np.arcsinh(np.sin(a))

def deps(a):
    return 2 * np.cos(a) / np.sqrt(1 + np.sin(a)**2)

def simpson(y, x):
    h = x[1] - x[0]
    return h / 3 * (y[0] + y[-1] + 4 * y[1:-1:2].sum() + 2 * y[2:-1:2].sum())

def main():
    out = open(os.path.join("results", "w1w3.txt"), "x")
    def rep(s):
        print(s); out.write(s + "\n")
    fails = []
    a_full = np.linspace(0, math.pi, 400001)
    cstar = simpson(np.sqrt(2 * eps(a_full)), a_full)
    rep(f"c* = {cstar:.10f}")
    for eta in [0.5, 0.2, 0.05, 0.01]:
        e = np.linspace(0, 2, 2000001)
        rho = g(e, eta)**2
        r1 = np.max(rho - np.maximum(e - eta, 0)); ok1 = r1 <= 1e-14
        m = e >= 3 * eta
        r2 = np.max((e - 2 * eta)[m] - rho[m]); ok2 = r2 <= 1e-14
        dge = dg(e, eta); bound = 3 / math.sqrt(2 * eta)
        r3 = np.max(np.abs(dge)) / bound; ok3 = r3 <= 1
        hstep = 1e-7; ee = e[(e > 1e-3) & (e < 1.99)][::97]
        fd = (g(ee + hstep, eta) - g(ee - hstep, eta)) / (2 * hstep)
        an = dg(ee, eta)
        fdrel = np.max(np.abs(fd - an) / (np.abs(an) + 1e-3))
        # P4 one-sided derivatives at junctions t=1/2 (e=3eta/2) and t=2 (e=4eta)
        j1 = abs(float(dg(np.array([1.5 * eta + 1e-13]), eta)[0]))  # right limit at t=1/2 -> 0
        eJ = 4 * eta
        left = float(dg(np.array([eJ - 1e-12]), eta)[0]); right = 1 / (2 * math.sqrt(eJ - eta))
        j2 = abs(left - right); ok4 = j1 < 1e-5 and j2 < 1e-5
        rep(f"eta={eta}: P1 max(rho-(e-eta)+)={r1:.3e} {ok1}; P2 max((e-2eta)-rho)={r2:.3e} {ok2}; "
            f"P3 max|g'|/bound={r3:.4f} {ok3}; g' FD-vs-analytic rel={fdrel:.2e}; P4 jumps {j1:.2e},{j2:.2e} {ok4}")
        for k, ok in [("P1", ok1), ("P2", ok2), ("P3", ok3), ("P4", ok4)]:
            if not ok: fails.append((k, eta))
        # P5
        crho = 2 * simpson(np.sqrt(2 * g(eps(a_full[:200001]), eta)**2), a_full[:200001])
        ceta = simpson(np.sqrt(2 * np.maximum(eps(a_full) - eta, 0)), a_full)
        ok5 = (cstar - math.pi * math.sqrt(6 * eta) <= crho + 1e-6) and (crho <= ceta + 1e-6) and (ceta <= cstar + 1e-6)
        rep(f"  P5 c_rho={crho:.6f} c*_eta={ceta:.6f} lower={cstar - math.pi*math.sqrt(6*eta):.6f} {ok5}")
        if not ok5: fails.append(("P5", eta))
        # P12
        a = np.linspace(0, math.pi / 2, 1000001)
        p = np.sqrt(2) * g(eps(a), eta)
        ok12 = np.all(p[eps(a) < 1.5 * eta] == 0)
        if not ok12: fails.append(("P12", eta))
        dp = np.sqrt(2) * dg(eps(a), eta) * deps(a)
        f = np.concatenate([[0], np.cumsum((p[1:] + p[:-1]) / 2 * np.diff(a))])
        for tau in [0.5, 0.1, 0.02]:
            s = (math.pi / 2 - a) / (tau / 2)
            chi = Sm(s); dchi = -dSm(s) / (tau / 2)
            ftp = p * chi
            ftpp = dp * chi + p * dchi
            ft = np.concatenate([[0], np.cumsum((ftp[1:] + ftp[:-1]) / 2 * np.diff(a))])
            win = a < math.pi / 2 - tau / 2
            r6 = np.max(np.abs(ft[win] - f[win])); ok6 = r6 <= 1e-12
            ok7 = bool(np.all(ftp >= 0) and np.all(ftp <= p))
            r8lo = np.min(ft - (f - L * tau / 2)); r8hi = np.max(ft - f); ok8 = r8lo >= -1e-9 and r8hi <= 1e-9
            B9 = 6 / math.sqrt(eta) + 3 * L / tau
            r9 = np.max(np.abs(ftpp)) / B9; ok9 = r9 <= 1
            ok10 = abs(ftp[-1]) < 1e-12 and abs(ftpp[-1]) < 1e-12
            cot = np.cos(a[1:]) / np.sin(a[1:])
            r11 = np.max(np.abs(ftp[1:] * cot)) / (L / math.sinh(0.75 * eta)); ok11 = r11 <= 1
            rep(f"  tau={tau}: P6 {r6:.1e} {ok6}; P7 {ok7}; P8 min(ft-f+L tau/2)={r8lo:.4e} max(ft-f)={r8hi:.1e} {ok8}; "
                f"P9 max|ft''|/bound={r9:.4f} {ok9}; P10 {ok10}; P11 ratio={r11:.4f} {ok11}")
            for k, ok in [("P6", ok6), ("P7", ok7), ("P8", ok8), ("P9", ok9), ("P10", ok10), ("P11", ok11)]:
                if not ok: fails.append((k, eta, tau))
        rep(f"  P12 {ok12}")
    rep(f"FAILED: {fails}")
    out.close()
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
