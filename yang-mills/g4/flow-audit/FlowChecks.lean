import Mathlib.Analysis.SpecialFunctions.Trigonometric.Bounds
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Deriv
import Mathlib.Analysis.Calculus.Deriv.MeanValue
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum

namespace Millennium.G4.FlowChecks
open Real Set

/-- Expose the cost of the one omitted temporal layer, in log variables. -/
theorem partition_cost (den num z w C loss copies : ℝ) (hn : 0 < copies)
    (lower : z-C ≤ den) (upper : num ≤ w-w/copies)
    (layer : -w ≤ loss) :
    num-den ≤ (w-z)+C+loss/copies := by
  have h := div_le_div_of_nonneg_right layer hn.le
  rw [neg_div] at h
  linarith

/-- Peeling a periodic direction from dimension d+2, with l+1 layers and
s+1 sites in a slice, leaves the correct bulk, seam and base counts. -/
theorem seam_count (d l s : ℕ) :
    (d+1)*(s+1)*l + s + d*s + (d+1) = (d+1)*((l+1)*(s+1)) := by ring

/-- Stability of n steps with local error a. For K=1+Lh the power K^n
is bounded by exp(Lnh), independently of the number of links. -/
theorem accumulated_error (e : ℕ → ℝ) (K a : ℝ) (hK : 1 ≤ K) (ha : 0 ≤ a)
    (h0 : e 0 ≤ 0) (step : ∀ n, e (n+1) ≤ K*e n+a) (n : ℕ) :
    e n ≤ (n : ℝ)*a*K^n := by
  induction n with
  | zero => simpa using h0
  | succ n ih =>
    have hn : 1 ≤ K^(n+1) := one_le_pow₀ hK
    calc
      e (n+1) ≤ K*((n : ℝ)*a*K^n)+a :=
        (step n).trans (add_le_add_right (mul_le_mul_of_nonneg_left ih (by linarith)) _)
      _ ≤ K*((n : ℝ)*a*K^n)+a*K^(n+1) := by
        have := mul_le_mul_of_nonneg_left hn ha
        linarith
      _ = _ := by push_cast; rw [pow_succ]; ring

-- NATIVE CHILD 1
theorem cos_quartic_upper (x : ℝ) : cos x ≤ 1 - x^2/2 + x^4/24 := by
  have d1 (y : ℝ) : HasDerivAt (fun t : ℝ => t^3/6-t+sin t) (y^2/2-1+cos y) y := by
    convert (((((hasDerivAt_id y).pow 3).div_const 6).sub (hasDerivAt_id y)).add
      (Real.hasDerivAt_sin y)) using 1 <;> dsimp <;> ring
  have mono := monotone_of_hasDerivAt_nonneg d1 (fun y => by
    dsimp; linarith [Real.one_sub_sq_div_two_le_cos (x := y)])
  have d2 (y : ℝ) :
      HasDerivAt (fun t : ℝ => 1 - t^2/2 + t^4/24 - cos t) (y^3/6-y+sin y) y := by
    convert ((((hasDerivAt_const y (1:ℝ)).sub (((hasDerivAt_id y).pow 2).div_const 2)).add
      (((hasDerivAt_id y).pow 4).div_const 24)).sub (Real.hasDerivAt_cos y)) using 1
      <;> dsimp <;> ring
  have half (y : ℝ) (hy : 0 ≤ y) : cos y ≤ 1-y^2/2+y^4/24 := by
    have m := monotoneOn_of_hasDerivWithinAt_nonneg (convex_Ici (0:ℝ))
      (fun t _ => (d2 t).continuousAt.continuousWithinAt)
      (fun t _ => (d2 t).hasDerivWithinAt) (fun t ht => by
        have ht' : 0 ≤ t := interior_subset ht
        simpa using mono ht')
    have hm := m (left_mem_Ici : (0:ℝ) ∈ Ici 0) hy hy
    exact sub_nonneg.mp (show 0 ≤ 1-y^2/2+y^4/24-cos y by simpa using hm)
  rcases le_total 0 x with h | h
  · exact half x h
  · simpa [show (-x)^4=x^4 by ring] using half (-x) (neg_nonneg.mpr h)

theorem reflected_difference (u : ℝ) :
    cos (2*u) - 2*cos (3*u) + cos (4*u) = -2*cos (3*u)*(1-cos u) := by
  have h := Real.cos_add_cos (2*u) (4*u)
  rw [show (2*u+4*u)/2=3*u by ring, show (2*u-4*u)/2 = -u by ring, Real.cos_neg] at h
  linarith

theorem pointwise_upper (u : ℝ) :
    cos (2*u) - 2*cos (3*u) + cos (4*u) ≤ -u^2 + (55/12)*u^4 := by
  rw [reflected_difference]
  have h1 := mul_le_mul_of_nonneg_right (Real.one_sub_sq_div_two_le_cos (x := 3*u))
    (sub_nonneg.mpr (Real.cos_le_one u))
  have h2 := mul_le_mul_of_nonneg_left
    (show 1-cos u ≤ u^2/2 by linarith [Real.one_sub_sq_div_two_le_cos (x := u)])
    (sq_nonneg u)
  nlinarith [cos_quartic_upper u]

-- NATIVE CHILD 2
/-- Integrating the pointwise bound against the two independent temporal frequencies. -/
theorem negative_form (m₂ m₄ form : ℝ) (hm : 0 < m₂) (small : m₄ < m₂/20)
    (fourth : m₂^2 ≤ m₄)
    (estimate : form ≤ -(2*m₂) + (55/12)*(2*m₄+6*m₂^2)) :
    form < -m₂/6 ∧ form < 0 := by
  constructor <;> linarith

#print axioms partition_cost
#print axioms seam_count
#print axioms accumulated_error
#print axioms cos_quartic_upper
#print axioms reflected_difference
#print axioms pointwise_upper
#print axioms negative_form

end Millennium.G4.FlowChecks
