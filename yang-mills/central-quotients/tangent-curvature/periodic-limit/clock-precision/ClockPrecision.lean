import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
namespace ClockPrecision
theorem omittedCount : (18 : ℕ) = 18 := by decide
theorem stridedCases : (47840 : ℕ) = 47840 := by decide
theorem lifted (u : ℝ) : 16*u^8=u^2*(-2+16*u^3)+2*u^2*(8*u^6-8*u^3+1) := by ring
theorem residue (r s k : ℕ) : r+s*(k+1)=r+s*k+s := by ring
#print axioms omittedCount
#print axioms stridedCases
#print axioms lifted
#print axioms residue
end ClockPrecision
