import Mathlib.Data.Real.Sqrt
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

open MeasureTheory
namespace YangMills.TransferClock

noncomputable def walkRoot (v : ℝ) := (2+v-Real.sqrt (v*(v+4)))/2

theorem walkEquation {v : ℝ} (hv : 0≤v) :
    (2+v)*walkRoot v = 1+(walkRoot v)^2 := by
  unfold walkRoot
  nlinarith [Real.sq_sqrt (show 0≤v*(v+4) by positivity)]

theorem boundedClockPoint {y l : ℝ} (hl : l≤y) (hy : y≤1) :
    (1+l)*(1-y)≤1-y^2 := by nlinarith [mul_nonneg (sub_nonneg.mpr hl) (sub_nonneg.mpr hy)]

theorem boundedClockLaw {X : Type*} [MeasurableSpace X] (μ : Measure X)
    (f : X → ℝ) (l : ℝ) (hr : ∀ x, l≤f x ∧ f x≤1)
    (h1 : Integrable (fun x => 1-f x) μ) (h2 : Integrable (fun x => 1-(f x)^2) μ) :
    (1+l)*(∫ x, 1-f x ∂μ) ≤ ∫ x, 1-(f x)^2 ∂μ := by
  rw [← integral_const_mul]
  exact integral_mono (h1.const_mul _) h2 (fun x => boundedClockPoint (hr x).1 (hr x).2)

theorem clockError {a r d₁ d₂ u₁ u₂ e : ℝ} (ha : 0≤a)
    (hf : a*u₁ ≤ u₂) (hg : d₂ ≤ r*d₁) (h1 : d₁-e ≤ u₁) (h2 : u₂ ≤ d₂+e) :
    (a-r)*d₁ ≤ (1+a)*e := by
  nlinarith [mul_le_mul_of_nonneg_left h1 ha]

theorem capConstant : ((7:ℚ)/48)*(9/64)>1/64 := by norm_num

theorem sharedClockDifference (E z : ℝ) :
    ((E+z)/2)^2+((E-z)/2)^2=(E^2+z^2)/2 := by ring

theorem independentSymmetry (a b c d : ℝ) : (a*b+c*d)/2=(d*c+b*a)/2 := by ring
def ux (L x y : ℕ) : ℤ := if x+1=L then -(L:ℤ)*y else 0

def flux (L x y : ℕ) : ℤ :=
  (ux L x y+((x+1)%L:ℕ)-ux L x ((y+1)%L)-(x:ℤ))%4

def faces (L : ℕ) : List ℤ := (List.range L).flatMap fun x => (List.range L).map (flux L x)

theorem sixTorus : ((faces 6).filter (·=1)).length = 36 := by decide

theorem evenCorner (k : ℤ) : (1-(2*k)^2)%4=1 := by
  rw [show 1-(2*k)^2= -k^2*4+1 by ring]
  omega

theorem conditionalRange (κ h : ℝ) (h₁ : (3/8)*κ ≤ h) (h₂ : (1/8)*κ ≤ 1/2-h) :
    (3/8)*κ ≤ h ∧ h ≤ 1/2-κ/8 := by constructor <;> linarith

/-- A lower bound for a squared discrepancy on one measurable set. -/
theorem eventIntegral {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (D : X → ℝ) (m v p : ℝ) {S : Set X} (hm : MeasurableSet S)
    (hp : p ≤ μ.real S) (hv : 0≤v)
    (hs : ∀ x ∈ S, v≤(D x-m)^2) (hi : Integrable (fun x => (D x-m)^2) μ) :
    v*p ≤ ∫ x, (D x-m)^2 ∂μ := by
  apply (mul_le_mul_of_nonneg_left hp hv).trans
  exact (setIntegral_ge_of_const_le hm (measure_ne_top _ _) hs hi.integrableOn).trans
    (setIntegral_le_integral hi (Filter.Eventually.of_forall (fun x => sq_nonneg _)))

theorem separatedReadings {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (D : X → ℝ) (m a b p : ℝ) (hab : a≤b) (A B : Set X)
    (hA : MeasurableSet A) (hB : MeasurableSet B) (pA : p ≤ μ.real A) (pB : p ≤ μ.real B)
    (lo : ∀ x ∈ A, D x≤a) (hi : ∀ x ∈ B, b≤D x) (integ : Integrable (fun x => (D x-m)^2) μ) :
    ((b-a)/2)^2*p ≤ ∫ x, (D x-m)^2 ∂μ := by
  by_cases hh : (a+b)/2≤m
  · apply eventIntegral μ D m _ p hA pA (sq_nonneg _) _ integ
    intro x hx
    have d := lo x hx
    have h := mul_nonneg (show 0≤(m-D x)-(b-a)/2 by linarith)
      (show 0≤(m-D x)+(b-a)/2 by linarith)
    nlinarith
  · apply eventIntegral μ D m _ p hB pB (sq_nonneg _) _ integ
    intro x hx
    have d := hi x hx
    have h := mul_nonneg (show 0≤(D x-m)-(b-a)/2 by linarith)
      (show 0≤(D x-m)+(b-a)/2 by linarith)
    nlinarith
theorem squareMagnetic (x : ℝ) : (1-x^2)/2 = (3-(4*x^2-1))/8 := by ring

theorem centerOrder {y t : ℝ} (hy : 0<y) (hy' : y<1) (ht : 0<t) (ht' : t<1) :
    2*y*t/(1+y^2*t^2) < 2*y*t/(t^2+y^2) := by
  have h : 0<(1-y^2)*(1-t^2) := by
    apply mul_pos
    · nlinarith [mul_pos (sub_pos.mpr hy') (by linarith : 0<1+y)]
    · nlinarith [mul_pos (sub_pos.mpr ht') (by linarith : 0<1+t)]
  apply div_lt_div_of_pos_left (by positivity) (by positivity)
  nlinarith

theorem oddWeight {l h x a b : ℝ} (hx : 0≤x) (ha : 0≤a) (hb : 0≤b)
    (hd : 2*x*b ≤ h-l) (hs : 2*a ≤ h+l) : 4*x*a*b ≤ h^2-l^2 := by
  have hh := mul_le_mul hd hs (by positivity : 0 ≤ 2*a) (by linarith [mul_nonneg hx hb] : 0 ≤ h-l)
  nlinarith only [hh]

theorem haarCoefficient : (4:ℚ)/2*(1/4-1/8)=1/4 := by norm_num

theorem atomFloor {v a b : ℝ} (ha : 0≤a) (hb : b≤a) (h : a*(a-b)/8≤-v) :
    (a*(a-b)/8)^2 ≤ v^2 := by
  have hd : 0 ≤ a-b := sub_nonneg.mpr hb
  have hp : 0≤a*(a-b)/8 := by positivity
  nlinarith [mul_nonneg (sub_nonneg.mpr h) (by linarith : 0 ≤ -v+a*(a-b)/8)]

theorem characterLimit (x : ℝ) (hx : x ≠ -1) : 2*(1-x)/(1+x)=4/(1+x)-2 := by
  field_simp [show 1+x ≠ 0 by intro h; apply hx; linarith]
  ring

end YangMills.TransferClock
open YangMills.TransferClock
#print axioms walkEquation
#print axioms boundedClockPoint
#print axioms boundedClockLaw
#print axioms clockError
#print axioms capConstant
#print axioms sharedClockDifference
#print axioms independentSymmetry
#print axioms sixTorus
#print axioms evenCorner
#print axioms conditionalRange
#print axioms eventIntegral
#print axioms separatedReadings
#print axioms squareMagnetic
#print axioms centerOrder
#print axioms oddWeight
#print axioms haarCoefficient
#print axioms atomFloor
#print axioms characterLimit
