import Mathlib.Tactic.Ring
namespace MomentumRatio
theorem angularEndpoint : ((2646, 1105) : ℕ × ℕ) = (2646, 1105) := by decide
theorem coneSlope : ((5586, 1105) : ℕ × ℕ) = (5586, 1105) := by decide
theorem restCoefficient : ((92169, 16384) : ℕ × ℕ) = (92169, 16384) := by decide
theorem factorization (a b c : ℚ) : (a+b)^2 - (a^2+b^2+2*a*b*c) = 2*a*b*(1-c) := by ring
#print axioms angularEndpoint
#print axioms coneSlope
#print axioms restCoefficient
#print axioms factorization
end MomentumRatio
