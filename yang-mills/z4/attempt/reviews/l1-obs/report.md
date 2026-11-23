Overall verdict: claims (i), (ii) and (iii) of observable-weights stand as stated, with their limits taken at fixed box. Every number I recomputed agrees: thresholds, weights, 3k(t)²/2, 4π and 24π². The shipped check.py does not run because a dependency is missing. Separately, (i) has a sub-threshold contribution of order h at single hard frequencies, which vanishes in the limit and is not stated.

Worker l1-obs, task T122, 2026-11-23. Control: control.txt = 0.272341 (−ln tanh 1). Lean READY present.

## Part A: verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| (i-a) single plaquette → \|Z\|²/2; slow part order | STANDS | Constant-field part of Y = 2h\|X_i×X_j\|²·(1+O(h²)). Relative error 6.1e-3, 6.1e-5, 6.1e-7 at h=1e-1, 1e-2, 1e-3 (prog_slow_v2, K3). It is O(h) per plaquette with X~n^{-1/3}, so the soft amplitude is O(h·n^{-4/3}). The Born-Oppenheimer O(h) term vanishes by colour contraction (analytic). |
| (i-a′) cross term (not stated in README) | STANDS, NOTE | Y − \|Z\|²/2 = 2h^{1/2} Z·(X_i×X_j) + o(h^{1/2}): residual D = 2.4e-2, 5.6e-3, 6.0e-4 at h=1e-2, 1e-4, 1e-6 (prog_cross, K9). This term has weight O(h)=O(β^{-1/3}) on one-hard-particle ⊗ slow-adjoint states at energies ω_p ∈ [E_ij/2, E_ij). At finite β, those states are the leading sub-threshold weight, not the soft levels. It vanishes in the limit, so (i) is not contradicted. No rate is claimed in the README ("No rate … follows"). This rate is analytic; I did not compute the spectral weight itself. |
| (i) limiting correlator 3k(t)²/2 | STANDS | Direct time-lattice Gaussian (periodic T=60, pinv) equals Fourier k(t) to 1e-12 at t=0,1,2 on 2³. Monte Carlo of the 3-colour Wick factor: 0.30703±0.00119 vs 3k²/2=0.30791 at t=0, and 0.00497±0.00050 vs 0.00473 at t=1. The doubled factor is excluded at t=0,1 (prog_spectrum P5, P6). Lean wickColor encodes the same identity. |
| (i) threshold "first pair of active hard frequencies" | STANDS | From the plaquette-link incidence spectrum I get the auditor's values to <5e-9. 2³: 3.52549435 / 0.046875. 3³: 3.13359847 / 0.01410935. 3×2×5: 3.13359847 / 0.00285714. The closed form 2 arcosh(1+2 sin²(π/max(N_i,N_j))) is exact to 1e-15, also on (4,3,2). The (3,2,5) box has an inactive lower frequency (1.1166 < 1.5668), as checks.md says. |
| (i) total weight in [0,b], b<E_ij → 0, also ÷ variance | STANDS (given parent) | Moments at integer t on x=e^{-E}∈[0,1] give weak convergence, and the closed set [e^{-b},1] has limit mass 0 (portmanteau). The limiting variance 3k(0)²/2 is >0 (0.3079 on 2³). This relies on the parent's vacuum and transfer identification, which I did not re-check. |
| (i) uniform exponential moment | STANDS (given ‖K‖≤1, λ₀→g>0) | e^{βS/2}Ω = λ₀^{-1}K e^{-βS/2}Ω gives ‖e^{βS/2}Ω‖ ≤ 1/λ₀. Y ≤ βS, so E[e^Y] ≤ λ₀^{-2}. I did not verify the normalisation of K in the parent. |
| (ii) winding probes reach every soft eigenspace | STANDS | f ranges over all bounded continuous SO(3)-invariant functions of (V₁,V₂,V₃), so separation is automatic. Traces alone would also do: the inner products and the triple product separate SO(3)-orbits, and these correspond to tr H_i, tr H_iH_j and tr H₁H₂H₃. The density argument holds: φ₀>0, unitary division by φ₀, C_c dense, group averaging. Center flips leave V_i invariant. The README asserts no single trace. This is consistent with MC_BOX (E, T2 resolved by squared winding loops), which I did not read. |
| (ii) plane average → 2h²X_i×X_j | STANDS | The quaternion commutator is [a,b]=2a×b. The shim run of the author's loop check reproduces checks.md (sheet error 0.01365 at h=0.04, 0.00157 at h=0.000625). Errors decay as ~h^{1/2}, consistent with the O(hs)/h² term. |
| (iii) N E_atom → 4π, N⁸μ_atom → 24π² | STANDS | Matrix equals closed form at N=4 and 8 to 1e-14. N·E−4π: −2.031, −0.601, −0.158, −0.0402 for N=4, 8, 16, 32. N⁸μ−24π²: −108.87, −40.66, −11.60, −3.007. Both rates are O(N⁻²) (successive ratio at 16→32: 3.94 and 3.86). N=32 gives 233.8636621, as in checks.md. |
| check.py (author) | DEFECT (reproducibility; repairable) | As shipped it raises FileNotFoundError for `target/second-box/transverse-plaquettes/check.py` (K4). With my 10-line quaternion shim it reproduces every number in checks.md (K8). |
| checks.md "winding" control | DEFECT (minor) | The control tests \|Im H\|²/(Nh)², not the V_i=(Re H)Im H/(Nh) defined in the README. The two are equal at leading order. |
| README display formula | DEFECT (typo) | `\tfrac32 k(t)^2,qquad` is missing a backslash. |
| ObservableWeights.lean | STANDS (scope: scalar ring identities only) | lake env lean exit 0 (K7); 7 declarations, axioms only propext, Classical.choice, Quot.sound; no sorry. curlLongitudinal and pairAtom are polynomial identities. wickColor is the colour-covariance identity. thresholdCoefficient is 3(4p)²/2=24p². variancePositive, massFromMoment and survivingWeight are elementary inequalities. None formalises an analytic step. |
| support-criterion/ (Eq. 1) | NOT CHECKED | I read the README and .lean in full. I spot-checked only the arithmetic: b=2N³−3N²+1, and the covariance floor 1/(8√3). |

## Part B: Pavel, arXiv:hep-th/0701283

H.-P. Pavel, "SU(2) Yang-Mills quantum mechanics of spatially constant fields", arXiv:hep-th/0701283v1, 30 Jan 2007, 7 pp. I fetched the PDF from arxiv.org into the scratchpad (outside this directory) and read it with pdftotext -layout. The bracket convention ("last two digits replaced by the bracket at 60 nodes") is stated after Eq. (50).

| quantity | paper (locator) | quoted | confirmed | ours | ours − paper |
|---|---|---|---|---|---|
| vacuum | 4.116719740(35) → 4.116719735 (Eq. 50, p.4; Table 1 row 0, p.5) | 4.116719735 | yes | 4.1167196 | −1.35e-7 |
| first excited even scalar | 6.386361(58) → 6.386358 (Table 1 row 1, p.5) | 6.386358 | yes | — | — |
| lowest even tensor | 6.014500 (Table 2 row 1, p.6; 30 nodes only, virial dev 6.3e-6) | 6.014500 | yes | — | — |
| tensor gap | 1.897780265 | 1.897780265 | yes | 1.8977806 | +3.35e-7 (within the paper's 6-decimal print) |
| scalar gap | 2.269638265 | 2.269638265 | yes | 2.2696457 | +7.435e-6 |

Our scalar gap is the least converged value: it implies E₁ = 6.3863653, which is 7.3e-6 above the paper's 60-node value. Our vacuum lies 1.35e-7 below the paper's variational value. A Ritz upper bound may lie below another upper bound, but this should be checked for truncation of our printed digits.

## Hypotheses used and where stated

- H1: fixed box; β→∞ before any volume limit (README §1 and last §).
- H2: the parent's ordered-spectrum, quasimode and transfer comparison (README §1, links ../full-neutral.md, ../README.md). Not re-checked (PRIOR_REVIEW_box covers it).
- H3: K is a contraction and K_β is a positive operator. This is used for x=e^{-E}∈[0,1] and for ‖e^{βS/2}Ω‖≤1/λ₀ (README §2, implicit).
- H4: φ₀>0 (README §1, used in §3).
- H5: center-neutral, globally colour-invariant sector (README §1 and §3).
- H6: Gaussian conventions: links exp(hX+sz), s²β=1, ground variance 1/(2 sinh ω) (README §2).

## Failed predicates

- P9 (prog_spectrum, K2): I predicted an O(h) relative correction; the observed correction was O(h²). At h=1e-3, floating-point cancellation in 1−ReP dominated. This is my own expectation and test design, not the target. It was redone as P9b with |ImP|²/(1+ReP), which is MET (K3).
- Q1 (prog_cross, K9): the error-ratio window [5,20] failed at the first step (4.34; second step 9.45). The run was pre-asymptotic at h=1e-2. This is my own tolerance; the coefficient converges.

Counts (my predicates): **23 met, 2 failed, 2 measured only**.

## Not checked

The parent fixed-box spectrum (H2); the projector-norm convergence argument; the normalisation of K; the support-criterion theorem (1); the weight of the one-hard-particle O(h) term beyond its pointwise coefficient; the worker.c/ELF replay (replay-guests.py is not in target); support-criterion/check.py, checks.md and worker.c; MC_BOX.md and PRIOR_REVIEW_box.md (not read).

Files read: README.md, checks.md, ObservableWeights.lean, check.py and worker.c in full; support-criterion/README.md and SupportCriterion.lean in full. The rest was not read.

## Delegated questions

- Child T125 (admitted with parent T122, released). Questions: (b) thresholds and weights from the incidence matrix for 2³, 3³ and 3×2×5; (d) atom limits for N=4, 8, 16, 32.
  - Control: arccosh(3)=1.76274717, graded correct before anything else was read.
  - Result: all auditor values matched (with ordered pairs; unordered would be half). Rates ≈ N⁻² (local exponents 1.98 and 1.95 at N=32).
  - I reread q.py and reran it (K5); the output is identical and agrees with my prog_spectrum.
- Grandchild T126 (parent T125, depth 3, admitted and released, graph seq 250/251). Question: which closed form (max over N₁,N₂; max over all sides; min) fits the threshold, on (5,2,3), (2,5,3) and (3,2,5).
  - Control: the (2,2,2) value passed.
  - Result: max(N₁,N₂) fits all three boxes. Max over all sides fails for (3,2,5).
  - I reran it (K6); the output is identical.

## Rerun commands (from /home/user/z4-workers/l1-obs)

Result files are opened with noclobber, so each rerun needs new output names.

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name spectrum1 --expect-exit 0 -- bash -c "set -o noclobber; OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 prog_spectrum.py > results_spectrum1.txt 2>&1"   # exits 1 (P9 failure kept)
$P check --ws pcp --name slow2 --expect-exit 0 -- bash -c "set -o noclobber; python3 prog_slow_v2.py > results_slow2.txt 2>&1"
$P check --ws pcp --name cross1 --expect-exit 0 -- bash -c "set -o noclobber; python3 prog_cross.py > results_cross1.txt 2>&1"   # exits 1 (Q1 failure kept)
$P check --ws pcp --name their-check-asis --expect-exit 1 -- bash -c "set -o noclobber; cd target/periodic-box-spectrum/observable-weights && python3 check.py > /home/user/z4-workers/l1-obs/results_their_check_asis.txt 2>&1"
$P check --ws pcp --name their-check-shim --expect-exit 0 -- bash -c "set -o noclobber; OPENBLAS_NUM_THREADS=1 python3 theirs/check_shim.py > results_their_check_shim.txt 2>&1"
$P check --ws pcp --name lean-observable-weights --cwd /home/user/z4-lean --timeout 600 --expect-exit 0 -- bash -c "PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/l1-obs/ObservableWeights_copy.lean > /home/user/z4-workers/l1-obs/results_lean1.txt 2>&1"
$P check --ws pcp --name child-q-rerun --cwd rerun_child --expect-exit 0 -- bash -c "python3 q.py > stdout_q.txt 2>&1"
$P check --ws pcp --name grandchild-rerun --cwd rerun_child --expect-exit 0 -- bash -c "python3 gc_run.py > stdout_gc.txt 2>&1"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Verify, last lines:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

This reviewer shares a model family with the director; this agreement is not independent review.
