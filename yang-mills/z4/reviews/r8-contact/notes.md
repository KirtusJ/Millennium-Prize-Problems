# notes (challenger r8-contact)
Step 0: control.txt = 0.272341 (-ln tanh 1).
Step 1: read input. Key observations:
- A4 O_b = (beta/b) sum_{spatial p at t} f_ij(center)(1-x_p), x_p = TrU_p/2. Prefactor beta/b, face-center sampling, no b^3 (b^3 implicit: beta/b * b^4 B^2).
- "loses": lower bound on variance REMOVED (Var O - Var Otilde >= D_b) and on prediction error from exterior; NOT a bound on Var itself except trivially Var >= D_b.
- 1/18 = (1/36)*(row sums)^2 for single orientation f_12 = f: rows i=1,2 give f, i=3 gives 0 -> 2||f||^2/36.
- Bench "C_b(0) b^5 -> 8.110e-3" is c*int f^2 for an f NOT specified in STATEMENT.md (two widths, ratio 8). So c alone is not recoverable from the text: missing convention. I compute c directly as c = 2 sum_r G(r)^2.
Step 2 (K2 conversion): beta(1-x_p) = sum_a theta_a^2/(2g^2)+O(g^2) => A4 O_b = (1/2) b^3 sum f(bx) sum_a (B_3^a)^2 = (1/2) sum_a O_bench,a.
 Free total coefficient of b^-5 int f^2: T = (3/4) c, c = 2 sum_r G(r)^2.
 4D lattice: Ghat4(q) = (qh1^2+qh2^2)/(qh sqrt(qh^2+4)); Hamiltonian: (qh1^2+qh2^2)/(2qh).
 Free removable (exact Gaussian conditioning on exterior of A4's mask): per masked link E Var = 4 s2 E(thb_p-thb_p')^2 + 8 s2^2, s2=g^2/6.
Step 3 (k2_free.py, check K1, exit 0): c4=0.56258, cH=1.45682, c4/cH=0.386. T=0.4219 (4D), 1.0926 (Hamiltonian analogue).
 Free removable R=0.13407 = radial 0.05556 (= A4's 1/18 exactly) + transverse 0.07851. 1/18 = 0.415 R = 0.132 T. 7 met, 0 failed.
 Bench back-out: cH * (pi*0.1^2)^{3/2} = 0.008112 vs bench 8.110e-3 -> consistent with a Gaussian of sigma=0.1 (INFERRED; f not stated in bench text).
Step 4 (K3): P_M O(t) depends on spatial links at t-1,t,t+1 and temporal links between; O(t+n) only on spatial links at t+n. Single replacement valid for all n != 0; double replacement needs n>=2. n=1 of Otilde generally changed. 2b -> 0 physically.
Step 5 (K4): 4^4, beta=2.2 checks the conditional variance identity (3.706 vs 2.063+1.622=3.685, residual 0.021+-0.043) and C(2) preservation (0.00031+-0.041: SE 100x the signal, uninformative). No asymptotic content.
Step 6 (K5): the quoted sentence "can still vanish, remain finite, or require further normalization" is NOT in the supplied files (grep). Nearest: README l.7.
Step 7: child rerun K2,K3 exit 0, identical; verify PASS; report.md written.
