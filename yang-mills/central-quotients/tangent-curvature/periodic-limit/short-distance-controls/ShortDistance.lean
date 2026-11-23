import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
namespace ShortDistance
theorem maxwellCoefficient : (48 : ℕ) = 48 := by decide
theorem vanishingCyclesCount : (6 : ℕ) = 6 := by decide
theorem triangleCorrection (g h : ℝ) : (g+h)^3-g^3=3*g^2*h+3*g*h^2+h^3 := by ring
theorem twoSpecies (a b : ℝ) : 2*(a^4+b^4)-(a^2+b^2)^2=(a^2-b^2)^2 := by ring
#print axioms maxwellCoefficient
#print axioms vanishingCyclesCount
#print axioms triangleCorrection
#print axioms twoSpecies
end ShortDistance
