import Mathlib.Data.Matrix.Notation
import Mathlib.LinearAlgebra.Matrix.NonsingularInverse
import Mathlib.Analysis.SpecialFunctions.Gamma.Basic
import Mathlib.Tactic.FinCases
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace Millennium.YangMills.WeakCavity
open MeasureTheory Set
noncomputable section

def curl (x y z : ℝ) : Matrix (Fin 3) (Fin 3) ℝ := !![0,-z,y; z,0,-x; -y,x,0]
def normal (x y z : ℝ) : Matrix (Fin 3) (Fin 3) ℝ :=
  fun i j => ![x,y,z] i * ![x,y,z] j

/-- Curl squared on a product mode is scalar after removal of the gradient. -/
theorem transverseCurl (x y z : ℝ) : (curl x y z).transpose * curl x y z + normal x y z =
    (x^2+y^2+z^2) • (1 : Matrix (Fin 3) (Fin 3) ℝ) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [curl, normal, Matrix.mul_apply, Matrix.one_apply, Fin.sum_univ_succ] <;> ring

theorem curlEnergy (x y z a b c : ℝ) :
    (y*c-z*b)^2+(z*a-x*c)^2+(x*b-y*a)^2 =
    (x^2+y^2+z^2)*(a^2+b^2+c^2)-(x*a+y*b+z*c)^2 := by ring

theorem triangleMetric (x y z a b c : ℝ) (h : x*a+y*b+z*c=0) :
    (y*c-z*b)^2+(z*a-x*c)^2+(x*b-y*a)^2 =
    (x^2+y^2+z^2)*(a^2+b^2+c^2) := by rw [curlEnergy,h]; ring

/-- The Gram matrix of tree-reduced increments must enter the magnetic Hessian. -/
theorem reducedCurl {ι κ μ : Type*} [Fintype ι] [Fintype κ]
    (d : Matrix μ ι ℝ) (C : Matrix ι κ ℝ) :
    (d*C)*(d*C).transpose = d*(C*C.transpose)*d.transpose := by
  rw [Matrix.transpose_mul]
  simp only [Matrix.mul_assoc]

theorem mehlerInvariant (η ω : ℝ) :
    (1+η^2*ω^2/2)^2-1 = η^2*(ω^2*(1+η^2*ω^2/4)) := by ring

theorem singletFloor (e a b : ℝ) (ha : e ≤ a) (hb : e ≤ b) : 2*e ≤ a+b := by linarith

theorem colorVector (x y z : ℝ) (hx : x = -x) (hy : y = -y) (hz : z = -z) :
    x=0 ∧ y=0 ∧ z=0 := by exact ⟨by linarith,by linarith,by linarith⟩

/-- Half-turns kill off-diagonal coefficients; the cyclic spatial color rotation
    equates the remaining three. This is the coefficient form for SU(2) adjoint colors. -/
theorem colorBilinear (A : Matrix (Fin 3) (Fin 3) ℝ)
    (signs : ∀ i j, i ≠ j → A i j = -A i j)
    (h₁ : A 0 0 = A 1 1) (h₂ : A 1 1 = A 2 2) : A = A 0 0 • 1 := by
  ext i j
  by_cases h : i=j
  · subst j
    fin_cases i <;> simp [Matrix.one_apply] <;> linarith
  · have q := signs i j h
    simp [Matrix.one_apply,h]
    linarith

theorem bentReading (u v t : ℝ) : ((u+v+2*t)-(u+v-2*t))/4=t := by ring

-- PCP begin geometry
theorem wickColors (d v c : ℝ) :
    d*(v^2+2*c^2)+d*(d-1)*v^2-(d*v)^2=2*d*c^2 := by ring
-- PCP end geometry

theorem radialAngular (a b c : ℝ) : (a+b)+(b+c)+(c+a)=2*(a+b+c) := by ring

theorem laplaceSeven {t : ℝ} (ht : 0<t) :
    (∫ E : ℝ in Ioi 0, E^7 * Real.exp (-(t*E))) = 5040/t^8 := by
  have h := Real.integral_rpow_mul_exp_neg_mul_Ioi (a := 8) (by norm_num) ht
  have hg : Real.Gamma 8 = 5040 := by
    convert Real.Gamma_nat_eq_factorial 7 using 1
    norm_num [Nat.factorial]
  have h₇ (x : ℝ) : x^(7:ℝ) = x^(7:ℕ) := Real.rpow_natCast x 7
  have h₈ (x : ℝ) : x^(8:ℝ) = x^(8:ℕ) := Real.rpow_natCast x 8
  rw [show (8:ℝ)-1=7 by norm_num, hg, h₈] at h
  simp only [h₇] at h
  rw [h]
  field_simp

/-- The nonzero three-point Wick cycle is fixed by the number of adjoint colors. -/
theorem triangleRatio (d x y z : ℝ) :
    d*(8*d*x*y*z)^2=8*((2*d*x^2)*(2*d*y^2)*(2*d*z^2)) := by ring

theorem spectralWindow (d E : ℝ) (hd : 0<d) (hE : 0<E) : 0<2*d*E^7 := by positivity

theorem continuumTensor (t x y z : ℝ) :
    4*(t^2+x^2+y^2+z^2)-8*(x^2+y^2+z^2)+8*z^2 =
      4*(t^2-x^2-y^2+z^2) := by ring

/-- A conjugate pair of adjoint eigenphases contributes this exact determinant. -/
theorem twistPair (q c s : ℝ) (circle : c^2+s^2=1) :
    (1-q*c)^2+(q*s)^2=(1-q)^2+2*q*(1-c) := by
  nlinarith [congrArg (fun t : ℝ => q^2*t) circle]

/-- The SU(2) conjugacy-angle factor in the thermal group projection. -/
theorem adjointAngle (q v : ℝ) : (1-q)^2+2*q*(1-(1-2*v^2))=(1-q)^2+4*q*v^2 := by ring

/-- Relative domination of a signed kernel error in a tested Lebesgue form.
    The underlying space can be the product of both endpoint configurations. -/
theorem kernelForm {X : Type*} [MeasurableSpace X] (μ : Measure X)
    (w K R : X → ℝ) (ε : ℝ) (hw : Integrable (fun x => w x * R x) μ)
    (hK : Integrable (fun x => |w x| * K x) μ)
    (dom : ∀ᵐ x ∂μ, |R x| ≤ ε*K x) :
    |∫ x, w x * R x ∂μ| ≤ ε * ∫ x, |w x| * K x ∂μ := by
  calc
    _ ≤ ∫ x, |w x * R x| ∂μ := by
      simpa only [Real.norm_eq_abs] using (norm_integral_le_integral_norm (μ := μ) (fun x => w x*R x))
    _ ≤ ∫ x, ε*(|w x| *K x) ∂μ := by
      apply integral_mono_ae hw.abs (hK.const_mul ε)
      filter_upwards [dom] with x hx
      rw [abs_mul]
      calc
        _ ≤ |w x| *(ε*K x) := mul_le_mul_of_nonneg_left hx (abs_nonneg _)
        _ = _ := by ring
    _ = _ := integral_const_mul _ _

/-- A positive closed path inherits one multiplicative comparison per bond. -/
theorem closedPath {ι : Type*} (S : Finset ι) (f h : ι → ℝ) (c : ℝ)
    (positive : ∀ i ∈ S, 0 ≤ f i) (dom : ∀ i ∈ S, f i ≤ c*h i) :
    ∏ i ∈ S, f i ≤ c^S.card * ∏ i ∈ S, h i := by
  calc
    _ ≤ ∏ i ∈ S, (c*h i) := Finset.prod_le_prod positive dom
    _ = _ := by rw [Finset.prod_mul_distrib, Finset.prod_const]

/-- Sum the squared ribbon bounds using the maximum number of chords through a face. -/
theorem ribbonSum {ι κ : Type*} [Fintype ι] [Fintype κ]
    (A : ι → κ → ℝ) (cost : ι → ℝ) (face : κ → ℝ) (l m : ℝ)
    (hl : 0≤l) (hp : ∀ p, 0≤face p) (uses : ∀ p, ∑ i, A i p ≤ m)
    (row : ∀ i, cost i ≤ l*∑ p, A i p * face p) :
    ∑ i, cost i ≤ l*m*∑ p, face p := by
  calc
    _ ≤ ∑ i, l*∑ p, A i p * face p := Finset.sum_le_sum fun i _ => row i
    _ = l*∑ p, (∑ i, A i p)*face p := by
      rw [← Finset.mul_sum]
      congr 1
      rw [Finset.sum_comm]
      simp only [Finset.sum_mul]
    _ ≤ l*∑ p, m*face p := by
      exact mul_le_mul_of_nonneg_left
        (Finset.sum_le_sum fun p _ => mul_le_mul_of_nonneg_right (uses p) (hp p)) hl
    _ = _ := by rw [← Finset.mul_sum, mul_assoc]

-- PCP begin certificate
def cubeA : Matrix (Fin 6) (Fin 6) ℤ := !![4,0,-1,-1,-1,-1; 0,4,-1,-1,-1,-1; -1,-1,4,0,-1,-1; -1,-1,0,4,-1,-1; -1,-1,-1,-1,4,0; -1,-1,-1,-1,0,4]

set_option maxRecDepth 10000 in
set_option maxHeartbeats 3000000 in
theorem cubePolynomial : cubeA*(cubeA-4•1)*(cubeA-6•1)=0 := by decide

theorem cubeSpectrum (a b : ℝ) (tr : 4*a+6*b=24) (tr₂ : 16*a+36*b=120) :
    a=3 ∧ b=2 := by constructor <;> linarith
-- PCP end certificate

end
#print axioms transverseCurl
#print axioms curlEnergy
#print axioms triangleMetric
#print axioms reducedCurl
#print axioms mehlerInvariant
#print axioms singletFloor
#print axioms colorVector
#print axioms colorBilinear
#print axioms bentReading
#print axioms wickColors
#print axioms radialAngular
#print axioms laplaceSeven
#print axioms triangleRatio
#print axioms spectralWindow
#print axioms continuumTensor
#print axioms twistPair
#print axioms adjointAngle
#print axioms kernelForm
#print axioms closedPath
#print axioms ribbonSum
#print axioms cubePolynomial
#print axioms cubeSpectrum
end Millennium.YangMills.WeakCavity
