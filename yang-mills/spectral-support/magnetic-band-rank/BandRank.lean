import Mathlib.Data.Fin.VecNotation
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace Millennium.YangMills.MagneticBandRank
open MeasureTheory Finset
noncomputable section

def window (a b x : ℝ) := (x-a)*(b-x)

/-- A nonpositive localizer outside an open transfer interval excludes its endpoints. -/
theorem exteriorSign {x a b : ℝ} (h : a ≤ b) (outside : x ≤ a ∨ b ≤ x) : window a b x ≤ 0 := by
  rcases outside with h₁ | h₂
  · exact mul_nonpos_of_nonpos_of_nonneg (sub_nonpos.mpr h₁) (sub_nonneg.mpr (h₁.trans h))
  · exact mul_nonpos_of_nonneg_of_nonpos (sub_nonneg.mpr (h.trans h₂)) (sub_nonpos.mpr h₂)

/-- A polynomial vanishing on every in-band atom gives a nonpositive form. -/
theorem annihilatedForm {ι : Type*} [MeasurableSpace ι] (μ : Measure ι) (x p : ι → ℝ)
    {a b : ℝ} (hab : a ≤ b)
    (vanish : ∀ i, a < x i → x i < b → p i = 0) :
    (∫ i, window a b (x i)*(p i)^2 ∂μ) ≤ 0 := by
  apply integral_nonpos
  intro i
  change window a b (x i)*(p i)^2 ≤ 0
  by_cases h : x i ≤ a
  · exact mul_nonpos_of_nonpos_of_nonneg (exteriorSign hab (Or.inl h)) (sq_nonneg _)
  by_cases j : b ≤ x i
  · exact mul_nonpos_of_nonpos_of_nonneg (exteriorSign hab (Or.inr j)) (sq_nonneg _)
  simp [vanish i (lt_of_not_ge h) (lt_of_not_ge j)]

/-- The annihilating polynomial for any finite set of distinct observed transfer values. -/
theorem nodeProduct (s : Finset ℝ) (z : ℝ) (hz : z ∈ s) : ∏ j ∈ s, (z-j) = 0 := by
  exact Finset.prod_eq_zero hz (sub_self z)

/-- A positive localized form on every monic quadratic requires a third in-band value. -/
theorem thirdValue {ι : Type*} [MeasurableSpace ι] (μ : Measure ι) (x : ι → ℝ)
    {a b : ℝ} (hab : a ≤ b) (first second : ℝ)
    (positive : ∀ c d : ℝ, 0 < ∫ i, window a b (x i)*(x i^2+c*x i+d)^2 ∂μ) :
    ∃ i, a < x i ∧ x i < b ∧ x i ≠ first ∧ x i ≠ second := by
  by_contra h
  have zero : ∀ i, a < x i → x i < b →
      x i^2+(-(first+second))*x i+first*second=0 := by
    intro i hi hj
    by_cases h₁ : x i = first
    · rw [h₁]; ring
    by_cases h₂ : x i = second
    · rw [h₂]; ring
    exact (h ⟨i,hi,hj,h₁,h₂⟩).elim
  exact (not_lt_of_ge (annihilatedForm μ x _ hab zero)) (positive (-(first+second)) (first*second))

/-- The third visible value still carries positive mass after any two levels are removed. -/
theorem thirdMass {ι : Type*} [MeasurableSpace ι] (μ : Measure ι) (x : ι → ℝ)
    {a b : ℝ} (hab : a ≤ b) (first second : ℝ)
    (positive : ∀ c d : ℝ, 0 < ∫ i, window a b (x i)*(x i^2+c*x i+d)^2 ∂μ) :
    0 < μ {i | a < x i ∧ x i < b ∧ x i ≠ first ∧ x i ≠ second} := by
  by_contra bad
  have null := nonpos_iff_eq_zero.mp (le_of_not_gt bad)
  have outside : ∀ᵐ i ∂μ, ¬(a < x i ∧ x i < b ∧ x i ≠ first ∧ x i ≠ second) := by
    apply ae_iff.mpr
    simpa using null
  apply (not_lt_of_ge ?_) (positive (-(first+second)) (first*second))
  apply integral_nonpos_of_ae
  filter_upwards [outside] with i hi
  change window a b (x i)*(x i^2+(-(first+second))*x i+first*second)^2 ≤ 0
  by_cases h : x i ≤ a
  · exact mul_nonpos_of_nonpos_of_nonneg (exteriorSign hab (Or.inl h)) (sq_nonneg _)
  by_cases j : b ≤ x i
  · exact mul_nonpos_of_nonpos_of_nonneg (exteriorSign hab (Or.inr j)) (sq_nonneg _)
  have zero : x i^2+(-(first+second))*x i+first*second=0 := by
    by_cases hf : x i = first
    · rw [hf]; ring
    by_cases hs : x i = second
    · rw [hs]; ring
    exact (hi ⟨lt_of_not_ge h,lt_of_not_ge j,hf,hs⟩).elim
  rw [zero]
  norm_num

/-- The three lagged moments entering one localizing matrix entry. -/
theorem readingIdentity (x a b : ℝ) (n : ℕ) :
    x^n*window a b x = -x^(n+2)+(a+b)*x^(n+1)-(a*b)*x^n := by
  simp only [window, pow_succ]
  ring

/-- Finite error on each matrix entry controls the error on every quadratic form. -/
theorem entryError (x y z : ℝ) :
    (|x|+|y|+|z|)^2 ≤ 3*(x^2+y^2+z^2) := by
  have h : (|x|+|y|+|z|)^2 ≤ 3*(|x|^2+|y|^2+|z|^2) := by
    nlinarith only [sq_nonneg (|x|-|y|),sq_nonneg (|y|-|z|),sq_nonneg (|x|-|z|)]
  simpa only [sq_abs] using h

def minorTwo (a b d : ℝ) := a*d-b^2
def minorThree (a b c d e f : ℝ) := a*d*f+2*b*c*e-a*e^2-d*c^2-f*b^2

/-- A fraction-free sum of squares converting three positive minors to a form bound. -/
theorem sylvesterFloor {a b c d e f : ℝ} (ha : 0 < a)
    (hd : 0 < minorTwo a b d) (hk : 0 ≤ minorThree a b c d e f) (x y z : ℝ) :
    0 ≤ a*x^2+2*b*x*y+2*c*x*z+d*y^2+2*e*y*z+f*z^2 := by
  have identity : (a*minorTwo a b d)*(a*x^2+2*b*x*y+2*c*x*z+d*y^2+2*e*y*z+f*z^2) =
      minorTwo a b d*(a*x+b*y+c*z)^2+(minorTwo a b d*y+(a*e-b*c)*z)^2+
      (a*minorThree a b c d e f)*z^2 := by unfold minorTwo minorThree; ring
  have h := add_nonneg (add_nonneg (mul_nonneg hd.le (sq_nonneg (a*x+b*y+c*z)))
    (sq_nonneg (minorTwo a b d*y+(a*e-b*c)*z))) (mul_nonneg (mul_nonneg ha.le hk) (sq_nonneg z))
  rw [← identity] at h
  exact nonneg_of_mul_nonneg_right h (mul_pos ha hd)

def moment (j : ℕ) : ℝ := 1 / ((j:ℝ)+1)^8

-- PCP begin certificate
def gammaEntry (n : ℕ) : ℝ :=
  -moment (n+2) + (513/1024)*moment (n+1) - (1/2048)*moment n
-- PCP end certificate

def margin : ℝ := 1/70000000

theorem exactMinors : 0 < gammaEntry 0 - margin ∧
    0 < minorTwo (gammaEntry 0-margin) (gammaEntry 1) (gammaEntry 2-margin) ∧
    0 < minorThree (gammaEntry 0-margin) (gammaEntry 1) (gammaEntry 2)
      (gammaEntry 2-margin) (gammaEntry 3) (gammaEntry 4-margin) := by
  norm_num [gammaEntry, moment, margin, minorTwo, minorThree]

/-- Exact lower bound for the unperturbed three-reading-direction quadratic form. -/
theorem momentFloor (x y z : ℝ) :
    margin*(x^2+y^2+z^2) ≤ gammaEntry 0*x^2+2*gammaEntry 1*x*y+
      2*gammaEntry 2*x*z+gammaEntry 2*y^2+2*gammaEntry 3*y*z+gammaEntry 4*z^2 := by
  have h := sylvesterFloor exactMinors.1 exactMinors.2.1 exactMinors.2.2.le x y z
  linarith only [h]

theorem profileRadius : (((1-(1/12800000:ℝ))^2)⁻¹-1)/256 < 1/1000000000 := by norm_num

-- PCP begin geometry
theorem sevenReadings : (3:ℝ)*(3075/2048)*(1/400000000) < margin := by norm_num [margin]
-- PCP end geometry

/-- Localized entries inherit the seven measured moment tolerances. -/
theorem lagError (m : ℕ → ℝ) (n : ℕ) (hn : n ≤ 4)
    (data : ∀ j ≤ 6, |m j - moment j| ≤ 1/400000000) :
    |(-m (n+2)+(513/1024)*m (n+1)-(1/2048)*m n)-gammaEntry n| ≤
      (3075/2048)*(1/400000000) := by
  have h₀ := abs_le.mp (data n (by omega))
  have h₁ := abs_le.mp (data (n+1) (by omega))
  have h₂ := abs_le.mp (data (n+2) (by omega))
  unfold gammaEntry
  rw [abs_le]
  constructor <;> linarith

/-- Every measured localizer is positive on a monic quadratic at the stated tolerance. -/
theorem measuredMonic (L : ℕ → ℝ)
    (error : ∀ j ≤ 4, |L j-gammaEntry j| ≤ (3075/2048)*(1/400000000)) (u v : ℝ) :
    0 < u^2*L 0+2*u*v*L 1+(2*u+v^2)*L 2+2*v*L 3+L 4 := by
  let h : ℝ := (3075/2048)*(1/400000000)
  have one (j : ℕ) (hj : j ≤ 4) (t : ℝ) : -(h*|t|) ≤ t*(L j-gammaEntry j) := by
    apply (neg_le_neg (mul_le_mul_of_nonneg_right (error j hj) (abs_nonneg t))).trans
    rw [mul_comm |L j-gammaEntry j|, ← abs_mul]
    exact neg_abs_le _
  have A := one 0 (by decide) (u^2)
  have B := one 1 (by decide) (u*v)
  have C := one 2 (by decide) u
  have D := one 2 (by decide) (v^2)
  have E := one 3 (by decide) v
  have F := one 4 (by decide) 1
  simp only [abs_sq, abs_mul, abs_one, mul_one, one_mul] at A B D F
  have control := mul_le_mul_of_nonneg_left (entryError u v 1) (show 0 ≤ h by norm_num [h])
  simp only [abs_one, one_pow] at control
  have expand : (|u|+|v|+1)^2 = u^2+v^2+1+2 * |u| * |v| + 2 * |u| + 2 * |v| := by
    calc
      _ = |u|^2+|v|^2+1+2 * |u| * |v| + 2 * |u| + 2 * |v| := by ring
      _ = _ := by rw [sq_abs,sq_abs]
  rw [expand] at control
  have positive := mul_lt_mul_of_pos_right sevenReadings (show 0 < u^2+v^2+1 by positivity)
  have floor := momentFloor u v 1
  rw [mul_assoc (3:ℝ) (3075/2048) (1/400000000)] at positive
  change 3*h*(u^2+v^2+1) < margin*(u^2+v^2+1) at positive
  linarith only [A,B,C,D,E,F,control,positive,floor]

/-- The seven-reading support certificate for an actual positive measure. -/
theorem certifiedBand {ι : Type*} [MeasurableSpace ι] (μ : Measure ι) (x : ι → ℝ)
    (ints : ∀ j : ℕ, Integrable (fun i => x i ^ j) μ)
    (data : ∀ j ≤ 6, |(∫ i, x i ^ j ∂μ) - moment j| ≤ 1/400000000) (first second : ℝ) :
    0 < μ {i | (1/1024:ℝ) < x i ∧ x i < 1/2 ∧ x i ≠ first ∧ x i ≠ second} := by
  let W (i : ι) := window (1/1024) (1/2) (x i)
  let m (n : ℕ) := ∫ i, x i^n ∂μ
  let L (n : ℕ) := ∫ i, x i^n * W i ∂μ
  have ident (n : ℕ) (i : ι) : x i^n*W i =
      -(x i^(n+2)) + (513/1024)*x i^(n+1) - (1/2048)*x i^n := by
    dsimp [W]; rw [readingIdentity]; ring
  have firstTwo (n : ℕ) : Integrable
      (fun i => -(x i^(n+2)) + (513/1024)*x i^(n+1)) μ :=
    (ints (n+2)).neg.add ((ints (n+1)).const_mul _)
  have intW (n : ℕ) : Integrable (fun i => x i^n*W i) μ := by
    simp_rw [ident]
    exact (firstTwo n).sub ((ints n).const_mul _)
  have lag (n : ℕ) : L n = -m (n+2)+(513/1024)*m (n+1)-(1/2048)*m n := by
    dsimp [L,m]; simp_rw [ident]
    rw [integral_sub (firstTwo n) ((ints n).const_mul _),
      integral_add (f := fun i => -(x i^(n+2))) (g := fun i => (513/1024)*x i^(n+1)) (ints (n+2)).neg ((ints (n+1)).const_mul _),
      integral_neg, integral_const_mul, integral_const_mul]
  apply thirdMass μ x (by norm_num) first second
  intro v u
  let cf : Fin 5 → ℝ := ![u^2,2*u*v,2*u+v^2,2*v,1]
  have decomp (i : ι) : W i*(x i^2+v*x i+u)^2 =
      ∑ n : Fin 5, cf n*(x i^n.val*W i) := by
    simp [Fin.sum_univ_succ,cf]
    ring
  change 0 < ∫ i, W i*(x i^2+v*x i+u)^2 ∂μ
  simp_rw [decomp]
  rw [integral_finset_sum _ (fun n _ => (intW n.val).const_mul (cf n))]
  simp_rw [integral_const_mul]
  change 0 < ∑ n : Fin 5, cf n*L n.val
  have good := measuredMonic L (fun n hn => by rw [lag]; exact lagError m n hn data) u v
  simpa [Fin.sum_univ_succ,cf,add_assoc] using good

/-- A finite energy-window projection controls the largest individual atom it contains. -/
theorem effectiveCount {ι : Type*} (s : Finset ι) (w : ι → ℝ) (cap : ℝ)
    (hn : ∀ i ∈ s, 0 ≤ w i) (hc : ∀ i ∈ s, w i ≤ cap) :
    ∑ i ∈ s, (w i)^2 ≤ cap*∑ i ∈ s, w i := by
  rw [Finset.mul_sum]
  exact Finset.sum_le_sum fun i hi => by
    simpa [pow_two] using mul_le_mul_of_nonneg_right (hc i hi) (hn i hi)

#print axioms lagError
#print axioms measuredMonic
#print axioms certifiedBand
#print axioms momentFloor
#print axioms profileRadius
#print axioms thirdMass
#print axioms thirdValue
#print axioms exteriorSign
#print axioms annihilatedForm
#print axioms nodeProduct
#print axioms readingIdentity
#print axioms entryError
#print axioms sylvesterFloor
#print axioms exactMinors
#print axioms sevenReadings
#print axioms effectiveCount

end
end Millennium.YangMills.MagneticBandRank
