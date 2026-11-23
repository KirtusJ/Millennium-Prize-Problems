# Report r5-lean (formalizer, S5) — 2026-11-23

Control: control.txt = 0.272341 (-ln tanh 1). Lean file: S5.lean (Lean 4.19.0 + Mathlib). It compiles with exit 0 and no `sorry`. Every `#print axioms` lists only [propext, Classical.choice, Quot.sound].

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| scalar x e^{-x} ≤ e^{-1} | STANDS | `S5.mul_exp_neg_le`, true for **all** real x (from x ≤ e^{x-1}) |
| scalar x² e^{-x} ≤ 4e^{-2} | STANDS (x ≥ 0) | `S5.sq_mul_exp_neg_le`. `sq_mul_exp_neg_fails_neg` proves it is false at x = −1, so x ≥ 0 is needed |
| S5(a), constant 1/(eτ) | STANDS | `S5.S5a`. Sharp: one atom at E = 1/τ gives ratio 1 (child numerics) |
| S5(b), constant 4/(e²τ²) | STANDS | `S5.S5b`. Sharp: one atom at E = 2/τ gives ratio 1 (child numerics) |
| S5(c) | STANDS | `S5.S5c`, via Mathlib `Finset.sum_sq_le_sum_mul_sum_of_sq_eq_mul`, for all real s, t |
| S5(d), tail bound and window bound | STANDS | `S5.S5d`, `S5.S5d_window` |
| S5(e) | STANDS | `S5.S5e`. Side conditions are derived, not assumed (`S5e_E0_pos`, see §2) |
| (f), gap direction | STANDS | `S5.S5f` |
| (g), converse, explicit t | STANDS | `S5.S5g_lower`, `S5.S5g` |
| mutation (a) → 1/(2eτ) | rejected | exit 1, "unsolved goals" at the theorem, sorryAx appears (PCP K2) |
| mutation (b) → 3 | rejected | exit 1, "unsolved goals", sorryAx appears (PCP K3) |
| measure version | NOT CHECKED | discussed in §4 |

Counts: 9 items STANDS, 0 DEFECT, 1 NOT CHECKED. No stated constant in S5 is wrong.

Predicate counts (met, failed, measured only):
- Lean: P1 compile, P2 axioms, P3 two mutations rejected. 3 met, 0 failed (one intermediate compile failure, listed in §3).
- Child numerics: 4 met (a, b, d, e, 0 failures in all qualifying cases), 0 failed. The max ratios and the sharpness/extremal-x numbers are measured only.

About the mutations: Lean rejecting a mutated file only shows that my proof does not prove the weaker constant. It does not show the mutated statement is false. That it is false comes from sharpness: one atom at E = 1/τ (resp. 2/τ) gives equality, so with 1/(2eτ) (resp. 3) the inequality fails. The child's numerics confirm this to rounding. I did not prove the falsity in Lean.

## 2. Hypotheses each statement uses (as stated in S5.lean)

Throughout: ι is a Fintype, w, E : ι → ℝ, and C t = Σ w i · exp(−t·E i).

- **(a) S5a**: w ≥ 0, τ > 0. **E ≥ 0 is not used**, because the scalar inequality holds for all real x.
- **(b) S5b**: w ≥ 0, E ≥ 0, τ > 0. E ≥ 0 is needed.
- **(c) S5c**: w ≥ 0 only. τ is not involved, and s, t may be any reals. E ≥ 0 is not used.
- **(d) S5d / S5d_window**: w ≥ 0, τ ≥ 0, E0 any real. **The stated E0 > 0 is not used, and neither is E ≥ 0.** "Weight in [0, E0]" is formalized as Σ over {i : E i ≤ E0} of w i e^{−2τE i}.
- **(e) S5e**: w ≥ 0, E ≥ 0, τ > 0, v > 0, v ≤ C(2τ), C(τ) ≤ V.
  - No extra side condition is needed. v ≤ V, V > 0 and E0 > 0 all follow, because C(τ) ≥ C(2τ) ≥ v when E ≥ 0 (`C_two_le`, `S5e_E0_pos`).
  - E ≥ 0 is used only for this monotonicity, which makes V > 0 so that log(2V/v) is the real log.
  - "At least v/2" does follow. The proof in fact gives the slightly stronger bound C(2τ) − (v/2V)·C(τ).
- **(f) S5f**: w ≥ 0, s ≤ t, and (w i > 0 → E i = 0 ∨ m ≤ E i). P0 = Σ_{E i = 0} w i. **The stated s ≥ 0 is not used, and neither is m > 0.**
- **(g) S5g_lower**: w ≥ 0 and E j ≠ 0. It needs neither w j > 0 nor E j < m.
- **(g) S5g**: w ≥ 0, w j > 0, 0 < E j < m.
  - For every K and T, the time t = max T (log((|K|+1)/w j)/(m − E j)) + 1 satisfies T ≤ t and K·e^{−mt} < C(t) − P0.
  - So no bound C(t) − P0 ≤ K e^{−mt} holds for all large t.

## 3. Failed predicates

- The first compile of S5.lean failed with one unsolved goal in S5e, a commutativity goal `τ * log … = log … * τ` left after `field_simp`. This was a defect in **my proof script**, not in the statement. Adding `ring` fixed it, and every other theorem passed on the first compile.
- No other predicate failed, in Lean or in the numerics.

## 4. What I did not check

- **Measure version**, for a finite positive Borel measure ν on [0, ∞):
  - (a), (b), (c), (d), (e) and (f) carry over word for word. Each proof is a pointwise inequality of integrands, integrated against ν. (c) is Cauchy–Schwarz / Hölder in L²(ν). (d), (e) and (f) split ν into a set and its complement.
  - The finite-sum proof of (g) does not carry over word for word. An atom becomes "ν((0, m)) > 0": take some [a, b] ⊂ (0, m) with positive mass and use C(t) − P0 ≥ ν([a, b])·e^{−tb}.
  - Mathlib already has the pieces needed: `MeasureTheory.integral_mono`, `integral_mul_le_Lp_mul_Lq` / `inner_mul_le_norm_mul_norm` in L², `setIntegral` splitting, and `IsFiniteMeasure`.
  - The obligation not met in the finite case is integrability: t ↦ e^{−tE} is bounded and measurable on [0, ∞), and E e^{−2τE} and E² e^{−2τE} are bounded for τ > 0. These need short boundedness lemmas.
  - Not attempted.
- I did not check the "Consequence" paragraph of S5, which links to A4, or the physical reading of S6. I proved only the abstract inequalities.
- Lean proofs of mutation falsity are not done (see §1).

## 5. Delegated question and outcome

- **Delegated:** a numerical sanity program for (a), (b), (d) and (e) on 2000 random atom sets with seed 12345. Hypotheses were counted first, and a search for the extremal x in x e^{−x} and x² e^{−x} checked that the constants are sharp. The child's control question was ln 2, which it answered correctly as 0.693147.
- **Returned (child/s5num.py, child/results.txt):**
  - Qualifying cases: (a) 2000, (b) 2000, (d) 19778 pairs of atom set and E0, (e) 1972. In the other 28 cases for (e) every weight is 0, so C(2τ) = 0.
  - All of them met, with 0 failures. Max LHS/RHS: (a) 0.99983, (b) 0.99847, (d) 0.99983. For (e), (v/2)/LHS ≤ 0.533.
  - Extremal x: 1.0000000 and 2.0000000. Single-atom equality holds to 2e−16.
  - The tolerance is 1e−12 relative, derived in the docstring from the float64 unit roundoff (n+5)u ≈ 3e−15.
  - The child's PCP verify reported PASS.
- **My check:** I reread the docstring and predicates. I reran the program through my own register (K4, exit 0), and it reproduced an identical table in child/results_2.txt. These numerics only sample the claims; the Lean proofs are what establish them.

## 6. Commands to rerun

```
cd C:/Users/donke/z4-workers/r5-lean
export PYTHONUTF8=1; P=C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py
python $P check --ws pcp --name lean_S5 --expect-exit 0 -- bash run_lean.sh C:/Users/donke/z4-workers/r5-lean/S5.lean
python $P check --ws pcp --name mut_a --expect-exit 1 -- bash run_lean.sh C:/Users/donke/z4-workers/r5-lean/mut/S5_mut_a.lean
python $P check --ws pcp --name mut_b --expect-exit 1 -- bash run_lean.sh C:/Users/donke/z4-workers/r5-lean/mut/S5_mut_b.lean
cd child && python $P check --ws ../pcp --name child_s5num_rerun --expect-exit 0 -- python s5num.py && cd ..
python $P verify --ws pcp
```
run_lean.sh runs `cd C:/Users/donke/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean <file>`.

Last line of verify: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

The director and I share a model family, so this agreement is not independent review. The Lean kernel check is the independent part.
