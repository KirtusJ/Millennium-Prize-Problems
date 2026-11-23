/-
S5 lifted to finite positive Borel measures on ℝ (M1–M6).
Predicates fixed before the first compile:
  Q1 file compiles with `lake env lean` (exit 0) and contains no `sorry`;
  Q2 `#print axioms` of every main theorem shows only propext, Classical.choice, Quot.sound;
  Q3 integrability of every integrand is proved inside the file, never assumed;
  Q4 mutations (in scratch copies, not this file): (b) without the support hypothesis,
     (a) with `exp 1` replaced by `2`, must FAIL to compile.
Setting: ν finite measure, support hypothesis `hsupp : ν (Set.Iio 0) = 0`,
C ν t = ∫ exp(-t E) dν.  The input file input/HeatRegularized.lean is not modified.
-/
import Mathlib

open MeasureTheory Real Set

namespace MH

variable (ν : Measure ℝ) [IsFiniteMeasure ν]

/-- C(t) = ∫ exp(-t E) dν(E). -/
noncomputable def C (t : ℝ) : ℝ := ∫ E, exp (-t * E) ∂ν

variable {ν}

lemma ae_nonneg (hsupp : ν (Iio 0) = 0) : ∀ᵐ E ∂ν, 0 ≤ E := by
  filter_upwards [measure_zero_iff_ae_nmem.mp hsupp] with E hE
  simpa using hE

/-- x e^{-x} ≤ e^{-1} for all real x. -/
lemma mul_exp_neg_le (x : ℝ) : x * exp (-x) ≤ exp (-1) := by
  have h := add_one_le_exp (x - 1)
  have h' : x ≤ exp (x - 1) := by linarith
  calc x * exp (-x) ≤ exp (x - 1) * exp (-x) :=
        mul_le_mul_of_nonneg_right h' (exp_pos _).le
    _ = exp (-1) := by rw [← exp_add]; ring_nf

/-- x² e^{-x} ≤ 4 e^{-2} for x ≥ 0. -/
lemma sq_mul_exp_neg_le (x : ℝ) (hx : 0 ≤ x) : x ^ 2 * exp (-x) ≤ 4 * exp (-2) := by
  have h := add_one_le_exp (x / 2 - 1)
  have h' : x / 2 ≤ exp (x / 2 - 1) := by linarith
  have h2 : (x / 2) * (x / 2) ≤ exp (x / 2 - 1) * exp (x / 2 - 1) :=
    mul_self_le_mul_self (by linarith) h'
  have h3 : exp (x / 2 - 1) * exp (x / 2 - 1) = exp (x - 2) := by
    rw [← exp_add]; ring_nf
  calc x ^ 2 * exp (-x) = 4 * ((x / 2) * (x / 2)) * exp (-x) := by ring
    _ ≤ 4 * exp (x - 2) * exp (-x) := by
        apply mul_le_mul_of_nonneg_right _ (exp_pos _).le; rw [← h3]; linarith
    _ = 4 * exp (-2) := by rw [mul_assoc, ← exp_add]; ring_nf

lemma exp_two (τ x : ℝ) : exp (-(2 * τ) * x) = exp (-τ * x) * exp (-τ * x) := by
  rw [← exp_add]; ring_nf

/-- Integrability of the heat kernel for t ≥ 0 (bounded by 1 on the support). -/
lemma integrable_exp (hsupp : ν (Iio 0) = 0) {t : ℝ} (ht : 0 ≤ t) :
    Integrable (fun E => exp (-t * E)) ν := by
  refine Integrable.mono' (integrable_const (1 : ℝ)) ?_ ?_
  · exact (by fun_prop : Continuous fun E : ℝ => exp (-t * E)).aestronglyMeasurable
  · filter_upwards [ae_nonneg hsupp] with E hE
    rw [Real.norm_eq_abs, abs_of_pos (exp_pos _)]
    apply exp_le_one_iff.mpr
    nlinarith

lemma C_nonneg (t : ℝ) : 0 ≤ C ν t :=
  integral_nonneg (fun E => (exp_pos _).le)

/-! ### M2 (d) -/

/-- (d) tail bound. Uses τ ≥ 0 and the support hypothesis (for integrability only). -/
theorem M2_tail (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 ≤ τ) (E0 : ℝ) :
    ∫ E in Ioi E0, exp (-(2 * τ) * E) ∂ν ≤ exp (-τ * E0) * C ν τ := by
  have hI2 := integrable_exp hsupp (t := 2 * τ) (by linarith)
  have hI1 := (integrable_exp hsupp hτ).const_mul (exp (-τ * E0))
  calc ∫ E in Ioi E0, exp (-(2 * τ) * E) ∂ν
      ≤ ∫ E in Ioi E0, exp (-τ * E0) * exp (-τ * E) ∂ν := by
        apply setIntegral_mono_on hI2.integrableOn hI1.integrableOn measurableSet_Ioi
        intro E hE
        have hE' : E0 < E := hE
        rw [exp_two]
        apply mul_le_mul_of_nonneg_right _ (exp_pos _).le
        apply exp_le_exp.mpr; nlinarith
    _ ≤ ∫ E, exp (-τ * E0) * exp (-τ * E) ∂ν :=
        setIntegral_le_integral hI1 (Filter.Eventually.of_forall
          (fun E => (mul_pos (exp_pos _) (exp_pos _)).le))
    _ = exp (-τ * E0) * C ν τ := by rw [integral_const_mul]; rfl

/-- (d) mass form: regularized weight of {E ≤ E0}. -/
theorem M2_window (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 ≤ τ) (E0 : ℝ) :
    C ν (2 * τ) - exp (-τ * E0) * C ν τ ≤ ∫ E in Iic E0, exp (-(2 * τ) * E) ∂ν := by
  have hI2 := integrable_exp hsupp (t := 2 * τ) (by linarith)
  have hsplit := integral_add_compl (μ := ν) (measurableSet_Iic (a := E0)) hI2
  rw [compl_Iic] at hsplit
  have ht := M2_tail hsupp τ hτ E0
  simp only [C] at ht ⊢
  linarith

/-! ### M4 (f) -/

/-- P0 = ν{0}. -/
noncomputable def P0 (ν : Measure ℝ) : ℝ := (ν {0}).toReal

lemma C_sub_P0 (hsupp : ν (Iio 0) = 0) {t : ℝ} (ht : 0 ≤ t) :
    C ν t - P0 ν = ∫ E, (exp (-t * E) - ({0} : Set ℝ).indicator (fun _ => (1 : ℝ)) E) ∂ν := by
  rw [integral_sub (integrable_exp hsupp ht)
    ((integrable_const (1 : ℝ)).indicator (measurableSet_singleton 0)),
    integral_indicator_const _ (measurableSet_singleton 0)]
  simp [C, P0, measureReal_def]

lemma integrable_sub_ind (hsupp : ν (Iio 0) = 0) {t : ℝ} (ht : 0 ≤ t) :
    Integrable (fun E => exp (-t * E) - ({0} : Set ℝ).indicator (fun _ => (1 : ℝ)) E) ν :=
  (integrable_exp hsupp ht).sub ((integrable_const (1 : ℝ)).indicator (measurableSet_singleton 0))

/-- (f) gap direction. Uses the support hypothesis, ν(0,m) = 0, 0 ≤ s ≤ t.
    m > 0 is not needed. -/
theorem M4_gap (hsupp : ν (Iio 0) = 0) (m : ℝ) (hgap : ν (Ioo 0 m) = 0)
    (s t : ℝ) (hs : 0 ≤ s) (hst : s ≤ t) :
    C ν t - P0 ν ≤ exp (-m * (t - s)) * (C ν s - P0 ν) := by
  have ht : 0 ≤ t := le_trans hs hst
  rw [C_sub_P0 hsupp ht, C_sub_P0 hsupp hs, ← integral_const_mul]
  apply integral_mono_ae (integrable_sub_ind hsupp ht)
    ((integrable_sub_ind hsupp hs).const_mul _)
  filter_upwards [ae_nonneg hsupp, measure_zero_iff_ae_nmem.mp hgap] with E hE hEm
  by_cases h0 : E = 0
  · subst h0; simp
  · have hpos : 0 < E := lt_of_le_of_ne hE (Ne.symm h0)
    have hmE : m ≤ E := by
      by_contra hc; exact hEm ⟨hpos, lt_of_not_le hc⟩
    simp only [indicator_of_not_mem (show E ∉ ({0} : Set ℝ) from h0), sub_zero]
    rw [← exp_add]; apply exp_le_exp.mpr; nlinarith

/-! ### M1 (a) -/

/-- (a) Integrability and bound. Uses τ > 0 and the support hypothesis (integrability). -/
theorem M1a (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 < τ) :
    Integrable (fun E => E * exp (-(2 * τ) * E)) ν ∧
    ∫ E, E * exp (-(2 * τ) * E) ∂ν ≤ C ν τ / (exp 1 * τ) := by
  have key : ∀ E : ℝ, E * exp (-τ * E) ≤ 1 / (exp 1 * τ) := by
    intro E
    rw [le_div_iff₀ (by positivity)]
    have h := mul_exp_neg_le (τ * E)
    have he : exp (-1) * exp 1 = 1 := by rw [← exp_add]; simp
    calc E * exp (-τ * E) * (exp 1 * τ)
        = (τ * E * exp (-(τ * E))) * exp 1 := by rw [neg_mul]; ring
      _ ≤ exp (-1) * exp 1 := mul_le_mul_of_nonneg_right h (exp_pos _).le
      _ = 1 := he
  have hpt : ∀ E : ℝ, E * exp (-(2 * τ) * E) ≤ 1 / (exp 1 * τ) * exp (-τ * E) := by
    intro E; rw [exp_two, ← mul_assoc]
    exact mul_le_mul_of_nonneg_right (key E) (exp_pos _).le
  have hg := (integrable_exp hsupp hτ.le).const_mul (1 / (exp 1 * τ))
  have hint : Integrable (fun E => E * exp (-(2 * τ) * E)) ν := by
    refine Integrable.mono' hg
      ((by fun_prop : Continuous fun E : ℝ => E * exp (-(2 * τ) * E)).aestronglyMeasurable) ?_
    filter_upwards [ae_nonneg hsupp] with E hE
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg hE (exp_pos _).le)]
    exact hpt E
  refine ⟨hint, ?_⟩
  calc ∫ E, E * exp (-(2 * τ) * E) ∂ν
      ≤ ∫ E, 1 / (exp 1 * τ) * exp (-τ * E) ∂ν :=
        integral_mono_ae hint hg (Filter.Eventually.of_forall hpt)
    _ = C ν τ / (exp 1 * τ) := by rw [integral_const_mul]; unfold C; ring

/-! ### M6 (c) -/

/-- (c) log-convexity, by the quadratic form 2ab C(u) ≤ a² C(s) + b² C(t). Uses s, t ≥ 0
    and the support hypothesis (integrability; without it C(s) may be a junk 0). -/
theorem M6 (hsupp : ν (Iio 0) = 0) (s t : ℝ) (hs : 0 ≤ s) (ht : 0 ≤ t) :
    C ν ((s + t) / 2) ^ 2 ≤ C ν s * C ν t := by
  have Is := integrable_exp hsupp hs
  have It := integrable_exp hsupp ht
  have Iu := integrable_exp hsupp (t := (s + t) / 2) (by linarith)
  have hp : ∀ a b E : ℝ, 2 * a * b * exp (-((s + t) / 2) * E)
      ≤ a ^ 2 * exp (-s * E) + b ^ 2 * exp (-t * E) := by
    intro a b E
    have hx : exp (-s * E) = exp (-s * E / 2) * exp (-s * E / 2) := by
      rw [← exp_add]; ring_nf
    have hy : exp (-t * E) = exp (-t * E / 2) * exp (-t * E / 2) := by
      rw [← exp_add]; ring_nf
    have hxy : exp (-((s + t) / 2) * E) = exp (-s * E / 2) * exp (-t * E / 2) := by
      rw [← exp_add]; ring_nf
    rw [hx, hy, hxy]
    nlinarith [sq_nonneg (a * exp (-s * E / 2) - b * exp (-t * E / 2))]
  have Q : ∀ a b : ℝ, 2 * a * b * C ν ((s + t) / 2) ≤ a ^ 2 * C ν s + b ^ 2 * C ν t := by
    intro a b
    have h := integral_mono_ae (Iu.const_mul (2 * a * b)) ((Is.const_mul (a ^ 2)).add
      (It.const_mul (b ^ 2))) (Filter.Eventually.of_forall (hp a b))
    simp only [Pi.add_apply] at h
    rw [integral_const_mul, integral_add (Is.const_mul _) (It.const_mul _),
      integral_const_mul, integral_const_mul] at h
    simpa [C] using h
  have hX := C_nonneg (ν := ν) s
  have hY := C_nonneg (ν := ν) t
  have hZ := C_nonneg (ν := ν) ((s + t) / 2)
  rcases hY.lt_or_eq with hY' | hY'
  · have h1 := Q (C ν t) (C ν ((s + t) / 2))
    nlinarith
  · rcases hX.lt_or_eq with hX' | hX'
    · have h1 := Q (C ν ((s + t) / 2)) (C ν s)
      rw [← hY'] at h1 ⊢
      nlinarith
    · have h1 := Q 1 1
      rw [← hY', ← hX'] at h1 ⊢
      nlinarith

/-! ### M3 (e) -/

lemma C_two_le (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 ≤ τ) : C ν (2 * τ) ≤ C ν τ := by
  apply integral_mono_ae (integrable_exp hsupp (t := 2 * τ) (by linarith))
    (integrable_exp hsupp hτ)
  filter_upwards [ae_nonneg hsupp] with E hE
  exact exp_le_exp.mpr (by nlinarith)

/-- (e). Uses support, τ > 0, v > 0, v ≤ C(2τ), C(τ) ≤ V. -/
theorem M3 (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 < τ) (v V : ℝ) (hv : 0 < v)
    (h2 : v ≤ C ν (2 * τ)) (hV : C ν τ ≤ V) :
    v / 2 ≤ ∫ E in Iic ((1 / τ) * log (2 * V / v)), exp (-(2 * τ) * E) ∂ν := by
  have hCC := C_two_le hsupp τ hτ.le
  have hVpos : 0 < V := by linarith
  have hwin := M2_window hsupp τ hτ.le ((1 / τ) * log (2 * V / v))
  have hexp : exp (-τ * ((1 / τ) * log (2 * V / v))) = v / (2 * V) := by
    have : -τ * ((1 / τ) * log (2 * V / v)) = -log (2 * V / v) := by
      field_simp; ring
    rw [this, exp_neg, exp_log (by positivity)]
    field_simp
  rw [hexp] at hwin
  have hq : v / (2 * V) * C ν τ ≤ v / (2 * V) * V :=
    mul_le_mul_of_nonneg_left hV (by positivity)
  have hq' : v / (2 * V) * V = v / 2 := by field_simp; ring
  linarith

/-! ### M1 (b) -/

/-- (b) Integrability and bound. Uses τ > 0 and the support hypothesis (pointwise AND
    integrability: x² e^{-x} ≤ 4e^{-2} needs x ≥ 0). -/
theorem M1b (hsupp : ν (Iio 0) = 0) (τ : ℝ) (hτ : 0 < τ) :
    Integrable (fun E => E ^ 2 * exp (-(2 * τ) * E)) ν ∧
    ∫ E, E ^ 2 * exp (-(2 * τ) * E) ∂ν ≤ 4 * C ν τ / (exp 1 ^ 2 * τ ^ 2) := by
  have key : ∀ E : ℝ, 0 ≤ E → E ^ 2 * exp (-τ * E) ≤ 4 / (exp 1 ^ 2 * τ ^ 2) := by
    intro E hE
    rw [le_div_iff₀ (by positivity)]
    have h := sq_mul_exp_neg_le (τ * E) (mul_nonneg hτ.le hE)
    have he : exp (-2) * exp 1 ^ 2 = 1 := by
      rw [sq, ← exp_add, ← exp_add]; norm_num
    calc E ^ 2 * exp (-τ * E) * (exp 1 ^ 2 * τ ^ 2)
        = ((τ * E) ^ 2 * exp (-(τ * E))) * exp 1 ^ 2 := by rw [neg_mul]; ring
      _ ≤ (4 * exp (-2)) * exp 1 ^ 2 := mul_le_mul_of_nonneg_right h (by positivity)
      _ = 4 := by rw [mul_assoc, he, mul_one]
  have hpt : ∀ᵐ E ∂ν, E ^ 2 * exp (-(2 * τ) * E) ≤ 4 / (exp 1 ^ 2 * τ ^ 2) * exp (-τ * E) := by
    filter_upwards [ae_nonneg hsupp] with E hE
    rw [exp_two, ← mul_assoc]
    exact mul_le_mul_of_nonneg_right (key E hE) (exp_pos _).le
  have hg := (integrable_exp hsupp hτ.le).const_mul (4 / (exp 1 ^ 2 * τ ^ 2))
  have hint : Integrable (fun E => E ^ 2 * exp (-(2 * τ) * E)) ν := by
    refine Integrable.mono' hg
      ((by fun_prop : Continuous fun E : ℝ => E ^ 2 * exp (-(2 * τ) * E)).aestronglyMeasurable) ?_
    filter_upwards [hpt] with E hE
    rw [Real.norm_eq_abs, abs_of_nonneg (mul_nonneg (sq_nonneg _) (exp_pos _).le)]
    exact hE
  refine ⟨hint, ?_⟩
  calc ∫ E, E ^ 2 * exp (-(2 * τ) * E) ∂ν
      ≤ ∫ E, 4 / (exp 1 ^ 2 * τ ^ 2) * exp (-τ * E) ∂ν := integral_mono_ae hint hg hpt
    _ = 4 * C ν τ / (exp 1 ^ 2 * τ ^ 2) := by rw [integral_const_mul]; unfold C; ring

/-! ### M5 (g), measure form -/

/-- A compact interval [a,b] ⊂ (0,m) of positive mass, via the countable cover
    (0,m) ⊆ ⋃ₙ [1/(n+1), m - 1/(n+1)] and countable subadditivity. -/
lemma exists_Icc_pos {m : ℝ} (h : 0 < ν (Ioo 0 m)) :
    ∃ a b : ℝ, 0 < a ∧ a ≤ b ∧ b < m ∧ 0 < ν (Icc a b) := by
  by_contra hcon
  push_neg at hcon
  have hsub : Ioo 0 m ⊆ ⋃ n : ℕ, Icc (1 / ((n : ℝ) + 1)) (m - 1 / ((n : ℝ) + 1)) := by
    intro x hx
    obtain ⟨n, hn⟩ := exists_nat_one_div_lt (lt_min hx.1 (sub_pos.mpr hx.2))
    refine mem_iUnion.mpr ⟨n, ?_, ?_⟩
    · exact (hn.trans_le (min_le_left _ _)).le
    · have := hn.trans_le (min_le_right _ _); linarith
  have hnull : ν (⋃ n : ℕ, Icc (1 / ((n : ℝ) + 1)) (m - 1 / ((n : ℝ) + 1))) = 0 := by
    apply measure_iUnion_null
    intro n
    have hpos : (0 : ℝ) < 1 / ((n : ℝ) + 1) := by positivity
    by_cases hab : 1 / ((n : ℝ) + 1) ≤ m - 1 / ((n : ℝ) + 1)
    · exact le_antisymm (hcon _ _ hpos hab (by linarith)) (zero_le _)
    · rw [Icc_eq_empty hab]; exact measure_empty
  have h0 := measure_mono_null hsub hnull
  rw [h0] at h
  exact lt_irrefl _ h

/-- Explicit lower bound: C(t) - P0 ≥ ν[a,b] e^{-tb} for 0 < a, t ≥ 0. -/
theorem M5_lower (hsupp : ν (Iio 0) = 0) {a b : ℝ} (ha : 0 < a) (t : ℝ) (ht : 0 ≤ t) :
    (ν (Icc a b)).toReal * exp (-t * b) ≤ C ν t - P0 ν := by
  rw [C_sub_P0 hsupp ht]
  have hI : (ν (Icc a b)).toReal * exp (-t * b)
      = ∫ E, (Icc a b).indicator (fun _ => exp (-t * b)) E ∂ν := by
    rw [integral_indicator_const _ measurableSet_Icc]
    simp [measureReal_def]
  rw [hI]
  refine integral_mono_ae ((integrable_const _).indicator measurableSet_Icc)
    (integrable_sub_ind hsupp ht) ?_
  filter_upwards with E
  by_cases hE : E ∈ Icc a b
  · have hE0 : E ≠ 0 := by
      have := hE.1; intro h; rw [h] at this; linarith
    rw [indicator_of_mem hE, indicator_of_not_mem (show E ∉ ({0} : Set ℝ) from hE0), sub_zero]
    exact exp_le_exp.mpr (by nlinarith [hE.2])
  · rw [indicator_of_not_mem hE]
    by_cases h0 : E = 0
    · subst h0; simp
    · rw [indicator_of_not_mem (show E ∉ ({0} : Set ℝ) from h0), sub_zero]
      exact (exp_pos _).le

/-- (g) measure form: if ν(0,m) > 0 no bound C(t) - P0 ≤ K e^{-mt} holds for all t ≥ T. -/
theorem M5_no_bound (hsupp : ν (Iio 0) = 0) (m : ℝ) (hpos : 0 < ν (Ioo 0 m)) (K T : ℝ) :
    ∃ t, T ≤ t ∧ K * exp (-m * t) < C ν t - P0 ν := by
  obtain ⟨a, b, ha, hab, hbm, hmass⟩ := exists_Icc_pos hpos
  have hwpos : 0 < (ν (Icc a b)).toReal :=
    ENNReal.toReal_pos hmass.ne' (measure_ne_top _ _)
  obtain ⟨w, hw⟩ : ∃ w, w = (ν (Icc a b)).toReal := ⟨_, rfl⟩
  rw [← hw] at hwpos
  obtain ⟨t, htd⟩ : ∃ t, t = max (max T 0) (log ((|K| + 1) / w) / (m - b)) + 1 := ⟨_, rfl⟩
  have hd : 0 < m - b := by linarith
  have hmax1 := le_max_left (max T 0) (log ((|K| + 1) / w) / (m - b))
  have hmax2 := le_max_right (max T 0) (log ((|K| + 1) / w) / (m - b))
  have hT := le_max_left T 0
  have h0 := le_max_right T 0
  have ht0 : 0 ≤ t := by rw [htd]; linarith
  refine ⟨t, by rw [htd]; linarith, ?_⟩
  have ht1 : log ((|K| + 1) / w) / (m - b) < t := by rw [htd]; linarith
  have hL : log ((|K| + 1) / w) < (m - b) * t := by
    rw [div_lt_iff₀ hd] at ht1; linarith
  have hp : 0 < (|K| + 1) / w := by positivity
  have hX : (|K| + 1) / w < exp ((m - b) * t) := by
    rw [← exp_log hp]; exact exp_lt_exp.mpr hL
  have hX2 : (|K| + 1) < w * exp ((m - b) * t) := by
    rw [div_lt_iff₀ hwpos] at hX; linarith
  have hsplit : exp ((m - b) * t) * exp (-m * t) = exp (-t * b) := by
    rw [← exp_add]; ring_nf
  have hem : 0 < exp (-m * t) := exp_pos _
  have h3 : (|K| + 1) * exp (-m * t) < w * exp (-t * b) := by
    rw [← hsplit]; nlinarith
  have hK : K * exp (-m * t) ≤ (|K| + 1) * exp (-m * t) :=
    mul_le_mul_of_nonneg_right (by linarith [le_abs_self K]) hem.le
  have hlow := M5_lower hsupp (b := b) ha t ht0
  rw [← hw] at hlow
  linarith

end MH

#print axioms MH.integrable_exp
#print axioms MH.M2_tail
#print axioms MH.M2_window
#print axioms MH.M4_gap
#print axioms MH.M1a
#print axioms MH.M6
#print axioms MH.M3
#print axioms MH.M1b
#print axioms MH.exists_Icc_pos
#print axioms MH.M5_lower
#print axioms MH.M5_no_bound
