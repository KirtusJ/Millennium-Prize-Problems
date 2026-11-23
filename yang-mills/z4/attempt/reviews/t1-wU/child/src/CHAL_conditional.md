Overall verdict: given Lemma F, I could not break Lemma R, Lemma K or the conditional theorem liminf (−log m_eo)/√β ≥ c*. The one false line I found (§5, the sign-trial identity) is off by a factor of 2 in the prefactor only, and the 1-D model is consistent with c* being the right constant.

Worker n1-chalT, task T135. I share a model family with the author and the director, so my agreement is not independent review. The 1-D computation was redone by a lower-tier child (T136) and a grandchild (T137) using different code.

## Verdict table

| # | item | verdict | evidence (one line) |
|---|---|---|---|
| 1 | Lemma R(i): the fibre well is the circle {x₁=x₂=0} | STANDS | V_a = 2βs²(x₁²+x₂²) vanishes exactly there. |
| 2 | Lemma R(ii): reduction to Legendre in t | STANDS | Torus double-coset invariance, t = cos 2χ is uniform, D^j₀₀ = P_j(t), K₂ eigenvalue I_{2j+1}/I₁, V_a = βs²(1−t); all rechecked by hand. Harmonic cross-check: the exact 1-D Mehler eigenvalue is e^{−asinh s} per transverse direction, so two directions give 2 asinh s = ε. |
| 3 | Lemma R(iii): numerical c(a) table | NOT CHECKED | eps_eff.py was not rerun. |
| 4 | (a) K₂^{1/2} exists; T = B*K₁B; B*B is fibrewise F_{U₁} with ‖F_{U₁}‖ = e^{−ε_eff(a₁)} | STANDS | K₂ is convolution by a central kernel with multipliers I_{n+1}/I₁ > 0. K₁ and K₂^{1/2} commute. Conjugating U₂ commutes with K₂, so the fibre norm depends on a₁ only. |
| 5 | Lemma K: statement and proof | STANDS | I rechecked every inequality: inner region (Lean `one_sub_cos_ge`, rerun), outer mass 2π², denominator ≥ (2π/β)^{3/2}(1−1/β) using Eθ² = 3/β. With η = β^{−1/8} the error is additive, O(β^{−1/4}). |
| 6 | (b) C² weight Φ∘a at the centres; Lipschitz and Hessian constants | STANDS | Φ ≡ 0 on I = {ε<η}, a neighbourhood of a₁ ∈ {0,π}. Hess(Φ∘a) = Φ''∇a⊗∇a + Φ' cot a (g − da⊗da) is bounded because Φ' = 0 near the poles, so H = H(η,τ). L = √(2ε(π/2)) = 1.8776. The constants are not written explicitly, but only their finiteness is used. |
| 7 | (b) Schur step: direction, and the bound e^{Φ'²/2 + o(1)} | STANDS (one missing line) | AM-GM plus symmetry of k gives an upper bound on the quadratic form, which is the needed direction. The missing line is the Taylor reduction cosh(√β(p·X + R)) ≤ cosh(√β p·X)·e^{√β Hθ²/2} with \|R\| ≤ Hθ²/2. It is trivial and repairable. o(1) is uniform because \|Φ'\| ≤ L and H is fixed. |
| 8 | (c) What E is; the region ε < E | STANDS | E = −log λ_ee = O(β^{−1/3}) by the gauge-invariant bump trial (rechecked). It is absorbed into the fixed η, and {ε < E} ⊂ I for large β. On I^c, q ≤ −3η/4 + o(1) < −η/4 ≤ log λ. |
| 9 | Estimate (B): ‖e^{√βΦ}g‖² ≤ C(η)‖g‖² | STANDS | Follows from (A), Lemma F with η/4, and λ ≥ e^{−η/4}. |
| 10 | (d) Sign-trial identity "½∫∫(s(x)−s(y))² gTg = 2⟨g1_A, T g1_{A^c}⟩" (§5) | DEFECT (prefactor only; repairable) | The correct value is 4⟨g1_A, T g1_{A^c}⟩, since 1 − s(x)s(y) = 2 on cross pairs and both orderings count. The 1-D analogue at β=16 gives a ratio of 2.0000000 to the paper's 2⟨…⟩ (M7). Exponent and conclusion are unaffected. |
| 11 | (d) The exponent is the full Agmon distance c* = ∫₀^π √(2ε), not half or double | STANDS | f(a_x) + f(π−a_y) ≥ 2f(π/2) − L(a_y−a_x) = c*_η − L·d₁. This is barrier mass e^{−√β c*/2} squared. The 1-D model's ratio rises to 4.493 at β = 16384 with local slope 4.56, so the limit is not c*/2 or 2c*. |
| 12 | (e) The cut at a₁ = π/2 for non-local K₁; cross terms | STANDS | The identity is exact for any symmetric kernel. Cross terms carry e^{−√β(Φ(x)+Φ(y))}, the weight on both sides. They are controlled by T ≤ K, Schur, and E_k e^{√βLθ} = O(1) (radial Lemma K, outer region e^{−β^{3/4}/2}). (B) is used on both sides via ‖h‖². |
| 13 | Conditional theorem liminf (−log m_eo)/√β ≥ c* | STANDS (given Lemma F) | Chain: m ≤ (λ_ee−λ_eo)/λ_eo, with λ_eo ≥ ⟨sg,Tsg⟩ → 1 (implicit). Then let δ, τ, η → 0, with c*_η → c* at rate O(√η). |
| 14 | (f) §6, the 2-D valley | STANDS as "not used" | §4–5 use only Lemma F, which takes the sup over all U₂. §6 is heuristic. Its minimiser claim and m_oo/m_eo → 2 are NOT CHECKED. |
| 15 | (g) Lean file | STANDS (scope is small) | Exit 0; axioms are only propext, Classical.choice, Quot.sound; no sorry. It proves only two scalar facts: arsinh monotonicity (valley) and 1 − cos θ ≥ (θ²/2)(1 − 5η²/48). Nothing in §4–5 beyond that inequality is formalised. |
| 16 | The 1-D model reproduces c* (my program plus the child's) | STANDS (consistent; a finite β cannot prove a limit) | −log m/√β: 3.898, 4.165, 4.328, 4.429, 4.470, 4.493 at β = 64…16384. Local slopes 4.433, 4.491, 4.530, …, 4.562 increase toward c* = 4.6054. 3-parameter fit c = 4.5635 (4 points) and 4.5788 (5 points). |

**Verdict counts: STANDS 14, DEFECT 1, NOT CHECKED 1.** (Partial NOT CHECKED items are listed below.)

**Predicate counts (my programs): met 15, failed 6, measured only 5.**
- Met: M1, M2×3, M3×4, M5, M6, M7, M8, E2, plus the Lean pass counted as one.
- Failed: M4×4, E1, E3.
- Measured only: the ratios, fit b and c0, local slopes, θ = 0.95 diagnosis, and the naive-difference comparison.

## Hypotheses each statement uses, and where they are stated

- **Lemma R:** β > 0; the Wilson kernel is positive with positive character coefficients (§0, "Kernel"); V = 2β\|u₁×u₂\|² (§0); top eigenvector simple by strict positivity (§1(ii)).
- **Lemma K:** β > 1, p ∈ ℝ³, H ≥ 0, 0 < η ≤ 1, β' > 0 (§3, Statement). It uses the exponential-coordinates Haar density (sin θ/θ)² (§3 preamble).
- **(A):** Φ is a function of a₁ only, with Φ∘a C² on SU(2) (§4, first line). Lemma K is applied with p = ∇(Φ∘a) and H = ‖Hess‖_∞ (§4, Result).
- **(B):**
  - Lemma F with η/4 (§4 bullets; Lemma F stated in §2).
  - λ_ee ≥ 1 − O(β^{−1/3}) (§4 bullet: proved by sketch, also CITED from A4).
  - The choice of weight (§4, "Choice of weight").
- **Theorem (§5):**
  - (B).
  - T ≤ K pointwise, from V ≥ 0.
  - The class angle is 1-Lipschitz.
  - The radial Lemma K bound E_k e^{√βLθ} = O(1). This is stated in §5 but not written as a lemma: a missing line, repairable by the same proof.
  - λ_eo bounded below. This is implicit.
- **§6:** harmonic linearisation at the valley (§6 bullets). Not used by §5.

## Failed predicates (all kept)

| predicate | what failed | whose defect |
|---|---|---|
| M4 (×4 β) | Grid h = 1/(5√β) vs 1/(8√β) changes log m by 2.0e-3 to 3.8e-3, more than my 1e-6 tolerance. | **My expectation.** ε = 2 asinh\|sin a\| has a kink at the wells, so the discretised model's prefactor depends on h at O(h²). The child's P1 (tolerance 1e-3 on the ratio) passed. The exponent is unaffected. |
| E1 | 5-point fit c = 4.5788, which is 0.58% from c*; my tolerance was 0.5%. | **My expectation.** The 3-term fit form leaves residuals of about 0.03 (child's note), and the local slopes are still rising. |
| E3 | θ = 0.9 vs θ = 1 at β = 16384 differ by 7.9e-5 in log m. | **My tolerance argument.** At θ = 0.9 the rescaled tail is 1.5e-10 relative, so eig round-off is about 1e-6 relative. θ = 0.95 agrees with θ = 1 to 2e-12 (diagnosis run inline, not a result file). |

There are no failed predicates that point to a defect of the target. The target's one defect (item 10) came from hand-checking and was confirmed by M7, which was met.

## What I did not check

- Lemma F itself. It is taken as given per the brief.
- The numerical table in §1(iii): eps_eff.py was not rerun.
- The A4 citation for λ_ee → 1. I checked the bump-trial sketch only.
- The precise constants H(η, τ) and C(η, τ).
- Existence of the smoothing ρ_η and of the kink smoothing with \|f̃'\| ≤ \|f'\|. Both are standard, but neither is written out.
- §6's path-minimiser claim and m_oo/m_eo → 2.
- §7 (limsup ≤ c*). It is declared MISSING by the author, and I agree.
- The SU(2) model's actual splitting. My 1-D model has no Haar Jacobian sin²a and no transverse fibre.
- β → ∞. Finite β up to 16384 is consistent with the limit, not a proof of it.
- theory.py and kernel_lemma.py were not rerun.

## Delegated questions and outcomes

- **Child (T136)**, admitted with parent T135 and released (child_admit.log, child_release.log). Run as check `child-run1`, exit 0, 188 s.
  - **Question:** the 1-D circle model's splitting m for β ∈ {64, 256, 1024, 4096}, and a fit of c.
  - **Control:** c* to 6 decimals. It answered 4.605413: graded CORRECT before I read anything else.
  - **Result:** STANDS (consistent), fit c = 4.5635.
  - **My check:** I reran its split.py in child_rerun/ (check `child-split-rerun`, exit 0). On grid h its log m agrees with my independent code to ≤ 7e-12 at all four β.
- **Grandchild (T137)**, admitted by the child under T136 and released (per the child's report).
  - **Question:** log m at β = 64 by an independent route.
  - **Control:** top eigenvalue of [[2,1],[1,2]] = 3 (passed).
  - **Result:** 90-digit decimal direct eigenvalue difference, log m = −31.180578395507448542. Mine is −31.180578395507386, a difference of 6e-14.
  - **My check:** I read its results.txt and the head of run.py. I did not rerun it myself; the child reran it in child/gc_rerun.
  - This gives a high-precision confirmation, independent of my identity method, at β = 64. My own M2 reached only β = 16.

## PCP OS record

- `python3 pcp_os.py verify --ws pcp` → "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl` → "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

Checks recorded:

| check | name | exit | expected |
|---|---|---|---|
| K1 | model1d-run1 | 1 | 0 |
| K2 | child-run1 | 0 | 0 |
| K3 | model1d-ext-run1 | 1 | 0 |
| K4 | lean-tunnel | 0 | 0 |
| K5 | child-split-rerun | 0 | 0 |

## Rerun commands

Result files are opened with mode "x", so use a new tag or remove the old result first.

```
cd /home/user/z4-workers/n1-chalT
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control 0.272341
$P check --ws pcp --name model1d-run2 --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 model1d.py run2
$P check --ws pcp --name model1d-ext-run2 --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 model1d_ext.py run2
$P check --ws pcp --name lean-tunnel2 --cwd /home/user/z4-lean --expect-exit 0 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/n1-chalT/Tunnel_check.lean'
mkdir child_rerun2 && cp child/split.py child_rerun2/ && $P check --ws pcp --name child-split-rerun2 --cwd child_rerun2 --expect-exit 0 -- env OMP_NUM_THREADS=1 python3 split.py
$P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Expected exits: model1d.py exits 1 (M4 fails) and model1d_ext.py exits 1 (E1 and E3 fail). Those failures are recorded above.
