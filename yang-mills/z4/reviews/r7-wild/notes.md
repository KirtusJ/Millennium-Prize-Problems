# r7-wild notes (wildcard, seed "refinement")

Step 0. control.txt = 0.272341 (-ln tanh 1).

Step 1. Read OVERALL_DISPOSITION, Z4 README trajectory audit (lines 143-171), C4 momentum/adjoint-refinement.md,
A4 hamiltonian-variance/README.md and excited-band/README.md, D4 adjoint-band/README.md.
Checked by hand the C4 adjoint-refinement chain (sphere identities, M1 lower bound, window algebra l=a/(4K), R=2D/a,
w=a^2/(2D), constants 1024, 12288, 1728): no fault found.

Step 2. Choice. Z4 README l.165-167 calls "beta^2 b bounded below" the *exact* condition for A4's window to stay in a
fixed physical window, and OVERALL_DISPOSITION repeats "beta = o(b^(-1/2))". This is exact only for A4's choice
L = A/16, which uses Var F <= 4 and wastes a factor (1+B). A4's own estimate K_e + g u <= B gives
Var F <= 8u <= 8B/g, so Var F * (1+B) is bounded uniformly in g, and A4's own extraction inequality with
M0 <= K_F gives L' = A/(4 K_F) >= c*kappa uniformly in g. Then L' -> infinity iff beta*b -> 0 (not beta^2 b -> 0).
D4 already has a coupling-uniform endpoint kappa/576 for the ADJOINT plaquette; Z4's audit did not use it.
Discarded: re-deriving C4's constants (they check); B4 gap constants (already cross-read by Z4).

Step 3. window_audit.py written, predicates P1-P7 fixed in docstring, run as register check K1 (exit 0).
results/run1.json: P1 4002/4002; P2 sup K_F(1+B) = 41.599 at g = 18.88 (<= 43; hand bound 42.08);
P3 min L'/kappa = 0.00676 >= 9/1376; P4 0 violations in 1e5 random measures (both extraction forms);
P5 met: on beta=b^-0.75, L_A4 goes 9.1e-3 -> 9.4e-8 while L' goes 0.048 -> 15.6 (b: 1e-2 -> 1e-12);
P6 met: beta=1/b, L' stays in [0.0154,0.0156]. 6 met, 0 failed.
Meaning: the "exact condition beta^2 b bounded below" (Z4 README l.164-167, OVERALL_DISPOSITION row Z4) is a
property of A4's choice L=A/16 only. A4's own inputs put the guaranteed band above kappa/148 for every g, so it
leaves every fixed physical window iff beta*b -> 0. Caveat: when beta -> infinity the weight w -> 0 anyway.
Step 4. Sub-agent launched: Lean proof of K_F(1+B) <= 43 for all g>0 (child/).

Step 5. Sub-agent returned KB_bound (Lean, exit 0, standard axioms). Reran it as my check K2 and its grid as K3. verify PASS.
report.md completed. Verdicts: STANDS 4, DEFECT 1, NOT CHECKED 1.
