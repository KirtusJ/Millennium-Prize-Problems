import Mathlib.Analysis.Convex.SpecificFunctions.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.YangMills.BlockedTime

/-- Bernoulli at the scale g/4, followed by twelve powers, bounds the block denominator. -/
theorem blockDenominator {g : ℝ} {m : ℕ} (glo : 4 ≤ g) (blocks : 3*g ≤ m) :
    44 ≤ (1+3/(2*g))^m := by
  have gp : 0 < g := by linarith
  have term : 0 < 3/(2*g) := by positivity
  have base : 1 ≤ 1+3/(2*g) := by linarith
  have h := one_add_mul_self_le_rpow_one_add
    (show -1 ≤ 3/(2*g) by linarith) (show 1 ≤ g/4 by linarith)
  have cancel : 1+g/4*(3/(2*g)) = 11/8 := by field_simp; ring
  rw [cancel] at h
  calc
    (44 : ℝ) ≤ (11/8:ℝ)^12 := by norm_num
    _ ≤ ((1+3/(2*g))^(g/4))^12 := pow_le_pow_left₀ (by norm_num) h 12
    _ = (1+3/(2*g))^(3*g) := by
      rw [← Real.rpow_natCast, ← Real.rpow_mul (by linarith : 0 ≤ 1+3/(2*g))]
      congr 1
      push_cast
      ring
    _ ≤ (1+3/(2*g))^(m:ℝ) := Real.rpow_le_rpow_of_exponent_le base blocks
    _ = _ := Real.rpow_natCast _ _

/-- Normalizing conditional bridge weights and restoring the endpoint weight is exact. -/
theorem weightedBridge {ι : Type*} [Fintype ι] (w v : ι → ℝ)
    (pos : 0 < ∑ i, w i) :
    (∑ i, w i) * ∑ i, (w i / ∑ j, w j)*v i = ∑ i, w i*v i := by
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  field_simp

-- PCP begin geometry
theorem rowAtTilt {δ p : ℝ} (heat : δ ≤ 1/10) (interaction : p ≤ 13/1536) :
    24*p+(δ+16*p)*(3+1/3) ≤ 569/576 := by linarith
theorem groupRowAtTilt {δ p : ℝ} (heat : δ ≤ 1/10) (interaction : p ≤ 1/120) :
    24*p+(δ+16*p)*(3+1/3) ≤ 44/45 := by linarith
-- PCP end geometry

-- PCP begin certificate
theorem rowAtOne {δ p z : ℝ} (heat : δ ≤ 1/10) (interaction : p ≤ 13*z/4)
    (small : z < 2/455) : 2*δ+56*p < 1 := by linarith
-- PCP end certificate

theorem rowMargin {δ p : ℝ} (heat : δ ≤ 1/10) (interaction : p ≤ 13/1536) :
    2*δ+56*p ≤ 647/960 := by linarith

/-- Iterating a nonnegative influence matrix preserves a weighted row bound. -/
theorem iterateInfluence {ι : Type*} [Fintype ι] (C : ι → ι → ℝ) (w : ι → ℝ) (q : ℝ)
    (nonneg : ∀ i j, 0 ≤ C i j) (hq : 0 ≤ q)
    (row : ∀ i, ∑ j, C i j*w j ≤ q*w i) (n : ℕ) (i : ι) :
    ((fun f i => ∑ j, C i j*f j)^[n] w) i ≤ q^n*w i := by
  induction n generalizing i with
  | zero => simp
  | succ n ih =>
    rw [Function.iterate_succ_apply']
    calc
      _ ≤ ∑ j, C i j*(q^n*w j) := Finset.sum_le_sum fun j _ =>
        mul_le_mul_of_nonneg_left (ih j) (nonneg i j)
      _ = q^n*∑ j, C i j*w j := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j _
        ring
      _ ≤ q^n*(q*w i) := mul_le_mul_of_nonneg_left (row i) (pow_nonneg hq _)
      _ = _ := by ring

/-- A boundary discrepancy cannot reach a site in fewer than its graph-distance steps. -/
theorem finitePropagation {ι : Type*} [Fintype ι] (C : ι → ι → ℝ) (dist : ι → ℕ)
    (f : ι → ℝ) (locality : ∀ i j, C i j ≠ 0 → dist i ≤ dist j+1)
    (support : ∀ i, 0 < dist i → f i = 0) (n : ℕ) (i : ι) (outside : n < dist i) :
    ((fun h i => ∑ j, C i j*h j)^[n] f) i = 0 := by
  induction n generalizing i with
  | zero => exact support i outside
  | succ n ih =>
    rw [Function.iterate_succ_apply']
    apply Finset.sum_eq_zero
    intro j _
    by_cases zero : C i j = 0
    · exact mul_eq_zero_of_left zero _
    · have neighbor := locality i j zero
      exact mul_eq_zero_of_right _ (ih j (by omega))

theorem physicalRate {s κ : ℝ} (hs : 0 < s) (hk : 0 < κ) (mesh : s ≤ 13*κ/4) :
    4*Real.log 3/(13*κ) ≤ Real.log 3/s := by
  apply (div_le_div_iff₀ (by positivity) hs).2
  have pos := Real.log_nonneg (by norm_num : (1:ℝ) ≤ 3)
  nlinarith only [mul_le_mul_of_nonneg_left mesh pos]

/-- A small exceptional weight controls the uniform density error of a mixture. -/
theorem mixtureWindow {bad good q δ K : ℝ} (hq : 0 ≤ q) (hp : q ≤ 1)
    (badBound : |bad-1| ≤ K) (goodBound : |good-1| ≤ δ) :
    |(1-q)*good+q*bad-1| ≤ (1-q)*δ+q*K := by
  rw [show (1-q)*good+q*bad-1 = (1-q)*(good-1)+q*(bad-1) by ring]
  apply (abs_add_le _ _).trans
  rw [abs_mul, abs_mul, abs_of_nonneg (sub_nonneg.mpr hp), abs_of_nonneg hq]
  exact add_le_add (mul_le_mul_of_nonneg_left goodBound (sub_nonneg.mpr hp))
                   (mul_le_mul_of_nonneg_left badBound hq)

/-- Comparing the mean and second moment of a normalized real character to Haar. -/
theorem haarVariance {m h second ref d : ℝ}
    (mBound : |m| ≤ 1) (hBound : |h| ≤ 1) (meanErr : |m-h| ≤ 2*d)
    (secondErr : ref-second ≤ 2*d) : ref-h^2-6*d ≤ second-m^2 := by
  have sumBound : |m+h| ≤ 2 := (abs_add_le _ _).trans (by linarith)
  have loss := mul_le_mul meanErr sumBound (abs_nonneg _) (by linarith [abs_nonneg (m-h)])
  have sq : m^2-h^2 ≤ 4*d := by
    calc
      _ = (m-h)*(m+h) := by ring
      _ ≤ |(m-h)*(m+h)| := le_abs_self _
      _ = |m-h| * |m+h| := abs_mul _ _
      _ ≤ 4*d := by linarith
  linarith

/-- The same summable spatial error controls every unit-modulus Fourier phase. -/
theorem fourierBound {ι : Type*} (S : Finset ι) (phase diff : ι → ℂ)
    (unit : ∀ j ∈ S, ‖phase j‖ ≤ 1) :
    ‖∑ j ∈ S, phase j*diff j‖ ≤ ∑ j ∈ S, ‖diff j‖ := by
  apply (norm_sum_le _ _).trans
  apply Finset.sum_le_sum
  intro j hj
  rw [norm_mul]
  simpa using mul_le_mul_of_nonneg_right (unit j hj) (norm_nonneg (diff j))

theorem spatialShell (r : ℝ) : (2*r+1)^3-(2*r-1)^3 = 24*r^2+2 := by ring

/-- In open temporal gauge the split crossing holonomy is conjugate to the Wilson face. -/
theorem crossingFace {G : Type*} [Group G] (u v hx hy left right : G) :
    (left*u*right⁻¹)*((left*hx)*v*(right*hy)⁻¹)⁻¹ =
    left*(u*hy*v⁻¹*hx⁻¹)*left⁻¹ := by
  simp [mul_assoc]

#print axioms crossingFace
#print axioms fourierBound
#print axioms spatialShell
#print axioms groupRowAtTilt
#print axioms mixtureWindow
#print axioms haarVariance
#print axioms blockDenominator
#print axioms weightedBridge
#print axioms rowAtTilt
#print axioms rowAtOne
#print axioms rowMargin
#print axioms iterateInfluence
#print axioms finitePropagation
#print axioms physicalRate

end Millennium.YangMills.BlockedTime
