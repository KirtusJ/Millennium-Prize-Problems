/-
Inheritance.lean -- f2-lean (task T238). Formalisation of the algebraic core of
target/inheritance.md ("Refinement with an exceptional set of coarse fields").
Every declaration proves exactly its displayed type; see report.md for the inventory.
-/
import Mathlib

namespace F2Lean
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

/-- L1c: with `x = e^{-tλ}` and `r = 2a/t`, `x^r = e^{-2aλ}` (`t ≠ 0`). -/
theorem exp_rpow_ratio (t a lam : ℝ) (ht : t ≠ 0) :
    exp (-t * lam) ^ (2 * a / t) = exp (-(2 * a) * lam) := by
  rw [← Real.exp_mul]; congr 1; field_simp; ring

/-! ## L2  accumulation on real sequences
Indexing: `M n = ∏_{j<n} K (j+1) = K_1 ⋯ K_n`, `M 0 = 1`; the sum over `i ∈ range n`
is the text's sum over `i+1 = 1..n`, with weight `M i = M_{(i+1)-1}`. -/

/-- `M n = K_1 ⋯ K_n`. -/
def M (K : ℕ → ℝ) (n : ℕ) : ℝ := ∏ j ∈ Finset.range n, K (j + 1)

theorem M_pos (K : ℕ → ℝ) (hK : ∀ i, 0 < K (i + 1)) (n : ℕ) : 0 < M K n :=
  Finset.prod_pos fun j _ => hK j

/-- L2 (multiplied form). Only `K_i > 0` is assumed; no sign condition on `κ_i, ε_i`. -/
theorem accum_mul (d b K κ ε : ℕ → ℝ) (hK : ∀ i, 0 < K (i + 1))
    (hd : ∀ i, (b (i + 1) - κ (i + 1)) / K (i + 1) ≤ d (i + 1))
    (hb : ∀ i, d i - ε (i + 1) ≤ b (i + 1)) (n : ℕ) :
    d 0 - ∑ i ∈ Finset.range n, M K i * (ε (i + 1) + κ (i + 1)) ≤ M K n * d n := by
  induction n with
  | zero => simp [M]
  | succ n ih =>
    have hMn := M_pos K hK n
    have h1 : b (n + 1) - κ (n + 1) ≤ K (n + 1) * d (n + 1) := by
      have := hd n; rw [div_le_iff₀ (hK n)] at this; linarith
    have h2 : d n - (ε (n + 1) + κ (n + 1)) ≤ K (n + 1) * d (n + 1) := by
      have := hb n; linarith
    have h3 := mul_le_mul_of_nonneg_left h2 hMn.le
    have hM : M K (n + 1) = M K n * K (n + 1) := Finset.prod_range_succ _ _
    rw [Finset.sum_range_succ, hM]
    nlinarith

/-- L2 (divided form): `d_n ≥ M_n^{-1} (d_0 - Σ_{i=1}^n M_{i-1}(ε_i + κ_i))`. -/
theorem accum (d b K κ ε : ℕ → ℝ) (hK : ∀ i, 0 < K (i + 1))
    (hd : ∀ i, (b (i + 1) - κ (i + 1)) / K (i + 1) ≤ d (i + 1))
    (hb : ∀ i, d i - ε (i + 1) ≤ b (i + 1)) (n : ℕ) :
    (d 0 - ∑ i ∈ Finset.range n, M K i * (ε (i + 1) + κ (i + 1))) / M K n ≤ d n := by
  rw [div_le_iff₀ (M_pos K hK n), mul_comm]; exact accum_mul d b K κ ε hK hd hb n

/-- L2 (positive-part form), with the text's hypothesis `d_i ≥ (b_i - κ_i)_+ / K_i` and `d_0 ≥ 0`. -/
theorem accum_pos (d b K κ ε : ℕ → ℝ) (hK : ∀ i, 0 < K (i + 1))
    (hd : ∀ i, max (b (i + 1) - κ (i + 1)) 0 / K (i + 1) ≤ d (i + 1))
    (hd0 : 0 ≤ d 0)
    (hb : ∀ i, d i - ε (i + 1) ≤ b (i + 1)) (n : ℕ) :
    max (d 0 - ∑ i ∈ Finset.range n, M K i * (ε (i + 1) + κ (i + 1))) 0 / M K n ≤ d n := by
  have hd' : ∀ i, (b (i + 1) - κ (i + 1)) / K (i + 1) ≤ d (i + 1) := fun i =>
    le_trans (div_le_div_of_nonneg_right (le_max_left _ _) (hK i).le) (hd i)
  have hdn : 0 ≤ d n := by
    cases n with
    | zero => exact hd0
    | succ m => exact le_trans (div_nonneg (le_max_right _ _) (hK m).le) (hd m)
  rcases le_total (d 0 - ∑ i ∈ Finset.range n, M K i * (ε (i + 1) + κ (i + 1))) 0 with h | h
  · rw [max_eq_right h, zero_div]; exact hdn
  · rw [max_eq_left h]; exact accum d b K κ ε hK hd' hb n

/-! ## L3  finite-dimensional operator version
Spectral data as interface: an orthonormal basis `e` of a finite-dimensional real inner
product space with eigenvalues `lam i`; `S s w := Σ_i e^{-s lam_i} ⟪e_i, w⟫ e_i`. -/

set_option linter.unusedSectionVars false
variable {ι E : Type*} [Fintype ι] [DecidableEq ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- the semigroup `S_s = e^{-sH}` defined from spectral data -/
noncomputable def S (e : OrthonormalBasis ι ℝ E) (lam : ι → ℝ) (s : ℝ) (w : E) : E :=
  ∑ i, (exp (-s * lam i) * ⟪e i, w⟫_ℝ) • e i

theorem S_quad (e : OrthonormalBasis ι ℝ E) (lam : ι → ℝ) (s : ℝ) (w : E) :
    ⟪w, S e lam s w⟫_ℝ = ∑ i, exp (-s * lam i) * ⟪e i, w⟫_ℝ ^ 2 := by
  unfold S; rw [inner_sum]; refine Finset.sum_congr rfl fun i _ => ?_
  rw [inner_smul_right, real_inner_comm]; ring

/-- spectral lower bound `S_s ⪰ e^{-s lam_{i0}} e_{i0} e_{i0}^*` (rank-one `E`) -/
theorem S_lower (e : OrthonormalBasis ι ℝ E) (lam : ι → ℝ) (s : ℝ) (i0 : ι) (w : E) :
    exp (-s * lam i0) * ⟪e i0, w⟫_ℝ ^ 2 ≤ ⟪w, S e lam s w⟫_ℝ := by
  rw [S_quad]
  exact Finset.single_le_sum (f := fun i => exp (-s * lam i) * ⟪e i, w⟫_ℝ ^ 2)
    (fun i _ => by positivity) (Finset.mem_univ i0)

theorem S_eig_quad (e : OrthonormalBasis ι ℝ E) (lam : ι → ℝ) (s : ℝ) (i0 : ι) :
    ⟪e i0, S e lam s (e i0)⟫_ℝ = exp (-s * lam i0) := by
  rw [S_quad, Finset.sum_eq_single i0]
  · rw [real_inner_self_eq_norm_sq, e.orthonormal.1 i0]; ring
  · intro i _ hi; rw [e.orthonormal.2 hi]; ring
  · simp

/-- `‖S_t w‖ ≤ e^{-t lam_{i0}} ‖w‖` when `lam_{i0}` is the smallest eigenvalue and `t ≥ 0`;
with `S_t e_{i0} = e^{-t lam_{i0}} e_{i0}` this identifies `‖S_t‖ = e^{-t lam_{i0}}`. -/
theorem S_norm_le (e : OrthonormalBasis ι ℝ E) (lam : ι → ℝ) (t : ℝ) (ht : 0 ≤ t) (i0 : ι)
    (hmin : ∀ i, lam i0 ≤ lam i) (w : E) :
    ‖S e lam t w‖ ≤ exp (-t * lam i0) * ‖w‖ := by
  have hsq : ‖S e lam t w‖ ^ 2 = ∑ i, (exp (-t * lam i) * ⟪e i, w⟫_ℝ) ^ 2 := by
    rw [← real_inner_self_eq_norm_sq]; unfold S
    rw [e.orthonormal.inner_sum]; simp [pow_two]
  have hpar : ‖w‖ ^ 2 = ∑ i, ⟪e i, w⟫_ℝ ^ 2 := by
    rw [← real_inner_self_eq_norm_sq, ← e.sum_inner_mul_inner w w]
    refine Finset.sum_congr rfl fun i _ => ?_; rw [real_inner_comm]; ring
  have hle : ‖S e lam t w‖ ^ 2 ≤ (exp (-t * lam i0) * ‖w‖) ^ 2 := by
    rw [hsq, mul_pow, hpar, Finset.mul_sum]
    refine Finset.sum_le_sum fun i _ => ?_
    rw [mul_pow]
    have : exp (-t * lam i) ≤ exp (-t * lam i0) := by
      apply Real.exp_le_exp.mpr; nlinarith [hmin i]
    have h0 : 0 ≤ exp (-t * lam i) := (exp_pos _).le
    exact mul_le_mul_of_nonneg_right (pow_le_pow_left₀ h0 this 2) (sq_nonneg _)
  exact (sq_le_sq₀ (norm_nonneg _) (by positivity)).mp hle

theorem S_eig (e : OrthonormalBasis ι ℝ E) (lam : ι → ℝ) (s : ℝ) (i0 : ι) :
    S e lam s (e i0) = exp (-s * lam i0) • e i0 := by
  unfold S; rw [Finset.sum_eq_single i0]
  · rw [real_inner_self_eq_norm_sq, e.orthonormal.1 i0]; simp
  · intro i _ hi; rw [e.orthonormal.2 hi]; simp
  · simp

/-- Deduction (B): from `‖B S_τ B‖ ≤ κ` (stated pointwise) and `S_τ ⪰ e^{-τ λ} vv^*`,
`e^{-τ λ} ‖B v‖² ≤ κ` for the unit eigenvector `v = e_{i0}`. Also yields `0 ≤ κ`. -/
theorem B_step (e : OrthonormalBasis ι ℝ E) (lam : ι → ℝ) (i0 : ι) (B : E →ₗ[ℝ] E)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x) (τ κ : ℝ)
    (h2 : ∀ u, ‖B (S e lam τ (B u))‖ ≤ κ * ‖u‖) :
    0 ≤ κ ∧ exp (-τ * lam i0) * ‖B (e i0)‖ ^ 2 ≤ κ := by
  set v := e i0
  have hv : ‖v‖ = 1 := e.orthonormal.1 i0
  have hκ : 0 ≤ κ := by have := h2 v; rw [hv, mul_one] at this; exact (norm_nonneg _).trans this
  refine ⟨hκ, ?_⟩
  set u := B v
  have hβ : ⟪v, u⟫_ℝ = ‖u‖ ^ 2 := by
    rw [← real_inner_self_eq_norm_sq]; show ⟪v, B v⟫_ℝ = ⟪B v, B v⟫_ℝ
    rw [hBsa, hBid]
  have hlow := S_lower e lam τ i0 u
  rw [hβ] at hlow
  have hup : ⟪u, S e lam τ u⟫_ℝ ≤ κ * ‖u‖ ^ 2 := by
    have : ⟪u, S e lam τ u⟫_ℝ = ⟪u, B (S e lam τ (B u))⟫_ℝ := by
      have hu : B u = u := hBid v
      rw [← hBsa, hu]
    rw [this]
    calc _ ≤ ‖u‖ * ‖B (S e lam τ (B u))‖ := real_inner_le_norm _ _
      _ ≤ ‖u‖ * (κ * ‖u‖) := mul_le_mul_of_nonneg_left (h2 u) (norm_nonneg _)
      _ = κ * ‖u‖ ^ 2 := by ring
  have hc : 0 < exp (-τ * lam i0) := exp_pos _
  rcases (sq_nonneg ‖u‖).eq_or_lt with h0 | h0
  · rw [← h0, mul_zero]; exact hκ
  · have : exp (-τ * lam i0) * ‖u‖ ^ 2 * ‖u‖ ^ 2 ≤ κ * ‖u‖ ^ 2 := by nlinarith
    exact le_of_mul_le_mul_right this h0

/-- Deduction (P): from `‖P S_t P‖ ≤ 1 - b` (pointwise) and `S_t ⪰ e^{-t λ} vv^*`,
`e^{-tλ} ‖P v‖² ≤ 1 - b` for `v = e_{i0}`. -/
theorem P_step (e : OrthonormalBasis ι ℝ E) (lam : ι → ℝ) (i0 : ι) (P : E →ₗ[ℝ] E)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x) (t b : ℝ)
    (h3 : ∀ u, ‖P (S e lam t (P u))‖ ≤ (1 - b) * ‖u‖) :
    exp (-t * lam i0) * ‖P (e i0)‖ ^ 2 ≤ 1 - b := by
  obtain ⟨hκ, h⟩ := B_step e lam i0 P hPsa hPid t (1 - b) h3
  exact h

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

/-- L3 MAIN. Finite-dimensional operator version of the gated inequality, for ANY eigen-index
`i0` with `lam ≥ 0`; with `i0` the smallest eigenvalue the left side `1 - e^{-t lam_{i0}}` is
`d = 1 - ‖S_t‖` (see `S_norm_le`, `S_eig`). Hypotheses:
 `h1` : `γ ‖G w‖² ≤ ⟪w, (I - S_{2a}) w⟫` for all `w` (form inequality `I - S_{2a} ⪰ γ G`, G = Q - B),
 `h2` : `‖B S_τ B u‖ ≤ κ ‖u‖` for all `u` (i.e. `‖B S_τ B‖ ≤ κ`),
 `h3` : `‖P S_t P u‖ ≤ (1-b) ‖u‖` for all `u` (i.e. `‖P S_t P‖ ≤ 1 - b`). -/
theorem gated_main (e : OrthonormalBasis ι ℝ E) (lam : ι → ℝ) (hlam : ∀ i, 0 ≤ lam i) (i0 : ι)
    (P B : E →ₗ[ℝ] E)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x)
    (hBP : ∀ x, B (P x) = 0)
    (a t τ γ κ b : ℝ) (ha : 0 ≤ a) (ht : 0 < t) (hτt : τ ≤ t) (hγ : 0 < γ)
    (h1 : ∀ w, γ * ‖w - P w - B w‖ ^ 2 ≤ ⟪w, w⟫_ℝ - ⟪w, S e lam (2 * a) w⟫_ℝ)
    (h2 : ∀ u, ‖B (S e lam τ (B u))‖ ≤ κ * ‖u‖)
    (h3 : ∀ u, ‖P (S e lam t (P u))‖ ≤ (1 - b) * ‖u‖) :
    (b - κ) / (1 + 2 * a / (γ * t)) ≤ 1 - exp (-t * lam i0) := by
  set v := e i0 with hvdef
  have hv : ‖v‖ = 1 := e.orthonormal.1 i0
  set x := exp (-t * lam i0) with hxdef
  set r := 2 * a / t with hrdef
  have hx0 : 0 ≤ x := (exp_pos _).le
  have hx1 : x ≤ 1 := by
    rw [hxdef]; apply Real.exp_le_one_iff.mpr; nlinarith [hlam i0]
  have hr : 0 ≤ r := by positivity
  -- (A) short-time form at v
  have hA : γ * ‖v - P v - B v‖ ^ 2 ≤ 1 - x ^ r := by
    have := h1 v
    rw [real_inner_self_eq_norm_sq, hv, hvdef, S_eig_quad] at this
    rw [hrdef, hxdef, exp_rpow_ratio t a (lam i0) ht.ne']; simpa using this
  -- (B)
  obtain ⟨hκ, hB⟩ := B_step e lam i0 B hBsa hBid τ κ h2
  -- (P)
  have hP : x * ‖P v‖ ^ 2 ≤ 1 - b := P_step e lam i0 P hPsa hPid t b h3
  -- (Q)
  obtain ⟨q1, q2⟩ := pyth P B hPsa hPid hBsa hBid hBP v
  rw [hv] at q1
  set g := ‖v - P v - B v‖ ^ 2
  set β := ‖B v‖ ^ 2
  have hg : x * g ≤ x * (1 - x ^ r) / γ := by
    rw [mul_div_assoc]; apply mul_le_mul_of_nonneg_left _ hx0
    rw [le_div_iff₀ hγ]; linarith
  have hxβ : x * β ≤ κ := by
    have hsplit : x = exp (-(t - τ) * lam i0) * exp (-τ * lam i0) := by
      rw [hxdef, ← Real.exp_add]; ring_nf
    have hle1 : exp (-(t - τ) * lam i0) ≤ 1 := by
      apply Real.exp_le_one_iff.mpr; nlinarith [hlam i0]
    have he0 : 0 ≤ exp (-(t - τ) * lam i0) := (exp_pos _).le
    rw [hsplit, mul_assoc]
    calc _ ≤ exp (-(t - τ) * lam i0) * κ := mul_le_mul_of_nonneg_left hB he0
      _ ≤ 1 * κ := mul_le_mul_of_nonneg_right hle1 hκ
      _ = κ := one_mul κ
  have hb : b ≤ 1 - x + x * (1 - x ^ r) / γ + κ := by
    have h' : ‖P v‖ ^ 2 = 1 - g - β := by linarith
    have e1 : x * ‖P v‖ ^ 2 = x - x * g - x * β := by rw [h']; ring
    linarith
  have := scalar_step b κ γ r x hγ hr hx0 hx1 hb
  have hrr : r / γ = 2 * a / (γ * t) := by rw [hrdef, div_div, mul_comm t γ]
  rwa [hrr] at this

/-- L3 COMPOSED, operator-norm form of the text's conclusion. With `lam_{i0}` the smallest
eigenvalue: for every `w`, `‖S_t w‖ ≤ (1 - (b-κ)_+/(1 + 2a/(γt))) ‖w‖`, i.e.
`d = 1 - ‖S_t‖ ≥ (b-κ)_+/(1+2a/(γt))` (and `S_eig` shows the bound `‖S_t‖ ≤ e^{-tλ}` is attained). -/
theorem gated_main_norm (e : OrthonormalBasis ι ℝ E) (lam : ι → ℝ) (hlam : ∀ i, 0 ≤ lam i) (i0 : ι)
    (hmin : ∀ i, lam i0 ≤ lam i)
    (P B : E →ₗ[ℝ] E)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x)
    (hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ) (hBid : ∀ x, B (B x) = B x)
    (hBP : ∀ x, B (P x) = 0)
    (a t τ γ κ b : ℝ) (ha : 0 ≤ a) (ht : 0 < t) (hτt : τ ≤ t) (hγ : 0 < γ)
    (h1 : ∀ w, γ * ‖w - P w - B w‖ ^ 2 ≤ ⟪w, w⟫_ℝ - ⟪w, S e lam (2 * a) w⟫_ℝ)
    (h2 : ∀ u, ‖B (S e lam τ (B u))‖ ≤ κ * ‖u‖)
    (h3 : ∀ u, ‖P (S e lam t (P u))‖ ≤ (1 - b) * ‖u‖) (w : E) :
    ‖S e lam t w‖ ≤ (1 - max (b - κ) 0 / (1 + 2 * a / (γ * t))) * ‖w‖ := by
  have hm := gated_main e lam hlam i0 P B hPsa hPid hBsa hBid hBP a t τ γ κ b ha ht hτt hγ h1 h2 h3
  have hx1 : exp (-t * lam i0) ≤ 1 := by
    apply Real.exp_le_one_iff.mpr; nlinarith [hlam i0]
  have hpos : max (b - κ) 0 / (1 + 2 * a / (γ * t)) ≤ 1 - exp (-t * lam i0) := by
    rcases le_total (b - κ) 0 with h0 | h0
    · rw [max_eq_right h0, zero_div]; linarith
    · rw [max_eq_left h0]; exact hm
  calc ‖S e lam t w‖ ≤ exp (-t * lam i0) * ‖w‖ := S_norm_le e lam t ht.le i0 hmin w
    _ ≤ _ := mul_le_mul_of_nonneg_right (by linarith) (norm_nonneg _)

/-! ## L4  reset-process example (3 states, weights `p, p, 1-2p`) -/

/-- stationary weights -/
noncomputable def piw (p : ℝ) : Fin 3 → ℝ := ![p, p, 1 - 2 * p]
/-- `𝔼 f = Σ π_i f_i` -/
noncomputable def Ex (p : ℝ) (f : Fin 3 → ℝ) : ℝ := ∑ i, piw p i * f i
/-- reset semigroup `S_t f = e^{-ℓt} f + (1 - e^{-ℓt}) 𝔼 f` -/
noncomputable def Sreset (p ℓ t : ℝ) (f : Fin 3 → ℝ) : Fin 3 → ℝ :=
  fun i => exp (-ℓ * t) * f i + (1 - exp (-ℓ * t)) * Ex p f
/-- the signed difference of the two fine labels on the event `A = {0,1}` -/
def fsig : Fin 3 → ℝ := ![1, -1, 0]

/-- L4: for every `p` (no condition on the mass of `A` is used), `fsig` is centered, has zero
coarse mean on `A` (`p f_0 + p f_1 = 0`), vanishes off `A`, `S_t fsig = e^{-ℓt} fsig`, and the
`L²(π)` Rayleigh quotient `⟪f, S_t f⟫_π = e^{-ℓt} ⟪f, f⟫_π` with `⟪f,f⟫_π = 2p`. Moreover
`S_t g = e^{-ℓt} g` for every centered `g`, so on the centered space `S_t = e^{-ℓt} I`. -/
theorem reset_example (p ℓ t : ℝ) :
    Ex p fsig = 0 ∧ p * fsig 0 + p * fsig 1 = 0 ∧ fsig 2 = 0 ∧
    Sreset p ℓ t fsig = (fun i => exp (-ℓ * t) * fsig i) ∧
    (∑ i, piw p i * fsig i * Sreset p ℓ t fsig i) = exp (-ℓ * t) * (∑ i, piw p i * fsig i ^ 2) ∧
    (∑ i, piw p i * fsig i ^ 2) = 2 * p ∧
    (∀ g : Fin 3 → ℝ, Ex p g = 0 → Sreset p ℓ t g = (fun i => exp (-ℓ * t) * g i)) := by
  have hE : Ex p fsig = 0 := by simp [Ex, piw, fsig, Fin.sum_univ_three]
  have hS : Sreset p ℓ t fsig = fun i => exp (-ℓ * t) * fsig i := by
    funext i; simp [Sreset, hE]
  refine ⟨hE, by simp [fsig], by simp [fsig], hS, ?_, ?_, ?_⟩
  · rw [hS]; simp [piw, fsig, Fin.sum_univ_three]; ring
  · simp [piw, fsig, Fin.sum_univ_three]; ring
  · intro g hg; funext i; simp [Sreset, hg]

end F2Lean

#print axioms F2Lean.xr_le
#print axioms F2Lean.scalar_step
#print axioms F2Lean.scalar_step_pos
#print axioms F2Lean.exp_rpow_ratio
#print axioms F2Lean.accum_mul
#print axioms F2Lean.accum
#print axioms F2Lean.accum_pos
#print axioms F2Lean.S_quad
#print axioms F2Lean.S_lower
#print axioms F2Lean.S_eig_quad
#print axioms F2Lean.S_norm_le
#print axioms F2Lean.S_eig
#print axioms F2Lean.B_step
#print axioms F2Lean.P_step
#print axioms F2Lean.pyth
#print axioms F2Lean.gated_main
#print axioms F2Lean.gated_main_norm
#print axioms F2Lean.reset_example
