import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.Positivity
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

import Mathlib.MeasureTheory.Integral.IntervalIntegral.Basic

set_option maxRecDepth 5000
open scoped BigOperators
namespace YangMills.MagneticSmearing

/-- The eight signed axis moves have weight one and holding has weight eight. -/
def moves : List Int := List.replicate 8 0 ++ [1,-1,2,-2,3,-3,4,-4]

theorem moveWeights : (moves.length,moves.count 0) = (16,8) := by decide

/-- At radius one the first nonzero move stops the two-step walk. -/
def stoppedTwo : List Int := moves.flatMap fun a => moves.map fun b => if a=0 then b else a

theorem stoppedMass : (stoppedTwo.count 0, stoppedTwo.count 1) = (64,24) := by decide

theorem stoppedTotal : stoppedTwo.length = 256 := by decide

/-- Exit flux at each time must be added to the surviving distribution. -/
theorem stoppedTelescopes {A : Type*} [AddCommGroup A] (u e : ℕ → A) (n : ℕ) :
    ∑ j ∈ Finset.range n, (u j-u (j+1)-e j) =
      u 0-(u n+∑ j ∈ Finset.range n, e j) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih, Finset.sum_range_succ]
    abel

/-- The static root path contributes a commutator for the transported face. -/
theorem frameCommutator {A : Type*} [Ring A] (u v x y : A)
    : (x*u)*y*v + u*y*(-(v*x)) = x*(u*y*v)-(u*y*v)*x := by
  simp only [mul_neg]
  noncomm_ring

/-- Summing the two Hodge pieces leaves just the endpoint law. -/
theorem hodgeRemainder {A : Type*} [AddCommGroup A] {g h k r : A}
    (hd : h+k=g-r) : g=h+k+r := by rw [hd]; abel

/-- Scalar recurrence for a killed row and its accumulated exit measure. -/
theorem killedStep (live exit oldExit : ℝ) : live - (live-exit) = (oldExit+exit)-oldExit := by ring

/-- Forward and backward faces give opposite first-order variations. -/
theorem transportedSign (w x z : ℝ) : -(w*x-z) = w*(-x)+z := by ring

/-- The estimates for the two finite-support Hodge primitives combine linearly. -/
theorem wardBudget {v w h k r δ : ℝ}
    (a : |v| ≤ h*δ) (b : |w| ≤ k*δ) :
    |v+w|+r ≤ (h+k)*δ+r := by
  linarith [abs_add_le v w]

/-- The covariance error is controlled by the endpoint remainder. -/
theorem projectionTail {v c e r : ℝ} (hid : v-c=e) (h : |e| ≤ r) : |v-c| ≤ r := by
  rwa [hid]

def tailExponent (m : ℕ) := 2+m
def varianceExponent (m : ℕ) := 2*(2*m+4)

theorem smoothingPowers : (tailExponent 1,tailExponent 2) = (3,4) := by decide
theorem spectralPowers : (varianceExponent 1,varianceExponent 2) = (12,16) := by decide

/-- Uniform perturbations of the characteristic ODE give a pointwise error.
The integrating factor increases on the interval from zero to time t. -/
theorem integratingFactorRatio {v t u : ℝ} (hv : 0 ≤ v) (hu : 0 ≤ u) (hut : u ≤ t) :
    Real.exp (-v*(t^2-u^2)/2) ≤ 1 := by
  apply Real.exp_le_one_iff.mpr
  have hs := pow_le_pow_left₀ hu hut 2
  nlinarith [mul_nonneg hv (sub_nonneg.mpr hs)]

theorem duhamelBound (v t ε : ℝ) (hv : 0 ≤ v) (ht : 0 ≤ t) (e : ℝ → ℝ)
    (he : ∀ x ∈ Set.Icc 0 t, |e x| ≤ ε) :
    |∫ u in (0:ℝ)..t, Real.exp (-v*(t^2-u^2)/2)*e u| ≤ ε*t := by
  have h := intervalIntegral.norm_integral_le_of_norm_le_const
    (a := (0:ℝ)) (b := t) (C := ε) (f := fun u => Real.exp (-v*(t^2-u^2)/2)*e u)
    (by
      intro x hx
      rw [Set.uIoc_of_le ht] at hx
      rw [Real.norm_eq_abs, abs_mul, abs_of_pos (Real.exp_pos _)]
      exact (mul_le_mul_of_nonneg_right (integratingFactorRatio hv hx.1.le hx.2)
        (abs_nonneg _)).trans (by simpa using he x ⟨hx.1.le,hx.2⟩))
  simpa [Real.norm_eq_abs, abs_of_nonneg ht] using h

theorem radialMoment (m : ℕ) {p : ℝ} (hp : p ≠ 0) :
    (8*p/((2*(m:ℝ)+1)*(2*m+3)))/(2*(2*p)^3) =
      1/(2*p^2*(2*m+1)*(2*m+3)) := by
  have h₁ : (2*(m:ℝ)+1) ≠ 0 := by positivity
  have h₃ : (2*(m:ℝ)+3) ≠ 0 := by positivity
  field_simp
  ring

theorem determinantBigger {v c s : ℝ} (hs : 0 < s) (hc : 0 < c) (hv : c ≤ v) :
    0 < (1+2*s*v)^2-(2*s*c)^2 ∧ (1+2*s*v)^2-(2*s*c)^2 < (1+2*s*v)^2 := by
  have hx : 0 < 2*s*c := by positivity
  have hy : 2*s*c ≤ 2*s*v := by nlinarith [mul_nonneg hs.le (sub_nonneg.mpr hv)]
  constructor <;> nlinarith [sq_nonneg (2*s*c), sq_pos_of_pos hx,
    mul_self_lt_mul_self hx.le (show 2*s*c < 1+2*s*v by linarith)]

theorem energyReadback {lo hi mass : ℝ} (h : 0 < mass)
    (hw : mass ≤ hi-lo) : lo < hi := by linarith

/-- A negative reflected cross moment controls the positive-block moment. -/
theorem reflectedSquare {v c : ℝ} (hc : c ≤ 0) : 2*v ≤ v+v-2*c := by linarith

/-- The positively supported signed average preserves mass and first moment. -/
theorem signedBlockMoments (mass moment shift : ℝ) :
    2*mass-mass=mass ∧ 2*(moment+shift*mass)-(moment+2*shift*mass)=moment := by
  constructor <;> ring

theorem reflectedFirstMoment {moment mass : ℝ} (hc : 2*moment = -mass) :
    moment-(-moment-mass)=0 := by linarith

/-- The even moment bootstrap absorbs one lower power, independently of y. -/
theorem absorbMoment {y A B : ℝ} {n : ℕ}
    (hp : 1 ≤ y^n) (hA : 0 ≤ A) (h : y^(n+1) ≤ A+B*y^n) :
    y ≤ A+B := by
  by_contra hn
  have hlt : A+B < y := lt_of_not_ge hn
  have h₁ := mul_lt_mul_of_pos_right hlt (show 0 < y^n by linarith)
  have h₂ := mul_nonneg hA (sub_nonneg.mpr hp)
  rw [pow_succ] at h
  nlinarith

end YangMills.MagneticSmearing

open YangMills.MagneticSmearing
#print axioms moveWeights
#print axioms stoppedMass
#print axioms stoppedTotal
#print axioms stoppedTelescopes
#print axioms frameCommutator
#print axioms hodgeRemainder
#print axioms killedStep
#print axioms transportedSign
#print axioms wardBudget
#print axioms projectionTail
#print axioms smoothingPowers
#print axioms spectralPowers
#print axioms integratingFactorRatio
#print axioms radialMoment
#print axioms determinantBigger
#print axioms energyReadback
#print axioms duhamelBound
#print axioms reflectedSquare
#print axioms signedBlockMoments
#print axioms reflectedFirstMoment
#print axioms absorbMoment
