import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Abel
import Mathlib.Algebra.BigOperators.Group.Finset.Basic

namespace YangMills.ToronVacuum

theorem twoStep (lo mid hi x : ℝ) (rec : lo-hi=x*mid)
    (h : hi ≤ mid) (hx : 0 ≤ x) : (1+x)*hi ≤ lo := by
  nlinarith only [mul_nonneg hx (sub_nonneg.mpr h), rec]

theorem fundamental (q z b : ℝ) (h : z ≤ q) (hb : 0 < b)
    (rec : b*(1-z)=4*q) (hq : q ≤ 1) : b*(1-q) ≤ 4 := by
  nlinarith only [rec, mul_nonneg hb.le (sub_nonneg.mpr h), hq]

theorem productScale (m b d : ℝ) (h : b*d^2=m) :
    m*b^2*d^4=m^3 := by
  calc
    m*b^2*d^4=m*(b*d^2)^2 := by ring
    _=m^3 := by rw [h]; ring

theorem occupation (survival cost fraction : ℝ) (h : survival ≤ 1-cost*fraction)
    (hc : 0 ≤ cost) (hf : 1/6 ≤ fraction) : survival ≤ 1-cost/6 := by
  nlinarith only [h, mul_nonneg hc (sub_nonneg.mpr hf)]

theorem superSolution (phi Kphi V e m : ℝ) (hm : 0 < m)
    (bound : phi ≤ m) (he : 0 ≤ e) (hV : 0 ≤ V)
    (tel : e*(1+V) ≤ (1+V)*phi-Kphi) :
    e*phi ≤ m*((1+V)*phi-Kphi) := by
  nlinarith only [mul_nonneg he (sub_nonneg.mpr bound),
    mul_nonneg hm.le (sub_nonneg.mpr tel), mul_nonneg (mul_nonneg hm.le he) hV]


/-- Summing survival iterates produces a supersolution when a whole
block loses mass. No independence between times is used. -/
theorem finiteSurvival {G : Type*} [AddCommGroup G] (B : G →+ G)
    (u : ℕ → G) (step : ∀ i, B (u i) = u (i+1)) (m : ℕ) :
    (∑ i ∈ Finset.range m, u i) - B (∑ i ∈ Finset.range m, u i) =
    u 0 - u m := by
  induction m with
  | zero => simp
  | succ m ih =>
    rw [Finset.sum_range_succ, map_add, step]
    calc
      _ = ((∑ i ∈ Finset.range m, u i) - B (∑ i ∈ Finset.range m, u i)) +
          u m - u (m+1) := by abel
      _ = _ := by rw [ih]; abel

end YangMills.ToronVacuum
#print axioms YangMills.ToronVacuum.twoStep
#print axioms YangMills.ToronVacuum.fundamental
#print axioms YangMills.ToronVacuum.productScale
#print axioms YangMills.ToronVacuum.occupation
#print axioms YangMills.ToronVacuum.superSolution
#print axioms YangMills.ToronVacuum.finiteSurvival
