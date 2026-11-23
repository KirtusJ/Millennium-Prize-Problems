# r12-vol report (builder, positive arc): a volume-uniform lower bound for the flowed correlator

Control: `control.txt` = 0.272341 (−ln tanh 1).

## Verdict table

| item | verdict | evidence |
|---|---|---|
| V1 at t = 0: C_{b,s}(0) ≥ (2/l³)[A·P_b − B′·Ψ′_b], with A ≍ s^(−5/2), B′ ≍ s^(−3/2) | STANDS (text proof, algebraic core in Lean) | P1: L ≤ C in 18/18 cases. L/C = 0.26 (bump) and 0.06 (∫f = 0) at s = 0.001, the same for l = 1, 2, 4 |
| V1 for t > 0: C(t) ≥ C(0)·exp(−t·M₁/M₀) ≥ L·exp(−t·Ū₁/L) | STANDS (Jensen is in Lean; the M₁ bound is B3's) | not run numerically: measured only, NOT CHECKED |
| V1 in the brief's form (int f², ‖∇f‖₂) | PARTIAL | proved with the lattice quantities P_b = b³Σf² and Ψ′_b = l⁻³Σ_q\|q\|²\|f̂_b(q)\|². The passage Ψ′_b ≤ ‖∇f‖₂² + aliasing error is not written. Only Ψ′_b ≤ (π²/4)l³‖∇f‖_∞² is available |
| V2: int f ≠ 0 removed; uniform in l | STANDS | no step uses ∫f. The constants depend on l only through Poisson errors e^(−l²/(16s)) and tails. P1 holds for the ∫f = 0 f, and L > 0 for it at s = 0.001 |
| V2: bound is non-vacuous for the brief's f at all s | DEFECT (of my bound's constant) | L > 0 needs sΨ′/P ≲ 0.14. Measured sΨ′/P = 0.077 / 0.155 / 0.387 at s = 0.001 / 0.002 / 0.005, so L < 0 at s = 0.002 and 0.005 (P3 failed 6/9) |
| V3: M₁/M₀ ≤ c/√s and M₂/M₀ ≤ c/s proved | STANDS under the hypothesis sΨ′_b/P_b ≤ θ < A s^(5/2)/(B′ s^(3/2)) ≈ 0.14 | follows from B3's upper bounds and the new L. Not evaluated numerically |
| V4 numerics (36 predicate instances) | see counts | P0 2/2, P1 18/18, P2 18/18, P4 18/18, P3 3/9 |
| V5 Lean | STANDS | `lean/R12Vol.lean`: exit 0. `#print axioms` shows only propext, Classical.choice, Quot.sound for all 6 theorems. No sorry |
| child number C = 2.177968313057 | STANDS | my own code reproduces it to 2.2·10⁻¹⁴ relative (run K2) |

Counts (met, failed, measured only): **59 met, 6 failed, 4 measured only**.
- Met: P0 2, P1 18, P2 18, P3 3, P4 18.
- Failed: P3 6.
- Measured only: L/C, R/true, sΨ′/P, and t > 0.

## The proof (t = 0, then t > 0)

Notation:
- φ(v) = g(v)e^(−2s\|v\|²), with g(v) = \|v_⊥\|²/(2\|v\|) and v_⊥ = (v₁, v₂).
- a(k) = φ(k̂vec(k)). This is the brief's a at t = 0.
- C = (2/l⁶) Σ_q \|f̂_b(q)\|² G(q), with G(q) = Σ_k a(k) a(q−k) (B1 step 1, upheld).

1. **Lattice → continuum, termwise.** Take \|k\|_∞ ≤ K ≤ π/b and ε = K²b²/24 < 1.
   - From sin y ≥ y − y³/6: k̂_i ≥ \|k_i\|(1−ε).
   - Also k̂ ≤ \|k\|.
   - Hence a(k) ≥ (1−ε)² φ(k). Elsewhere a ≥ 0.
2. **Pair bound (second order in q).** Put u = p + q/2, w = q/2 − p.
   - The Gaussians combine exactly: e^(−2s(\|u\|²+\|w\|²)) = e^(−4s\|p\|²) e^(−s\|q\|²).
   - \|u\|\|w\| ≤ \|p\|² + \|q\|²/4.
   - \|u_⊥\|²\|w_⊥\|² ≥ (\|p_⊥\|² − \|q_⊥\|²/4)² ≥ \|p_⊥\|⁴ − \|p_⊥\|²\|q\|²/2 [Lean `perp_prod`, `sq_sub_ge`].
   - Hence 4g(u)g(w) ≥ \|p_⊥\|⁴/\|p\|² − (3/4)\|q\|² [Lean `pair_core`] ≥ p₁² + p₂² − p₃² − (3/4)\|q\|² [Lean `sq_div_ge`].
   - When the numerator is negative, the bound holds trivially.
   - An earlier version used (\|p\| + \|q\|/2)² for \|u\|\|w\|. It gave a first-order error of about 4.5·η and was vacuous, so I discarded it.
3. **Region.** For \|q\|_∞ ≤ Q ≤ K, keep the shifted cube \|p\|_∞ ≤ K′ = K − Q/2. Every kept term then has \|k\|_∞, \|q−k\|_∞ ≤ K. The lower bound is a product of 1-D sums S₀ = Σe^(−4sp²) and S₁ = Σp²e^(−4sp²) on grids of spacing Δ = 2π/l with arbitrary shift:
   G(q) ≥ (1−ε)⁴ e^(−s\|q\|²)/4 · [2L₁L₀² − U₁U₀² − (3/4)\|q\|² U₀³].
4. **1-D sums, uniform in shift.**
   - Full-line sums use Poisson summation, which is exact for Gaussians: \|ΔS₀/√(π/α) − 1\| ≤ δ₀ = 2Σ_{m≥1} e^(−m²l²/(4α)), with α = 4s. Likewise for S₁, with δ₁ = 2Σ\|1 − m²l²/(2α)\| e^(−m²l²/(4α)).
   - Truncation tails are bounded by the integral from K′ − Δ. This needs K′ − Δ ≥ 1/√α, so that the summand is decreasing there.
   - This is the Riemann-sum lemma used. Its hypothesis is a Schwartz function for Poisson, plus monotone tails.
5. **Linearize in \|q\|².** Write A = (1−ε)⁴(2L₁L₀² − U₁U₀²)/4 and B′ = (1−ε)⁴(3/16)U₀³ + sA.
   - Using e^(−x) ≥ 1 − x [Lean `gauss_lin`, needs B ≥ 0]: G(q) ≥ A − B′\|q\|² for \|q\|_∞ ≤ Q.
   - For \|q\|_∞ > Q, the requirement Q² ≥ A/B′ makes the right side ≤ 0 ≤ G.
   - Hence the bound holds for every BZ representative q.
6. **Sum against \|f̂_b\|².** Parseval gives Σ_q\|f̂_b\|² = l³P_b. So
   **C_{b,s}(0) ≥ L := (2/l³)[A P_b − B′ Ψ′_b].**
   - Asymptotically (l/√s → ∞, b/√s → 0): (2/l³)A s^(5/2) → (5/8)·√π/(640π²) = 1.754·10⁻⁴. The factor 5/8 is the angular loss of the x − y step.
   - With κ = 2.5, θ = 0.5 and b = √s/2 the numbers are 0.48·(true) and B′-term ≈ 3.4·(true)·s. So L ≈ 0.48·2.806·10⁻⁴ s^(−5/2)(P_b − 7.0 sΨ′_b).
7. **t > 0.**
   - The atoms W_{kk′} ≥ 0 at E = k̂ + k̂′ (B1 step 1). Jensen [Lean `jensen_exp`] gives C(t) ≥ C(0) e^(−t M₁/M₀).
   - B3 gives M₁ ≤ (4/l³)Φ√(A₀A₂) =: Ū₁, and M₀ = C(0) ≥ L. Hence C(t) ≥ L·exp(−t Ū₁/L).
   - Since Ū₁ ≍ Φ s^(−3), we get Ū₁/L ≍ (Φ/P_b) s^(−1/2). So c(τ) = c₀ e^(−c₂τ), with τ = t/√s.
8. **V3.** M₁/M₀ ≤ Ū₁/L and M₂/M₀ ≤ (4/l³)Φ(√(A₀A₄) + A₂)/L.
   - The numerators scale as s^(−3) and s^(−7/2) by the explicit U_q bounds.
   - So both ratios are ≤ const·s^(−1/2) and ≤ const·s^(−1), provided sΨ′_b/P_b stays below a fixed θ < A/(B′s) (≈ 0.14 here).

Missing step, named:
- The comparison of P_b and Ψ′_b with ∫f² and ‖∇f‖₂² is not done. For P_b, the aliasing lemma applied to f² at q = 0 gives P_b ≥ ∫f² − S₄(b/2π)⁴‖Δ²(f²)‖₁ (PROOF_FREE_BOUNDS 2b, cited, not rechecked).
- For Ψ′_b, I only have the crude bound (π²/4) l³ sup\|∇f\|². So the "‖∇f‖₂" form of V1 is **not proved**.
- The uniform-in-c form of the U_q bounds used in steps 7 and 8 is written in one line, not checked numerically.

## Hypotheses used and where stated

| hypothesis | where stated |
|---|---|
| H1 (normalization of D, flow factor once per field) | THEOREMS_B |
| H2 (Wick), HΩ = 0 | SETTING / THEOREMS_B |
| f real and periodic (C⁴ only for the aliasing step). **∫f ≠ 0 is not used** | THEOREMS_B (H3, weakened here) |
| b, s, l: ε = K²b²/24 < 1; K ≤ π/b; Q ≤ K; K − Q/2 − 2π/l ≥ 1/(2√s); Q² ≥ A/B′. In V4 this is b ≤ √s/2 and l/√s ≥ 14 | here, step 1–5 and `vol.py` lower_consts |
| B1 step 1 (momentum representation), B3 upper bounds on M₁, M₂ | THEOREMS_B (upheld by challenger) |
| Poisson summation for Gaussians; Jensen | standard; Jensen in Lean |

## Failed predicates

- **P3 (L > 0 for the bump), 6 of 9 failed.** All at s = 0.002 and 0.005, for l = 1, 2, 4.
  - This is my own expectation, not a defect of the target.
  - L > 0 needs sΨ′/P ≲ 0.14, and the bump of width 0.15 gives 0.155 and 0.387. √s = 0.045 to 0.071 is not well separated from 0.15.
  - The true deficit is real but about 10× smaller: R/true = 0.88 and 0.73.
  - The bound's q²-coefficient is about 10× loose.
- Brief defect: the child's control answer "0.00028061" given in the brief is wrong. √π/(640π²) = 0.0002806049, which is 0.00028060 to 8 decimals. The child answered 0.00028060, which is correct.
- Lean, first compile: `gauss_lin` was false as I first stated it (it needs B ≥ 0), and one `jensen_exp` rewrite was wrong. Both were fixed. The final file compiles.

## Numbers (t = 0; `results_vol_run1.json`)

R = C s^(5/2)/P_b and R/true, with true = √π/(640π²).

- Bump, s = 0.001 / 0.002 / 0.005: R/true = 0.942 / 0.881 / 0.747 (l = 4). For l = 1 and l = 2 the values agree to within 0.015.
- ∫f = 0 (x₁-derivative): R/true = 0.901 / 0.816 / 0.644.
- L/C:
  - s = 0.001: 0.26 for the bump and 0.06 for ∫f = 0.
  - s = 0.002: L < 0.
  - s = 0.005: L < 0.
- C/V = 0.014 to 0.047. V is the B1 bound with Φ = b³Σf².
- N = ⌈2l/√s⌉, which ranges from 29 to 253. b ≤ √s/2 in all 18 cases.

## What I did not check

- t > 0 numerically.
- The V3 ratio bounds numerically.
- Ψ′_b against ‖∇f‖₂².
- The aliasing step for P_b.
- Whether a sharper q²-coefficient (≈ 0.7 is suggested by the data, against 7 proved) is provable.
- The 1-D unimodal/Poisson lemmas are not in Lean.

## Delegated questions

- **Child (sonnet, run `child-run1`, exit 0).**
  - Question: an independent FFT value of C_{b,s}(0) at l = 1, N = 48, s = 0.005, with f = ∏g(y_i), g(u) = Σ_{m=−2..2} exp(−(u − 0.3 − m)²/(2·0.15²)).
  - Control graded first: correct (see above).
  - Returned C = 2.177968313057, b³Σf² = 0.01879479225576 and ratio 2.0485·10⁻⁴.
  - I reran it with my own code (`rerun_child.py`, K2): C = 2.1779683130570, relative difference 2.2·10⁻¹⁴, so it passes.
- **Grandchild (child's sub-agent).**
  - Question: at N = 8, does a brute-force (k, k′) momentum double sum equal the position-space value?
  - Returned: agreement to 2.4·10⁻¹³.
  - The child reran it (its K3). My own P0 checks the same identity at N = 6 independently (≤ 4.7·10⁻¹⁶).

## Register

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp` → `Result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` → `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## Rerun commands

The result files are opened with mode "x", so delete or rename the old outputs first.

```
cd /home/user/z4-workers/r12-vol
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
OMP_NUM_THREADS=1 $P check --ws pcp --name vol-run2 --expect-exit 0 --timeout 600 -- python3 vol.py results_vol_run2.json
$P check --ws pcp --name rerun-child2 --expect-exit 0 -- python3 rerun_child.py results_rerun_child2.json
$P check --ws pcp --name lean-R12Vol-2 --expect-exit 0 --cwd /home/user/z4-lean -- bash -c "PATH=$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/r12-vol/lean/R12Vol.lean"
$P check --ws pcp --name child-run2 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

The agreement of the director's model family with mine is not independent review. The proof steps 1–6 should be attacked by a challenger, above all step 3, where the region choice must keep \|k\|_∞ and \|q−k\|_∞ ≤ K, and step 4, the Poisson and tail bounds.
