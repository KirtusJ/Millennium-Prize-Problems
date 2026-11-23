import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Analysis.Calculus.Deriv.Pow
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

import Mathlib.MeasureTheory.Integral.Bochner.Basic

open MeasureTheory

namespace YangMills.TangentCurvature

/-- Each of the four coordinates of a cube cell is low, high or free. -/
def cellCounts : ℕ → List ℕ
  | 0 => [1]
  | d+1 => let a := cellCounts d
           (a.map (2*·) ++ [0]).zipWith (·+·) (0::a)

theorem fourCubeCounts : cellCounts 4 = [16,32,24,8,1] := by decide

/-- In each coordinate a missing bit is fixed at the lower or upper endpoint. -/
def cells (k : ℕ) : List (Nat × Nat) :=
  ((List.range 16).flatMap fun m => (List.range 16).map fun v => (m,v)).filter
    fun (m,v) => (m &&& v) == 0 && ((List.range 4).filter fun i => m.testBit i).length == k

def incident (high low : Nat × Nat) : Bool :=
  (List.range 4).any fun i => high.1.testBit i &&
    low.1 == high.1 - 2^i && (low.2 == high.2 || low.2 == high.2 + 2^i)

def row (columns : List (Nat × Nat)) (high : Nat × Nat) : UInt32 :=
  columns.zipIdx.foldl (fun bits entry =>
    if incident high entry.1 then bits ||| ((1 : UInt32) <<< entry.2.toUInt32) else bits) 0

/-- Eliminate pivot columns of a binary matrix from low to high. -/
def binaryRank (rows : List UInt32) : ℕ :=
  ((List.range 32).foldl (fun (state : ℕ × List UInt32) i =>
    let mask := (1 : UInt32) <<< i.toUInt32
    match state.2.find? (fun x => x &&& mask != 0) with
    | none => state
    | some pivot => (state.1+1, state.2.map (fun x => if x &&& mask != 0 then x ^^^ pivot else x)))
    (0,rows)).1

def incidenceRank (k : ℕ) : ℕ := binaryRank ((cells (k+1)).map (row (cells k)))

set_option maxRecDepth 10000 in
set_option maxHeartbeats 8000000 in
theorem cubeRanks : (incidenceRank 1, incidenceRank 2) = (17,7) := by decide

theorem exactFaceCount : 24-7 = (17 : ℕ) := by decide

/-- The alternating face sum of a gradient vanishes. -/
theorem squareGradient (a b c d : ℝ) : (b-a)+(c-b)-(c-d)-(d-a) = 0 := by ring

/-- Unit quaternion scalar deficit and the magnitude of its imaginary part. -/
theorem quaternionDeficit {w x y z : ℝ} (hs : w^2+x^2+y^2+z^2=1) :
    2*(1-w) = x^2+y^2+z^2+(1-w)^2 := by nlinarith

theorem temporalTilt {γ u logRatio cost : ℝ} (hγ : 0 < γ)
    (ht : γ*u/2 ≤ logRatio+cost) : u ≤ 2*(logRatio+cost)/γ := by
  apply (le_div_iff₀ hγ).2
  linarith

/-- The signed local incidence at an interior edge has squared norm six. -/
theorem edgeVariance (x y z : ℝ) :
    3*(x^2+y^2+z^2)+3*((-x)^2+(-y)^2+(-z)^2)=6*(x^2+y^2+z^2) := by ring

/-- Integrating factor for either real component of the Ward characteristic ODE. -/
theorem wardCharacteristic (a b : ℝ) (f : ℝ → ℝ)
    (h : ∀ t, HasDerivAt f (-(a+b*t)*f t) t) (t : ℝ) :
    f t = f 0 * Real.exp (-(a*t+b*t^2/2)) := by
  let q := fun s : ℝ => a*s+b*s^2/2
  have hq (s : ℝ) : HasDerivAt q (a+b*s) s := by
    have h1 := ((hasDerivAt_id s).const_mul a).add
      ((((hasDerivAt_id s).pow 2).const_mul b).div_const 2)
    convert h1 using 1
    simp [q]
    ring
  have hz (s : ℝ) : HasDerivAt (fun r => f r * Real.exp (q r)) 0 s := by
    convert (h s).mul (hq s).exp using 1
    ring
  have hc := is_const_of_deriv_eq_zero (fun s => (hz s).differentiableAt)
    (fun s => (hz s).deriv) t 0
  change f t * Real.exp (q t) = f 0 * Real.exp (q 0) at hc
  simp [q] at hc
  rw [Real.exp_neg, ← hc]
  field_simp

/-- Completing the square after removal of the Gaussian projection. -/
theorem residualFactor (g u : ℝ) :
    -g*(u-g)-(u-g)^2/2=g^2/2-u^2/2 := by ring

theorem projectionDiagonal {a b c d : ℝ} (h : a+b+c+d ≠ 0) :
    (a+b)/(a+b+c+d)+(c+d)/(a+b+c+d)=1 := by
  field_simp
  ring

theorem traceOfProjection {a b c d : ℝ} (h : a+b+c+d ≠ 0) :
    ((a+b)+(a+c)+(a+d)+(b+c)+(b+d)+(c+d))/(a+b+c+d)=3 := by
  field_simp
  ring

theorem colorFloor {D H loss : ℝ} (hh : 0 ≤ H) (hl : 0 ≤ loss)
    (h : 3*(1/2:ℝ)+H+loss ≤ 2*D) : 3/4 ≤ D := by linarith

theorem harmonicDifference {u v cross : ℝ} (hu : u=cross) (hv : v=cross) :
    u+v-2*cross=0 := by linarith

/-- A temporal Fourier coefficient solves the second-order Green recurrence. -/
theorem greenInterior {r t : ℝ} (hr : r ≠ 0) (ht : t = r+r⁻¹) (n : ℕ) :
    t*r^(n+1)-r^n-r^(n+2)=0 := by
  rw [ht, pow_succ, pow_succ, pow_succ]
  field_simp
  ring

theorem greenSource {r : ℝ} (h : r⁻¹-r ≠ 0) :
    ((r+r⁻¹)-2*r)/(r⁻¹-r)=1 := by
  apply (div_eq_one_iff_eq h).2
  ring

theorem radialCoefficient {p : ℝ} (hp : p ≠ 0) :
    (120*(8*p/15))/(2*(2*p)^3)=4/p^2 := by
  field_simp
  ring

theorem doubledThreshold : (Nat.choose 12 6)*Nat.factorial 6^2 = Nat.factorial 12 := by decide

/-- Reflection gives a nonpositive expectation of a nonnegative square. -/
theorem oddReflectionVanishes {α : Type*} [MeasurableSpace α] {μ : Measure α}
    (f : α → ℝ) {c : ℝ} (hc : 0 < c) (hi : Integrable (fun x => (f x)^2) μ)
    (hr : 0 ≤ -c * ∫ x, (f x)^2 ∂μ) : ∀ᵐ x ∂μ, f x = 0 := by
  have hpos : 0 ≤ ∫ x, (f x)^2 ∂μ := integral_nonneg fun x => sq_nonneg (f x)
  have hzero : (∫ x, (f x)^2 ∂μ) = 0 := by nlinarith
  have he := (integral_eq_zero_iff_of_nonneg (fun x => sq_nonneg (f x)) hi).1 hzero
  filter_upwards [he] with x hx
  change (f x)^2 = 0 at hx
  nlinarith

theorem singleFaceCoefficient {p : ℝ} (hp : p ≠ 0) :
    (6*(8*p/3))/(2*(2*p)^3)=1/p^2 := by
  field_simp
  ring

theorem faceThreshold : (Nat.choose 8 4)*Nat.factorial 4^2 = Nat.factorial 8 := by decide

/-- Iterating site-reflection Cauchy-Schwarz over successive doubled blocks. -/
theorem iterateReflection (a : ℕ → ℝ) (hn : ∀ i, 0 ≤ a i)
    (h : ∀ i, (a i)^2 ≤ a (i+1)) (n : ℕ) : (a 0)^(2^n) ≤ a n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, pow_mul]
    exact (pow_le_pow_left₀ (pow_nonneg (hn 0) _) ih 2).trans (h n)

/-- The unbounded action is one half of the squared length of three colors. -/
theorem actionMoments : ((3/4 : ℝ)^2+3/8=15/16) ∧ (3/2 : ℝ)*(1/2)^2=3/8 := by
  norm_num

end YangMills.TangentCurvature

open YangMills.TangentCurvature
#print axioms fourCubeCounts
#print axioms cubeRanks
#print axioms exactFaceCount
#print axioms squareGradient
#print axioms quaternionDeficit
#print axioms temporalTilt
#print axioms edgeVariance
#print axioms wardCharacteristic
#print axioms residualFactor
#print axioms projectionDiagonal
#print axioms traceOfProjection
#print axioms colorFloor
#print axioms harmonicDifference
#print axioms greenInterior
#print axioms greenSource
#print axioms radialCoefficient
#print axioms doubledThreshold
#print axioms oddReflectionVanishes
#print axioms singleFaceCoefficient
#print axioms faceThreshold
#print axioms iterateReflection
#print axioms actionMoments
