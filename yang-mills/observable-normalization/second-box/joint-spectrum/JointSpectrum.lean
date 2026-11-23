import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace YangMills.JointSpectrum

theorem meanVariance (s h : ℝ) (hh : h ≠ 0) (scale : s^2=h^3) :
    s^2/(8*h^2)=h/8 := by
  rw [scale]
  field_simp
  ring

theorem matrixDilation (k v : ℝ) :
    4*k/16+16*v/16=(k/2+2*v)/2 := by ring

/-- An orbit tilt linear in the background enters the transverse curl squared
only quadratically on this two-site lattice. -/
theorem transverseCurl (s q t a b w : ℝ) :
    (s+t^2*a)*(q+t^2*b)-(t*w)^2-s*q =
    t^2*(a*q+s*b+t^2*a*b-w^2) := by ring

theorem sumDifference (u v k l : ℝ) :
    (u+k)^2+(v+l)^2-(u^2+v^2)=2*(u*k+v*l)+(k^2+l^2) := by ring

/-- Separate ordered energy bounds do not give a lower bound for a difference. -/
theorem trialOrdering : ∃ (a₀ a₁ u₀ u₁ : ℝ), a₀ < a₁ ∧ a₀ ≤ u₀ ∧ a₁ ≤ u₁ ∧
    a₁-a₀ < u₁-u₀ := by
  exact ⟨0,1,1,3,by norm_num,by norm_num,by norm_num,by norm_num⟩

/-- Equal cross terms among eight image vectors, each normalized by 1/√8. -/
theorem centerAverage (diagonal off : ℝ) :
    (8*diagonal+56*off)/8=diagonal+7*off := by ring

end YangMills.JointSpectrum

#print axioms YangMills.JointSpectrum.meanVariance
#print axioms YangMills.JointSpectrum.matrixDilation
#print axioms YangMills.JointSpectrum.transverseCurl
#print axioms YangMills.JointSpectrum.sumDifference
#print axioms YangMills.JointSpectrum.trialOrdering
#print axioms YangMills.JointSpectrum.centerAverage
