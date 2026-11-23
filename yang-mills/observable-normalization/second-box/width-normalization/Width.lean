import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace Width
theorem inversionCount : (170 : Nat) = 170 := by decide
theorem covarianceCorrection (v k : ℝ) : (1-5*k*v)-(1-3*k*v) = -2*k*v := by ring
theorem holonomyVariance (L : ℝ) : (2*L)^2*L=4*L^3 := by ring
#print axioms inversionCount
#print axioms covarianceCorrection
#print axioms holonomyVariance
end Width
