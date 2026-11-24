/-
Discrete.lean. The refinement inequality (Theorem "Refinement with an exceptional set") in its
discrete form, on a finite-dimensional real inner product space, for a positive self-adjoint
contraction given by spectral data: an orthonormal basis `e` and eigenvalues `mu i` in `[0,1]`.
Eigenvalue zero is allowed, so the operator may have a kernel. The first hypothesis is taken at
a general lag `2k` (k = 1 is the theorem; general k is the remark on a longer mixing lag).
The scalar lemmas `xr_le`, `scalar_step`, `scalar_step_pos` and the lemma `pyth` are copied
unchanged from Inheritance.lean so that this file stands alone.
-/
import Mathlib

namespace Discrete
open Real
open scoped BigOperators InnerProductSpace

/-! ## L1  scalar core -/

/-- L1a: `x(1 - x^r) ≤ r(1 - x)` for `x ∈ [0,1]` and REAL `r ≥ 0` (`x ^ r` is `Real.rpow`). -/
theorem xr_le (x r : ℝ) (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (hr : 0 ≤ r) :
    x * (1 - x ^ r) ≤ r * (1 - x) := by
  rcases hx0.eq_or_lt with h | h
  · subst h; simp; nlinarith
  · have h1 : x ^ r = exp (log x * r) := Real.rpow_def_of_pos h r
    have h2 := Real.add_one_le_exp (log x * r)
    have h3 : -log x ≤ 1/x - 1 := by
      have := Real.log_le_sub_one_of_pos (one_div_pos.mpr h)
      rw [one_div, Real.log_inv] at this; rwa [one_div]
    have h4 : -(x * log x) ≤ 1 - x := by
      have := mul_le_mul_of_nonneg_left h3 h.le
      rw [mul_sub, mul_one_div_cancel h.ne'] at this; linarith
    rw [h1]
    have h5 : x * (1 - exp (log x * r)) ≤ x * (-(log x * r)) :=
      mul_le_mul_of_nonneg_left (by linarith) h.le
    nlinarith

/-- L1b: the final scalar step. From `b ≤ 1 - x + x(1-x^r)/γ + κ`, `x ∈ [0,1]`, `γ > 0`, `r ≥ 0`
deduce `(b - κ)/(1 + r/γ) ≤ 1 - x`. -/
theorem scalar_step (b κ γ r x : ℝ) (hγ : 0 < γ) (hr : 0 ≤ r) (hx0 : 0 ≤ x) (hx1 : x ≤ 1)
    (h : b ≤ 1 - x + x * (1 - x ^ r) / γ + κ) :
    (b - κ) / (1 + r / γ) ≤ 1 - x := by
  have k := xr_le x r hx0 hx1 hr
  have k2 : x * (1 - x ^ r) / γ ≤ r * (1 - x) / γ := div_le_div_of_nonneg_right k hγ.le
  have hpos : 0 < 1 + r / γ := by positivity
  rw [div_le_iff₀ hpos]
  have : r * (1 - x) / γ = (1 - x) * (r / γ) := by ring
  nlinarith

/-- L1b, positive-part form (uses `x ≤ 1`). -/
theorem scalar_step_pos (b κ γ r x : ℝ) (hγ : 0 < γ) (hr : 0 ≤ r) (hx0 : 0 ≤ x) (hx1 : x ≤ 1)
    (h : b ≤ 1 - x + x * (1 - x ^ r) / γ + κ) :
    max (b - κ) 0 / (1 + r / γ) ≤ 1 - x := by
  rcases le_total (b - κ) 0 with h0 | h0
  · rw [max_eq_right h0, zero_div]; linarith
  · rw [max_eq_left h0]; exact scalar_step b κ γ r x hγ hr hx0 hx1 h


set_option linter.unusedSectionVars false
variable {ι E : Type*} [Fintype ι] [DecidableEq ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- `A^n` defined from spectral data: `A^n w = Σ_i mu_i^n ⟪e_i, w⟫ e_i`. -/
noncomputable def Apow (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (n : ℕ) (w : E) : E :=
  ∑ i, (mu i ^ n * ⟪e i, w⟫_ℝ) • e i

theorem Apow_quad (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (n : ℕ) (w : E) :
    ⟪w, Apow e mu n w⟫_ℝ = ∑ i, mu i ^ n * ⟪e i, w⟫_ℝ ^ 2 := by
  unfold Apow; rw [inner_sum]; refine Finset.sum_congr rfl fun i _ => ?_
  rw [inner_smul_right, real_inner_comm]; ring

theorem Apow_lower (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (hmu : ∀ i, 0 ≤ mu i) (n : ℕ)
    (i0 : ι) (w : E) :
    mu i0 ^ n * ⟪e i0, w⟫_ℝ ^ 2 ≤ ⟪w, Apow e mu n w⟫_ℝ := by
  rw [Apow_quad]
  exact Finset.single_le_sum (f := fun i => mu i ^ n * ⟪e i, w⟫_ℝ ^ 2)
    (fun i _ => mul_nonneg (pow_nonneg (hmu i) n) (sq_nonneg _)) (Finset.mem_univ i0)

theorem Apow_eig_quad (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (n : ℕ) (i0 : ι) :
    ⟪e i0, Apow e mu n (e i0)⟫_ℝ = mu i0 ^ n := by
  rw [Apow_quad, Finset.sum_eq_single i0]
  · rw [real_inner_self_eq_norm_sq, e.orthonormal.1 i0]; ring
  · intro i _ hi; rw [e.orthonormal.2 hi]; ring
  · simp

theorem Apow_eig (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (n : ℕ) (i0 : ι) :
    Apow e mu n (e i0) = (mu i0 ^ n) • e i0 := by
  unfold Apow; rw [Finset.sum_eq_single i0]
  · rw [real_inner_self_eq_norm_sq, e.orthonormal.1 i0]; simp
  · intro i _ hi; rw [e.orthonormal.2 hi]; simp
  · simp

/-- `‖A^n w‖ ≤ mu_{i0}^n ‖w‖` when `mu_{i0}` is the largest eigenvalue; with `Apow_eig` this
identifies `‖A^n‖ = mu_{i0}^n`. -/
theorem Apow_norm_le (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (hmu : ∀ i, 0 ≤ mu i) (n : ℕ)
    (i0 : ι) (hmax : ∀ i, mu i ≤ mu i0) (w : E) :
    ‖Apow e mu n w‖ ≤ mu i0 ^ n * ‖w‖ := by
  have hsq : ‖Apow e mu n w‖ ^ 2 = ∑ i, (mu i ^ n * ⟪e i, w⟫_ℝ) ^ 2 := by
    rw [← real_inner_self_eq_norm_sq]; unfold Apow
    rw [e.orthonormal.inner_sum]; simp [pow_two]
  have hpar : ‖w‖ ^ 2 = ∑ i, ⟪e i, w⟫_ℝ ^ 2 := by
    rw [← real_inner_self_eq_norm_sq, ← e.sum_inner_mul_inner w w]
    refine Finset.sum_congr rfl fun i _ => ?_; rw [real_inner_comm]; ring
  have h0 : 0 ≤ mu i0 ^ n := pow_nonneg (hmu i0) n
  have hle : ‖Apow e mu n w‖ ^ 2 ≤ (mu i0 ^ n * ‖w‖) ^ 2 := by
    rw [hsq, mul_pow, hpar, Finset.mul_sum]
    refine Finset.sum_le_sum fun i _ => ?_
    rw [mul_pow]
    have : mu i ^ n ≤ mu i0 ^ n := pow_le_pow_left₀ (hmu i) (hmax i) n
    exact mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (pow_nonneg (hmu i) n) this 2) (sq_nonneg _)
  exact (sq_le_sq₀ (norm_nonneg _) (mul_nonneg h0 (norm_nonneg _))).mp hle

/-- From `‖B A^j B‖ ≤ κ` (pointwise) and `A^j ⪰ mu^j vv^*`: `0 ≤ κ` and `mu^j ‖B v‖² ≤ κ`
for the unit eigenvector `v = e_{i0}`. -/
theorem B_step (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (hmu : ∀ i, 0 ≤ mu i) (i0 : ι)
    (B : E →ₗ[ℝ] E)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x) (j : ℕ) (κ : ℝ)
    (h2 : ∀ u, ‖B (Apow e mu j (B u))‖ ≤ κ * ‖u‖) :
    0 ≤ κ ∧ mu i0 ^ j * ‖B (e i0)‖ ^ 2 ≤ κ := by
  set v := e i0
  have hv : ‖v‖ = 1 := e.orthonormal.1 i0
  have hκ : 0 ≤ κ := by have := h2 v; rw [hv, mul_one] at this; exact (norm_nonneg _).trans this
  refine ⟨hκ, ?_⟩
  set u := B v
  have hβ : ⟪v, u⟫_ℝ = ‖u‖ ^ 2 := by
    rw [← real_inner_self_eq_norm_sq]; show ⟪v, B v⟫_ℝ = ⟪B v, B v⟫_ℝ
    rw [hBsa, hBid]
  have hlow := Apow_lower e mu hmu j i0 u
  rw [hβ] at hlow
  have hup : ⟪u, Apow e mu j u⟫_ℝ ≤ κ * ‖u‖ ^ 2 := by
    have : ⟪u, Apow e mu j u⟫_ℝ = ⟪u, B (Apow e mu j (B u))⟫_ℝ := by
      have hu : B u = u := hBid v
      rw [← hBsa, hu]
    rw [this]
    calc _ ≤ ‖u‖ * ‖B (Apow e mu j (B u))‖ := real_inner_le_norm _ _
      _ ≤ ‖u‖ * (κ * ‖u‖) := mul_le_mul_of_nonneg_left (h2 u) (norm_nonneg _)
      _ = κ * ‖u‖ ^ 2 := by ring
  rcases (sq_nonneg ‖u‖).eq_or_lt with h0 | h0
  · rw [← h0, mul_zero]; exact hκ
  · have : mu i0 ^ j * ‖u‖ ^ 2 * ‖u‖ ^ 2 ≤ κ * ‖u‖ ^ 2 := by nlinarith
    exact le_of_mul_le_mul_right this h0

/-- Deduction (Q): `‖v‖² = ‖Pv‖² + ‖Qv‖²` and `‖Qv‖² = ‖Gv‖² + ‖Bv‖²`, `Q = I - P`,
`G = Q - B`, for self-adjoint idempotent `P, B` with `B P = 0`. -/
theorem pyth (P B : E →ₗ[ℝ] E)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x)
    (hBP : ∀ x, B (P x) = 0) (v : E) :
    ‖v‖ ^ 2 = ‖P v‖ ^ 2 + ‖v - P v‖ ^ 2 ∧
    ‖v - P v‖ ^ 2 = ‖v - P v - B v‖ ^ 2 + ‖B v‖ ^ 2 := by
  have o1 : ⟪P v, v - P v⟫_ℝ = 0 := by
    rw [inner_sub_right, hPsa v v, hPsa v (P v), hPid, sub_self]
  have o2 : ⟪v - P v - B v, B v⟫_ℝ = 0 := by
    have a1 : ⟪P v, B v⟫_ℝ = 0 := by rw [← hBsa, hBP, inner_zero_left]
    have a2 : ⟪B v, B v⟫_ℝ = ⟪v, B v⟫_ℝ := by rw [hBsa, hBid]
    rw [inner_sub_left, inner_sub_left, a1, a2]; ring
  constructor
  · have := norm_add_sq_real (P v) (v - P v)
    rw [o1, add_sub_cancel] at this; linarith
  · have := norm_add_sq_real (v - P v - B v) (B v)
    rw [o2, sub_add_cancel] at this; linarith


/-- MAIN (discrete form, general lag). For ANY eigen-index `i0`:
`(b - κ)/(1 + 2k/(γ m)) ≤ 1 - mu_{i0}^m`. With `i0` the largest eigenvalue the right side is
`1 - ‖A^m‖` (see `Apow_norm_le`, `Apow_eig`). Hypotheses, for integers `k ≥ 1`, `m ≥ j ≥ 1`
(only `1 ≤ m`, `j ≤ m` are used):
 `h1` : `γ ‖G w‖² ≤ ⟪w, (I - A^{2k}) w⟫` for all `w`, with `G = I - P - B`,
 `h2` : `‖B A^j B u‖ ≤ κ ‖u‖` for all `u`,
 `h3` : `‖P A^m P u‖ ≤ (1-b) ‖u‖` for all `u`. -/
theorem refinement_main (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (hmu0 : ∀ i, 0 ≤ mu i)
    (hmu1 : ∀ i, mu i ≤ 1) (i0 : ι)
    (P B : E →ₗ[ℝ] E)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x)
    (hBP : ∀ x, B (P x) = 0)
    (k j m : ℕ) (hm : 1 ≤ m) (hjm : j ≤ m) (γ κ b : ℝ) (hγ : 0 < γ)
    (h1 : ∀ w, γ * ‖w - P w - B w‖ ^ 2 ≤ ⟪w, w⟫_ℝ - ⟪w, Apow e mu (2 * k) w⟫_ℝ)
    (h2 : ∀ u, ‖B (Apow e mu j (B u))‖ ≤ κ * ‖u‖)
    (h3 : ∀ u, ‖P (Apow e mu m (P u))‖ ≤ (1 - b) * ‖u‖) :
    (b - κ) / (1 + 2 * (k : ℝ) / (γ * (m : ℝ))) ≤ 1 - mu i0 ^ m := by
  set v := e i0 with hvdef
  have hv : ‖v‖ = 1 := e.orthonormal.1 i0
  set q := mu i0 with hqdef
  have hq0 : 0 ≤ q := hmu0 i0
  have hq1 : q ≤ 1 := hmu1 i0
  set x := q ^ m with hxdef
  have hmR : (0 : ℝ) < (m : ℝ) := by exact_mod_cast hm
  set r := 2 * (k : ℝ) / (m : ℝ) with hrdef
  have hx0 : 0 ≤ x := pow_nonneg hq0 m
  have hx1 : x ≤ 1 := pow_le_one₀ hq0 hq1
  have hr : 0 ≤ r := by positivity
  -- x ^ r = q ^ (2k)
  have hxr : x ^ r = q ^ (2 * k) := by
    rw [hxdef, hrdef, ← Real.rpow_natCast q m, ← Real.rpow_mul hq0]
    have : (m : ℝ) * (2 * (k : ℝ) / (m : ℝ)) = ((2 * k : ℕ) : ℝ) := by
      push_cast; field_simp
    rw [this, Real.rpow_natCast]
  -- (A) mixing form at v
  have hA : γ * ‖v - P v - B v‖ ^ 2 ≤ 1 - x ^ r := by
    have := h1 v
    rw [real_inner_self_eq_norm_sq, hv, hvdef, Apow_eig_quad] at this
    rw [hxr]; simpa using this
  -- (B)
  obtain ⟨hκ, hB⟩ := B_step e mu hmu0 i0 B hBsa hBid j κ h2
  -- (P)
  obtain ⟨_, hP⟩ := B_step e mu hmu0 i0 P hPsa hPid m (1 - b) h3
  -- (Q)
  obtain ⟨q1, q2⟩ := pyth P B hPsa hPid hBsa hBid hBP v
  rw [hv] at q1
  set g := ‖v - P v - B v‖ ^ 2
  set β := ‖B v‖ ^ 2
  have hg : x * g ≤ x * (1 - x ^ r) / γ := by
    rw [mul_div_assoc]; apply mul_le_mul_of_nonneg_left _ hx0
    rw [le_div_iff₀ hγ]; linarith
  have hxβ : x * β ≤ κ := by
    have hsplit : x = q ^ (m - j) * q ^ j := by
      rw [hxdef, ← pow_add, Nat.sub_add_cancel hjm]
    have hle1 : q ^ (m - j) ≤ 1 := pow_le_one₀ hq0 hq1
    have he0 : 0 ≤ q ^ (m - j) := pow_nonneg hq0 _
    rw [hsplit, mul_assoc]
    calc _ ≤ q ^ (m - j) * κ := mul_le_mul_of_nonneg_left hB he0
      _ ≤ 1 * κ := mul_le_mul_of_nonneg_right hle1 hκ
      _ = κ := one_mul κ
  have hb : b ≤ 1 - x + x * (1 - x ^ r) / γ + κ := by
    have h' : ‖P v‖ ^ 2 = 1 - g - β := by linarith
    have e1 : x * ‖P v‖ ^ 2 = x - x * g - x * β := by rw [h']; ring
    linarith
  have := scalar_step b κ γ r x hγ hr hx0 hx1 hb
  have hrr : r / γ = 2 * (k : ℝ) / (γ * (m : ℝ)) := by rw [hrdef, div_div, mul_comm (m : ℝ) γ]
  rwa [hrr] at this

/-- OPERATOR-NORM FORM. With `mu_{i0}` the largest eigenvalue: for every `w`,
`‖A^m w‖ ≤ (1 - (b-κ)_+/(1 + 2k/(γ m))) ‖w‖`, that is,
`1 - ‖A^m‖ ≥ (b-κ)_+/(1 + 2k/(γ m))`. -/
theorem refinement_norm (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (hmu0 : ∀ i, 0 ≤ mu i)
    (hmu1 : ∀ i, mu i ≤ 1) (i0 : ι) (hmax : ∀ i, mu i ≤ mu i0)
    (P B : E →ₗ[ℝ] E)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x)
    (hBP : ∀ x, B (P x) = 0)
    (k j m : ℕ) (hm : 1 ≤ m) (hjm : j ≤ m) (γ κ b : ℝ) (hγ : 0 < γ)
    (h1 : ∀ w, γ * ‖w - P w - B w‖ ^ 2 ≤ ⟪w, w⟫_ℝ - ⟪w, Apow e mu (2 * k) w⟫_ℝ)
    (h2 : ∀ u, ‖B (Apow e mu j (B u))‖ ≤ κ * ‖u‖)
    (h3 : ∀ u, ‖P (Apow e mu m (P u))‖ ≤ (1 - b) * ‖u‖) (w : E) :
    ‖Apow e mu m w‖ ≤ (1 - max (b - κ) 0 / (1 + 2 * (k : ℝ) / (γ * (m : ℝ)))) * ‖w‖ := by
  have hm' := refinement_main e mu hmu0 hmu1 i0 P B hPsa hPid hBsa hBid hBP k j m hm hjm γ κ b hγ
    h1 h2 h3
  have hx1 : mu i0 ^ m ≤ 1 := pow_le_one₀ (hmu0 i0) (hmu1 i0)
  have hpos : max (b - κ) 0 / (1 + 2 * (k : ℝ) / (γ * (m : ℝ))) ≤ 1 - mu i0 ^ m := by
    rcases le_total (b - κ) 0 with h0 | h0
    · rw [max_eq_right h0, zero_div]; linarith
    · rw [max_eq_left h0]; exact hm'
  calc ‖Apow e mu m w‖ ≤ mu i0 ^ m * ‖w‖ := Apow_norm_le e mu hmu0 m i0 hmax w
    _ ≤ _ := mul_le_mul_of_nonneg_right (by linarith) (norm_nonneg _)

/-! ## The theorem for an arbitrary symmetric operator on a finite-dimensional space

`A` is any linear map that is symmetric with `0 ≤ ⟪w, A w⟫ ≤ ⟪w, w⟫`. The spectral theorem of
Mathlib supplies the eigenbasis, so no spectral data are assumed. -/

theorem map_eigsum (A : E →ₗ[ℝ] E) (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ)
    (hAe : ∀ i, A (e i) = mu i • e i) (c : ι → ℝ) :
    A (∑ i, c i • e i) = ∑ i, (mu i * c i) • e i := by
  rw [map_sum]; refine Finset.sum_congr rfl fun i _ => ?_
  rw [map_smul, hAe, smul_smul, mul_comm]

theorem pow_eq_Apow (A : E →ₗ[ℝ] E) (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ)
    (hAe : ∀ i, A (e i) = mu i • e i) (n : ℕ) (w : E) :
    (A ^ n) w = Apow e mu n w := by
  induction n with
  | zero =>
    unfold Apow; simp only [pow_zero, one_mul]
    exact (e.sum_repr' w).symm
  | succ n ih =>
    rw [pow_succ']; show A ((A ^ n) w) = _
    rw [ih]; unfold Apow
    rw [map_eigsum A e mu hAe]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [pow_succ, ← mul_assoc, mul_comm (mu i) (mu i ^ n)]

/-- Theorem (refinement with an exceptional set), finite dimension, as stated in the paper with
a general mixing lag `2k`: for a symmetric `A` with `0 ≤ A ≤ I`, orthogonal projections `P`, `B`
with `B P = 0` (so the range of `B` lies in that of `I - P`), `G = I - P - B`, integers
`m ≥ 1`, `j ≤ m`, and real `γ > 0`, `κ`, `b`:
if `γ ‖G w‖² ≤ ⟪w, (I - A^{2k}) w⟫`, `‖B A^j B u‖ ≤ κ ‖u‖` and `‖P A^m P u‖ ≤ (1-b) ‖u‖`
for all vectors, then `‖A^m w‖ ≤ (1 - (b-κ)_+ / (1 + 2k/(γ m))) ‖w‖` for all `w`. -/
theorem refinement_fin [FiniteDimensional ℝ E] (A : E →ₗ[ℝ] E) (hA : A.IsSymmetric)
    (hA0 : ∀ w, 0 ≤ ⟪w, A w⟫_ℝ) (hA1 : ∀ w, ⟪w, A w⟫_ℝ ≤ ⟪w, w⟫_ℝ)
    (P B : E →ₗ[ℝ] E)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x)
    (hBP : ∀ x, B (P x) = 0)
    (k j m : ℕ) (hm : 1 ≤ m) (hjm : j ≤ m) (γ κ b : ℝ) (hγ : 0 < γ)
    (h1 : ∀ w, γ * ‖w - P w - B w‖ ^ 2 ≤ ⟪w, w⟫_ℝ - ⟪w, (A ^ (2 * k)) w⟫_ℝ)
    (h2 : ∀ u, ‖B ((A ^ j) (B u))‖ ≤ κ * ‖u‖)
    (h3 : ∀ u, ‖P ((A ^ m) (P u))‖ ≤ (1 - b) * ‖u‖) (w : E) :
    ‖(A ^ m) w‖ ≤ (1 - max (b - κ) 0 / (1 + 2 * (k : ℝ) / (γ * (m : ℝ)))) * ‖w‖ := by
  classical
  set e := hA.eigenvectorBasis (n := Module.finrank ℝ E) rfl with he
  set mu : Fin (Module.finrank ℝ E) → ℝ := fun i => hA.eigenvalues rfl i with hmu
  have hAe : ∀ i, A (e i) = mu i • e i := fun i => by
    have := hA.apply_eigenvectorBasis (n := Module.finrank ℝ E) rfl i
    simp only [he, hmu]; exact this
  have hquad : ∀ i, ⟪e i, A (e i)⟫_ℝ = mu i := fun i => by
    rw [hAe, inner_smul_right, real_inner_self_eq_norm_sq, e.orthonormal.1 i]; ring
  have hmu0 : ∀ i, 0 ≤ mu i := fun i => by rw [← hquad i]; exact hA0 _
  have hmu1 : ∀ i, mu i ≤ 1 := fun i => by
    have := hA1 (e i)
    rw [hquad, real_inner_self_eq_norm_sq, e.orthonormal.1 i] at this; simp at this; exact this
  have hpow : ∀ n u, (A ^ n) u = Apow e mu n u := fun n u => pow_eq_Apow A e mu hAe n u
  rcases isEmpty_or_nonempty (Fin (Module.finrank ℝ E)) with hemp | hne
  · have hw : w = 0 := by
      rw [← e.sum_repr' w]; exact Finset.sum_eq_zero (fun i _ => (hemp.false i).elim)
    rw [hw]; simp
  · obtain ⟨i0, _, hmax⟩ := Finset.exists_max_image Finset.univ mu Finset.univ_nonempty
    have hmax' : ∀ i, mu i ≤ mu i0 := fun i => hmax i (Finset.mem_univ i)
    rw [hpow]
    exact refinement_norm e mu hmu0 hmu1 i0 hmax' P B hPsa hPid hBsa hBid hBP k j m hm hjm γ κ b hγ
      (fun w => by rw [← hpow]; exact h1 w)
      (fun u => by rw [← hpow]; exact h2 u)
      (fun u => by rw [← hpow]; exact h3 u) w

end Discrete

#print axioms Discrete.refinement_main
#print axioms Discrete.refinement_norm
#print axioms Discrete.Apow_norm_le
#print axioms Discrete.Apow_eig
#print axioms Discrete.refinement_fin
