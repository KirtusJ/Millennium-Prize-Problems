# notes.md (builder, W1-W4)
Step 0: control.txt = 0.272341 (-ln tanh 1).
Step 1: read README. Convention: U(1) M_r = -N^2 log(I_r(N^2)/I_0(N^2)); SU(2) spin j: M_j = -N^2 log(I_{2j+1}(4N^2)/I_1(4N^2)). To verify against M(64) (hypothesis H).
Observation before computing: with W = (c1/c0)^(R T N^2), -log W/(RT) = -N^2 log(c1/c0) = M_1(N) identically. So sigma_N = M(N): W1 is the README table re-read, not new information. Rate = rate of M.
Step 2: wrote wilson2d.py with predicates H,Q,P1-P6 in docstring; sub-agent launched on Haar-quadrature sigma (child/).
Step 3: wilson2d run K1 (expect 0, got exit 1): met 12, failed 1, measured only 3. H met (M(64)=0.500061048820197, 0.375011444266388) -> convention verified.
 P1: area law exact, sigma_N(A) = M_1(N) for all 123 qualifying (N,A) of 183 (A N^2 integer), dev 5e-61.
 sigma_U1(N=4..64)=0.51661,0.50396,0.50098,0.50024,0.500061 -> 1/2, N^2(sigma-1/2)->1/4; SU2 -> 3/8, N^2(sigma-3/8)->0.046875=3/64.
 Z2,Z3 on b=N^2: sigma->0 (README values reproduced). Z2 own traj b=artanh(e^{-1/(2N^2)}) sigma=1/2 exactly, b matches README. Z3 own traj b_N ~ (4/3)log N + (2/3) log 6 (measured).
 FAIL P6_f2_U1: second moment at N=64 off limit by 1.02e-3 > 1e-3. Own expectation (tolerance assumed C~1 for O(1/N^2); higher charges have larger correction ~ r^4/N^2), not a target defect. Distance shrinks with N (4.43->4.18).
 Rerun K2 with expect-exit 1 to a new file: compare.
Step 4: Lean WilsonLimit.lean: draft 1 failed (field_simp left a goal; kept as WilsonLimit_draft1_failed.lean), fixed with ring: exit 0, axioms propext, Classical.choice, Quot.sound. Registered as K3.
Step 5: child returned sigma by trapezoid Haar quadrature; reran sigma_quad.py (new file results_quad_1.txt), values equal mine to all 12 printed decimals at N=4..64, both groups.
Step 6: report.md written. Verdicts: 11 STANDS, 1 DEFECT (own tolerance P6_f2_U1), 1 NOT CHECKED (Z2 Lean bound), 1 measured only.
