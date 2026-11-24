/-
Hilbert.lean. The refinement inequality on an arbitrary real inner product space (any dimension,
completeness not used), for a bounded symmetric positive operator `A` of norm at most one.
The proof uses approximate eigenvectors for the top of the spectrum instead of a spectral projection.
The scalar lemmas are copied unchanged from Inheritance.lean so that this file stands alone.
-/
import Mathlib

namespace RefinementHilbert
open Real
open scoped InnerProductSpace

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


variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-! ## Powers of a symmetric positive contraction -/

theorem pow_succ_apply (A : E →L[ℝ] E) (n : ℕ) (x : E) : (A ^ (n + 1)) x = A ((A ^ n) x) := by
  rw [pow_succ']; rfl

theorem pow_succ_apply' (A : E →L[ℝ] E) (n : ℕ) (x : E) : (A ^ (n + 1)) x = (A ^ n) (A x) := by
  rw [pow_succ]; rfl

theorem pow_sym (A : E →L[ℝ] E) (hsym : ∀ x y, ⟪A x, y⟫_ℝ = ⟪x, A y⟫_ℝ) (n : ℕ) (x y : E) :
    ⟪(A ^ n) x, y⟫_ℝ = ⟪x, (A ^ n) y⟫_ℝ := by
  induction n generalizing x y with
  | zero => simp
  | succ n ih => rw [pow_succ_apply, hsym, ih, ← pow_succ_apply']

theorem pow_pos_form (A : E →L[ℝ] E) (hsym : ∀ x y, ⟪A x, y⟫_ℝ = ⟪x, A y⟫_ℝ)
    (hpos : ∀ x, 0 ≤ ⟪x, A x⟫_ℝ) (n : ℕ) (x : E) : 0 ≤ ⟪x, (A ^ n) x⟫_ℝ := by
  induction n using Nat.twoStepInduction generalizing x with
  | zero => simp; exact real_inner_self_nonneg
  | one => simpa using hpos x
  | more n ih _ =>
    have : (A ^ (n + 2)) x = A ((A ^ n) (A x)) := by
      rw [pow_succ_apply, pow_succ_apply']
    rw [this, ← hsym]; exact ih (A x)

theorem pow_norm_le (A : E →L[ℝ] E) (n : ℕ) (x : E) : ‖(A ^ n) x‖ ≤ ‖A‖ ^ n * ‖x‖ := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ_apply]
    calc ‖A ((A ^ n) x)‖ ≤ ‖A‖ * ‖(A ^ n) x‖ := A.le_opNorm _
      _ ≤ ‖A‖ * (‖A‖ ^ n * ‖x‖) := mul_le_mul_of_nonneg_left ih (norm_nonneg _)
      _ = ‖A‖ ^ (n + 1) * ‖x‖ := by ring

/-- Cauchy--Schwarz for a symmetric positive form. -/
theorem cs_form (T : E → E) (hadd : ∀ x y, T (x + y) = T x + T y)
    (hsmul : ∀ (c : ℝ) x, T (c • x) = c • T x)
    (hsym : ∀ x y, ⟪T x, y⟫_ℝ = ⟪x, T y⟫_ℝ) (hpos : ∀ x, 0 ≤ ⟪x, T x⟫_ℝ) (x y : E) :
    ⟪x, T y⟫_ℝ ^ 2 ≤ ⟪x, T x⟫_ℝ * ⟪y, T y⟫_ℝ := by
  have key : ∀ s : ℝ, 0 ≤ ⟪y, T y⟫_ℝ * (s * s) + (2 * ⟪x, T y⟫_ℝ) * s + ⟪x, T x⟫_ℝ := by
    intro s
    have h := hpos (x + s • y)
    rw [hadd, hsmul, inner_add_left, inner_add_right, inner_add_right, real_inner_smul_left,
      real_inner_smul_left, real_inner_smul_right, real_inner_smul_right] at h
    have hyx : ⟪y, T x⟫_ℝ = ⟪x, T y⟫_ℝ := by rw [← hsym, real_inner_comm]
    rw [hyx] at h; nlinarith
  have := discrim_le_zero (a := ⟪y, T y⟫_ℝ) (b := 2 * ⟪x, T y⟫_ℝ) (c := ⟪x, T x⟫_ℝ) key
  unfold discrim at this; nlinarith

/-! ## Approximate eigenvectors at the top -/

theorem approx_pow (A : E →L[ℝ] E) (h1 : ‖A‖ ≤ 1) (w : E) (η : ℝ)
    (hw : ‖A w - ‖A‖ • w‖ ≤ η) (n : ℕ) :
    ‖(A ^ n) w - ‖A‖ ^ n • w‖ ≤ n * η := by
  have hη : 0 ≤ η := (norm_nonneg _).trans hw
  have hq0 : 0 ≤ ‖A‖ := norm_nonneg _
  induction n with
  | zero => simp
  | succ n ih =>
    have e1 : (A ^ (n + 1)) w - ‖A‖ ^ (n + 1) • w
        = A ((A ^ n) w - ‖A‖ ^ n • w) + ‖A‖ ^ n • (A w - ‖A‖ • w) := by
      rw [pow_succ_apply, map_sub, map_smul, smul_sub, smul_smul, pow_succ]; abel
    rw [e1]
    have hp1 : ‖A‖ ^ n ≤ 1 := pow_le_one₀ hq0 h1
    calc _ ≤ ‖A ((A ^ n) w - ‖A‖ ^ n • w)‖ + ‖‖A‖ ^ n • (A w - ‖A‖ • w)‖ := norm_add_le _ _
      _ ≤ ‖A‖ * ‖(A ^ n) w - ‖A‖ ^ n • w‖ + ‖A‖ ^ n * ‖A w - ‖A‖ • w‖ := by
          gcongr
          · exact A.le_opNorm _
          · rw [norm_smul, Real.norm_of_nonneg (pow_nonneg hq0 n)]
      _ ≤ 1 * (n * η) + 1 * η := by
          gcongr
      _ = ((n + 1 : ℕ) : ℝ) * η := by push_cast; ring

theorem exists_approx_eig [Nontrivial E] (A : E →L[ℝ] E)
    (hsym : ∀ x y, ⟪A x, y⟫_ℝ = ⟪x, A y⟫_ℝ) (hpos : ∀ x, 0 ≤ ⟪x, A x⟫_ℝ) (h1 : ‖A‖ ≤ 1)
    (η : ℝ) (hη : 0 < η) : ∃ w : E, ‖w‖ = 1 ∧ ‖A w - ‖A‖ • w‖ ≤ η := by
  set q := ‖A‖ with hqdef
  have hq0 : 0 ≤ q := norm_nonneg _
  rcases hq0.eq_or_lt with hz | hqpos
  · -- A = 0
    obtain ⟨x, hx⟩ := exists_ne (0 : E)
    refine ⟨(‖x‖⁻¹) • x, ?_, ?_⟩
    · rw [norm_smul, norm_inv, norm_norm, inv_mul_cancel₀ (norm_ne_zero_iff.mpr hx)]
    · have hA0 : A = 0 := by rw [← norm_eq_zero]; exact hz.symm
      rw [hA0, ← hz]; simp; exact hη.le
  · set θ := min q (η ^ 2 / 4) with hθdef
    have hθpos : 0 < θ := lt_min hqpos (by positivity)
    have hθq : θ ≤ q := min_le_left _ _
    have hθη : θ ≤ η ^ 2 / 4 := min_le_right _ _
    obtain ⟨x, hx⟩ := A.exists_mul_lt_of_lt_opNorm (r := q - θ) (by linarith) (by linarith)
    have hxne : x ≠ 0 := by
      rintro rfl; simp at hx
    have hxn : 0 < ‖x‖ := norm_pos_iff.mpr hxne
    obtain ⟨w, hwdef⟩ : ∃ w : E, w = (‖x‖⁻¹) • x := ⟨_, rfl⟩
    have hw1 : ‖w‖ = 1 := by
      rw [hwdef, norm_smul, norm_inv, norm_norm, inv_mul_cancel₀ hxn.ne']
    have hAw : q - θ ≤ ‖A w‖ := by
      rw [hwdef, map_smul, norm_smul, norm_inv, norm_norm]
      rw [le_inv_mul_iff₀ hxn]; linarith [mul_comm ‖x‖ (q - θ)]
    have hAw_le : ‖A w‖ ≤ q := by
      have := A.le_opNorm w; rw [hw1, mul_one] at this; exact this
    have hsq : q ^ 2 - η ^ 2 / 2 ≤ ‖A w‖ ^ 2 := by
      have hnn : 0 ≤ q - θ := by linarith
      have : (q - θ) ^ 2 ≤ ‖A w‖ ^ 2 := pow_le_pow_left₀ hnn hAw 2
      nlinarith
    -- A(Aw) is close to q² w
    have hAAw : ‖A (A w)‖ ≤ q ^ 2 := by
      calc ‖A (A w)‖ ≤ q * ‖A w‖ := A.le_opNorm _
        _ ≤ q * q := mul_le_mul_of_nonneg_left hAw_le hq0
        _ = q ^ 2 := by ring
    have hin : ⟪A (A w), w⟫_ℝ = ‖A w‖ ^ 2 := by
      rw [hsym, real_inner_self_eq_norm_sq]
    have hclose : ‖A (A w) - q ^ 2 • w‖ ^ 2 ≤ (q * η) ^ 2 := by
      rw [norm_sub_sq_real, real_inner_smul_right, hin, norm_smul, hw1, mul_one,
        Real.norm_of_nonneg (by positivity)]
      have h2 : ‖A (A w)‖ ^ 2 ≤ (q ^ 2) ^ 2 := pow_le_pow_left₀ (norm_nonneg _) hAAw 2
      nlinarith
    have hclose' : ‖A (A w) - q ^ 2 • w‖ ≤ q * η :=
      (sq_le_sq₀ (norm_nonneg _) (by positivity)).mp hclose
    obtain ⟨u, hudef⟩ : ∃ u : E, u = A w - q • w := ⟨_, rfl⟩
    have hAu : A u + q • u = A (A w) - q ^ 2 • w := by
      rw [hudef, map_sub, map_smul, smul_sub, smul_smul]; rw [pow_two]; abel
    have hlow : q * ‖u‖ ^ 2 ≤ ‖u‖ * (q * η) := by
      have h3 : q * ‖u‖ ^ 2 ≤ ⟪u, A u + q • u⟫_ℝ := by
        rw [inner_add_right, real_inner_smul_right, real_inner_self_eq_norm_sq]
        linarith [hpos u]
      have h4 : ⟪u, A u + q • u⟫_ℝ ≤ ‖u‖ * ‖A u + q • u‖ := real_inner_le_norm _ _
      rw [hAu] at h3 h4
      have h5 : ‖u‖ * ‖A (A w) - q ^ 2 • w‖ ≤ ‖u‖ * (q * η) :=
        mul_le_mul_of_nonneg_left hclose' (norm_nonneg _)
      linarith
    refine ⟨w, hw1, ?_⟩
    rw [← hudef]
    rcases (norm_nonneg u).eq_or_lt with h0 | h0
    · rw [← h0]; exact hη.le
    · have : q * ‖u‖ * ‖u‖ ≤ q * ‖u‖ * η := by nlinarith
      exact le_of_mul_le_mul_left this (mul_pos hqpos h0)

/-! ## The three estimates at an approximate eigenvector -/

theorem quad_lower (A : E →L[ℝ] E) (h1 : ‖A‖ ≤ 1) (w : E) (hw1 : ‖w‖ = 1) (η : ℝ)
    (hw : ‖A w - ‖A‖ • w‖ ≤ η) (n : ℕ) : ‖A‖ ^ n - n * η ≤ ⟪w, (A ^ n) w⟫_ℝ := by
  have hap := approx_pow A h1 w η hw n
  have e : ⟪w, (A ^ n) w⟫_ℝ = ‖A‖ ^ n + ⟪w, (A ^ n) w - ‖A‖ ^ n • w⟫_ℝ := by
    rw [inner_sub_right, real_inner_smul_right, real_inner_self_eq_norm_sq, hw1]; ring
  have h2 : -(‖w‖ * ‖(A ^ n) w - ‖A‖ ^ n • w‖) ≤ ⟪w, (A ^ n) w - ‖A‖ ^ n • w⟫_ℝ := by
    have := abs_real_inner_le_norm w ((A ^ n) w - ‖A‖ ^ n • w)
    exact (abs_le.mp this).1
  rw [hw1, one_mul] at h2
  rw [e]; linarith

/-- For a self-adjoint idempotent `R` with `‖R A^n R u‖ ≤ c ‖u‖` and an approximate top
eigenvector `w`: `0 ≤ c` and `‖A‖^n ‖R w‖² ≤ c + 2 n η`. -/
theorem proj_step (A : E →L[ℝ] E) (hsym : ∀ x y, ⟪A x, y⟫_ℝ = ⟪x, A y⟫_ℝ)
    (hpos : ∀ x, 0 ≤ ⟪x, A x⟫_ℝ) (h1 : ‖A‖ ≤ 1)
    (R : E → E) (hRsa : ∀ x y, ⟪R x, y⟫_ℝ = ⟪x, R y⟫_ℝ) (hRid : ∀ x, R (R x) = R x)
    (n : ℕ) (c : ℝ) (hc : ∀ u, ‖R ((A ^ n) (R u))‖ ≤ c * ‖u‖)
    (w : E) (hw1 : ‖w‖ = 1) (η : ℝ) (hw : ‖A w - ‖A‖ • w‖ ≤ η) :
    0 ≤ c ∧ ‖A‖ ^ n * ‖R w‖ ^ 2 ≤ c + 2 * (n * η) := by
  have hη : 0 ≤ η := (norm_nonneg _).trans hw
  have hq0 : 0 ≤ ‖A‖ := norm_nonneg _
  have hc0 : 0 ≤ c := by have := hc w; rw [hw1, mul_one] at this; exact (norm_nonneg _).trans this
  refine ⟨hc0, ?_⟩
  obtain ⟨u, hu⟩ : ∃ u : E, u = R w := ⟨_, rfl⟩
  rw [← hu]
  have hRu : R u = u := by rw [hu, hRid]
  have hwu : ⟪w, u⟫_ℝ = ‖u‖ ^ 2 := by
    rw [← real_inner_self_eq_norm_sq, hu, hRsa, hRid]
  have hu1 : ‖u‖ ≤ 1 := by
    have h := real_inner_le_norm w u
    rw [hwu, hw1, one_mul] at h
    rcases (norm_nonneg u).eq_or_lt with h0 | h0
    · rw [← h0]; exact zero_le_one
    · have : ‖u‖ * ‖u‖ ≤ ‖u‖ * 1 := by nlinarith
      exact le_of_mul_le_mul_left this h0
  have hQ0 : 0 ≤ ‖A‖ ^ n := pow_nonneg hq0 n
  have hQ1 : ‖A‖ ^ n ≤ 1 := pow_le_one₀ hq0 h1
  -- upper bound of the form at u
  have hup : ⟪u, (A ^ n) u⟫_ℝ ≤ c * ‖u‖ ^ 2 := by
    have e : ⟪u, (A ^ n) u⟫_ℝ = ⟪u, R ((A ^ n) (R u))⟫_ℝ := by
      rw [← hRsa, hRu]
    rw [e]
    calc _ ≤ ‖u‖ * ‖R ((A ^ n) (R u))‖ := real_inner_le_norm _ _
      _ ≤ ‖u‖ * (c * ‖u‖) := mul_le_mul_of_nonneg_left (hc u) (norm_nonneg _)
      _ = c * ‖u‖ ^ 2 := by ring
  have hunn : 0 ≤ ⟪u, (A ^ n) u⟫_ℝ := pow_pos_form A hsym hpos n u
  -- the form at w
  have hww : ⟪w, (A ^ n) w⟫_ℝ ≤ ‖A‖ ^ n := by
    have := real_inner_le_norm w ((A ^ n) w)
    have h2 := pow_norm_le A n w
    rw [hw1] at this h2; linarith
  have hwwnn : 0 ≤ ⟪w, (A ^ n) w⟫_ℝ := pow_pos_form A hsym hpos n w
  -- lower bound of the mixed term
  have hap := approx_pow A h1 w η hw n
  have hlow : ‖A‖ ^ n * ‖u‖ ^ 2 - n * η ≤ ⟪w, (A ^ n) u⟫_ℝ := by
    have e : ⟪w, (A ^ n) u⟫_ℝ = ‖A‖ ^ n * ‖u‖ ^ 2 + ⟪(A ^ n) w - ‖A‖ ^ n • w, u⟫_ℝ := by
      rw [inner_sub_left, real_inner_smul_left, hwu, pow_sym A hsym]; ring
    have h2 : -(‖(A ^ n) w - ‖A‖ ^ n • w‖ * ‖u‖) ≤ ⟪(A ^ n) w - ‖A‖ ^ n • w, u⟫_ℝ := by
      have := abs_real_inner_le_norm ((A ^ n) w - ‖A‖ ^ n • w) u
      exact (abs_le.mp this).1
    have h3 : ‖(A ^ n) w - ‖A‖ ^ n • w‖ * ‖u‖ ≤ n * η * 1 :=
      mul_le_mul hap hu1 (norm_nonneg _) (by positivity)
    rw [e]; linarith
  -- Cauchy--Schwarz for the form of A^n
  have hcs := cs_form (fun x => (A ^ n) x) (fun x y => map_add _ x y) (fun c x => map_smul _ c x)
    (pow_sym A hsym n) (pow_pos_form A hsym hpos n) w u
  simp only at hcs
  have hcs2 : ⟪w, (A ^ n) u⟫_ℝ ^ 2 ≤ c * (‖A‖ ^ n * ‖u‖ ^ 2) := by
    calc ⟪w, (A ^ n) u⟫_ℝ ^ 2 ≤ ⟪w, (A ^ n) w⟫_ℝ * ⟪u, (A ^ n) u⟫_ℝ := hcs
      _ ≤ ‖A‖ ^ n * (c * ‖u‖ ^ 2) := mul_le_mul hww hup hunn hQ0
      _ = c * (‖A‖ ^ n * ‖u‖ ^ 2) := by ring
  obtain ⟨tt, htt⟩ : ∃ tt : ℝ, tt = ‖A‖ ^ n * ‖u‖ ^ 2 := ⟨_, rfl⟩
  obtain ⟨ee, hee⟩ : ∃ ee : ℝ, ee = (n : ℝ) * η := ⟨_, rfl⟩
  rw [← htt] at hlow hcs2 ⊢
  rw [← hee] at hlow ⊢
  have hee0 : 0 ≤ ee := by rw [hee]; positivity
  have htt0 : 0 ≤ tt := by rw [htt]; positivity
  rcases le_or_lt tt ee with hcase | hcase
  · linarith
  · have hLpos : 0 ≤ tt - ee := by linarith
    have hsq : (tt - ee) ^ 2 ≤ ⟪w, (A ^ n) u⟫_ℝ ^ 2 := pow_le_pow_left₀ hLpos hlow 2
    have hmain : (tt - ee) ^ 2 ≤ c * tt := hsq.trans hcs2
    by_contra! hneg
    have htpos : 0 < tt := by linarith
    have := mul_pos htpos (by linarith : 0 < tt - (c + 2 * ee))
    nlinarith

/-- Pythagoras for the three parts (functions `P`, `B` that are self-adjoint idempotents with
`B P = 0`). -/
theorem pyth (P B : E → E)
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

/-! ## The theorem -/

/-- Refinement with an exceptional set, on any non-zero real inner product space.
`A` is a bounded operator, symmetric, positive, of norm at most one; `P`, `B` are self-adjoint
idempotent maps with `B P = 0`; `G = I - P - B`; `k`, `j`, `m` are natural numbers with
`1 ≤ m`, `j ≤ m`; `γ > 0`. If
 `γ ‖G w‖² ≤ ⟪w, (I - A^{2k}) w⟫`, `‖B A^j B u‖ ≤ κ ‖u‖`, `‖P A^m P u‖ ≤ (1 - b) ‖u‖`
for all vectors, then `(b - κ)/(1 + 2k/(γ m)) ≤ 1 - ‖A‖^m`. -/
theorem refinement_hilbert [Nontrivial E] (A : E →L[ℝ] E)
    (hsym : ∀ x y, ⟪A x, y⟫_ℝ = ⟪x, A y⟫_ℝ) (hpos : ∀ x, 0 ≤ ⟪x, A x⟫_ℝ) (h1 : ‖A‖ ≤ 1)
    (P B : E → E)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x)
    (hBP : ∀ x, B (P x) = 0)
    (k j m : ℕ) (hm : 1 ≤ m) (hjm : j ≤ m) (γ κ b : ℝ) (hγ : 0 < γ)
    (H1 : ∀ w, γ * ‖w - P w - B w‖ ^ 2 ≤ ⟪w, w⟫_ℝ - ⟪w, (A ^ (2 * k)) w⟫_ℝ)
    (H2 : ∀ u, ‖B ((A ^ j) (B u))‖ ≤ κ * ‖u‖)
    (H3 : ∀ u, ‖P ((A ^ m) (P u))‖ ≤ (1 - b) * ‖u‖) :
    (b - κ) / (1 + 2 * (k : ℝ) / (γ * (m : ℝ))) ≤ 1 - ‖A‖ ^ m := by
  obtain ⟨q, hq⟩ : ∃ q : ℝ, q = ‖A‖ := ⟨_, rfl⟩
  have hq0 : 0 ≤ q := by rw [hq]; exact norm_nonneg _
  have hq1 : q ≤ 1 := by rw [hq]; exact h1
  obtain ⟨x, hxdef⟩ : ∃ x : ℝ, x = q ^ m := ⟨_, rfl⟩
  have hmR : (0 : ℝ) < (m : ℝ) := by exact_mod_cast hm
  obtain ⟨r, hrdef⟩ : ∃ r : ℝ, r = 2 * (k : ℝ) / (m : ℝ) := ⟨_, rfl⟩
  have hx0 : 0 ≤ x := by rw [hxdef]; exact pow_nonneg hq0 m
  have hx1 : x ≤ 1 := by rw [hxdef]; exact pow_le_one₀ hq0 hq1
  have hr : 0 ≤ r := by rw [hrdef]; positivity
  have hxr : x ^ r = q ^ (2 * k) := by
    rw [hxdef, hrdef, ← Real.rpow_natCast q m, ← Real.rpow_mul hq0]
    have : (m : ℝ) * (2 * (k : ℝ) / (m : ℝ)) = ((2 * k : ℕ) : ℝ) := by
      push_cast; field_simp
    rw [this, Real.rpow_natCast]
  -- the constant in front of η
  obtain ⟨C, hC⟩ : ∃ C : ℝ, C = 2 * (k : ℝ) / γ + 2 * (j : ℝ) + 2 * (m : ℝ) := ⟨_, rfl⟩
  have hC0 : 0 ≤ C := by rw [hC]; positivity
  have hb : b ≤ 1 - x + x * (1 - x ^ r) / γ + κ := by
    apply le_of_forall_pos_le_add
    intro ε hε
    obtain ⟨η, hηdef⟩ : ∃ η : ℝ, η = ε / (C + 1) := ⟨_, rfl⟩
    have hηpos : 0 < η := by rw [hηdef]; positivity
    have hCη : C * η ≤ ε := by
      rw [hηdef, mul_div_assoc']
      rw [div_le_iff₀ (by linarith)]; nlinarith
    obtain ⟨w, hw1, hw⟩ := exists_approx_eig A hsym hpos h1 η hηpos
    rw [← hq] at hw
    have hw' : ‖A w - ‖A‖ • w‖ ≤ η := by rw [← hq]; exact hw
    -- (A)
    have hA : γ * ‖w - P w - B w‖ ^ 2 ≤ 1 - x ^ r + 2 * (k : ℝ) * η := by
      have h := H1 w
      rw [real_inner_self_eq_norm_sq, hw1] at h
      have hl := quad_lower A h1 w hw1 η hw' (2 * k)
      rw [← hq] at hl
      rw [hxr]; push_cast at hl; linarith
    -- (B)
    obtain ⟨hκ, hB⟩ := proj_step A hsym hpos h1 B hBsa hBid j κ H2 w hw1 η hw'
    -- (P)
    obtain ⟨_, hP⟩ := proj_step A hsym hpos h1 P hPsa hPid m (1 - b) H3 w hw1 η hw'
    rw [← hq] at hB hP
    rw [← hxdef] at hP
    obtain ⟨q1, q2⟩ := pyth P B hPsa hPid hBsa hBid hBP w
    rw [hw1] at q1
    obtain ⟨g, hg⟩ : ∃ g : ℝ, g = ‖w - P w - B w‖ ^ 2 := ⟨_, rfl⟩
    obtain ⟨β, hβ⟩ : ∃ β : ℝ, β = ‖B w‖ ^ 2 := ⟨_, rfl⟩
    obtain ⟨π', hπ⟩ : ∃ π' : ℝ, π' = ‖P w‖ ^ 2 := ⟨_, rfl⟩
    rw [← hg] at hA q2
    rw [← hβ] at hB q2
    rw [← hπ] at hP q1
    have hg0 : 0 ≤ g := by rw [hg]; positivity
    have hβ0 : 0 ≤ β := by rw [hβ]; positivity
    have hη0 : 0 ≤ η := hηpos.le
    have hkη : 0 ≤ 2 * (k : ℝ) * η := by positivity
    have hjη : 0 ≤ 2 * ((j : ℝ) * η) := by positivity
    -- x g
    have hxg : x * g ≤ x * (1 - x ^ r) / γ + 2 * (k : ℝ) / γ * η := by
      have hg' : g ≤ (1 - x ^ r + 2 * (k : ℝ) * η) / γ := by
        rw [le_div_iff₀ hγ]; linarith
      have h2 : x * g ≤ x * ((1 - x ^ r + 2 * (k : ℝ) * η) / γ) :=
        mul_le_mul_of_nonneg_left hg' hx0
      have h3 : x * ((1 - x ^ r + 2 * (k : ℝ) * η) / γ)
          = x * (1 - x ^ r) / γ + x * (2 * (k : ℝ) / γ * η) := by field_simp; ring
      have h4 : x * (2 * (k : ℝ) / γ * η) ≤ 1 * (2 * (k : ℝ) / γ * η) :=
        mul_le_mul_of_nonneg_right hx1 (by positivity)
      linarith
    -- x β
    have hxβ : x * β ≤ κ + 2 * ((j : ℝ) * η) := by
      have hsplit : x = q ^ (m - j) * q ^ j := by
        rw [hxdef, ← pow_add, Nat.sub_add_cancel hjm]
      have hle1 : q ^ (m - j) ≤ 1 := pow_le_one₀ hq0 hq1
      have he0 : 0 ≤ q ^ (m - j) := pow_nonneg hq0 _
      rw [hsplit, mul_assoc]
      calc _ ≤ q ^ (m - j) * (κ + 2 * ((j : ℝ) * η)) := mul_le_mul_of_nonneg_left hB he0
        _ ≤ 1 * (κ + 2 * ((j : ℝ) * η)) := mul_le_mul_of_nonneg_right hle1 (by linarith)
        _ = κ + 2 * ((j : ℝ) * η) := one_mul _
    have hπ' : π' = 1 - g - β := by linarith
    have e1 : x * π' = x - x * g - x * β := by rw [hπ']; ring
    have hfin : b ≤ 1 - x + x * (1 - x ^ r) / γ + κ + C * η := by
      rw [hC]; nlinarith
    linarith
  have := scalar_step b κ γ r x hγ hr hx0 hx1 hb
  have hrr : r / γ = 2 * (k : ℝ) / (γ * (m : ℝ)) := by rw [hrdef, div_div, mul_comm (m : ℝ) γ]
  rw [hrr, hxdef, hq] at this
  exact this

/-- Operator-norm form: `‖A^m w‖ ≤ (1 - (b-κ)_+/(1 + 2k/(γ m))) ‖w‖` for every `w`. -/
theorem refinement_hilbert_norm [Nontrivial E] (A : E →L[ℝ] E)
    (hsym : ∀ x y, ⟪A x, y⟫_ℝ = ⟪x, A y⟫_ℝ) (hpos : ∀ x, 0 ≤ ⟪x, A x⟫_ℝ) (h1 : ‖A‖ ≤ 1)
    (P B : E → E)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x)
    (hBP : ∀ x, B (P x) = 0)
    (k j m : ℕ) (hm : 1 ≤ m) (hjm : j ≤ m) (γ κ b : ℝ) (hγ : 0 < γ)
    (H1 : ∀ w, γ * ‖w - P w - B w‖ ^ 2 ≤ ⟪w, w⟫_ℝ - ⟪w, (A ^ (2 * k)) w⟫_ℝ)
    (H2 : ∀ u, ‖B ((A ^ j) (B u))‖ ≤ κ * ‖u‖)
    (H3 : ∀ u, ‖P ((A ^ m) (P u))‖ ≤ (1 - b) * ‖u‖) (w : E) :
    ‖(A ^ m) w‖ ≤ (1 - max (b - κ) 0 / (1 + 2 * (k : ℝ) / (γ * (m : ℝ)))) * ‖w‖ := by
  have hmn := refinement_hilbert A hsym hpos h1 P B hPsa hPid hBsa hBid hBP k j m hm hjm γ κ b hγ
    H1 H2 H3
  have hx1 : ‖A‖ ^ m ≤ 1 := pow_le_one₀ (norm_nonneg _) h1
  have hposp : max (b - κ) 0 / (1 + 2 * (k : ℝ) / (γ * (m : ℝ))) ≤ 1 - ‖A‖ ^ m := by
    rcases le_total (b - κ) 0 with h0 | h0
    · rw [max_eq_right h0, zero_div]; linarith
    · rw [max_eq_left h0]; exact hmn
  calc ‖(A ^ m) w‖ ≤ ‖A‖ ^ m * ‖w‖ := pow_norm_le A m w
    _ ≤ _ := mul_le_mul_of_nonneg_right (by linarith) (norm_nonneg _)

/-! ## The hypothesis `0 ≤ A ≤ I` in form language -/

/-- A symmetric operator with `0 ≤ ⟪w, A w⟫ ≤ ⟪w, w⟫` has norm at most one. -/
theorem norm_le_one_of_form (A : E →L[ℝ] E)
    (hsym : ∀ x y, ⟪A x, y⟫_ℝ = ⟪x, A y⟫_ℝ) (hpos : ∀ x, 0 ≤ ⟪x, A x⟫_ℝ)
    (hle : ∀ x, ⟪x, A x⟫_ℝ ≤ ⟪x, x⟫_ℝ) : ‖A‖ ≤ 1 := by
  refine A.opNorm_le_bound zero_le_one fun w => ?_
  rw [one_mul]
  have hcs := cs_form (fun x => A x) (fun x y => map_add _ x y) (fun c x => map_smul _ c x)
    hsym hpos (A w) w
  simp only at hcs
  have e1 : ⟪A w, A w⟫_ℝ = ‖A w‖ ^ 2 := real_inner_self_eq_norm_sq _
  have h2 : ⟪A w, A (A w)⟫_ℝ ≤ ‖A w‖ ^ 2 := by
    have := hle (A w); rwa [real_inner_self_eq_norm_sq] at this
  have h3 : ⟪w, A w⟫_ℝ ≤ ‖w‖ ^ 2 := by
    have := hle w; rwa [real_inner_self_eq_norm_sq] at this
  have h4 : 0 ≤ ⟪w, A w⟫_ℝ := hpos w
  have h5 : 0 ≤ ⟪A w, A (A w)⟫_ℝ := hpos (A w)
  rw [e1] at hcs
  have hmain : (‖A w‖ ^ 2) ^ 2 ≤ ‖A w‖ ^ 2 * ‖w‖ ^ 2 :=
    hcs.trans (mul_le_mul h2 h3 h4 (sq_nonneg _))
  rcases (sq_nonneg ‖A w‖).eq_or_lt with h0 | h0
  · have : ‖A w‖ = 0 := by nlinarith [norm_nonneg (A w)]
    rw [this]; exact norm_nonneg _
  · have h6 : ‖A w‖ ^ 2 ≤ ‖w‖ ^ 2 := by
      have : ‖A w‖ ^ 2 * ‖A w‖ ^ 2 ≤ ‖A w‖ ^ 2 * ‖w‖ ^ 2 := by nlinarith
      exact le_of_mul_le_mul_left this h0
    exact (sq_le_sq₀ (norm_nonneg _) (norm_nonneg _)).mp h6

/-- The theorem with the hypothesis `0 ≤ A ≤ I` stated through the quadratic form, as in the
paper. -/
theorem refinement_hilbert_form [Nontrivial E] (A : E →L[ℝ] E)
    (hsym : ∀ x y, ⟪A x, y⟫_ℝ = ⟪x, A y⟫_ℝ) (hpos : ∀ x, 0 ≤ ⟪x, A x⟫_ℝ)
    (hle : ∀ x, ⟪x, A x⟫_ℝ ≤ ⟪x, x⟫_ℝ)
    (P B : E → E)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x)
    (hBP : ∀ x, B (P x) = 0)
    (k j m : ℕ) (hm : 1 ≤ m) (hjm : j ≤ m) (γ κ b : ℝ) (hγ : 0 < γ)
    (H1 : ∀ w, γ * ‖w - P w - B w‖ ^ 2 ≤ ⟪w, w⟫_ℝ - ⟪w, (A ^ (2 * k)) w⟫_ℝ)
    (H2 : ∀ u, ‖B ((A ^ j) (B u))‖ ≤ κ * ‖u‖)
    (H3 : ∀ u, ‖P ((A ^ m) (P u))‖ ≤ (1 - b) * ‖u‖) (w : E) :
    ‖(A ^ m) w‖ ≤ (1 - max (b - κ) 0 / (1 + 2 * (k : ℝ) / (γ * (m : ℝ)))) * ‖w‖ :=
  refinement_hilbert_norm A hsym hpos (norm_le_one_of_form A hsym hpos hle) P B hPsa hPid hBsa hBid
    hBP k j m hm hjm γ κ b hγ H1 H2 H3 w

/-! ## Complex scalars

A complex inner product space is a real inner product space under the real part of its inner
product, with the same norm; the theorem transfers. -/

section ComplexCase
variable {F : Type*} [NormedAddCommGroup F] [InnerProductSpace ℂ F]

theorem restrict_pow (A : F →L[ℂ] F) (n : ℕ) (x : F) :
    ((A.restrictScalars ℝ) ^ n) x = (A ^ n) x := by
  induction n generalizing x with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, pow_succ]
    show ((A.restrictScalars ℝ) ^ n) ((A.restrictScalars ℝ) x) = (A ^ n) (A x)
    rw [ih]; rfl

/-- Refinement with an exceptional set on a non-zero complex inner product space. -/
theorem refinement_complex [Nontrivial F] (A : F →L[ℂ] F)
    (hsym : ∀ x y, ⟪A x, y⟫_ℂ = ⟪x, A y⟫_ℂ) (hpos : ∀ x, 0 ≤ (⟪x, A x⟫_ℂ).re)
    (hle : ∀ x, (⟪x, A x⟫_ℂ).re ≤ ‖x‖ ^ 2)
    (P B : F → F)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℂ = ⟪x, P y⟫_ℂ) (hPid : ∀ x, P (P x) = P x)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℂ = ⟪x, B y⟫_ℂ) (hBid : ∀ x, B (B x) = B x)
    (hBP : ∀ x, B (P x) = 0)
    (k j m : ℕ) (hm : 1 ≤ m) (hjm : j ≤ m) (γ κ b : ℝ) (hγ : 0 < γ)
    (H1 : ∀ w, γ * ‖w - P w - B w‖ ^ 2 ≤ ‖w‖ ^ 2 - (⟪w, (A ^ (2 * k)) w⟫_ℂ).re)
    (H2 : ∀ u, ‖B ((A ^ j) (B u))‖ ≤ κ * ‖u‖)
    (H3 : ∀ u, ‖P ((A ^ m) (P u))‖ ≤ (1 - b) * ‖u‖) (w : F) :
    ‖(A ^ m) w‖ ≤ (1 - max (b - κ) 0 / (1 + 2 * (k : ℝ) / (γ * (m : ℝ)))) * ‖w‖ := by
  letI : InnerProductSpace ℝ F := InnerProductSpace.rclikeToReal ℂ F
  have hin : ∀ x y : F, ⟪x, y⟫_ℝ = (⟪x, y⟫_ℂ).re := fun x y => real_inner_eq_re_inner ℂ x y
  have hA : ∀ x, (A.restrictScalars ℝ) x = A x := fun x => rfl
  have hre : ∀ x : F, (((‖x‖ : ℝ) : ℂ) ^ 2).re = ‖x‖ ^ 2 := fun x => by
    rw [← Complex.ofReal_pow]; exact Complex.ofReal_re _
  have := refinement_hilbert_form (A.restrictScalars ℝ)
    (fun x y => by rw [hin, hin, hA, hA, hsym])
    (fun x => by rw [hin, hA]; exact hpos x)
    (fun x => by
      rw [hin, hin, hA, inner_self_eq_norm_sq_to_K]
      refine (hle x).trans_eq ?_
      norm_cast)
    P B
    (fun x y => by rw [hin, hin, hPsa]) hPid
    (fun x y => by rw [hin, hin, hBsa]) hBid hBP k j m hm hjm γ κ b hγ
    (fun w => by
      rw [hin, hin, restrict_pow, inner_self_eq_norm_sq_to_K]
      refine (H1 w).trans_eq ?_
      congr 1
      norm_cast)
    (fun u => by rw [restrict_pow]; exact H2 u)
    (fun u => by rw [restrict_pow]; exact H3 u) w
  rwa [restrict_pow] at this

end ComplexCase

end RefinementHilbert

#print axioms RefinementHilbert.refinement_hilbert
#print axioms RefinementHilbert.refinement_hilbert_norm
#print axioms RefinementHilbert.exists_approx_eig
#print axioms RefinementHilbert.proj_step
#print axioms RefinementHilbert.refinement_hilbert_form
#print axioms RefinementHilbert.refinement_complex
