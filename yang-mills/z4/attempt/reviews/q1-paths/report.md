# report.md — worker q1-paths (task T151)

**Proved in writing (unreviewed):** Lemma P'c, the continuum flow form of the canonical-path lemma, on any measure space: Δ ≥ 2∫_S f²/(nρ). Corollary B, an explicit chain-of-balls bound on ρ, with a loss that is only polynomial in β. The 1D continuum theorem limsup (−log m)/√β ≤ c*, with no grid. The continuum-P' gap of TUNNEL_LOWER2 is closed. The SU(2)² target is still NOT proved: it rests on (E1), (E3), H4 and (H-c), all CLAIMED. Details are in PATHS.md.

I share a model family with the director and the input authors, so this is not independent review.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| Lemma P'c (flow form): for random paths x → σx with Σπ_k ≤ ρQ, Δ ≥ 2∫_S f²/(nρ) | STANDS | PATHS §1 proof; Lean scalar steps (Paths.lean, exit 0); F1 Bflow ≤ Δ at 5/5 β (16…4096) |
| Corollary B: ρ ≤ n sup g² max(1/v, \|S\|/v²)/Q_min, loss polynomial in β | STANDS | PATHS §2.1; F2 met 5/5; Δ/Bflow = 73…1583 ≈ β^{0.9–1.5} (F3 met 4/4) |
| Brief's ball-to-ball Poincaré (m₀ − m_N)² ≤ N Σ … ≤ 2Nρ_CB D(h) | STANDS | Jensen + CS (PATHS §2.2); child T153 L ≤ M ≤ R at 7/7 β; I reran it (K5) and got identical numbers. The brief omits the factor 2 on D |
| Brief's route "CB with the wells as end sets gives Δ ≥ e^{−√β(c*+o(1))}" | DEFECT | It needs \|mean_{B₀} f/g\| ≥ e^{−o(√β)}, a sign or concentration fact about f that is not available for SU(2)² (TUNNEL_LOWER (I0)). The point-start flow form P'c avoids it |
| 1D continuum theorem: limsup (−log m)/√β ≤ c* | STANDS (in writing) | PATHS §3: (L), (M), (H) with tubes, (S) with the exact Gaussian moment, (C), (P). −log Bflow/√β = 4.586, 4.548, 4.540, 4.546 ≤ c* = 4.6054 for β = 64…4096 |
| TUNNEL_LOWER §2 "1D continuum (κ → 0 with tubes) CLAIMED" | STANDS (now proved) | PATHS §3 (H) and (P) |
| TUNNEL_LOWER P' with ordered edges (z, z') | DEFECT (constant only) | If both orientations of an edge are used, Σ_e Q(dh)² = 2E, not ≤ E: a factor 2, which does not affect the exponent |
| TUNNEL_LOWER2 §4 "continuum Lemma P' MISSING" | STANDS as closed | P'c + Corollary B are dimension-free; the remaining inputs are listed in the PATHS §4 table |
| SU(2)² target limsup (−log m_eo)/√β ≤ c* | NOT CHECKED (not proved) | It depends on (E1), (E3), H4 and the path geometry (H-c), all CLAIMED in TUNNEL_LOWER2 |
| TUNNEL_LOWER2 (H-a), (H-b), M4, (B) | NOT CHECKED | Cited only |

## 2. Hypotheses each statement uses, and where they are stated

- **(GS) E(h) = Δ:**
  - (H1) symmetric kernel T ≥ 0, bounded on L².
  - (H2) σ is measure preserving and commutes with T.
  - (H3) g > 0 even and f odd eigenfunctions, both of norm 1.
  - Stated in PATHS §0.
- **P'c:** (H1)–(H4); S is σ-invariant; x ↦ P_x is a measurable kernel; Σπ_k ≤ ρQ off the diagonal. PATHS §1.
- **Corollary B:** a metric measure space; v = inf ball volume > 0; measurable centres; the uniform-ball noise is independent across k; Q_min > 0 on the support U. PATHS §2.1.
- **CB:** probability measures ν_i on B_i; Σ ν_i ⊗ ν_{i+1} ≤ ρ_CB Q. PATHS §2.2.
- **1D theorem:**
  - The circle with Lebesgue measure, ε = 2 asinh|sin|, Gaussian K of variance 1/β (periodised), σ = +π.
  - Jentzsch's theorem (g > 0 simple) and (L2), (L3) of TUNNEL_LOWER (Lean there).
  - η ∈ (0, η₀) fixed, then β ≥ β₀(η).
  - PATHS §3.
- **SU(2)² transfer:** the inputs in the PATHS §4 table: M4 and (B), (H-a), (H-b), H4, (H-c), (E1), (E3), Lemma F.

## 3. Failed predicates (all kept)

- **F0** (flow_paths.py, β ≥ 256): FAILED. My float evaluation of E(h) = ½Σ T(f_i g_j − f_j g_i)²/(g_i g_j) has a rounding floor of about 10⁻²⁹ from well–well pairs.
  - Defect of my program, not of the target.
  - The child's 50-digit computation gives Δ(identity) = Δ(E(h)) to 10⁻⁴⁹ (checked at β = 16…256).
- **F4**: FAILED. This was my expectation: that |−log Bflow/√β − c*| decreases monotonically.
  - Measured 0.0195, 0.0654, 0.0595 at β = 64, 1024, 4096. −log Δ/√β approaches c* from below, while the polynomial path loss is positive, so their sum crosses c*.
  - Consistent with limsup ≤ c*. Not a defect of the target.
- **Lean first attempt**: FAILED. `tilt_square` had an unsolved goal, which showed up as sorryAx.
  - My proof defect. Fixed via s = √β; the rerun exits 0.
- **Child P7** ("h odd under x → −x"): FAILED.
  - My prompt said "odd" meaning σ-odd. h is σ-odd and even under x → −x.
  - A wording defect of my prompt, not of the math.
- **Child P8** (Δ/λ_e < 10⁻¹⁶ for β ≥ 36): FAILED at 2 of 6 β (36, 64). This was the child's expectation, taken from my prompt's loose wording.
- **Child P10** (Δ converges in κ to within 10⁻³): FAILED. Δ changes by 1.5% between κ = 0.25 and 0.125 (grid quadrature). This was the child's expectation; the exponent is unaffected.

**Counts.**
- My main run (K2): met 4 (F1, F2, F3, F5), failed 2 (F0, F4). Measured only: the exponent columns and Δ/Bflow.
- Smoke run (K1): met 4, failed 0.
- Lean: 5 theorems pass, after 1 failed attempt.
- Child T153: met 5 (P2–P6), failed 3 (P7, P8, P10), measured only 2 (P1, P9).

## 4. What I did not check

- TUNNEL_THEOREM.md and LEMMA_F.md were not reread.
- (H-a), (H-b), M4 and (B) of TUNNEL_LOWER2 are cited only.
- (E1), (E3), H4 and (H-c) are untouched and remain CLAIMED.
- The existence in SU(2)² of chains of balls of radius r/√β from every corner point to its σ-image that stay inside D_K ∪ (tube core) is (H-c) geometry: CLAIMED, not proved here.
- The 1D proof's constants (β₀(η), the choice of M in Lemma S) are not made explicit.
- Lemma (L) for λ_o is a sketch at the same level as TUNNEL_LOWER.
- P'c was tested numerically only on the grid model with κ = 0.25. That is a legitimate test, since the lemma holds on any measure space, but it does not test the continuum limit itself.

## 5. Delegated questions and outcomes

**Child T153** (admitted under T151, then released).
- Question: a numerical test of the chain-of-balls inequality L ≤ M ≤ R on the 1D continuum model by fine discretisation.
- Control: the Gaussian tilt integral at β = 4, ρ = 1. Known answer e^{1/2} = 1.648721. The child answered **1.648721: correct** (graded before reading anything else).
- Result: L ≤ M ≤ R at 7/7 β (16…256). L ≈ 4, i.e. m₀ ≈ 1. M/L = 6.3–27 and R/M = 38–64. Its Δ equals mine at β = 16, 64, 256.
- I reran chain.py at β = 16, 64 (check K5): identical.

**Grandchild T155** (admitted under T153 by the child, then released).
- Question: Δ at β = 16 by direct subtraction of the sector eigenvalues, against the identity value.
- Control: e² = 7.389056, correct.
- Result: 6.003928380016e−07 against 6.003928380885e−07, relative 1.4·10⁻¹⁰ (float rounding). My K2 value is 6.003928e−07. The child reported rerunning it; I did not rerun the grandchild myself.

**Task-graph records:** admit.log (T151), child_admit.log (T153), child_release.log (T153 released).

## 6. Exact commands to rerun

```
cd /home/user/z4-workers/q1-paths
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"      # control 0.272341
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name flow-smoke --expect-exit 0 -- python3 flow_paths.py smoke 16,64      # results_flow_smoke.txt must not exist (mode x)
$P check --ws pcp --name flow-main --expect-exit 0 -- python3 flow_paths.py main 16,64,256,1024,4096
$P check --ws /home/user/z4-workers/q1-paths/pcp --name lean-paths --cwd /home/user/z4-lean --expect-exit 0 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/q1-paths/Paths.lean'
$R task-admit $G --by principal --label q1-paths-child --parent T151
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T153
$P check --ws pcp --name child-rerun --cwd child_rerun --timeout 280 --expect-exit 0 -- python3 chain.py rerun 0.25 16 64
$P verify --ws pcp
$R verify pcp/register.jsonl
```

**Last lines of the verifications:**
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
