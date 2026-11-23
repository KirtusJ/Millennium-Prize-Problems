import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

open scoped BigOperators InnerProductSpace Interval
open MeasureTheory
namespace Millennium.YangMills.D4.ElectricSlab

/-- T is the intervening propagation and B inserts a whole slab. -/
theorem slabCenter {V : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
    (T B : V →ₗ[ℝ] V) (o : V) (m : ℝ) (hT : T o = o)
    (hTs : ∀ x y, ⟪x, T y⟫_ℝ = ⟪T x, y⟫_ℝ)
    (hB : ∀ x y, ⟪x, B y⟫_ℝ = ⟪B x, y⟫_ℝ)
    (unit : ⟪o, o⟫_ℝ = 1) (mass : ⟪o, B o⟫_ℝ = m) :
    ⟪B o-m • o,T (B o-m • o)⟫_ℝ = ⟪o,B (T (B o))⟫_ℝ-m^2 := by
  have rev : ⟪B o,o⟫_ℝ=m := (real_inner_comm _ _).trans mass
  have left : ⟪o,T (B o)⟫_ℝ=m := by rw [hTs,hT,mass]
  rw [hB o]
  simp only [map_sub, map_smul, hT, inner_sub_left, inner_sub_right,
    real_inner_smul_left, real_inner_smul_right, rev, left, unit]
  ring

/-- Discrete product rule for the positive graph Laplacian at one site. -/
theorem cutoffLaplacian {ι : Type*} (s : Finset ι) (a b : ℝ) (f g : ι → ℝ) :
    (∑ i ∈ s, (a*b-f i*g i)) =
    a*(∑ i ∈ s, (b-g i)) + b*(∑ i ∈ s, (a-f i)) -
    ∑ i ∈ s, (f i-a)*(g i-b) := by
  rw [Finset.mul_sum, Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro i _
  ring

/-- Uniform absolute error propagation in the Gaussian moment recursion. -/
theorem momentStep (e v a b u : ℝ) (h : |e-v*a| ≤ u) (ha : |a| ≤ b) :
    |e| ≤ u+|v| * b := by
  calc
    |e| = |(e-v*a)+(v*a)| := by ring_nf
    _ ≤ |e-v*a|+|v*a| := abs_add_le _ _
    _ ≤ _ := by rw [abs_mul]; exact add_le_add h (mul_le_mul_of_nonneg_left ha (abs_nonneg _))

noncomputable def phase (E k : ℝ) := (E^2-k^2)^2 + 8/15*k^4

theorem phasePositive (E k : ℝ) (h : 0 < E) :
    0 < phase E k := by
  unfold phase
  by_cases hk : k=0
  · simp [hk, h.ne'] ; positivity
  · have h4 : 0 < k^4 := by positivity
    nlinarith only [sq_nonneg (E^2-k^2),h4]

theorem threshold (k : ℝ) : phase k k=8/15*k^4 := by unfold phase; ring

def angular (E k z : ℝ) :=
  (E^2-k^2*z^2)^2+(2*k^2-E^2-k^2*z^2)^2

theorem angularExpansion (E k z : ℝ) :
    angular E k z = (2*E^4-4*E^2*k^2+4*k^4) + (-4*k^4)*z^2 + (2*k^4)*z^4 := by
  unfold angular
  ring

theorem angularIntegral (E k : ℝ) : (∫ z in (-1:ℝ)..1, angular E k z)=4*phase E k := by
  simp_rw [angularExpansion]
  rw [intervalIntegral.integral_add (by apply Continuous.intervalIntegrable; fun_prop) (by apply Continuous.intervalIntegrable; fun_prop)]
  rw [intervalIntegral.integral_add, intervalIntegral.integral_const, intervalIntegral.integral_const_mul,
      intervalIntegral.integral_const_mul, integral_pow, integral_pow]
  · unfold phase
    norm_num
    ring
  all_goals apply Continuous.intervalIntegrable; fun_prop

def spatialPolynomial (t s : ℝ) := (t^2+s)^2+2*(s-t^2)^2

theorem restReading (t : ℝ) (ht : t ≠ 0) :
    spatialPolynomial t 0/(384*(t^2+0)^6) = 1/(128*t^8) := by
  unfold spatialPolynomial
  field_simp
  ring

def step (site axis : ℕ) : ℕ :=
  let stride := [1,4,12,36][axis]!
  let size := if axis=0 then 4 else 3
  if site/stride%size+1=size then site-(size-1)*stride else site+stride

def meets (s i j bond : ℕ) : Bool :=
  let x := bond/4
  let a := bond%4
  (a==i && (x==s || x==step s j)) || (a==j && (x==s || x==step s i))

def faceCount (bond : ℕ) : ℕ :=
  ((List.range 108).map fun s => ((List.range 4).map fun i =>
    ((List.range 4).filter fun j => i<j && meets s i j 0 && meets s i j bond).length).sum).sum

/-- Orthogonality of a row of the four-dimensional inversion fixes its scalar sum. -/
theorem scalarOrientation (I : Fin 4 → ℝ) (unit : ∑ i, (I i)^2 = 1) :
    (∑ i, (1+2*(I i)^2))/4=3/2 := by
  rw [Finset.sum_add_distrib, ← Finset.mul_sum, unit]
  norm_num

/-- Radial bi-Laplacian of (h+s)^(-2), with h=t^2 and s the squared radius. -/
theorem tensorInverse (h s : ℝ) (hs : h+s ≠ 0) :
    60*(6/(h+s)^4) + 80*s*(-24/(h+s)^5) + 16*s^2*(120/(h+s)^6) =
    120*(3*h^2-10*h*s+3*s^2)/(h+s)^6 := by
  field_simp
  ring

theorem splitChannels (h s : ℝ) :
    2*((h+s)^2+2*(s-h)^2) = 3*(h+s)^2+(3*h^2-10*h*s+3*s^2) := by ring

theorem mixedConeValue (t : ℝ) (ht : t ≠ 0) :
    3*(t^2)^2-10*t^2*t^2+3*(t^2)^2 < 0 := by
  have h4 : 0 < t^4 := by positivity
  nlinarith only [h4]

/-- Conjugating a signed cycle by the Hodge involution preserves its trace. -/
theorem oddTrace {n : Type*} [Fintype n] [DecidableEq n] (J M : Matrix n n ℝ)
    (hj : J*J=1) (hm : J*M=-(M*J)) : Matrix.trace M=0 := by
  have left : J*M*J = -M := by rw [hm, neg_mul, Matrix.mul_assoc, hj, mul_one]
  have same : Matrix.trace (J*M*J)=Matrix.trace M := by
    rw [Matrix.trace_mul_comm (J*M) J, ← Matrix.mul_assoc, hj, one_mul]
  rw [left, Matrix.trace_neg] at same
  linarith

-- BEGIN PCP OS generated slab controls
theorem latticeIncidence : faceCount 0=6 ∧ faceCount 4=0 ∧ faceCount 16=1 := by decide

theorem marginalPolynomial (z : ℝ) : z^2*phase 1 z=z^2-2*z^4+(23/15)*z^6 := by unfold phase; ring

theorem marginalConstant : (1:ℝ)/3-2/5+(23/15)/7=16/105 := by norm_num

theorem marginalIntegral : (∫ z in (0:ℝ)..1, z^2*phase 1 z)=16/105 := by
  simp_rw [marginalPolynomial]
  rw [intervalIntegral.integral_add,intervalIntegral.integral_sub,intervalIntegral.integral_const_mul,intervalIntegral.integral_const_mul,integral_pow,integral_pow,integral_pow]
  · norm_num
  all_goals apply Continuous.intervalIntegrable; fun_prop

theorem collinearWeights : (8*9:ℚ)^2/(2*9)^3=8/9 ∧ (16*18:ℚ)/(2*18)^2=2/9 := by norm_num

#print axioms oddTrace
#print axioms collinearWeights
#print axioms scalarOrientation
#print axioms tensorInverse
#print axioms splitChannels
#print axioms mixedConeValue
#print axioms slabCenter
#print axioms cutoffLaplacian
#print axioms momentStep
#print axioms angularExpansion
#print axioms angularIntegral
#print axioms phasePositive
#print axioms threshold
#print axioms restReading
#print axioms latticeIncidence
#print axioms marginalPolynomial
#print axioms marginalConstant
#print axioms marginalIntegral
end Millennium.YangMills.D4.ElectricSlab
