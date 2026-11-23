import Mathlib.Analysis.Complex.AbsMax
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Tactic.Linarith

open MeasureTheory Set Filter
namespace YangMills.UniformBand

/-- The high-order zero is supplied as a holomorphic quotient g. -/
theorem diskPower {g : ℂ → ℂ} {R M : ℝ} (n : ℕ) (hr : 0 < R)
    (hg : DiffContOnCl ℂ g (Metric.ball 0 R))
    (hb : ∀ z : ℂ, ‖z‖ = R → ‖z^n*g z‖ ≤ M)
    {w : ℂ} (hw : w ∈ closure (Metric.ball 0 R)) :
    ‖w^n*g w‖ ≤ (‖w‖/R)^n*M := by
  have inner : ‖g w‖ ≤ M/R^n := by
    apply Complex.norm_le_of_forall_mem_frontier_norm_le Metric.isBounded_ball hg _ hw
    rw [frontier_ball (0 : ℂ) hr.ne']
    intro z hz
    have hz' : ‖z‖ = R := by simpa [Metric.mem_sphere] using hz
    have h := hb z hz'
    rw [norm_mul, norm_pow, hz'] at h
    exact (le_div_iff₀ (pow_pos hr n)).2 (by simpa [mul_comm] using h)
  rw [norm_mul, norm_pow, div_pow]
  calc
    _ ≤ ‖w‖^n*(M/R^n) := mul_le_mul_of_nonneg_left inner (pow_nonneg (norm_nonneg _) _)
    _ = _ := by ring

/-- An arbitrary fixed prefactor disappears when all moment orders are tested. -/
theorem zeroTail {m C q : ℝ} (hm : 0 ≤ m) (hq : 1 < q)
    (h : ∀ n : ℕ, m*q^n ≤ C) : m = 0 := by
  by_contra ne
  have hp : 0 < m := lt_of_le_of_ne hm (Ne.symm ne)
  obtain ⟨n, hn⟩ := pow_unbounded_of_one_lt (C/m) hq
  have hn' := (div_lt_iff₀ hp).mp hn
  linarith [h n, mul_comm m (q^n)]

theorem momentTail {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsFiniteMeasure μ]
    (f : X → ℝ) (s : Set X) (hs : MeasurableSet s) {q C : ℝ} (hq : 1 < q)
    (hf : ∀ x, 0 ≤ f x) (lower : ∀ x ∈ s, q ≤ f x)
    (hi : ∀ n : ℕ, Integrable (fun x => f x ^ n) μ)
    (bound : ∀ n : ℕ, ∫ x, f x^n ∂μ ≤ C) : μ.real s = 0 := by
  apply zeroTail measureReal_nonneg hq
  intro n
  have le := setIntegral_mono_on (μ := μ)
    (f := fun _ : X => q^n) (integrable_const _).integrableOn (hi n).integrableOn hs
    (fun x hx => pow_le_pow_left₀ (by linarith : 0 ≤ q) (lower x hx) n)
  simpa [setIntegral_const, smul_eq_mul] using
    le.trans ((setIntegral_le_integral (hi n)
      (Filter.Eventually.of_forall fun x => pow_nonneg (hf x) n)).trans (bound n))

/-- Apply the two alternatives to the vacuum-subtracted scaled transfer. -/
theorem split {x b e : ℝ} (hb : 3/4 ≤ b)
    (h : |x^2*(x-b)| ≤ e) :
    x^2 ≤ 4*e ∨ |x-b| ≤ 4*e := by
  rw [abs_mul, abs_of_nonneg (sq_nonneg x)] at h
  by_cases small : x ≤ 1/2
  · left
    have ht : 1/4 ≤ |x-b| := by rw [abs_of_nonpos (by linarith)]; linarith
    nlinarith [mul_le_mul_of_nonneg_left ht (sq_nonneg x)]
  · right
    have ht : (1/2:ℝ)^2 ≤ x^2 := pow_le_pow_left₀ (by norm_num) (le_of_not_ge small) 2
    nlinarith [mul_le_mul_of_nonneg_right ht (abs_nonneg (x-b))]

theorem seedCoefficient : (4*(-1/24)-2*(1/4)^2 : ℝ) = -7/24 := by norm_num

theorem nearSimpleRoot {x a b c e d : ℝ} (hd : 0 < d)
    (hb : d ≤ |x-b|) (hc : d ≤ |x-c|) (h : |(x-a)*(x-b)*(x-c)| ≤ e) :
    |x-a| ≤ e/d^2 := by
  rw [abs_mul, abs_mul] at h
  apply (le_div_iff₀ (sq_pos_of_pos hd)).2
  calc
    _ ≤ |x-a| * (|x-b| * |x-c|) := by
      apply mul_le_mul_of_nonneg_left _ (abs_nonneg _)
      simpa [pow_two] using mul_le_mul hb hc hd.le (abs_nonneg _)
    _ ≤ e := by simpa [mul_assoc] using h

theorem quarticCoefficient (θ : ℝ) :
    (1/48 + 1/96 + 1/128 + 1/48 + θ/256 : ℝ) = 23/384 + θ/256 := by ring

theorem secondLagUpper {y d : ℝ} (hy : |y-1| ≤ d) :
    |1-y^2| ≤ d*(2+d) := by
  rw [show 1-y^2 = -(y-1)*(y+1) by ring, abs_mul, abs_neg]
  have hb : |y+1| ≤ 2+d := by
    calc
      |y+1| = |(y-1)+2| := by ring_nf
      _ ≤ |y-1|+|2| := abs_add_le _ _
      _ ≤ 2+d := by rw [abs_of_nonneg (by norm_num : (0:ℝ) ≤ 2)]; linarith
  exact mul_le_mul hy hb (abs_nonneg _) ((abs_nonneg _).trans hy)

theorem secondLagLower {y d : ℝ} (hy : 0 ≤ y) (hd : y ≤ d) :
    |y^2| ≤ d^2 := by
  rw [abs_of_nonneg (sq_nonneg _)]
  exact pow_le_pow_left₀ hy hd 2

/-- Two centered atoms and a centered atom split into a wider pair agree
through the third raw moment. -/
noncomputable def mix (a d : ℝ) (n : ℕ) : ℝ := 1-a+a*((1-d)^n+(1+d)^n)/2

theorem matched (a w : ℝ) :
    ∀ n ∈ Finset.range 4, mix a (w/2) n = mix (a/16) (2*w) n := by
  intro n hn
  have hn' := Finset.mem_range.mp hn
  interval_cases n <;> unfold mix <;> ring

end YangMills.UniformBand
#print axioms YangMills.UniformBand.zeroTail
#print axioms YangMills.UniformBand.momentTail
#print axioms YangMills.UniformBand.split
#print axioms YangMills.UniformBand.seedCoefficient
#print axioms YangMills.UniformBand.matched
#print axioms YangMills.UniformBand.diskPower
#print axioms YangMills.UniformBand.nearSimpleRoot
#print axioms YangMills.UniformBand.quarticCoefficient
#print axioms YangMills.UniformBand.secondLagUpper
#print axioms YangMills.UniformBand.secondLagLower
