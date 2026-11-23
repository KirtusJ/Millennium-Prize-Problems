import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.G4.Floor

theorem quaternion_sum (a b c d : ℝ) (h : a^2+b^2+c^2+d^2=1) :
    2 ≤ 3*a^2+2*(b^2+c^2+d^2) := by nlinarith [sq_nonneg a]

theorem density_cost (s h : ℝ) (hs : s*h = 1/4) :
    12*s*h+7*s^2*h^2 < 4 := by
  calc
    12*s*h+7*s^2*h^2 = 12*(s*h)+7*(s*h)^2 := by ring
    _ < 4 := by rw [hs]; norm_num

-- NATIVE CHILD 1
theorem mixed_floor (v w t : ℝ) (h : 16*v ≥ 16/9*t)
    (ht : t ≥ w/4096) : v ≥ w/36864 := by linarith

theorem two_ends (norm lag err left right : ℝ)
    (h : 2*lag ≤ left+right)
    (hl : left ≤ norm-err) (hr : right ≤ norm-err) : err ≤ norm-lag := by linarith

-- NATIVE CHILD 2
theorem colour_average (loss amount : ℝ) (h : amount ≤ 24*loss) :
    amount/24 ≤ loss := by linarith

theorem adjoint_square (v b : ℝ)
    (h : v ≤ (4*b)^2+42*b^2) : v ≤ (8*b)^2 := by
  nlinarith only [sq_nonneg b, h]

theorem score_duality (v c : ℝ) (h : 4*c ≤ 72^2*v) : c/1296 ≤ v := by
  linarith

theorem block_increment (m oldSum newSum : ℝ) (hm : 0 < m)
    (h : 0 ≤ newSum-oldSum) : oldSum/m ≤ newSum/m := by
  exact div_le_div_of_nonneg_right (by linarith) (le_of_lt hm)

noncomputable def longitudinalSum (c : ℕ → ℝ) (sites : ℕ) (length : ℝ) : ℝ :=
  c 0 + 2 * ∑ r ∈ Finset.range sites, max 0 (1-((r:ℝ)+1)/length)*c (r+1)

theorem longitudinal_monotone (c : ℕ → ℝ) (sites : ℕ) (L M : ℝ)
    (hc : ∀ r, 0 ≤ c (r+1)) (hL : 0 < L) (hLM : L ≤ M) :
    longitudinalSum c sites L ≤ longitudinalSum c sites M := by
  unfold longitudinalSum
  apply add_le_add_left
  apply mul_le_mul_of_nonneg_left _ (by norm_num)
  apply Finset.sum_le_sum
  intro r _
  apply mul_le_mul_of_nonneg_right _ (hc r)
  apply max_le_max_left
  apply sub_le_sub_left
  exact div_le_div_of_nonneg_left (by positivity) hL hLM

#print axioms quaternion_sum
#print axioms density_cost
#print axioms mixed_floor
#print axioms two_ends
#print axioms colour_average
#print axioms adjoint_square
#print axioms score_duality
#print axioms block_increment
#print axioms longitudinal_monotone
end Millennium.G4.Floor
