import Mathlib

/-! u1-gapB (T174): scalar cores of the corner absorption in Lemma tu:L-S4 (S4-alg). -/

/-- Weighted AM-GM step: for 0 < γ < 1, k = 1/(1-γ), c > 0,
  P x^γ ≤ γ c x + (1-γ) (P c^{-γ})^{k}.  Stated with v := (P c^{-γ})^{1/(1-γ)} given. -/
theorem amgm_step (x c v γ : ℝ) (hx : 0 ≤ x) (hc : 0 ≤ c) (hv : 0 ≤ v)
    (hγ0 : 0 ≤ γ) (hγ1 : γ ≤ 1) :
    (c * x) ^ γ * v ^ (1 - γ) ≤ γ * (c * x) + (1 - γ) * v :=
  Real.geom_mean_le_arith_mean2_weighted hγ0 (by linarith) (mul_nonneg hc hx) hv (by ring)

/-- The corner combination.  Q stands for P x^γ.
  Slice y = 0: a(1-x) + Q ≤ 1 - m0, from Q ≤ a1 x + R, a ≤ a1 = 1 - 2 m0, R ≤ m0.
  Slice y = 1: Q + b ≤ 1 - m1, from Q ≤ m1, b ≤ 1 - 2 m1.
  F is affine in y, so F ≤ 1 - min m0 m1. -/
theorem corner (a a1 b x y Q R m0 m1 : ℝ)
    (hx0 : 0 ≤ x) (hx1 : x ≤ 1) (hy0 : 0 ≤ y) (hy1 : y ≤ 1)
    (ha : 0 ≤ a) (haa : a ≤ a1) (hQ0 : Q ≤ a1 * x + R) (hR : R ≤ m0)
    (ha1 : a1 = 1 - 2 * m0) (hQ1 : Q ≤ m1) (hb : b ≤ 1 - 2 * m1) (hm1 : 0 ≤ m1) :
    a * (1 - x) * (1 - y) + Q + b * y ≤ 1 - min m0 m1 := by
  have hmin0 : min m0 m1 ≤ m0 := min_le_left _ _
  have hmin1 : min m0 m1 ≤ m1 := min_le_right _ _
  -- slice y = 0
  have s0 : a * (1 - x) + Q ≤ 1 - m0 := by
    have : a * (1 - x) ≤ a1 * (1 - x) := mul_le_mul_of_nonneg_right haa (by linarith)
    nlinarith
  -- slice y = 1
  have s1 : Q + b ≤ 1 - m1 := by linarith
  have e : a * (1 - x) * (1 - y) + Q + b * y
      = (1 - y) * (a * (1 - x) + Q) + y * (Q + b) := by ring
  rw [e]
  have h1 : (1 - y) * (a * (1 - x) + Q) ≤ (1 - y) * (1 - min m0 m1) :=
    mul_le_mul_of_nonneg_left (by linarith) (by linarith)
  have h2 : y * (Q + b) ≤ y * (1 - min m0 m1) :=
    mul_le_mul_of_nonneg_left (by linarith) hy0
  nlinarith

/-- Strip a₂ < ℓ: F(x,y) ≤ F(x,0) + y·b with b ≤ 1, y ≤ yβ. -/
theorem strip (a b x y Q m0 yb : ℝ) (hx1 : x ≤ 1) (hy0 : 0 ≤ y) (hyb : y ≤ yb)
    (ha : 0 ≤ a) (hb : b ≤ 1) (hb0 : 0 ≤ b) (hs0 : a * (1 - x) + Q ≤ 1 - m0) :
    a * (1 - x) * (1 - y) + Q + b * y ≤ 1 - m0 + yb := by
  have : 0 ≤ a * (1 - x) * y := mul_nonneg (mul_nonneg ha (by linarith)) hy0
  have : b * y ≤ yb := by nlinarith
  nlinarith

/-- Error absorption: if F ≤ 1 - u and δ ≤ u with 0 ≤ u, then e^δ F ≤ 1 (for F ≥ 0). -/
theorem absorb (F u δ : ℝ) (hF0 : 0 ≤ F) (hF : F ≤ 1 - u) (hδ : δ ≤ u) :
    Real.exp δ * F ≤ 1 := by
  have h1 : Real.exp δ ≤ Real.exp u := Real.exp_le_exp.mpr hδ
  have h2 : 1 - u ≤ Real.exp (-u) := by linarith [Real.add_one_le_exp (-u)]
  have h3 : Real.exp u * Real.exp (-u) = 1 := by rw [← Real.exp_add]; simp
  have hF' : F ≤ Real.exp (-u) := le_trans hF h2
  calc Real.exp δ * F ≤ Real.exp u * F := mul_le_mul_of_nonneg_right h1 hF0
    _ ≤ Real.exp u * Real.exp (-u) := mul_le_mul_of_nonneg_left hF' (Real.exp_pos u).le
    _ = 1 := h3

/-- Corner bound on D: e is 2-Lipschitz-type step  S - s ≤ (S^2 - s^2)/(2 s). -/
theorem sq_step (S s : ℝ) (hs : 0 < s) (hS : s ≤ S) : S - s ≤ (S ^ 2 - s ^ 2) / (2 * s) := by
  rw [le_div_iff₀ (by linarith)]
  nlinarith [sq_nonneg (S - s)]

#print axioms amgm_step
#print axioms corner
#print axioms strip
#print axioms absorb
#print axioms sq_step
