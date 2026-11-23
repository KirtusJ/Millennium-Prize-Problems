import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

open MeasureTheory
namespace YangMills.SpatialFlow

/-- Count the lowest visible axis modes and the first modes which also move in time. -/
def modes : List (ℕ × ℕ) := (List.range 4).flatMap fun i =>
  (List.range 2).map fun sign => (i,sign)
def leading := modes.filter (fun p => p.1 < 2)
def temporal := leading.flatMap fun p => (modes.filter (fun v => v.1=3)).map fun v => (p,v)
theorem firstShells : (leading.length,temporal.length) = (4,8) := by decide

theorem singleExponential (E t h : ℝ) :
    Real.exp (-E*t)-2*Real.exp (-E*(t+h))+Real.exp (-E*(t+2*h))
    = Real.exp (-E*t)*(1-Real.exp (-E*h))^2 := by
  rw [show -E*(t+h)= -E*t+(-E*h) by ring,
      show -E*(t+2*h)=(-E*t+(-E*h))+(-E*h) by ring]
  simp only [Real.exp_add]
  ring

/-- This necessary positive-time test also permits a measure with infinite total mass. -/
theorem spectralSecondDifference (μ : Measure ℝ) (t h : ℝ)
    (i0 : Integrable (fun E : ℝ => Real.exp (-E*t)) μ)
    (i1 : Integrable (fun E : ℝ => Real.exp (-E*(t+h))) μ)
    (i2 : Integrable (fun E : ℝ => Real.exp (-E*(t+2*h))) μ) :
    0 ≤ (∫ E, Real.exp (-E*t) ∂μ)-2*(∫ E, Real.exp (-E*(t+h)) ∂μ)+
      (∫ E, Real.exp (-E*(t+2*h)) ∂μ) := by
  have isub : Integrable (fun E : ℝ => Real.exp (-E*t)-2*Real.exp (-E*(t+h))) μ :=
    i0.sub (i1.const_mul 2)
  have hp : ∀ E : ℝ, 0 ≤ Real.exp (-E*t)-2*Real.exp (-E*(t+h))+Real.exp (-E*(t+2*h)) := by
    intro E
    rw [singleExponential]
    positivity
  have hh : 0 ≤ ∫ E : ℝ, Real.exp (-E*t)-2*Real.exp (-E*(t+h))+Real.exp (-E*(t+2*h)) ∂μ := integral_nonneg hp
  rw [integral_add isub i2,integral_sub i0 (i1.const_mul 2),integral_const_mul] at hh
  exact hh

theorem negativeAgainstSpectrum {a b c : ℝ} (h : a-2*b+c<0) : ¬ 0≤a-2*b+c := not_le.mpr h

theorem subtractMean (a b c m : ℝ) :
    (a-m^2)-2*(b-m^2)+(c-m^2)=a-2*b+c := by ring

/-- Three outward-rounded upper/lower endpoints for normalized squared torus covariances. -/
def upperWitness : ℤ := 913459-2*822440+721559
theorem torusWitness : upperWitness = -9862 := by decide

theorem torusUpper {a b c : ℝ} (ha : a≤913459/1000000)
    (hb : 822440/1000000≤b) (hc : c≤721559/1000000) :
    a-2*b+c ≤ -9862/1000000 := by linarith

theorem midpointObstruction {a b c : ℝ} (ha : 0 ≤ a) (hc : 0 ≤ c) (h : a+c<2*b) :
    a*c<b^2 := by
  have hb : 0 ≤ b := by linarith
  nlinarith [mul_pos (show 0<2*b-(a+c) by linarith) (show 0<2*b+(a+c) by linarith),
    sq_nonneg (a-c)]

theorem secondShellSign {c u : ℝ} (hc : 0<c) (hu : u<1) :
    2*c*(u-1)<0 := mul_neg_of_pos_of_neg (by positivity) (sub_neg.mpr hu)

theorem smoothingCurvature {a u : ℝ} (ha : 0<a) (ha2 : a<2)
    (h : u≤1/4) : a*(2*a*u-1)<0 := by
  apply mul_neg_of_pos_of_neg ha
  nlinarith [mul_nonneg ha.le (sub_nonneg.mpr h)]

theorem gaussianSecondDerivative (c : ℝ) (x : ℝ) :
    HasDerivAt (fun t : ℝ => -2*c*t*Real.exp (-c*t^2))
      (2*c*(2*c*x^2-1)*Real.exp (-c*x^2)) x := by
  have h1 := ((hasDerivAt_id x).pow 2).const_mul (-c)
  have h2 := (((hasDerivAt_id x).const_mul (-2*c)).mul h1.exp)
  convert h2 using 1; simp; ring

def densityPower (base : ℕ) : ℕ := base+1
theorem thresholdPowers : (densityPower 4,4+4) = (5,8) := by decide

theorem positiveCutoff {s e : ℝ} (he : 0<e) : 0<e^4*Real.exp (-s*e^2) := by positivity

theorem projectedTrace (a b c : ℝ) (h : a^2+b^2+c^2=1) :
    (1-a^2)^2+(1-b^2)^2+(1-c^2)^2+2*((a*b)^2+(a*c)^2+(b*c)^2)=2 := by
  nlinarith [congrArg (fun x : ℝ => x^2) h]

theorem energyRatio : ((1/32:ℚ)/(3/128))=4/3 := by norm_num

theorem continuumWitness {a b c : ℝ} (ha : a≤960/1000) (hb : 910/1000≤b)
    (hc : c≤848/1000) : a-2*b+c ≤ -12/1000 := by linarith

theorem heatDifference {k : ℝ} (h : 0<k) : 0<k/4 := by positivity

/-- One summable initial defect permits a persistent discrepancy even with common initial data. -/
def mismatch (n : ℕ) : ℝ := if n=0 then 0 else 1
def defect (n : ℕ) : ℝ := if n=0 then 1 else 0
theorem persistentDiscrepancy (n : ℕ) :
    mismatch 0=0 ∧ mismatch (n+1)=1 ∧ mismatch (n+1)≤mismatch n+defect n := by
  cases n <;> simp [mismatch,defect]

/-- A positive rank-one remainder annihilates the first basis vector but can be measured
    between two equal swap insertions on that vector. -/
def swap (v : ℝ × ℝ) := (v.2,v.1)
def remOp (v : ℝ × ℝ) : ℝ × ℝ := (0,v.2)
def vacuum : ℝ × ℝ := (1,0)
theorem insertionSeesRemainder : remOp vacuum=(0,0) ∧
    (swap (remOp (swap vacuum))).1=1 ∧ (∀ v : ℝ × ℝ, 0≤v.1*(remOp v).1+v.2*(remOp v).2) := by
  refine ⟨rfl,rfl,?_⟩
  intro v
  simp [remOp,mul_self_nonneg]

end YangMills.SpatialFlow
open YangMills.SpatialFlow
#print axioms firstShells
#print axioms singleExponential
#print axioms spectralSecondDifference
#print axioms negativeAgainstSpectrum
#print axioms subtractMean
#print axioms torusWitness
#print axioms torusUpper
#print axioms midpointObstruction
#print axioms secondShellSign
#print axioms smoothingCurvature
#print axioms gaussianSecondDerivative
#print axioms thresholdPowers
#print axioms positiveCutoff
#print axioms projectedTrace
#print axioms energyRatio
#print axioms continuumWitness
#print axioms heatDifference
#print axioms persistentDiscrepancy
#print axioms insertionSeesRemainder
