Overall verdict: I found no false line in return.md, inheritance.md or geometry.md. Every step I checked STANDS. I could not rerun the measurements or the evidence verifier because `returns.zip` and `evidence.zip` are not in the target directory. One wording issue in return.md is listed under "for the author".

Worker: y1-g4ret (task T193). Control: `control.txt` = 0.272341 (= −ln tanh 1).

## Verdict table

| # | Item | Verdict | One line of evidence |
|---|---|---|---|
| 1 | (a) One-link conditional law, cap, rearrangement, monotonicity in k | STANDS | A link lies in 6 plaquettes in 4D. ½Tr(UW) = β‖W‖ u·v with ‖W‖ ≤ 6, so k ≤ 6β. Since d(XUY, −I) = d(U, −X⁻¹Y⁻¹), the event is a cap. The density is radially decreasing, so Hardy–Littlewood rearrangement applies. d/dk = Cov(1_cap, cos r) ≥ 0 by Chebyshev's sum inequality. Checks R3 (400 off-centre caps, max excess 2.4e-15), R4 (monotone on a grid) and R5 (40 Monte Carlo holonomy problems, max \|MC−quad\|/SE = 2.12) all met. |
| 2 | (b) From the conditional bound to ‖R S_τ R‖ ≤ p | STANDS | A_θ is conjugation invariant because −I is central. For gauge-invariant f, g, ⟨f, S_τ g⟩ = E[f(slice 0) g(slice τ)], and τ ≥ 1 keeps slice 0 among the frozen links. The tower property gives P(y∈A \| x) ≤ p ν-a.e., and AM–GM plus endpoint exchange finishes the bound. The vacuum passage uses wilson.md's total-variation convergence of slab marginals, which preserves the event inequality. R7: 200 toy reversible kernels, ‖RSR‖ ≤ row supremum. |
| 3 | (c) Full gauge-invariant space vs centered space | STANDS | The row bound holds for every g ∈ L²(vacuum). B = RQ annihilates constants (I1). |
| 4 | (d) C and the numbers at β = 3.399810242 | STANDS | C = π²√e/4 = 4.068056677. I reproduced the Z lower bound and the numerator step by hand, and R2 checks the envelope on a grid. Simpson (my method) gives 0.003072387580, 0.156180436616, 0.934803629970, matching the target to all printed digits (R1). The child (Gauss–Legendre) and grandchild (Simpson) agree. |
| 5 | (e) Dyadic cost | STANDS | (3N³/8)·C·c³·N⁻⁴ = (3C/8)c³/N (R6). It is summable over N = 2ⁿ. |
| 6 | Union bound over M gates | STANDS | P(y∈∪A_j \| x) ≤ Σ_j P(y∈A_j \| x) ≤ Mp. No independence is used. |
| 7 | (f) B = RQ is an orthogonal projection | STANDS | R is coarse-measurable, so RP = PR, which makes B symmetric and idempotent. B and G map centered functions to centered functions (I1, 300 cases). |
| 8 | (g) e^{−τL}‖BE‖² ≤ κ, so ‖Bv‖² ≤ e^{τL}κ | STANDS | S_τ ⪰ e^{−τL}E (they commute) gives B S_τ B ⪰ e^{−τL}BEB, and ‖BEB‖ = ‖EB‖². I3 checked this on 3446 eigenvectors. |
| 9 | (h) 1 − b ≥ e^{−tL}(1 − ‖Qv‖²) | STANDS | ⟨Pv, S_t Pv⟩ ≥ e^{−tL}‖EPv‖² ≥ e^{−tL}⟨v,Pv⟩² = e^{−tL}‖Pv‖⁴. Dividing by ‖Pv‖² gives the claim, and the Pv = 0 case is fine because b ≤ 1. I3 met. |
| 10 | (i) d ≥ (b−κ)₊/(1 + 2a/(γt)) | STANDS | Redone by hand: x(1−x^r) ≤ r(1−x) holds because φ = r(1−x) − x + x^{r+1} has φ(1) = 0 and φ′ ≤ 0. No failures in any numerical test: 1723 structured Markov cases, 2000 generic cases, 40 adversarial searches (min slack 0.0, i.e. tight, never negative), and the child's 3000 cases, rerun byte-identically. |
| 11 | (j) Accumulation formula | STANDS | Induction checked by hand, and the worst-case recursion was tested on 2000 random sequences (I6). |
| 12 | (k) Reset-process counterexample | STANDS | On the centered space S_t = e^{−ℓt}I. ‖BS_tB‖ = e^{−ℓt} for event mass 1e-1, 1e-3 and 1e-6 (I5). |
| 13 | (l) geometry.md, 1/504 | STANDS (conditional) | weighted.py reran and its output matches the table. I checked the m_e column by hand against 2·#odd transverse coordinates; every edge with m_e = 0 has w_e = 0; and w_e ≤ 3m_e holds, with equality at 110/y. The Gram block [[6,±1],[±1,6]] has eigenvalues 5 and 7, so its inverse is ⪰ I/7. 24·7 = 168 and 3·168 = 504. I did not enumerate the colours myself, and I took the residual ≤ ‖ΠSc‖² input from gaussian.md without checking it. |
| 14 | Lean (Checks.lean) | STANDS | Lean ran with exit 0 and no sorry. All five declarations print axioms [propext, Classical.choice, Quot.sound]. They prove only scalar and finite-sum facts: the weighted row sum, 3·168 = 504, the final rearrangement (b−k)g ≤ d(g+r), a monotone product, and one accumulation step. They do not prove x(1−x^r) ≤ r(1−x), the spectral steps or the Wilson law. |
| 15 | Sufficient Wilson input for I − S_{2a} ⪰ γG (inheritance.md, ¶2) | NOT CHECKED | This is an outline that depends on a 24-colour Wilson inequality not given here. |
| 16 | measurements.md / returns.py | NOT CHECKED | returns.zip is absent, so returns.py raises FileNotFoundError (K9). |
| 17 | verify.py (evidence archive) | NOT CHECKED | evidence.zip is absent, so verify.py raises FileNotFoundError (K10). |

**Counts:** 14 STANDS, 0 DEFECT, 3 NOT CHECKED.

**Predicates:**
- My programs: 15 met, 0 failed. That is R1–R7 (7) and I1, I2-S, I2-U, I3, I4, I5, I6 (8).
- Child's programs, rerun by me: 2 met, 0 failed (A and B).
- Measured only: minimum slacks (2.8e-19 structured, 6.2e-10 generic, 0.0 adversarial, 6.4e-3 child), the Monte Carlo z-score 2.12, and the off-centre excess 2.4e-15.

## Hypotheses each statement uses, and where they are stated

- **return.md theorem:**
  - 4D isotropic SU(2) Wilson measure, even spatial torus N ≥ 6, β ≥ 0 (¶1).
  - Time vacuum at fixed spatial regulator, reached through finite-slab convergence ([wilson.md "Time vacuum and the domain"](target/full-complement/wilson.md)).
  - Positive integer lag, and slices distinct modulo the period at finite T (¶3).
  - Reversibility of the two-slice law (¶3).
  - The one-link density bound for every exterior (¶2).
- **Envelope:**
  - sin r ≥ 2r/π on [0, π/2].
  - k(cos r − 1) ≥ −1/2 on r ≤ (1+k)^{−1/2}.
  - sin r ≤ r (¶4).
- **inheritance.md:**
  - H ≥ 0 self-adjoint on centered gauge-invariant functions, S_t = e^{−tH}; this needs the Lüscher positivity of the transfer.
  - P is a conditional expectation and A is coarse (¶1).
  - a > 0, 0 < τ ≤ t, γ > 0, and the three operator hypotheses (displayed).
  - Accumulation additionally needs b_i ≥ d_{i−1} − ε_i and matching time units (¶Accumulation).
- **geometry.md:**
  - The retraction, Π and exteriors of gaussian.md.
  - Each colour selects an edge at most once.
  - Pairs within one colour have disjoint support (gaussian.md l.28).
  - The residual is at most ‖ΠSc‖².

## Failed predicates

None of my predicates failed, and neither did the child's. The two runs of the target's returns.py and verify.py were recorded with `--expect-exit 1`. Both failed as I expected, because their archives are missing from the target directory. That is missing input, not a defect in the mathematics.

## What I did not check

- The 24-colour Wilson input (row 15).
- wilson.md's proof of total-variation slab convergence: I checked only that it suffices.
- Lüscher positivity, which is cited.
- gaussian.md's residual and colour construction, and my own enumeration of the colour coverage.
- The measurements and the evidence archive.
- Whether the claimed refinement mixing on the good set can be obtained at all, which the authors also leave open.

## Delegated questions and outcomes

- **Child** (task T195, admitted under T193, released): Statement A was the random finite-dimensional test of (i). Statement B was the quadrature of (d) and the envelope.
  - Control: ∫₀^π sin² = π/2. The child answered 1.570796, which is **correct**; I graded it before reading anything else.
  - Returned: A had 3000 qualifying cases out of 3000, 0 failures, min slack 6.42e-3. B gave 0.003072388, 0.156180437, 0.934803630 and C = 4.068056677, with the envelope at θ = 0.05 equal to 0.050336499.
  - Rerun in my register (K7, K8): A_cases.csv is byte-identical, there were 0 bisection mismatches, and the B table is identical.
  - Caveat: the child's random P and B are generic projections, not conditional expectations. My family S covers the structured case.
- **Grandchild** (task T196, label y1-g4ret-child-grandchild, parent T195, admitted and released according to the graph): an independent Simpson computation of p_k(0.2).
  - Control: ∫₀^π sin r = 2, answered 2.000000, which is correct.
  - Result 0.156180436616, which I reran and which matches.

## For the author

1. return.md ¶4 calls 0.003072388, 0.156180437 and 0.934803630 "the one-link envelope … evaluations of the upper bound". They are the sharp p_{6β}(θ). The C-envelope just stated in the same paragraph gives 0.0503, 1 and 1. Please say which bound the numbers evaluate.
2. inheritance.md ¶2 says the second hypothesis follows "since … S_τ is positive". Positivity is not needed: ‖BS_τB‖ = ‖B(RS_τR)B‖ ≤ ‖RS_τR‖ because B = RB.
3. The Lean file does not contain x(1−x^r) ≤ r(1−x), which is the only non-trivial scalar step in the gated proof. It would be easy to add.
4. README links evidence.zip and returns.zip, but neither is in the deposited directory, so verify.py and returns.py cannot run.

## Exact rerun commands

```
cd /home/user/z4-workers/y1-g4ret
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
# results files are opened with mode "x": move results_return.txt / results_inherit.txt away first
$P check --ws pcp --name return-checks --expect-exit 0 -- python3 check_return.py
$P check --ws pcp --name inherit-checks --expect-exit 0 -- python3 check_inherit.py
$P check --ws pcp --name target-checks-py --expect-exit 0 -- python3 tcopy/rare-coarse-fields/checks.py
$P check --ws pcp --name target-weighted-py --expect-exit 0 -- python3 tcopy/rare-coarse-fields/weighted.py
$P check --ws pcp --name target-returns-py --expect-exit 1 -- python3 tcopy/rare-coarse-fields/returns.py
$P check --ws pcp --name target-verify-py --expect-exit 1 -- python3 tcopy/rare-coarse-fields/verify.py
# child reruns (delete child_rerun/A_cases.csv first)
$P check --ws pcp --name child-rerun-A --cwd child_rerun --expect-exit 0 -- python3 stmtA.py
$P check --ws pcp --name child-rerun-B --cwd child_rerun --expect-exit 0 -- python3 stmtB.py
(cd child_rerun && python3 gc_check.py)
# Lean
cd /home/user/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/y1-g4ret/TargetChecks.lean
# child launch (as run)
cd /home/user/z4-workers/y1-g4ret
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
# verification
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last lines of the verification:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

The director and I share a model family, so this agreement is not independent review.
