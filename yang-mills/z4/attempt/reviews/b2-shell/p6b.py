"""p6b.py -- follow-up to P6 (b2-shell). Predicates fixed before run:
Q1 W(N)/N^2 -> L = (1/3) int_0^{1/2} u^2 cosh(u-1/2)/cosh(1/2) du  (kernel limit of (1/(3N^3)) sum r^2 k_s(r)),
   with |W/N^2 - L| * N bounded (<= 1) for N=16..1024 and decreasing error.
Q2 L > 0.  Integral by composite Simpson, 2000 panels, decimal 40 digits (error << 1e-12; tolerance 1e-10 on L).
Output results_p6b.txt (mode x)."""
from decimal import Decimal as D, getcontext
import sys
getcontext().prec = 40
out = open("results_p6b.txt", "x"); fails = []
def log(s): print(s); out.write(s + "\n")
one = D(1); h = one/2
cosh = lambda x: (x.exp() + (-x).exp())/2
n = 2000; a, b = D(0), h; dx = (b-a)/n
f = lambda u: u*u*cosh(u-h)/cosh(h)
S = f(a) + f(b) + sum((4 if i % 2 else 2)*f(a+i*dx) for i in range(1, n))
L = S*dx/3/3
log(f"L = {L:.12f}")
if not L > 0: fails.append("Q2")
q = (-one).exp(); prev = None; ok = True
for N in (16, 32, 64, 128, 256, 512, 1024):
    s = (-one/N).exp(); k = lambda a_, r: (a_**r + a_**(N-r))/(1+a_**N)
    W = sum(r*r*(k(s, r) + 2*k(q, r)) for r in range(1, N//2+1))/(3*N)
    err = abs(W/N/N - L)
    log(f"N={N} W/N^2={W/N/N:.8f} err*N={err*N:.5f}")
    ok = ok and err*N <= 1 and (prev is None or err < prev); prev = err
log(("MET" if ok else "FAILED") + " Q1"); log(("MET" if "Q2" not in fails else "FAILED") + " Q2")
if not ok: fails.append("Q1")
out.close(); sys.exit(1 if fails else 0)
