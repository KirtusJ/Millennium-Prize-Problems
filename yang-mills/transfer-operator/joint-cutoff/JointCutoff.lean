import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.YangMills.JointCutoff

/-- Integration by parts and Gamma domination give the consecutive-ratio bounds. -/
theorem ratioFromScore {r g k : ℝ} (hg : 0 < g)
    (score : (2*k+1)*r ≤ 2*g*(1-r)) (gamma : g*(1-r) ≤ k+1/2) :
    1-r ≤ (k+1/2)/g ∧ r*(1+(k+1/2)/g) ≤ 1 := by
  constructor
  · apply (le_div_iff₀ hg).2
    linarith only [gamma]
  · apply (mul_le_mul_iff_of_pos_right hg).1
    have scaled : r*(1+(k+1/2)/g)*g = r*(g+k+1/2) := by
      field_simp [hg.ne']
      ring
    rw [scaled]
    linarith only [score]

/-- The all-factor product yields bounds on the kinetic defect. -/
theorem kineticBounds {a x r : ℝ} (ha : 0 < a) (hx : 0 ≤ x)
    (lower : 1-r ≤ a*x) (upper : r*(1+a*x) ≤ 1) :
    x/(1+a*x) ≤ (1-r)/a ∧ (1-r)/a ≤ x := by
  refine ⟨(div_le_div_iff₀ (by positivity) ha).2 ?_, (div_le_iff₀ ha).2 ?_⟩ <;> linarith

/-- Assemble the two one-sided estimates for any finite set of Bessel ratio factors. -/
theorem productBounds {ι : Type*} (S : Finset ι) (r z : ι → ℝ)
    (hz : ∀ i, 0 ≤ z i) (hr : ∀ i, 0 ≤ r i ∧ r i ≤ 1)
    (lower : ∀ i, 1-r i ≤ z i) (upper : ∀ i, r i*(1+z i) ≤ 1) :
    1-∏ i ∈ S, r i ≤ ∑ i ∈ S, z i ∧
      (∏ i ∈ S, r i)*(1+∑ i ∈ S, z i) ≤ 1 := by
  classical
  induction S using Finset.induction_on with
  | empty => simp
  | @insert i S hi ih =>
    simp only [Finset.prod_insert hi, Finset.sum_insert hi]
    let p := ∏ j ∈ S, r j
    let s := ∑ j ∈ S, z j
    have hp : 0 ≤ p := Finset.prod_nonneg fun j _ => (hr j).1
    have hs : 0 ≤ s := Finset.sum_nonneg fun j _ => hz j
    have pbound : p ≤ 1 := by
      calc
        p ≤ p*(1+s) := by nlinarith [mul_nonneg hp hs]
        _ ≤ 1 := ih.2
    have cross := mul_nonneg (sub_nonneg.mpr (hr i).2) (sub_nonneg.mpr pbound)
    have mult := mul_le_mul (upper i) ih.2 (mul_nonneg hp (by linarith : 0 ≤ 1+s)) (by norm_num)
    change 1-r i*p ≤ z i+s ∧ r i*p*(1+(z i+s)) ≤ 1
    constructor
    · linarith only [ih.1, lower i, cross]
    · nlinarith only [mult, mul_nonneg (mul_nonneg (hr i).1 hp) (mul_nonneg (hz i) hs)]

/-- The bounded kinetic defect and the true kinetic resolvent differ by at most a/(1+ac). -/
theorem freeResolvent {a c x d : ℝ} (ha : 0 < a) (hc : 0 < c) (hx : 0 ≤ x)
    (hlo : x/(1+a*x) ≤ d) (hhi : d ≤ x) :
    0 ≤ 1/(c+d)-1/(c+x) ∧ 1/(c+d)-1/(c+x) ≤ a/(1+a*c) := by
  have hxden : 0 < 1+a*x := by positivity
  have hy := div_nonneg hx hxden.le
  have hd := hy.trans hlo
  have monotone := one_div_le_one_div_of_le (by linarith : 0 < c+d) (by linarith : c+d ≤ c+x)
  refine ⟨by linarith, ?_⟩
  have replaceD := one_div_le_one_div_of_le (by linarith : 0 < c+x/(1+a*x))
    (by linarith : c+x/(1+a*x) ≤ c+d)
  suffices bound : 1/(c+x/(1+a*x))-1/(c+x) ≤ a/(1+a*c) by linarith
  have pos : 0 < c*(1+a*x)+x := by positivity
  rw [show c+x/(1+a*x) = (c*(1+a*x)+x)/(1+a*x) by field_simp]
  rw [one_div_div]
  apply (sub_le_iff_le_add).2
  rw [div_add_div _ _ (by positivity : 1+a*c ≠ 0) (by linarith : c+x ≠ 0)]
  apply (div_le_div_iff₀ pos (by positivity)).2
  ring_nf
  nlinarith only [mul_nonneg ha.le (sq_nonneg c), mul_nonneg (sq_nonneg a) (mul_nonneg (sq_nonneg c) hx),
    mul_nonneg ha.le (mul_nonneg hc.le hx), mul_nonneg (sq_nonneg a) (mul_nonneg hc.le (sq_nonneg c))]

/-- Resolvent differences with a common perturbation; no factors commute here. -/
theorem commonPotential {A : Type*} [Ring A] (x y u v w : A)
    (leftEq : (1-u*w)*x = u) (rightEq : y*(1-w*v) = v) :
    (1-u*w)*(x-y)*(1-w*v) = u-v := by
  rw [mul_sub (1-u*w) x y, sub_mul _ _ (1-w*v), leftEq, mul_assoc, rightEq]
  rw [mul_sub, sub_mul, mul_one, one_mul, mul_assoc]
  abel

/-- The common perturbation costs at most four times the free error in operator norm. -/
theorem commonPotentialNorm {A : Type*} [NormedRing A] (x y u v w : A) {a : ℝ}
    (leftEq : (1-u*w)*x = u) (rightEq : y*(1-w*v) = v)
    (hl : ‖1-u*w‖ ≤ 2) (hr : ‖1-w*v‖ ≤ 2) (free : ‖x-y‖ ≤ a) :
    ‖u-v‖ ≤ 4*a := by
  rw [← commonPotential x y u v w leftEq rightEq]
  have first := (norm_mul_le (1-u*w) (x-y)).trans
    (mul_le_mul hl free (norm_nonneg _) (by norm_num))
  have second := (norm_mul_le ((1-u*w)*(x-y)) (1-w*v)).trans
    (mul_le_mul_of_nonneg_right first (norm_nonneg _))
  have ha := (norm_nonneg (x-y)).trans free
  nlinarith only [second, mul_le_mul_of_nonneg_left hr (show 0 ≤ 2*a by linarith)]

/-- Combine the two magnetic corrections and the common-potential norm estimate. -/
theorem wilsonResolventError {A : Type*} [NormedAddCommGroup A] (r s u v : A) {a : ℝ}
    (outer : ‖r-s‖ ≤ 2*a) (effective : ‖s-u‖ ≤ 3*a) (common : ‖u-v‖ ≤ 4*a) :
    ‖r-v‖ ≤ 9*a := by
  have one := dist_triangle r s v
  have two := dist_triangle s u v
  simp only [dist_eq_norm] at one two
  linarith

/-- Undoing the reciprocal estimate below a common energy ceiling. -/
theorem energyFromResolvent {a c e m : ℝ} (ha : 0 < a) (hc : 0 < c)
    (he : 0 ≤ e) (hm : 0 ≤ m) (cap : e ≤ c) (step : a*c ≤ 1/36)
    (err : |1/(c+m)-1/(c+e)| ≤ 9*a) :
    |m-e| ≤ 72*a*c^2 ∧ m ≤ 3*c := by
  have ep : 0 < c+e := by linarith
  have mp : 0 < c+m := by linarith
  have small : 9*a*(c+e) ≤ 1/2 := by nlinarith only [step, mul_le_mul_of_nonneg_left cap ha.le]
  have ratio : |m-e| ≤ 9*a*((c+m)*(c+e)) := by
    rw [div_sub_div _ _ mp.ne' ep.ne', abs_div, abs_of_pos (mul_pos mp ep)] at err
    rw [div_le_iff₀ (mul_pos mp ep)] at err
    convert err using 1
    rw [show 1*(c+e)-(c+m)*1 = -(m-e) by ring, abs_neg]
  have diff := (le_abs_self (m-e)).trans ratio
  have scaled := mul_le_mul_of_nonneg_right small mp.le
  have mcap : c+m ≤ 2*(c+e) := by nlinarith only [scaled, diff]
  have product := mul_le_mul mcap (show c+e ≤ 2*c by linarith) ep.le (by linarith)
  have ccap : 2*(c+e) ≤ 4*c := by linarith
  have extent := mul_le_mul_of_nonneg_right ccap (show 0 ≤ 2*c by linarith)
  constructor
  · nlinarith only [ratio, mul_le_mul_of_nonneg_left (product.trans extent) (show 0 ≤ 9*a by positivity)]
  · linarith

/-- Converting a bounded defect eigenvalue into its physical transfer energy. -/
theorem logLift {a m : ℝ} (ha : 0 < a) (h : a*m ≤ 1/2) :
    m ≤ -Real.log (1-a*m)/a ∧ -Real.log (1-a*m)/a ≤ m+2*a*m^2 := by
  have hd : 0 < 1-a*m := by linarith
  have lo := Real.log_le_sub_one_of_pos hd
  have hi := Real.log_le_sub_one_of_pos (inv_pos.mpr hd)
  rw [Real.log_inv] at hi
  constructor
  · apply (le_div_iff₀ ha).2
    linarith
  · apply (div_le_iff₀ ha).2
    apply hi.trans
    apply (sub_le_iff_le_add).2
    rw [inv_eq_one_div]
    apply (div_le_iff₀ hd).2
    nlinarith only [mul_nonneg (sq_nonneg (a*m)) (show 0 ≤ 1-2*(a*m) by linarith)]

-- PCP begin constants
theorem combinedError {a c e m energy : ℝ} (ha : 0 ≤ a)
    (hm : 0 ≤ m) (cap : m ≤ 3*c) (defect : |m-e| ≤ 72*a*c^2)
    (lo : m ≤ energy) (hi : energy ≤ m+2*a*m^2) : |energy-e| ≤ 90*a*c^2 := by
  obtain ⟨left, right⟩ := abs_le.mp defect
  have sq := mul_self_le_mul_self hm cap
  have scaled := mul_le_mul_of_nonneg_left sq ha
  apply abs_le.mpr
  constructor <;> nlinarith [mul_nonneg ha (sq_nonneg c)]
-- PCP end constants

-- PCP begin control
/-- A positive contraction with diagonal entries 3/4 and off-diagonal 1/4.
    Rescaling its kinetic form by multiplication has neither order on all vectors. -/
theorem sandwichControl :
    (¬ ∀ x y : ℝ, ((x+3*y)/4)^2 ≤ y^2) ∧
    (¬ ∀ x y : ℝ, y^2 ≤ ((x+3*y)/4)^2) := by
  constructor
  · intro h
    have bad := h 1 0
    norm_num at bad
  · intro h
    have bad := h 0 1
    norm_num at bad
-- PCP end control

theorem gapError {E₀ E₁ A₀ A₁ b : ℝ}
    (h₀ : |A₀-E₀| ≤ b) (h₁ : |A₁-E₁| ≤ b) :
    |(A₁-A₀)-(E₁-E₀)| ≤ 2*b := by
  obtain ⟨l₀,u₀⟩ := abs_le.mp h₀
  obtain ⟨l₁,u₁⟩ := abs_le.mp h₁
  apply abs_le.mpr
  constructor <;> linarith

#print axioms commonPotential
#print axioms commonPotentialNorm
#print axioms wilsonResolventError
#print axioms gapError
#print axioms ratioFromScore
#print axioms kineticBounds
#print axioms productBounds
#print axioms freeResolvent
#print axioms energyFromResolvent
#print axioms logLift
#print axioms combinedError
#print axioms sandwichControl
end Millennium.YangMills.JointCutoff
