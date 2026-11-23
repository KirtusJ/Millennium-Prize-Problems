**Overall verdict: none of the three claimed proofs (E13, HARNACK, PATHS) broke under challenge. I found no false line in any step I checked. One minor DEFECT: E13 §6's numerical parameters (r₀ = 0.15, ℓ = 0.08, η' = 0.5 with η = 0.25) violate the constraints TUNNEL_LOWER2 §2 puts on them. This affects only the numerical tables, not the asymptotic proof. Verdict counts: 21 STANDS, 1 DEFECT, 5 NOT CHECKED. Predicates: 12 met, 2 failed (both my own wrong tolerances), 2 measured only. The SU(2)² target limsup ≤ c* is still not proved, as the files themselves say. I share a model family with the director and the authors, so this is not independent review.**

Worker r1-chal, task T159. Control: control.txt = 0.272341 (−ln tanh 1). No network was used. Lean READY exists, but I did not compile any Lean file and claim no Lean result.

## 1. Verdict table

| # | item | verdict | one line of evidence |
|---|---|---|---|
| E1 | kernel density on the ball; Z/ρ direction | STANDS | Lower bound on Tφ needs ρ ≤ …, and E13 uses the exact ρ (term +2 log ρ, sign correct). I₁ ≤ I₀ with (I6) gives ρ ≤ 1 + O(β^{−2/3}) + O(√β e^{−β^{1/3}/2}). The (I7) lower bound is used only for (E3). Asymptotic formula: ρ = 1 − 3/(8β) − … < 1. |
| E2 | exact step u' = u + Rξ − (1−g₀)u, RRᵀ = I − uuᵀ, remainder ρ_ξ | STANDS | Rederived by quaternion product. |
| E3 | Lemma G1 (ℓℓᵀ) and G2 (ℓp = −κw) | STANDS | Rederived: [u₂]×u₁u₁ᵀ[u₂]×ᵀ = wwᵀ, and R_iû_i = x0_i û_i. κ is bounded at a₂ → 0 because Θ' cot a₂ → θ₀/ℓ. |
| E4 | Taylor remainder Err (W, h(S), geodesic Hessian) | STANDS | EP3: 20000/20000 random samples qualify at β = 4096, L = 3, with 0 violations. Worst \|F−M\|/Err = 0.27, using my own exact F (quaternion step, quadrature for Ψ). |
| E5 | Gaussian log J over 6 directions (rank ≤ 3 form); flat identity | STANDS | EP1: the closed form equals the det/solve form to 4e−15 on 300 points. I rederived the per-singular-direction completion of the square. Kernel and valley directions give e^{\|p_ker\|²/2}. |
| E6 | gap bounds DG1/DG3 (corrected version) | NOT CHECKED | The §5 numbers use the exact gap, and so did I. |
| E7 | tails: (E1) ball restriction (lower bound, positivity) and (E3) outer region Q | STANDS | Rederived: the N(p, I) shift gives P(χ₃ > L − \|p_i\|). The outer region uses Ψ Λ-Lipschitz and class angle 1-Lipschitz. |
| E8 | uniformity near a₂ = 0 and a₁ = η', π − η' | STANDS | S ≥ sin η' on K, so h and σ₋ stay bounded. Θ∘a₂ is smooth at U₂ = 1 with Hessian ≤ θ₀/ℓ. q is never differentiated: the exact algebra is used. |
| E9 | explicit numbers sup_K Δ1 = 36.8 / 13.8 / 0.167 at β = 4096 / 16384 / 2.7e8 | STANDS | Recomputed from the formula on my own grid: 36.93 / 13.84 / 0.171, nonincreasing (EP4, EP5). The sup sits at a₂ = r₀, a₁ = π/2, \|b\| ≈ M. |
| E10 | §6 parameters versus the TUNNEL_LOWER2 §2 constraints | DEFECT (minor, repairable) | The constraints are r₀²/sin a₋ ≤ η/4 and ℓ < r₀/2. With η = 0.25 they fail: 0.089 > 0.0625 and 0.08 > 0.075. Also η' = 0.5 > a₋ = 0.255, so the numeric tube does not cover a₁ ∈ [a₋, 0.5). The tables are not numbers for the tube that TUNNEL_LOWER2 uses. The theorem itself is for general parameters. |
| E11 | child MC T156 (\|δ\| ≤ 0.06 at β = 16384) | NOT CHECKED | Not rerun. |
| H1 | (sup), (I₁ up), (k_min), (vol), (infl) | STANDS | HP5: I₁/bound ≤ 0.6365. HP4: v/(11r³/24π) ≥ 1.38. k_min and (infl) were rederived algebraically. |
| H2 | Lemma Ch, the ball-to-ball minorisation | STANDS | A positive kernel restricted to z_j ∈ B_j gives a valid lower bound, so leaving the region is irrelevant. Factor count: 2n kernel factors and n−1 product balls, so ℓ(K') = K' + R² + log(π/2) + 2 log(24π/(11ρ³)) is correct. |
| H3 | path geometry, phases 0–3; V monotone; phase-0 length (π/2)√M β^{−1/4} | STANDS | Rederived. HP6 (scalar sampling of the length bound): 0 violations out of 38260, worst ratio 0.957. |
| H4 | Theorem H4 assembly (g ≥ T^n g with λ ≤ 1; ∫_B g ≥ λm_B/k_sup²; uniform n by padding) | STANDS | Rederived. Each interior point is assigned the larger bound of its two adjacent phases. The n factors (rather than n−1) are conservative, since ℓ > 0. |
| H5 | constants 8.35, 9.09, 35, and 0.5 ℓ(K_M)√M β^{1/4} | STANDS | HP1: min ℓ(K₀)/d = 8.346 at d = 3.645, ρ = 0.264. HP2: 9.085. HP3: coefficients 25.8 and 34.1, both ≤ 35. (π/2)/3.65 = 0.43 ≤ 0.5. |
| H6 | junction points satisfy V ≤ 2M² and a_i ≤ π/2; symmetries σ₁, σ₂ | STANDS | G > c₁ gives V < 2M²S/√(1+S²). g∘σ_i = g by uniqueness of the positive top eigenvector. |
| H7 | λ_ee ≥ 1 − O(β^{−1/3}) (bump sketch, TUNNEL_THEOREM l.82) | STANDS (with a note) | The bump depends on (a₁, a₂), so it is gauge invariant. It is not ee-symmetric, but that is not needed: λ_ee is the global top, so the plain variational bound applies. Note: "1 − ⟨φ,Kφ⟩ = O(1/(βr²))" holds only for a smooth bump. An indicator gives O(β^{−1/6}), which still gives λ → 1, and that is all M4 uses. |
| H8 | m_B ≥ 1/4 − o(1) via M4, (B) and Lemma F | NOT CHECKED | (B) and Lemma F were not rechecked. |
| P1 | ground-state identity E(h) = Δ | STANDS | Rederived. Numerically, E(f/g) equals the child's 300-digit λ_e − λ_o to 1.4e−13 at β = 64 (OP1). |
| P2 | Lemma P'c: Δ ≥ 2∫_S f²/(nρ) | STANDS | Rederived from the flux identity. CS along the path gives 4h(x)² ≤ nΣ(Δh)². Weight by g², integrate over S, dominate by ρQ, and ∫∫Tgg(Δh)² = 2E = 2Δ. Oddness of h comes from f∘σ = −f and g∘σ = g. Diagonal atoms carry zero integrand. |
| P3 | Corollary B: ρ ≤ n sup_S g² max(1/v, \|S\|/v²)/Q_min; polynomial factors only | STANDS | Recomputed the p_k: interior ≤ sup g²\|S\|/v², ends ≤ sup g²/v (σ-substitution at k = n−1), 1D ≤ sup g²/(2r). With n = O(√β) and v ≍ β^{−d/2}, the only exponential comes from inf g. |
| P4 | Corollary CB, and why the well-end-set version needs \|m₀\| | STANDS | Triangle sum, Jensen and CS. The factor-2 remark is correct. |
| P5 | 1D steps (L), (M), (H), (S), (C), (P) | STANDS | Each was rederived. In (L) the trial 1_I is not σ-even, but g is the global top (Jentzsch), so this is fine. (H): steps ≤ 2/√β and ε ≤ 3η + 2r on J_k. (S): the exact Gaussian tilt e^{ρ²/2} = e^{ε+η}. (C): ‖T_ΩΩ‖ ≤ e^{−2η} < λ_e. (P): T_min ≥ e^{−2 asinh 1 − 2}√(β/2π), and m ≥ Δ since λ_e ≤ 1. |
| P6 | 1D theorem against a fine-grid computation (child T162 and me) | STANDS | −log m/√β = 3.898 (β = 64), 4.166 (256), 4.328 (1024), 4.430 (4096, single grid). All are below c* = 4.6054 and increasing. −log m ≤ c*√β + 3 log β held 4/4. Two of the child's runs were rerun bit-identically, and my own double-precision code agrees at β = 64. |
| P7 | SU(2)² transfer table, PATHS §4 (cited inputs) | NOT CHECKED | The cited items were not rechecked. PATHS itself tags the target NOT PROVED. |
| P8 | Lean lemmas cited by all three files (odd_sq, path_cs, tilt_square, phase0_len, flat_identity, cross_bound, …) | NOT CHECKED | The .lean files are not in my directory, and I compiled none. |

Counts: 21 STANDS, 1 DEFECT, 5 NOT CHECKED.

Remarks that do not change any verdict:
- **The E13 kink remark is moot for the use.** G and E are σ₁-invariant, so φ_L ≥ φ_R exactly when a₁ ≤ π/2. So (E1) and (E3) are needed only on a₁ ∈ [a₋, π/2]. TUNNEL_LOWER2's "[a₋, π − a₋/2]" asks for more than it uses.
- **E13's (H1) "0.1" margin** around [η', π − η'] is cosmetic. What is needed is the λ'-neighbourhood.
- **The explicit Δ1 is still useless at simulable β** (13.8 at β = 16384), as E13 says itself.

## 2. Hypotheses each statement uses (and where they are stated)

- **E13 (E1)/(E3):**
  - Ψ∘a₁ C² with H_Ψ and Λ finite (E13 §0, H1).
  - Θ = θ₀(√(a² + ℓ²) − ℓ) (H2).
  - x ∈ K = {a₁ ∈ [η', π − η'], a₂ ≤ r₀, βαq/2 < M²} (H3).
  - λ small against sin²η' (§2).
  - Kernel facts (I1), (I2), (I6), (I7) from LEMMA_F.
  - The reading of Ψ as smooth across π − a₋/2 (§0 Remark).
- **HARNACK H4:**
  - Tg = λg with λ ≤ 1, g > 0 continuous, unique (§0).
  - σ₁, σ₂ symmetries.
  - x ∈ D_M = {a_i ≤ π/2, V ≤ 2M²}.
  - β ≥ max(1, 4ρ²), ρ ≤ 1/2 (§3).
  - m_B from M4 ⇐ (B) ⇐ Lemma F plus λ_ee ≥ e^{−η/4} (header, §5).
  - a* ≤ π/4 (§2).
- **PATHS P'c:**
  - (H1)–(H4) of §0: σ-finite space, symmetric bounded T, measure-preserving involution σ, g > 0 even and f odd eigenfunctions.
  - x ↦ P_x a measurable kernel (§1 Data).
- **Corollary B:**
  - metric measure space with v = inf |B(c, r_β)| > 0;
  - measurable centres;
  - uniform independent z_k (§2.1).
- **1D theorem:** the model of §3 (circle, Gaussian K of variance 1/β, ε = 2 asinh|sin x|), with η < η₀ fixed and β ≥ β₀(η).

## 3. Failed predicates (all kept)

- **e13_recompute K1 (run 1):** exit 1 because scipy is not installed. Cause: my defect (environment). Fixed with numpy Gauss–Legendre in v2.
- **EP2** (D ≤ ρ ≤ 1 at 11 β): FAILED, 10/11. At β = 2.7e8 my 200-node quadrature of e^{−β}I₁ has relative error about 3e−9, which exceeds ρ − D = 4.7e−10. The asymptotic series gives ρ > D. Cause: my own numerical defect, not the target.
- **OP2** (plain double eigenvalue difference within 1e−2 of Δ at β = 64): FAILED, rel 1.75e−2. My tolerance was a wrong expectation: the cancellation error is about 0.73·4e−16/2e−14 ≈ 1.5e−2. Not a target defect.
- **Child-side failures** (its own tolerances, reported by it and confirmed by my rerun):
  - child P1 (grid difference < 1e−3) failed at β = 64, 256, 1024: the scheme is O(h²) because ε has a kink at the wells;
  - grandchild predicate (1e−6 between N = 200 and 400 at β = 16) failed for the same reason.

Measured only:
- the location of sup_K Δ1;
- the child's 4-point fit of −log m = a√β + b log β + c, which gives a = 4.564 against c* = 4.605. The 4096 point uses a single grid, and the 3-point fit is exact, so neither is a test.

## 4. What I did not check

- E13: the DG1/DG3 gap bounds, and the MC of child T156.
- HARNACK: Lemma M4, (B), Lemma F and TUNNEL_THEOREM §4, beyond reading the bump sketch.
- PATHS: the §4 SU(2)² inputs ((H-a), (H-b), (H-c), M4).
- No Lean file was compiled.
- E13's own programs (e13_bounds.py, p5fix.py) and HARNACK's numerics (P1–P8, child T152/T154) were not available here and were not rerun. My checks are independent re-implementations from the formulas.
- 1D at β = 4096 was computed on one grid only (h√β = 1/4; estimated discretisation error about 0.01 nats).
- The 1D theorem is a limsup, and finite-β numerics cannot prove or refute it. They are only consistent with it: −log m/√β rises towards c* from below, and the gap shrinks from 0.71 to 0.18.

## 5. Delegated questions and outcomes

- **Child T162** (admitted under T159; graph seq 322 admitted, 328 released).
  - Question: compute −log m(β) for the 1D continuum model on a fine Nyström grid, for β = 64 to 4096, and test −log m ≤ c*√β + 3 log β, monotonicity below c*, and a fit.
  - Control: c* = ∫₀^π √(2ε) to four decimals. It answered 4.6054. I graded it CORRECT before reading anything else (my Gauss–Legendre value with 2000 nodes is 4.605413).
  - Method: σ-fold, conjugate by e^{−√βΦ}, Newton refinement in 300-digit Decimal.
  - Outcome:
    - −log m = 31.1867 (β = 64, Richardson), 66.6491 (256), 138.5105 (1024), 283.494 (4096, N = 806);
    - ratios 3.898, 4.166, 4.328, 4.430, all < c*;
    - Q1 met 4/4.
  - My checks:
    - reran hp.py at (64, 102) and (256, 202) in rerun_child/: byte-identical;
    - independent double code (identity Δ = E(f/g)) at β = 64, N = 204 agrees to 1.4e−13.
- **Grandchild T163** (child-admitted, parent T162, depth 3; seq 324 admitted, 326 released; I verified this in the graph file).
  - Question: independent unfolded plain-double −log m at β = 16, N = 200/400.
  - Control: ∫₀^π sin = 2, answered 1.99999999999999 (GL), CORRECT.
  - Outcome: 13.816575 and 13.815443. Its 1e−6 predicate failed (O(h²) grid error).
  - I reran it in rerun_grandchild/: identical.

## 6. Exact commands to rerun

```
cd /home/user/z4-workers/r1-chal
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl
python3 -c "import math;print('%.6f'%(-math.log(math.tanh(1))))"
$P init pcp --principal principal --principal-name "Kirtus Justus"     # only in a fresh directory
$P check --ws pcp --name e13-recompute-v2 --expect-exit 0 -- python3 e13_recompute.py results_e13_runN.txt   # new N each time (mode "x")
$P check --ws pcp --name harnack-consts --expect-exit 0 -- python3 harnack_consts.py results_harnack_runN.txt
$P check --ws pcp --name oned-indep --expect-exit 0 -- python3 oned_indep.py results_oned_indep_runN.txt
mkdir -p rerun_child2 && cp child/hp.py rerun_child2/
$P check --ws pcp --name rerun-child-hp-64-102 --cwd rerun_child2 --expect-exit 0 -- python3 hp.py 64 102
$P check --ws pcp --name rerun-child-hp-256-202 --cwd rerun_child2 --expect-exit 0 -- python3 hp.py 256 202
mkdir -p rerun_grandchild2 && cp child/grandchild/run.py rerun_grandchild2/
$P check --ws pcp --name rerun-grandchild --cwd rerun_grandchild2 --expect-exit 0 -- python3 run.py out_me
# child (as run): $R task-admit $G --by principal --label r1-chal-child --parent T159   -> T162
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T162
$P verify --ws pcp
$R verify pcp/register.jsonl
```

PCP OS, last lines:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

The register holds K1 (failed e13 run, exit 1), K2–K6, K7 (child run, 554 s) and K8.
