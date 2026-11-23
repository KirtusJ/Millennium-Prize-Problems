import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Analysis.SpecialFunctions.ImproperIntegrals
import Mathlib.Tactic.Linarith

open Real Set MeasureTheory

namespace YangMills.MaxwellEnergy

/-- The electric and magnetic amplitudes exchange the two polarizations. -/
theorem mixing (a b c : ℝ) :
    (a+b*c)^2+(a*c+b)^2 =
    ((a+b)/2)^2*(2*(1+c)^2)+((a-b)/2)^2*(2*(1-c)^2) := by ring

/-- The inverse signs distinguish the total energy and the scalar. -/
theorem angleFactors {r s Q c : ℝ} (hr : 0 < r) (hs : 0 < s)
    (momentum : Q^2=r^2+s^2+2*r*s*c) :
    1+c=(Q^2-(r-s)^2)/(2*r*s) ∧
    1-c=((r+s)^2-Q^2)/(2*r*s) := by
  constructor <;> field_simp <;> nlinarith only [momentum]

theorem flatBandIntegral (q : ℝ) :
    (∫ z in -q..q, (q^2-z^2)^2) = 16*q^5/15 := by
  let G := fun x : ℝ => q^4*x - 2*q^2*x^3/3 + x^5/5
  have hd (x : ℝ) : HasDerivAt G ((q^2-x^2)^2) x := by
    unfold G
    convert (((hasDerivAt_id x).const_mul (q^4)).sub
      (((hasDerivAt_pow 3 x).const_mul (2*q^2)).div_const 3)).add
      ((hasDerivAt_pow 5 x).div_const 5) using 1
    simp
    ring
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => hd x)
    ((by fun_prop : Continuous (fun z : ℝ => (q^2-z^2)^2)).intervalIntegrable _ _)]
  dsimp [G]
  ring

/-- Two-photon spectral densities after the difference of the photon
energies has been integrated out. The same Fourier convention is used in both. -/
theorem totalDensity {q : ℝ} (hq : 0 < q) :
    (∫ z in -q..q, (q^2-z^2)^2)/(128*π^2*q) = q^4/(120*π^2) := by
  rw [flatBandIntegral]
  field_simp
  ring

theorem scalarDensity {q : ℝ} (hq : 0 < q) (E : ℝ) :
    (∫ _z in -q..q, (E^2-q^2)^2)/(128*π^2*q) = (E^2-q^2)^2/(64*π^2) := by
  rw [intervalIntegral.integral_const]
  simp only [smul_eq_mul]
  field_simp
  ring

theorem thresholdLaplace {t : ℝ} (ht : 0 < t) (q : ℝ) :
    (∫ E : ℝ in Ioi q, exp (-t*E)) = exp (-t*q)/t := by
  rw [integral_exp_mul_Ioi (neg_lt_zero.mpr ht)]
  ring

theorem scalarPolynomial (q y : ℝ) :
    ((q+y)^2-q^2)^2=y^4+4*q*y^3+4*q^2*y^2 := by ring

/-- At fixed momentum, the three positive readings retain at least one third. -/
theorem detectorFraction {a : ℝ} (ha : 0 ≤ a) (hb : a ≤ 1) :
    1/3 ≤ 1-a+a^2/3 ∧ 1-a+a^2/3 ≤ 1 := by
  constructor
  · nlinarith [mul_nonneg (sub_nonneg.mpr hb) (show 0 ≤ 2-a by linarith)]
  · nlinarith [mul_nonneg ha (sub_nonneg.mpr hb)]

/-- Two different scalar coefficients at two clocks identify the two squared
mixing amplitudes from the rescaled covariance. -/
theorem twoClocks {T U g h : ℝ} (distinct : g ≠ h) :
    ((T+g*U)-(T+h*U))/(g-h)=U ∧
    (g*(T+h*U)-h*(T+g*U))/(g-h)=T := by
  have hn : g-h ≠ 0 := sub_ne_zero.mpr distinct
  constructor <;> field_simp <;> ring

theorem strictClock {x y q : ℝ} (hy : 0 < y) (hxy : y < x) (hq : 0 ≤ q) :
    3*y^4+3*q*y^3+q^2*y^2 < 3*x^4+3*q*x^3+q^2*x^2 := by
  have h₂ := pow_lt_pow_left₀ hxy hy.le (by decide : (2:ℕ) ≠ 0)
  have h₃ := pow_lt_pow_left₀ hxy hy.le (by decide : (3:ℕ) ≠ 0)
  have h₄ := pow_lt_pow_left₀ hxy hy.le (by decide : (4:ℕ) ≠ 0)
  nlinarith [mul_nonneg hq (sub_nonneg.mpr h₃.le),
    mul_nonneg (sq_nonneg q) (sub_nonneg.mpr h₂.le)]

end YangMills.MaxwellEnergy
#print axioms YangMills.MaxwellEnergy.mixing
#print axioms YangMills.MaxwellEnergy.angleFactors
#print axioms YangMills.MaxwellEnergy.flatBandIntegral
#print axioms YangMills.MaxwellEnergy.totalDensity
#print axioms YangMills.MaxwellEnergy.scalarDensity
#print axioms YangMills.MaxwellEnergy.thresholdLaplace
#print axioms YangMills.MaxwellEnergy.scalarPolynomial
#print axioms YangMills.MaxwellEnergy.detectorFraction
#print axioms YangMills.MaxwellEnergy.twoClocks
#print axioms YangMills.MaxwellEnergy.strictClock
