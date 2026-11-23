import Mathlib.Data.Real.Basic
import Mathlib.Analysis.Convex.Jensen
import Mathlib.Analysis.Convex.Mul
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace YangMills.Observable

/-- Squared fundamental trace-gradient in SU(2) quaternion coordinates. -/
theorem traceGradient {a b c d : ℝ}
    (unit : a^2+b^2+c^2+d^2 = 1) :
    (-b)^2 + (-c)^2 + (-d)^2 = 1 - (2*a)^2/4 := by
  linarith only [unit]

/-- Chain rule factor for the adjoint character A=F²−1. -/
theorem adjointGradient (F : ℝ) :
    (2*F)^2 * (1-F^2/4) = ((F^2-1)+1)*(3-(F^2-1)) := by ring

/-- Jensen's bound on the transfer spectral measure normalized to unit mass. -/
theorem normalizedStepBound {ι : Type*} (s : Finset ι) (p x : ι → ℝ)
    (hp : ∀ i ∈ s, 0 ≤ p i) (sum : ∑ i ∈ s, p i = 1)
    (hx : ∀ i ∈ s, 0 ≤ x i) (k : ℕ) :
    (1 - ∑ i ∈ s, p i * (1 - x i)) ^ k ≤ ∑ i ∈ s, p i * x i ^ k := by
  have he : (∑ i ∈ s, p i * (1 - x i)) = 1 - ∑ i ∈ s, p i * x i := by
    simp only [mul_sub, mul_one, Finset.sum_sub_distrib, sum]
  rw [he, sub_sub_cancel]
  simpa only [smul_eq_mul] using
    (convexOn_pow (𝕜 := ℝ) k).map_sum_le hp sum (p := x) hx

/-- A one-atom transfer distribution attains the normalized bound. -/
theorem singleAtomStep (x : ℝ) (k : ℕ) : (1 - (1 - x)) ^ k = x ^ k := by
  rw [sub_sub_cancel]

end YangMills.Observable
#print axioms YangMills.Observable.traceGradient
#print axioms YangMills.Observable.adjointGradient
#print axioms YangMills.Observable.normalizedStepBound
#print axioms YangMills.Observable.singleAtomStep
