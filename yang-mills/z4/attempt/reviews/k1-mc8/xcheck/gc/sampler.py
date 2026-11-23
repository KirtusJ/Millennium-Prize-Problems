import numpy as np, sys

def kp_a0(k, n, rng):
    """Kennedy-Pendleton: a0 ~ sqrt(1-a0^2) exp(k a0) on [-1,1]. Exact."""
    out = np.empty(0)
    while out.size < n:
        m = int((n - out.size) * 1.5) + 100
        r1, r2, r3, r4 = (1.0 - rng.random(m) for _ in range(4))  # in (0,1]
        x = -(np.log(r1) + np.cos(2*np.pi*r2)**2 * np.log(r3)) / k
        ok = r4**2 <= 1.0 - x/2.0
        out = np.concatenate([out, 1.0 - x[ok]])
    return out[:n]

def bessel_int(n, k, M=4000):
    th = np.linspace(0, np.pi, M+1)
    f = np.exp(k*np.cos(th))*np.cos(n*th)
    h = np.pi/M
    simp = h/3*(f[0]+f[-1]+4*f[1:-1:2].sum()+2*f[2:-1:2].sum())
    return simp/np.pi

def ratio_direct(k, N=2000):
    # Gauss-Chebyshev 2nd kind: int sqrt(1-x^2) g(x) dx = sum w_i g(x_i)
    i = np.arange(1, N+1)
    x = np.cos(i*np.pi/(N+1)); w = np.pi/(N+1)*np.sin(i*np.pi/(N+1))**2
    g = np.exp(k*x)
    return (w*x*g).sum()/(w*g).sum()

if __name__ == "__main__":
    k, n, seed = 3.0, 400000, 12345
    a0 = kp_a0(k, n, np.random.default_rng(seed))
    mean = a0.mean(); se = a0.std(ddof=1)/np.sqrt(n)
    q1 = bessel_int(2, k)/bessel_int(1, k)
    q2 = ratio_direct(k)
    z = (mean-q2)/se
    p1 = abs(mean-q1) < 4*se and abs(mean-q2) < 4*se
    p2 = abs(q1-q2) < 1e-8
    lines = [f"# SU(2) heat-bath check, k={k}, n={n}, seed={seed}",
             f"- sample mean a0 = {mean:.8f}", f"- standard error = {se:.8f}",
             f"- I2/I1 (Simpson Bessel integrals) = {q1:.12f}",
             f"- direct quadrature ratio (Gauss-Chebyshev II) = {q2:.12f}",
             f"- z = (mean - quad)/SE = {z:.3f}",
             f"- |quad1-quad2| = {abs(q1-q2):.2e}",
             f"- predicate 4 SE: {'PASS' if p1 else 'FAIL'}",
             f"- predicate quadratures agree 1e-8: {'PASS' if p2 else 'FAIL'}",
             f"- OVERALL: {'PASS' if (p1 and p2) else 'FAIL'}"]
    txt = "\n".join(lines)+"\n"
    print(txt)
    with open("result.md", "x") as fh: fh.write(txt)
