import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
namespace StaticFloor
theorem odd_orbit (d : ℚ) : d^2+(-d)^2+0^2 = 2*d^2 := by ring
theorem share : let floor : ℚ := 250/1000000; let rem : ℚ := 2/10000000000; 999999/1000000 < floor/(floor+rem) := by norm_num
theorem constant_cancels (d : ℚ) : -d+(13/3)*d-(13/3)*d+d=0 := by ring
theorem signed_share : (74:ℚ)/100 < 1132/(1132+391) := by norm_num
#print axioms signed_share
#print axioms odd_orbit
#print axioms share
#print axioms constant_cancels
end StaticFloor
