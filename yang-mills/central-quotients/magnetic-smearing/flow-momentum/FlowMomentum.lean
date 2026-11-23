import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Finset.Max
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
namespace YangMills.FlowMomentum

/-- A nonnegative bounded sequence cannot have a doubling continuation from every index. -/
theorem boundedDoubling (v : ℕ → ℝ) (K : ℝ) (h0 : ∀ n, 0 ≤ v n)
    (hb : ∀ n, v n ≤ K) (hg : ∀ n, ∃ j, 2*v n ≤ v j) (n : ℕ) : v n = 0 := by
  by_contra hn
  have hp : 0 < v n := lt_of_le_of_ne (h0 n) (Ne.symm hn)
  have hstep : ∀ m : ℕ, ∃ j, ((m:ℝ)+1)*v n ≤ v j := by
    intro m
    induction m with
    | zero => exact ⟨n, by simp⟩
    | succ m ih =>
      obtain ⟨j,hj⟩ := ih
      obtain ⟨k,hk⟩ := hg j
      refine ⟨k,?_⟩
      push_cast
      nlinarith [mul_nonneg (Nat.cast_nonneg (α:=ℝ) m) hp.le]
  obtain ⟨m,hm⟩ := exists_nat_gt (K/v n)
  obtain ⟨j,hj⟩ := hstep m
  nlinarith [(div_lt_iff₀ hp).mp hm,hb j]

/-- After multiplying by a geometric weight, a finite recurrence gives a doubling step. -/
theorem supergeometricZero (b : ℕ → ℝ) (A : ℝ) (hA : 0 ≤ A)
    (hs : ∀ B : ℝ, 1 ≤ B → ∃ K : ℝ, ∀ n : ℕ, B^n*|b n| ≤ K)
    (hg : ∀ n : ℕ, ∃ j : ℕ, 0 < j ∧ |b n| ≤ A*|b (n+j)|)
    (n : ℕ) : b n = 0 := by
  let B := 2*(A+1)
  have hB : 1 ≤ B := by dsimp [B]; linarith
  obtain ⟨K,hK⟩ := hs B hB
  have grow : ∀ m : ℕ, ∃ k : ℕ, 2*(B^m*|b m|) ≤ B^k*|b k| := by
    intro m
    obtain ⟨j,hj,hh⟩ := hg m
    have hj' : B ≤ B^j := by
      simpa using pow_le_pow_right₀ hB (show 1 ≤ j from hj)
    have hcomp : 2*A ≤ B^j := le_trans (by dsimp [B]; linarith) hj'
    have hx : 2*|b m| ≤ B^j*|b (m+j)| := by
      nlinarith [mul_le_mul_of_nonneg_right hcomp (abs_nonneg (b (m+j)))]
    refine ⟨m+j,?_⟩
    rw [pow_add]
    nlinarith [mul_le_mul_of_nonneg_left hx (pow_nonneg (by linarith : 0 ≤ B) m)]
  have h := boundedDoubling (fun m => B^m*|b m|) K
    (fun m => mul_nonneg (pow_nonneg (by linarith : 0 ≤ B) m) (abs_nonneg _)) hK grow n
  have hn : 0 < B^n := pow_pos (by linarith) n
  exact abs_eq_zero.mp ((mul_eq_zero.mp h).resolve_left hn.ne')

theorem recurrenceStep (b a : ℕ → ℝ) (c : ℝ) (hc : c ≠ 0) (S : Finset ℕ) (hS : S.Nonempty)
    (n : ℕ) (eqn : c*b n + ∑ j ∈ S, a j*b (n+j) = 0) :
    ∃ j ∈ S, |b n| ≤ ((∑ i ∈ S, |a i|)/|c|)*|b (n+j)| := by
  obtain ⟨j,hj,hmax⟩ := S.exists_max_image (fun i => |b (n+i)|) hS
  refine ⟨j,hj,?_⟩
  have h : |b n| * |c| ≤ (∑ i ∈ S, |a i|)*|b (n+j)| := by
    calc
      _ = |-(∑ i ∈ S, a i*b (n+i))| := by
        rw [← abs_mul, mul_comm (b n) c, show c*b n = -(∑ i ∈ S, a i*b (n+i)) by linarith]
      _ ≤ ∑ i ∈ S, |a i*b (n+i)| := by rw [abs_neg]; exact Finset.abs_sum_le_sum_abs _ _
      _ ≤ _ := by
        rw [Finset.sum_mul]
        apply Finset.sum_le_sum
        intro i hi
        rw [abs_mul]
        exact mul_le_mul_of_nonneg_left (hmax i hi) (abs_nonneg _)
  rw [div_mul_eq_mul_div]
  exact (le_div_iff₀ (abs_pos.mpr hc)).2 h

theorem recurrentSupergeometric (b a : ℕ → ℝ) (c : ℝ) (hc : c ≠ 0)
    (S : Finset ℕ) (hS : S.Nonempty) (hpos : ∀ j ∈ S, 0 < j)
    (hs : ∀ B : ℝ, 1 ≤ B → ∃ K : ℝ, ∀ n : ℕ, B^n*|b n| ≤ K)
    (heq : ∀ n, c*b n+∑ j ∈ S, a j*b (n+j)=0) (n : ℕ) : b n=0 := by
  apply supergeometricZero b ((∑ j ∈ S, |a j|)/|c|) (by positivity) hs _ n
  intro m
  obtain ⟨j,hj,hh⟩ := recurrenceStep b a c hc S hS m (heq m)
  exact ⟨j,hpos j hj,hh⟩

theorem filterFixture (x : ℝ) : (-1+x+2*x^2)^2=1-2*x-3*x^2+4*x^3+4*x^4 := by ring
theorem phaseFactor (E k z : ℝ) :
    (E^2-z^2)^2+(2*k^2-E^2-z^2)^2 =
    2*((E^2-k^2)^2+(k^2-z^2)^2) := by ring

theorem polarizationWeight (c : ℝ) : 0 < 1+c^2 := by positivity

theorem thresholdAngle {k z : ℝ} (_hk : 0<k) (hz : |z|<k) : 0<(k^2-z^2)^2 := by
  have h := abs_lt.mp hz
  have hp := mul_pos (by linarith : 0<k-z) (by linarith : 0<k+z)
  exact sq_pos_of_pos (by nlinarith)

theorem spatialHeatFactor (s E z : ℝ) :
    Real.exp (-2*s*(((E+z)/2)^2+((E-z)/2)^2)) =
      Real.exp (-s*E^2)*Real.exp (-s*z^2) := by
  rw [← Real.exp_add]
  congr 1
  ring

theorem freeSplit (E k : ℝ) :
    ((E^2-k^2)^2/64+k^4/120)/4 =
    (E^4-2*k^2*E^2+(23/15)*k^4)/256 := by ring

theorem thresholdCoefficient : ((1:ℚ)/120)/4=1/480 := by norm_num

theorem restDensity (E : ℝ) : ((E^2-(0:ℝ)^2)^2/64+(0:ℝ)^4/120)/4=E^4/256 := by ring
theorem propagatorDeficit (a b x y : ℝ) :
    a*b-x*y = (a-x)*b+x*(b-y) := by ring

theorem gaussianTail {a s t : ℝ} (ha : 0<a) (h : a≤2*s) :
    Real.exp (-(t^2)/(4*a)) ≤ Real.exp (-(t^2)/(16*s))*Real.exp (-(t^2)/(8*a)) := by
  have hs : 0<s := by linarith
  rw [← Real.exp_add,Real.exp_le_exp]
  have H : t^2/(16*s) ≤ t^2/(8*a) := div_le_div_of_nonneg_left (sq_nonneg _) (by positivity) (by linarith)
  rw [show -(t^2)/(4*a) = -(t^2)/(8*a) + -(t^2)/(8*a) by ring]
  simp only [neg_div]
  linarith only [H]

theorem temporalFilter (a b x : ℝ) : a^2 + 2*a*b*x + b^2*x^2=(a+b*x)^2 := by ring

theorem coneDensityPositive {s E k z : ℝ} (hk : 0<k) (hz : |z|<k) :
    0<Real.exp (-s*(E^2+z^2))*((E^2-k^2)^2+(k^2-z^2)^2) :=
  mul_pos (Real.exp_pos _) (add_pos_of_nonneg_of_pos (sq_nonneg _) (thresholdAngle hk hz))

theorem torusBound {a b c : ℝ} (ha : a≤918686/1000000)
    (hb : 832895/1000000≤b) (hc : c≤737430/1000000) :
    a-2*b+c ≤ -9674/1000000 := by linarith

end YangMills.FlowMomentum
open YangMills.FlowMomentum
#print axioms boundedDoubling
#print axioms supergeometricZero
#print axioms recurrenceStep
#print axioms recurrentSupergeometric
#print axioms phaseFactor
#print axioms polarizationWeight
#print axioms thresholdAngle
#print axioms spatialHeatFactor
#print axioms freeSplit
#print axioms thresholdCoefficient
#print axioms restDensity
#print axioms propagatorDeficit
#print axioms gaussianTail
#print axioms temporalFilter
#print axioms coneDensityPositive
#print axioms filterFixture
#print axioms torusBound
