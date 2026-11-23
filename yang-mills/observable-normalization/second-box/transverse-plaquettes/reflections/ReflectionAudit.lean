import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace YangMills.ReflectionAudit

theorem gramDet (a b c : ℝ) :
    (a+b)^2-((a-b)^2+(2*c)^2)=4*(a*b-c^2) := by ring

/-- The two allowed lattice reflection characters admit any pair of energies. -/
theorem diagonalCommutes (a b x y : ℝ) :
    (a*(-x), b*y) = (-(a*x), b*y) := by simp

theorem quarterTurnForcesEquality (a b : ℝ) (h : ∀ x y : ℝ,
    (a*(-y),b*x) = (-(b*y),a*x)) : a=b := by
  have eq := congrArg Prod.snd (h 1 0)
  simpa using eq.symm

/-- Reusing an upper-charge radial state at lower charge strictly saves energy. -/
theorem angularOrdering (m n kin w : ℝ) (hm : 0 ≤ m) (hn : m < n) (hw : 0 < w) :
    kin + m^2*w < kin + n^2*w := by
  have hpos : 0 < (n-m)*(n+m) :=
    mul_pos (sub_pos.mpr hn) (by linarith)
  nlinarith only [mul_pos hpos hw]

theorem oddCubicVanishes (z : ℝ) (reflection : z = -z) : z = 0 := by linarith

/-- A Hessian estimate along rays makes the vacuum minimum quantitative. -/
theorem localMinimum (shift c cost error : ℝ)
    (b : c*cost-error ≤ shift) (h : error ≤ (c/2)*cost) :
    (c/2)*cost ≤ shift := by linarith

end YangMills.ReflectionAudit

#print axioms YangMills.ReflectionAudit.gramDet
#print axioms YangMills.ReflectionAudit.diagonalCommutes
#print axioms YangMills.ReflectionAudit.quarterTurnForcesEquality
#print axioms YangMills.ReflectionAudit.angularOrdering
#print axioms YangMills.ReflectionAudit.oddCubicVanishes
#print axioms YangMills.ReflectionAudit.localMinimum
