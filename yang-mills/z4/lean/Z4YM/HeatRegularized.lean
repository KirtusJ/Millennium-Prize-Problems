/-
S5 (a)-(g) for finite positive sums of atoms.
Predicates fixed before first compile:
  P1 file compiles (exit 0), no sorry;
  P2 #print axioms of every main theorem shows only propext, Classical.choice, Quot.sound;
  P3 mutated constants (a: 1/(2 e tau), b: 3) are rejected (checked in scratch copies).
Hypotheses are stated exactly as used; see report.md for which stated ones are unused.
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

/-- E0 in (e) is automatically positive. -/
theorem S5e_E0_pos (hw : ∀ i, 0 ≤ w i) (hE : ∀ i, 0 ≤ E i) (τ : ℝ) (hτ : 0 < τ)
    (v V : ℝ) (hv : 0 < v) (h2 : v ≤ C w E (2 * τ)) (hV : C w E τ ≤ V) :
    0 < (1 / τ) * log (2 * V / v) := by
  have hCC := C_two_le w E hw hE τ hτ.le
  have h1 : 1 < 2 * V / v := by rw [lt_div_iff₀ hv]; linarith
  exact mul_pos (by positivity) (log_pos h1)

/-- P0 = total weight at E = 0. -/
noncomputable def P0 : ℝ := ∑ i ∈ univ.filter (fun i => E i = 0), w i

lemma C_sub_P0 (t : ℝ) :
    C w E t - P0 w E = ∑ i ∈ univ.filter (fun i => ¬ E i = 0), w i * exp (-t * E i) := by
  unfold C P0
  have hsplit := Finset.sum_filter_add_sum_filter_not univ (fun i => E i = 0)
    (fun i => w i * exp (-t * E i))
  have h0 : ∑ i ∈ univ.filter (fun i => E i = 0), w i * exp (-t * E i)
      = ∑ i ∈ univ.filter (fun i => E i = 0), w i := by
    apply Finset.sum_congr rfl
    intro i hi
    rw [(Finset.mem_filter.mp hi).2]; simp
  linarith

/-- (f) gap direction. Uses w ≥ 0, s ≤ t, and: w_i > 0 → E_i = 0 ∨ m ≤ E_i.
    Neither s ≥ 0 nor m > 0 is needed. -/
theorem S5f (hw : ∀ i, 0 ≤ w i) (m : ℝ) (hgap : ∀ i, 0 < w i → E i = 0 ∨ m ≤ E i)
    (s t : ℝ) (hst : s ≤ t) :
    C w E t - P0 w E ≤ exp (-m * (t - s)) * (C w E s - P0 w E) := by
  rw [C_sub_P0, C_sub_P0, Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  have hne : ¬ E i = 0 := (Finset.mem_filter.mp hi).2
  rcases (hw i).lt_or_eq with hpos | hzero
  · have hm : m ≤ E i := (hgap i hpos).resolve_left hne
    have : exp (-t * E i) ≤ exp (-m * (t - s)) * exp (-s * E i) := by
      rw [← exp_add]; apply exp_le_exp.mpr; nlinarith
    calc w i * exp (-t * E i) ≤ w i * (exp (-m * (t - s)) * exp (-s * E i)) :=
          mul_le_mul_of_nonneg_left this (hw i)
      _ = exp (-m * (t - s)) * (w i * exp (-s * E i)) := by ring
  · rw [← hzero]; simp

/-- (g) part 1: a single atom with w_j > 0, E_j ≠ 0 bounds C(t) - P0 from below. -/
theorem S5g_lower (hw : ∀ i, 0 ≤ w i) (j : ι) (hEj : E j ≠ 0) (t : ℝ) :
    w j * exp (-t * E j) ≤ C w E t - P0 w E := by
  rw [C_sub_P0]
  apply Finset.single_le_sum (f := fun i => w i * exp (-t * E i))
  · intro i _; exact mul_nonneg (hw i) (exp_pos _).le
  · simp [hEj]

/-- (g) part 2: if 0 < E_j < m with w_j > 0, no bound C(t) - P0 ≤ K e^{-m t} holds for large t:
    explicit t = max T (log((|K|+1)/w_j)/(m - E_j)) + 1 violates it. -/
theorem S5g (hw : ∀ i, 0 ≤ w i) (m : ℝ) (j : ι) (hwj : 0 < w j) (hE0 : 0 < E j)
    (hEm : E j < m) (K T : ℝ) :
    let t := max T (log ((|K| + 1) / w j) / (m - E j)) + 1
    T ≤ t ∧ K * exp (-m * t) < C w E t - P0 w E := by
  intro t
  have hd : 0 < m - E j := by linarith
  have ht1 : log ((|K| + 1) / w j) / (m - E j) < t := by
    have := le_max_right T (log ((|K| + 1) / w j) / (m - E j)); simp only [t]; linarith
  refine ⟨by have := le_max_left T (log ((|K| + 1) / w j) / (m - E j)); simp only [t]; linarith, ?_⟩
  have hL : log ((|K| + 1) / w j) < (m - E j) * t := by
    rw [div_lt_iff₀ hd] at ht1; linarith
  have hpos : 0 < (|K| + 1) / w j := by positivity
  have hX : (|K| + 1) / w j < exp ((m - E j) * t) := by
    rw [← exp_log hpos]; exact exp_lt_exp.mpr hL
  have hX2 : (|K| + 1) < w j * exp ((m - E j) * t) := by
    rw [div_lt_iff₀ hwj] at hX; linarith
  have hsplit : exp ((m - E j) * t) * exp (-m * t) = exp (-t * E j) := by
    rw [← exp_add]; ring_nf
  have hem : 0 < exp (-m * t) := exp_pos _
  have h3 : (|K| + 1) * exp (-m * t) < w j * exp (-t * E j) := by
    rw [← hsplit]; nlinarith
  have hK : K * exp (-m * t) ≤ (|K| + 1) * exp (-m * t) :=
    mul_le_mul_of_nonneg_right (by linarith [le_abs_self K]) hem.le
  have hlow := S5g_lower w E hw j (ne_of_gt hE0) t
  linarith

end S5

#print axioms S5.mul_exp_neg_le
#print axioms S5.sq_mul_exp_neg_le
#print axioms S5.sq_mul_exp_neg_fails_neg
#print axioms S5.S5a
#print axioms S5.S5b
#print axioms S5.S5c
#print axioms S5.S5d
#print axioms S5.S5d_window
#print axioms S5.S5e
#print axioms S5.S5e_E0_pos
#print axioms S5.S5f
#print axioms S5.S5g_lower
#print axioms S5.S5g
