import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

open Finset
namespace YangMills.SpatialPacket

/-- A long spatial difference is the sum of R translates of a unit difference. -/
theorem strideDifference (f : ℤ → ℝ) (x : ℤ) (R : ℕ) :
    ∑ k ∈ range R, (f (x+k)-f (x+k+1)) = f x-f (x+R) := by
  induction R with
  | zero => simp
  | succ R ih =>
    rw [sum_range_succ, ih, Nat.cast_succ, ← add_assoc]
    ring

/-- A test on at most L edges per path charges at most H*L per unit of mass. -/
theorem pathBudget {P E : Type*} (ps : Finset P) (path : P → Finset E)
    (mass : P → ℝ) (charge : E → ℝ) (H L : ℝ)
    (hm : ∀ p ∈ ps, 0 ≤ mass p) (hh : 0 ≤ H)
    (hcharge : ∀ p ∈ ps, ∀ e ∈ path p, charge e ≤ H)
    (hlen : ∀ p ∈ ps, ((path p).card : ℝ) ≤ L) :
    ∑ p ∈ ps, mass p * ∑ e ∈ path p, charge e ≤
      (∑ p ∈ ps, mass p) * (L*H) := by
  rw [sum_mul]
  apply sum_le_sum
  intro p hp
  apply mul_le_mul_of_nonneg_left _ (hm p hp)
  calc
    ∑ e ∈ path p, charge e ≤ ∑ _e ∈ path p, H := sum_le_sum (hcharge p hp)
    _ = ((path p).card : ℝ)*H := by simp
    _ ≤ L*H := mul_le_mul_of_nonneg_right (hlen p hp) hh

/-- The split at diffusion time R² leaves a total spatially weighted cost of R⁴.
The four inputs are the separate termwise summations for early and late times. -/
theorem heatBudget (R A B C D : ℝ) (hR : 0 ≤ R)
    (hA : A ≤ R^2) (hB : B ≤ 2*R) (hC : R*C ≤ 3) (hD : R^2*D ≤ 2) :
    R^2*(A+R*B)+R^5*(C+R*D) ≤ 8*R^4 := by
  have h₁ := mul_le_mul_of_nonneg_left hA (sq_nonneg R)
  have h₂ := mul_le_mul_of_nonneg_left hB (pow_nonneg hR 3)
  have h₃ := mul_le_mul_of_nonneg_left hC (pow_nonneg hR 4)
  have h₄ := mul_le_mul_of_nonneg_left hD (pow_nonneg hR 4)
  linarith only [show R^2*A ≤ R^4 by nlinarith only [h₁],
    show R^3*B ≤ 2*R^4 by nlinarith only [h₂],
    show R^5*C ≤ 3*R^4 by nlinarith only [h₃],
    show R^6*D ≤ 2*R^4 by nlinarith only [h₄],
    show R^2*(A+R*B)+R^5*(C+R*D) = R^2*A+R^3*B+R^5*C+R^6*D by ring]

/-- With s=β^(1/8), any R ≤ c*s has comparison error factor ≤ c⁴. -/
theorem packetScale {R c s : ℝ} (hR : 0 ≤ R) (hs : 0 < s)
    (h : R ≤ c*s) : R^4/s^4 ≤ c^4 := by
  apply (div_le_iff₀ (pow_pos hs 4)).mpr
  simpa only [mul_pow] using pow_le_pow_left₀ hR h 4

/-- A resolved single reading and its norm ceiling give a gap upper bound. -/
theorem singleLag {m R b F W V : ℝ} (hR : 0 < R) (hb : 0 < b)
    (hfree : 2*b ≤ F) (herr : |W-F| ≤ b) (hnorm : V ≤ 1)
    (htransfer : W ≤ Real.exp (-m*R)*V) :
    m ≤ -Real.log b/R := by
  have hw : b ≤ W := by have := (abs_le.mp herr).1; linarith
  have h := hw.trans (htransfer.trans
    (mul_le_mul_of_nonneg_left hnorm (Real.exp_pos _).le))
  rw [mul_one] at h
  have ht := Real.log_le_log hb h
  rw [Real.log_exp] at ht
  apply (le_div_iff₀ hR).mpr
  linarith

/-- A positive difference of two readings forces weight in the interior:
if the response outside a band is at most e/2 and the response inside
is at most 1/4, a total response of at least e needs band mass ≥ 2e. -/
theorem positiveBandMass {e outside inside band : ℝ}
    (hm : e ≤ outside+inside) (hout : outside ≤ e/2)
    (hin : inside ≤ band/4) : 2*e ≤ band := by linarith

end YangMills.SpatialPacket
#print axioms YangMills.SpatialPacket.strideDifference
#print axioms YangMills.SpatialPacket.pathBudget
#print axioms YangMills.SpatialPacket.heatBudget
#print axioms YangMills.SpatialPacket.packetScale
#print axioms YangMills.SpatialPacket.singleLag
#print axioms YangMills.SpatialPacket.positiveBandMass
