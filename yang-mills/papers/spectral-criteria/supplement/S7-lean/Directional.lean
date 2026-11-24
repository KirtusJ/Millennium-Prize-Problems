/-
Algebraic steps in the proof of the directional sufficient form (the proposition after the remark on
the exact and sufficient forms of the mixing hypothesis). Lean 4.19.0, Mathlib v4.19.0.

Not formalised here: the measure theory (conditional laws, the derivative of the conditional
expectation, the weighted Poincare inequality as a hypothesis on a fibre) and the integration over
coarse fields.
-/
import Mathlib

namespace Directional

open scoped RealInnerProductSpace

/-- The scalar step. `Vf`, `Vh` are the conditional variances of `f(X)` and `h(X)`, `W` the expected
conditional variance of `g(Y)` given `X`, and `z = β² J`. From `Vh ≤ z W` the lower bound
`Vf + Vh + W - 2 √(Vf Vh)` for the conditional mean square of `f(X) - g(Y)` is at least `Vf / (1 + z)`. -/
theorem scalar_step (Vf Vh W z : ℝ) (hf : 0 ≤ Vf) (hh : 0 ≤ Vh) (hz : 0 < z) (hW : Vh ≤ z * W) :
    Vf / (1 + z) ≤ Vf + Vh + W - 2 * Real.sqrt (Vf * Vh) := by
  obtain ⟨s, hs, rfl⟩ : ∃ s, 0 ≤ s ∧ Vf = s ^ 2 :=
    ⟨Real.sqrt Vf, Real.sqrt_nonneg _, (Real.sq_sqrt hf).symm⟩
  obtain ⟨t, ht, rfl⟩ : ∃ t, 0 ≤ t ∧ Vh = t ^ 2 :=
    ⟨Real.sqrt Vh, Real.sqrt_nonneg _, (Real.sq_sqrt hh).symm⟩
  have h1 : Real.sqrt (s ^ 2 * t ^ 2) = s * t := by
    rw [← mul_pow]; exact Real.sqrt_sq (mul_nonneg hs ht)
  have hz1 : (0 : ℝ) < 1 + z := by linarith
  rw [h1, div_le_iff₀ hz1]
  have hW' : t ^ 2 / z ≤ W := by rw [div_le_iff₀ hz]; linarith
  have key : s ^ 2 ≤ (s ^ 2 + t ^ 2 + t ^ 2 / z - 2 * (s * t)) * (1 + z) := by
    have hzne : z ≠ 0 := hz.ne'
    have e : (s ^ 2 + t ^ 2 + t ^ 2 / z - 2 * (s * t)) * (1 + z) - s ^ 2
        = (z * s - (1 + z) * t) ^ 2 / z := by
      field_simp; ring
    have : 0 ≤ (z * s - (1 + z) * t) ^ 2 / z := by positivity
    linarith
  nlinarith [mul_le_mul_of_nonneg_right hW' hz1.le]

/-- The case `z = 0`: then `Vh = 0` and the bound is `Vf` itself. -/
theorem scalar_step_zero (Vf Vh W : ℝ) (hh : 0 ≤ Vh) (hW0 : 0 ≤ W) (hW : Vh ≤ 0 * W) :
    Vf / (1 + 0) ≤ Vf + Vh + W - 2 * Real.sqrt (Vf * Vh) := by
  have : Vh = 0 := le_antisymm (by simpa using hW) hh
  subst this; simp; exact hW0

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- The weight bound, without square roots of matrices. `S` is the conditional covariance of the next
slice, `M` the weight, `b` the covariance vector of the next slice with `g`, `V` the conditional
variance of `g`. The hypothesis `hJ` says `‖S^{1/2} M S^{1/2}‖ ≤ J` in the form
`⟪S u, M (S u)⟫ ≤ J ⟪u, S u⟫`; `hcs` is the Cauchy–Schwarz inequality for covariances. -/
theorem weight_bound (S M : E →ₗ[ℝ] E) (J V : ℝ) (b u₀ : E)
    (hSpos : ∀ x, 0 ≤ ⟪x, S x⟫)
    (hJ : ∀ u, ⟪S u, M (S u)⟫ ≤ J * ⟪u, S u⟫)
    (hJ0 : 0 ≤ J) (hV : 0 ≤ V)
    (hb : b = S u₀)
    (hcs : ∀ w, ⟪w, b⟫ ^ 2 ≤ ⟪w, S w⟫ * V) :
    ⟪b, M b⟫ ≤ J * V := by
  subst hb
  have h1 := hJ u₀
  have h2 := hcs u₀
  have hq0 : 0 ≤ ⟪u₀, S u₀⟫ := hSpos u₀
  have hqV : ⟪u₀, S u₀⟫ ≤ V := by
    rcases eq_or_lt_of_le hq0 with h | h
    · rw [← h]; exact hV
    · nlinarith
  calc ⟪S u₀, M (S u₀)⟫ ≤ J * ⟪u₀, S u₀⟫ := h1
    _ ≤ J * V := mul_le_mul_of_nonneg_left hqV hJ0

/-- In finite dimension the covariance vector lies in the range of a symmetric `S` as soon as the
Cauchy–Schwarz inequality holds. -/
theorem mem_range_of_cs [FiniteDimensional ℝ E] (S : E →ₗ[ℝ] E) (V : ℝ) (b : E)
    (hS : ∀ x y, ⟪S x, y⟫ = ⟪x, S y⟫)
    (hcs : ∀ w, ⟪w, b⟫ ^ 2 ≤ ⟪w, S w⟫ * V) : b ∈ LinearMap.range S := by
  have hK : (LinearMap.range S)ᗮ ≤ LinearMap.ker S := by
    intro x hx
    rw [LinearMap.mem_ker]
    have h : ⟪S (S x), x⟫ = 0 := (Submodule.mem_orthogonal _ _).1 hx _ ⟨S x, rfl⟩
    have h' : ⟪S x, S x⟫ = 0 := by rw [← hS]; exact h
    exact inner_self_eq_zero.1 h'
  have hb : b ∈ (LinearMap.ker S)ᗮ := by
    rw [Submodule.mem_orthogonal]
    intro w hw
    have h := hcs w
    rw [LinearMap.mem_ker.1 hw, inner_zero_right, zero_mul] at h
    exact pow_eq_zero_iff two_ne_zero |>.1 (le_antisymm h (sq_nonneg _))
  have h2 : b ∈ ((LinearMap.range S)ᗮ)ᗮ := Submodule.orthogonal_le hK hb
  rwa [Submodule.orthogonal_orthogonal] at h2

/-- The two together, in finite dimension. -/
theorem weight_bound_fd [FiniteDimensional ℝ E] (S M : E →ₗ[ℝ] E) (J V : ℝ) (b : E)
    (hS : ∀ x y, ⟪S x, y⟫ = ⟪x, S y⟫)
    (hSpos : ∀ x, 0 ≤ ⟪x, S x⟫)
    (hJ : ∀ u, ⟪S u, M (S u)⟫ ≤ J * ⟪u, S u⟫)
    (hJ0 : 0 ≤ J) (hV : 0 ≤ V)
    (hcs : ∀ w, ⟪w, b⟫ ^ 2 ≤ ⟪w, S w⟫ * V) :
    ⟪b, M b⟫ ≤ J * V := by
  obtain ⟨u₀, hu⟩ := mem_range_of_cs S V b hS hcs
  exact weight_bound S M J V b u₀ hSpos hJ hJ0 hV hu.symm hcs

end Directional

#print axioms Directional.scalar_step
#print axioms Directional.scalar_step_zero
#print axioms Directional.weight_bound
#print axioms Directional.mem_range_of_cs
#print axioms Directional.weight_bound_fd
