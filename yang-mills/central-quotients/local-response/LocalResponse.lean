import Mathlib.Analysis.Calculus.Deriv.Mul
import Mathlib.Analysis.Calculus.Deriv.Add
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace YangMills.CentralQuotient.LocalResponse

def lateralWeight (odd : Bool) : ℕ :=
  ((List.range 16).map fun mask =>
    let k := ((List.range 4).filter mask.testBit).length
    if (k % 2 == 1) == odd then 4^(4-k) else 0).sum

theorem lateralCensus : lateralWeight false = 353 ∧ lateralWeight true = 272 := by decide +kernel

/-- Uniform average over a single unbiased center sign. -/
noncomputable def signAverage (f : ℝ → ℝ) : ℝ := (f 1 + f (-1)) / 2

/-- Conditional face parity fixes the fourth lateral sign from the other three. -/
theorem cubeParityAverage (p a b c d : ℝ) :
    signAverage (fun x => signAverage (fun y => signAverage (fun z =>
      (1+a*x)*(1+b*y)*(1+c*z)*(1+d*p*x*y*z)))) = 1 + p*a*b*c*d := by
  unfold signAverage
  ring

/-- Mean of the next sign conditioned on the preceding sign. Here j is its
signed bond, including the preceding sign, and m is the effective suffix bias. -/
noncomputable def nextMean (m j : ℝ) : ℝ := (m+j)/(1+m*j)

noncomputable def transmission (m j : ℝ) : ℝ := j*(1-m^2)/(1-(m*j)^2)

private theorem mul_abs_lt_one {m j : ℝ} (hm : |m| ≤ 1) (hj : |j| < 1) :
    |m*j| < 1 := by
  rw [abs_mul]
  calc |m| * |j| ≤ 1 * |j| := mul_le_mul_of_nonneg_right hm (abs_nonneg j)
       _ < 1 := by simpa using hj

theorem conditionalSlope {m j : ℝ} (hm : |m| ≤ 1) (hj : |j| < 1) :
    (nextMean m j - nextMean m (-j))/2 = transmission m j := by
  obtain ⟨lo,hi⟩ := abs_lt.mp (mul_abs_lt_one hm hj)
  have hp : 1+m*j ≠ 0 := by linarith
  have hn : 1-m*j ≠ 0 := by linarith
  have hprod : 1-(m*j)^2 ≠ 0 := by
    rw [show 1-(m*j)^2 = (1-m*j)*(1+m*j) by ring]
    exact mul_ne_zero hn hp
  simp only [nextMean, transmission, mul_neg, ← sub_eq_add_neg]
  field_simp [hp, hn, hprod]
  ring


theorem signedChannelExample : (nextMean (3/5) (1/2) - nextMean (3/5) (-(1/2)))/2 =
    (32/91 : ℝ) := by norm_num [nextMean]
/-- Uniform over every suffix field. Equality holds when m = 0. -/
theorem transmissionBound {m j : ℝ} (hm : |m| ≤ 1) (hj : |j| < 1) :
    |transmission m j| ≤ |j| := by
  obtain ⟨mlo,mhi⟩ := abs_le.mp hm
  obtain ⟨jlo,jhi⟩ := abs_lt.mp hj
  obtain ⟨lo,hi⟩ := abs_lt.mp (mul_abs_lt_one hm hj)
  have hm2 : 0 ≤ 1-m^2 := by nlinarith [mul_nonneg (by linarith : 0 ≤ 1-m) (by linarith : 0 ≤ 1+m)]
  have hj2 : 0 ≤ 1-j^2 := by nlinarith [mul_nonneg (by linarith : 0 ≤ 1-j) (by linarith : 0 ≤ 1+j)]
  have hd : 0 < 1-(m*j)^2 := by
    nlinarith [mul_pos (by linarith : 0 < 1-m*j) (by linarith : 0 < 1+m*j)]
  have hsmall : 1-m^2 ≤ 1-(m*j)^2 := by nlinarith [mul_nonneg (sq_nonneg m) hj2]
  rw [transmission, abs_div, abs_mul, abs_of_nonneg hm2, abs_of_pos hd, div_le_iff₀ hd]
  exact mul_le_mul_of_nonneg_left hsmall (abs_nonneg j)

theorem zeroFieldSharp (j : ℝ) : transmission 0 j = j := by simp [transmission]

theorem stripPropagation (v m j B : ℕ → ℝ)
    (bias : ∀ n, |m n| ≤ 1) (bond : ∀ n, |j n| < 1)
    (majorant : ∀ n, |j n| ≤ B n)
    (step : ∀ n, v (n+1) = transmission (m n) (j n) * v n) (d : ℕ) :
    |v d| ≤ |v 0| * ∏ i ∈ Finset.range d, B i := by
  induction d with
  | zero => simp
  | succ n ih =>
    rw [step, abs_mul, Finset.prod_range_succ]
    calc
      _ ≤ B n * |v n| :=
        mul_le_mul_of_nonneg_right ((transmissionBound (bias n) (bond n)).trans (majorant n)) (abs_nonneg _)
      _ ≤ B n * (|v 0| * ∏ i ∈ Finset.range n, B i) :=
        mul_le_mul_of_nonneg_left ih ((abs_nonneg _).trans (majorant n))
      _ = _ := by ring

/-- Both endpoints have bare bias m and the interior has effective bond k. -/
theorem endpointCovariance (m k : ℝ) (h : 1+k*m^2 ≠ 0) :
    (m^2+k)/(1+k*m^2) - (m*(1+k)/(1+k*m^2))^2 =
      k*(1-m^2)^2/(1+k*m^2)^2 := by
  field_simp
  ring

/-- The missing two-step return through the orthogonal complement.
The algebraic identity needs only idempotence. -/
theorem twoStepDifference {A : Type*} [Ring A] (P T : A) (hP : P*P = P) :
    P*T^2*P - (P*T*P)^2 = P*T*(1-P)*T*P := by
  have cancel : (P*T*P)^2 = P*T*P*T*P := by
    calc (P*T*P)^2 = P*T*(P*P)*T*P := by noncomm_ring
         _ = _ := by rw [hP]
  rw [cancel]
  noncomm_ring

open scoped ComplexInnerProductSpace

/-- Quadratic-form version for a complex Hilbert-space test fixed by P.
The symmetry premises are sufficient for this identity. -/
theorem twoStepEnergy {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (P T : H → H) (p2 : ∀ x, P (P x) = P x)
    (ps : ∀ x y, ⟪P x,y⟫ = ⟪x,P y⟫) (ts : ∀ x y, ⟪T x,y⟫ = ⟪x,T y⟫)
    (f : H) (fixed : P f = f) :
    (⟪f,P (T (T f))⟫).re - (⟪f,P (T (P (T f)))⟫).re =
      ‖T f-P (T f)‖^2 := by
  have first : ⟪f,P (T (T f))⟫ = ⟪T f,T f⟫ := by
    calc _ = ⟪P f,T (T f)⟫ := (ps _ _).symm
         _ = ⟪f,T (T f)⟫ := by rw [fixed]
         _ = _ := (ts _ _).symm
  have second : ⟪f,P (T (P (T f)))⟫ = ⟪T f,P (T f)⟫ := by
    calc _ = ⟪P f,T (P (T f))⟫ := (ps _ _).symm
         _ = ⟪f,T (P (T f))⟫ := by rw [fixed]
         _ = _ := (ts _ _).symm
  rw [first, second]
  have cross : ⟪T f,P (T f)⟫ = ⟪P (T f),P (T f)⟫ := by rw [ps (T f), p2]
  rw [norm_sub_sq (𝕜 := ℂ), cross]
  change (RCLike.re ⟪T f,T f⟫) - (RCLike.re ⟪P (T f),P (T f)⟫) =
    ‖T f‖^2 - 2*(RCLike.re ⟪P (T f),P (T f)⟫) + ‖P (T f)‖^2
  simp only [inner_self_eq_norm_sq]
  ring

/-- The lists give twice the real parts of the second and third roots of unity. -/
theorem centerSquareSums :
    (([2, -2] : List ℤ).map (fun x => x^2)).sum = 8 := by decide +kernel

theorem cubicCenterSquareSum :
    (([2, -1, -1] : List ℤ).map (fun x => x^2)).sum = 6 := by decide +kernel

/-- Differentiate the weighted Wronskian using the two radial equations. -/
theorem fluxDerivative (u v p : ℝ → ℝ) (r du dv au av w E l κ : ℝ)
    (hu : HasDerivAt u du r) (hv : HasDerivAt v dv r)
    (hpu : HasDerivAt (fun x => p x * deriv u x) au r)
    (hpv : HasDerivAt (fun x => p x * deriv v x) av r)
    (su : κ*au = -(E+l*r)*w*u r) (sv : κ*av = -(E-l*r)*w*v r) :
    HasDerivAt (fun x => κ * (p x * deriv u x * v x - p x * deriv v x * u x))
      (-2*l*r*w*u r*v r) r := by
  have h := ((hpu.mul hv).sub (hpv.mul hu)).const_mul κ
  convert h using 1
  rw [hu.deriv, hv.deriv]
  linear_combination -(v r)*su + (u r)*sv

/-- Fibrewise density reduces to two independent real rows. -/
theorem fibreSeparation {K : Type*} [Field K] (u v a b x y : K)
    (det : u*b-v*a ≠ 0) (h : u*x+v*y = 0) (k : a*x+b*y = 0) : x=0 ∧ y=0 := by
  have hx : (u*b-v*a)*x = 0 := by linear_combination b*h - v*k
  have hy : (u*b-v*a)*y = 0 := by linear_combination u*k - a*h
  exact ⟨(mul_eq_zero.mp hx).resolve_left det, (mul_eq_zero.mp hy).resolve_left det⟩

end YangMills.CentralQuotient.LocalResponse

open YangMills.CentralQuotient.LocalResponse
#print axioms lateralCensus
#print axioms cubeParityAverage
#print axioms conditionalSlope
#print axioms transmissionBound
#print axioms signedChannelExample
#print axioms centerSquareSums
#print axioms cubicCenterSquareSum
#print axioms zeroFieldSharp
#print axioms stripPropagation
#print axioms endpointCovariance
#print axioms twoStepDifference
#print axioms twoStepEnergy
#print axioms fluxDerivative
#print axioms fibreSeparation
