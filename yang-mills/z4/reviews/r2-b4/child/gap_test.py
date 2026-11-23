"""Test of the claim M := <w,(H-E0)w> == (2/kappa)(4 - s) on SU(2) class functions.

Basis chi_0..chi_N (orthonormal).  H = (2/kappa)(-Delta) + lambda(1 - cos theta):
  H_nn = (2/kappa) n(n+2) + lambda,  H_{n,n+1} = H_{n+1,n} = -lambda/2   (cos = chi_1/2).
F = chi_1:  F_{n,n+1} = F_{n+1,n} = 1 (truncated at N).
Omega = normalized ground vector, E0 its energy, s = <Omega,F^2 Omega>,
w = (F - <F>)Omega, M = <w, H w> - E0 <w, w>   (computed directly from the matrix,
the identity is NOT used).  Ground state: Sturm bisection for E0 to full precision,
then inverse iteration (tridiagonal Thomas solve).  Pure Python (numpy unavailable).

PREDICATES (fixed before running), for kappa in {0.5,1,2}, lambda in {0.1,1,10,100}:
  P0 (truncation): |c_N| < 1e-12 at N=40 (ground coefficient in the top mode).
     Justification of tol: truncation perturbs Omega by O(|c_N|) and M, s by
     O(|c_N| * ||H|| ) <~ 1e-12 * 1e4 = 1e-8 worst case, in practice O(c_N^2);
     roundoff ~ eps * ||H|| * cond ~ 1e-16 * 1e4 = 1e-12.
  P1 (claim):  |M - (2/kappa)(4-s)| <= tol, tol = 1e-8 * max(1, (2/kappa)(4-s)), at N=40 and N=60.
  P2 (stability): |M(N=40) - M(N=60)| <= tol.
  P3 (falsification control): |M - (1/kappa)(4-s)| > 1e-3 (wrong coefficient must FAIL the identity).
Exit 0 iff all P0..P3 hold for all 12 parameter points.
"""
import os, sys

def build(kappa, lam, N):
    d = [(2.0 / kappa) * n * (n + 2) + lam for n in range(N + 1)]
    e = [-lam / 2.0] * N
    return d, e

def sturm_count(d, e, x):
    # number of eigenvalues < x
    cnt, q = 0, 1.0
    for i in range(len(d)):
        q = d[i] - x - (e[i - 1] ** 2 / q if i > 0 else 0.0)
        if q == 0.0:
            q = 1e-300
        if q < 0:
            cnt += 1
    return cnt

def lowest_eig(d, e):
    lo = min(d[i] - (abs(e[i - 1]) if i > 0 else 0) - (abs(e[i]) if i < len(e) else 0) for i in range(len(d)))
    hi = d[0] + 1.0
    for _ in range(300):
        mid = 0.5 * (lo + hi)
        if mid == lo or mid == hi:
            break
        if sturm_count(d, e, mid) >= 1:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)

def tri_solve(d, e, shift, b):
    n = len(d)
    a = [d[i] - shift for i in range(n)]
    c = list(e)
    cp, bp = [0.0] * n, [0.0] * n
    den = a[0] if a[0] != 0 else 1e-300
    cp[0] = c[0] / den if n > 1 else 0.0
    bp[0] = b[0] / den
    for i in range(1, n):
        den = a[i] - e[i - 1] * cp[i - 1]
        if den == 0:
            den = 1e-300
        cp[i] = c[i] / den if i < n - 1 else 0.0
        bp[i] = (b[i] - e[i - 1] * bp[i - 1]) / den
    x = [0.0] * n
    x[-1] = bp[-1]
    for i in range(n - 2, -1, -1):
        x[i] = bp[i] - cp[i] * x[i + 1]
    return x

def normalize(v):
    nr = sum(x * x for x in v) ** 0.5
    return [x / nr for x in v]

def matvec_tri(d, e, v):
    n = len(v)
    out = [d[i] * v[i] for i in range(n)]
    for i in range(n - 1):
        out[i] += e[i] * v[i + 1]
        out[i + 1] += e[i] * v[i]
    return out

def Fmul(v):
    n = len(v)
    return [(v[i - 1] if i > 0 else 0.0) + (v[i + 1] if i < n - 1 else 0.0) for i in range(n)]

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def analyse(kappa, lam, N):
    d, e = build(kappa, lam, N)
    E = lowest_eig(d, e)
    v = normalize([1.0] * (N + 1))
    for _ in range(6):
        v = normalize(tri_solve(d, e, E - 1e-10 * max(1.0, abs(E)), v))
    if v[0] < 0:
        v = [-x for x in v]
    E0 = dot(v, matvec_tri(d, e, v))  # Rayleigh quotient
    Fv = Fmul(v)
    meanF = dot(v, Fv)
    s = dot(Fv, Fv)                    # <Omega,F^2 Omega>
    w = [Fv[i] - meanF * v[i] for i in range(N + 1)]
    M = dot(w, matvec_tri(d, e, w)) - E0 * dot(w, w)
    resid = max(abs(x - E0 * y) for x, y in zip(matvec_tri(d, e, v), v))
    return dict(E0=E0, s=s, M=M, cN=abs(v[-1]), resid=resid)

def main():
    here = os.path.dirname(os.path.abspath(__file__))
    name = "results.txt"; k = 1
    while os.path.exists(os.path.join(here, name)):
        k += 1; name = "results_%d.txt" % k
    lines = []
    ok_all = True
    hdr = "%5s %6s %3s %20s %20s %20s %10s %10s %3s %3s %3s %3s" % (
        "kappa", "lambda", "N", "s", "M", "(2/k)(4-s)", "diff", "|c_N|", "P0", "P1", "P2", "P3")
    lines.append(hdr)
    for kappa in (0.5, 1.0, 2.0):
        for lam in (0.1, 1.0, 10.0, 100.0):
            r40 = analyse(kappa, lam, 40)
            r60 = analyse(kappa, lam, 60)
            for N, r in ((40, r40), (60, r60)):
                pred = (2 / kappa) * (4 - r["s"])
                wrong = (1 / kappa) * (4 - r["s"])
                tol = 1e-8 * max(1.0, pred)
                diff = r["M"] - pred
                P0 = r40["cN"] < 1e-12
                P1 = abs(diff) <= tol
                P2 = abs(r40["M"] - r60["M"]) <= tol
                P3 = abs(r["M"] - wrong) > 1e-3
                ok_all &= P0 and P1 and P2 and P3
                f = lambda b: "ok" if b else "FAIL"
                lines.append("%5.1f %6.1f %3d %20.15f %20.15f %20.15f %10.2e %10.2e %3s %3s %3s %3s   wrong(1/k)(4-s)=%.12f diff_wrong=%.3e resid=%.1e" % (
                    kappa, lam, N, r["s"], r["M"], pred, diff, r["cN"], f(P0), f(P1), f(P2), f(P3),
                    wrong, r["M"] - wrong, r["resid"]))
    lines.append("ALL PREDICATES: %s" % ("PASS" if ok_all else "FAIL"))
    txt = "\n".join(lines) + "\n"
    with open(os.path.join(here, name), "w") as fh:
        fh.write(txt)
    print(txt)
    print("wrote", name)
    sys.exit(0 if ok_all else 1)

if __name__ == "__main__":
    main()
