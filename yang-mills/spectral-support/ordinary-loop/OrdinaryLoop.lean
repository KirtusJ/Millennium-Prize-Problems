import Mathlib.Tactic.NoncommRing
import Mathlib.Algebra.Quaternion
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

open MeasureTheory Real Set
open scoped Quaternion
namespace Millennium.YangMills.D4.OrdinaryLoop

def dots (a b : ℍ[ℝ]) : ℝ := a.imI*b.imI+a.imJ*b.imJ+a.imK*b.imK

def triple (a b c : ℍ[ℝ]) : ℝ :=
  a.imI*(b.imJ*c.imK-b.imK*c.imJ) - a.imJ*(b.imI*c.imK-b.imK*c.imI) +
  a.imK*(b.imI*c.imJ-b.imJ*c.imI)

/-- Signed combinations of ordinary traces give all dot and determinant generators. -/
theorem dotWord (a b : ℍ[ℝ]) : ((a*star b).re-(a*b).re)/2 = dots a b := by
  simp [dots]
  ring

theorem orientedWord (a b c : ℍ[ℝ]) :
    ((a*c*b).re-(a*b*c).re)/2 = triple a b c := by
  simp [triple]
  ring

theorem ordinaryProduct (a b : ℍ[ℝ]) :
    a.re*b.re=((a*b).re+(a*star b).re)/2 := by
  simp

theorem scalarDefect (q : ℍ[ℝ]) (hq : Quaternion.normSq q = 1) :
    (1-q.re)^2 + dots q q = 2*(1-q.re) := by
  rw [Quaternion.normSq_def'] at hq
  change q.re^2+q.imI^2+q.imJ^2+q.imK^2=1 at hq
  unfold dots
  nlinarith

theorem productRemainder {A : Type*} [Ring A] (a b : A) :
    a*b-1-(a-1)-(b-1)=(a-1)*(b-1) := by noncomm_ring

/-- The denominator is measured at a strictly positive time. -/
theorem normalizedReading (v c d f g η : ℝ) (hv : 0 < v) (hd : v ≤ d)
    (hg : v ≤ g) (hc : |c-f| ≤ η) (he : |d-g| ≤ η) :
    |c/d-f/g| ≤ η/v + |f| * η/v^2 := by
  have hd0 : 0 < d := hv.trans_le hd
  have hg0 : 0 < g := hv.trans_le hg
  have decomp : c/d-f/g=(c-f)/d + f*(g-d)/(d*g) := by field_simp; ring
  have first : |(c-f)/d| ≤ η/v := by
    rw [abs_div,abs_of_pos hd0]
    exact div_le_div₀ ((abs_nonneg _).trans hc) hc hv hd
  have last : |f*(g-d)/(d*g)| ≤ |f| * η/v^2 := by
    rw [abs_div,abs_mul,abs_of_pos (mul_pos hd0 hg0),abs_sub_comm g d]
    apply div_le_div₀ (mul_nonneg (abs_nonneg _) ((abs_nonneg _).trans he))
      (mul_le_mul_of_nonneg_left he (abs_nonneg _)) (sq_pos_of_pos hv)
    rw [pow_two]
    exact mul_le_mul hd hg hv.le hd0.le
  rw [decomp]
  exact (abs_add_le _ _).trans (add_le_add first last)

/-- Later readings exist even when the sharp-time spectral mass is infinite. -/
theorem integrableLater (μ : Measure ℝ) (hs : ∀ᵐ E ∂μ, 0 ≤ E) (s t : ℝ)
    (h : s ≤ t) (init : Integrable (fun E : ℝ => exp (-s*E)) μ) :
    Integrable (fun E : ℝ => exp (-t*E)) μ := by
  apply init.mono' (by fun_prop : Continuous fun E : ℝ => exp (-t*E)).aestronglyMeasurable
  filter_upwards [hs] with E he
  rw [Real.norm_eq_abs,abs_of_pos (exp_pos _)]
  apply exp_le_exp.mpr
  nlinarith only [mul_nonneg (sub_nonneg.mpr h) he]

theorem tiltedTail (μ : Measure ℝ) (hs : ∀ᵐ E ∂μ, 0 ≤ E) (s h R : ℝ) (hh : 0 ≤ h)
    (init : Integrable (fun E : ℝ => exp (-s*E)) μ) :
    (∫ E in Ioi R, exp (-(s+h)*E) ∂μ) ≤ exp (-h*R)*(∫ E : ℝ, exp (-s*E) ∂μ) := by
  have later := integrableLater μ hs s (s+h) (by linarith) init
  have upper := init.const_mul (exp (-h*R))
  rw [← integral_const_mul]
  apply le_trans _ (setIntegral_le_integral (s := Ioi R) upper (Filter.Eventually.of_forall
    (fun E => (mul_pos (exp_pos _) (exp_pos _)).le)))
  apply setIntegral_mono_on later.integrableOn upper.integrableOn measurableSet_Ioi
  intro E he
  rw [← exp_add]
  apply exp_le_exp.mpr
  change R < E at he
  nlinarith only [mul_nonneg hh (sub_nonneg.mpr he.le)]

structure Term where
  s : ℤ
  r : ℕ
  g : ℕ
  b : ℕ

def wick (K : ℕ → ℕ → ℝ) (l : List Term) : ℝ :=
  (l.map (fun a => (l.map (fun b => (a.s:ℝ)*(b.s:ℝ)*K a.r b.r*K a.g b.g*K a.b b.b)).sum)).sum

def detCov (K : ℕ → ℕ → ℝ) : ℝ :=
  K 0 0*(K 1 1*K 2 2-K 1 2*K 2 1)-K 0 1*(K 1 0*K 2 2-K 1 2*K 2 0)+
  K 0 2*(K 1 0*K 2 1-K 1 1*K 2 0)

def matchings : ℕ → List ℕ → ℕ
  | 0, l => if l.isEmpty then 1 else 0
  | _+1, [] => 1
  | k+1, a::l => ((l.filter (fun b => a/2 != b/2)).map (fun b => matchings k (l.erase b))).sum


/-- Dimensionless square and oriented trace coefficients at separated times. -/
theorem triangleRatio (a b c : ℝ) :
    3*(3*a*b*c)^2 = 8*((3/2)*a^2)*((3/2)*b^2)*((3/2)*c^2) := by ring

theorem orientedRatio (k : ℝ) :
    3*(6*k^3)^2 = 32*((3/2)*k^2)^3 := by ring

/-- Denominator comparison in the exact square contour integral.
Here l is the square of the dilation of physical time. -/
theorem squareDilation (l x a b : ℝ) (hl : 1 ≤ l) (hx : 0 ≤ x)
    (ha : 0 ≤ a) (hb : 0 ≤ b) :
    (l*x+a)*(l*x+b) ≤ l^2*((x+a)*(x+b)) := by
  have hl0 : 0 ≤ l := zero_le_one.trans hl
  have first : l*x+a ≤ l*(x+a) := by nlinarith only [mul_nonneg (sub_nonneg.mpr hl) ha]
  have last : l*x+b ≤ l*(x+b) := by nlinarith only [mul_nonneg (sub_nonneg.mpr hl) hb]
  calc
    _ ≤ (l*(x+a))*(l*(x+b)) :=
      mul_le_mul first last (add_nonneg (mul_nonneg hl0 hx) hb) (mul_nonneg hl0 (add_nonneg hx ha))
    _ = _ := by ring

/-- Power budget for absolute moments through degree d, for the explicit sharp-loop scale. -/
theorem degreeBudget (r u : ℝ) (d : ℕ)
    (error : ℝ) (he : error ≤ r^(3*d+4)*u)
    (hscale : r^(3*d+6)*u ≤ 1) : error*r^2 ≤ 1 := by
  calc
    error*r^2 ≤ r^(3*d+4)*u*r^2 := mul_le_mul_of_nonneg_right he (sq_nonneg _)
    _ = r^(3*d+6)*u := by rw [show 3*d+6=3*d+4+2 by omega, pow_add]; ring
    _ ≤ 1 := hscale

/-- Double traversal is an ordinary square of the quaternion word. -/
theorem twiceWound (q : ℍ[ℝ]) (hq : Quaternion.normSq q = 1) :
    1-(q*q).re = 4*(1-q.re)-2*(1-q.re)^2 := by
  rw [Quaternion.normSq_def'] at hq
  simp only [Quaternion.mul_re]
  nlinarith only [hq]

/-- The measured two-winding Gram determinant eliminates mixing for any coefficient. -/
theorem windingGram (a b c u : ℝ) :
    a*(u^2*a-4*u*b+4*c)-(u*a-2*b)^2=4*(a*c-b^2) := by ring

theorem windingCalibration (k : ℝ) :
    3*(4*((3/2)*k^2)*((15/2)*k^4))=40*((3/2)*k^2)^3 := by ring

-- BEGIN PCP OS generated trace contractions
def terms : List Term := [⟨1, 0, 1, 2⟩, ⟨-1, 0, 2, 1⟩, ⟨-1, 1, 0, 2⟩, ⟨1, 1, 2, 0⟩, ⟨1, 2, 0, 1⟩, ⟨-1, 2, 1, 0⟩]

theorem determinantWick (K : ℕ → ℕ → ℝ) : wick K terms=6*detCov K := by
  simp [wick,terms,detCov]
  ring

theorem squarePairings : matchings 2 (List.range 4)=2 ∧ matchings 3 (List.range 6)=8 := by decide

theorem colorWeights : 3*(matchings 2 (List.range 4):ℚ)/4=3/2 ∧ 3*(matchings 3 (List.range 6):ℚ)/8=3 := by norm_num [squarePairings.1,squarePairings.2]

theorem radialCounts : Nat.factorial 3=6 ∧ Nat.factorial 5=120 ∧ Nat.factorial 7=5040 := by decide

#print axioms dotWord
#print axioms orientedWord
#print axioms ordinaryProduct
#print axioms scalarDefect
#print axioms productRemainder
#print axioms normalizedReading
#print axioms integrableLater
#print axioms tiltedTail
#print axioms determinantWick
#print axioms radialCounts
#print axioms twiceWound
#print axioms windingGram
#print axioms windingCalibration
#print axioms squareDilation
#print axioms degreeBudget
#print axioms triangleRatio
#print axioms orientedRatio
#print axioms squarePairings
#print axioms colorWeights

end Millennium.YangMills.D4.OrdinaryLoop
