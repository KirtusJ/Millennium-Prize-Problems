import Mathlib

-- Director Z4, 23 November 2026: placed in namespace R12Vol when added to the library (the worker's file had none).
namespace R12Vol

/-- x^2/(x+y) ≥ x - y  (used for |p_perp|^4/|p|^2 ≥ p1^2+p2^2-p3^2). -/
theorem sq_div_ge (x y : ℝ) (hx : 0 ≤ x) (hy : 0 ≤ y) (h : 0 < x + y) :
    x - y ≤ x ^ 2 / (x + y) := by
  rw [le_div_iff₀ h]; nlinarith [sq_nonneg y]

/-- (P+A)^2 - 4C ≥ (P-A)^2 when C ≤ P*A  (C = (p_perp·a_perp)^2 ≤ |p_perp|^2 |a_perp|^2). -/
theorem perp_prod (P A C : ℝ) (hC : C ≤ P * A) :
    (P - A) ^ 2 ≤ (P + A) ^ 2 - 4 * C := by nlinarith

/-- (X - a)^2 ≥ X^2 - 2 X a for X, a ≥ 0. -/
theorem sq_sub_ge (X a : ℝ) (hX : 0 ≤ X) (ha : 0 ≤ a) : X ^ 2 - 2 * X * a ≤ (X - a) ^ 2 := by
  nlinarith [sq_nonneg a]

/-- Pair-bound core: X = |p_perp|^2 ≤ R = |p|^2, q2 = |q|^2, numerator M ≥ X^2 - X q2/2,
    0 < W ≤ R + q2/4 (W = |u||w|), M ≥ 0.  Then M / W ≥ X^2/R - (3/4) q2. -/
theorem pair_core (X R q2 M W : ℝ) (hX : 0 ≤ X) (hXR : X ≤ R) (hR : 0 < R) (hq : 0 ≤ q2)
    (hM : X ^ 2 - X * q2 / 2 ≤ M) (hM0 : 0 ≤ M) (hW : 0 < W) (hWR : W ≤ R + q2 / 4) :
    X ^ 2 / R - 3 / 4 * q2 ≤ M / W := by
  have h1 : M / (R + q2 / 4) ≤ M / W := by
    apply div_le_div_of_nonneg_left hM0 hW hWR
  have h2 : X ^ 2 / R - 3 / 4 * q2 ≤ M / (R + q2 / 4) := by
    have hRq : 0 < R + q2 / 4 := by linarith
    rw [le_div_iff₀ hRq]
    have hXR2 : X ^ 2 ≤ R ^ 2 := by nlinarith
    have e : (X ^ 2 / R - 3 / 4 * q2) * (R + q2 / 4)
        = X ^ 2 + X ^ 2 / R * (q2 / 4) - 3 / 4 * q2 * R - 3 / 16 * q2 ^ 2 := by
      field_simp; ring
    rw [e]
    have hdiv : X ^ 2 / R ≤ R := by rw [div_le_iff₀ hR]; nlinarith
    have hXq : X * q2 / 2 ≤ R * q2 / 2 := by nlinarith
    nlinarith [mul_le_mul_of_nonneg_right hdiv (by linarith : (0:ℝ) ≤ q2 / 4), sq_nonneg q2]
  linarith

/-- e^{-x} (A - B q) ≥ A - (B + x' ) q style step: for x = s q ≥ 0 and A - B q ≥ 0, A ≥ 0:
    exp(-s q) (A - B q) ≥ A - (B + s A) q. -/
theorem gauss_lin (s q A B : ℝ) (hs : 0 ≤ s) (hq : 0 ≤ q) (hB : 0 ≤ B) (hAB : 0 ≤ A - B * q) :
    A - (B + s * A) * q ≤ Real.exp (-(s * q)) * (A - B * q) := by
  have he : 1 - s * q ≤ Real.exp (-(s * q)) := by
    have := Real.add_one_le_exp (-(s * q)); linarith
  have hsq : 0 ≤ s * q := mul_nonneg hs hq
  nlinarith [mul_le_mul_of_nonneg_right he hAB, mul_nonneg (mul_nonneg hs hB) (sq_nonneg q)]

/-- Jensen for a finite positive measure (the step C(t) ≥ C(0) exp(-t M1/M0)):
    for weights w_i ≥ 0 with sum M0 > 0, sum w_i exp(-t E_i) ≥ M0 exp(-t (sum w_i E_i)/M0). -/
theorem jensen_exp {ι : Type*} (S : Finset ι) (w E : ι → ℝ) (t : ℝ) (hw : ∀ i ∈ S, 0 ≤ w i)
    (hM : 0 < ∑ i ∈ S, w i) :
    (∑ i ∈ S, w i) * Real.exp (-t * ((∑ i ∈ S, w i * E i) / ∑ i ∈ S, w i))
      ≤ ∑ i ∈ S, w i * Real.exp (-t * E i) := by
  set M := ∑ i ∈ S, w i
  set m := (∑ i ∈ S, w i * E i) / M
  -- tangent line: exp(y) ≥ exp(c)(1 + y - c)
  have key : ∀ i ∈ S, w i * (Real.exp (-t * m) * (1 + (-t * E i) - (-t * m)))
      ≤ w i * Real.exp (-t * E i) := by
    intro i hi
    apply mul_le_mul_of_nonneg_left _ (hw i hi)
    have := Real.add_one_le_exp (-t * E i - -t * m)
    rw [Real.exp_sub] at this
    have hpos := Real.exp_pos (-t * m)
    calc Real.exp (-t * m) * (1 + -t * E i - -t * m)
        = Real.exp (-t * m) * ((-t * E i - -t * m) + 1) := by ring
      _ ≤ Real.exp (-t * m) * (Real.exp (-t * E i) / Real.exp (-t * m)) :=
          mul_le_mul_of_nonneg_left this hpos.le
      _ = Real.exp (-t * E i) := by field_simp
  have hsum := Finset.sum_le_sum key
  have hlhs : ∑ i ∈ S, w i * (Real.exp (-t * m) * (1 + (-t * E i) - (-t * m)))
      = Real.exp (-t * m) * M + (-t * Real.exp (-t * m)) * (∑ i ∈ S, w i * E i)
        + (t * m * Real.exp (-t * m)) * M := by
    simp only [M]
    rw [Finset.mul_sum, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib,
      ← Finset.sum_add_distrib]
    apply Finset.sum_congr rfl; intro i _; ring
  have hmM : m * M = ∑ i ∈ S, w i * E i := by
    simp only [m]; field_simp
  have : Real.exp (-t * m) * M + (-t * Real.exp (-t * m)) * (∑ i ∈ S, w i * E i)
        + (t * m * Real.exp (-t * m)) * M = M * Real.exp (-t * m) := by
    rw [← hmM]; ring
  rw [hlhs, this] at hsum
  exact hsum

#print axioms sq_div_ge
#print axioms perp_prod
#print axioms sq_sub_ge
#print axioms pair_core
#print axioms gauss_lin
#print axioms jensen_exp

end R12Vol
