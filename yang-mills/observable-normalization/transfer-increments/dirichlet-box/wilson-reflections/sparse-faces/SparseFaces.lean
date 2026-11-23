import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace YangMills.SparseFaces

/-- Cauchy for the chord lengths of the five complementary faces. -/
theorem fiveChord (a b c d e : ℝ) :
    (a+b+c+d+e)^2 ≤ 5*(a^2+b^2+c^2+d^2+e^2) := by
  nlinarith only [sq_nonneg (a-b), sq_nonneg (a-c), sq_nonneg (a-d),
    sq_nonneg (a-e), sq_nonneg (b-c), sq_nonneg (b-d), sq_nonneg (b-e),
    sq_nonneg (c-d), sq_nonneg (c-e), sq_nonneg (d-e)]

/-- Each of four complementary disks pays one fifth of the central deficit. -/
theorem cubeBudget (s A B C D : ℝ) (ha : s ≤ 5*A) (hb : s ≤ 5*B)
    (hc : s ≤ 5*C) (hd : s ≤ 5*D) :
    9*s ≤ 5*(s+A+B+C+D) := by linarith

theorem pressureReserve (S P l : ℝ) (hl : 0 ≤ l) (h : 9*P ≤ 5*S) :
    (1-5*l/9)*S ≤ S-l*P := by
  nlinarith only [mul_nonneg hl (sub_nonneg.mpr h)]

theorem positiveReserve (l : ℝ) (h : l < 9/5) : 0 < 1-5*l/9 := by
  linarith

theorem endpointSlack : (1 : ℝ) < 3/2 ∧ (3/2 : ℝ) < 9/5 := by
  constructor <;> linarith

theorem densityExponent : (4:ℕ)^4*9=2*1152 := by decide

end YangMills.SparseFaces
#print axioms YangMills.SparseFaces.fiveChord
#print axioms YangMills.SparseFaces.cubeBudget
#print axioms YangMills.SparseFaces.pressureReserve
#print axioms YangMills.SparseFaces.positiveReserve
#print axioms YangMills.SparseFaces.endpointSlack
#print axioms YangMills.SparseFaces.densityExponent
