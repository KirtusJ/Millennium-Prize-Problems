/-
R9Bounds.lean -- r9-proof (builder).  Scalar and finite-sum steps of the two-sided bound.
Predicates fixed before first compile:
  L1 file compiles with exit 0, no `sorry` in the source;
  L2 `#print axioms` of jordan_khat, keep_terms, keep_terms_card, factor_upper, window_from_two_sided
     shows only propext, Classical.choice, Quot.sound.
Section S5 is copied verbatim from input/HeatRegularized.lean (lines 13-177: namespace S5 through S5e),
so that this file is self-contained (input/ is not a lake module).
-/
import Mathlib

open Real Finset

namespace S5

/-- x e^{-x} ≤ e^{-1} for ALL real x. -/
lemma mul_exp_neg_le (x : ℝ) : x * exp (-x) ≤ exp (-1) := by
  have h := add_one_le_exp (x - 1)
  have h' : x ≤ exp (x - 1) := by linarith
  calc x * exp (-x) ≤ exp (x - 1) * exp (-x) :=
        mul_le_mul_of_nonneg_right h' (exp_pos _).le
    _ = exp (-1) := by rw [← exp_add]; ring_nf

/-- x² e^{-x} ≤ 4 e^{-2} for real x ≥ 0. -/
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

/-- The hypothesis x ≥ 0 cannot be dropped in the second scalar inequality (x = -1). -/
lemma sq_mul_exp_neg_fails_neg : ¬ ((-1 : ℝ) ^ 2 * exp (-(-1)) ≤ 4 * exp (-2)) := by
  intro h
  have e1 : (1 : ℝ) + 1 < exp 1 := add_one_lt_exp one_ne_zero
  have e2 : (2 : ℝ) + 1 < exp 2 := add_one_lt_exp two_ne_zero
  have e3 : exp (-2) * exp 2 = 1 := by rw [← exp_add]; simp
  have hp : 0 < exp (-2) := exp_pos _
  norm_num at h
  nlinarith

variable {ι : Type*} [Fintype ι] (w E : ι → ℝ)

/-- C(t) = Σ w_i e^{-t E_i}. -/
noncomputable def C (t : ℝ) : ℝ := ∑ i, w i * exp (-t * E i)

lemma exp_two (τ x : ℝ) : exp (-(2 * τ) * x) = exp (-τ * x) * exp (-τ * x) := by
  rw [← exp_add]; ring_nf

/-- (a). Uses w ≥ 0 and τ > 0; does NOT use E ≥ 0. -/
theorem S5a (hw : ∀ i, 0 ≤ w i) (τ : ℝ) (hτ : 0 < τ) :
    ∑ i, w i * E i * exp (-(2 * τ) * E i) ≤ C w E τ / (exp 1 * τ) := by
  unfold C
  rw [Finset.sum_div]
  apply Finset.sum_le_sum
  intro i _
  have key : E i * exp (-τ * E i) ≤ 1 / (exp 1 * τ) := by
    rw [le_div_iff₀ (by positivity)]
    have h := mul_exp_neg_le (τ * E i)
    have he : exp (-1) * exp 1 = 1 := by rw [← exp_add]; simp
    calc E i * exp (-τ * E i) * (exp 1 * τ)
        = (τ * E i * exp (-(τ * E i))) * exp 1 := by rw [neg_mul]; ring
      _ ≤ exp (-1) * exp 1 := mul_le_mul_of_nonneg_right h (exp_pos _).le
      _ = 1 := he
  rw [exp_two]
  calc w i * E i * (exp (-τ * E i) * exp (-τ * E i))
      = (w i * exp (-τ * E i)) * (E i * exp (-τ * E i)) := by ring
    _ ≤ (w i * exp (-τ * E i)) * (1 / (exp 1 * τ)) :=
        mul_le_mul_of_nonneg_left key (mul_nonneg (hw i) (exp_pos _).le)
    _ = w i * exp (-τ * E i) / (exp 1 * τ) := by ring

/-- (b). Uses w ≥ 0, E ≥ 0, τ > 0. -/
theorem S5b (hw : ∀ i, 0 ≤ w i) (hE : ∀ i, 0 ≤ E i) (τ : ℝ) (hτ : 0 < τ) :
    ∑ i, w i * E i ^ 2 * exp (-(2 * τ) * E i) ≤ 4 * C w E τ / (exp 1 ^ 2 * τ ^ 2) := by
  unfold C
  rw [Finset.mul_sum, Finset.sum_div]
  apply Finset.sum_le_sum
  intro i _
  have key : E i ^ 2 * exp (-τ * E i) ≤ 4 / (exp 1 ^ 2 * τ ^ 2) := by
    rw [le_div_iff₀ (by positivity)]
    have h := sq_mul_exp_neg_le (τ * E i) (mul_nonneg hτ.le (hE i))
    have he : exp (-2) * exp 1 ^ 2 = 1 := by
      rw [sq, ← exp_add, ← exp_add]; norm_num
    calc E i ^ 2 * exp (-τ * E i) * (exp 1 ^ 2 * τ ^ 2)
        = ((τ * E i) ^ 2 * exp (-(τ * E i))) * exp 1 ^ 2 := by rw [neg_mul]; ring
      _ ≤ (4 * exp (-2)) * exp 1 ^ 2 := mul_le_mul_of_nonneg_right h (by positivity)
      _ = 4 := by rw [mul_assoc, he, mul_one]
  rw [exp_two]
  calc w i * E i ^ 2 * (exp (-τ * E i) * exp (-τ * E i))
      = (w i * exp (-τ * E i)) * (E i ^ 2 * exp (-τ * E i)) := by ring
    _ ≤ (w i * exp (-τ * E i)) * (4 / (exp 1 ^ 2 * τ ^ 2)) :=
        mul_le_mul_of_nonneg_left key (mul_nonneg (hw i) (exp_pos _).le)
    _ = 4 * (w i * exp (-τ * E i)) / (exp 1 ^ 2 * τ ^ 2) := by ring

/-- (c) Cauchy–Schwarz / log-convexity. Uses only w ≥ 0; s, t arbitrary reals. -/
theorem S5c (hw : ∀ i, 0 ≤ w i) (s t : ℝ) :
    C w E ((s + t) / 2) ^ 2 ≤ C w E s * C w E t := by
  unfold C
  apply Finset.sum_sq_le_sum_mul_sum_of_sq_eq_mul
  · intro i _; exact mul_nonneg (hw i) (exp_pos _).le
  · intro i _; exact mul_nonneg (hw i) (exp_pos _).le
  · intro i _
    have : exp (-((s + t) / 2) * E i) ^ 2 = exp (-s * E i) * exp (-t * E i) := by
      rw [sq, ← exp_add, ← exp_add]; ring_nf
    calc (w i * exp (-((s + t) / 2) * E i)) ^ 2
        = w i * w i * exp (-((s + t) / 2) * E i) ^ 2 := by ring
      _ = w i * exp (-s * E i) * (w i * exp (-t * E i)) := by rw [this]; ring

/-- (d) tail bound. Uses w ≥ 0 and τ ≥ 0; E0 > 0 and E ≥ 0 are NOT used. -/
theorem S5d (hw : ∀ i, 0 ≤ w i) (τ : ℝ) (hτ : 0 ≤ τ) (E0 : ℝ) :
    ∑ i ∈ univ.filter (fun i => E0 < E i), w i * exp (-(2 * τ) * E i)
      ≤ exp (-τ * E0) * C w E τ := by
  unfold C
  rw [Finset.mul_sum]
  calc ∑ i ∈ univ.filter (fun i => E0 < E i), w i * exp (-(2 * τ) * E i)
      ≤ ∑ i ∈ univ.filter (fun i => E0 < E i), exp (-τ * E0) * (w i * exp (-τ * E i)) := by
        apply Finset.sum_le_sum
        intro i hi
        have hEi : E0 < E i := (Finset.mem_filter.mp hi).2
        rw [exp_two]
        have : exp (-τ * E i) ≤ exp (-τ * E0) := by
          apply exp_le_exp.mpr; nlinarith
        calc w i * (exp (-τ * E i) * exp (-τ * E i))
            = (w i * exp (-τ * E i)) * exp (-τ * E i) := by ring
          _ ≤ (w i * exp (-τ * E i)) * exp (-τ * E0) :=
              mul_le_mul_of_nonneg_left this (mul_nonneg (hw i) (exp_pos _).le)
          _ = exp (-τ * E0) * (w i * exp (-τ * E i)) := by ring
    _ ≤ ∑ i, exp (-τ * E0) * (w i * exp (-τ * E i)) := by
        apply Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _)
        intro i _ _
        exact mul_nonneg (exp_pos _).le (mul_nonneg (hw i) (exp_pos _).le)

/-- (d) second half: regularized weight in [0, E0] (i.e. E_i ≤ E0). -/
theorem S5d_window (hw : ∀ i, 0 ≤ w i) (τ : ℝ) (hτ : 0 ≤ τ) (E0 : ℝ) :
    C w E (2 * τ) - exp (-τ * E0) * C w E τ
      ≤ ∑ i ∈ univ.filter (fun i => E i ≤ E0), w i * exp (-(2 * τ) * E i) := by
  have hd := S5d w E hw τ hτ E0
  have hsplit := Finset.sum_filter_add_sum_filter_not univ (fun i => E i ≤ E0)
    (fun i => w i * exp (-(2 * τ) * E i))
  have hf : univ.filter (fun i => ¬ E i ≤ E0) = univ.filter (fun i => E0 < E i) := by
    ext i; simp [not_le]
  rw [hf] at hsplit
  unfold C at *
  linarith

lemma C_two_le (hw : ∀ i, 0 ≤ w i) (hE : ∀ i, 0 ≤ E i) (τ : ℝ) (hτ : 0 ≤ τ) :
    C w E (2 * τ) ≤ C w E τ := by
  unfold C
  apply Finset.sum_le_sum
  intro i _
  apply mul_le_mul_of_nonneg_left _ (hw i)
  apply exp_le_exp.mpr
  nlinarith [hE i]

/-- (e). Uses w ≥ 0, E ≥ 0, τ > 0, v > 0, v ≤ C(2τ), C(τ) ≤ V.
    v ≤ V, V > 0 and E0 > 0 are consequences, not hypotheses. -/
theorem S5e (hw : ∀ i, 0 ≤ w i) (hE : ∀ i, 0 ≤ E i) (τ : ℝ) (hτ : 0 < τ)
    (v V : ℝ) (hv : 0 < v) (h2 : v ≤ C w E (2 * τ)) (hV : C w E τ ≤ V) :
    v / 2 ≤ ∑ i ∈ univ.filter (fun i => E i ≤ (1 / τ) * log (2 * V / v)),
      w i * exp (-(2 * τ) * E i) := by
  have hCC := C_two_le w E hw hE τ hτ.le
  have hVpos : 0 < V := by linarith
  have hwin := S5d_window w E hw τ hτ.le ((1 / τ) * log (2 * V / v))
  have hexp : exp (-τ * ((1 / τ) * log (2 * V / v))) = v / (2 * V) := by
    have : -τ * ((1 / τ) * log (2 * V / v)) = -log (2 * V / v) := by
      field_simp; ring
    rw [this, exp_neg, exp_log (by positivity)]
    field_simp
  rw [hexp] at hwin
  have hq : v / (2 * V) * C w E τ ≤ v / (2 * V) * V :=
    mul_le_mul_of_nonneg_left hV (by positivity)
  have hq' : v / (2 * V) * V = v / 2 := by field_simp; ring
  linarith

end S5

namespace R9

/-- Jordan + sin x ≤ x on [0, π/2], extended to |y| ≤ π/2 with absolute values. -/
lemma abs_sin_bounds (y : ℝ) (hy : |y| ≤ π / 2) :
    2 / π * |y| ≤ |sin y| ∧ |sin y| ≤ |y| := by
  rcases le_total 0 y with h | h
  · have hs : 0 ≤ sin y := sin_nonneg_of_nonneg_of_le_pi h (by linarith [abs_of_nonneg h, pi_pos])
    rw [abs_of_nonneg h, abs_of_nonneg hs]
    rw [abs_of_nonneg h] at hy
    exact ⟨mul_le_sin h hy, sin_le h⟩
  · have h' : 0 ≤ -y := by linarith
    have hy' : -y ≤ π / 2 := by rw [abs_of_nonpos h] at hy; exact hy
    have hs : 0 ≤ sin (-y) := sin_nonneg_of_nonneg_of_le_pi h' (by linarith [pi_pos])
    rw [abs_of_nonpos h, ← abs_neg (sin y), ← sin_neg, abs_of_nonneg hs]
    exact ⟨mul_le_sin h' hy', sin_le h'⟩

/-- (a) componentwise bound on the lattice momentum: for b > 0 and |k b| ≤ π,
    (2/π)|k| ≤ |(2/b) sin(k b/2)| ≤ |k|. -/
theorem jordan_khat (b k : ℝ) (hb : 0 < b) (hk : |k * b| ≤ π) :
    2 / π * |k| ≤ |2 / b * sin (k * b / 2)| ∧ |2 / b * sin (k * b / 2)| ≤ |k| := by
  have hy : |k * b / 2| ≤ π / 2 := by
    rw [abs_div, abs_two]; linarith
  obtain ⟨h1, h2⟩ := abs_sin_bounds (k * b / 2) hy
  have habs : |k * b / 2| = |k| * b / 2 := by
    rw [abs_div, abs_mul, abs_two, abs_of_pos hb]
  rw [habs] at h1 h2
  have h2b : |2 / b| = 2 / b := abs_of_pos (by positivity)
  rw [abs_mul, h2b]
  constructor
  · have := mul_le_mul_of_nonneg_left h1 (by positivity : (0:ℝ) ≤ 2 / b)
    calc 2 / π * |k| = 2 / b * (2 / π * (|k| * b / 2)) := by field_simp; ring
      _ ≤ 2 / b * |sin (k * b / 2)| := this
  · have := mul_le_mul_of_nonneg_left h2 (by positivity : (0:ℝ) ≤ 2 / b)
    calc 2 / b * |sin (k * b / 2)| ≤ 2 / b * (|k| * b / 2) := this
      _ = |k| := by field_simp; ring

variable {ι : Type*} [Fintype ι]

/-- (b) keeping a subset of nonnegative terms gives a lower bound. -/
theorem keep_terms (a : ι → ℝ) (ha : ∀ i, 0 ≤ a i) (K : Finset ι) :
    ∑ i ∈ K, a i ≤ ∑ i, a i :=
  Finset.sum_le_sum_of_subset_of_nonneg (Finset.subset_univ K) (fun i _ _ => ha i)

/-- (b) quantitative form: K.card terms each at least c. -/
theorem keep_terms_card (a : ι → ℝ) (ha : ∀ i, 0 ≤ a i) (K : Finset ι) (c : ℝ)
    (hc : ∀ i ∈ K, c ≤ a i) : K.card * c ≤ ∑ i, a i := by
  have h1 : ∑ _i ∈ K, c ≤ ∑ i ∈ K, a i := Finset.sum_le_sum hc
  rw [Finset.sum_const, nsmul_eq_mul] at h1
  linarith [keep_terms a ha K]

/-- Upper-bound step: Σ_{i,j} F_ij u_i u_j ≤ Fmax (Σ u)^2 for 0 ≤ F_ij ≤ Fmax, u ≥ 0
    (F_ij plays |fhat_b(k+k')|^2, u plays w(k) e^{-t khat}). -/
theorem factor_upper (F : ι → ι → ℝ) (u : ι → ℝ) (Fmax : ℝ)
    (hF : ∀ i j, F i j ≤ Fmax) (hu : ∀ i, 0 ≤ u i) :
    ∑ i, ∑ j, F i j * (u i * u j) ≤ Fmax * (∑ i, u i) ^ 2 := by
  have h : ∀ i j, F i j * (u i * u j) ≤ Fmax * (u i * u j) := fun i j =>
    mul_le_mul_of_nonneg_right (hF i j) (mul_nonneg (hu i) (hu j))
  calc ∑ i, ∑ j, F i j * (u i * u j) ≤ ∑ i, ∑ j, Fmax * (u i * u j) :=
        Finset.sum_le_sum fun i _ => Finset.sum_le_sum fun j _ => h i j
    _ = Fmax * (∑ i, u i) ^ 2 := by
        rw [sq, Finset.sum_mul_sum, Finset.mul_sum]
        refine Finset.sum_congr rfl fun i _ => ?_
        rw [Finset.mul_sum]

/-- (c) corollary: if a kept subset K of the (nonnegative) atoms already gives v at time 2τ,
    and C(τ) ≤ V, then the regularized weight in [0, (1/τ) log(2V/v)] is at least v/2. -/
theorem window_from_two_sided (w E : ι → ℝ) (hw : ∀ i, 0 ≤ w i) (hE : ∀ i, 0 ≤ E i)
    (τ : ℝ) (hτ : 0 < τ) (v V : ℝ) (hv : 0 < v) (K : Finset ι)
    (hK : v ≤ ∑ i ∈ K, w i * exp (-(2 * τ) * E i)) (hV : S5.C w E τ ≤ V) :
    v / 2 ≤ ∑ i ∈ univ.filter (fun i => E i ≤ (1 / τ) * log (2 * V / v)),
      w i * exp (-(2 * τ) * E i) := by
  have h2 : v ≤ S5.C w E (2 * τ) := by
    unfold S5.C
    exact le_trans hK (keep_terms _ (fun i => mul_nonneg (hw i) (exp_pos _).le) K)
  exact S5.S5e w E hw hE τ hτ v V hv h2 hV

end R9

#print axioms R9.jordan_khat
#print axioms R9.keep_terms
#print axioms R9.keep_terms_card
#print axioms R9.factor_upper
#print axioms R9.window_from_two_sided
