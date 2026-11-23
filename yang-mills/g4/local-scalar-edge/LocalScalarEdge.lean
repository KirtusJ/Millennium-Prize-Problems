import Mathlib.Analysis.Complex.AbsMax
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

open MeasureTheory
open scoped BigOperators

namespace Millennium.G4.LocalScalarEdge

/-- Transport a boundary estimate through a Taylor zero of known order.
The analytic quotient is supplied by the removable singularity argument. -/
theorem disk_zero_bound (f h : ℂ → ℂ) (r M : ℝ) (n : ℕ) (hr : 0 < r)
    (hd : DiffContOnCl ℂ h (Metric.ball 0 r))
    (fac : ∀ w ∈ Metric.closedBall 0 r, f w = w^n * h w)
    (bound : ∀ w ∈ Metric.sphere 0 r, ‖f w‖ ≤ M)
    (z : ℂ) (hz : z ∈ Metric.closedBall 0 r) :
    ‖f z‖ ≤ ‖z‖^n * (M / r^n) := by
  have hh : ‖h z‖ ≤ M / r^n := by
    apply Complex.norm_le_of_forall_mem_frontier_norm_le Metric.isBounded_ball hd
    · rw [frontier_ball (0 : ℂ) hr.ne']
      intro w hw
      have hn : ‖w‖ = r := by simpa [dist_zero_right] using Metric.mem_sphere.mp hw
      have hfw := bound w hw
      rw [fac w (Metric.sphere_subset_closedBall hw), norm_mul, norm_pow, hn] at hfw
      exact (le_div_iff₀ (pow_pos hr n)).2 (by simpa [mul_comm] using hfw)
    · rwa [closure_ball (0 : ℂ) hr.ne']
  rw [fac z hz, norm_mul, norm_pow]
  exact mul_le_mul_of_nonneg_left hh (by positivity)

/-- A positive filter charges at least its threshold times the wrong-branch weight.
Here w can be the indicator of that branch against the spectral measure. -/
theorem filter_weight {X : Type*} [MeasurableSpace X] (μ : Measure X)
    (w f : X → ℝ) (a : ℝ) (ha : 0 < a) (hw : Integrable w μ) (hf : Integrable f μ)
    (h : ∀ᵐ x ∂μ, a * w x ≤ f x) :
    (∫ x, w x ∂μ) ≤ (∫ x, f x ∂μ) / a := by
  apply (le_div_iff₀ ha).2
  rw [mul_comm, ← integral_const_mul]
  exact integral_mono_ae (hw.const_mul a) hf h

/-- The squared polynomial is bounded below on a separated upper branch. -/
theorem separated_filter (x b d : ℝ) (hx : 1/2 ≤ x) (hd : 0 ≤ d)
    (h : d ≤ b-x) : (1/2 : ℝ)^8 * d^2 ≤ x^8 * (x-b)^2 := by
  have hpow : (1/2 : ℝ)^8 ≤ x^8 := pow_le_pow_left₀ (by norm_num) hx 8
  have hs : d^2 ≤ (b-x)^2 := pow_le_pow_left₀ hd h 2
  have ht : d^2 ≤ (x-b)^2 := by nlinarith only [hs]
  exact mul_le_mul hpow ht (sq_nonneg _) (by positivity)

/-- A first moment forces mass into the upper cluster. -/
theorem upper_cluster_floor (m lo hi : ℝ) (h₁ : 3/4 ≤ m)
    (h₂ : m ≤ lo + 2 * hi) (h₃ : lo ≤ 1/4) : 1/4 ≤ hi := by
  linarith

-- NATIVE CHILD 1
/-- Average over all momentum modes, retaining a measured subset. -/
theorem momentum_mass {I : Type*} [Fintype I] (s : Finset I) (w : I → ℝ)
    (a : ℝ) (hw : ∀ i, 0 ≤ w i) (hs : ∀ i ∈ s, a ≤ w i) :
    (s.card : ℝ) * a ≤ ∑ i, w i := by
  classical
  calc
    (s.card : ℝ) * a = ∑ _i ∈ s, a := by simp
    _ ≤ ∑ i ∈ s, w i := Finset.sum_le_sum hs
    _ ≤ ∑ i, w i := Finset.sum_le_sum_of_subset_of_nonneg
      (Finset.subset_univ s) (fun i _ _ => hw i)

/-- An upper dispersion bound confines every state in the window. -/
theorem window_radius (x b err width stiffness ksq : ℝ) (hc : 0 < stiffness)
    (upper : x ≤ b + err - stiffness * ksq) (inside : b - width ≤ x) :
    ksq ≤ (err + width) / stiffness := by
  apply (le_div_iff₀ hc).2
  linarith

-- NATIVE CHILD 2
lemma top_weight (total wrong top : ℝ) (h : total = wrong + top)
    (h₁ : 1 / 4 ≤ total) (h₂ : wrong ≤ 1 / 8) : 1 / 8 ≤ top := by
  linarith

/-- Comparison of two lags after bounding their common phase-volume factor. -/
theorem two_lag_lower (q₁ q₂ H₁ H₂ a b c : ℝ) (hq : 0 < q₁)
    (hb : 0 < b) (ha : 0 ≤ a) (hc : 0 ≤ c)
    (small : q₁ ≤ b * H₁) (large : a * H₂ ≤ q₂) (ratio : c * H₁ ≤ H₂) :
    a*c/b ≤ q₂/q₁ := by
  rw [div_le_div_iff₀ hb hq]
  calc
    a*c*q₁ ≤ a*c*(b*H₁) := mul_le_mul_of_nonneg_left small (mul_nonneg ha hc)
    _ = b*(a*(c*H₁)) := by ring
    _ ≤ b*q₂ := mul_le_mul_of_nonneg_left
      ((mul_le_mul_of_nonneg_left ratio ha).trans large) hb.le
    _ = q₂*b := mul_comm _ _

/-- The scalar Rayleigh quadratic term has one spatial Laplacian contribution
and four thirds from the off-diagonal orientation entries. -/
theorem scalar_curvature (p q r : ℝ) :
    ((p+q+r) + ((p+q)+(q+p)+(p+r)+(r+p)+(q+r)+(r+q))/3)/256 =
      (7/768 : ℝ)*(p+q+r) := by ring

#print axioms disk_zero_bound
#print axioms filter_weight
#print axioms separated_filter
#print axioms upper_cluster_floor
#print axioms momentum_mass
#print axioms window_radius
#print axioms top_weight
#print axioms two_lag_lower
#print axioms scalar_curvature

end Millennium.G4.LocalScalarEdge
