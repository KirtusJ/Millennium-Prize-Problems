In my reading M0 (c β^{-1/3} ≤ E_0 ≤ C β^{-1/3}, k = 2, 3) and M1 ((1−λ_j)/h → e_j, gap/h → e_1 − e_0 > 0, center-even gauge-invariant sector, k = 2, 3) both stand as written proofs: I found no false line, only one wording slip ("concavity" for the convexity chord bound in M0); the Lean files prove only scalar lemmas, and the k = 2 exact numerics agree with the M1 limits (−log λ_0/h → 3.3537, −log λ_1/h → 5.3316 against e_0 = 3.3505, e_1 = 5.3255), while (1−λ_j)/h is still 16–23 % low at β = 1024.

Worker h1-a4, task T88. Control: control.txt = 0.272341. Lean: /home/user/z4-lean/READY exists; both target Lean files were rerun.
Caveat: I share a model family with Director Z4. My agreement is not independent review. The author is of a different lineage.

## 1. Verdict table

| # | item | verdict | evidence (one line) |
|---|---|---|---|
| 1 | M0 smoothing: density ≤ Σ n²(I_n/I_1)^j ≤ C d^{-3} | STANDS | \|χ_n\| ≤ n and the eigenvalue I_n/I_1 per rep; the Gaussian piece O((β/j)^{3/2}); n<8 and n>β pieces bounded. The target check's scaled partial sum is 1.264, 1.256, 1.254 at β = 64, 1000, 32768 (shim run K14). |
| 2 | M0 Bessel-ratio bound I_n/I_1 ≤ (1+n/β)^{-n/8} | STANDS | The recurrence step is exact. The ≈n/4 pairs centred at ≥ n/2 give exponent ≥ n/8. Child grid (my rerun K4): 255,552/255,552 met for n = 8..4000, β ∈ [1, 10⁴]. Least slack 0.0023505 at n=8, β=10⁴, confirmed by the grandchild at 40 digits (my rerun K13). |
| 3 | M0 displacement 2(1−q^j) ≤ 8j/β | STANDS | 1−q ≤ 1−I_3/I_1 = 4q/β ≤ 4/β, and E[U] = q^j·1 in the fundamental rep. Lean `fundamental` is this scalar step. |
| 4 | M0 tube volume ≤ C R d (εd)² | STANDS | In coordinates (√(1−\|w\|²)e^{it}, w) the Haar density is constant in dt dw. The arc inside a ball of radius Rd is O(Rd), uniformly in the start. |
| 5 | M0 escape Pr{V(X_j) ≥ a/m} ≥ 1/2 | STANDS | 8/R² + CRε² + Cε³ < 1/2. V ≥ 2βε⁴d⁴ and mβd⁴ = m³/β ≥ 1 (Lean `productScale`). Target MC: late fraction ≥ 0.98 at β = 64, 1000, 32768. |
| 6 | M0 supersolution (B = (1+V)^{-1}K, φ = Σ_{i<m}B^i1, κ) | STANDS (wording) | (1+V)φ − Kφ = (1+V)(1−B^m1) holds exactly (my F5: error ≤ 1.2e−15). The line "Concavity on 0 ≤ N/m ≤ 1" should read "convexity of s ↦ e^{−cs} (chord bound)". The inequality is correct. |
| 7 | M0 lower bound −log λ_0 ≥ κ/(2m) | STANDS | The numerator ⟨g,(I−K+W)g⟩ over the denominator ‖g‖² + ⟨W⟩ with W = e^V−1 ≥ V. The two-case split is correct. The ground-state identity needs only symmetry of K (my F4: error ≤ 3.2e−16). |
| 8 | M0 upper bound (radial bumps within d of ±1) | STANDS | ⟨f,(I−K)f⟩ ≤ Cβ^{-1}‖∇f‖² and ‖∇f‖² ≤ Cd^{-2}‖f‖². W ≤ Cβd⁴ with βd⁴ → 0, so the bound is O(β^{-1/3}). Numerics: −log λ_0·β^{1/3} = 3.06 … 3.32 for β = 32 … 1024 (k=2). |
| 9 | M0 three directions | STANDS | K_3 fixes φ(u_1,u_2), and the extra commutator terms are ≥ 0. |
| 10 | M1 (1) I − K_j + V_ij ≥ c r, uniformly, r ≥ h | STANDS | m = ⌈8/r⌉ ≤ 9/h. mV_ij ≥ 2ε²(mr)² ≥ 128ε² on the good event (Lean `fiberScale`). Discretised fibre (exact torus reduction): min μ/r on [h,1] is 0.976 (β=64) and 0.976 (β=256), attained at r=1. Near r=h, μ/r = 1.70 and 1.82, close to the oscillator value 2. |
| 11 | M1 "B^m1 ≤ 1−κ"; "Σ_{a<m}B^a1 gives I−K_j+V_ij ≥ κ/m"; is B = (1+V)^{-1}K right? | STANDS | (I+V−K) = (1+V)(I−B) exactly, so B is the right operator for the form I−K+V. Checked exactly on the discretised fibre (F4, F5, F6 met in 24/24 cases). Measured max B^m1 ≤ 1.2e−4. κ_eff/m is 7–13 % of μ, so the bound holds but is not sharp. |
| 12 | M1 (2) and the commuting valley | STANDS | K ≤ K_j (commuting positive contractions) and V ≥ V_ij. (1) penalises every link with \|u_i\| ≥ h, whatever the other links' angles: pairs or triples with a common axis and any class angles are covered. Only max_i \|u_i\| ≲ Rh is left, and that is the compact scaled region. |
| 13 | M1 numerator identity ⟨F,(I−T)F⟩ = ⟨g,(I−K)g⟩ + ⟨g,(e^V−1)g⟩ | STANDS | ‖F‖² = ⟨g,e^Vg⟩ and ⟨F,TF⟩ = ⟨g,Kg⟩. Child random test (my rerun K3): 600/600, max rel 5.1e−16. ‖F−g‖² ≤ ‖F‖² − ‖g‖² (Lean `weightLoss`). |
| 14 | M1 (3) 1−K ≥ c′ min(D/β,1) | STANDS (β ≥ β_0) | Use the largest-Casimir factor (Lean `coarseDefect`). n ≥ 8 by item 2. For 2 ≤ n < 8: I_n/I_1 = 1 − (n²−1)/(2β) + O(β^{-2}). |
| 15 | M1 isometry J_h on center-even functions | STANDS | Product of hemispheres; density ∝ h^{3k}Π sinc²(h\|x_i\|); the cut has measure zero. |
| 16 | M1 local H¹ bound | STANDS | ‖∇g_<‖² ≤ (β/c′)⟨g,(I−K)g⟩ = O(h^{-2}), so the scaled gradient is O(1). The density's log-derivative is O(h²\|x\|) on balls. |
| 17 | M1 strong L² compactness (local compactness + tightness) | STANDS | (2) gives ∫\|u_i\|\|g\|² = O(h) for each i. Mass{θ_i > Rh} ≤ (π/2Rh)·O(h) = O(1/R). A union over i ≤ 3 controls max_i θ_i, which covers all directions of (R³)^k. Rellich applies on balls. |
| 18 | M1 (4) J_h(I−T)ψ_h/h → Hψ in L² | STANDS | Remainder ≤ C E\|ξ\|³‖∇³w_h‖ = O(β^{-3/2}h^{-3}) = O(h^{3/2}), globally in L² by Haar invariance. Leaving the chart is harmless: J_h is isometric on all center-even functions and the quadratic term has compact support. The quadratic term is E[ξ_1²]Dw/2 with β h³ = 1, which gives −Δ/2. |
| 19 | M1 §4 form core; compact resolvent (k = 2 and 3) | STANDS | H ≥ 2\|x_i\| for each i (2-D transverse oscillator of frequency 2\|x_i\|; the other terms are ≥ 0). With H ≥ −Δ/2 this gives a compact embedding for k = 2 and 3. |
| 20 | M1 simplicity of the ground state on the invariant subspace | STANDS | The semigroup is positivity improving, so the ground state is unique and positive, hence rotation invariant. Therefore e_1(invariant) ≥ the second full eigenvalue > e_0. |
| 21 | M1 liminf (eigenvectors → strong limits → weak eigenfunctions → min-max) | STANDS | The strong limits stay orthonormal because J_h is an isometry. Each is an eigenfunction at μ_a. A (j+1)-dimensional span with quotient ≤ μ_j gives e_j ≤ liminf, multiplicities included. |
| 22 | M1 limsup by min-max with J_h^*ψ | STANDS | The Gram matrix is exact for compact support, and the form matrix converges by (4). |
| 23 | M1 last line −log λ_j = (1−λ_j) + O(h²) | STANDS (as a limit) | Numerics: at β=1024, (1−λ_0)/h = 2.828 and −log λ_0/h = 3.319 against e_0 = 3.351. The O(h) relative correction e²h/2 dominates at reachable β. |
| 24 | Lean ToronVacuum.lean (6 declarations) | STANDS (scalar only) | Rerun K6 exit 0. Axioms: propext, Classical.choice, Quot.sound only; no sorry. SHA-256 9178ba5e… equals checks.md. See §1a. |
| 25 | Lean ToronExcitation.lean (7 declarations) | STANDS (scalar only) | Rerun K7 exit 0, same axioms; no sorry. SHA-256 c4974a58… equals checks.md. |
| 26 | target/check.py | STANDS | Without a shim it does not run (scipy missing, K8). With my numpy `ive` shim (K14, exit 0) it reproduces checks.md: survival 0.401073, 0.263368, 0.214746. |
| 27 | target/excitation/check.py | NOT CHECKED | It does not run (K9): it needs scipy.integrate and scipy.stats.qmc (seeded scrambled Sobol), which cannot be reproduced here. |
| 28 | M1 limits against exact k=2 transfer numerics (item d) | STANDS (measured) | Gaps equal NUMERICS to ≤ 1e−9 (β = 32..1024). Quadratic extrapolation in h of −log λ_j/h: 3.35372 (e_0 3.350533) and 5.33164 (e_1 5.325497). |
| 29 | M1 for k = 3, numerically | NOT CHECKED | Not computed. The cost is as in NUMERICS.md §6. |
| 30 | Cited sources (DLMF 10.32.2, 10.29.1, 10.40.1; Lüscher 1983) | NOT CHECKED | Not fetched. I re-derived the three DLMF formulas used (integral ratio = E x, recurrence, large-argument expansion) and checked them numerically. |

**Verdict counts:** STANDS 27, DEFECT 0, NOT CHECKED 3.
**Predicate counts over my own programs:** met 141, failed 2, measured only 60.
- fibre.py: met 97, failed 2, measured 52.
- transfer2.py: met 23 over 11 runs.
- analyse2.py: met 21; 8 measured-only lines are counted in the 60.

Child predicates, rerun by me: met 4 (PA1 over 255,552 cases, PA2, PB0 600/600, PB1 600/600), failed 0. The grandchild's value was rerun and is identical.

### 1a. What each Lean declaration proves, and the line of text it serves

All are real-number lemmas. None is an analytic statement about operators, measures or Bessel functions.

- `twoStep`: lo − hi = x·mid, hi ≤ mid, x ≥ 0 ⇒ (1+x)hi ≤ lo. This is the step I_{h−1} ≥ (1+2h/β)I_{h+1}, given the recurrence and monotonicity as hypotheses.
- `fundamental`: b(1−z) = 4q, z ≤ q ≤ 1, b > 0 ⇒ b(1−q) ≤ 4. This is 1−q ≤ 4/β.
- `productScale`: b d² = m ⇒ m b² d⁴ = m³. The text uses m β d⁴ = m³/β, which is the same identity divided by b.
- `occupation`: s ≤ 1 − c·f, f ≥ 1/6, c ≥ 0 ⇒ s ≤ 1 − c/6. The convexity step that produces s ≤ 1 − c·E[N/m] is not formalised.
- `superSolution`: pointwise scalar e(1+V) ≤ (1+V)φ − Kφ, φ ≤ m ⇒ eφ ≤ m((1+V)φ − Kφ).
- `finiteSurvival`: Σ_{i<m}u_i − B(Σ u_i) = u_0 − u_m for an additive map with B u_i = u_{i+1}. This is the telescoping identity. It does not include the factor (1+V).
- `fiberScale`: b d² = m ⇒ m b r² d² = (m r)². This is the fibre scale.
- `coarseDefect`: u ≤ 1, v ≥ 0 ⇒ 1−v ≤ 1−uv. This is 1 − Πλ_i ≥ 1 − λ_{i*}.
- `weightLoss`: 0 ≤ a ≤ 1 ⇒ (1−a)² ≤ 1−a². This gives ‖F−g‖² ≤ ‖F‖² − ‖g‖².
- `scaleKinetic` and `scaleQuartic`: ring identities in h.
- `separation`: e_1 − η ≤ a_1 and a_0 ≤ e_0 + η ⇒ e_1 − e_0 − 2η ≤ a_1 − a_0.
- `eventualGap`: convergent sequences with u < v eventually satisfy b_n − a_n > (v−u)/2.

Each is the scalar inequality the text uses at that point. The analytic content (items 1–5, 10–12, 14–22) rests on the written proofs.

## 2. Hypotheses used and where they are stated

M0 (target/README.md):
- Wilson increment density ∝ e^{β Re Tr U/2} against probability Haar measure; K is the product of independent central walks. Stated in the README's opening paragraph.
- T = e^{−V/2}Ke^{−V/2}, V = 2β\|u×v\|². Opening paragraph.
- The temporal gauge projector is the identity on conjugation-invariant functions. Opening paragraph.
- β is sufficiently large: needed for d → 0, εd < 1/2 and m ≤ β. Statement and "Escape".
- Character expansion with dimension convention \|χ_n\| ≤ n. "Smoothing".
- The Bessel integral (DLMF 10.32.2) and recurrence (DLMF 10.29.1). "Smoothing".
- k = 2 or 3. Statement.

M1 (target/excitation/README.md):
- Everything above.
- The sector: gauge-invariant, even under each center flip. Statement.
- h = β^{−1/3}. Statement.
- (1) is needed only for r ≥ h. §1.
- The M0 density bound for 1 ≤ t ≤ β. §1.
- Large-argument Bessel expansion (DLMF 10.40) for 2 ≤ n < 8. §2.
- The exponential chart U = exp(hx) and the radial increment law ∝ sin²θ e^{−β(1−cosθ)}. §2–3.
- V ≥ 0 continuous polynomial potential for H, and Schrödinger semigroup positivity improvement. §4.
- e_j are counted on the simultaneous-rotation-invariant subspace. Statement.

## 3. Failed predicates (kept)

1. **fibre2 F1, β = 64:** row-sum error of the discretised K is 1.66e−6 > 1e−6. Own expectation (midpoint quadrature near the η endpoints); not a target defect. Its effect on μ is about 1e−5, against μ ≥ 0.1.
2. **fibre2 F1, β = 256:** the same, 6.59e−6. Own expectation.

These are runs, not predicates:
- K2 (fibre1): exit 1 because scipy is not installed. Own environment; no result file was written.
- K10 and K11: my scipy shim for the target check was wrong. K10 was a scalar/array bug. In K11 the continued-fraction start was too low at β = 32768, so the ratio came out > 1. Both are my own defects, and K14 is the fixed run.
- My besselnp.ratio has the same limitation for β ≫ 400². My runs use β ≤ 1024, where I verified it against a longer start (identical to 16 digits at β = 256 and 1000).

## 4. What I did not check

- target/excitation/check.py was not run (scipy.stats.qmc).
- k = 3 numerics.
- Constants: c, C, κ are not computed beyond the discretised fibre (κ_eff ≈ 0.9999, μ/r ≥ 0.976).
- The cited papers and DLMF pages were not fetched. Formulas were re-derived only.
- The positivity-improving and form-core facts in §4 are standard results I did not re-derive in full.
- The β = 1024 transfer run has one truncation (N = 128) only. Its gap equals NUMERICS to 3e−10.
- The fibre discretisation is reduced to the torus-invariant sector. This is exact for the lowest eigenvalue because K_j is positivity improving and V_ij and K_j are torus invariant.
- The target's guest/kernel replay (replay-guests.py) was not run; it is not in this directory.

## 5. Delegated questions and outcomes

- **Child T89** (h1-a4-child, parent T88). It was admitted by me, run as K1 `child-run1` in my register (exit 0, 103 s), and released by me (event 189). Model: sonnet.
  - Control: ∫₀^∞ x e^{−x} dx. I graded it first: 1.000000, correct.
  - Questions:
    - (A) the Bessel-ratio bound on n = 8..4000 and 64 β-points in [1, 10⁴];
    - (B) the numerator identity on 600 random symmetric Markov instances.
  - Outcomes:
    - (A) 255,552/255,552 met, max D = −0.002350477 at n = 8, β = 10⁴.
    - (B) 600/600, max rel 5.1e−16.
  - I reread checkA.py and checkB.py and reran them in rerun_child/ (K4, K3). The outputs were identical.
  - The child reports it ran `pip download scipy`, which used the network outside its brief. It says it deleted the wheels without installing them. I report this as a rule breach by the child.
  - Independence: the child's Bessel method (backward continued fraction) is the same method as my besselnp.py.
- **Grandchild T91** (h1-a4-grandchild, parent T89). Admitted 17:24:29Z and released 17:24:55Z by the child.
  - Control: I_0(1), met.
  - Question: recompute D at n = 8, β = 10⁴ in 40-digit decimal arithmetic (power series).
  - Outcome: D = −0.0023504771758247552440807. I reran it as K13: identical.

## 6. Registers

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Checks K1–K16:

| check | name | exit |
|---|---|---|
| K1 | child-run1 | 0 |
| K2 | fibre1 | 1 |
| K3 | child-rerunB | 0 |
| K4 | child-rerunA | 0 |
| K5 | fibre2 | 1 (F1) |
| K6 | lean-vacuum | 0 |
| K7 | lean-excitation | 0 |
| K8 | target-check-vacuum | 1 |
| K9 | target-check-excitation | 1 |
| K10 | target-check-vacuum-shim | 1 |
| K11 | target-check-vacuum-shim2 | 1 |
| K12 | transfer-sweep1 | 0 |
| K13 | grandchild-rerun | 0 |
| K14 | target-check-vacuum-shim3 | 0 |
| K15 | transfer-sweep2 | 0 |
| K16 | analyse2 | 0 |

Task graph:
- T88: this worker.
- T89: child, admitted under T88 and released.
- T91: grandchild, admitted under T89 and released.

## 7. Key numbers (k = 2, center-even gauge-invariant sector; results/analysis2.md)

| β | λ_0 | (1−λ_0)/h | −log λ_0/h | (1−λ_1)/h | −log λ_1/h | log(λ_0/λ_1) |
|---|---|---|---|---|---|---|
| 32 | 0.3812459338 | 1.96442 | 3.06150 | 2.45172 | 4.69704 | 0.5151641763 |
| 64 | 0.4535524816 | 2.18579 | 3.16258 | 2.83152 | 4.92235 | 0.4399423291 |
| 128 | 0.5269180102 | 2.38418 | 3.22898 | 3.19532 | 5.06595 | 0.3645007923 |
| 256 | 0.5972830532 | 2.55709 | 3.27236 | 3.53195 | 5.15897 | 0.2971232997 |
| 512 | 0.6619520025 | 2.70438 | 3.30050 | 3.83358 | 5.21908 | 0.2398232122 |
| 1024 | 0.7194632487 | 2.82763 | 3.31863 | 4.09675 | 5.25773 | 0.1923831345 |

- λ_1 and λ_2 form the split doublet. log(λ_1/λ_2)/h = 0.108 → 0.0093, so in the limit e_1 = e_2, as M1's multiplicity counting requires.
- Both forms converge to e_j. At reachable β, −log λ/h is within 1–1.3 % of e_j, while (1−λ)/h is still 16–23 % below it.

## 8. Rerun commands (from /home/user/z4-workers/h1-a4; result files are opened with mode "x", so move results/ and the target files away first)

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"            # control 0.272341
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name fibre2 --expect-exit 0 --timeout 1500 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 fibre.py results/fibre2.json   # exits 1 (F1, own tolerance)
$P check --ws pcp --name transfer-sweep1 --expect-exit 0 --timeout 3000 -- ./run2.sh
$P check --ws pcp --name transfer-sweep2 --expect-exit 0 --timeout 3000 -- ./run3.sh
$P check --ws pcp --name analyse2 --expect-exit 0 --tail 40 -- python3 analyse2.py results/analysis2.md
# single transfer run: python3 transfer2.py <beta> <N> <M> <out.json> [v0|-] [lanczos_steps]
# Lean (copies of the target files in lean/):
$P check --ws pcp --name lean-vacuum --cwd /home/user/z4-lean --expect-exit 0 --timeout 600 -- bash -c "PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/h1-a4/lean/ToronVacuum.lean"
$P check --ws pcp --name lean-excitation --cwd /home/user/z4-lean --expect-exit 0 --timeout 600 --tail 40 -- bash -c "PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/h1-a4/lean/ToronExcitation.lean"
# target checks (copies in target_runs/; scipy absent, numpy shim in target_runs/shim):
$P check --ws pcp --name target-check-vacuum --cwd target_runs --expect-exit 0 --timeout 300 --tail 5 -- python3 check_vacuum.py          # exits 1, no scipy
$P check --ws pcp --name target-check-excitation --cwd target_runs --expect-exit 0 --timeout 300 --tail 5 -- python3 check_excitation.py  # exits 1, no scipy
$P check --ws pcp --name target-check-vacuum-shim3 --cwd target_runs --expect-exit 0 --timeout 900 --tail 30 -- env PYTHONPATH=shim OMP_NUM_THREADS=1 python3 check_vacuum.py
# child (graph admission first):
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label h1-a4-child --parent T88
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T89
# reruns of the child's programs:
$P check --ws pcp --name child-rerunB --cwd rerun_child --expect-exit 0 -- python3 checkB.py
$P check --ws pcp --name child-rerunA --cwd rerun_child --expect-exit 0 --timeout 900 -- python3 checkA.py
$P check --ws pcp --name grandchild-rerun --cwd rerun_child/grandchild --expect-exit 0 --timeout 300 -- bash -c "python3 solve.py control && python3 solve.py"
$P verify --ws pcp ; $R verify pcp/register.jsonl
```

Files:
- programs: fibre.py, transfer2.py, analyse2.py, besselnp.py, run2.sh, run3.sh;
- results: results/*.json, results/analysis2.md;
- notes.md, child/, rerun_child/, target_runs/, lean/.
