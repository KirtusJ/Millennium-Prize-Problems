import Mathlib.Tactic.NormNum
namespace HaarClover
theorem centerCount : (1536 : ℕ) = 1536 := by decide
theorem siteCount : (48 : ℕ) = 48 := by decide
theorem contact : (48:ℚ)*3/4096 = 9/256 := by norm_num
theorem quadratic : (48:ℚ)*((1/4-1/8)/(4*256)-(3/4096)/4) = -3/1024 := by norm_num
#print axioms centerCount
#print axioms siteCount
#print axioms contact
#print axioms quadratic
end HaarClover
