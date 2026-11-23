# r3-chaos report: mutation test of Director Z4 (Lean files and two_dim_control.py)

Control: control.txt = 0.272341 (-ln tanh 1). Baseline (hypothesis test): all 6 originals compile with exit 0, no sorry, axioms only propext/Classical.choice/Quot.sound (B0: 6 of 6 qualify). Program baseline: exit 0, H/P1/P2/P3 MET, JSON byte-identical to input (sha256 24939c8d…9d0f).

## 1. Verdict table (one row per mutation)

Lean evidence = exit code and first error line (results/m1_result.json). FALSE/TRUE is my prediction for the mutated statement, made before compiling.

| # | file / theorem | change | pred. | verdict | evidence |
|---|---|---|---|---|---|
| S1 | Scaling / physical_gap_tendsto_atTop | drop `0 < c` | FALSE | CAUGHT | exit 1, 36:79 unknown identifier 'hc' |
| S2 | Scaling / lattice_gap_tendsto_zero | limit 𝓝 0 → 𝓝 1 | FALSE | CAUGHT | exit 1, 28:8 application type mismatch |
| S3 | Scaling / lattice_gap_tendsto_zero | drop `a n ≠ 0` | FALSE | CAUGHT | exit 1, 28:48 unknown identifier 'ha0' |
| T1 | TwoSided / twoSided_cluster | `c ≤ L` → `c < L` | FALSE | CAUGHT | exit 1, 14:9 application type mismatch |
| T2 | TwoSided / twoSided_of_tendsto | `(M/2)*a n` → `M*a n` | FALSE | CAUGHT | exit 1, 36:39 linarith failed |
| T3 | TwoSided / twoSided_cluster | drop `0 < c` | TRUE | ACCEPTED-AS-TRUE | exit 0: hypothesis unnecessary (also flagged by linter) |
| F1 | FiniteGroupControl / z2_physical_gap_le | 1/(1+x) → 1/(2+x) | TRUE | REJECTED-BUT-TRUE (see note) | exit 1, 51:51 unsolved goals; numerically max x(-log tanh x)(2+x) = 0.971 < 1 at x≈0.568 |
| F2 | FiniteGroupControl / z2_gap_le | 2/(e^{2x}-1) → 1/(e^{2x}-1) | FALSE | CAUGHT | exit 1, 39:60 unsolved goals |
| F3 | FiniteGroupControl / z2_gap_pos | drop `0 < x` | FALSE | CAUGHT | exit 1, 30:64 linarith failed |
| L1 | LevelsControl / levels_gap_le | drop spacing hgap | FALSE | CAUGHT | exit 1, 54:39 unknown identifier 'hgap' |
| L2 | LevelsControl / levels_gap_le | drop smallness hsmall | FALSE | CAUGHT | exit 1, 75:37 linarith failed |
| L3 | LevelsControl / levels_gap_le | 4K → 2K | FALSE | CAUGHT | exit 1, 36:90 unsolved goals (counterexample: K large, q=1/(2K), χ=-1 off i0 gives log 3 > 1) |
| L4 | LevelsControl / levels_physical_gap_tendsto_zero | drop `0 < d` | FALSE | CAUGHT | exit 1, 129:39 unknown identifier 'hd' |
| C1 | CharTransfer / conv_char | drop multiplicativity | FALSE | CAUGHT | exit 1, 58:54 unknown identifier 'hψ' |
| C2 | CharTransfer / coeff_real_even | drop evenness | FALSE | CAUGHT | exit 1, 110:10 unknown identifier 'heven' |
| C3 | CharTransfer / iterate_char | exponent N → N+1 | FALSE | CAUGHT | exit 1, 65:9 unsolved goals |
| C4 | CharTransfer / coeff_real_even | drop `‖ψ y‖ = 1` | TRUE | REJECTED-BUT-TRUE (see note) | exit 1, 94:24 unknown identifier 'hu'; on a finite group multiplicative ψ is ≡0 or unitary (argument, not formalized) |
| A1 | TrajectoryAudit / w_upper | drop `D ≥ 36κ²` | FALSE | CAUGHT | exit 1, 73:25 linarith failed |
| A2 | TrajectoryAudit / L_lower | 9/64 → 10/64 | FALSE | CAUGHT | exit 1, 65:2 linarith failed |
| A3 | TrajectoryAudit / w_upper | 9/512 → 8/512 | TRUE | REJECTED-BUT-TRUE (see note) | exit 1, 79:2 linarith failed; numerically max((1+β)/(2(1+B)))² = 0.4665, so sharp constant ≈ 9·0.4665/512 |
| A4 | TrajectoryAudit / L_bounded_forces | drop `b ≤ b0` | FALSE | CAUGHT | exit 1, 124:42 unknown identifier 'hb0' |
| A5 | TrajectoryAudit / L_tendsto_top | atTop → atBot | FALSE | CAUGHT | exit 1, 85:6 rewrite failed |
| A6 | TrajectoryAudit / w_upper | (1+β)^2 → (1+β)^3 | FALSE | CAUGHT | exit 1, 79:2 linarith failed |
| Pa | two_dim_control.py | I_1 → I_2 in U(1) gap (l.101) | P1 | CAUGHT | exit 1, P1 failed (child) |
| Pa2 | two_dim_control.py | u1_closed uses I_{n+1} (l.62) | H | CAUGHT | exit 1, H and P1 failed (child) |
| Pb | two_dim_control.py | β = N² → N²+1 for U(1) | P1 | CAUGHT | exit 1, P1 failed (child) |
| Pc | two_dim_control.py | SU(2) 4N² → 2N² | P2 | CAUGHT | exit 1, P2 FAILED; **rerun by me**: H MET, P1 MET, P2 FAILED, P3 MET |
| Pd | two_dim_control.py | Z_n asymptote k·d → k·d/2 | P3 | CAUGHT | exit 1, P3 failed (ratio 2.0) (child) |
| Pe | two_dim_control.py | TOL_H × 1e6 | none | NOT CAUGHT | exit 0; **rerun by me**: exit 0, JSON sha256 identical to input |
| Pe2 | two_dim_control.py | P3 tolerance 1e-6 × 1e6 | none | NOT CAUGHT | exit 0, JSON byte-identical (child) |
| M4 | two_dim_control_result.json copy | one digit changed (l.197, P1 M for N=8) | not noticed | NOT CAUGHT by input/ checks | program never reads an existing result; no Lean file reads it; only rerun + byte compare detects it (equal False) |

**Counts (caught, not caught, accepted as true): 24, 3, 1.** In addition, 3 mutations (F1, C4, A3) are measured only: the statements stay true, yet Lean rejects them.
Lean: 19 caught, 0 not caught, 1 accepted as true, 3 rejected but true. Program: 5 caught, 2 not caught. M4: 1 not caught.

No FALSE-predicted mutation compiled with exit 0, so there is no serious finding. None of the mutated sources contains `sorry`. The JSON flag `sorry: True` on the rejected mutants comes from Lean inserting sorryAx after an elaboration error. It is not a sorry in the source.

**Plain reading:**
1. A Lean rejection here does not show that the mutated statement is false. 10 of 19 catches are "unknown identifier": the proof names a hypothesis that was removed, which is a purely mechanical catch. F1, C4 and A3 are rejected just as firmly although their statements are true. Lean checks that a proof fits a statement, and that is all it checks. Whether a statement is sharp has to be argued separately.
2. **Non-sharp originals (findings):**
   - TwoSided: twoSided_cluster has unused `0 < c`, `c ≤ C` and `StrictMono φ`.
   - FiniteGroupControl: z2_physical_gap_le, where 1/(2+x) also holds numerically.
   - CharTransfer: coeff_real_even, where `‖ψ‖ = 1` is redundant on a finite group.
   - TrajectoryAudit: w_upper's 9/512, where about 4.4 bits of slack remain (factor 0.4665).
   These do not make anything false. The original statements are weaker than they could be.
3. **Program:** a loosened tolerance is invisible to every predicate and to a byte comparison. H only tests the helper closed forms, while P1 and P2 make their own Bessel calls, so H does not guard them.

## 2. Hypotheses each statement uses (where stated)
- Scaling: lattice_gap_tendsto_zero uses a→0, a n≠0 and m/a→M (l.22–24). physical_gap_tendsto_atTop uses 0<c, a→0⁺ and c≤m n (l.32–33). The no-go theorem uses all of these (l.45–47).
- TwoSided: cluster uses 0<c, c≤C (unused), a>0, two-sided bounds, StrictMono φ (unused in the first theorem) and the subsequence limit (l.5–8, 16–19). of_tendsto uses a>0, M>0 and m/a→M (l.29–31).
- FiniteGroupControl: 0<x in every theorem (l.30, 39, 51). The transfer-eigenvalue identification is NOT formalized (docstring).
- LevelsControl: hgap, |χ|≤1, χ i0=1, b≥0, hsmall (l.31–34); 0<d for the limit (l.116). The Z_n identification is NOT formalized (docstring).
- CharTransfer: multiplicativity (F1–F3 only for F1/F2); F4 uses multiplicativity, ‖ψ‖=1 (redundant) and evenness (l.86–88); coeff_eq_lam1 uses evenness of c.
- TrajectoryAudit: β>0, b>0 throughout; D≥36κ² (w_upper, w_tendsto_zero); β→∞ (w_tendsto_zero); β(1+2β)b→0 (L_tendsto_top); b≤b0, C>0, L≤C (L_bounded_forces).
- two_dim_control.py: hypotheses and predicates are in its docstring (H, P1, P2, P3). Read by the sub-agent; I read only the two lines that were mutated.

## 3. Failed predicates
- Mine (mutate.py): none failed. B0 6/6, A 23/23 unique, K 19/19 rejected.
- My expectation vs outcome: for F1, C4 and A3 I wrote "may accept". Lean rejected all three. That was a gap in my own expectation (the proofs are tailored to the constants and hypotheses). It is not a defect of the target.
- Child: K12, a mis-pathed command (exit 2, expected 1). This was the child's own error and is kept in child/pcp.
- Target: Pe and Pe2 pass when they should be caught. This is a defect of the target's check design. The predicate that needs adding: write the tolerances into the JSON and compare them against the docstring, plus negative controls (a perturbed closed form must fail H, and a ratio of 1+1e-5 must fail P3), or pin a hash of the program source. For M4 the program would need a mode that re-derives and compares an existing result.

## 4. Not checked
- I did not prove in Lean that F1, C4 and A3 are true. F1 and A3 rest on a numerical scan in step 1e-4 / 1e-3 (pure float, no interval bounds). C4 rests on a paper argument.
- I did not formalize any counterexample for the FALSE predictions. The prediction "false" is a paper argument, written in the `why` field of mutate.py.
- Only 23 single mutations. I did not mutate downstream theorems separately (for example w_tendsto_zero, iterate_eq_kern, coeff_one_eq_lam0, complementary_needs_b_bound).
- Of the child's program mutations I reread and reran 2 (Pc, Pe). The other 5 are its claims.

## 5. Delegated question and outcome
- **Delegated:** M3 (at least five single mutations of two_dim_control.py: Bessel order, β=N²+1, SU(2) 2N², Z_n constant halved, loosened tolerance; report which predicate fails) and M4 (one digit changed in a result copy; would any input/ check notice?).
- **Control question:** -ln tanh 1 = 0.272341, answered correctly.
- **What came back:** 7 mutations, 5 caught (P1, H+P1, P1, P2, P3) and 2 tolerance mutations not caught. M4 is not noticed in input/ and is detected only by rerun plus byte compare. The child's verify result was PASS.
- **My check:** I reread the diffs of Pc and Pe (single-line changes, as claimed) and reran both in fresh dirs rerun/ under my own register (K1 exit 1 with P2 FAILED, K2 exit 0 with JSON identical). Both claims are confirmed.

PCP verify (my register), last line:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

## 6. Rerun commands (Git Bash, from C:/Users/donke/z4-workers/r3-chaos, PYTHONUTF8=1)
```
P=C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py; SP=C:/Users/donke/AppData/Roaming/Python/Python314/site-packages
mv results/m1_result.json results/m1_result.prev.json   # program refuses to overwrite
python $P check --ws pcp --name m1_lean_mutations --expect-exit 0 -- python mutate.py   # ~11 min, 6 parallel lean
# single file by hand: cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r3-chaos/mut/<NAME>/<File>.lean
rm -rf rerun/X && mkdir -p rerun/X && cp child/mut/c_su2_2N2/two_dim_control.py rerun/X/ && (cd rerun/X && python $P check --ws ../../pcp --name rerun_c --expect-exit 1 -- python -I two_dim_control.py $SP)
rm -rf rerun/Y && mkdir -p rerun/Y && cp child/mut/e_tolH_1e6/two_dim_control.py rerun/Y/ && (cd rerun/Y && python $P check --ws ../../pcp --name rerun_e --expect-exit 0 -- python -I two_dim_control.py $SP)
python $P verify --ws pcp
# child: see child/report.md section "Rerun commands"
```
