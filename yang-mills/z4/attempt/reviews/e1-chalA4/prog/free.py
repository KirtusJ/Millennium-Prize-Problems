"""Own free-field computation (independent of the child's midpoint quadrature).
(a) infinite volume c(m) = C(0; m e1) by Gauss-Legendre in the 3D (time-integrated) form, two meshes 48/64 nodes/axis
    after the substitution for the 1/|q| singularity being integrable (tolerance = mesh difference);
(b) 8^4 torus values (exact finite sums, p=0 mode omitted = projection onto exact cochains on the torus),
    for comparison with mc.py (times 3 colours, measured only).
PREDICATES (fixed before first run):
 F1: |c_inf(0) - 1/2| <= 1e-4 (control; tolerance = generous vs mesh difference).
 F2: |c_inf(1) - (-0.0688747)| <= max(1e-5, 10*meshdiff)  (child's value, rerun check).
 F3: X_inf(1) = 2c(2)+c(1)+c(3) < 0 and torus X_8(d) <= 0 for d=1,2,3.
"""
import numpy as np, sys
from numpy.polynomial.legendre import leggauss
def cinf(n):
    x, w = leggauss(n); q = np.pi*x; w = np.pi*w
    h = 2*np.sin(q/2)
    a, b, c = np.meshgrid(h*h, h*h, h*h, indexing="ij")
    r = np.sqrt(a+b+c); om = 2*np.arcsinh(r/2)
    amp = (a+b)/(2*np.sinh(om))
    W = w[:, None, None]*w[None, :, None]*w[None, None, :]
    return np.array([np.sum(W*amp*np.cos(m*q)[:, None, None])/(2*np.pi)**3 for m in range(12)])
cA, cB = cinf(48), cinf(64); md = np.abs(cA-cB).max()
N = 8; p = 2*np.pi*np.arange(N)/N; h2 = 4*np.sin(p/2)**2
H = [h2[(slice(None),)+(None,)*k+(slice(None) if False else None,)*0] for k in range(1)]
h0, h1, h2_, h3 = np.meshgrid(h2, h2, h2, h2, indexing="ij")
den = h0+h1+h2_+h3; den[0, 0, 0, 0] = 1.0
sym = (h1+h2_)/den; sym[0, 0, 0, 0] = 0.0
ct = np.real(np.fft.ifftn(sym))  # C(x) on torus, index [x0,x1,x2,x3]
c8 = ct[0, :, 0, 0]
X = lambda c, d: 2*c[(2*d) % len(c)]+c[(2*d-1) % len(c)]+c[(2*d+1) % len(c)]
lines = [f"mesh diff {md:.2e}", "c_inf: " + " ".join(f"{v:.7f}" for v in cB[:9]),
         "c_torus8: " + " ".join(f"{v:.7f}" for v in c8)]
lines.append("X_inf(d=1..3): " + " ".join(f"{X(cB,d):.6f}" for d in (1, 2, 3)))
lines.append("X_torus8(d=1..3): " + " ".join(f"{X(c8,d):.6f}" for d in (1, 2, 3)))
VD8 = 2*c8[0]+2*c8[1]
lines.append(f"torus8 x3 colours: E D.D'(d=1..3) " + " ".join(f"{3*X(c8,d):.4f}" for d in (1,2,3)) + f"; E|D|^2 {3*VD8:.4f}")
ms = [3*sum(c8[(u-v) % N] for u in range(L) for v in range(L))/L**2 for L in (2, 4, 8)]
lines.append("torus8 x3 colours MS(L=2,4,8): " + " ".join(f"{v:.4f}" for v in ms))
msinf = [sum(cB[abs(u-v)] if abs(u-v) < 12 else 0 for u in range(L) for v in range(L))/L**2 for L in (2, 4, 8)]
F1 = abs(cB[0]-.5) <= 1e-4; F2 = abs(cB[1]+0.0688747) <= max(1e-5, 10*md)
F3 = X(cB, 1) < 0 and all(X(c8, d) <= 0 for d in (1, 2, 3))
lines.append(f"F1 {'MET' if F1 else 'FAILED'} c(0)={cB[0]:.8f}; F2 {'MET' if F2 else 'FAILED'} c(1)={cB[1]:.8f}; F3 {'MET' if F3 else 'FAILED'}")
open("../results/free.txt", "x").write("\n".join(lines)+"\n"); print("\n".join(lines))
sys.exit(0 if F1 and F2 and F3 else 1)
