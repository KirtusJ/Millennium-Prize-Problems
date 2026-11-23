Overall verdict: **yes after listed repairs.** The second half (tun_lower.tex, Sections 5–8) proves limsup (−log m_eo)/√β ≤ c* as written, provided the results of the first half hold. The repairs are bookkeeping: an incomplete parameter list in §8.1, one missing one-line argument, and notation. None of them is a mathematical error that changes a bound.

Referee: worker v1-chL, task T180. Same model family as the authors, so my agreement is not independent review.

## Verdict table (in the order of the note)

| # | Item (label) | Verdict | One line of evidence |
|---|---|---|---|
| 1 | Lemma tu:L-flux (I0, I1, I2) | STANDS | Checked by hand. (I2) factor 4: both orderings of A×A^c each give 2⟨g1_A,Tg1_{A^c}⟩. (I1) needs λ = sup spec, which the proof states. |
| 2 | Lemma tu:L-GS | STANDS | Checked by hand. Tonelli applies with nonnegative integrands; the two square terms are finite (each equals λ), so E(h) is finite. |
| 3 | Lemma tu:L-C (comparison) | STANDS | Checked the identity (λ−T_ΩΩ)w_Ω = (Tφ−λφ)_Ω + T_{ΩΩ^c}w_{Ω^c} term by term; the Neumann series is positive. |
| 4 | Lemma tu:L-Pc | STANDS | Cauchy–Schwarz plus oddness plus the GS lemma. f and g are continuous, so h is defined at every point. n must be the same for all x (it is, by the statement). |
| 5 | Corollary tu:L-B | STANDS | Density bounds for p_0, p_k, p_{n−1} checked (σ preserves measure, g∘σ = g); Q_min ≥ T_min (inf g)². |
| 6 | Scalar facts (L2), (L3) | STANDS | (L3): child Q5d/e (minimum slack 0.0034 and 0.0044). (L2) is not used. |
| 7 | Lemma tu:L-L4 | STANDS | Trial function u is odd/even under σ1/σ2 as required; the 8 cross terms are bounded correctly. L_β recomputed: 0.0138, 0.0965, 0.3083, 0.5313, 0.7519 (prog1 C12). |
| 8 | Lemma tu:L-M4 | **GAP** (minor) | φ_min(η) = inf_{ε≥2η}Φ > 0 is asserted (l.230) but is not among the stated properties of tu:U-weight. It follows from tu:U-W13 (ρ_η > 0 for ε > 3η/2, so f > 0 where ε ≥ 2η, and f̃ ≥ f̃(π/2−τ/2) > 0 on the window). Repair: add that line. The a₂ bound is tu:U-B(2), so "the same proof gives" (l.233) is backed by a stated result. |
| 9 | Lemma tu:L-tangent | STANDS | Motivation only; no later proof uses it. The exact version is tu:L-exact (G1), which prog2 M2 checks. |
| 10 | Lemma tu:L-ansatz-props | STANDS | (i)–(v) checked. (iii): V < 2M²S/√(1+S²) is correct. Nit: at S = 0, q is 0/0 and needs the convention q := 0. |
| 11 | Lemma tu:L-exact (a)–(f) | STANDS | prog2 M1/M2: 20000 random configurations, worst \|r_ξ\|/bound = 0.877; ℓℓᵀ, singular values and ℓp = −κw exact to 1e-10. D_β ≤ ϱ ≤ 1 (prog1 C9); (b) inequality (C11). |
| 12 | Lemma tu:L-taylor, incl. Δh (patched) | STANDS | Δh derivation checked by hand (A₀−A₁ step, monotonicity of σ^{3/2}√(1+σ)). The explicit chain to 5r_b/S² is checked (child Q5a/b). prog2 M3: 6000 points on the tube with a concrete C^∞ χ, η ∈ {0.4, 0.1}, β ∈ {1e4, 1e6}: worst \|F−𝓜\|/Err = 0.332, 0 violations; \|h(S′)−h(S)\| ≤ stated Δh ≤ 5r_b/S². |
| 13 | Lemma tu:L-gauss, DG1/DG3 (patched) | STANDS | 1-D Gaussian factors, flat identity and exact-gap algebra rederived by hand. prog2 M4: 20000 configurations, β ∈ [10, 1e8]. Formula vs 6-D determinant: relative 3.6e-14. Exact gap vs direct: 1.4e-11. gap ≤ DG1′ ≤ DG1 and −gap ≤ DG3′ ≤ DG3 with 0 violations. Monte Carlo of J agrees (7e-4, s.e. 2.8e-3). (gap-unif) dominates both DG1′ and DG3′ given A, D_w ≥ 1. |
| 14 | Lemma tu:L-tails | STANDS | χ₃ tail formula (prog1 C15); 1 − cos θ ≥ 2θ²/π²; the density bound for t = √β θ is uniform in β. |
| 15 | Proposition tu:L-E13 | STANDS | Δ₁ and Δ₃ bookkeeping rederived: two links give e^{−L⁴/β}, the upper density gives 1/(ϱ²(1−r_b²)). (err-explicit) constants 17/8 → 2.2, 81/64·5 → 6.4, 0.503 → 0.51, 0.17/8 → 0.03 checked; arcsin facts from child Q5c. Nit: the constant C in L = √(C log β) is never fixed (any fixed C > 0 works). |
| 16 | Lemma tu:L-E2 | STANDS | tu:U-K is used within its hypotheses (its η = β^{−1/8} ≤ 1, β > 1, β′ > 0 for large β). The second term is about e^{−β^{3/4}/2 + O(√β)}. |
| 17 | Lemma tu:L-S4 (new (M_A), margin m/2) (patched) | STANDS | Steps 1–7 rederived by hand: weighted AM–GM with k(1−γ) = 1; log R ≤ log m₀ and P ≤ m₁ under (M_A); affine in y_c; strip bound F ≤ 1−m₀+y_β; e^u(1−u) ≤ 1. Grids: prog1 C13/C14 (66591 cases, minimum slack 3.8e-2 off the strip and 8.1e-5 on it); child Q7 (1.93e6 points, 0 violations). M_A² values reproduce: 12.06, 20.55, 37.91, 72.82, 352.5. |
| 18 | Lemma tu:L-norm | STANDS | T = B*K₁B with K's commuting square roots (tu:U-kernel(3)); fibrewise ‖F_{a₁}‖ (tu:U-R(1)); tu:U-F used with η/2 within its hypotheses. |
| 19 | Proposition tu:L-sub | STANDS | (i)–(iii) of tu:L-C checked. Ω^c = {φ = 0} ∪ R_well. The σ₁ reflection for a₁ > π/2 is correct. g ≥ φ holds on all of X. |
| 20 | Lemma tu:L-elem | STANDS | (I₁ up), (k_min), (vol), (sup), (infl): prog1 C10b (after my own overflow failure), C10 vol ratio ≥ 1.38; prog2 M5 (20000 cases, worst ratio 1.0000, 0 violations). |
| 21 | Lemma tu:L-chain | STANDS | 2n factors of k, n−1 interior points, β cancels in k_min²v². Needs ρ/√β ≤ 1/2 (stated). |
| 22 | Lemma tu:L-geom | STANDS | Phase-0 length mψ ≤ (π/2)√M β^{−1/4}; V monotone in phases 0 and 3; padding is stated. |
| 23 | Theorem tu:L-H4 | STANDS | g ≥ T^n g because λ ≤ 1; ∫_B g ≥ λm_B/k_sup². |
| 24 | Corollary tu:L-H4cor | STANDS | c_ch(K₀)/d = 8.3459 and c_ch(K₁)/d = 9.0850 at (3.65, 0.265); the grid minimum is 8.3459 at (3.645, 0.264) (prog1 C2/C3). 8.35(2a₋+r₀) + 9.09a₋ ≤ 35(a₋+r₀). Needs M ≥ √(1/2), which (M_A) implies. |
| 25 | §8.1 parameter list and order of limits (patched) | **DEFECT** (minor, repairable) | See failed item A below. The list is consistent, but it is **not complete**. β₀ of (B) depends on (η, δ, τ) and the choices in (W1)/(W3) (tu:U-B), and δ, τ are fixed nowhere in this half. χ and Θ̃ (which set H_Ψ, Λ and Δ₂'s constant) are fixed only in §6.4, not in the list. C in L is not fixed. μ is listed among the "fixed" parameters but depends on β (√β, R_β, m_B). No threshold depends on μ, so nothing breaks. Repair: add δ = τ = 1/2 with the explicit tu:U-W13 construction, χ, Θ̃, C = 1, and move μ out of the list. Then every β₀ is a function of η alone. |
| 26 | Lemma tu:L-balls (patched) | STANDS (nits) | Case (I): z ∈ D_{M″}, and n₁₂ ≤ 3a₋√β/d + 3 checked. Case (II): prog2 M6 at the smallest admissible β and at 10× it, η ∈ {0.4, 0.1}: G − c₁ − e^{−0.375}/2 ≥ 0.3586 and E − c₂ − 1/2 ≥ 0.204, 0 violations. 1.4804 and 0.3436 reproduce (C5/C6). Nits: μ′ is only bounded, never defined (set μ′ := e^{−35a₋√β − R′_β}). §8.2 does not say that chains are padded to a common n, which tu:L-Pc requires (padding as in tu:L-geom works). |
| 27 | Theorem tu:L-main | STANDS | −log Δ ≤ 2√βΨ(π/2) + 70(a₋+r₀)√β + O(β^{1/4}); m_eo ≥ Δ/λ ≥ Δ; then η → 0. |
| 28 | Corollary tu:L-limit | STANDS (given tu:U-main) | c* = 4.6054131945 (prog1 C1; child; grandchild). |

**Counts (statements):** 26 STANDS, 1 GAP, 1 DEFECT, 0 NOT CHECKED.
**Counts (predicates), mine:** 21 met, 1 failed, 1 measured only.
- prog1: 14 met, 1 failed (C10).
- prog1b: 1 met.
- prog2: 6 met, M7 measured only.

**Child (rerun by me, identical output):** Q1–Q7 all agree; 1 failed (Q2b, its own float cancellation, rechecked in high precision).

### Notation defects (nits, no mathematical effect)
- ε is used as ε(a) = 2 asinh(sin a) (l.301, l.783, matching tu:U-intro) and also as ε(sin a) meaning 2 asinh(sin a) (l.226, l.229, l.702). Read literally, "ε(sin a₋) = 2η" at l.226 is false.
- S names both the radius √(|u₁|²+|u₂|²) and the set C_η ∩ {V ≤ 1}.
- a₁ names both the class angle and e^{−3η/4} in S4 Step 4.
- In the Taylor lemma, "ΔS² ≤ …" is a definition written as an inequality.

## Hypotheses used and where they are stated

- **Section 5 (abstract):** σ-finite space; T(x,y) ≥ 0 symmetric and bounded self-adjoint; σ a measure-preserving involution commuting with T; g > 0, Tg = λg, g∘σ = g; f odd with Tf = λ_o f (l.7–11). (I1) and the Comparison use λ = sup spec T (l.35, l.72).
- **Model:** X = SU(2)², the kernel, V and σ₁/σ₂ (tu:U-intro, l.9–40); λ = ‖T‖ is simple and g is invariant (tu:U-intro l.42–47); λ_eo is taken on gauge-invariant functions (l.49–52).
- **Parameters:** η ∈ (0, 0.4], with a₋, r₀, ℓ, θ₀, χ, Θ̃, M (§6.4, §8.1); (M_A) (l.666); ρ = 0.265, d = 3.65, ρ_B = 1/2, ϰ = 1 (l.905, §8.1).
- **β-conditions:**
  - δ ≤ m/2 and y_β ≤ m/2 (l.670–672);
  - the four conditions of tu:L-balls (l.982);
  - β ≥ max(1, 4ρ²) (tu:L-H4);
  - λ, λ_eo ≥ e^{−η/4} (tu:L-L4);
  - tu:U-F with η/2;
  - (B) of tu:U-B;
  - m_B ≥ 1/8 and ∫_S f² ≥ 1/2 (tu:L-M4).
- **Cross-half results relied on, each checked to be used within the hypotheses at its label:**
  - tu:U-kernel: K ≥ 0, commuting square roots, ‖K‖ ≤ 1.
  - tu:U-K: η := β^{−1/8} ∈ (0, 1], β > 1, β′ > 0 for large β.
  - tu:U-R(1): fibre norm.
  - tu:U-F: any η > 0; used with η/2.
  - tu:U-B: η ∈ (0, 1/2] covers 0.4; real eigenfunctions g and f with eigenvalue ≥ e^{−η/4}; C(η) is a bound on the square of the norm. It **also needs δ, τ and the (W1)/(W3) choices fixed, which this half does not do** (item 25).
  - tu:U-weight / tu:U-W13: Φ vanishes on {ε < η}, but **φ_min > 0 is not stated there** (item 8).
  - tu:U-I1: D_β, β > 1.
  - tu:U-bessel: δ = β^{−1/3} ≤ 1.
  - tu:U-main: liminf, used only in tu:L-limit.

## Failed predicates

1. **prog1 C10 — my own defect, not the target's.** exp(β cos θ) overflowed at β = 1e4 and gave nan. I reran with the identical predicate in a scaled form (prog1b): MET, ratio k/k_min ≥ 1.57.
2. **Child Q2b — the child's own expectation, not the target's.** It used double precision for (h−2)(1+2S²h) = h at S ~ 1e6 (cancellation in h−2). Its 60-digit recheck: error 1e-48.
3. **Referee "predicate" A (item 25), against the brief's question.** "Every β ≥ β₀ threshold is a function of the fixed parameters only" is not met as written: β₁ of tu:U-B depends on δ and τ, which are never fixed in this half. This is a **defect of the target** (completeness), and it is repairable.

**Measured only (M7, β = 1e4, η = 0.4, 6 points of the tube):** the true one-step defects are d₁ ∈ [−0.18, +0.05] and d₃ ∈ [−0.03, +0.21], against the margin m/2 = 0.0151. So the hypotheses of tu:L-S4 are not met at β = 1e4. The note claims only β → ∞, so this is not a defect, but no finite β₀ is exhibited anywhere (the note says so itself).

## What I did not check

- The first half's proofs. Its results were taken as given; only their use was checked.
- No Lean file was compiled for this report. /home/user/z4-lean/READY exists, but I used no Lean; the note's "Lean-checked" claims (corner.lean, delta_h) are unverified by me.
- No numerical check of tu:L-C, tu:L-Pc or Cor tu:L-B on a discretized operator (by hand only).
- No check of tu:L-L4's trial-vector cross terms numerically, nor tu:L-norm or tu:L-M4 numerically.
- (E2) was not tested by Monte Carlo.
- The H_Ψ used in M3 is a numerical sup on a 4e5-point grid; the worst ratio of 0.33 leaves ample room.
- The repo files cited in the note (prog/gap_dh.py, check_gaps.py, child/grid.py) are not available and were not run.

## Delegated questions and outcomes

- **Child, task T182** (admitted under T180, released). Question: recompute the explicit constants and scalar inequalities Q1–Q7: c*, flat identities, M_A² and M_{c1}² tables, the Δh/arcsin scalar facts, the margin values, and the S4 scalar grid.
  - Control: ∫₀^π sin² = 1.570796. **Graded correct** before I read anything else.
  - Outcome: all of Q1–Q7 agree. Remark: the first branch of max{} in M_A² is active on all of [1e-3, 0.4].
  - I reran its pcp_q.py in child_rerun/ through my register (check K2): output identical.
- **Grandchild, task T183** (admitted under T182, released by the child). Question: an independent quadrature of c* with boundary and symmetry checks.
  - Reported 4.605413194531, which agrees with my prog1 C1 (4.6054131945).

## What a reader of another lineage should look at first

1. **§8.1 parameter list.** Do δ, τ, χ, Θ̃ and C really get fixed as functions of η, and is (B)'s β₁ uniform once they are? This is the only place where "β ≥ β₀(η)" is not literally justified.
2. **tu:L-gauss exact gap (eq. tu:L-gap-exact).** The algebra is new and was written for this note. My check is numerical (to 1e-11) plus by hand, and both of us are the same family.
3. **tu:L-S4 Steps 3(c)–5.** These are the reduction x_c = e^{−M²+kV/2} and the AM–GM exponent bookkeeping that carries the whole subsolution. The grid slack on the strip is only 8e-5 at small η.
4. **tu:L-balls case (II) together with tu:L-sub on all of X.** This is the step that produces the tent exponent 2Ψ(π/2) rather than 2Ψ(π−a₋).
5. **The proof of the cross-half input tu:U-B**, especially for f (not positive). The lower half's mass bounds depend on it entirely.

## Exact commands to rerun

```
cd /home/user/z4-workers/v1-chL
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"            # control.txt (0.272341)
$P init pcp --principal principal --principal-name "Kirtus Justus"
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label v1-chL-child --parent T180         # -> T182
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T182
$P check --ws pcp --name child-rerun-pcp_q --cwd child_rerun --expect-exit 0 -- python3 pcp_q.py
$P check --ws pcp --name prog1_constants --expect-exit 0 -- python3 prog1_constants.py
$P check --ws pcp --name prog1b_kmin --expect-exit 0 -- python3 prog1b_kmin.py
$P check --ws pcp --name prog2_model --expect-exit 0 -- python3 prog2_model.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Result files are opened with mode "x": delete result_prog*.txt (and child_rerun/results_q.txt) before rerunning in a fresh copy.

Last lines of the verifies:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Note: the register labels the checks K1–K5 in run order (K1 child-run1, K2 child-rerun, K3 prog1, K4 prog1b, K5 prog2).
