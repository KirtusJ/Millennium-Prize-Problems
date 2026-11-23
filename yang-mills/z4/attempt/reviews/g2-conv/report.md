# report g2-conv (task T77, Director Z4)

**What is proved, as the first line of SCALING_LIMIT.md says:**
- PROVED: with K normalised (κ_0 = 1), limsup β^{1/3}ν_k ≤ E_k for every k.
- CLAIMED, not proved: liminf β^{1/3}ν_k ≥ E_k for every k, and therefore β^{1/3}m_e → E_1 − E_0. The final compactness step (L6, L7) is only a sketch.
- As posed, with K unnormalised, the theorem is false (an additive constant of about 3 ln β).

I am the same model family as the director. My agreement with my own proof is not independent review.

## 1. Verdict table

| item | verdict | one line of evidence |
|---|---|---|
| Theorem as stated in the brief (K eigenvalue e^{−β}(2/β)I_{2j+1}) | DEFECT | −log T_brief = −log T_norm + c(β), with c(β) = 3 ln β + O(1) → ∞, so β^{1/3}μ_k → ∞. Gaps are unaffected (SCALING_LIMIT §0). |
| h has compact resolvent; E_0 ≥ 2.9458 | STANDS | Fibre oscillator bound gives h ≥ −¼Δ + \|Y_1\| + \|Y_2\| (C1). Airy constant reproduced (B7); 2.9458 ≤ 3.3505 (B8). |
| limsup β^{1/3}ν_k ≤ E_k, every k | STANDS (PROVED) | U0–U5: cited Bessel-ratio lower bound, chart comparison sin²a ≤ a², V ≤ 2β\|A_1×A_2\|², center cross terms O(β³e^{−β}). No eigenfunction decay is needed. |
| L4 capped fibre lemma, (1−K_1) + 2βσ²\|x⃗×n\|² ≥ σ − 1/β for σ ≤ 0.002 | STANDS (PROVED) | The potential is banded (degree 2), so spin-IMS costs about 98.7σ²; B4 plus S7 (rechecked, Lean F4). |
| L5 tightness: the arms carry o(1) mass at energy O(β^{−1/3}) | STANDS (PROVED from L3, L4) | Mass outside the boxes is ≤ (E + C/R²)/R. |
| liminf β^{1/3}ν_k ≥ E_k, every k | NOT CHECKED (CLAIMED) | L1–L5 are proved; the Γ-liminf L6 and conclusion L7 are sketches. |
| β^{1/3}m_e → E_1 − E_0 > 0 | NOT CHECKED (CLAIMED) | Depends on the previous row. NUMERICS.md data agree (measured). |
| Brief's coercivity 2(a), in the uncapped form 1−K+V ≥ D − Cβ^{−1/3}, D = \|sin a_1\|+\|sin a_2\| | DEFECT (of that form) | Child: β^{1/3}·inf = −2.39 (β=16) and −3.35 (β=64), Galerkin upper bounds still falling. Cause: 1−K ≤ 1. The capped form (L4/L5) is what holds. |
| Gap on the full gauge-invariant space is not of order β^{−1/3} | STANDS (measured, not proved) | Center-odd copies are split by e^{−c√β} (NUMERICS.md). |
| U(1)² discriminator: L4/L5 fail, gap 2/β | STANDS | V ≡ 0 removes L4. β·(−ln(I_2/I_0)) = 2.064, 2.016, 2.004, 2.001 (checks M1). |
| Child control −ln(I_3(16)/I_1(16)) = 0.257416 | STANDS | My power series gives 0.257416, computed before reading the child's output. |
| Child numbers | STANDS | Rerun in rerun_child/ (K4, K5): identical. |

**Predicate counts.**
- My programs: **met 9, failed 1, measured only 1**. The failure is checks run K1, which exited 1. That was my own defect: a print statement crashed after all predicates were already met in results/checks.json.
- Lean: 6 of 6 lemmas pass (exit 0; axioms propext, Classical.choice, Quot.sound).
- Delegated: **met 1, failed 1, measured only 2**. The failed one, P1, was my own expectation.

## 2. Hypotheses each statement uses, and where they are stated

| Hypothesis | Used by | Where stated |
|---|---|---|
| H1. K normalised, κ_n = I_{n+1}/I_1. Sector S = center-even, conjugation-invariant. | all statements | SCALING_LIMIT §0 |
| H2. Bessel-ratio bounds: Ruiz-Antolín & Segura, arXiv:1606.02008 (2016), Thm 2 (b_0, b_1). Read through a fetch sub-agent from the arXiv HTML. | U1, L2, L4 | U1. Also NUM B1, B2: 5614 cases, 0 failures. |
| H3. Reed–Simon IV XIII.47 and XIII.67; Abramowitz–Stegun Table 10.13. Cited from memory, not reread. | C1, C2 | C1, C2 |
| H4. The Friedrichs extension defines h. | C3 | C3 |
| H5. TORON_GAP S1 (exact reformulation) and S7 (fibre Jacobi bound). S7 was recomputed here. | U0, L4 | U0, L4 |
| H6. Rellich compactness and weak lower semicontinuity. | L6 | L6 (sketch) |
| H7. NUMERICS.md value E_0 = 3.3505330. | B8 consistency check only | C1 |

## 3. Failed predicates (all kept)

1. **checks K1 (exit 1).** My own defect: json.dumps of numpy booleans raised an error after results/checks.json had been written. All B0–B8 were met in that file. Rerun as K2 to results/checks2.json: exit 0.
2. **Child P1**, β^{1/3}·inf spec(1−K+V−D) ≥ −1. It qualified in 0 of 2 β values (β=256 not run).
   - This was my own expectation, not a defect of the target. I set the predicate from the continuum, where h ≥ −¼Δ + |Y_1| + |Y_2|, and ignored that the lattice kinetic term is capped at 1.
   - The tolerance −1 was my own choice. The continuum value would be ≥ 0.

## 4. Not checked

- L6 and L7 in full detail. The whole liminf half has had no independent reader.
- The Reed–Simon and Abramowitz–Stegun locators were not reread. Ruiz-Antolín–Segura was read only through a sub-agent (its last third summarised).
- β = 256 for the coercivity numerics.
- The swap-symmetric, L-even reduction the child used at N > 12. The child flagged this as an assumption.
- The upper-bound constants as explicit numbers in β. No rate of convergence.
- Three spatial directions.
- The center-odd splitting (not proved).

## 5. Delegated questions and outcomes

- **Child T82** (admitted under T77, run recorded as K3 `child-run1`, then released).
  - Question: the coercivity check 2(a), i.e. Λ(β, c1) = inf spec(1−K+V−c1·D) for c1 ∈ {0, 1}, at β = 16, 64 (and 256 if time allowed), Galerkin.
  - Control: graded first, correct.
  - Outcome:
    - c1 = 0: β^{1/3}Λ = 2.0038 (β=16), 2.4601 (β=64). Converged to about 1e−4.
    - c1 = 1: −2.39 and −3.35. Not converged; the values keep decreasing with N.
    - P4 sanity value 0.811274 was met.
  - I reran lam.py check and main in a copy (K4, K5): identical outputs.
- **Grandchild T85** (admitted by the child under T82, released; both seen in the task graph).
  - Question: an independent recomputation of Λ(16, 0) at N = 12, using Gauss–Legendre in a and the full space.
  - Control: 0.257416.
  - Outcome: 0.811274, the same as the child.
  - I did not rerun the grandchild myself; the child reports that it did.

## 6. Registers

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## 7. Rerun commands

Run from /home/user/z4-workers/g2-conv. Result files are opened with mode "x", so move results/ and rerun_child/result_*.json away first.

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control 0.272341
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
OMP_NUM_THREADS=1 $P check --ws pcp --name checks2 --expect-exit 0 -- python3 checks.py
cd /home/user/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/g2-conv/scalar.lean; cd /home/user/z4-workers/g2-conv
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label g2-conv-child --parent T77
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T82
cp child/lam.py rerun_child/ && cd rerun_child && export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 && \
  $P check --ws ../pcp --name rerun-child-check --cwd . --expect-exit 0 -- python3 lam.py check && \
  $P check --ws ../pcp --name rerun-child-main --cwd . --expect-exit 0 --timeout 200 -- python3 lam.py main; cd ..
$P verify --ws pcp ; $R verify pcp/register.jsonl
```

**Files:**
- control.txt, notes.md, checks.py, results/checks{,2}.json, scalar.lean, lean_run1.log
- SCALING_LIMIT.md
- child/ (report, lam.py, extra.py, grandchild/), rerun_child/
