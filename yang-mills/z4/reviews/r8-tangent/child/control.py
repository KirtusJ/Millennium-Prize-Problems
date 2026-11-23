"""STEP 0 control: 4D simple-cubic lattice Green function at origin.

Method: Schwinger representation 1/F = int_0^inf exp(-tF) dt, which factorises:
  G(0) = int_0^inf a(t)^4 dt,  a(t) = (1/2pi) int dk exp(-t(2-2cos k)) = e^{-2t} I0(2t).
a(t) computed by periodic trapezoid rule in k (M=8192 points, spectrally accurate for t<=T).
t-integral: substitution t=e^u, trapezoid in u on [-14, ln T], T=2e4, 6000 nodes.
Tail t>T: a(t)~(4 pi t)^{-1/2}(1+1/(16t)+...) -> tail = 1/(16 pi^2 T) * (1 + 1/(8T)) approx.
Cross-check: direct midpoint quadrature on n^4 grid (offset by half-step), n=48,64 (O(h^2) error).

PREDICATE (fixed before first run): |G_schwinger - 0.15493339| < 2e-6 -> exit 0, else exit 1.
Writes control.txt (refuses to overwrite).
"""
import os, sys, numpy as np

OUT = "control.txt"
if os.path.exists(OUT):
    print("control.txt exists; refusing to overwrite"); sys.exit(2)

M = 8192
k = 2*np.pi*np.arange(M)/M
f = 2-2*np.cos(k)
T = 2e4
u = np.linspace(-14, np.log(T), 6000)
t = np.exp(u)
a = np.array([np.mean(np.exp(-ti*f)) for ti in t])
integrand = a**4 * t
G_main = np.trapz(integrand, u) if hasattr(np, "trapz") else np.trapezoid(integrand, u)
tail = 1/(16*np.pi**2*T)*(1+1/(8*T))
G = G_main + tail

def midpoint(n):
    kk = 2*np.pi*(np.arange(n)+0.5)/n - np.pi
    ff = 2-2*np.cos(kk)
    s = 0.0
    for f1 in ff:
        F = f1 + ff[:,None,None] + ff[None,:,None] + ff[None,None,:]
        s += np.sum(1.0/F)
    return s/n**4
m48, m64 = midpoint(48), midpoint(64)
lines = [f"G(0) Schwinger/trapezoid = {G:.9f}  (main {G_main:.9f} + tail {tail:.2e}; M={M}, 6000 u-nodes, T={T})",
         f"midpoint n=48: {m48:.7f}  n=64: {m64:.7f}  Richardson(h^2): {(64**2*m64-48**2*m48)/(64**2-48**2):.7f}",
         "known: 0.15493339"]
ok = abs(G-0.15493339) < 2e-6
lines.append(f"PREDICATE |G-0.15493339|<2e-6: {'PASS' if ok else 'FAIL'}")
open(OUT, "w").write("\n".join(lines)+"\n")
print("\n".join(lines))
sys.exit(0 if ok else 1)
