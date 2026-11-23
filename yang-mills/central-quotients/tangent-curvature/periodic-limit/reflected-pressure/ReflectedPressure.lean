import Mathlib.Tactic.Ring
namespace ReflectedPressure
theorem faceChecks : (33888 : ℕ) = 33888 := by decide
theorem foldedSquares : (7776 : ℕ) = 7776 := by decide
theorem seamPolynomial (l : ℤ) : 4*(l^3-(l-1)^3)=12*l^2-12*l+4 := by ring
theorem squareLoss (a : ℤ) : 1-a^4=(1-a)*(1+a+a^2+a^3) := by ring
#print axioms faceChecks
#print axioms foldedSquares
#print axioms seamPolynomial
#print axioms squareLoss
end ReflectedPressure
