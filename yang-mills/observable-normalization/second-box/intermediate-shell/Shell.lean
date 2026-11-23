import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace Shell
theorem cells : (4095 : Nat) = 4095 := by decide
theorem oscillator (p q : ℝ) : (p^2+q^2)^2-(q^2-p^2)^2=4*p^2*q^2 := by ring
theorem cutoff (a b c d : ℝ) : (a-c)^2+(b-d)^2=(a^2+b^2)+(c^2+d^2)-2*(a*c+b*d) := by ring
#print axioms cells
#print axioms oscillator
#print axioms cutoff
end Shell
