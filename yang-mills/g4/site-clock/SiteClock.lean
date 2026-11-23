import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.Linarith

noncomputable section
open MeasureTheory
namespace Millennium.G4.SiteClock

variable {α : Type*} [MeasurableSpace α]

/-- Bound the low end of a contraction moment by its cutoff and the mass above it. -/
theorem moment_cut_upper (μ : Measure α) [IsFiniteMeasure μ] {S : Set α}
    (hs : MeasurableSet S) {f : α → ℝ} (hf : Integrable f μ) {r : ℝ}
    (hr : 0 ≤ r) (hout : ∀ x ∉ S, f x ≤ r) (hin : ∀ x ∈ S, f x ≤ 1) :
    (∫ x, f x ∂μ) ≤ μ.real Set.univ * r + μ.real S := by
  have hi : Integrable (S.indicator (fun _ : α => (1 : ℝ))) μ :=
    (integrable_const _).indicator hs
  have hb : ∀ x, f x ≤ r + S.indicator (fun _ : α => (1 : ℝ)) x := by
    intro x
    by_cases hx : x ∈ S
    · simp only [Set.indicator_of_mem hx]
      linarith [hin x hx]
    · simpa only [Set.indicator_of_not_mem hx, add_zero] using hout x hx
  calc
    (∫ x, f x ∂μ) ≤ ∫ x, r + S.indicator (fun _ : α => (1 : ℝ)) x ∂μ :=
      integral_mono hf ((integrable_const r).add hi) hb
    _ = μ.real Set.univ * r + μ.real S := by
      rw [integral_add (integrable_const r) hi, integral_const, integral_indicator hs,
        setIntegral_const, smul_eq_mul, smul_eq_mul, mul_one]

-- NATIVE CHILD 1
/-- Positive mass on a spectral window gives a positive integrated moment. -/
theorem moment_cut_lower (μ : Measure α) [IsFiniteMeasure μ] {S : Set α}
    (hs : MeasurableSet S) {f : α → ℝ} (hf : Integrable f μ)
    (hn : ∀ x, 0 ≤ f x) {c : ℝ} (hc : 0 < c) (hS : ∀ x ∈ S, c ≤ f x)
    (hm : 0 < μ.real S) : 0 < ∫ x, f x ∂μ := by
  have hi : Integrable (S.indicator (fun _ : α => c)) μ :=
    (integrable_const c).indicator hs
  have hb : ∀ x, S.indicator (fun _ : α => c) x ≤ f x := by
    intro x
    by_cases hx : x ∈ S
    · simpa only [Set.indicator_of_mem hx] using hS x hx
    · simpa only [Set.indicator_of_not_mem hx] using hn x
  have h := integral_mono hi hf hb
  rw [integral_indicator hs, setIntegral_const, smul_eq_mul] at h
  exact lt_of_lt_of_le (mul_pos hm hc) h

/-- A uniform polynomial approximation controls its integral against spectral mass. -/
theorem integral_truncation (μ : Measure α) [IsFiniteMeasure μ] {f p : α → ℝ}
    (hf : Integrable f μ) (hp : Integrable p μ) {e : ℝ} (h : ∀ x, |f x - p x| ≤ e) :
    |(∫ x, f x ∂μ) - (∫ x, p x ∂μ)| ≤ μ.real Set.univ * e := by
  rw [← integral_sub hf hp]
  calc
    |∫ x, f x - p x ∂μ| ≤ ∫ x, |f x - p x| ∂μ := abs_integral_le_integral_abs
    _ ≤ ∫ _ : α, e ∂μ := integral_mono (hf.sub hp).abs (integrable_const e) h
    _ = μ.real Set.univ * e := by rw [integral_const, smul_eq_mul]

-- NATIVE CHILD 2
/-- A lower bound on successive ratios propagates an observed positive moment. -/
theorem anchor_floor (M : ℕ → ℝ) {r : ℕ} {q : ℝ} (hq : 0 ≤ q)
    (h : ∀ k, M (r+k)*q ≤ M (r+(k+1))) (t : ℕ) :
    M r * q^t ≤ M (r+t) := by
  induction t with
  | zero => simp
  | succ t ih =>
    calc
      M r * q^(t+1) = (M r * q^t)*q := by rw [pow_succ, mul_assoc]
      _ ≤ M (r+t)*q := mul_le_mul_of_nonneg_right ih hq
      _ ≤ M (r+(t+1)) := h t

theorem midpoint_interval {a b loA hiA loB hiB : ℝ} (ha : loA ≤ a) (ha' : a ≤ hiA) (hb : loB ≤ b) (hb' : b ≤ hiB) (hlo : 0 < loB) (hz : 0 ≤ loA) : loA / hiB ≤ a / b ∧ a / b ≤ hiA / loB := by
  have hbpos : 0 < b := lt_of_lt_of_le hlo hb
  have hhipos : 0 < hiB := lt_of_lt_of_le hbpos hb'
  have hhiA : 0 ≤ hiA := le_trans hz (le_trans ha ha')
  constructor
  · apply (div_le_div_iff₀ hhipos hbpos).2
    calc
      loA * b ≤ loA * hiB := mul_le_mul_of_nonneg_left hb' hz
      _ ≤ a * hiB := mul_le_mul_of_nonneg_right ha hhipos.le
  · apply (div_le_div_iff₀ hbpos hlo).2
    calc
      a * loB ≤ hiA * loB := mul_le_mul_of_nonneg_right ha' hlo.le
      _ ≤ hiA * b := mul_le_mul_of_nonneg_left hb hhiA

#print axioms moment_cut_upper
#print axioms moment_cut_lower
#print axioms integral_truncation
#print axioms anchor_floor
#print axioms midpoint_interval

end Millennium.G4.SiteClock
