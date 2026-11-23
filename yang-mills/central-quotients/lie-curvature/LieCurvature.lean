import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

import Mathlib.Algebra.Star.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring.Finset

open scoped BigOperators
set_option maxRecDepth 10000
open MeasureTheory

namespace YangMills.LieCurvature

/-- The six monotone paths around an elementary cube, changing one adjacent pair. -/
def paths : List (List Nat) :=
  [[1,2,3],[2,1,3],[2,3,1],[3,2,1],[3,1,2],[1,3,2]]

def swaps (a b : List Nat) : Bool :=
  (a == [b[1]!,b[0]!,b[2]!] || a == [b[0]!,b[2]!,b[1]!])

theorem sixPaths : paths.length = 6 ∧
    (paths.zip (paths.drop 1 ++ paths.take 1)).all (fun p => swaps p.1 p.2) = true := by decide

theorem cubeProduct {G : Type*} [Group G] (a b c d e f : G) :
    (a*b⁻¹)*(b*c⁻¹)*(c*d⁻¹)*(d*e⁻¹)*(e*f⁻¹)*(f*a⁻¹) = 1 := by simp [mul_assoc]

def jetMul {R : Type*} [Ring R] (a b : R × R) : R × R :=
  (a.1+b.1, a.2+b.2+a.1*b.1)

theorem jetAssociative {R : Type*} [Ring R] (a b c : R × R) :
    jetMul (jetMul a b) c = jetMul a (jetMul b c) := by
  apply Prod.ext
  · exact add_assoc _ _ _
  · simp only [jetMul]
    noncomm_ring

def bracket {R : Type*} [Ring R] (x y : R) := x*y-y*x

theorem shiftedBracket {R : Type*} [Ring R] (u v : R) :
    bracket (u-1) (v-1) = bracket u v := by unfold bracket; noncomm_ring

theorem translatedCommutator {R : Type*} [Ring R] (u v ui vi : R)
    (hu : u*ui=1) (hv : v*vi=1) :
    u*v*ui*vi-1=(u*v-v*u)*ui*vi := by
  have ht : v*u*ui*vi=1 := by rw [mul_assoc v u ui,hu,mul_one,hv]
  rw [sub_mul,sub_mul,ht]

/-- Quadratic terms in an inverse-odd coordinate give one half of the bracket. -/
theorem skewProduct {R : Type*} [Ring R] [StarRing R] (a b : R)
    (ha : star a = -a) (hb : star b = -b) :
    a*b-star (a*b)=bracket a b := by simp [star_mul,ha,hb,bracket]

theorem jacobiInsertion {R : Type*} [Ring R] (b c d : R) :
    bracket b (bracket c d)-bracket d (bracket c b)=bracket c (bracket b d) := by
  unfold bracket
  noncomm_ring

theorem tensorBianchi {R : Type*} [Ring R] (B : R → R →+ ℝ)
    (hi : ∀ a b c, B (bracket a b) c=B a (bracket b c)) (a b c d : R) :
    B (bracket a b) (bracket c d)-B (bracket a d) (bracket c b)
      = B (bracket a c) (bracket b d) := by
  rw [hi,hi,hi,← map_sub,jacobiInsertion]

/-- Permuting tensor slots preserves the three norms in the Bianchi relation. -/
theorem symTensorNorm (n cross : ℝ) (h : n+n-2*cross=n) :
    (n+n+2*cross)/4=3*n/4 := by linarith

def colorDimension (n : Nat) := n*n-1
def adjointCasimir (n : Nat) := 2*n*n
def bracketSum (n : Nat) := colorDimension n * adjointCasimir n

theorem twoCharacterChecks : (bracketSum 2, bracketSum 3) = (24,144) := by decide

theorem casimirExpansion {R : Type*} [Ring R] (t : Finset ℕ) (T : ℕ → R) (x : R) :
    ∑ i ∈ t, bracket (T i) (bracket (T i) x) =
    (∑ i ∈ t, T i*T i)*x + x*(∑ i ∈ t, T i*T i)
    - ((∑ i ∈ t, T i*x*T i)+(∑ i ∈ t, T i*x*T i)) := by
  rw [Finset.sum_mul, Finset.mul_sum, ← Finset.sum_add_distrib, ← Finset.sum_add_distrib,
      ← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro i _
  unfold bracket
  noncomm_ring

def orderSign (i j : ℕ) : ℤ := if i < j then 1 else if j < i then -1 else 0
def cubeBlock (odd : Bool) (i j : ℕ) : ℤ :=
  let same : ℤ := if i=j then 3 else 0
  let opposite : ℤ := if (i+3)%6=j then 3 else 0
  if odd then same-opposite else same+opposite-1

def contraction (a b : Bool) : ℤ :=
  ((List.range 6).map fun i => ((List.range 6).map fun j =>
    ((List.range 6).map fun k => ((List.range 6).map fun l =>
      orderSign i j*orderSign k l*cubeBlock a i k*cubeBlock b j l).sum).sum).sum).sum

set_option maxHeartbeats 6000000 in
theorem cubeContractions : (contraction true true, contraction true false, contraction false false)
    = (216,0,24) := by decide

/-- Pair and triple sums in the given ordering, without a choice of Lie basis. -/
def pairs {R : Type*} [Ring R] : List R → R
  | [] => 0
  | a::xs => bracket a xs.sum + pairs xs

def triples {R : Type*} [Ring R] (form : R →+ R →+ ℝ) : List R → ℝ
  | [] => 0
  | a::xs => form (pairs xs) a + triples form xs

theorem orderedContraction {R : Type*} [Ring R] (form : R →+ R →+ ℝ)
    (hl : ∀ a b, form (bracket a b) a=0) (hr : ∀ a b, form (bracket a b) b=0)
    (xs : List R) : form (pairs xs) xs.sum = triples form xs := by
  induction xs with
  | nil => simp [pairs,triples]
  | cons a xs ih =>
    simp [pairs,triples,hl,hr,ih]

theorem gramTrace {a b : ℝ} (h : 3*a+2*b=3) : b=(3/2)*(1-a) := by linarith

theorem orderedCubeRatio {a b : ℝ} (h : 3*a+2*b=3) :
    6*a^2+2*b^2/3 = (15*a^2-6*a+3)/2 := by rw [gramTrace h]; ring

theorem cubeRatioLower {a b : ℝ} (h : 3*a+2*b=3) (ha : 1/2 < a) :
    15/8 < 6*a^2+2*b^2/3 := by
  rw [orderedCubeRatio h]
  nlinarith [sq_nonneg (a-1/2)]

theorem cubicThreshold : 3*4=12 := by decide
theorem quarticThreshold : 4*4=16 := by decide

theorem wrongSubtraction (v c q : ℝ) : c*v-q=0 ↔ q=c*v := by constructor <;> intro h <;> linarith

theorem gaussianRatio {v : ℝ} (hv : v ≠ 0) (d : ℝ) (hd : d ≠ 0) :
    d*(d+2)*v^2/(d*v)^2=(d+2)/d := by
  field_simp
  ring

theorem suThreeChannels : (bracketSum 3, 3*colorDimension 3*(adjointCasimir 3)^2)
    = (144,7776) := by decide

theorem bracketDimensionRatio {d c : ℝ} (hd : d ≠ 0) (hc : c ≠ 0) :
    (7*d*c^2/64)/(d*c/8)^2=7/d := by
  field_simp
  ring

theorem excessSecondChannel (d c v t : ℝ) :
    (2*d*t^2)*(c*v)^2+(2*d*t^2)*(c*v)^2=4*d*c^2*v^2*t^2 := by ring

theorem singletDeterminant (d c v x : ℝ) :
    (d*x^2)*(4*d*c^2*v^2*x^2+3*d*c^2*x^4)-(2*c*v*d*x^2)^2 =
    3*(d*c*x^3)^2 := by ring

theorem determinantShift (m n h k : ℝ) :
    m*(h+2*k*n+k^2*m)-(n+k*m)^2=m*h-n^2 := by ring

def symmetricNorm (n : ℕ) := 2*(n*n-1)*(n*n-4)

theorem symmetricColorChecks : (symmetricNorm 2,symmetricNorm 3,symmetricNorm 4) =
    (0,80,360) := by decide

theorem oddSelection {α : Type*} [MeasurableSpace α] {μ : Measure α} (f : α → ℝ)
    (s : α ≃ᵐ α) (hp : MeasurePreserving s μ μ) (hi : Integrable f μ)
    (hneg : ∀ x, f (s x) = -f x) : Integrable f μ ∧ ∫ x, f x ∂μ = 0 := by
  have h := hp.integral_comp' f
  simp_rw [hneg] at h
  rw [integral_neg] at h
  exact ⟨hi, by linarith⟩

theorem chargeRatio {n : ℝ} (hn : 1 < n) :
    (2*(n^2-1)*(n^2-4))/(2*n^2*(n^2-1))=1-4/n^2 := by
  have h1 : n^2-1 ≠ 0 := by nlinarith [sq_nonneg (n-1)]
  have h2 : n ≠ 0 := by linarith
  field_simp
  ring

theorem oddPlaquetteVariance : (6/12^2 : ℝ)*80*(1/2)^3=5/12 := by norm_num

end YangMills.LieCurvature

open YangMills.LieCurvature
#print axioms sixPaths
#print axioms cubeProduct
#print axioms jetAssociative
#print axioms shiftedBracket
#print axioms translatedCommutator
#print axioms skewProduct
#print axioms jacobiInsertion
#print axioms tensorBianchi
#print axioms symTensorNorm
#print axioms twoCharacterChecks
#print axioms casimirExpansion
#print axioms cubeContractions
#print axioms gramTrace
#print axioms orderedCubeRatio
#print axioms cubeRatioLower
#print axioms cubicThreshold
#print axioms quarticThreshold
#print axioms wrongSubtraction
#print axioms gaussianRatio
#print axioms suThreeChannels
#print axioms bracketDimensionRatio
#print axioms excessSecondChannel
#print axioms orderedContraction
#print axioms singletDeterminant
#print axioms determinantShift
#print axioms symmetricColorChecks
#print axioms oddSelection
#print axioms chargeRatio
#print axioms oddPlaquetteVariance
