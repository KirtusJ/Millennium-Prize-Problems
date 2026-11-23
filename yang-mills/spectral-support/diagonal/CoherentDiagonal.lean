import Mathlib.MeasureTheory.Measure.Portmanteau
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

open Filter MeasureTheory Set
open scoped ENNReal Topology

namespace Millennium.YangMills.D4

/-- A weak limit of finite measures inherits a null open tail if the cutoff tail
masses tend to zero. The proof uses convergence of total mass and Portmanteau
on the closed complement, so no normalization of the test vector is required. -/
theorem nullTailOfWeakLimit (ν : ℕ → FiniteMeasure ℝ) (μ : FiniteMeasure ℝ)
    (weak : Tendsto ν atTop (𝓝 μ)) (s : ℝ)
    (vanish : Tendsto (fun k => (ν k : Measure ℝ).real (Ioi s)) atTop (𝓝 0)) :
    (μ : Measure ℝ) (Ioi s) = 0 := by
  have total : Tendsto (fun k => (ν k : Measure ℝ).real univ) atTop
      (𝓝 ((μ : Measure ℝ).real univ)) :=
    (NNReal.continuous_coe.tendsto μ.mass).comp ((FiniteMeasure.continuous_mass.tendsto μ).comp weak)
  have closedReal : Tendsto (fun k => (ν k : Measure ℝ).real (Iic s)) atTop
      (𝓝 ((μ : Measure ℝ).real univ)) := by
    simpa only [← measureReal_compl (s := Ioi s) measurableSet_Ioi, compl_Ioi, sub_zero]
      using total.sub vanish
  have closedMass : Tendsto (fun k => (ν k : Measure ℝ) (Iic s)) atTop
      (𝓝 ((μ : Measure ℝ) univ)) := by
    have bridge (ρ : FiniteMeasure ℝ) (S : Set ℝ) :
        ENNReal.ofReal ((ρ : Measure ℝ).real S) = (ρ : Measure ℝ) S :=
      ofReal_measureReal (measure_ne_top _ _)
    simpa only [Function.comp_def, bridge] using ENNReal.tendsto_ofReal closedReal
  have inclusion := FiniteMeasure.limsup_measure_closed_le_of_tendsto weak (isClosed_Iic (a := s))
  rw [closedMass.limsup_eq] at inclusion
  have eq := le_antisymm (measure_mono (subset_univ (Iic s)) : (μ : Measure ℝ) (Iic s) ≤ _) inclusion
  rw [← compl_Iic, measure_compl measurableSet_Iic (measure_ne_top _ _), eq, tsub_self]

/-- One measured time per cutoff suffices when the same positive cutoff measure
generates its moments and these finite measures converge weakly. -/
theorem diagonalSpectralExclusion (ν : ℕ → FiniteMeasure ℝ) (μ : FiniteMeasure ℝ)
    (weak : Tendsto ν atTop (𝓝 μ)) (t : ℕ → ℕ) (late : Tendsto t atTop atTop)
    {r M : ℝ} (hr : 0 ≤ r)
    (positive : ∀ k, ∀ᵐ x ∂(ν k : Measure ℝ), 0 ≤ x)
    (integrable : ∀ k, Integrable (fun x : ℝ => x ^ (t k)) (ν k : Measure ℝ))
    (diagonal : ∀ᶠ k in atTop, (∫ x, x ^ (t k) ∂(ν k : Measure ℝ)) ≤ M * r ^ (t k)) :
    (μ : Measure ℝ) (Ioi r) = 0 := by
  have tail (s : ℝ) (hrs : r < s) : (μ : Measure ℝ) (Ioi s) = 0 := by
    have hs : 0 < s := lt_of_le_of_lt hr hrs
    have bound : ∀ᶠ k in atTop, (ν k : Measure ℝ).real (Ioi s) ≤ M * (r / s) ^ (t k) := by
      filter_upwards [diagonal] with k hk
      have low := setIntegral_ge_of_const_le (μ := (ν k : Measure ℝ)) (c := s ^ (t k))
        measurableSet_Ioi (measure_ne_top _ _)
        (fun x (hx : s < x) => pow_le_pow_left₀ hs.le hx.le (t k)) (integrable k).integrableOn
      have hp : 0 ≤ᵐ[(ν k : Measure ℝ)] (fun x : ℝ => x ^ (t k)) := by
        filter_upwards [positive k] with x hx using pow_nonneg hx _
      have upper := (setIntegral_le_integral (s := Ioi s) (integrable k) hp).trans hk
      rw [div_pow, ← mul_div_assoc, le_div_iff₀ (pow_pos hs _)]
      simpa only [mul_comm ((ν k : Measure ℝ).real (Ioi s))] using low.trans upper
    have lim : Tendsto (fun k => M * (r/s) ^ (t k)) atTop (𝓝 0) := by
      simpa using (tendsto_const_nhds (x := M)).mul
        ((tendsto_pow_atTop_nhds_zero_of_lt_one (div_nonneg hr hs.le) ((div_lt_one hs).2 hrs)).comp late)
    exact nullTailOfWeakLimit ν μ weak s (squeeze_zero' (Eventually.of_forall fun _ => measureReal_nonneg) bound lim)
  let s (n : ℕ) : ℝ := r + 1 / (n + 1 : ℝ)
  have cover : Ioi r ⊆ ⋃ n, Ioi (s n) := by
    intro x hx
    obtain ⟨n, hn⟩ := exists_nat_one_div_lt (sub_pos.mpr (show r < x from hx))
    exact mem_iUnion.mpr ⟨n, show r + 1 / (n + 1 : ℝ) < x by linarith⟩
  exact measure_mono_null cover (measure_iUnion_null fun n => tail (s n) (lt_add_of_pos_right r (by positivity)))

/-- A bounded time window can fit the rate 1/2 at a genuine unit transfer eigenvalue:
a fixed finite prefactor pays for every observation in the window. -/
theorem boundedWindow (L n : ℕ) (hn : n ≤ L) :
    (∫ x : ℝ, x ^ n ∂Measure.dirac 1) ≤ (2 : ℝ)^L * ((1:ℝ)/2)^n ∧
      Measure.dirac (1:ℝ) (Ioi (1/2)) = 1 := by
  constructor
  · rw [integral_dirac, one_pow, div_pow, one_pow, ← div_eq_mul_one_div,
        le_div_iff₀ (pow_pos (by norm_num : 0 < (2:ℝ)) n), one_mul]
    exact pow_le_pow_right₀ (by norm_num : 1 ≤ (2:ℝ)) hn
  · exact Measure.dirac_apply_of_mem (by norm_num [mem_Ioi])

/-- A soft mode of vanishing weight can satisfy the diagonal estimate even
when its own transfer value tends to one. Both weights sum to one. -/
theorem disappearingWeight (k : ℕ) {r x : ℝ} (hr : 0 ≤ r) (hr1 : r ≤ 1)
    (hx : 0 ≤ x) (hx1 : x ≤ 1) :
    0 ≤ 1 - r ^ k ∧
    (1 - r ^ k) * r ^ k + r ^ k * x ^ k ≤ 2 * r ^ k := by
  have hpow : x ^ k ≤ 1 := pow_le_one₀ hx hx1
  constructor
  · exact sub_nonneg.mpr (pow_le_one₀ hr hr1)
  · nlinarith only [mul_nonneg (pow_nonneg hr k) (sub_nonneg.mpr hpow), sq_nonneg (r ^ k)]

-- BEGIN PCP OS generated array control
/-- A diagonal alone does not constrain an array without a common measure in each row. -/
theorem arbitraryArrayControl :
    (∀ n : ℕ, Tendsto (fun k : ℕ => if k = n then (0 : ℝ) else 1) atTop (𝓝 1)) ∧
    (∀ k : ℕ, (if k = k then (0 : ℝ) else 1) = 0) := by
  constructor
  · intro n
    apply Tendsto.congr' _ (tendsto_const_nhds (x := (1 : ℝ)))
    filter_upwards [eventually_gt_atTop n] with k hk
    simp [ne_of_gt hk]
  · intro k
    simp

#print axioms nullTailOfWeakLimit
#print axioms diagonalSpectralExclusion
#print axioms boundedWindow
#print axioms disappearingWeight
#print axioms arbitraryArrayControl

end Millennium.YangMills.D4
