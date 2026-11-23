import Mathlib
open Filter Topology
namespace Edge
/-- eventual version of the lower bound: only eventually c ≤ m n is needed -/
theorem phys_eventually {a m : ℕ → ℝ} {c : ℝ} (hc : 0 < c)
    (ha : Tendsto a atTop (𝓝[>] 0)) (hm : ∀ᶠ n in atTop, c ≤ m n) :
    Tendsto (fun n => m n / a n) atTop atTop := by
  have hinv : Tendsto (fun n => (a n)⁻¹) atTop atTop := tendsto_inv_nhdsGT_zero.comp ha
  have h2 : Tendsto (fun n => c * (a n)⁻¹) atTop atTop := hinv.const_mul_atTop hc
  have hpos : ∀ᶠ n in atTop, 0 < a n := ha.eventually self_mem_nhdsWithin
  refine tendsto_atTop_mono' _ ?_ h2
  filter_upwards [hpos, hm] with n hn hmn
  rw [div_eq_mul_inv]
  exact mul_le_mul_of_nonneg_right hmn (inv_nonneg.mpr hn.le)
/-- negative spacings: a n = -1/(n+1), m n = 1: m/a -> -infinity, NOT +infinity, so "from above" is needed -/
theorem neg_case : Tendsto (fun n : ℕ => (1:ℝ) / (-(1 / ((n:ℝ)+1)))) atTop atBot := by
  have : (fun n : ℕ => (1:ℝ) / (-(1 / ((n:ℝ)+1)))) = fun n : ℕ => -((n:ℝ)+1) := by
    funext n; have : ((n:ℝ)+1) ≠ 0 := by positivity
    field_simp
  rw [this]
  exact tendsto_neg_atTop_atBot.comp (tendsto_atTop_add_const_right _ 1 tendsto_natCast_atTop_atTop)
/-- negative M and negative m allowed in lattice_gap_tendsto_zero: a n = 1/(n+1), m n = -a n, M=-1 -/
theorem neg_ok : Tendsto (fun n : ℕ => -(1 / ((n:ℝ)+1))) atTop (𝓝 0) := by
  simpa using tendsto_one_div_add_atTop_nhds_zero_nat.neg
end Edge
#print axioms Edge.phys_eventually
#print axioms Edge.neg_case
#print axioms Edge.neg_ok
