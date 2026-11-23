# Report: q1-harnack (task T150)

**What is proved:** the Harnack chain (H4) is proved in writing and unreviewed; see HARNACK.md. For x with a₁, a₂ ≤ π/2 and V(x) ≤ 2M²:

g(x) ≥ λ m_B k_min²/k_sup² · e^{−M²−K/2} · e^{−n₀ℓ(K_M) − n₁₂ℓ(K₀) − n₃ℓ(K_K)}.

On the junction R_well and on the corners of S this gives

−log g ≤ 35(a₋ + r₀)√β + O(M^{5/2}β^{1/4}) + O(log β) − log(4m_B).

- The constant 35 is absolute.
- m_B ≥ 1/4 − o(1) is Lemma M4. M4 rests on (B), which rests on Lemma F and λ_ee → 1; I did not recheck either.
- The target limsup ≤ c* is still NOT proved, because (E1), (E3) and continuum P' remain MISSING.

I share a model family with the director, so this is not independent review.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| Theorem H4: pointwise lower bound on g on D_M, given m_B | STANDS | Proof in HARNACK.md §1–3. P1–P8 met 9, failed 0 (results_harnack_run2.txt). Lean: 5 lemmas, exit 0 |
| Corollary: on R_well and corners of S, −log g ≤ 35(a₋+r₀)√β + o(√β) | STANDS (given M4) | ℓ(K₀)/d = 8.35, ℓ(K_K)/d = 9.09 (measured minimum, d = 3.65, ρ = 0.265) |
| TUNNEL_LOWER2 (H-a): per-step kernel lower bound | STANDS | Mine is sharper (e^{−r²/2} per link); P3, P8 |
| TUNNEL_LOWER2 (H-b): sup g ≤ Cβ³ | STANDS | Rederived; P7 (ratio to bound ≤ 0.999999) |
| TUNNEL_LOWER2 (H-c): chain geometry, V ≤ K' along the chain | STANDS | Was a sketch; now proved with 4 phases. P4, P5, P6 met. Lean `phase0_len`, `phase3_mono` |
| TUNNEL_LOWER2 H4 statement (C(K,M) in front of √β) | STANDS | Sharpened: the coefficient of √β is absolute; M enters only the β^{1/4} term |
| Is a lower bound on \|f\| needed? | STANDS (no) | Lemma P' uses Σ_S f² (M4) and g on the edges only |
| TUNNEL_LOWER2 §3 writes (B) as ‖e^{√βΦ}f‖ ≤ C(η); TUNNEL_THEOREM (B) has ‖·‖² ≤ C(η)‖g‖² | DEFECT (notational, harmless) | M4's error term 2C(η)e^{−2√βφ_min} matches the squared form, so nothing downstream changes |
| Lemma M4 (mass ≥ 1/4 − o(1) per corner) | NOT CHECKED | Only its first inequality (∫_{V>K} g² ≤ (1−λ)/(1−e^{−K})) and the σ₁, σ₂ split were rederived |
| λ_ee ≥ 1 − O(β^{−1/3}) | NOT CHECKED | Sketch in the sources. Child measured (1−λ)β^{1/3} = 1.15–1.23 in the 1D model only |

Verdict counts: STANDS 7, DEFECT 1, NOT CHECKED 2.

## 2. Hypotheses each statement uses, and where they are stated

- **Lemma Ch** (HARNACK §1) uses:
  - the product kernel T = e^{−V/2}K₁K₂e^{−V/2} (TUNNEL_LOWER2 §0);
  - k = e^{β cos θ}/Z and Z = 2I₁/β (LEMMA_F I1, I2);
  - ρ ≤ √β/2.
- **Path geometry** (HARNACK §2) uses:
  - a₁, a₂ ≤ π/2 and V(x) ≤ 2M²;
  - a* ≤ π/4 and V(y) ≤ K.
- **Theorem H4** (HARNACK §3) uses:
  - λ ≤ 1 (‖K‖ ≤ 1);
  - g > 0 and continuous, with Tg = λg and ‖g‖₂ = 1;
  - β ≥ max(1, 4ρ²);
  - m_B as defined there;
  - k_sup ≤ β√(2πβ)/(2D) (LEMMA_F I7).
- **Corollary** uses:
  - the cut-off definitions of TUNNEL_LOWER2 §2: G > c₁ ⇒ V < 2M², E > c₂ ⇒ a₂ < r₀, a₋ = arcsin sinh η;
  - M4 (TUNNEL_LOWER2 §3), which uses (B) (TUNNEL_THEOREM §4), Lemma F (LEMMA_F.md) and λ ≥ e^{−η/4};
  - the σ₁, σ₂ symmetries of g, from uniqueness of the positive eigenvector.

## 3. Failed predicates (all kept in the register)

- **My K1** (harnack-check-run1): exit 1, because scipy is not installed. This was a defect of my program, not of the target. I replaced scipy's ive with my own trapezoid quadrature and reran it as K3 (run2): met 9, failed 0, measured only 6.
- **My first Lean compile:** unknown identifier `cos_sq_half`, and a linarith failure. Both were my errors. I fixed them; the recorded run is K5, with exit 0.
- **Child K2:** the predicate "g > 0 everywhere" failed with min g = −6.1e−16. This was the child's own expectation, broken by roundoff in the far tail, not a defect of the target. The child revised the predicate and the rerun passed.

Totals:
- mine: met 9, failed 0 in the final run (plus 1 failed run: program defect), measured only 6;
- child: met 24, failed 0, measured only 36.

## 4. What I did not check

- I did not compute the SU(2)² (or reduced) eigenfunction g. The bound is tested only through its ingredients (P1–P8) and on the 1D analogue.
- Lemma F, (B), M4 beyond its first inequality, and λ → 1 were not checked.
- (E1), (E3) and continuum P' were not checked; they are not my step.
- The tolerance of the Monte-Carlo checks is 4 SE. P2b at r = 0.3 sits at 1.7 SE.
- The chain is lossy: P8 is about 14.8 nats below the true T², and in 1D the true cost is ≈ (4/3)a^{3/2} against my 8.35a. This does not matter for η → 0.

## 5. Delegated questions and outcomes

- **Child T152** (admitted under T150, run as register check K2 child-run1, released).
  - Question: in the 1D grid model (κ = 0.5, β ∈ {256, 1024, 4096}, a ∈ {0.05, 0.1, 0.2, 0.4}):
    - (Q1) √β L(a) ≤ √β J(a) + log β;
    - (Q2) L(a) ≤ 10a.
  - Control: c* = 4.6054, graded CORRECT before reading the rest.
  - Outcome: Q1 met 12, failed 0. Q2 met 12, failed 0. √β(L − J) ∈ [−2.09, −0.05].
  - My rerun of its main.py (K4, in child_rerun/) reproduced the numbers.
  - The reduced two-direction model was not delegated, because it was not feasible in 6 minutes.
- **Grandchild T154** (admitted by the child under T152, released by the child).
  - Question: an independent recomputation of √β L(0.1) at β = 256, and the boundary case L(0) = 0.
  - Control: c* = 4.605413, correct.
  - Outcome: 0.375048, and L(0) = 0. The child's rerun agreed.
  - I did not rerun the grandchild myself; I reran only the child's main.py, which gives the same 0.375048.

## 6. Rerun commands (from /home/user/z4-workers/q1-harnack)

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name harnack-check-rerun --expect-exit 0 -- python3 harnack_check.py <newtag>
$P check --ws pcp --name lean-harnack-rerun --cwd /home/user/z4-lean --expect-exit 0 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/q1-harnack/Harnack.lean'
mkdir child_rerun2 && cp child/main.py child_rerun2/ && $P check --ws pcp --name child-main-rerun2 --cwd child_rerun2 --expect-exit 0 -- python3 main.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Child (original run):

```
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label q1-harnack-child --parent T150
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T152
```

Last line of each verify:
- `$P verify --ws pcp`: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- `pcpos verify pcp/register.jsonl`: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
