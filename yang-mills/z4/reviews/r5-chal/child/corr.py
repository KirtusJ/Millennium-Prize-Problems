"""corr.py -- C(t) = <O(f) e^{-tH} O(f)> by direct 2D quadrature, and extraction of
the short- and long-time power laws from the numerics (local log-slopes).

Formula used (derived in notes.md, Wick + derived G, verified by twopoint_check.py and,
independently in momentum space, by mc_check.py):
  C(t) = 2 Int d^3x F(x) G(x,t)^2,  F(x) = pi^{3/2} exp(-r^2/4),
  G = (t^2 + r^2 (2c^2 - 1)) / (pi^2 (r^2+t^2)^3),  c = cos(angle to e3).
  => C(t) = 4 pi^{5/2} Int_0^inf dr r^2 e^{-r^2/4} Int_{-1}^{1} dc G^2   (numerical, mpmath).
Local slope s(t) = d ln C / d ln t by central difference, step h = 1e-3 in ln t.

PREDICATES (fixed before first run):
 P0a (short-time power): -s(1e-3) and -s(1e-4) are each within 1e-3 of the same integer,
     and |s(1e-3) - s(1e-4)| < 1e-3.  p0 := that integer.
 P0b (short-time amplitude): |C(1e-4) * (1e-4)^p0 / A0_closed - 1| < 1e-4, A0_closed = 1/(10 sqrt(pi)).
 Pinfa (long-time power): same as P0a at t = 1e3 and 1e4.  pinf := that integer.
 Pinfb (long-time amplitude): |C(1e4) * (1e4)^pinf / Ainf_closed - 1| < 1e-4, Ainf_closed = 16/pi.
Tolerance source: the leading power laws come from Taylor-expanding a smooth even function
(F around x=0 for t->0; G in x^2/t^2 for t->inf), so corrections are relative O(t^2)
resp. O(<r^2>_F / t^2) ~ O(10/t^2): <= ~1e-6 at the chosen t. Central-difference error
for a near-pure power is O(h^2 * correction) ~ negligible; mpmath quad at dps=30 is ~1e-20.
1e-3 (slope) and 1e-4 (amplitude) thus leave >=100x margin while still excluding any
neighbouring integer/half-integer power or O(1) normalization error.
Exit 0 iff all four pass, else 1. Results appended to a NEW file (never overwritten).
"""
import os, sys
import mpmath as mp

mp.mp.dps = 30
PI = mp.pi

def C(t):
    t = mp.mpf(t)
    def inner(r):
        num0 = t*t
        den = PI**2 * (r*r + t*t)**3
        return mp.quad(lambda c: ((num0 + r*r*(2*c*c - 1)) / den)**2, [-1, 0, 1])
    pts = sorted(set([mp.mpf(0)] + [t*k for k in (0.5, 1, 2, 5, 20, 100)] + [mp.mpf(v) for v in (1, 3, 6, 12, 25)]))
    pts = [p for p in pts if p <= 25] + [mp.inf]
    val = mp.quad(lambda r: r*r * mp.exp(-r*r/4) * inner(r), pts)
    return 4 * PI**mp.mpf(2.5) * val

def slope(t, h=mp.mpf('1e-3')):
    lt = mp.log(t)
    return (mp.log(C(mp.exp(lt + h))) - mp.log(C(mp.exp(lt - h)))) / (2*h)

A0c = 1 / (10*mp.sqrt(PI)); Ainfc = 16 / PI
lines = []
def out(s):
    print(s); lines.append(s)

out("t, C(t), local slope")
for e in range(-4, 5):
    t = mp.mpf(10)**e
    out(f"t=1e{e:+d}  C={mp.nstr(C(t), 15)}  s={mp.nstr(slope(t), 10)}")

def power_pred(ta, tb, label):
    sa, sb = slope(mp.mpf(ta)), slope(mp.mpf(tb))
    na, nb = mp.nint(-sa), mp.nint(-sb)
    ok = abs(-sa - na) < 1e-3 and abs(-sb - nb) < 1e-3 and na == nb and abs(sa - sb) < 1e-3
    out(f"{label}: -s({ta})={mp.nstr(-sa,12)}  -s({tb})={mp.nstr(-sb,12)}  -> {'PASS' if ok else 'FAIL'} (p={int(na)})")
    return ok, int(na)

ok0a, p0 = power_pred('1e-3', '1e-4', 'P0a')
t = mp.mpf('1e-4'); A0n = C(t) * t**p0
ok0b = abs(A0n / A0c - 1) < 1e-4
out(f"P0b: A0_num={mp.nstr(A0n,15)}  A0_closed=1/(10 sqrt pi)={mp.nstr(A0c,15)}  rel={mp.nstr(abs(A0n/A0c-1),3)} -> {'PASS' if ok0b else 'FAIL'}")
okia, pinf = power_pred('1e3', '1e4', 'Pinfa')
t = mp.mpf('1e4'); Ain = C(t) * t**pinf
okib = abs(Ain / Ainfc - 1) < 1e-4
out(f"Pinfb: Ainf_num={mp.nstr(Ain,15)}  Ainf_closed=16/pi={mp.nstr(Ainfc,15)}  rel={mp.nstr(abs(Ain/Ainfc-1),3)} -> {'PASS' if okib else 'FAIL'}")

allok = ok0a and ok0b and okia and okib
out("ALL: " + ("PASS" if allok else "FAIL"))
here = os.path.dirname(os.path.abspath(__file__))
i = 1
while os.path.exists(os.path.join(here, f"results_corr_{i}.txt")):
    i += 1
with open(os.path.join(here, f"results_corr_{i}.txt"), "x", encoding="utf-8") as fh:
    fh.write("\n".join(lines) + "\n")
sys.exit(0 if allok else 1)
