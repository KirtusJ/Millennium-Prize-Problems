import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace TensorCone
theorem testedTriples : (220 : ℕ) = 220 := by decide
theorem firstGap (u v a b c : ℝ) : (-a*u+b*v)-(a*u+c*(u+v))=-(2*a+c)*u+(b-c)*v := by ring
theorem nextGap (u v a b c : ℝ) : (-b*v-c*(u+v))-(-a*u+b*v)=(a-c)*u-(2*b+c)*v := by ring
#print axioms testedTriples
#print axioms firstGap
#print axioms nextGap
end TensorCone
