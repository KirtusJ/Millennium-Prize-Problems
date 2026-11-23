/-
Director Z4 | Yang–Mills | adverse control: gauge group Z₂ on the two-dimensional cylinder.

Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada.
Formalized with assistance from Claude (Anthropic), acting as Director Z4.

For Z₂ with plaquette weight exp(β s), s = ±1, the character coefficients are
cosh β and sinh β, so the ratio of the non-trivial to the trivial transfer
eigenvalue for one plaquette is tanh β. With N links, spacing 1/N and β = N²
the gap in physical units is N² · (−log tanh N²). The theorems bound
x · (−log tanh x) for every real x > 0 and take x = N².
The identification of the transfer eigenvalues is not formalized here.
-/
import Mathlib

open Filter Topology

namespace Z4YM

theorem tanh_eq_ratio (x : ℝ) :
    Real.tanh x = (Real.exp (2 * x) - 1) / (Real.exp (2 * x) + 1) := by
  have h : Real.exp (2 * x) = Real.exp x * Real.exp x := by
    rw [← Real.exp_add]; ring_nf
  have hpos := Real.exp_pos x
  rw [Real.tanh_eq_sinh_div_cosh, Real.sinh_eq, Real.cosh_eq, h, Real.exp_neg]
  field_simp

/-- The lattice-unit gap of one plaquette is positive: tanh x < 1 gives −log tanh x > 0. -/
theorem z2_gap_pos (x : ℝ) (hx : 0 < x) : 0 < -Real.log (Real.tanh x) := by
  have hE : 1 < Real.exp (2 * x) := Real.one_lt_exp_iff.mpr (by linarith)
  rw [tanh_eq_ratio]
  have h1 : 0 < (Real.exp (2 * x) - 1) / (Real.exp (2 * x) + 1) := by
    apply div_pos <;> linarith
  have h2 : (Real.exp (2 * x) - 1) / (Real.exp (2 * x) + 1) < 1 := by
    rw [div_lt_one (by linarith)]; linarith
  linarith [Real.log_neg h1 h2]

theorem z2_gap_le (x : ℝ) (hx : 0 < x) :
    -Real.log (Real.tanh x) ≤ 1 / (Real.exp (2 * x) - 1) := by
  have hE : 1 < Real.exp (2 * x) := Real.one_lt_exp_iff.mpr (by linarith)
  rw [tanh_eq_ratio, ← Real.log_inv, inv_div]
  have hpos : 0 < (Real.exp (2 * x) + 1) / (Real.exp (2 * x) - 1) := by
    apply div_pos <;> linarith
  have hne : Real.exp (2 * x) - 1 ≠ 0 := by linarith
  calc Real.log ((Real.exp (2 * x) + 1) / (Real.exp (2 * x) - 1))
      ≤ (Real.exp (2 * x) + 1) / (Real.exp (2 * x) - 1) - 1 := Real.log_le_sub_one_of_pos hpos
    _ = 2 / (Real.exp (2 * x) - 1) := by field_simp; ring

/-- The physical gap along the trajectory, as a function of x = β: at most 1/(1+x). -/
theorem z2_physical_gap_le (x : ℝ) (hx : 0 < x) :
    x * (-Real.log (Real.tanh x)) ≤ 1 / (1 + x) := by
  have hq : 1 + 2 * x + (2 * x) ^ 2 / 2 ≤ Real.exp (2 * x) :=
    Real.quadratic_le_exp_of_nonneg (by linarith)
  have hden : 0 < Real.exp (2 * x) - 1 := by nlinarith
  calc x * (-Real.log (Real.tanh x)) ≤ x * (2 / (Real.exp (2 * x) - 1)) :=
        mul_le_mul_of_nonneg_left (z2_gap_le x hx) hx.le
    _ ≤ 1 / (1 + x) := by
        rw [← mul_div_assoc, div_le_div_iff₀ hden (by linarith)]
        nlinarith

/-- Z₂ on the trajectory β = N²: the physical gap is positive at every N ≥ 1 and tends to zero. -/
theorem z2_physical_gap_tendsto_zero :
    Tendsto (fun N : ℕ => ((N : ℝ) + 1) ^ 2 * (-Real.log (Real.tanh (((N : ℝ) + 1) ^ 2))))
      atTop (𝓝 0) := by
  have hpos : ∀ N : ℕ, 0 < ((N : ℝ) + 1) ^ 2 := fun N => by positivity
  refine squeeze_zero (g := fun N : ℕ => 1 / ((N : ℝ) + 1))
    (fun N => (mul_pos (hpos N) (z2_gap_pos _ (hpos N))).le) (fun N => ?_)
    tendsto_one_div_add_atTop_nhds_zero_nat
  refine (z2_physical_gap_le _ (hpos N)).trans ?_
  have hN : (0 : ℝ) ≤ N := Nat.cast_nonneg N
  apply one_div_le_one_div_of_le (by linarith)
  nlinarith

end Z4YM

#print axioms Z4YM.z2_gap_pos
#print axioms Z4YM.z2_physical_gap_le
#print axioms Z4YM.z2_physical_gap_tendsto_zero
