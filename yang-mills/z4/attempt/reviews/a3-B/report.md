# report a3-B: claim (B), SU(2), d = 4. Builder, positive arc

**Not a proof.** The chain in PROOF.md has three CLAIMED steps (S3a, S3b, S3c). Control: `control.txt` = 0.272341. Lean: `/home/user/z4-lean/READY` exists, and `S2.lean` passes.

## 1. Verdict table (step: tag, one line of evidence)

| item | tag / verdict | evidence |
|---|---|---|
| S0 infinite-volume RP state, OS transfer matrix, m(β) := −log‖T\|Ω⊥‖ | CITED (+ PROVED elementary parts) | OS78 / Lüscher 1977 (LIT_RIGOROUS R2, abstract only); G4 Lean RP (INDEX (a)1); RP is closed under weak limits |
| S1 C(n) ≤ e^{−mn}C(0), n even | PROVED | spectral theorem for T² ≥ 0; positivity of T not needed |
| S2 liminf C(n)/C(0) ≥ c(n) ~ Kn^{−p} ⇒ m(β) → 0 | PROVED | `S2.lean`: `s2_gap_le` and `s2_power`; exit 0; axioms propext, Classical.choice, Quot.sound only |
| free target c(n) = (G(n)/G(0))², power decay | PROVED numerically (free field) | `free_benchmark.py`: G(0) = 0.5; G > 0; log-convex; c(n) ~ n^{−8}, n·b(n) → 7.8; 5 met / 0 failed |
| S3a uniform tails P(O_p > t) ≤ C e^{−t/8} (chessboard + two-sided free energy) | CLAIMED | 2D exact test (v2): 240/240 cases (149 informative, min log(bound/P) = 0.594); Δ(β) → 1.037 vs (3/2)log 2 = 1.040. Weakest point: site-plane RP and chessboard for gauge links in 4D, not located in the literature |
| S3b every β → ∞ limit is a free-Maxwell Gibbs state (L → ∞ and β → ∞ exchanged) | CLAIMED | argument in PROOF.md §1; NOT tested. Weakest point: uniform Laplace limit of the DLR kernel over boundary data |
| S3c classification F = ξ + constant f ⇒ ratio ≥ c(n) | CLAIMED | scalar case Georgii Ch. 13 FROM MEMORY (not read); 1-form case not proved. The min-inequality algebra is PROVED given the decomposition |
| conclusion (B) | NOT ESTABLISHED (conditional on S3a–c) | — |
| A1 §6 discriminator row "2D: (B) true" | DEFECT (of the target A1) | infinite-volume 2D plaquettes are i.i.d., so the gauge-invariant OS space is ℂΩ and m = +∞; "(B) true" holds only for the string tension or a finite circle |
| discriminators U(1) d=4, finite G, U(1) d=3, d=2 | STANDS (chain consistent) | finite G breaks at S3b (no Lie algebra, no Laplace); U(1) d=4 and d=3 give m → 0, which is correct; d=2 gives c(n) = 0, no conclusion |

Predicate counts (all my programs): **met 8, failed 2, measured only 5**. The void v1 Q2 is not counted. The child's own counts are in §5.

## 2. Hypotheses each statement uses (where stated)
These are listed in PROOF.md §2. The two not confirmed by any source read in this program:
- (H-RP-site) RP of Wilson SU(2) for reflections in coordinate planes through sites, in all four directions, used by the chessboard estimate in S3a.
- (H-Gauss-1form) the Gibbs classification of the free Maxwell specification (S3c).
Order of limits: L → ∞ (fixed β), then β → ∞ (fixed n), then n → ∞. Volume uniformity is used only in S3a, where the 1/L·log β terms vanish because L → ∞ first.

## 3. Failed predicates
- `sharp_chess2d.py` (K4, exit 1):
  - Q1 normalisation FAILED. **Defect of my own program**: P_L was returned as â₀·P, so v1's torus Q2 result is void. The infinite-volume rows were correct.
  - Q3 FAILED: **my own expectation**. A 1e-30 tolerance is below the double-precision quadrature floor.
  - The run also used about 3.6 cores through numpy threads, a breach of rule 8 by me. Later runs were pinned to 1 thread.
- `sharp_chess2d_v2.py` (K5): Q1, Q2 and Q3 all MET, but the process **exited 1**. The final count line adds numpy booleans (logical or), printing "met True, failed 2". This is a bookkeeping defect of my program, not a predicate failure. The per-predicate lines in `result_sharp_chess2d_v2.txt` are authoritative.
- 4D chessboard numbers in `result_free_benchmark_1.txt` (measured only) omit the 1/4 image factor, so they are too optimistic. This is my error, superseded by the −t/8 form in PROOF.md.
- No predicate failure was a defect of the target claim.

## 4. What I did not check
- S3b and S3c are not tested at all (no 4D Monte Carlo, no fixed-box Laplace check with boundary data).
- The 4D inputs of S3a: site-plane RP, the image count |Λ|/4, the −(9/2) log β free energy and the constant 48 in the lower bound are argued, not computed.
- Georgii Ch. 13, Patrascioiu–Seiler (superinstantons), FILS (chessboard): not read; network was not used.
- Whether (B) for SU(2) d = 4 is already settled in the literature (Chatterjee 2018 Problem 5.1 lists ξ(β) → ∞ as open, per LIT_RIGOROUS).
- A literature search for an infrared bound (Gaussian domination) for non-abelian lattice gauge theory, which would be an alternative route.

## 5. Delegated questions and outcomes
- **Child** (`child/`, sonnet, register K3, exit 0, 348 s). Question: exact 2D test of the crude chessboard bad-plaquette bound P(1 − cos α_p > δ) ≤ min_ε exp(−βδ + β(1 − cos 4ε) − 2 log H(ε)), on L = 2, 4, 6, 8 and ∞, for 8 β values and 5 δ values.
  - Control: (2/π)∫₀^π e^{2cos a} sin²a da = I₁(2) = 1.590637. I computed it first (trapezoid and series agree). The child answered **1.590637: correct**, graded before reading anything else.
  - Returned: 200/200 satisfy the bound; only 30 are informative (bound < 1); min log ratio 6.7; the bound is very loose where informative. Self-counts: met 8, failed 0, measured only 2.
  - I reread `pcp_main.py` (normalisation correct: r = A/A₀, rp = Ap/A₀). My rerun is in `child_rerun/` (register K6, exit 0, 178 s, one thread). `results.jsonl`, `table.md` and `m1.md` are byte-identical to the child's. Note: K5 and K6 ran at the same time, so for about 16 s I used 2 cores (rule 8).
- **Grandchild** (`child/grandchild/`, via the child's Agent tool). Question: independent Monte Carlo of P_inf(β = 16, δ = 0.2).
  - Control: E_Haar[e^{2cos α}] = 1.590637; it got 1.590466 ± 0.00042: passed.
  - Result: 0.08936 ± 0.00009 vs quadrature 0.0892708 (1.0 SE). The child reran it and the output was identical.
  - My cross-check: my v2 infinite-volume formula is independent code, and for its own grid agrees with the child's structure. I did not rerun the grandchild myself.

## 6. Commands to rerun (from /home/user/z4-workers/a3-B)
```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name free-benchmark-1 --expect-exit 0 -- python3 free_benchmark.py result_free_benchmark_1.txt      # new output name per rerun (mode x)
$P check --ws pcp --name lean-S2 --cwd /home/user/z4-lean --expect-exit 0 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/a3-B/S2.lean'
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name sharp-chess2d-1 --expect-exit 0 -- python3 sharp_chess2d.py result_sharp_chess2d_1.txt
$P check --ws pcp --name sharp-chess2d-v2 --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 sharp_chess2d_v2.py result_sharp_chess2d_v2.txt
$P check --ws pcp --name child-main-rerun --cwd child_rerun --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I pcp_main.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
Last line of `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
Register: K1–K6. K4 and K5 exited 1 (expected 0); both are explained in §3.
