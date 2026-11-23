import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.Linarith
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.Tactic.SplitIfs

noncomputable section
open MeasureTheory Filter
open scoped Topology

namespace Millennium.G4.ReflectedTails

/-- The signed strict exceedance test at the two symmetric thresholds. -/
def signedCut (c a : ℝ) : ℝ := if c < a then 1 else if a < -c then -1 else 0

theorem signedCut_odd {c : ℝ} (hc : 0 ≤ c) (a : ℝ) :
    signedCut c (-a) = -signedCut c a := by
  unfold signedCut
  split_ifs <;> linarith

theorem abs_signedCut_le_one (c a : ℝ) : |signedCut c a| ≤ 1 := by
  unfold signedCut
  split_ifs <;> norm_num

theorem measurable_signedCut (c : ℝ) : Measurable (signedCut c) := by
  exact Measurable.ite (measurableSet_lt measurable_const measurable_id) measurable_const
    (Measurable.ite (measurableSet_lt measurable_id measurable_const) measurable_const measurable_const)

-- NATIVE CHILD 1

/-- Deterministic inequality, including equality at the strict thresholds. -/
theorem tail_pointwise (a z u : ℝ) (hu : 0 ≤ u) :
    (if 3*u/2 < |a| then (1 : ℝ) else 0) ≤
      2*(if u < |a-z| then (1 : ℝ) else 0) + signedCut (u/2) a * signedCut (u/2) z := by
  by_cases hd : u < |a-z|
  · rw [if_pos hd]
    have hbound : |signedCut (u/2) a * signedCut (u/2) z| ≤ 1 := by
      rw [abs_mul]
      simpa using mul_le_mul (abs_signedCut_le_one (u/2) a) (abs_signedCut_le_one (u/2) z)
        (abs_nonneg _) (by norm_num : (0 : ℝ) ≤ 1)
    have hmin := (abs_le.mp hbound).1
    split_ifs <;> linarith
  · rw [if_neg hd]
    obtain ⟨hl,hr⟩ := abs_le.mp (le_of_not_gt hd)
    by_cases ha : 3*u/2 < |a|
    · rw [if_pos ha]
      by_cases hpos : 0 ≤ a
      · rw [abs_of_nonneg hpos] at ha
        have h₁ : u/2 < a := by linarith
        have h₂ : u/2 < z := by linarith
        norm_num [signedCut, h₁, h₂]
      · rw [abs_of_neg (lt_of_not_ge hpos)] at ha
        have h₁ : ¬u/2 < a := by linarith
        have h₂ : ¬u/2 < z := by linarith
        have h₃ : a < -(u/2) := by linarith
        have h₄ : z < -(u/2) := by linarith
        norm_num [signedCut, h₁, h₂, h₃, h₄]
    · rw [if_neg ha]
      unfold signedCut
      split_ifs <;> norm_num at * <;> linarith

variable {Ω : Type*} [MeasurableSpace Ω]

theorem cutProduct_integrable (μ : Measure Ω) [IsFiniteMeasure μ]
    {X Z : Ω → ℝ} (hX : Measurable X) (hZ : Measurable Z) (c : ℝ) :
    Integrable (fun w => signedCut c (X w) * signedCut c (Z w)) μ := by
  apply Integrable.mono' (integrable_const (1 : ℝ))
    (((measurable_signedCut c).comp hX).mul ((measurable_signedCut c).comp hZ)).aestronglyMeasurable
  apply Filter.Eventually.of_forall
  intro w
  rw [Real.norm_eq_abs, abs_mul]
  simpa using mul_le_mul (abs_signedCut_le_one c (X w)) (abs_signedCut_le_one c (Z w))
    (abs_nonneg _) (by norm_num : (0 : ℝ) ≤ 1)

theorem tail_transfer (μ : Measure Ω) [IsFiniteMeasure μ] {X Z : Ω → ℝ}
    (hX : Measurable X) (hZ : Measurable Z) (u : ℝ) (hu : 0 ≤ u)
    (hcut : (∫ w, signedCut (u/2) (X w) * signedCut (u/2) (Z w) ∂μ) ≤ 0) :
    μ.real {w | 3*u/2 < |X w|} ≤ 2 * μ.real {w | u < |X w - Z w|} := by
  let A := {w | 3*u/2 < |X w|}
  let B := {w | u < |X w - Z w|}
  have hA : MeasurableSet A := measurableSet_lt measurable_const (continuous_abs.measurable.comp hX)
  have hB : MeasurableSet B := measurableSet_lt measurable_const
    (continuous_abs.measurable.comp (hX.sub hZ))
  have iA : Integrable (A.indicator (fun _ => (1 : ℝ))) μ := (integrable_const _).indicator hA
  have iB : Integrable (B.indicator (fun _ => (1 : ℝ))) μ := (integrable_const _).indicator hB
  have hi := integral_mono iA ((iB.const_mul 2).add (cutProduct_integrable μ hX hZ (u/2)))
    (fun w => by
      simpa only [Set.indicator_apply, A, B, Set.mem_setOf_eq, Pi.add_apply] using
        tail_pointwise (X w) (Z w) u hu)
  change (∫ w, A.indicator (fun _ => (1 : ℝ)) w ∂μ) ≤
    ∫ w, 2 * B.indicator (fun _ => (1 : ℝ)) w +
      signedCut (u/2) (X w) * signedCut (u/2) (Z w) ∂μ at hi
  rw [integral_add (iB.const_mul 2) (cutProduct_integrable μ hX hZ _), integral_const_mul,
      integral_indicator_const _ hA, integral_indicator_const _ hB] at hi
  simp only [smul_eq_mul, mul_one] at hi
  change μ.real A ≤ 2 * μ.real B
  linarith

-- NATIVE CHILD 2

/-- A reflected half-test yields a tail bound for the sum of its reflected pair. -/
theorem reflected_tail (μ : Measure Ω) [IsFiniteMeasure μ]
    (θ : Ω → Ω) (hθ : Measurable θ) (Y : Ω → ℝ) (hY : Measurable Y)
    (u : ℝ) (hu : 0 ≤ u)
    (hrp : 0 ≤ ∫ w, signedCut (u/2) (Y w) * signedCut (u/2) (Y (θ w)) ∂μ) :
    μ.real {w | 3*u/2 < |Y w|} ≤ 2 * μ.real {w | u < |Y w + Y (θ w)|} := by
  have hc : 0 ≤ u/2 := by linarith
  have he : (∫ w, signedCut (u/2) (Y w) * signedCut (u/2) (-Y (θ w)) ∂μ) ≤ 0 := by
    simpa only [signedCut_odd hc, mul_neg, integral_neg, neg_nonpos] using hrp
  simpa only [sub_neg_eq_add] using
    tail_transfer μ hY (hY.comp hθ).neg u hu he

#print axioms signedCut
#print axioms signedCut_odd
#print axioms abs_signedCut_le_one
#print axioms measurable_signedCut
#print axioms tail_pointwise
#print axioms cutProduct_integrable
#print axioms tail_transfer
#print axioms reflected_tail

/-- Continuous approximation to the strict positive half-line indicator. -/
def ramp (n : ℕ) (v : ℝ) : ℝ := min 1 (max 0 ((n : ℝ) * v))

theorem ramp_bounds (n : ℕ) (v : ℝ) : 0 ≤ ramp n v ∧ ramp n v ≤ 1 :=
  ⟨le_min (by norm_num) (le_max_left _ _), min_le_left _ _⟩

theorem ramp_eventually (v : ℝ) :
    ∀ᶠ n : ℕ in Filter.atTop, ramp n v = if 0 < v then 1 else 0 := by
  by_cases hv : 0 < v
  · obtain ⟨N, hN⟩ := exists_nat_ge (1/v)
    filter_upwards [Filter.eventually_ge_atTop N] with n hn
    have hn' : (1 : ℝ)/v ≤ (n : ℝ) := hN.trans (by exact_mod_cast hn)
    have h := (div_le_iff₀ hv).mp hn'
    simp [ramp, hv, max_eq_right (show 0 ≤ (n : ℝ)*v by positivity), min_eq_left h]
  · exact Filter.Eventually.of_forall fun n => by
      simp [ramp, hv, max_eq_left (mul_nonpos_of_nonneg_of_nonpos (Nat.cast_nonneg n) (le_of_not_gt hv))]

def continuousCut (n : ℕ) (c a : ℝ) : ℝ := ramp n (a-c) - ramp n (-a-c)

theorem continuous_continuousCut (n : ℕ) (c : ℝ) : Continuous (continuousCut n c) := by
  unfold continuousCut ramp
  fun_prop

theorem abs_continuousCut_le_one (n : ℕ) (c a : ℝ) : |continuousCut n c a| ≤ 1 := by
  obtain ⟨h₁,h₂⟩ := ramp_bounds n (a-c)
  obtain ⟨h₃,h₄⟩ := ramp_bounds n (-a-c)
  unfold continuousCut
  exact abs_le.mpr ⟨by linarith, by linarith⟩

theorem continuousCut_eventually {c : ℝ} (hc : 0 ≤ c) (a : ℝ) :
    ∀ᶠ n : ℕ in Filter.atTop, continuousCut n c a = signedCut c a := by
  filter_upwards [ramp_eventually (a-c), ramp_eventually (-a-c)] with n hn hp
  unfold continuousCut signedCut
  rw [hn,hp]
  split_ifs <;> linarith

/-- Continuous bounded scalar half-tests suffice, even at atoms of the threshold law. -/
theorem reflected_tail_of_continuous_tests (μ : Measure Ω) [IsFiniteMeasure μ]
    (θ : Ω → Ω) (hθ : Measurable θ) (Y : Ω → ℝ) (hY : Measurable Y)
    (hrp : ∀ f : ℝ → ℝ, Continuous f → (∀ a, |f a| ≤ 1) →
      0 ≤ ∫ w, f (Y w) * f (Y (θ w)) ∂μ)
    (u : ℝ) (hu : 0 ≤ u) :
    μ.real {w | 3*u/2 < |Y w|} ≤ 2 * μ.real {w | u < |Y w + Y (θ w)|} := by
  apply reflected_tail μ θ hθ Y hY u hu
  let c := u / 2
  have hc : 0 ≤ c := by dsimp [c]; linarith
  let F (n : ℕ) (w : Ω) := continuousCut n c (Y w) * continuousCut n c (Y (θ w))
  have hm (n : ℕ) : Measurable (F n) :=
    (((continuous_continuousCut n c).measurable.comp hY).mul
      ((continuous_continuousCut n c).measurable.comp (hY.comp hθ)))
  have hb (n : ℕ) (w : Ω) : ‖F n w‖ ≤ (1 : ℝ) := by
    simp only [F, Real.norm_eq_abs, abs_mul]
    simpa using mul_le_mul (abs_continuousCut_le_one n c (Y w)) (abs_continuousCut_le_one n c (Y (θ w)))
      (abs_nonneg _) (by norm_num : (0 : ℝ) ≤ 1)
  have hl (w : Ω) : Filter.Tendsto (fun n => F n w) Filter.atTop
      (𝓝 (signedCut c (Y w) * signedCut c (Y (θ w)))) := by
    apply Filter.Tendsto.congr' _ tendsto_const_nhds
    filter_upwards [continuousCut_eventually hc (Y w), continuousCut_eventually hc (Y (θ w))] with n h₁ h₂
    simp only [F, h₁, h₂]
  exact ge_of_tendsto' (tendsto_integral_of_dominated_convergence (fun _ => (1 : ℝ))
    (fun n => (hm n).aestronglyMeasurable) (integrable_const _)
    (fun n => Filter.Eventually.of_forall (hb n)) (Filter.Eventually.of_forall hl))
    (fun n => hrp _ (continuous_continuousCut n c) (abs_continuousCut_le_one n c))

#print axioms ramp
#print axioms ramp_bounds
#print axioms ramp_eventually
#print axioms continuousCut
#print axioms continuous_continuousCut
#print axioms abs_continuousCut_le_one
#print axioms continuousCut_eventually
#print axioms reflected_tail_of_continuous_tests

end Millennium.G4.ReflectedTails
