import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Topology.Algebra.Order.Field
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace YangMills.ToronExcitation

theorem fiberScale (b d m r : ℝ) (h : b*d^2=m) :
    m*b*r^2*d^2=(m*r)^2 := by
  calc
    _=m*r^2*(b*d^2) := by ring
    _=_ := by rw [h]; ring

theorem coarseDefect (u v : ℝ) (hu : u ≤ 1) (hv : 0 ≤ v) :
    1-v ≤ 1-u*v := by nlinarith only [mul_nonneg (sub_nonneg.mpr hu) hv]

theorem weightLoss (a : ℝ) (ha : 0 ≤ a) (hb : a ≤ 1) :
    (1-a)^2 ≤ 1-a^2 := by nlinarith only [mul_nonneg ha (sub_nonneg.mpr hb)]

theorem scaleKinetic (h : ℝ) : h^3*h^2=h*(h^2)^2 := by ring
theorem scaleQuartic (h : ℝ) : h^4=h^3*h := by ring

theorem separation (e0 e1 a0 a1 eta : ℝ) (l : e1-eta ≤ a1)
    (u : a0 ≤ e0+eta) : e1-e0-2*eta ≤ a1-a0 := by linarith

/-- Once both scaled levels converge, a strictly positive limiting
separation supplies a lower bound along the entire sequence. -/
theorem eventualGap (a b : ℕ → ℝ) (u v : ℝ) (hu : Filter.Tendsto a Filter.atTop (nhds u))
    (hv : Filter.Tendsto b Filter.atTop (nhds v)) (hlt : u < v) :
    ∀ᶠ n in Filter.atTop, (v-u)/2 < b n-a n := by
  have pos : (v-u)/2 < v-u := by linarith
  exact (hv.sub hu).eventually (lt_mem_nhds pos)

end YangMills.ToronExcitation
#print axioms YangMills.ToronExcitation.fiberScale
#print axioms YangMills.ToronExcitation.coarseDefect
#print axioms YangMills.ToronExcitation.weightLoss
#print axioms YangMills.ToronExcitation.scaleKinetic
#print axioms YangMills.ToronExcitation.scaleQuartic
#print axioms YangMills.ToronExcitation.separation
#print axioms YangMills.ToronExcitation.eventualGap
