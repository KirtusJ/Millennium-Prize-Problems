import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic.NormNum

namespace YangMills.WindingCount

def rank (l : ℕ) := l^2 * (2*l).choose l + l^3*(l-1)

theorem sideFour : rank 4 = 1312 := by decide

theorem sideFive : rank 5 = 6800 := by decide

theorem sideSix : rank 6 = 34344 := by decide

end YangMills.WindingCount
#print axioms YangMills.WindingCount.sideFour
#print axioms YangMills.WindingCount.sideFive
#print axioms YangMills.WindingCount.sideSix
