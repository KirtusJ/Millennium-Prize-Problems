import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.NormNum

open MeasureTheory Set

namespace Millennium.G4.MagneticVariance

/-- The cap and the comparison-series tail each contribute at most 1/16 per link. -/
theorem plaquette_error (localTerm tail link face : ℝ)
    (hlocal : localTerm ≤ 1/16) (htail : tail ≤ 1/32)
    (hlink : link ≤ localTerm + 2 * tail) (hface : face ≤ 4 * link) :
    face ≤ 1/2 := by linarith

/-- Two separated tails, each charged with probability p, give a lower bound
on prediction error for every constant prediction, including the conditional mean
when the measure is a conditional law. -/
theorem two_tail_variance {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (F : X → ℝ) (low high : Set X) (hl : MeasurableSet low) (hh : MeasurableSet high)
    (hd : Disjoint low high) (p z l r : ℝ) (hp : 0 ≤ p) (hlr : l ≤ r)
    (pl : p ≤ μ.real low) (ph : p ≤ μ.real high)
    (fl : ∀ x ∈ low, F x ≤ l) (fh : ∀ x ∈ high, r ≤ F x)
    (hi : Integrable (fun x => (F x - z)^2) μ) :
    p*(r-l)^2/2 ≤ ∫ x, (F x - z)^2 ∂μ := by
  let a := max (z - l) 0
  let b := max (r - z) 0
  have ha : 0 ≤ a := le_max_right _ _
  have hb : 0 ≤ b := le_max_right _ _
  have hab : r-l ≤ a + b := by
    dsimp [a,b]
    linarith [le_max_left (z-l) 0, le_max_left (r-z) 0]
  have geom : (r-l)^2/2 ≤ a^2 + b^2 := by
    nlinarith [sq_nonneg (a-b), pow_le_pow_left₀ (sub_nonneg.mpr hlr) hab 2]
  have left (x) (hx : x ∈ low) : a^2 ≤ (F x - z)^2 := by
    have h : a ≤ |F x - z| := max_le (by linarith [fl x hx, neg_le_abs (F x-z)]) (abs_nonneg _)
    simpa using pow_le_pow_left₀ ha h 2
  have right (x) (hx : x ∈ high) : b^2 ≤ (F x - z)^2 := by
    have h : b ≤ |F x - z| := max_le (by linarith [fh x hx, le_abs_self (F x-z)]) (abs_nonneg _)
    simpa using pow_le_pow_left₀ hb h 2
  have il := setIntegral_ge_of_const_le hl (measure_ne_top μ low) left hi.integrableOn
  have ir := setIntegral_ge_of_const_le hh (measure_ne_top μ high) right hi.integrableOn
  have whole := setIntegral_le_integral (s := low ∪ high) hi
    (Filter.Eventually.of_forall fun x => sq_nonneg (F x-z))
  rw [setIntegral_union hd hh hi.integrableOn hi.integrableOn] at whole
  nlinarith [mul_le_mul_of_nonneg_right geom hp,
    mul_le_mul_of_nonneg_left pl (sq_nonneg a), mul_le_mul_of_nonneg_left ph (sq_nonneg b)]

-- NATIVE CHILD 1
/-- Recording the Markov prediction error as a two-step covariance loss. -/
theorem prediction_loss (mass covariance err ρ : ℝ) (projection : mass = covariance + err)
    (floor : ρ ≤ err) : covariance ≤ mass - ρ := by linarith

/-- A low/high spectral split converts the one-step prediction loss into mass
above the energy threshold. The spectral measure has total mass at most one. -/
theorem high_energy_mass (ρ mass high loss : ℝ) (hρ : 0 ≤ ρ) (hmax : ρ ≤ 1)
    (hm : mass ≤ 1) (floor : ρ ≤ loss)
    (split : loss ≤ ρ/2 * (mass-high) + high) :
    ρ/(2-ρ) ≤ high := by
  apply (div_le_iff₀ (by linarith : 0 < 2-ρ)).mpr
  nlinarith [mul_le_mul_of_nonneg_left hm hρ]

-- NATIVE CHILD 2
/-- A transfer measure with small scaled second moment cannot carry much weight
outside the relative band. The measure and observable may vary with the cutoff. -/
theorem scaled_band_tail {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (x : X → ℝ) (outside : Set X) (ho : MeasurableSet outside)
    (η : ℝ) (hη : 0 < η) (hout : ∀ y ∈ outside, η ≤ |x y - 1|)
    (hi : Integrable (fun y => (x y - 1)^2) μ) :
    μ.real outside ≤ (∫ y, (x y - 1)^2 ∂μ)/η^2 := by
  have h (y) (hy : y ∈ outside) : η^2 ≤ (x y - 1)^2 := by
    simpa using pow_le_pow_left₀ hη.le (hout y hy) 2
  have localBound := setIntegral_ge_of_const_le ho (measure_ne_top μ outside) h hi.integrableOn
  have fullBound := setIntegral_le_integral (s := outside) hi
    (Filter.Eventually.of_forall fun y => sq_nonneg (x y - 1))
  exact (le_div_iff₀ (sq_pos_of_pos hη)).mpr (by linarith)

/-- A perturbation of at most one eighth preserves positive projected weight. -/
theorem projected_mass (bare flowed distance : ℝ) (hb : 3/8 ≤ bare)
    (hd : distance ≤ 1/8) (triangle : bare ≤ flowed + distance) : 1/16 ≤ flowed^2 := by
  have positiveNorm : 1/4 ≤ flowed := by linarith
  nlinarith [pow_le_pow_left₀ (by norm_num : (0 : ℝ) ≤ 1/4) positiveNorm 2]

/-- The error is measured on the centered subspace, with its full transfer norm B. -/
theorem stable_overlap (bare flowed error c B : ℝ) (hB : 0 ≤ B)
    (signal : 2*c*B ≤ bare) (budget : 2*error ≤ c)
    (loss : bare-flowed ≤ 2*error*B) : c*B ≤ flowed := by
  linarith [mul_le_mul_of_nonneg_right budget hB]

/-- A normalized positive measure supported below B and with first moment at
least cB has definite mass above cB/2. Sharp for the corresponding scalar split. -/
theorem transfer_band (c B mass weight first : ℝ)
    (hc : 0 ≤ c) (hc' : c ≤ 1) (hB : 0 < B) (hm : mass ≤ 1)
    (signal : c*B ≤ first) (split : first ≤ (c*B/2)*(mass-weight) + B*weight) :
    c/(2-c) ≤ weight := by
  apply (div_le_iff₀ (by linarith : 0 < 2-c)).mpr
  apply le_of_mul_le_mul_right (a := B) _ hB
  nlinarith [mul_le_mul_of_nonneg_right hm (mul_nonneg hc hB.le)]

-- The exact alternating solution has tangent coordinate z at the observed time.
theorem checkerboard_attenuation (z : ℝ) (hz : 0 ≤ z) :
    2 * z^2 / (1 + z^2) ≤ 2 * z^2 := by
  have hs : 0 ≤ z^2 := sq_nonneg z
  have hd : 0 < 1 + z^2 := by linarith
  apply (div_le_iff₀ hd).2
  calc
    2 * z^2 = (2 * z^2) * 1 := by ring
    _ ≤ (2 * z^2) * (1 + z^2) :=
      mul_le_mul_of_nonneg_left (by linarith) (mul_nonneg (by norm_num) hs)

#print axioms plaquette_error
#print axioms two_tail_variance
#print axioms prediction_loss
#print axioms high_energy_mass
#print axioms scaled_band_tail
#print axioms projected_mass
#print axioms stable_overlap
#print axioms transfer_band
#print axioms checkerboard_attenuation

end Millennium.G4.MagneticVariance
