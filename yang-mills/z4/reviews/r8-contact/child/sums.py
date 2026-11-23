"""cA, cB and G4(0,1,0) via Parseval in the 3D Brillouin zone.

Ghat4(q) = N/sqrt(A(A+4)), GhatH(q) = N/(2 sqrt A), N = kh1^2+kh2^2, A = |kh|^2 (3D).
(k4 integral done analytically; checked numerically in control.py.)
cA = 2 int d^3q/(2pi)^3 Ghat4^2 = 2 <N^2/(A(A+4))>,  cB = 2 <N^2/(4A)>.
G4(0,1,0) = <cos(q2) Ghat4>, G4(0)= <Ghat4>, GH(0) = <GhatH>.
Midpoint grids n = 64, 128, 256 (no q=0 point; integrands bounded).

PREDICATES (fixed before first run):
 Q1 convergence: relative change of cA, cB, G4(0,1,0) between n=128 and n=256
    < 1e-4 (origin: 3 sig figs needs <5e-4; midpoint error for bounded integrand
    with a cusp at q=0 expected O(n^-3) or better).
 Q2 exact ordering cA < cB (origin: sqrt(A(A+4)) >= 2 sqrt(A) since A+4 >= 4,
    so Ghat4 <= GhatH pointwise).
 Q3 |G4(0) - 0.5| < 1e-4 at n=256 (origin: control, exact symmetry value).
 Q4 Parseval cross-check at n=64: discrete FFT of Ghat4 on the grid gives G4(r)
    on a 64^3 periodic box; 2*sum_r G4(r)^2 equals cA(n=64) to rel 1e-10
    (origin: discrete Parseval is exact up to rounding), and G4(0,1,0) from the
    FFT equals the direct cosine sum to 1e-12.
No randomness. Writes sums_result_<timestamp>.txt (never overwrites).
"""
import numpy as np, os, time, sys

ok = True
def pred(name, cond, msg):
    global ok
    print(("PASS " if cond else "FAIL ") + name + ": " + msg)
    ok &= bool(cond)

def mid(n):
    return -np.pi + (np.arange(n) + 0.5) * 2 * np.pi / n

def compute(n):
    q = mid(n)
    kh2 = 4 * np.sin(q / 2) ** 2
    c2 = np.cos(q)
    sA = sB = s010 = s0 = sH0 = 0.0
    for i in range(n):  # axis 0 = q1
        A = kh2[i] + kh2[:, None] + kh2[None, :]
        N = kh2[i] + kh2[:, None] + 0 * kh2[None, :]
        g4 = N / np.sqrt(A * (A + 4))
        gh = N / (2 * np.sqrt(A))
        sA += (g4 ** 2).sum(); sB += (gh ** 2).sum()
        s010 += (c2[:, None] * g4).sum()  # axis 1 = q2
        s0 += g4.sum(); sH0 += gh.sum()
    V = n ** 3
    return dict(cA=2 * sA / V, cB=2 * sB / V, G010=s010 / V, G0=s0 / V, GH0=sH0 / V)

res = {}
for n in (64, 128, 256):
    t = time.time()
    res[n] = compute(n)
    print(n, {k: f"{v:.10f}" for k, v in res[n].items()}, f"{time.time()-t:.1f}s")

r1, r2 = res[128], res[256]
rel = {k: abs(r2[k] / r1[k] - 1) for k in ("cA", "cB", "G010")}
pred("Q1", max(rel.values()) < 1e-4, "rel change 128->256: " + ", ".join(f"{k}={v:.2e}" for k, v in rel.items()))
pred("Q2", r2["cA"] < r2["cB"], f"cA={r2['cA']:.8f} < cB={r2['cB']:.8f}")
pred("Q3", abs(r2["G0"] - 0.5) < 1e-4, f"G4(0)={r2['G0']:.10f}")

# Q4 FFT Parseval
n = 64
q = mid(n); kh2 = 4 * np.sin(q / 2) ** 2
A = kh2[:, None, None] + kh2[None, :, None] + kh2[None, None, :]
N = kh2[:, None, None] + kh2[None, :, None]
g4hat = N / np.sqrt(A * (A + 4))
# G(r) = (1/n^3) sum_q e^{i q r} ghat(q); with midpoint offset q = -pi+(j+1/2)h the phase
# e^{i(-pi+h/2) r} has unit modulus so |G(r)| and sum G^2 are unaffected; use full complex.
r = np.arange(n)
ph = np.exp(1j * q[:, None] * r[None, :])  # 1D transform matrices
G = np.einsum("ia,jb,kc,ijk->abc", ph, ph, ph, g4hat, optimize=True) / n ** 3
cA_fft = 2 * np.sum(np.abs(G) ** 2)
G010_fft = G[0, 1, 0].real
pred("Q4", abs(cA_fft / res[64]["cA"] - 1) < 1e-10 and abs(G010_fft - res[64]["G010"]) < 1e-12
     and abs(G[0, 1, 0].imag) < 1e-12,
     f"cA_fft={cA_fft:.12f} vs {res[64]['cA']:.12f}; G010_fft={G010_fft:.12f} vs {res[64]['G010']:.12f}")

fn = f"sums_result_{time.strftime('%Y%m%d_%H%M%S')}.txt"
assert not os.path.exists(fn)
with open(fn, "x") as f:
    for n in res:
        f.write(f"n={n}: " + ", ".join(f"{k}={v:.12f}" for k, v in res[n].items()) + "\n")
    f.write(f"cA/cB (n=256) = {r2['cA']/r2['cB']:.10f}\nrel change 128->256: {rel}\nall_pass: {ok}\n")
print(f"cA/cB = {r2['cA']/r2['cB']:.8f}")
print("wrote", fn)
sys.exit(0 if ok else 1)
