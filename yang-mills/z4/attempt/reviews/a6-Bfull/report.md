# a6-Bfull report: PROOF_B_v2 for (B)

Worker a6-Bfull, Director Z4. Principal: Kirtus Justus. I share a model family with the director, so my agreement is not independent review.
- Control: `control.txt` = 0.272341.
- Lean READY exists, but Lean was not used in this run.
- The budget ended after item 7, with all seven brief items done at the depth stated below. L3 and L4 were left at outline level because of the budget.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| Statement: Theorem B′ (§0) | STANDS (as a statement) | Covers limit points along L = 2^k only, every such limit, and m defined on all of Ω^⊥; bounded through the single vector ψ = O_{p₀} − ⟨O⟩. This is weaker than (B) as stated in the attempt (dyadic L, periodic states only). |
| Hilbert space and T (OS construction) | STANDS (proved in §1) | Contraction by the iterated Cauchy–Schwarz bound ‖τF‖ ≤ ‖F‖^{1−2^{−j}}‖F‖_∞^{2^{−j}}; self-adjoint because θτ = τ⁻¹θ. |
| S3a(a): site-plane RP in all 4 directions | STANDS (proved) | No plaquette straddles a site plane. W = W₊ + W₊∘ϑ with weight ½ on in-plane plaquettes. Plane links belong to 𝒜₊. |
| S3a(b): chessboard estimate | STANDS for L = 2^k (proved here) | Dyadic doubling with closed blocks; faces allowed. Biskup's theorem was not read verbatim, so nothing is cited for it. |
| S3a(c): tails | STANDS (proved) | μ(O_p > t) ≤ e^{60.2 − t/8} for β ≥ 1, every limit state. Uses the temporal forest gauge, ẑ ≤ (π/2)^{5/2}b^{−3/2} and c_H = 2 sin²1/(3π). |
| S3b: circular gauge fixing | DEFECT of v1 confirmed; repaired | Test H3: a global axial tree's spatial part pins 2, 12, 36 physical links in boxes N = 2, 3, 4. v2 conditions on gauge-invariant data, with a shell-only tree plus an interior temporal forest. |
| S3b: compactness in gauge-invariant terms | STANDS (proved) | The 2-skeleton of ∂(4-cube) ≅ S³ is simply connected, so shell potentials are bounded by K_N·max shell √O_q. There are no holonomy variables. |
| S3b: Lemma H (nondegenerate Hessian) | STANDS (proved; tested H1 3/3, H2 3/3) | Closed form on the box, then λ = 0 on the shell, then λ = 0 on the interior through the forest. |
| S3b: L3, uniform Laplace limit | NOT CHECKED (CLAIMED, outline) | Only the δ-split argument is written; constants uniform in \|ψ\| ≤ M are not written. |
| S3b: L4, limit field (Bianchi, invariances, UI) | NOT CHECKED (CLAIMED, bookkeeping) | The lasso and BCH estimates are stated, not written out. |
| S3c: Gibbs classification | NOT NEEDED (bypassed) | Lemma R: the downward martingale gives F = ξ + h with ξ ⊥ h. h is harmonic and second-order stationary, hence a random constant. |
| Lemma D: C^R ↑ P = G | STANDS (proved; tested M1; child) | C^N_pp = 0.4927, 0.4992, 0.4998 (N = 4, 6, 8); C⁸(p₀,p₁) = 0.06867 vs G(1) = 0.06887. |
| Lemma G: G(n) > 0, ≥ c n^{−5} | STANDS (proved; tested G1–G4) | Exact k₀ integral; 12/12 positive, ≤ G(0), and above the explicit lower bound. |
| Direct-DLR positivity route (brief item 4, alternative) | DEFECT of that route | The child gives Cov(F_p², F_q² \| data) = −0.009278 < 0 for means (1, −C₀₁) at N = 6. This is algebraic only: realisability by boundary data was not checked. v2 uses the tail decomposition instead. |
| Discriminators (finite G, U(1) d4, SU(2) d3, d2) | STANDS | Finite G breaks at L3. U(1) d4 and SU(2) d3 go through. In d = 2, P = I gives c(n) = 0. |

Verdict counts: STANDS 10, DEFECT 2, NOT CHECKED 2, NOT NEEDED 1. The two DEFECTs are v1's gauge fixing (now repaired) and the naive conditional-positivity route.

Predicate counts (met, failed, measured only):
- My predicates: met 7 (G1, G2, G3, G4, M1, H1, H2), failed 0, measured only 3 (M2, H3, G values).
- Child control grading: met 1. Child-rerun identity (90/90 fields): met 1.
- Child's own predicates: met 9, failed 3 in its run 1 (its own expectation), measured only 2.
- Total: **met 18, failed 3, measured only 5**.

## 2. Hypotheses each statement uses, and where they are stated

- Theorem B′ (PROOF_B_v2 §0): L = 2^k, β → ∞, every limit point in 𝓛_β.
- Lemma 1: L even, and ½Tr U⁻¹ = ½Tr U (specific to SU(2)).
- Lemma 1′: Feller property of the local specification.
- Lemma 2: L = 2^k, f ≥ 0 supported on a closed unit cube.
- Lemma 3: β ≥ 1, and the forest gauge lemma (proved).
- Compactness: the S³ shell is simply connected (N ≥ 1).
- L3: Lemma H, smoothness of Haar in exponential coordinates.
- L4: tightness from S3a, BCH.
- Lemma D: Gaussian conditional variance as a sup.
- Lemma R: L² moments (S3a), the downward martingale theorem (standard, not cited from a read text), and translation invariance of the law of F (L4).
- Inequality: G(n) ≥ 0 and independence of ξ from f.

## 3. Failed predicates

- My programs: none.
- Child run 1: C2, C5 and C4(n = 2) failed, and so did one crash. The child's own expectation was at fault: at N = 4, p₂ lies on the shell, so F ≡ 0 and CG returned nan. This is not a defect of the target. The predicates were kept, the docstring amended, and the program rerun.

## 4. What I did not check

- L3 and L4 written to referee standard.
- The chessboard estimate for general even L (FILS/Biskup statement not read verbatim; Biskup arXiv:math-ph/0610025 was read on the abs page and in HTML Sections 1–3.4 only, through a web-fetch agent, with no text stored here).
- Rerunning the v1 Lean S2 check.
- Non-periodic Gibbs states.
- Monte Carlo of any kind.
- Whether the child's negative-covariance means are realisable by boundary data.

## 5. Delegated questions and outcomes

- **Child** (sonnet, headless, register K2, exit 0).
  - Question: the Dirichlet curvature covariance for N = 4, 6, 8 against G(n), and the sign of the conditional covariance of the squares.
  - Control: 1/√5. It answered 0.447214, **correct**, graded first.
  - Returned: the table in §1. I reran its cov.py in scratch (K3): 90/90 numeric fields were identical. Its values match my independent M1 values for N = 4 and 6.
- **Grandchild** (the child's sub-agent).
  - Question: G(0), G(1), G(2) by a direct 4D grid.
  - Control: G(0) = 0.5, correct.
  - Returned: G(1) = 0.0688747, which agrees with the child to 3e−9 and with mine (0.068875). I did not rerun it.

## 6. Rerun (from /home/user/z4-workers/a6-Bfull; result files open with mode "x", so rename them first)

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name test_newsteps --expect-exit 0 -- python3 test_newsteps.py test_newsteps_result.json
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
S=<scratch dir>; cp child/cov.py child/gquad.py child/gquad_result.json $S/
$P check --ws pcp --name child-cov-rerun --cwd $S --expect-exit 0 --timeout 300 -- python3 -I cov.py cov_rerun.json
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Register entries: K1 test_newsteps, K2 child-run1, K3 child-cov-rerun.
- Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Last line of the Rust verify: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
