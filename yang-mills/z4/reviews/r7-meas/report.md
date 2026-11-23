# r7-meas: S5 lifted to finite measures (formalizer report)

Control: control.txt = 0.272341 (−ln tanh 1). File: `MeasureHeat.lean` (namespace `MH`); input not modified.
Compile K1: exit 0, no `sorry` (the word appears only in the header comment), every `#print axioms` = `[propext, Classical.choice, Quot.sound]`.

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| M2 (d) tail, `MH.M2_tail` | STANDS | K1, std axioms |
| M2 (d) mass form, `MH.M2_window` | STANDS | K1, std axioms |
| M4 (f), `MH.M4_gap` | STANDS | K1, std axioms |
| M1 (a), `MH.M1a` (integrability + bound) | STANDS | K1, std axioms |
| M6 (c), `MH.M6` | STANDS | K1 (AM-GM quadratic-form proof); independently K2 (child's Hölder proof, recompiled by me) |
| M3 (e), `MH.M3` | STANDS | K1, std axioms |
| M1 (b), `MH.M1b` (integrability + bound) | STANDS | K1, std axioms |
| M5 (g), `MH.exists_Icc_pos`, `MH.M5_lower`, `MH.M5_no_bound` | STANDS | K1, std axioms |
| Mutation: (a) with e→2 | rejected by compiler, but **the statement is TRUE** | K3 exit 1; K6 P2 2000/2000. Since 2 < e the bound is weaker. The rejection shows only that the proof is brittle, not that the statement is false |
| Mutation: (a) with e→3 (added) | rejected, statement FALSE | K4 exit 1; ν = δ_{1/τ}, τ=1: 0.1353 > 0.1226 (K6 P3) |
| Mutation: (b) without support | rejected, statement FALSE | K5 exit 1 (`unknown identifier hsupp`). Counterexample ν = δ_{−1}, τ=1: e² = 7.389 > 4/e = 1.472 (K6 P4). For ν with density e^{x} on (−∞,0], τ=1, the Integrable conjunct fails, but the inequality holds vacuously because the Bochner integral is a junk 0 |

Counts (met, failed, measured only): Lean predicates Q1–Q4: 4, 0, 0, counted on the final file. The failed intermediate compiles are listed in §3. mutcheck.py: 5, 0, 0. Child: 1, 0, 0 after my recompile.

### Exact signatures
Common: `variable (ν : Measure ℝ) [IsFiniteMeasure ν]`, `C ν t := ∫ E, exp (-t * E) ∂ν`, `P0 ν := (ν {0}).toReal`.
```lean
theorem M2_tail (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 ≤ τ) (E0 : ℝ) :
    ∫ E in Ioi E0, exp (-(2 * τ) * E) ∂ν ≤ exp (-τ * E0) * C ν τ
theorem M2_window (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 ≤ τ) (E0 : ℝ) :
    C ν (2 * τ) - exp (-τ * E0) * C ν τ ≤ ∫ E in Iic E0, exp (-(2 * τ) * E) ∂ν
theorem M4_gap (hsupp : ν (Iio 0) = 0) (m : ℝ) (hgap : ν (Ioo 0 m) = 0)
    (s t : ℝ) (hs : 0 ≤ s) (hst : s ≤ t) :
    C ν t - P0 ν ≤ exp (-m * (t - s)) * (C ν s - P0 ν)
theorem M1a (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 < τ) :
    Integrable (fun E => E * exp (-(2 * τ) * E)) ν ∧
    ∫ E, E * exp (-(2 * τ) * E) ∂ν ≤ C ν τ / (exp 1 * τ)
theorem M6 (hsupp : ν (Iio 0) = 0) (s t : ℝ) (hs : 0 ≤ s) (ht : 0 ≤ t) :
    C ν ((s + t) / 2) ^ 2 ≤ C ν s * C ν t
theorem M3 (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 < τ) (v V : ℝ) (hv : 0 < v)
    (h2 : v ≤ C ν (2 * τ)) (hV : C ν τ ≤ V) :
    v / 2 ≤ ∫ E in Iic ((1 / τ) * log (2 * V / v)), exp (-(2 * τ) * E) ∂ν
theorem M1b (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 < τ) :
    Integrable (fun E => E ^ 2 * exp (-(2 * τ) * E)) ν ∧
    ∫ E, E ^ 2 * exp (-(2 * τ) * E) ∂ν ≤ 4 * C ν τ / (exp 1 ^ 2 * τ ^ 2)
lemma exists_Icc_pos {m : ℝ} (h : 0 < ν (Ioo 0 m)) :
    ∃ a b : ℝ, 0 < a ∧ a ≤ b ∧ b < m ∧ 0 < ν (Icc a b)
theorem M5_lower (hsupp : ν (Iio 0) = 0) {a b : ℝ} (ha : 0 < a) (t : ℝ) (ht : 0 ≤ t) :
    (ν (Icc a b)).toReal * exp (-t * b) ≤ C ν t - P0 ν
theorem M5_no_bound (hsupp : ν (Iio 0) = 0) (m : ℝ) (hpos : 0 < ν (Ioo 0 m)) (K T : ℝ) :
    ∃ t, T ≤ t ∧ K * exp (-m * t) < C ν t - P0 ν
```
`#print axioms` output (K1, `measureheat_compile.log`). Each of integrable_exp, M2_tail, M2_window, M4_gap, M1a, M6, M3, M1b, exists_Icc_pos, M5_lower and M5_no_bound gives `depends on axioms: [propext, Classical.choice, Quot.sound]`. Child (K2): `'M6_child' depends on axioms: [propext, Classical.choice, Quot.sound]`.

## 2. Hypotheses each statement uses
- Support `hsupp : ν (Iio 0) = 0` is turned into `∀ᵐ E, 0 ≤ E` (lemma `ae_nonneg`). In M2, M3, M4, M5, M6 and M1a it is used **only for integrability**, through `integrable_exp`: e^{−tE} ≤ 1 a.e. for t ≥ 0. M1b also uses it **pointwise**: x²e^{−x} ≤ 4e^{−2} needs x ≥ 0. M4 also uses it pointwise to split E = 0 from E ≥ m.
- τ ≥ 0 suffices in M2 (stated so). M1a, M1b and M3 need τ > 0 (division by τ).
- M4: m > 0 is not assumed and not needed. s ≥ 0 is needed for integrability of C(s).
- M5: K and T are arbitrary, m is arbitrary. If m ≤ 0 the hypothesis ν(0,m) > 0 is impossible.
- M6: s, t ≥ 0 are needed. Without integrability, Lean's C(s) is a junk 0 and the inequality can fail.
- M3: v ≤ V, V > 0 and E0 > 0 are not assumed. V > 0 is derived inside the proof.
- E0 in M2 is an arbitrary real. The draft's "E0 > 0" is unnecessary.
- Unused hypotheses: none stated in the final signatures. Lean reports only "unused section variable [IsFiniteMeasure ν]" for `ae_nonneg`, `C_nonneg` and `exists_Icc_pos`. Finiteness is not needed there.

**Lemmas that carry integrability:** `Integrable.mono'` with `integrable_const 1` (bounded by 1 on a finite measure) and `Continuous.aestronglyMeasurable` (via `fun_prop`). `Integrable.const_mul`, `Integrable.indicator`, `Integrable.sub` and `Integrable.add` combine the pieces. For M1a and M1b, the dominating function is the constant times e^{−τE}. Other main lemmas: `setIntegral_mono_on`, `setIntegral_le_integral`, `integral_add_compl` with `compl_Iic`, `integral_mono_ae`, `integral_indicator_const`, `measure_zero_iff_ae_nmem`, `measure_iUnion_null`, `measure_mono_null`, `exists_nat_one_div_lt`, `ENNReal.toReal_pos`. The child used `integral_mul_le_Lp_mul_Lq_of_nonneg` with `Real.HolderConjugate.two_two` and `MemLp.of_bound`.

## 3. Failed predicates
- Intermediate compiles. All failures were my own slips, not defects of the target. Compile 1: `M2_window` (C left folded in the linarith hypothesis) and `C_sub_P0` (this Mathlib phrases `integral_indicator_const` with `ν.real`). Compile 2: `M6` (`integral_add` against the `Pi.add` form) and `M3` (`field_simp` left a `ring` goal). All four were fixed. The final file has no failures and no `*_failed.lean` was needed.
- Mutation e→2: I expected it to be "rejected because false". It was rejected, but the statement is true (K6 P2). The mutation is a bad test, not a defect of the target. e→3 was added as the meaningful mutation.
- Mutation (b) without support: rejected for a syntactic reason (`unknown identifier hsupp`). It is false mathematically (δ_{−1}).

## 4. Not checked
- Sharpness of the constants in the measure form. This follows from the atom case and was not re-proved.
- Measures that are not finite, or σ-finite ν with C(t) < ∞. These are not covered (IsFiniteMeasure is assumed).
- C(t) for t < 0, and continuity or differentiability of C (the moments as −C′, C″ are not linked to C in Lean).
- Equivalence of `hsupp` with "support ⊆ [0,∞)" for the closed support. Only the null-set form is used.
- The inner-regularity route for M5. The countable union of intervals was used instead.

## 5. Delegated question (rule 7)
Question to child/: prove M6 in the form `(∫ exp(−((s+t)/2)E))² ≤ (∫ exp(−sE))(∫ exp(−tE))` for finite ν with ν(Iio 0) = 0 and s, t ≥ 0, via Mathlib's Hölder/Cauchy–Schwarz, proving all MemLp conditions. Control: ∫₀¹x² = 0.333333.
What came back: child/control.txt = 0.333333 (correct) and child/M6child.lean, proved by `integral_mul_le_Lp_mul_Lq_of_nonneg` (p = q = 2). The child claimed exit 0, std axioms and register verify PASS. I reread the file (no sorry, same statement as my M6 unfolded) and recompiled it (K2, exit 0, std axioms). My own M6 uses a different route (2ab·C(u) ≤ a²C(s) + b²C(t)), so M6 has two proofs. Both came from the same model family.

## 6. Commands to rerun
```
cd C:/Users/donke/z4-lean
PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r7-meas/MeasureHeat.lean
PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r7-meas/child/M6child.lean
PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r7-meas/mutants/mutA_e_to_2.lean   # expect exit 1
PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r7-meas/mutants/mutA_e_to_3.lean   # expect exit 1
PATH=$HOME/.elan/bin:$PATH lake env lean C:/Users/donke/z4-workers/r7-meas/mutants/mutB_nosupp.lean   # expect exit 1
cd C:/Users/donke/z4-workers/r7-meas && python mutcheck.py   # refuses if mutcheck_result.txt exists
PYTHONUTF8=1 python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
Register checks: K1 MeasureHeat (exit 0), K2 child recompile (0), K3–K5 mutants (1, 1, 1), K6 mutcheck (0).
Verify, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Director, worker and child are one model family; this is not independent review.
