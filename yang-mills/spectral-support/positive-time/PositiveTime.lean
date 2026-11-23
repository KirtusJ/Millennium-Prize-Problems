import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

open Filter MeasureTheory Set
open scoped Topology ENNReal

namespace Millennium.YangMills.D4

/-- The unnormalized Euclidean two-point function at physical time s. -/
noncomputable def laplace (ν : Measure ℝ) (s : ℝ) : ℝ :=
  ∫ E, Real.exp (-E * s) ∂ν

private theorem tilt (b E s : ℝ) :
    Real.exp (b*s) * Real.exp (-E*s) = Real.exp ((b-E)*s) := by
  rw [← Real.exp_add]
  congr 1
  ring

/-- The tilted contribution of each energy is monotone in time in one direction.
Its value inside a time window is bounded by the sum of its endpoint values. -/
theorem tiltedWindow (ν : Measure ℝ) (b : ℝ) {u t T : ℝ}
    (hut : u ≤ t) (htT : t ≤ T)
    (iu : Integrable (fun E : ℝ => Real.exp (-E*u)) ν)
    (it : Integrable (fun E : ℝ => Real.exp (-E*t)) ν)
    (iT : Integrable (fun E : ℝ => Real.exp (-E*T)) ν) :
    Real.exp (b*t) * laplace ν t ≤
      Real.exp (b*u) * laplace ν u + Real.exp (b*T) * laplace ν T := by
  have hu := iu.const_mul (Real.exp (b*u))
  have hT := iT.const_mul (Real.exp (b*T))
  unfold laplace
  simp only [← integral_const_mul]
  rw [← integral_add hu hT]
  apply integral_mono (it.const_mul _) (hu.add hT)
  intro E
  simp only [tilt, Pi.add_apply]
  rcases le_total b E with h | h
  · exact (Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left hut (sub_nonpos.mpr h))).trans
      (le_add_of_nonneg_right (Real.exp_pos _).le)
  · exact (Real.exp_le_exp.mpr (mul_le_mul_of_nonneg_left htT (sub_nonneg.mpr h))).trans
      (le_add_of_nonneg_left (Real.exp_pos _).le)

/-- Transfer a cofinal late-time estimate without weak or equal-time convergence.
The physical clock readings u_k and t_k may drift with the cutoff. -/
theorem positiveTimeTransfer (ν : ℕ → Measure ℝ) (u t T : ℕ → ℝ) {u₀ t₀ U V m : ℝ}
    (hu : Tendsto u atTop (𝓝 u₀)) (ht : Tendsto t atTop (𝓝 t₀))
    (window : ∀ᶠ k in atTop, u k ≤ t k ∧ t k ≤ T k)
    (iu : ∀ k, Integrable (fun E : ℝ => Real.exp (-E * u k)) (ν k))
    (it : ∀ k, Integrable (fun E : ℝ => Real.exp (-E * t k)) (ν k))
    (iT : ∀ k, Integrable (fun E : ℝ => Real.exp (-E * T k)) (ν k))
    (anchor : Tendsto (fun k => laplace (ν k) (u k)) atTop (𝓝 U))
    (observed : Tendsto (fun k => laplace (ν k) (t k)) atTop (𝓝 V))
    (late : ∀ b < m, Tendsto (fun k => Real.exp (b*T k) * laplace (ν k) (T k)) atTop (𝓝 0)) :
    Real.exp (m*t₀) * V ≤ Real.exp (m*u₀) * U := by
  have below (b : ℝ) (_hb : b ∈ Iio m) : Real.exp (b*t₀) * V ≤ Real.exp (b*u₀) * U := by
    have lhs := ((tendsto_const_nhds (x := b)).mul ht).rexp.mul observed
    have rhs := (((tendsto_const_nhds (x := b)).mul hu).rexp.mul anchor).add (late b _hb)
    apply le_of_tendsto_of_tendsto lhs (by simpa using rhs)
    filter_upwards [window] with k hk using tiltedWindow (ν k) b hk.1 hk.2 (iu k) (it k) (iT k)
  exact le_on_closure below
    (((Real.continuous_exp.comp (continuous_id.mul continuous_const)).mul continuous_const).continuousOn)
    (((Real.continuous_exp.comp (continuous_id.mul continuous_const)).mul continuous_const).continuousOn)
    (by simp : m ∈ closure (Iio m))

/-- A fixed exponential envelope at actual cofinal physical times implies the
late hypothesis at every strict subrate. -/
theorem subrateOfEnvelope {C T : ℕ → ℝ} {m M : ℝ} (hT : Tendsto T atTop atTop)
    (positive : ∀ k, 0 ≤ C k)
    (envelope : ∀ᶠ k in atTop, C k ≤ M * Real.exp (-m*T k)) (b : ℝ) (hb : b < m) :
    Tendsto (fun k => Real.exp (b*T k) * C k) atTop (𝓝 0) := by
  have dec := Real.tendsto_exp_neg_atTop_nhds_zero.comp
    ((tendsto_const_mul_atTop_of_pos (sub_pos.mpr hb)).2 hT)
  have lim := (tendsto_const_nhds (x := M)).mul dec
  apply squeeze_zero' (Eventually.of_forall fun k => mul_nonneg (Real.exp_pos _).le (positive k))
    _ (by simpa using lim)
  filter_upwards [envelope] with k hk
  calc
    _ ≤ Real.exp (b*T k) * (M * Real.exp (-m*T k)) := mul_le_mul_of_nonneg_left hk (Real.exp_pos _).le
    _ = M * Real.exp (-((m-b)*T k)) := by
      rw [mul_left_comm, ← Real.exp_add]
      congr 2
      ring

/-- A reconstructed measure with bounded tilted moments at cofinal positive
times puts zero mass below the rate, even when its total mass is infinite. -/
theorem energySupportOfEnvelope (μ : Measure ℝ) (T : ℕ → ℝ) {m M : ℝ}
    (hT : Tendsto T atTop atTop) (clock : ∀ k, 0 ≤ T k)
    (integrable : ∀ k, Integrable (fun E : ℝ => Real.exp (-E*T k)) μ)
    (envelope : ∀ᶠ k in atTop, laplace μ (T k) ≤ M * Real.exp (-m*T k)) :
    μ (Iio m) = 0 := by
  have tail (b : ℝ) (hb : b < m) : μ (Iic b) = 0 := by
    have nonneg (k : ℕ) : 0 ≤ laplace μ (T k) := integral_nonneg fun E => (Real.exp_pos _).le
    have lim := subrateOfEnvelope hT nonneg
      envelope b hb
    have bound (k : ℕ) : μ (Iic b) ≤ ENNReal.ofReal (Real.exp (b*T k) * laplace μ (T k)) := by
      unfold laplace
      rw [← integral_const_mul]
      apply ((integrable k).const_mul (Real.exp (b*T k))).measure_le_integral
        (ae_of_all _ fun E => mul_nonneg (Real.exp_pos _).le (Real.exp_pos _).le)
      intro E hE
      rw [tilt, Real.one_le_exp_iff]
      exact mul_nonneg (sub_nonneg.mpr hE) (clock k)
    apply le_antisymm _ (zero_le _)
    exact ge_of_tendsto' (by simpa only [Function.comp_def, ENNReal.ofReal_zero] using ENNReal.tendsto_ofReal lim) bound
  let b (n : ℕ) : ℝ := m - 1 / (n + 1 : ℝ)
  have cover : Iio m ⊆ ⋃ n, Iic (b n) := by
    intro E hE
    obtain ⟨n, hn⟩ := exists_nat_one_div_lt (sub_pos.mpr (show E < m from hE))
    exact mem_iUnion.mpr ⟨n, show E ≤ m - 1 / (n + 1 : ℝ) by linarith⟩
  exact measure_mono_null cover (measure_iUnion_null fun n => tail (b n) (sub_lt_self _ (by positivity)))

/-- A single positive-time anchor bounding the tilted reconstructed correlator
on a cofinal sequence suffices to apply the spectral support theorem. -/
theorem supportFromPositiveAnchor (μ : Measure ℝ) (T : ℕ → ℝ) {m u U : ℝ}
    (hT : Tendsto T atTop atTop) (clock : ∀ k, 0 ≤ T k)
    (integrable : ∀ k, Integrable (fun E : ℝ => Real.exp (-E*T k)) μ)
    (comparison : ∀ᶠ k in atTop, Real.exp (m*T k) * laplace μ (T k) ≤ Real.exp (m*u) * U) :
    μ (Iio m) = 0 := by
  apply energySupportOfEnvelope μ T (M := Real.exp (m*u)*U) hT clock integrable
  filter_upwards [comparison] with k hk
  have h := mul_le_mul_of_nonneg_right hk (Real.exp_pos (-m*T k)).le
  simpa only [mul_right_comm (Real.exp (m*T k)), ← Real.exp_add, neg_mul,
    add_neg_cancel, Real.exp_zero, one_mul] using h

/-- One unit-weight state at each integer energy 1,...,N. Here q=exp(-s). -/
noncomputable def tower (N : ℕ) (q : ℝ) : ℝ :=
  q * ∑ j ∈ Finset.range N, q ^ j

theorem towerAtZero (N : ℕ) : tower N 1 = N := by simp [tower]

theorem towerAtPositiveTime {q : ℝ} (hq : 0 ≤ q) (hq1 : q < 1) :
    Tendsto (fun N => tower N q) atTop (𝓝 (q * (1-q)⁻¹)) := by
  exact tendsto_const_nhds.mul (hasSum_geometric_of_lt_one hq hq1).tendsto_sum_nat

theorem towerLateBound (N : ℕ) {q : ℝ} (hq : 0 ≤ q) (hhalf : q ≤ 1/2) :
    tower N q ≤ 2*q := by
  have partialSum : ∑ j ∈ Finset.range N, q^j ≤ (2 : ℝ) := by
    calc
      _ ≤ ∑ j ∈ Finset.range N, ((1:ℝ)/2)^j :=
        Finset.sum_le_sum fun j _ => pow_le_pow_left₀ hq hhalf j
      _ ≤ 2 := sum_le_hasSum _ (fun j _ => pow_nonneg (by norm_num) j) hasSum_geometric_two
  simpa only [tower, mul_comm (2:ℝ) q] using mul_le_mul_of_nonneg_left partialSum hq

/-- A lattice transfer spectrum in [0,q] contracts between any two samples of
the same vector. Its total norm may grow across the regulators. -/
theorem laterMomentBound (ν : Measure ℝ) {q : ℝ} (n d : ℕ)
    (spectrum : ∀ᵐ x ∂ν, 0 ≤ x ∧ x ≤ q)
    (earlier : Integrable (fun x : ℝ => x^n) ν)
    (later : Integrable (fun x : ℝ => x^(n+d)) ν) :
    (∫ x, x^(n+d) ∂ν) ≤ q^d * ∫ x, x^n ∂ν := by
  rw [← integral_const_mul]
  apply integral_mono_ae later (earlier.const_mul _)
  filter_upwards [spectrum] with x hx
  rw [pow_add, mul_comm (q^d)]
  exact mul_le_mul_of_nonneg_left (pow_le_pow_left₀ hx.1 hx.2 d) (pow_nonneg hx.1 n)

/-- A fixed lattice-unit contraction kills every later physical correlation
whenever the earlier separation has an eventually bounded correlation. -/
theorem collapseAfterPositiveTime (ν : ℕ → Measure ℝ) (n d : ℕ → ℕ) {B q : ℝ}
    (hq : 0 ≤ q) (hq1 : q < 1) (steps : Tendsto d atTop atTop)
    (spectrum : ∀ k, ∀ᵐ x ∂(ν k), 0 ≤ x ∧ x ≤ q)
    (earlier : ∀ k, Integrable (fun x : ℝ => x^(n k)) (ν k))
    (later : ∀ k, Integrable (fun x : ℝ => x^(n k + d k)) (ν k))
    (anchor : ∀ᶠ k in atTop, (∫ x, x^(n k) ∂(ν k)) ≤ B) :
    Tendsto (fun k => ∫ x, x^(n k + d k) ∂(ν k)) atTop (𝓝 0) := by
  have lim := ((tendsto_pow_atTop_nhds_zero_of_lt_one hq hq1).comp steps).mul
    (tendsto_const_nhds (x := B))
  apply squeeze_zero' _ _ (by simpa using lim)
  · apply Eventually.of_forall
    intro k
    apply integral_nonneg_of_ae
    filter_upwards [spectrum k] with x hx using pow_nonneg hx.1 _
  · filter_upwards [anchor] with k hk
    exact (laterMomentBound (ν k) (n k) (d k) (spectrum k) (earlier k) (later k)).trans
      (mul_le_mul_of_nonneg_left hk (pow_nonneg hq _))

/-- Conditional independence reduces a covariance to the inner product of two
centered exterior conditional means in real L². This is the Hilbert-space step. -/
theorem exteriorPairBound {H : Type*} [SeminormedAddCommGroup H] [InnerProductSpace ℝ H]
    (f g : H) {cov θ φ : ℝ} (identity : cov = inner ℝ f g)
    (hf : ‖f‖ ≤ 2 * Real.exp (-θ)) (hg : ‖g‖ ≤ 2 * Real.exp (-φ)) :
    |cov| ≤ 4 * Real.exp (-θ) * Real.exp (-φ) := by
  rw [identity]
  calc
    _ ≤ ‖f‖ * ‖g‖ := abs_real_inner_le_norm f g
    _ ≤ (2*Real.exp (-θ)) * (2*Real.exp (-φ)) :=
      mul_le_mul hf hg (norm_nonneg _) (by positivity)
    _ = _ := by ring

/-- Divergent renormalizations are allowed if both weighted conditional means vanish. -/
theorem renormalizedPairVanishes (C Z W θ φ : ℕ → ℝ)
    (bound : ∀ᶠ k in atTop, |C k| ≤ 4 * Real.exp (-θ k) * Real.exp (-φ k))
    (hZ : Tendsto (fun k => |Z k| * Real.exp (-θ k)) atTop (𝓝 0))
    (hW : Tendsto (fun k => |W k| * Real.exp (-φ k)) atTop (𝓝 0)) :
    Tendsto (fun k => Z k * W k * C k) atTop (𝓝 0) := by
  apply tendsto_zero_iff_norm_tendsto_zero.mpr
  have lim := ((tendsto_const_nhds (x := (4:ℝ))).mul hZ).mul hW
  apply squeeze_zero' (Eventually.of_forall fun k => norm_nonneg _) _ (by simpa using lim)
  filter_upwards [bound] with k hk
  simp only [Real.norm_eq_abs, abs_mul]
  calc
    _ ≤ |Z k| * |W k| * (4 * Real.exp (-θ k) * Real.exp (-φ k)) :=
      mul_le_mul_of_nonneg_left hk (mul_nonneg (abs_nonneg _) (abs_nonneg _))
    _ = _ := by ring

/-- A one-step Laplace measurement bounds a moving low-energy threshold. -/
theorem scaledLowEnergyBound (μ : Measure ℝ) (a R : ℝ)
    (int : Integrable (fun E : ℝ => Real.exp (-E*a)) μ) :
    μ {E | a*E ≤ R} ≤ ENNReal.ofReal (Real.exp R * laplace μ a) := by
  unfold laplace
  rw [← integral_const_mul]
  apply (int.const_mul (Real.exp R)).measure_le_integral
    (ae_of_all _ fun E => mul_nonneg (Real.exp_pos _).le (Real.exp_pos _).le)
  intro E hE
  rw [← Real.exp_add, Real.one_le_exp_iff]
  have : a*E ≤ R := hE
  nlinarith only [this]

-- BEGIN PCP OS generated signed-spectrum control
noncomputable def signedShape (q : ℝ) : ℝ := 1 - 4*q + 4*q^2

/-- Pointwise nonnegativity coexists with a zero at the late sample. -/
theorem signedShapeControl : (∀ q : ℝ, 0 ≤ signedShape q) ∧
    signedShape (1/2) = 0 ∧ signedShape 1 = 1 := by
  refine ⟨fun q => ?_, by norm_num [signedShape], by norm_num [signedShape]⟩
  unfold signedShape
  nlinarith only [sq_nonneg (1-2*q)]

/-- Reflected times T/2 and 3T/2 with the positive energy factor scaled out. -/
theorem signedReflectionWitness :
    2^2 * signedShape (1/2) + 2*2*(-1) * signedShape (1/4)
      + (-1)^2 * signedShape (1/8) = -7/16 := by norm_num [signedShape]

#print axioms tiltedWindow
#print axioms positiveTimeTransfer
#print axioms subrateOfEnvelope
#print axioms energySupportOfEnvelope
#print axioms supportFromPositiveAnchor
#print axioms towerAtZero
#print axioms towerAtPositiveTime
#print axioms towerLateBound
#print axioms laterMomentBound
#print axioms collapseAfterPositiveTime
#print axioms exteriorPairBound
#print axioms renormalizedPairVanishes
#print axioms scaledLowEnergyBound
#print axioms signedShapeControl
#print axioms signedReflectionWitness

end Millennium.YangMills.D4
