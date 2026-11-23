/-
Director Z4 | Yang–Mills | the scaling obligation, as pure analysis of two sequences.

Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada.
Formalized with assistance from Claude (Anthropic), acting as Director Z4.

`a n` is the lattice spacing of the n-th regulated theory, `m n` its gap in lattice
units (minus the logarithm of the norm of the one-step transfer operator on the
complement of the vacuum), and `m n / a n` its gap in physical units.
Nothing here constructs a theory; the statements constrain any family of
regulated theories that is offered as a route to a continuum mass gap.
-/
import Mathlib

open Filter Topology

namespace Z4YM

/-- If the spacing tends to zero and the physical gap converges to a real number,
the gap in lattice units tends to zero (the correlation length in lattice units
diverges whenever that gap is positive). -/
theorem lattice_gap_tendsto_zero {a m : ℕ → ℝ} {M : ℝ}
    (ha : Tendsto a atTop (𝓝 0)) (ha0 : ∀ n, a n ≠ 0)
    (hM : Tendsto (fun n => m n / a n) atTop (𝓝 M)) :
    Tendsto m atTop (𝓝 1) := by
  have h := hM.mul ha
  rw [mul_zero] at h
  exact h.congr fun n => div_mul_cancel₀ (m n) (ha0 n)

/-- Adverse form: a gap in lattice units bounded below by a positive constant along
spacings tending to zero from above gives a physical gap that tends to infinity. -/
theorem physical_gap_tendsto_atTop {a m : ℕ → ℝ} {c : ℝ} (hc : 0 < c)
    (ha : Tendsto a atTop (𝓝[>] 0)) (hm : ∀ n, c ≤ m n) :
    Tendsto (fun n => m n / a n) atTop atTop := by
  have hinv : Tendsto (fun n => (a n)⁻¹) atTop atTop := tendsto_inv_nhdsGT_zero.comp ha
  have h2 : Tendsto (fun n => c * (a n)⁻¹) atTop atTop := hinv.const_mul_atTop hc
  have hpos : ∀ᶠ n in atTop, 0 < a n := ha.eventually self_mem_nhdsWithin
  refine tendsto_atTop_mono' _ ?_ h2
  filter_upwards [hpos] with n hn
  rw [div_eq_mul_inv]
  exact mul_le_mul_of_nonneg_right (hm n) (inv_nonneg.mpr hn.le)

/-- Consequently no family with spacings tending to zero from above can have both a
uniform positive lower bound on the lattice-unit gap and a convergent physical gap. -/
theorem not_uniform_lattice_gap_and_finite_physical_gap {a m : ℕ → ℝ} {c M : ℝ}
    (hc : 0 < c) (ha : Tendsto a atTop (𝓝[>] 0)) (hm : ∀ n, c ≤ m n)
    (hM : Tendsto (fun n => m n / a n) atTop (𝓝 M)) : False :=
  not_tendsto_nhds_of_tendsto_atTop (physical_gap_tendsto_atTop hc ha hm) M hM

end Z4YM

#print axioms Z4YM.lattice_gap_tendsto_zero
#print axioms Z4YM.physical_gap_tendsto_atTop
#print axioms Z4YM.not_uniform_lattice_gap_and_finite_physical_gap
