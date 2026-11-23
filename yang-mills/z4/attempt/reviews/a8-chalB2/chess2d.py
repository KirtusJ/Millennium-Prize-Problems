"""chess2d.py -- exact test of Lemma 2 (chessboard, all images in reflection planes) in d=2.

In d=2 on an LxL periodic torus (L=2,4) every plaquette lies in site reflection planes, and the
chessboard images of p0 under the dyadic reflection group are all N=L^2 plaquettes, each hit once.
Lemma 2 then asserts   P(O_p0 > t) <= Z_all(t)^(1/N),   Z_all(t) := mu(all plaquettes have O_p > t).
Exact formulas (torus = genus 1, character expansion):
  U(1):  Z = sum_n w_n^N,   w_n = int w(th) cos(n th) dth/2pi
  SU(2): Z = sum_j (c_j/d_j)^N, c_j = int w chi_j dU, d_j=2j+1, Haar class density (2/pi) sin^2 a.
  P(O_p0>t) = sum w'_n w_n^(N-1) / Z ;  Z_all = sum w'_n^N / Z, with w' = w*1{O>t}.
Quadrature: 20000-point midpoint rule on [0,pi] (integrands smooth except the indicator jump,
error O(1/20000) relative) ; character sums truncated at |n|,j <= 200 (terms decay like I_n(beta)).

PREDICATES (fixed before first run):
 P1 (for all beta in {1,2,4,8,16}, t in {0.5,1,2,4,8}, L in {2,4}, G in {U1,SU2}):
     P_true <= Zall^(1/N) * (1+1e-6)     [tolerance: quadrature/truncation, see above]
 P2 per case: Zall^(1/N) <= exp(D - t/8) is NOT tested here (D is the d=4 constant); measured only:
     ratio r = log(Zall^(1/N)) / log(P_true)  (r<=1 means the bound is weaker than the truth).
 P3 sanity: sum over characters gives Z>0 and 0<=P_true<=1 for all cases.
Output: chess2d_results.txt (mode 'x').
"""
import numpy as np, sys
M = 20000
a = (np.arange(M) + 0.5) * np.pi / M
da = np.pi / M
out = open(sys.argv[1] if len(sys.argv) > 1 else "chess2d_results.txt", "x")
fails = []; n_cases = 0; n_met = 0
for G in ("U1", "SU2"):
    for L in (2, 4):
        N = L * L
        for beta in (1, 2, 4, 8, 16):
            w = np.exp(-beta * (1 - np.cos(a)))
            if G == "U1":
                # theta in [-pi,pi], symmetric: int dth/2pi = (1/pi) int_0^pi
                meas = da / np.pi * np.ones(M)
                chars = [np.cos(n * a) for n in range(0, 201)]
                mult = [1] + [2] * 200  # n and -n
                dims = [1] * 201
            else:
                meas = da * (2 / np.pi) * np.sin(a) ** 2
                chars = [np.sin((2 * j + 1) * a) / np.sin(a) for j in range(0, 201)]
                mult = [1] * 201
                dims = [2 * j + 1 for j in range(0, 201)]
            for t in (0.5, 1, 2, 4, 8):
                ind = (beta * (1 - np.cos(a)) > t).astype(float)
                cw = np.array([np.sum(meas * w * c) for c in chars]) / np.array(dims)
                cw2 = np.array([np.sum(meas * w * ind * c) for c in chars]) / np.array(dims)
                mlt = np.array(mult, float)
                Z = np.sum(mlt * cw ** N)
                Zall = np.sum(mlt * cw2 ** N) / Z
                P = np.sum(mlt * cw2 * cw ** (N - 1)) / Z
                n_cases += 1
                ok3 = Z > 0 and -1e-12 <= P <= 1 + 1e-12 and Zall >= -1e-15
                bound = max(Zall, 0) ** (1.0 / N)
                ok1 = P <= bound * (1 + 1e-6) + 1e-300
                r = np.log(bound) / np.log(P) if 0 < P < 1 and bound > 0 else float('nan')
                line = f"{G} L={L} beta={beta} t={t} P_true={P:.6e} Zall^(1/N)={bound:.6e} r={r:.4f} P1={'met' if ok1 else 'FAILED'} P3={'met' if ok3 else 'FAILED'}"
                print(line, file=out)
                if ok1 and ok3: n_met += 1
                else: fails.append(line)
print(f"SUMMARY cases={n_cases} met={n_met} failed={len(fails)}", file=out)
for f in fails: print("FAIL", f, file=out)
out.close()
print(f"SUMMARY cases={n_cases} met={n_met} failed={len(fails)}")
sys.exit(0 if not fails else 1)
