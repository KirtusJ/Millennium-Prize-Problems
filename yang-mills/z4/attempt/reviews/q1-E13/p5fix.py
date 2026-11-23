"""p5fix.py -- worker q1-E13. Recheck of predicate P5 of e13_bounds.py with the CORRECTED cross-term bound.
Defect found by run4 (P5 FAILED 9/11, E3 side only): I had bounded 2h s_w |p_w b_w|/(1+2h s_w^2) by |p_w||b|, which is false
for h s_w^2 small relative to h s_w (sup_s 2hs/(1+2hs^2) = sqrt(h/2)). Correct: 2hs/(1+2hs^2) <= 1/s, so the cross term is
<= |p_w||b|/s_w = kappa |b|^2/(sqrt(beta) s_w^2).
PREDICATE (fixed before run): P5' -DG3' <= logJflat - logJ <= DG1' at every point of the same tube grid as e13_bounds.py,
beta = 256*4^k, k = 0..10, both E1 and E3 tilts; tolerance 1e-12 (rounding). Output results_p5fix_<tag>.txt, mode "x".
"""
import sys, math, numpy as np, importlib.util
spec = importlib.util.spec_from_file_location('eb', 'e13_bounds.py'); eb = importlib.util.module_from_spec(spec); spec.loader.exec_module(eb)
out = open(f"results_p5fix_{sys.argv[1]}.txt", "x")
nok = nfail = 0; worst = 0.0
for k in range(11):
    beta = 256 * 4 ** k
    for a1 in np.linspace(0.5, math.pi - 0.5, 7):
        for a2 in [0.0, 0.02, 0.06, 0.1, 0.15]:
            for frac in [0.0, 0.5, 0.99]:
                S = math.sqrt(math.sin(a1)**2 + math.sin(a2)**2); wmax = math.sqrt(frac*4*2*S*S/(beta*eb.alpha(S))); den = math.sin(a1)*math.sin(a2)
                if den == 0:
                    if frac > 0: continue
                    chi = 0.0
                else:
                    if wmax > den: continue
                    chi = math.asin(wmax/den)
                U1, U2 = eb.point(a1, a2, chi); w, S = eb.invariants(U1, U2); h = eb.hfun(S); b = math.sqrt(beta)*w; l = eb.lmat(U1, U2)
                b2 = b @ b; sw2 = S*S - 2*(w @ w)
                for wt in (True, False):
                    p = eb.pvec(U1, U2, wt); gap = (-eb.eps(S) + p @ p/2) - ((h-2)*b2 + eb.logJ_det(l, b, p, h))
                    kap = abs(eb.dPsi(a1)*U1[0]/math.sin(a1) + ((eb.dTheta(a2)*U2[0]/math.sin(a2)) if (wt and a2 > 0) else 0))
                    if wt:
                        D = 2*h*b2/(beta*S*S) + kap**2*b2/(2*beta*sw2) + kap*b2/(math.sqrt(beta)*sw2) + 4*h*h*b2*b2/beta
                        ok = gap <= D + 1e-12; r = gap/D if D > 0 else 0
                    else:
                        D = h*(2 + 2/(S*S))*b2/beta + kap*b2/(math.sqrt(beta)*sw2)
                        ok = -gap <= D + 1e-12; r = -gap/D if D > 0 else 0
                    nok += ok; nfail += (not ok); worst = max(worst, r)
s = f"P5' met {nok}, failed {nfail}; max gap/bound = {worst:.3f} {'MET' if nfail == 0 else 'FAILED'}"
print(s); out.write(s + "\n"); out.close(); sys.exit(0 if nfail == 0 else 1)
