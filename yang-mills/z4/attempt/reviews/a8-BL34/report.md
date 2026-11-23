# report a8-BL34 — Theorem B′: closing L3 and L4

Worker a8-BL34 for Director Z4. Principal: Kirtus Justus. I am the same model family as the author of PROOF_B_v2, so this is not independent review.

## Verdict table

| # | item | verdict | evidence (one line) |
|---|---|---|---|
| 1 | L3(a): exact conditional density in the chart, Haar Jacobian J = (sin\|x\|/\|x\|)²/(2π²), and ψ depending on shell variables only | STANDS | L3_L4.md §2(a). Locality of plaquettes, the forest gauge lemma with T_int, and a shell gauge built from T_s. |
| 2 | L3(b): lower bound βS ≥ c\|φ\|² − 7M² on the whole chart | STANDS | §2(b). Near region: c = λ/16 via (E1)–(E3) and the Lean inequalities. Far region: η(δ) > 0 by compactness plus the zero set of Lemma A. |
| 3 | L3(c,d): uniform Laplace limit over \|ψ\| ≤ M, with uniform tightness | STANDS | §2(c,d). Gaussian domination e^{7M²−c\|φ\|²}, uniform convergence on compacts, and Z_∞ ≥ z_M > 0. |
| 4 | Zero set of S_R with trivial shell data is {U ≡ 1} (no gauge copies, no non-trivial flat connections) | STANDS | Lemma A: an axial-tree induction, valid for any group. |
| 5 | Shell of a 4-box is simply connected (v2's K_N) | STANDS | Lemma B: gluing the 8 faces, valid for any group. Also prog1 Q2: H¹(shell; ℝ) = 0 for N = 1, 2, 3. |
| 6 | L4(a): lasso field F, path and base independence, colour and translation invariance, Bianchi with order β^{−1/2} | STANDS | §3(a)(i)–(iv). The base-change step uses a Haar-gauge randomisation argument. |
| 7 | L4(b): tightness, joint convergence of O_p → ½\|F_p\|², convergence of moments up to 4th | STANDS* | §3(b). Exact identity O_p = f_β(\|F_p\|) and the S3a tails. |
| 8 | L4(c): DLR of the limit for the Maxwell–Dirichlet specification (precise statement and test class) | STANDS* | §3(c). Uses L3 on \|ψ\| ≤ M, the S3a tail off it, and ψ = L F_sh + o_P(1). |
| 9 | Explicit c, C(M) in L3(b), as the brief asked | DEFECT | The far-region constant η(δ) is proved positive but is not explicit. |
| 10 | v2's L4 definition of F through a global axial tree | DEFECT | It is fragile, because it relies on fixed links being fixed-size loops. Replaced here by the lasso field. |
| 11 | v2's M1 test box labels | DEFECT (harmless) | v2's 0.2917 and 0.4927 equal my C_pp for N = 1 and 2, so v2's "N" there is the side length 2N. |
| 12 | Theorem B′ PROVED in this folder's strict sense | DEFECT | Six standard measure-theory facts (L3_L4.md §6) are used with no source read in this run. |
| 13 | Numerical test of L3(b), N = 1 box, β = 10/100/1000 | STANDS | Child T2: c_eff ≥ 0.1738 ≥ λ/16 = 0.0524 in 120/120 cases. |
| 14 | Monte Carlo Gaussian limit of E O_p against (3/2)C_pp = 0.4375 | STANDS | Child t3b at β = 1000: 0.437448 ± 0.000852. I reran it and the output is bit-identical. |
| 15 | Lean: 1 − cos x ≥ 2x²/π²; ½(a−b)₊² ≥ a²/4 − b²/2; ‖u+v‖² ≥ ½‖u‖² − ‖v‖²; e^s − 1 − s ≤ (s²/2)e^s | STANDS | L34.lean exits 0. Axioms: propext, Classical.choice, Quot.sound. No sorry. /home/user/z4-lean/READY exists. |
| 16 | The rest of PROOF_B_v2 (Lemmas 1, 1′, 2, 3, D, R, G, the inequality) | NOT CHECKED | Not re-audited. Used as stated. |

\* Modulo the standard facts listed in item 12.

Verdict counts: STANDS 11, DEFECT 4, NOT CHECKED 1.

**Theorem B′ after this work.** L3 and L4 are PROVED here, apart from item 12. Theorem B′ is therefore PROVED in this folder's sense except for one line: the six textbook probability facts in L3_L4.md §6, which are uncited and unread. v2's restrictions remain: L = 2^k, periodic limit states only, and the conclusion m → 0.

## Hypotheses and where each is stated

- **β ≥ β₀(M) = max(M²/δ², 144 n_s M²/η²).** Stated in L3_L4.md §2(b). δ is fixed by 48δ²e^{8δ} ≤ min(λ/16, 1).
- **λ > 0.** This is Lemma H of PROOF_B_v2 §3 (T_int pinned, Dirichlet shell).
- **μ ∈ 𝓛_β with β ≥ 1.** Translation and gauge invariance, and the DLR property for finite link sets, come from Lemma 1′. The tail μ(O_p > t) ≤ e^{60.2 − t/8} is the Corollary to S3a. These are PROOF_B_v2 §1–2.
- **Test-function classes.**
  - L3 applies to bounded measurable W, uniformly in ‖W‖_∞.
  - L4(c) applies to bounded Lipschitz w_in and w_out, the latter depending on finitely many F_q with q ∉ P_R.

## Failed predicates

- **prog1, run K1.** Exit 1 with no output: scipy is not installed. This was my own defect, not a defect of the target. Run v2 (K2) used closed-form SU(2) exp/log, and all of Q1–Q5 were met.
- **Lean, two compile attempts.** Both failed on tactic steps (|x|² vs x² after field_simp, and a `- 0` in a HasDerivAt term). These were my own defects and are fixed. The final run is K3, exit 0.
- **Child, t3 run 1.** The child's docstring expected an acceptance rate of 30–60%; the actual rate was about 5%. This was the child's own expectation failing, not a defect of the target. The child retuned the step in t3b and kept run 1.
- **Child, P2.** "c_eff > 0" is trivially true (the numerator is ≥ 7M²). The child flagged this itself. P2b (≥ λ/16) is the informative predicate, and it was met.

Counts (met, failed, measured only):
- mine: 6, 0, 1. Q1–Q5 and the Lean pass were met. λ and C_pp values are measured only. Separately, there was one failed run (K1) and two failed Lean compiles, all my own defects.
- child: 5, 1, 1. P1, P2, P2b, P4 and P5 were met. The acceptance expectation failed. P3 is measured only.

## What I did not check

- Lemmas 1, 1′, 2, 3, D, R and G, and the final inequality, of PROOF_B_v2.
- S2's Lean check from v1.
- An explicit value of η(δ), or the bound (b) for N ≥ 2 numerically.
- The six standard facts of L3_L4.md §6: no source was read, and no network access was used.
- The removal of the restriction L = 2^k.

## Delegated questions and outcomes

**Child** (Sonnet, headless; register child/pcp; check K4, exit 0, 265 s).
- Question: the numerical test on the N = 1 box: λ, C_pp, a minimisation of (βS + 7|ψ|²)/|φ|² over the chart, and a Monte Carlo estimate of E O_p.
- Control: λ_min of tridiag(−1, 2, −1) 5×5 = 2 − √3 = 0.267949, which I computed first. The child answered 0.267949: **correct** (graded before reading anything else).
- Returned:
  - λ = 0.837722 and C_pp = 7/24. Both match my prog1.
  - c_eff between 0.1738 and 0.2659 over 120 cases.
  - Monte Carlo E O_p: 0.438867 / 0.437357 / 0.437448 (SE about 0.00085) at β = 10 / 100 / 1000, against 0.4375.
- Its register verifies with PASS.
- My rerun (K5) on a scratch copy of t1, grandchild/prog.py, t3b 1000 and t2 1000 gave **bit-identical** outputs.
- I reread the child's action: W = V₁V₂^{−1} and U_p = U_a W U_b^{−1}, which matches the definition.

**Grandchild** (the child's sub-agent).
- Question: an independent recomputation of λ and C_pp.
- Control: 2 − √2 = 0.585786438: correct.
- Result: 0.837722340 and 0.291666667. The child reran it, and so did I (inside K5), with identical results.

## PCP OS record

- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.` The line before it gives SHA-256 64ff54d2….

The register holds K1 (prog1-checks, failed), K2 (prog1-checks-v2), K3 (lean-L34), K4 (child-run1) and K5 (rerun-child). A final verify run happens after this file is written.

## Exact commands to rerun

```
cd /home/user/z4-workers/a8-BL34
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control 0.272341
$P check --ws pcp --name prog1-checks-v2b --expect-exit 0 -- python3 prog1_checks.py result_prog1_rerun.txt   # new result filename (mode "x")
$P check --ws pcp --name lean-L34b --cwd /home/user/z4-lean --expect-exit 0 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/a8-BL34/L34.lean'
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
S=<fresh empty dir>; mkdir -p $S/out $S/grandchild; cp child/*.py $S/; cp child/grandchild/prog.py $S/grandchild/
$P check --ws pcp --name rerun-child --cwd $S --timeout 280 --expect-exit 0 -- bash -c "python3 t1.py && python3 grandchild/prog.py && python3 t3b.py 1000 && python3 t2.py 1000"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
