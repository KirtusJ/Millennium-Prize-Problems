# report: h1-liminf (T86), the lower half of the scaling limit

Deliverable: `LIMINF.md`. Control: `control.txt` = 0.272341 (−ln tanh 1).
Lean was ready (`/home/user/z4-lean/READY` exists).
The director, the target's author and I share a model family, so this is not independent review.

## Verdict table
| item | verdict | evidence |
|---|---|---|
| L6 (Γ-liminf in one box) | STANDS (now written in full) | LIMINF §4. Spin split (2.1); restriction to □' instead of a commutator; Rellich; mollification puts ψ in Q(h); lsc; m → 0 last |
| L7 (liminf β^{1/3}ν_k ≥ E_k, every k) | STANDS (now written in full) | LIMINF §5. IMS error explicit, π⁴/(4R²)·β^{−1/3}; Gram matrix ≥ (1−τ_R)I; limits in the order β, then m, then R. Uses no §2 input (the case Λ = ∞ is trivial) |
| Corollary liminf β^{1/3}m_e ≥ E_1−E_0 | NOT CHECKED (conditional) | Needs the §2 limsup for k = 0 (not rechecked by me) and C2 (cited from memory in the target) |
| L1 (T → H, lower direction) | STANDS | Rechecked line by line: monotone in w, then t/(1+t) |
| L2 (∫k d² ≤ π²/β) | STANDS | Rechecked; 1 − r_1 ≤ 2/β from (A) |
| L3 (IMS for K) | DEFECT (minor: sign typo), STANDS in the form used | The correction term enters with the opposite sign to the one printed; only its absolute value is used |
| L4 (capped fibre lemma) | DEFECT (minor: constant), STANDS | Commutator bound is 8π²σ² ≈ 79σ². The text has "98.7σ²", but its own formula gives 197σ² (it dropped ‖B‖ = 2βσ²). Both close: √2 − 0.158 > 1 and √2 − 0.394 > 1 |
| L5 (tightness) | DEFECT (minor: partition), repaired | χ_1 = η_1(1−η_2²)^{1/2} need not be Lipschitz. Replaced by the sin/cos (S²-embedding) partition, which gives the explicit Lipschitz bound |
| S7 (TORON_GAP fibre bound) | STANDS | (−Δφ)/φ recomputed; minimisation is Lean G4 |
| Bessel bounds (A), (B) | STANDS (CITED + NUM) | Ruiz-Antolín–Segura arXiv:1606.02008 Thm 2, read; my program and the child each found 0 failures on 5614+5614 cases |
| K1, K2 (spin-cutoff inequalities) | STANDS | Proved from (A), (B) with Lean G1, G2, G3, G6a, G6b, G7; NUM Q3–Q5, 0 failures |
| Chart comparison | STANDS | LIMINF §3; Lean G5; NUM Q7 |

Counts (met, failed, measured only):
- my predicates Q0–Q7: 8 met, 0 failed, 0 measured only;
- child predicates A–D: 4 met, 0 failed;
- Lean lemmas: 9 met (G1–G8, with G6 counted as a and b), 0 failed in the final run. The first run failed (see below).

## Hypotheses each statement uses, and where they are stated
- **K1:** Bessel bounds (A), (B) (LIMINF §1, CITED: RS Thm 2); integer n ≥ 0, β > 0.
- **K2 / (2.1):** K1; m ∈ (0, ½], M = ⌊m√β⌋; K diagonal in Peter–Weyl degree (SCALING_LIMIT §0).
- **Chart (3.1), (3.2):** a_max ≤ 1 (i.e. β ≥ (4R)³); exponential coordinates; normalised Haar measure (LIMINF §3).
- **L6:** f_l supported in B_β (rescaled radius ≤ 3R), ‖f_l‖ ≤ 1, β^{1/3}⟨f_l,Hf_l⟩ ≤ C; R fixed; Rellich–Kondrachov (CITED, Evans §5.7, from memory) (LIMINF §4).
- **L7:**
  - Λ := liminf β^{1/3}ν^H_k < ∞ (otherwise trivial);
  - β ≥ max(β_0 of L4, (R/s_*)³, (4R)³, β_1(R));
  - R ≥ R_0 with τ_R < ½;
  - L1–L4 in the restated forms;
  - Weyl's theorem and the min-max principle (CITED, Reed–Simon IV XIII.1–2, from memory);
  - center-evenness and conjugation invariance of S (LIMINF §5).
- **E_k:** defined as min-max values of h on L²_inv. They equal eigenvalues under C1 (target, cited there), which the inequality does not need.

## Failed predicates
- Lean run K2 (lean-run1) exited 1: the proof of G2 left a goal open (sorryAx appeared in its axioms). **Own error, not a target defect**: a `1/x` vs `x⁻¹` mismatch. Fixed; run K4 exited 0 with axioms {propext, Classical.choice, Quot.sound} for every lemma.
- No numerical predicate failed.
- Tolerances:
  - my Q1–Q5: 1e−10 relative, from a 100× margin over about 1e−12 accumulated double-precision error;
  - my Q6/Q7: 1e−12;
  - my Q0: 1e−9 against known values, and 1e−7 against the finite-difference derivative of np.i0 (truncation O(h²) plus rounding about 1e−11);
  - child: 1e−25 with Decimal precision 70.
- Tightest margins:
  - Q1 has relative slack 9.7e−10 at (ν = 400, x = 0.5), only about 10× the tolerance. The child confirmed it at 70 digits (9.6686e−10).
  - Q3: 2.0e−4 at n = 1, β = 10⁴.

## What I did not check
- SCALING_LIMIT §2 (the upper half, including the upper direction of L1 / U0, U1–U5) and C1/C2 (compact resolvent of h, simplicity, E_1 > E_0). Hence the corollary is conditional.
- Rellich–Kondrachov, Weyl's theorem and the min-max principle: cited from memory, not reread.
- RS 2016 was read by a fetch sub-agent: the HTML v1, first 40k of 73k characters, which contain Thm 2. Its reference list (the attribution of the bounds to Amos or others) was not read.
- The Lean file covers only the scalar steps. The operator arguments are paper proofs.
- No rate of convergence. The lower bound is not uniform in k (constants depend on k through Λ).
- The constant in ε_X (four-box cross terms) is elementary but was not checked numerically.

## Delegated questions and outcomes
- **Child T90** (admitted under T86 as event 178; released as event 187). Run recorded as K3 in my register, exit 0, 91.6 s.
  - Question: an independent numerical check of (A), (B), (C), (D), on n, ν = 0..400 and 14 values of β in [0.5, 10⁴].
  - Control: I_1(1)/I_0(1) = 0.446390. **Graded correct** before reading anything else.
  - Outcome: A, B, C, D all met, 0 failures. Its smallest slacks agree with mine to 3 digits.
  - I reread its program (Decimal precision 70; backward continued fraction at two depths) and reran it (K5, exit 0, identical counts and slacks).
- **Grandchild T92** (admitted by the child under T90 as event 182; released as event 184).
  - Question: independently recompute −ln κ_1 and −ln κ_2 at β = 1000 and 10⁴ against (C), and the tightest case of (B), by power series.
  - Control: 0.446390, correct.
  - Outcome: all met. (B) slack 2.5001e−9 at (0, 10⁴), matching both the child and me.
  - Rerun by the child, and by me (unrecorded in gc_rerun/, recorded as K6): identical output.

## Commands to rerun (from /home/user/z4-workers/h1-liminf)
```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name scalars-rerun --expect-exit 0 -- python3 prog/scalars.py results/scalars_rerun.json
$P check --ws pcp --name lean-rerun --expect-exit 0 --cwd /home/user/z4-lean -- bash -c "PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/h1-liminf/lean/Liminf.lean"
$P check --ws pcp --name child-bessel-rerun --expect-exit 0 --cwd child --timeout 600 -- python3 bessel_check.py results_rerun3.json
mkdir -p gc_rerun3 && $P check --ws pcp --name grandchild-rerun2 --expect-exit 0 --cwd gc_rerun3 --timeout 300 -- python3 /home/user/z4-workers/h1-liminf/child/grandchild/chk.py
$P check --ws pcp --name child-run2 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"   # needs a fresh task-admit; outputs are mode "x"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Last line of `$P verify --ws pcp`:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Last line of `pcpos verify pcp/register.jsonl`:
`A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
