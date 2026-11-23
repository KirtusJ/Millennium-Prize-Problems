import Mathlib.Data.Real.Sqrt
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

open Finset
namespace YangMills.ReflectedStrip

/-- Bounded squared norms of shifted staples have a contractive first shift
once reflection positivity supplies the ordinary second-difference inequality. -/
theorem shiftContraction (q : ℕ → ℝ) (K : ℝ) (bound : ∀ n, q n ≤ K)
    (convex : ∀ n, 2*q (n+1) ≤ q n+q (n+2)) : q 1 ≤ q 0 := by
  have hstep (n : ℕ) : q 1-q 0 ≤ q (n+1)-q n := by
    induction n with
    | zero => simp
    | succ n ih =>
      change q 1 - q 0 ≤ q (n+2) - q (n+1)
      linarith [convex n]
  have hline (n : ℕ) : q 0+(n:ℝ)*(q 1-q 0) ≤ q n := by
    induction n with
    | zero => simp
    | succ n ih =>
      rw [Nat.cast_succ, add_mul, one_mul]
      linarith [hstep n]
  by_contra! hn
  have hd : 0 < q 1-q 0 := sub_pos.mpr hn
  obtain ⟨n,hn'⟩ := exists_nat_gt ((K-q 0)/(q 1-q 0))
  have hh := (div_lt_iff₀ hd).mp hn'
  linarith [bound n, hline n]

/-- The deficit is at most linear in strip length even if the one-step
self-adjoint contraction has a negative part. -/
theorem stripDeficit (x : ℝ) (hx : |x| ≤ 1) (n : ℕ) :
    1-x^n ≤ (n:ℝ)*(1-x) := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hp : x^n ≤ 1 := (le_abs_self _).trans (by
      rw [abs_pow]
      exact pow_le_one₀ (abs_nonneg _) hx)
    have hx' := (le_abs_self x).trans hx
    have h := mul_nonneg (sub_nonneg.mpr hp) (sub_nonneg.mpr hx')
    rw [pow_succ, Nat.cast_succ]
    nlinarith

/-- Interpolate the half-weighted norm from unweighted and weighted norms. -/
theorem halfWeight {ι : Type*} (s : Finset ι) (a w : ι → ℝ)
    (ha : ∀ i, 0 ≤ a i) (hw : ∀ i, 0 ≤ w i) :
    (∑ i ∈ s, a i * Real.sqrt (w i))^2 ≤
        (∑ i ∈ s, a i)*(∑ i ∈ s, a i*w i) := by
  have hc := sum_mul_sq_le_sq_mul_sq s (fun i => Real.sqrt (a i))
    (fun i => Real.sqrt (a i)*Real.sqrt (w i))
  simpa only [← mul_assoc, ← sq, mul_pow, Real.sq_sqrt (ha _),
    Real.sq_sqrt (hw _)] using hc

/-- The R³ and R⁴ estimates together supply the R⁷ squared norm. -/
theorem squaredBudget {A B Q R C : ℝ} (hB : 0 ≤ B) (hR : 0 ≤ R)
    (hC : 0 ≤ C) (hq : Q^2 ≤ A*B) (hA : A ≤ C*R^3)
    (hB' : B ≤ C*R^4) : Q^2 ≤ C^2*R^7 := by
  calc
    Q^2 ≤ A*B := hq
    _ ≤ (C*R^3)*(C*R^4) := mul_le_mul hA hB' hB (by positivity)
    _ = C^2*R^7 := by ring

/-- Testing against the correlation scale uses the seventh power of the width. -/
theorem errorAtScale {R c s : ℝ} (hR : 0 ≤ R) (hs : 0 < s) (h : R ≤ c*s) :
    R^7/s^7 ≤ c^7 := by
  apply (div_le_iff₀ (pow_pos hs 7)).mpr
  simpa only [mul_pow] using pow_le_pow_left₀ hR h 7

/-- Fix one side, bound its deficit by its value at length one, then
apply the same estimate in the perpendicular direction. -/
theorem rectangleDeficit (W : ℕ → ℕ → ℝ)
    (along : ∀ m n, 1-W m n ≤ (n:ℝ)*(1-W m 1))
    (across : ∀ m, 1-W m 1 ≤ (m:ℝ)*(1-W 1 1)) (m n : ℕ) :
    1-W m n ≤ ((m:ℝ)*(n:ℝ))*(1-W 1 1) := by
  calc
    1-W m n ≤ (n:ℝ)*(1-W m 1) := along m n
    _ ≤ (n:ℝ)*((m:ℝ)*(1-W 1 1)) :=
      mul_le_mul_of_nonneg_left (across m) (Nat.cast_nonneg n)
    _ = _ := by ring

end YangMills.ReflectedStrip
#print axioms YangMills.ReflectedStrip.shiftContraction
#print axioms YangMills.ReflectedStrip.stripDeficit
#print axioms YangMills.ReflectedStrip.halfWeight
#print axioms YangMills.ReflectedStrip.squaredBudget
#print axioms YangMills.ReflectedStrip.errorAtScale
#print axioms YangMills.ReflectedStrip.rectangleDeficit
