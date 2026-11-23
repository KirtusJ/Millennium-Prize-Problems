import Mathlib.Analysis.SpecialFunctions.Arsinh
import Mathlib.Topology.ContinuousMap.Weierstrass
import Mathlib.MeasureTheory.Measure.ProbabilityMeasure
import Mathlib.MeasureTheory.Integral.BoundedContinuousFunction
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace Millennium.YangMills.StapleSpectrum
open MeasureTheory Filter Polynomial
open scoped Topology
noncomputable section

abbrev Cut := Set.Icc (0:ℝ) 1

private theorem polyInt (p : ℝ[X]) (μ : ProbabilityMeasure Cut) :
    Integrable (fun x : Cut => p.eval x.val) (μ : Measure Cut) := by
  exact (p.continuous.comp continuous_subtype_val).integrable_of_hasCompactSupport
    (HasCompactSupport.of_compactSpace _)

/-- Moments control all polynomial tests before a uniform approximation is chosen. -/
theorem polynomialReadings (μ : ℕ → ProbabilityMeasure Cut) (ν : ProbabilityMeasure Cut)
    (h : ∀ j : ℕ, Tendsto (fun i => ∫ x : Cut, x.val^j ∂(μ i : Measure Cut)) atTop
      (𝓝 (∫ x : Cut, x.val^j ∂(ν : Measure Cut)))) (p : ℝ[X]) :
    Tendsto (fun i => ∫ x : Cut, p.eval x.val ∂(μ i : Measure Cut)) atTop
      (𝓝 (∫ x : Cut, p.eval x.val ∂(ν : Measure Cut))) := by
  induction p using Polynomial.induction_on' with
  | add p q hp hq =>
    simpa only [eval_add, integral_add (polyInt p _) (polyInt q _)] using hp.add hq
  | monomial n a =>
    simpa only [eval_monomial, integral_const_mul] using (h n).const_mul a

private theorem uniformError (μ : ProbabilityMeasure Cut) (f : BoundedContinuousFunction Cut ℝ) (p : ℝ[X])
    {ε : ℝ} (h : ∀ x : Cut, |p.eval x.val - f x| ≤ ε) :
    |(∫ x : Cut, p.eval x.val ∂(μ : Measure Cut)) - ∫ x, f x ∂(μ : Measure Cut)| ≤ ε := by
  rw [← integral_sub (polyInt p _) (f.integrable _)]
  simpa [Real.norm_eq_abs] using
    (norm_integral_le_of_norm_le_const (μ := (μ : Measure Cut))
      (f := fun x : Cut => p.eval x.val - f x) (C := ε)
      (ae_of_all _ fun x => by simpa [Real.norm_eq_abs] using h x))

/-- All adjacent-and-later normalized readings determine weak convergence, including
possible atoms at either end of the compact transfer interval. -/
theorem reconstruct (μ : ℕ → ProbabilityMeasure Cut) (ν : ProbabilityMeasure Cut)
    (h : ∀ j : ℕ, Tendsto (fun i => ∫ x : Cut, x.val^j ∂(μ i : Measure Cut)) atTop
      (𝓝 (∫ x : Cut, x.val^j ∂(ν : Measure Cut)))) : Tendsto μ atTop (𝓝 ν) := by
  apply ProbabilityMeasure.tendsto_iff_forall_integral_tendsto.mpr
  intro f
  apply Metric.tendsto_nhds.mpr
  intro ε hε
  obtain ⟨p, hp⟩ := exists_polynomial_near_continuousMap 0 1 f.toContinuousMap (ε/4) (by positivity)
  have he : ∀ x : Cut, |p.eval x.val - f x| ≤ ε/4 := by
    intro x
    exact ((ContinuousMap.norm_lt_iff _ (by positivity : 0 < ε/4)).mp hp x).le
  filter_upwards [Metric.tendsto_nhds.mp (polynomialReadings μ ν h p) (ε/4) (by positivity)] with i hi
  rw [Real.dist_eq] at *
  have h₁ := abs_le.mp (uniformError (μ i) f p he)
  have h₂ := abs_le.mp (uniformError ν f p he)
  rcases abs_lt.mp hi with ⟨il, ir⟩
  apply abs_lt.mpr
  constructor <;> linarith

/-- The extra transfer power in the density is already present at adjacent slabs. -/
theorem slabOffset (x : ℝ) (j : ℕ) : x^j*x = x^(j+1) := (pow_succ x j).symm

/-- A scalar contraction at the complete staggering momentum vanishes for arbitrary
complex transverse factors. -/
theorem checkerboard (a b : Fin 3 → ℂ) :
    (∑ j, a j * (1 + (-1:ℂ)) * b j) = 0 := by simp

theorem phaseNorm (s c : ℝ) (h : s^2+c^2=1) :
    (1+c)^2+s^2=2*(1+c) := by nlinarith

theorem endpointAverage (A B m : ℝ) (h : A+B ≤ 2*m) (f : ℝ → ℝ)
    (concave : (f A+f B)/2 ≤ f ((A+B)/2)) (incr : Monotone f) :
    f A+f B ≤ 2*f m := by
  have z := incr (show (A+B)/2 ≤ m by linarith)
  linarith

/-- Hyperbolic midpoint inequality for the sharp upper threshold. -/
theorem upperDispersion (u v w : ℝ) (hw : 0 ≤ w)
    (h : Real.cosh u + Real.cosh v ≤ 2*Real.cosh w) : u+v ≤ 2*w := by
  let m := (u+v)/2
  let d := (u-v)/2
  have hu : m+d=u := by dsimp [m,d]; ring
  have hv : m-d=v := by dsimp [m,d]; ring
  rw [← hu, ← hv, Real.cosh_add, Real.cosh_sub] at h
  have z : Real.cosh m ≤ Real.cosh w := by
    nlinarith [mul_nonneg (Real.cosh_pos m).le (sub_nonneg.mpr (Real.one_le_cosh d))]
  have hmw := Real.cosh_le_cosh.mp z
  rw [abs_of_nonneg hw] at hmw
  have hm := (le_abs_self m).trans hmw
  dsimp [m] at hm
  linarith

theorem transverseCorner (t : ℝ) (h : t^2=3) : t^2+t^2=6 := by linarith

-- PCP begin geometry
/-- Subadditivity of the lattice dispersion once the three-link chord triangle
inequality is supplied. This covers soft endpoints as well. -/
theorem lowerDispersion (x y z : ℝ) (hx : 0 ≤ x) (hy : 0 ≤ y) (hz : z ≤ x+y) :
    2*Real.arsinh (z/2) ≤ 2*Real.arsinh (x/2)+2*Real.arsinh (y/2) := by
  have h : Real.arsinh (z/2) ≤ Real.arsinh (x/2)+Real.arsinh (y/2) := by
    apply Real.sinh_le_sinh.mp
    rw [Real.sinh_add, Real.sinh_arsinh, Real.sinh_arsinh, Real.sinh_arsinh]
    nlinarith [mul_nonneg hx (sub_nonneg.mpr (Real.one_le_cosh (Real.arsinh (y/2)))),
      mul_nonneg hy (sub_nonneg.mpr (Real.one_le_cosh (Real.arsinh (x/2))))]
  linarith
-- PCP end geometry

-- PCP begin certificate
theorem cornerCoefficient (r p : ℝ) (hr : r^2=3) (hp : p ≠ 0) :
    6*(8*r)^3/(1536*128*p^3) = 3*r/(64*p^3) := by
  have h₃ : r^3=3*r := by rw [pow_succ, hr]
  rw [mul_pow, h₃]
  field_simp
  ring
-- PCP end certificate

theorem irCoefficient (p : ℝ) (hp : p ≠ 0) :
    12/(36*p^4*140*1536)=1/(128*p^4*5040) := by field_simp; ring

theorem zeroMomentumWeight (h : ℝ) : h^2*(2^2*2)/1536=h^2/192 := by ring

theorem zeroMomentumIR (p : ℝ) (hp : p ≠ 0) :
    24/(2*p^2*4*192*32)=1/(2048*p^2) := by field_simp; ring

/-- Angular integration of the transverse polarization kernel on a two-particle shell.
The second and fourth centered coordinate moments are q²/3 and q⁴/5. -/
theorem continuumShell (e q : ℝ) :
    (2*e^4-4*e^2*q^2+4*q^4-4*q^2*(q^2/3)+2*(q^4/5))/16 =
      ((e^2-q^2)^2+8*q^4/15)/8 := by ring

theorem shellToPoint : (1:ℝ)/3-2/5+(1+8/15)/7=16/105 := by norm_num

theorem edgeRatio (s : ℝ) (hs : s ≠ 0) : (1-s)/s=1/s-1 := by field_simp

end
end Millennium.YangMills.StapleSpectrum

#print axioms Millennium.YangMills.StapleSpectrum.polynomialReadings
#print axioms Millennium.YangMills.StapleSpectrum.reconstruct
#print axioms Millennium.YangMills.StapleSpectrum.slabOffset
#print axioms Millennium.YangMills.StapleSpectrum.checkerboard
#print axioms Millennium.YangMills.StapleSpectrum.phaseNorm
#print axioms Millennium.YangMills.StapleSpectrum.endpointAverage
#print axioms Millennium.YangMills.StapleSpectrum.transverseCorner
#print axioms Millennium.YangMills.StapleSpectrum.upperDispersion
#print axioms Millennium.YangMills.StapleSpectrum.lowerDispersion
#print axioms Millennium.YangMills.StapleSpectrum.cornerCoefficient
#print axioms Millennium.YangMills.StapleSpectrum.irCoefficient
#print axioms Millennium.YangMills.StapleSpectrum.edgeRatio

#print axioms Millennium.YangMills.StapleSpectrum.zeroMomentumWeight
#print axioms Millennium.YangMills.StapleSpectrum.zeroMomentumIR

#print axioms Millennium.YangMills.StapleSpectrum.continuumShell
#print axioms Millennium.YangMills.StapleSpectrum.shellToPoint
