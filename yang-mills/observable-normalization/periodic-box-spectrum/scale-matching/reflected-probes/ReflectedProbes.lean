import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace ReflectedProbes
theorem reflectedGram (x y u v : ℝ) : (x^2+y^2)*(u^2+v^2)-(x*u+y*v)^2=(x*v-y*u)^2 := by ring
theorem splitCross (a b c d e f : ℝ) : (a+d)*(c+f)-(b+e)^2-(a*c-b^2)-(d*f-e^2)=a*f+d*c-2*b*e := by ring
theorem rectangle : (2287 : Nat)^2 > 29865 * 175 := by decide
#print axioms reflectedGram
#print axioms splitCross
#print axioms rectangle
end ReflectedProbes
