import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! A two-sector comparison for the defect of a positive transfer operator.
The estimates below concern a regulator; they do not construct a Yang–Mills field. -/
namespace Millennium.YangMills.Transfer

open scoped ComplexInnerProductSpace

def defect (u v c x y : ℝ) : ℝ := u*x^2 - 2*c*x*y + v*y^2

/-- A completed-square identity for the shifted quadratic form. -/
theorem pivot_identity (u v c m x y : ℝ) :
    (u-m) * (defect u v c x y - m*(x^2+y^2)) =
      ((u-m)*x - c*y)^2 + ((u-m)*(v-m)-c^2)*y^2 := by
  unfold defect
  ring

/-- With a strictly positive first pivot the determinant test is exact. -/
theorem comparison_iff {u v c m : ℝ} (hu : m < u) :
    (∀ x y : ℝ, m*(x^2+y^2) ≤ defect u v c x y) ↔
      c^2 ≤ (u-m)*(v-m) := by
  -- PCP begin comparison
  constructor
  · intro h
    have key := sub_nonneg.mpr (h c (u-m))
    have id := pivot_identity u v c m c (u-m)
    rw [mul_comm (u-m) c, sub_self, zero_pow (by decide), zero_add] at id
    have hp : 0 ≤ ((u-m)*(v-m)-c^2)*(u-m)^2 := id ▸ mul_nonneg (sub_nonneg.mpr hu.le) key
    have := nonneg_of_mul_nonneg_left hp (sq_pos_of_pos (sub_pos.mpr hu))
    linarith
  · intro h x y
    have hsum := add_nonneg (sq_nonneg ((u-m)*x - c*y))
      (mul_nonneg (sub_nonneg.mpr h) (sq_nonneg y))
    rw [← pivot_identity] at hsum
    exact sub_nonneg.mp (nonneg_of_mul_nonneg_right hsum (sub_pos.mpr hu))
  -- PCP end comparison

/-- The reassembled complex inner-product estimate. D may be I-T.
The cross term combines both orders, avoiding an implicit symmetry assumption. -/
theorem block_defect {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    (D : H →ₗ[ℂ] H) (p q : H) (u v c m a : ℝ)
    (ha : 0 ≤ a) (hu : m < u) (hdet : c^2 ≤ (u-m)*(v-m))
    (hortho : ⟪p, q⟫ = 0)
    (hpp : a*(u*‖p‖^2) ≤ (⟪p, D p⟫).re)
    (hqq : a*(v*‖q‖^2) ≤ (⟪q, D q⟫).re)
    (hpq : -(a*(2*c*‖p‖*‖q‖)) ≤ (⟪p, D q⟫).re + (⟪q, D p⟫).re) :
    a*m*‖p+q‖^2 ≤ (⟪p+q, D (p+q)⟫).re := by
  have comp := mul_le_mul_of_nonneg_left ((comparison_iff hu).2 hdet ‖p‖ ‖q‖) ha
  have pyth : ‖p+q‖^2 = ‖p‖^2 + ‖q‖^2 := by
    simpa only [hortho, map_zero, mul_zero, add_zero] using (norm_add_sq (𝕜 := ℂ) p q)
  rw [pyth, map_add, inner_add_left, inner_add_right, inner_add_right]
  simp only [Complex.add_re]
  unfold defect at comp
  linarith only [comp, hpp, hqq, hpq]

/-- Physical time per step is a; r is a positive transfer spectral value. -/
theorem energy_floor {a r m : ℝ} (ha : 0 < a) (hr : 0 < r) (h : a*m ≤ 1-r) :
    m ≤ -Real.log r / a := by
  apply (le_div_iff₀ ha).2
  linarith only [h, Real.log_le_sub_one_of_pos hr]

/-- Equal diagonal defects can hide a direction of arbitrarily small cost. -/
theorem equal_sector_witness (e : ℝ) :
    defect 1 1 (1-e) 1 1 = 2*e ∧ defect 1 1 (1-e) 1 (-1) = 2*(2-e) := by
  constructor <;> unfold defect <;> ring

/-- For e=a the slow mode has r=1-a²; its positive physical energy tends to zero. -/
theorem soft_energy (a : ℝ) (ha : 0 < a) (hsmall : a ≤ 1/2) :
    0 < -Real.log (1-a^2)/a ∧ -Real.log (1-a^2)/a ≤ 2*a := by
  have ha2 : a^2 ≤ 1/4 := by nlinarith [mul_nonneg (sub_nonneg.mpr hsmall) (show 0 ≤ 1/2+a by linarith)]
  have hr : 0 < 1-a^2 := by linarith
  constructor
  · exact div_pos (neg_pos.mpr (Real.log_neg hr (by nlinarith [sq_pos_of_pos ha]))) ha
  · have hrec : (1-a^2)⁻¹ ≤ 1+2*a^2 := by
      rw [inv_eq_one_div, div_le_iff₀ hr]
      nlinarith [mul_nonneg (sq_nonneg a) (show 0 ≤ 1-2*a^2 by linarith)]
    apply (div_le_iff₀ ha).2
    linarith only [Real.one_sub_inv_le_log_of_pos hr, hrec]

/-- Each positive step has a positive energy, yet no single positive floor works for all steps. -/
theorem no_uniform_floor :
    ¬ ∃ m : ℝ, 0 < m ∧ ∀ a : ℝ, 0 < a → a ≤ 1/2 → m ≤ -Real.log (1-a^2)/a := by
  -- PCP begin collapse
  rintro ⟨m, hm, hall⟩
  let a := min (m/3) (1/4)
  have ha : 0 < a := lt_min (by linarith) (by norm_num)
  have hfirst : a ≤ m/3 := min_le_left _ _
  have hsecond : a ≤ 1/4 := min_le_right _ _
  have hsmall : a ≤ 1/2 := by linarith
  linarith only [hm, hfirst, hall a ha hsmall, (soft_energy a ha hsmall).2]
  -- PCP end collapse

/-- In the equal-sector control the two transfer eigenvalues are positive and at most one. -/
theorem soft_transfer (a : ℝ) (ha : 0 < a) (hs : a ≤ 1/2) :
    0 < 1-a*(2-a) ∧ 1-a*(2-a) ≤ 1-a^2 ∧ 1-a^2 < 1 := by
  have h : a < 1 := by linarith
  constructor
  · nlinarith only [sq_pos_of_pos (sub_pos.mpr h)]
  constructor
  · nlinarith only [mul_nonneg ha.le (sub_nonneg.mpr h.le)]
  · nlinarith only [sq_pos_of_pos ha]

/-- A moment certificate for the FPHPM one-link SU(2) convolution.
In the application r is the first excited Bessel ratio and s is the second moment.
The integral identity and the model's identification of its spectrum are analytic inputs. -/
theorem one_link_floor (g r s : ℝ) (hg : 0 < g) (hr : 0 < r)
    (hvar : r^2 ≤ s) (hibp : g*(1-s) = 3*r) :
    3*g/(2*g+3) ≤ -g*Real.log r := by
  have hquad : 3*r ≤ g*(1-r^2) := by
    nlinarith only [hibp, mul_nonneg hg.le (sub_nonneg.mpr hvar)]
  have hlinear : 3*r ≤ 2*g*(1-r) := by
    nlinarith only [hquad, mul_nonneg hg.le (sq_nonneg (1-r))]
  have hden : 0 < 2*g+3 := by linarith
  have hratio : 3/(2*g+3) ≤ 1-r := by
    apply (div_le_iff₀ hden).2
    linarith only [hlinear]
  have henergy : 1-r ≤ -Real.log r := by linarith only [Real.log_le_sub_one_of_pos hr]
  calc
    3*g/(2*g+3) = g*(3/(2*g+3)) := by ring
    _ ≤ g*(-Real.log r) := mul_le_mul_of_nonneg_left (hratio.trans henergy) hg.le
    _ = -g*Real.log r := by ring

#print axioms one_link_floor
#print axioms soft_transfer
#print axioms no_uniform_floor
#print axioms pivot_identity
#print axioms comparison_iff
#print axioms block_defect
#print axioms energy_floor
#print axioms equal_sector_witness
#print axioms soft_energy

end Millennium.YangMills.Transfer
