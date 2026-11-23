# Report a2-leanR: the elementary inequalities of Theorem R, formalized in Lean

Control: `control.txt` = 0.272341 (−ln tanh 1). Lean was ready (`/home/user/z4-lean/READY` exists). The file is `A1R.lean`, namespace `A1R`. It compiled with exit 0 (register check K4). All 11 `#print axioms` lines show only `[propext, Classical.choice, Quot.sound]`. There is no `sorryAx`; the only occurrence of the word "sorry" is in the docstring.

Setting: `s : Finset ι`, `w E : ι → ℝ`, `C s w E t = ∑ i∈s, w i * exp(-(t*E i))`, `T s w E K = ∑ i∈s.filter (K < E ·), w i * exp(-E i)`, `Ebar = (∑ w i * E i * exp(-E i)) / C 1`.

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| L1 (R2 tightness) | STANDS | `A1R.L1` proved; uses only w ≥ 0 |
| L2 (iterated) | STANDS | `A1R.L2` proved; uses w ≥ 0 and c ≤ 1 only (c > 0 not needed) |
| L3 (R4 upper) | STANDS | `A1R.L3` proved; uses w ≥ 0, E_i ≥ 1, t ≥ 1 |
| L4 (R4 lower, Jensen) | STANDS (more general) | `A1R.L4` proved for EVERY real t (t ≥ 1 not needed), uses w ≥ 0 and C(1) > 0; E ≥ 1 not needed |
| L5 (mean energy ≤ 2 log D) | STANDS | `A1R.L5`; uses w ≥ 0, C(1) > 0 |
| "D ≥ 1 follows" | DEFECT as stated without E ≥ 0; STANDS with E ≥ 1 | `A1R.D_ge`: E ≥ 1 ⇒ D ≥ e^{1/2}. `A1R.D_ge_one_needs_E_nonneg`: one atom at E = −2 admits D = e^{−1} < 1 |
| L6 (spectral subspace [1,2]) | STANDS, sharp constant e | `A1R.L6` (uses only E ≤ 2), `A1R.L6_sharp'`: no D < e works (atom at E = 2), so e^{1/2} is wrong as a bound. The text's "≤ e" in A1 §2 is correct |
| L7 (converse: tail ⇒ C(c) bound) | STANDS | `A1R.L7`: C(c) ≤ (1 + D(e^a−1)/(1−e^{a−1/2}))·C(1), a = 1−c ∈ [0,1/2); needs D ≥ 0 |
| Mutation (exp(−K) in L1) | false, as intended | `A1R.mutation_false`, proved in Lean with one atom: w=1, E=2, D=e, K=3/2 |
| L8 (measure version) | NOT CHECKED | not attempted for lack of time |
| Child numeric check L1–L7 | STANDS | 10^4/10^4 qualify per statement, 0 violations; rerun reproduced identical JSON (K2) |

Counts (met, failed, measured only): **met 10** (L1, L2, L3, L4, L5, D_ge with E ≥ 1, L6, L6 sharpness, L7, mutation shown false); **failed 1** ("D ≥ 1 follows" without E ≥ 0); **measured only 3** (child's L6 maximum ratio 2.71738; L7 ratio maxima 0.99963 and 0.99976; L4 for t < 1, numerically and also in Lean).

## Exact statements proved (Lean names) and their hypotheses

All statements are stated in A1R.lean. Each uses only the hypotheses listed here.
- `L2 (hw : ∀ i∈s, 0 ≤ w i) (hc : c ≤ 1) (hC : C c ≤ D*C 1) (K)`: `T K ≤ D*exp(-((1-c)*K))*C 1`. **Dropped:** E ≥ 1, c > 0, D ≥ 0, K ≥ 0.
- `L1 (hw) (hC : C(1/2) ≤ D*C 1) (K)`: `T K ≤ D*exp(-K/2)*C 1`. This is the case c = 1/2 of L2. Same drops. The proof in A1 (R2) is correct; E ≥ 1 is not used.
- `L3 (hw) (hE : ∀ i∈s, 1 ≤ E i) (ht : 1 ≤ t)`: `C t ≤ exp(-(t-1))*C 1`.
- `L4 (hw) (hpos : 0 < C 1) (t : ℝ)`: `C 1 * exp(-(t-1)*Ebar) ≤ C t`. **Dropped:** t ≥ 1, E ≥ 1. The proof uses the tangent line of exp and no Jensen library.
- `L5 (hw) (hpos) (hC : C(1/2) ≤ D*C 1)`: `Ebar ≤ 2*log D`. **Dropped:** E ≥ 1. It is L4 at t = 1/2.
- `D_ge (hw) (hE : 1 ≤ E i) (hpos) (hC)`: `exp(1/2) ≤ D`.
- `L6 (hw) (hE : ∀ i∈s, E i ≤ 2)`: `C(1/2) ≤ exp 1 * C 1`. **Dropped:** E ≥ 1. `L6_sharp'`: `∀ D < e`, the one-atom set at E = 2 violates it.
- `L7 (hw) (hD : 0 ≤ D) (hT : ∀ K, T K ≤ D*exp(-K/2)*C 1) (ha0 : 0 ≤ a) (ha : a < 1/2)`: `C(1-a) ≤ (1 + D*(exp a - 1)/(1 - exp(a - 1/2))) * C 1`.
  - **Added:** D ≥ 0. It follows from hT when C(1) > 0, but it must be assumed when C(1) = 0.
  - **Used:** hT only at integer K ≥ 0.
  - **Dropped:** E ≥ 1.
  - The proof is a layer-cake on integer levels (lemma `layer`).
  - The continuous layer-cake gives the smaller constant 1 + 2aD/(1−2a). That one is checked numerically only (child and `l7_check.py`, 0 violations); it is not in Lean. The Lean constant was ≥ that one in all 10^4 cases.

Remarks on A1_REDUCTION.md that come out of this:
- (R4)'s "G(t) ≥ exp(−2(t−1) log D)" follows from L4 + L5 only when t ≥ 1. The direction is fine.
- The Jensen bound holds for all t, so it is stronger than the text uses.
- "By Jensen it implies mean energy ≤ 2 log D" (§2): correct.
- The claim D ≥ 1 is implicit in log D ≥ 0. It needs E ≥ 0, which (A) supplies.

## Failed predicates

- "D ≥ 1 follows" (brief, L5 note), stated without a sign condition on E: false. Counterexample proved in Lean (`D_ge_one_needs_E_nonneg`). This is a missing hypothesis in the brief's remark, not in A1, where E ≥ 1 holds.
- Compile failures during development. These were my own proof errors (wrong rewrite patterns, a nonexistent lemma name `exp_lt_one`). None was a defect of the target.
- No predicate of the target failed.

## Not checked

- L8 (finite Borel measure version) was not attempted. The atom proofs carry over line by line, but no Lean statement was made for it.
- The sharp constant in L7 was not studied.
- L7's continuous constant is not in Lean.
- (R1), (R3) (Prokhorov, uniform integrability), (R5) and (R6) are out of scope.
- The child sampled at most n ≤ 8 atoms and a single E-distribution, Exponential(scale 2) shifted by 1. For L6 it drew E uniform in [1, 2].

## Delegated questions and outcomes

- **Child** (`child/`, sonnet, register `child/pcp`, run as check `child-run1` in my register). Question: a Python check of L1–L7 plus the mutation on 10^4 random atom sets each.
  - Control: 2·log(e) = 2. Answer "2.0", graded correct before I read its other output.
  - Result: all statements STANDS (0 violations, 10^4 qualifying each). L4 also holds for t ∈ [−1, 1). The maximum observed C(1/2)/C(1) on [1, 2] was 2.71738 < e. The mutation fails with one atom (w=1, E=2, K=1.5).
  - I reran its program through my register (K2, `results_parent_rerun.json`). The output is identical to its `results_main.json`.
- **Grandchild** (`child/grandchild/`, Agent of the child). Question: recompute, for the atom w=1, E=2, the ratio C(1/2)/C(1) and both sides of the mutated L1 at D=e, K=1.5.
  - Control answered 3.0. The child graded it correct; I did not see the control question itself.
  - Returned: 2.718281828459045; T = 0.1353352832366127 > 0.08208499862389879 = e^{−2.5}.
  - The same counterexample is proved in Lean (`mutation_false`), so it is independently confirmed.

## Register

- `$P verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## Rerun commands

```
cd /home/user/z4-workers/a2-leanR
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name lean-A1R-rerun --cwd /home/user/z4-lean --timeout 290 --expect-exit 0 -- env PATH=/root/.elan/bin:/usr/bin:/bin lake env lean /home/user/z4-workers/a2-leanR/A1R.lean
$P check --ws pcp --name l7-numeric-rerun --expect-exit 0 -- python3 l7_check.py l7_result_rerun.json
$P check --ws pcp --name rerun-child-check2 --cwd child --expect-exit 0 -- python3 pcp_check.py results_parent_rerun2.json
$P check --ws pcp --name child-run2 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Note: the child's result files are opened with mode "x". A second child run in the same directory will fail on existing names unless it picks new ones.
