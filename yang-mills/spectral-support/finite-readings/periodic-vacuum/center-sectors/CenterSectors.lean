import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
namespace CenterSectors
theorem chebyshev_tail : (2:ℚ)/20000 * (6^19/121645100408832000) / (1-6/20) < 1/1000000 := by norm_num
theorem occupation : let s : ℚ := 3*(494/532)^48; 78/1000 < s/(1+s) := by norm_num
theorem contrast_gate : (2730:ℚ)/100000 < 7/100 := by norm_num
theorem band_margin : (155:ℚ)/1000 < 278/1000 - (318/1000000)/(3199/100000) - (708/1000)*(353/1000000)/(226/100000) := by norm_num
#print axioms band_margin
#print axioms chebyshev_tail
#print axioms occupation
#print axioms contrast_gate
end CenterSectors
