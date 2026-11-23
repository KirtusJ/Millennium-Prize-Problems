# a4-chalcurv — report (challenger of PROOF_A_curv.md, curvature route)

Control: `control.txt` = 0.272341 (−ln tanh 1). The control was written first.
Everything below comes from my own code (`lat.py`, `run_a1.py`, `run_a2.py`, `run_a4.py`). I did not have the builder's program.

**Bottom line.** The builder's refutation of S6 is right for the boxes it was run on. My independent code reproduces it: κ_H is between −1.1 and −2.0 on 24 of 24 periodic samples at β_W = 4 to 48 (L = 3 and L = 4). The cause is not rare bad plaquettes. It is a second-order downward push ("level repulsion") on the soft modes, of size k·c. Here c = β·ε² measures the fluctuation size, and c = 1 is equilibrium. The constant k is about 2.5 for SU(2) at one-loop equilibrium, and Ricci is overcome once c > c₀ ≈ 0.4. So equilibrium lies well past the threshold.

On the torus the soft modes are the toron (zero-momentum) modes. On a small open box (L = 4, β ≥ 12) there are no soft modes, and κ_H is large and positive (+3 to +23). There S6's literal statement holds on 9 of 9 samples. That positivity is itself a finite-size gap: it grows like β·p_min². The route needs constants uniform in Λ and τ. Any box with L ≳ √β, or with periodic directions, has soft modes. So the open-box result does not reopen the route. I did not test the infinite-volume statement directly.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| A1: my Hess V and horizontal projection | STANDS | Finite differences agree with the analytic Hessian to 2.7e-8 (SU(2)) and 1.4e-8 (SU(3)) on random L = 3 configurations. One plaquette with Q = −1: B has eigenvalues 1−2β (×3) and 1 (×9) to 1e-15, and the 3 negative modes are horizontal. (`result_a1.txt`) |
| A1: gauge-direction space (dimension, kernel at U = 1) | STANDS | rank G = 240 = 243 − 3 at U = 1 (the constant-ω kernel) and 243 at a generic configuration. At U = 1, κ_H = 1 with exactly 12 horizontal eigenvalues equal to 1 (torons: 3 colours × 4 directions). SU(3): rank 640, κ_H = 1.5, 32 torons. |
| File S4 (κ_H = 1 at flat configurations) | STANDS | Flat configurations are global minima of V, so Hess V ≥ 0 there. Equality needs a horizontal zero mode of the curl form: 12 on the torus (verified), none in an open box, and spectrum accumulating at 0 in infinite volume. |
| File S2 (horizontal Bakry–Émery for invariant f) | STANDS | Γ₂ ≥ κ_H Γ is needed only along P_t f, which stays gauge-invariant (L commutes with the isometric gauge action). The horizontal distribution does not need to be preserved or integrable. LSI uses Kato's inequality, which holds for every f. Checked by argument only, not numerically. |
| A2: the file's S6 test (κ_H ≈ −1.5 to −2.2 at equilibrium, periodic) | STANDS (refutation of S6 reproduced) | Heat-bath controls pass: plaquette vs 1 − 3/(4β) at β = 12, 24, 48 and the strong-coupling value at β = 0.5. κ_H on L = 3: β = 4: −1.46 to −1.79; β = 6: −1.39 to −1.96; β = 12: −1.12 to −1.52; β = 24: −1.12 to −1.93; β = 48: −1.55 to −2.04. On L = 4: β = 6: −1.77, −1.26; β = 24: −1.15, −1.67. That is 0/24 samples with κ_H ≥ 0.5. |
| A3: is it a finite-volume artefact? | Partly (measured only) | Periodic, β ≥ 24: 3–4 negative modes, then a jump to the β scale. The lowest eigenvector is extended (IPR·n_E = 1.4–3) and has zero-momentum weight 0.96–0.99 in Landau gauge, so it is a toron mode. No change from L = 3 to L = 4. Open L = 4: β = 4 gives −1.67 to −2.40 (localized: IPR·n_E up to 27, up to 34% of the weight on the links of the top-1% plaquettes); β = 6 gives +0.16, −0.32, −0.04; β = 12, 24, 48 give +3, +9.6, +23. No correlation with the largest plaquette deviation at β ≥ 12. |
| A4: mechanism (second-order level repulsion, deficit ∝ c) | STANDS (measured) | κ_H → Ric − k·c, constant for β from 16 to 1024. k does not depend on c to 3–4 digits. One-loop equilibrium ensemble G: k = 2.62, 2.51, so c₀ = Ric/k = 0.38–0.40, below c = 1 (equilibrium), and κ_H(c = 1) → −1.62, −1.51. White noise W: k = 8.1–9.1, c₀ = 0.11–0.12. |
| A5: SU(3) vs SU(2) | Measured only | SU(3), ensemble G, 1 seed: k = 3.42, c₀ = 0.44 (SU(2): 0.38–0.40). At c = 1, (κ_H − Ric)/Ric = −2.28 vs −2.51 to −2.62 for SU(2). The relative deficit is slightly smaller for SU(3), but it is still far from closing the gap. |
| The builder's sentence "volume trend can only push the minimum down" | DEFECT (minor) | The boundary condition changes κ_H by an O(β) amount: open L = 4 is strongly positive at β ≥ 12. The sign of the volume effect depends on whether soft modes exist; it is not monotone in general. |
| S3, S5 (1 − 4.31β), S7–S10 | NOT CHECKED | — |

**Predicate counts (met, failed, measured only): 71, 53, 5** (the 5 are the plaquette controls at β = 4 and 6, where one-loop does not apply). The A3, A4 and A5 diagnostics (IPR, zero-momentum weight, k, c₀) are measured only.

## 2. Hypotheses each statement uses, and where they are stated

- **S2:** Bakry–Émery on a compact manifold with smooth V (file S2, citing SZZ Thm 1.4); P_t preserves invariant functions (file S1); ∇f is horizontal for invariant f (file S1); κ_H ≥ K uniformly in U, Λ and τ (file S2). The last of these is false for β > 1/2 (file S5).
- **S4:** Q_p = 1 for all p; metric −Tr; Ric = N/2 (file Conventions, S4).
- **S6:** the "rare bad plaquettes" picture (file S6). It implicitly assumes that small |F| means a small curvature deficit. That is false: the deficit is set by β|F|², which is O(1).
- **My A4:** fluctuations around U = 1 with no toron fluctuation in G; 1–2 seeds; one box size per group.

## 3. Failed predicates

The failures that matter for the director are the T2′ failures at β ≥ 4 on periodic boxes (28), which are the target's own refutation reproduced. Every other failure is either my own over-broad predicate (T2′ at β = 0.5, all T2″ failures, M1 on the open box) or the target's claim holding under open boundaries.

| predicate | where | cases | whose failure |
|---|---|---|---|
| T2′ (S6: κ_H ≥ 0.5) | L3 periodic, β = 4–48 | 20/20 | **Target (S6)**, as the builder says |
| T2′ | L4 periodic, β = 6, 24 | 4/4 | **Target (S6)** |
| T2′ | L3 periodic, β = 0.5 | 4/4 | **Mine**: S6 makes no claim at small β |
| T2′ | L4 open, β = 4, 6 | 6/6 | **Target (S6)** |
| T2′ | L4 open, β = 12, 24, 48 | 9/9 **met** | — (S6 holds there) |
| T2″ (κ_H ∈ [−2.4, −1.0], the file's range) | L3 periodic, β = 0.5 | 4 | **Mine** (range applied outside the file's scope) |
| T2″ | L4 open, β = 6–48 | 12 | **Mine** (I did not expect the open box to be positive) |
| M1 (κ_H tends to a constant as β → ∞ at fixed c) | SU(2) L3 open, W | 3/3 | **Mine**: the open box has no soft modes, so κ_H ∝ β |

My own code defects, fixed and recorded:
- The heat bath and the Landau-gauge relaxation lost unitarity (the error grew 10× per sweep). The first A2 run (K4, exit 1, kept as `result_a2_L3p_FAILEDRUN1.txt`) produced meaningless gauge-fixed columns. Its κ_H values for β = 0.5 and β = 4 (first two samples) were later reproduced exactly by run 2 with the same seeds. Fixed with a quaternion re-projection.
- Child predicate P5 was vacuous, a design defect of the child that it reported itself. A replacement test passed.

## 4. What I did not check

- The infinite-volume (or L ≫ √β) behaviour directly. My argument that soft long-wavelength modes take the same O(1) push is an extrapolation from the toron result, not a measurement.
- Open boxes larger than L = 4.
- Toron fluctuations in ensemble G.
- More than 1–2 seeds in A4 and A5.
- Autocorrelation of toron modes at large β (cold start plus 300 sweeps).
- S3 (‖Hess V‖ ≤ 12β), S5 (1 − 4.31β), S7–S10, and the literature (SZZ, Stroock–Zegarlinski).
- I did not use Lean. It was READY, but nothing here was suited to formalization in the time available.

## 5. Delegated questions and outcomes

- **Child** (`child/`, sonnet, run `child-run1`, K1, 73 s). The task was a finite-difference Hessian check on a single plaquette with Q = −1 and on a 2×2 two-dimensional periodic lattice. Control "1 − 2·3": the child answered **−5, correct**. I graded it before reading anything else.
  - Single plaquette at β = 1 and 3: 1−2β (×3) and 1 (×9), within 1e-6.
  - 2×2 lattice at U = 1: 15 zero modes, then eigenvalues 2 (×6) and 4 (×3).
  - Random configuration: smallest eigenvalue of B = −1.3079.
  - I reran the child's `hess.py` in `rerun_child/` (K3) and got identical output. My own code on the 2×2 lattice gives 15 zeros, 2 (×6) and 4 (×3), in agreement.
- **Grandchild** (`child/grandchild/`, started by the child). Control "2 + 2·3": answered **8, correct**. Question: smallest eigenvalue of B for one plaquette with Q = −1 at β = 3. It returned −4.99999919 (×3) and 0.99999981 (×9). The child reran it (`child/rerun_gc`) and got identical numbers. Same step and stencil as the child, so this is not a strongly independent check.

## 6. Rerun commands

Run from `/home/user/z4-workers/a4-chalcurv`. Set `export OPENBLAS_NUM_THREADS=1` and `P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"`. Result files are opened with mode "x", so move the old ones aside first.

```
$P check --ws pcp --name a1 --expect-exit 0 -- python3 run_a1.py
$P check --ws pcp --name a2-L3p-run2 --expect-exit 0 -- python3 run_a2.py 3 p 4 0.5 4 6 12 24 48
$P check --ws pcp --name a2-L4o --expect-exit 0 -- python3 run_a2.py 4 o 3 4 6 12 24 48
$P check --ws pcp --name a2-L4p --expect-exit 0 -- python3 run_a2.py 4 p 2 6 24
$P check --ws pcp --name a4-su2-L3p-W --expect-exit 0 -- python3 run_a4.py 2 3 p W 2 16,64,256,1024 0.25,0.5,1
$P check --ws pcp --name a4-su2-L3p-G --expect-exit 0 -- python3 run_a4.py 2 3 p G 2 16,64,256,1024 0.25,0.5,1
$P check --ws pcp --name a4-su2-L3o-W --expect-exit 0 -- python3 run_a4.py 2 3 o W 1 16,64,256,1024 0.25,0.5,1
$P check --ws pcp --name a5-su3-L3p-G --expect-exit 0 -- python3 run_a4.py 3 3 p G 1 256,1024 0.5,1
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
(cd rerun_child && $P check --ws ../pcp --name rerun-child-hess --expect-exit 0 -- python3 hess.py results.txt)
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last lines of the two verify commands:
- Python: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

The director and I share a model family, so my agreement with the builder is not independent review.
