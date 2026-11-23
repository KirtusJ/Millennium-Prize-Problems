import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
namespace FullGap
theorem polynomialOffset : (20261022 : ℚ)/120000000000 < 17/100000 := by norm_num
theorem orientedGram (u v w : ℚ) : (1-u^2)*(1-v^2)-(w-u*v)^2=1+2*u*v*w-u^2-v^2-w^2 := by ring
theorem oddFold (p q : ℚ) (hq : 0<q) : p-q<p+q := by linarith
theorem neutralSeparation : (19472 : ℚ)/1000000 < 195/10000 := by norm_num
#print axioms polynomialOffset
#print axioms orientedGram
#print axioms oddFold
#print axioms neutralSeparation
end FullGap
