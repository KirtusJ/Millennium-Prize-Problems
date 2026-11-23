# notes.md — worker n1-lemF (task T134)
Step 0: control.txt = 0.272341 (-ln tanh 1). Lean READY exists. Register pcp/ initialised (method not found: expected).
Step 1: read TUNNEL_THEOREM.md, eps_eff.py. Plan: Schur/Barta test with psi=exp(-beta alpha rho^2/2), alpha=2s sqrt(1+s^2), A=1+2s^2+alpha=e^{2asinh s};
 key reductions: (i) s<s0 trivial since ||F||<=1 and 2asinh(s)<=2s; (ii) interior r<=tau: AM-GM + decreasing I0 envelope -> flat Gaussian identity (1/A) * E[G];
 (iii) outer r>=tau: I0<=e^z + weak duality on circle -> Phi(r) <= -(r^2/64)(1-1/A^2)^2.
Step 2: child admitted T138, PROMPT written, child-run1 launched in background 20:27:31
Step 3: wrote check_lemF.py (predicates Q1-Q8 in docstring before first run); smoke tests of the Bessel helper only (not of predicates); reduced rho grid for speed (in docstring).
Step 4: check_lemF run1 exit 1: ZeroDivision at beta=64 (tau=1/4 outside hypothesis tau<1/5): my program defect. Q1-Q4 printed fine before crash (Q4 worst Phi-bound = -1.6e-8). Patched tau=min(beta^-1/3,0.15), run2.
Step 5: LemmaF.lean (L1 2arsinh=log A, L2 fixed point, L3 weak duality, L4 AM-GM pair, L5 quad step) passes: exit 0, axioms propext/Classical.choice/Quot.sound, no sorry. First attempt of L1 failed (proof script), fixed.
Step 6: child-run1 exit 0 (370 s). Child control 1.130318 = correct (2 I1(1)). T138 released. Grandchild T139 (per child).
Step 7: check_lemF run2 exit 0, 102 met 0 failed. Child barta.py rerun by me (K5) exit 0. Master bound valid but weak at accessible beta (deficit 6.5-14 at beta<=4096).
Step 8: LEMMA_F.md and report.md written; registers verify PASS (both).
