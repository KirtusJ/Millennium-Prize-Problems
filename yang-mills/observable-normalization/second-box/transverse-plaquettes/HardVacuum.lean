import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace YangMills.HardVacuum

/-- Nonconstant Fourier modes of the three-component curl. -/
theorem curlSymbol (p q r x y z : ℝ) :
    (p*y-q*x)^2+(p*z-r*x)^2+(q*z-r*y)^2 =
    (p^2+q^2+r^2)*(x^2+y^2+z^2)-(p*x+q*y+r*z)^2 := by ring

theorem hardCount : 3*2*(3+3+1) = 42 := by decide

/-- Inversion annihilates a first-order diagonal matrix element. -/
theorem parityCancellation (m : ℝ) (odd : m = -m) : m=0 := by linarith

/-- All linear color-invariant covectors vanish, tested against two half turns. -/
theorem invariantLinear (a b c : ℝ) (h1 : b = -b ∧ c = -c) (h2 : a = -a) :
    a = 0 ∧ b = 0 ∧ c = 0 := by
  obtain ⟨hb,hc⟩ := h1
  exact ⟨by linarith, by linarith, by linarith⟩

/-- A complementary spectral gap absorbs first-order off-diagonal coupling. -/
theorem rayleighCost (t d b e : ℝ) (hd : 0 < d)
    (h : e ≤ 2*b*t-d*t^2) : d*e ≤ b^2 := by
  have hmul := mul_le_mul_of_nonneg_left h hd.le
  nlinarith only [hmul, sq_nonneg (d*t-b)]

theorem softScale (h : ℝ) (hh : h ≠ 0) : h^3 * (1/h)^2 = h := by
  field_simp
  ring

/-- Numerator of the moving-plane diagonal coefficient after multiplying by √3. -/
theorem positiveCurvature (u v : ℝ) (hu : 0 < u) (hv : 0 < v)
    (two : u^2 = 2) (six : v^2 = 6) : 0 < v-u-1 := by
  have small : u < 3/2 := by
    by_contra! bad
    nlinarith only [two, mul_nonneg (sub_nonneg.mpr bad) (show 0 ≤ u+3/2 by linarith)]
  by_contra! bad
  have q := mul_nonneg (show 0 ≤ u+1-v by linarith) (show 0 ≤ u+1+v by linarith)
  nlinarith only [q, small, two, six]

/-- Scalar color component of the fixed-plane quadratic form. -/
theorem fixedCurvature (x y z : ℝ) :
    -4*(x^2+y^2+z^2) + x*y+x*z+y*z ≤ -3*(x^2+y^2+z^2) := by
  nlinarith only [sq_nonneg (x-y), sq_nonneg (x-z), sq_nonneg (y-z)]

end YangMills.HardVacuum
#print axioms YangMills.HardVacuum.curlSymbol
#print axioms YangMills.HardVacuum.hardCount
#print axioms YangMills.HardVacuum.parityCancellation
#print axioms YangMills.HardVacuum.invariantLinear
#print axioms YangMills.HardVacuum.rayleighCost
#print axioms YangMills.HardVacuum.softScale

#print axioms YangMills.HardVacuum.positiveCurvature
#print axioms YangMills.HardVacuum.fixedCurvature
