import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

open scoped BigOperators
namespace Millennium.G4.Covariance

theorem schur_row {ι : Type*} [Fintype ι] (w : ι → ι → ℝ) (x : ι → ℝ) (b : ℝ)
    (hn : ∀ i j, 0 ≤ w i j) (hs : ∀ i j, w i j = w j i)
    (hb : ∀ i, ∑ j, w i j ≤ b) :
    ∑ i, ∑ j, 2 * (w i j * x i * x j) ≤ 2 * (b * ∑ i, x i ^ 2) := by
  have hswap : (∑ i, ∑ j, w i j * x j ^ 2) = ∑ i, ∑ j, w i j * x i ^ 2 := by
    rw [Finset.sum_comm]
    exact Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => by rw [hs j i]))
  have hrows : (∑ i, ∑ j, w i j * x i ^ 2) ≤ b * ∑ i, x i ^ 2 := by
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro i _
    rw [← Finset.sum_mul]
    exact mul_le_mul_of_nonneg_right (hb i) (sq_nonneg _)
  calc
    _ ≤ ∑ i, ∑ j, (w i j * x i ^ 2 + w i j * x j ^ 2) := by
      apply Finset.sum_le_sum
      intro i _
      apply Finset.sum_le_sum
      intro j _
      nlinarith only [mul_nonneg (hn i j) (sq_nonneg (x i - x j))]
    _ = _ + ∑ i, ∑ j, w i j * x i ^ 2 := by simp_rw [Finset.sum_add_distrib]; rw [hswap]
    _ ≤ _ := by linarith only [hrows]

-- NATIVE CHILD 1
-- Coordinates (i,j) are distinct fine plaquettes, with j indexing the eight corners.
theorem eight_corner_isometry {ι : Type*} [Fintype ι] (c : ι → ℂ)
    (w : ι → Fin 8 → ℂ) (hw : ∀ i j, ‖w i j‖^2 = 1/8) :
    ∑ i, ∑ j, ‖w i j * c i‖^2 = ∑ i, ‖c i‖^2 := by
  have h8 (t : ℝ) : (∑ _j : Fin 8, (1/8 : ℝ)*t) = t := by simp
  simp_rw [norm_mul, mul_pow, hw, h8]

theorem variance_defect (r j g : ℝ) (hj : g*r ≤ j) (t : ℝ)
    (ht : t ≤ r-j) : t ≤ (1-g)*r := by
  linarith

theorem mixed_contraction (a g t c : ℝ) (hg : 0 ≤ g) (hg1 : g ≤ 1)
    (hc : c ≤ a) (ht : t ≤ 1) :
    (1-g)*t + g*c ≤ 1-g*(1-a) := by
  nlinarith only [mul_nonneg (sub_nonneg.mpr hg1) (sub_nonneg.mpr ht),
    mul_nonneg hg (sub_nonneg.mpr hc)]

-- NATIVE CHILD 2
theorem same_packet_metric (g h s δ B : ℝ) (hB : 0 < B) (hd : 0 ≤ δ)
    (upper : g ≤ B*s) (innovation : δ*s ≤ g-h) : (δ/B)*g ≤ g-h := by
  calc
    (δ/B)*g ≤ (δ/B)*(B*s) := mul_le_mul_of_nonneg_left upper (div_nonneg hd hB.le)
    _ = δ*s := by rw [← mul_assoc, div_mul_cancel₀ _ (ne_of_gt hB)]
    _ ≤ g-h := innovation

theorem sliding_filter_ratio (w h g : ℝ) (hw : w ≠ 0) :
    (w*h)/(w*g) = h/g := mul_div_mul_left h g hw

theorem half_ceiling (r z : ℝ) (hz : z ≤ r*(1-r)) : 4*z ≤ 1 := by
  nlinarith only [sq_nonneg (2*r-1), hz]

#print axioms schur_row
#print axioms eight_corner_isometry
#print axioms variance_defect
#print axioms mixed_contraction
#print axioms same_packet_metric
#print axioms sliding_filter_ratio
#print axioms half_ceiling

end Millennium.G4.Covariance
