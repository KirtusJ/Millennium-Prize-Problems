import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace PhysicalScalar
theorem affineIntercept (a b c f : ℝ) : c*(a+b*f)-f*(a+b*c)=(c-f)*a := by ring
theorem quadraticError (k c f : ℝ) : c*(k*f^2)-f*(k*c^2)= -(c-f)*k*c*f := by ring
theorem inverseSideResidual : (20 : Nat)*847-12*840 = 6860 := by decide
#print axioms affineIntercept
#print axioms quadraticError
#print axioms inverseSideResidual
end PhysicalScalar
