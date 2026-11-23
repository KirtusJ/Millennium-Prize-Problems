import Mathlib.Analysis.Calculus.Deriv.Inv
import Mathlib.Tactic.Group
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

open MeasureTheory Set
open scoped BigOperators
namespace YangMills.MagneticConnector

/-- Temporal faces at the location of one selected spatial edge, on a five-slice circle. -/
def doubleFaces (lag : ℕ) : ℕ :=
  ((List.range 5).filter fun t =>
    (t=0 ∨ t=lag) ∧ ((t+1)%5=0 ∨ (t+1)%5=lag)).length

theorem markedRows : (doubleFaces 1,doubleFaces 2,doubleFaces 4) = (1,0,1) := by decide

/-- Different collinear positive bonds cannot be the two parallel edges of a square. -/
theorem straightPrivate {x y x' y' : ℤ} (row : y=y') :
    ¬ (x=x' ∧ (y'=y+1 ∨ y=y'+1)) := by omega

theorem rebaseConnector {G : Type*} [Group G] (p w a b : G) :
    (p⁻¹*a*p)⁻¹*(w*b*w⁻¹)=p⁻¹*(a⁻¹*(p*w)*b*(p*w)⁻¹)*p := by group

theorem orthogonalDeficit (x y z : ℝ) :
    (x-y)^2 ≤ 2*((x-z)^2+(y-z)^2) := by nlinarith [sq_nonneg (x+y-2*z)]

/-- Centering changes the measured second moment by a squared mean. -/
theorem secondMomentError {s m v δ : ℝ} (hs : |s-v| ≤ δ) (hm : |m| ≤ δ) :
    |(s-m^2)-v| ≤ δ+δ^2 := by
  have hsq : m^2 ≤ δ^2 := by
    nlinarith [sq_abs m, mul_nonneg (sub_nonneg.mpr hm) (add_nonneg
      (le_trans (abs_nonneg m) hm) (abs_nonneg m))]
  rw [abs_le] at hs ⊢
  constructor <;> nlinarith [sq_nonneg m, sq_nonneg δ]

/-- The two-slice transfer moment is an ordinary exponential-moment bound. -/
theorem twoStepWindow (μ : Measure ℝ) [IsFiniteMeasure μ] (u : ℝ)
    (hi : Integrable (fun x : ℝ => Real.exp (-2*x)) μ) :
    Real.exp (-2*u) * μ.real (Iic u) ≤ ∫ x, Real.exp (-2*x) ∂μ := by
  have hs : MeasurableSet (Iic u) := measurableSet_Iic
  have h := integral_mono_ae ((integrable_const (μ := μ) (Real.exp (-2*u))).indicator hs) hi
    (Filter.Eventually.of_forall (fun x =>
      show (Iic u).indicator (fun _ => Real.exp (-2*u)) x ≤ Real.exp (-2*x) by
        by_cases hx : x ∈ Iic u
        · rw [indicator_of_mem hx]
          exact Real.exp_le_exp.mpr (by change x ≤ u at hx; linarith)
        · rw [indicator_of_not_mem hx]
          exact (Real.exp_pos _).le))
  rw [integral_indicator hs] at h
  simpa [mul_comm] using h

/-- Squared entry and linear entry sums from the six axial images of a unit vector. -/
def axialSample : List ℤ := [1,-1,0,0,0,0]

theorem axialMoments : (axialSample.length,axialSample.sum,
    (axialSample.map (fun x => x*x)).sum) = (6,0,2) := by decide

theorem twoStepExponent (s θ : ℝ) :
    Real.exp (-2*s) / Real.exp (-2*((1-θ)*s))=Real.exp (-2*θ*s) := by
  rw [← Real.exp_sub]
  congr 1
  ring

theorem varianceBudget {a b v δ : ℝ} (ha : |a-v| ≤ δ) (hb : b^2 ≤ δ^2) :
    |a-b^2-v| ≤ δ+δ^2 := by
  rw [abs_le] at ha ⊢
  constructor <;> nlinarith [sq_nonneg b,sq_nonneg δ]

theorem driftPartialBudget {n : ℕ} {e : ℕ → ℝ} {δ : ℝ} (he : ∀ i < n, |e i| ≤ δ) :
    |∑ i ∈ Finset.range n, e i| ≤ n*δ := by
  calc
    _ ≤ ∑ i ∈ Finset.range n, |e i| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _i ∈ Finset.range n, δ :=
      Finset.sum_le_sum fun i hi => he i (Finset.mem_range.mp hi)
    _ = _ := by simp

theorem innovationIdentity {α : Type*} [MeasurableSpace α] (μ : Measure α)
    [IsProbabilityMeasure μ] (f : α → ℝ) (hi : Integrable f μ)
    (hi2 : Integrable (fun x => f x ^ 2) μ) :
    ∫ x, (f x - ∫ y, f y ∂μ)^2 ∂μ = (∫ x, f x^2 ∂μ) - (∫ x, f x ∂μ)^2 := by
  let m := ∫ y, f y ∂μ
  change ∫ x, (f x-m)^2 ∂μ = _ - m^2
  have hp : ∀ x, (f x-m)^2 = (f x^2-(2*m)*f x)+m^2 := by intro x; ring
  simp_rw [hp]
  have his : Integrable (fun x => f x^2 - (2*m)*f x) μ := hi2.sub (hi.const_mul _)
  rw [integral_add his (integrable_const (m^2)),
      integral_sub hi2 (hi.const_mul _), integral_const_mul, integral_const]
  simp [m]
  ring

/-- The family may overlap arbitrarily. Only the individual one-step norms enter. -/
theorem sumPrediction {E : Type*} [NormedAddCommGroup E] [NormedSpace ℝ E]
    (s : Finset ℕ) (c δ : ℕ → ℝ) (u : ℕ → E) (hu : ∀ i ∈ s, ‖u i‖ ≤ δ i) :
    ‖∑ i ∈ s, c i • u i‖ ≤ ∑ i ∈ s, |c i| * δ i := by
  calc
    _ ≤ ∑ i ∈ s, ‖c i • u i‖ := norm_sum_le _ _
    _ ≤ _ := Finset.sum_le_sum fun i hi => by
      rw [norm_smul, Real.norm_eq_abs]
      exact mul_le_mul_of_nonneg_left (hu i hi) (abs_nonneg _)

theorem dressingCost {q w ε : ℝ} (he : 0<ε) (h : q ≤ (w*ε)^2) :
    q/ε^2 ≤ w^2 := by
  apply (div_le_iff₀ (sq_pos_of_pos he)).mpr
  nlinarith [mul_pow w ε 2]

def disc (z h k : ℝ) := (z+h)^2-4*z*h*k

theorem angularDiscriminant {z h k : ℝ} (hz : 0 < z) (hh : 0 < h) (hk : k < 1) :
    0 < disc z h k := by
  unfold disc
  nlinarith [sq_nonneg (z-h),mul_pos (mul_pos hz hh) (sub_pos.mpr hk)]

theorem angularNumerator (z h k : ℝ) :
    2*disc z h k-(z-h)*(2*(z+h)-4*h*k)=4*h*(z+h)*(1-k) := by unfold disc; ring

theorem angularDerivative {z h k : ℝ} (hz : 0 < z) (hh : 0 < h) (hk : k < 1) :
    HasDerivAt (fun x => (x-h)/Real.sqrt (disc x h k))
      (2*h*(z+h)*(1-k)/(Real.sqrt (disc z h k))^3) z := by
  have hd := angularDiscriminant hz hh hk
  have hs := (Real.sqrt_pos.2 hd).ne'
  have da : HasDerivAt (fun x : ℝ => disc x h k) (2*(z+h)-4*h*k) z := by
    unfold disc
    convert ((((hasDerivAt_id z).add_const h).pow 2).sub
      (((hasDerivAt_id z).const_mul 4).mul_const h |>.mul_const k)) using 1; simp
  convert (((hasDerivAt_id z).sub_const h).div (da.sqrt hd.ne') hs) using 1
  field_simp
  set u := Real.sqrt (disc z h k)
  have hu : u^2=disc z h k := Real.sq_sqrt hd.le
  rw [show u*(2*u)=2*disc z h k by nlinarith [hu],angularNumerator,← hu]
  ring

theorem radialSlopePositive {z h k : ℝ} (hz : 0 < z) (hh : 0 < h) (hk : k < 1) :
    0 < 2*h*(z+h)*(1-k)/(Real.sqrt (disc z h k))^3 := by
  exact div_pos (mul_pos (mul_pos (mul_pos (by norm_num) hh) (add_pos hz hh)) (sub_pos.mpr hk))
    (pow_pos (Real.sqrt_pos.2 (angularDiscriminant hz hh hk)) _)

theorem commonRadialCancellation {a b : ℝ} (h : a+b=0) : b = -a := by linarith

theorem radialCovariancePair (x y fx fy : ℝ) :
    (x-y)*(fx-fy)=x*fx+y*fy-x*fy-y*fx := by ring

theorem strictRadialPair {x y fx fy : ℝ} (hx : x<y) (hf : fx<fy) :
    0 < (x-y)*(fx-fy) := mul_pos_of_neg_of_neg (sub_neg.mpr hx) (sub_neg.mpr hf)

theorem normalizedLaplacianCoefficients (v w t u : ℝ) :
    (v+w)*(t+u)+(v-w)*(t-u) = 2*(v*t+w*u) := by ring

def firstPowers : List Nat := [4+4,6+6,4+4+4+4]
theorem windowPowers : firstPowers = [8,12,16] := by decide

theorem densitySimplex : (6:ℚ)^2/40320=1/1120 := by norm_num

theorem positiveReading {h a rest : ℝ} (hh : 0<h) (ha : 0<a) (hr : 0≤rest) :
    0<h*a^2+rest := add_pos_of_pos_of_nonneg (mul_pos hh (sq_pos_of_pos ha)) hr

end YangMills.MagneticConnector
open YangMills.MagneticConnector
#print axioms markedRows
#print axioms straightPrivate
#print axioms rebaseConnector
#print axioms orthogonalDeficit
#print axioms secondMomentError
#print axioms twoStepWindow
#print axioms axialMoments
#print axioms twoStepExponent
#print axioms varianceBudget
#print axioms driftPartialBudget
#print axioms innovationIdentity
#print axioms angularDiscriminant
#print axioms angularNumerator
#print axioms angularDerivative
#print axioms radialSlopePositive
#print axioms commonRadialCancellation
#print axioms radialCovariancePair
#print axioms strictRadialPair
#print axioms normalizedLaplacianCoefficients
#print axioms windowPowers
#print axioms densitySimplex
#print axioms positiveReading
#print axioms sumPrediction
#print axioms dressingCost
