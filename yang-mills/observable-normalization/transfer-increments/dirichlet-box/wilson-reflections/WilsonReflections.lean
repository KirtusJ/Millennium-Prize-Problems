import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Real.Sqrt
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace YangMills.WilsonReflections

/-- The forward pullback takes a half-space site to another such site. -/
theorem forwardSite (t : ℤ) (ht : 0 ≤ t) : 0 ≤ t+1 := by omega

/-- Bond reflection of the translated label is site reflection of the original. -/
theorem adjacentReflection (t : ℤ) : 1-(t+1) = -t := by ring

/-- First slope of the even log-moments is below the secant slope
on each finite interval. Only inequalities inside the interval enter. -/
theorem evenChord (f : ℕ → ℝ) (m : ℕ)
    (hc : ∀ n, n+2 ≤ m → 2*f (n+1) ≤ f n+f (n+2)) :
    (m:ℝ)*(f 1-f 0) ≤ f m-f 0 := by
  have step (i : ℕ) (hi : i+1 ≤ m) : f 1-f 0 ≤ f (i+1)-f i := by
    induction i with
    | zero => simp
    | succ i ih =>
      have h := ih (by omega)
      have h' := hc i (by omega)
      change f 1-f 0 ≤ f (i+2)-f (i+1)
      linarith
  have run (i : ℕ) (hi : i ≤ m) : (i:ℝ)*(f 1-f 0) ≤ f i-f 0 := by
    induction i with
    | zero => simp
    | succ i ih =>
      have h := ih (by omega)
      have h' := step i hi
      rw [Nat.cast_succ, add_mul, one_mul]
      linarith
  exact run m le_rfl

/-- One layer is controlled by the full even period after reflection. -/
theorem layerBound (u v w : ℝ) (m : ℕ) (h : 2*u ≤ v) (hch : (m:ℝ)*v ≤ w) :
    (2*(m:ℝ))*u ≤ w := by
  calc
    _ = (m:ℝ)*(2*u) := by ring
    _ ≤ (m:ℝ)*v := mul_le_mul_of_nonneg_left h (by positivity)
    _ ≤ w := hch

/-- Independent central link matrices give the power of their mean
on each plaquette. Its deficit is bounded by the incidence count. -/
theorem trialDeficit (x : ℝ) (hx : |x| ≤ 1) (k : ℕ) :
    1-x^k ≤ (k:ℝ)*(1-x) := by
  induction k with
  | zero => simp
  | succ k ih =>
    have hpow : x^k ≤ 1 := (le_abs_self _).trans (by
      rw [abs_pow]
      exact pow_le_one₀ (abs_nonneg _) hx)
    have hpos : 0 ≤ 1-x := by linarith [(le_abs_self x).trans hx]
    have h := mul_le_mul_of_nonneg_right hpow hpos
    rw [pow_succ, Nat.cast_succ]
    nlinarith

/-- The SU(2) Haar radial integral after scaling has an increasing
weight on the old integration interval. -/
theorem radialWeight (x s t : ℝ) (hx : 0 ≤ x) (hs : 0 < s) (hst : s ≤ t) :
    Real.sqrt (2-x/s) ≤ Real.sqrt (2-x/t) := by
  apply Real.sqrt_le_sqrt
  have h := div_le_div_of_nonneg_left hx hs hst
  linarith

/-- Dropping the two finite-size logarithmic corrections only takes
place after fixing the coupling and sending this side to infinity. -/
theorem seamIdentity (z w m : ℝ) :
    3*(1-m)*z - (3+m)*w = 3*(z-w) - m*(3*z+w) := by ring

end YangMills.WilsonReflections
#print axioms YangMills.WilsonReflections.forwardSite
#print axioms YangMills.WilsonReflections.adjacentReflection
#print axioms YangMills.WilsonReflections.evenChord
#print axioms YangMills.WilsonReflections.layerBound
#print axioms YangMills.WilsonReflections.trialDeficit
#print axioms YangMills.WilsonReflections.radialWeight
#print axioms YangMills.WilsonReflections.seamIdentity
