# notes r11-flowbounds
Step 0: control.txt = 0.272341 (-ln tanh 1). Lean: /home/user/z4-lean/READY absent at start -> no Lean claims unless it appears.
Step 1: register pcp initialised.
Step 2: child started (child-run1) 09:57:53; delegated: C_{b,s}(0), M1/M0 at N=16,32, s=0.005, my f.
Step 3: proof plan (details in report):
 - B1 upper: AM-GM a(k)a(k') <= (a(k)^2+a(k')^2)/2 + Parseval sum_q|fhat_b(q)|^2 = l^3 b^3 sum f(bx)^2
   => C_{b,s}(t) <= (2/l^3) Phi_b sum_k a(k)^2 (a = w e^{-t khat/... } e^{-2s khat^2}). Gives s^{-5/2} scaling (the sup|fhat| route of r9 gives only s^{-4}).
   khat in [(2/pi)|k|,|k|] -> sum a^2 <= (pi^2/l^2) sum_n |n|^2 e^{-64 s |n|^2/l^2}; theta-function bounds.
 - B1 lower: v1 = r9's 4-mode bound times e^{-16 pi^2 s/l^2}; v2 = keep ALL pairs (k,-k) with |n|_inf<=M<=(N-1)/2 -> ~ s^{-5/2}.
 - B3: M1 <= (4/l^3)Phi sqrt(A0 A2), M2 <= (4/l^3)Phi(sqrt(A0A4)+A2) (weighted AM-GM), / v2 -> s^{-1/2}, s^{-1}.
 - B2: mean value on phi(p)=(p1^2+p2^2)/(2|p|) e^{-t|p|-2s|p|^2}, |grad phi|<=(3/2+|p|(t+4s|p|)/2)E, |khat-k|<=b^2|k|^3/24,
   aliasing for q in BZ, Gaussian tail e^{-s/b^2}<=b^2/(e s) for pairs with k+k' outside BZ or k outside BZ.
Step 4: smoke run (N<=16, registered smoke-N16): all predicates met (P0 rel 1e-15; P1 18/18; P1b 9/9; P2 6/6; P3 18/18; P5 met:
 R(s)=0.4950,0.8783,0.9390,0.9663,0.9821,0.9907 for s=.02..2.5e-4, deviation halves with s -> claimed constant stands).
 K of B2 is valid but loose by ~1e9 (tail term b^2/(es) and sup|ftilde|). Added P3b Parseval form K1 b^2 + K2 e^{-s/b^2} before main run.
Step 5: main run run1 (main-N128, N=8..128): P0 2/0, P1 45/0, P1b 36/0, P1c 45/0, P2 15/0, P3 45/0, P3b 45/0, P4_err 18/0 (ratios 4.004-4.077), P4_diff 9/0 (4.018-4.096), P5 1/0.
Step 6: child control 6.2429 graded CORRECT before reading output. Child values C0(N16)=574.6795784, M1/M0=21.9566923; N32 542.7336836, 21.7118326 = mine to all digits. Grandchild: finite-difference M1/M0 at N16 (fwd3 h=1e-4: 21.95669218). Child program rerun in rerun_child/ (check child-rerun).
Step 7: Lean R11Flow.lean (6 theorems) exit 0, standard axioms only, no sorry (one failed compile before: two tactic errors, fixed).
Step 8: report.md written; registers verified.
