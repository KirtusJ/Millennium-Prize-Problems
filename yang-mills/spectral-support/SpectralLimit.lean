import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! Scalar transfer moments and coverage of a spectral projection.
The power variable is x = exp(-tau * E), with fixed positive physical time step.
Construction of the Hamiltonian and the regulator bound are separate obligations. -/

open Filter MeasureTheory Set
open scoped Topology

namespace Millennium.YangMills.D4

/-- If N regulator steps cover the requested physical time, a one-step defect
estimate yields a decay envelope at that time. -/
theorem decayAtRoundedTime {q a m time : ℝ} (N : ℕ) (hq : 0 ≤ q) (hm : 0 ≤ m)
    (oneStep : q ≤ 1 - a * m) (clock : time ≤ (N : ℝ) * a) :
    q ^ N ≤ Real.exp (-m * time) := by
  have one : q ≤ Real.exp (-a * m) := by
    linarith only [oneStep, Real.add_one_le_exp (-a * m)]
  calc
    q ^ N ≤ (Real.exp (-a * m)) ^ N := pow_le_pow_left₀ hq one N
    _ = Real.exp ((N : ℝ) * (-a * m)) := (Real.exp_nat_mul _ _).symm
    _ ≤ _ := Real.exp_le_exp.mpr (by nlinarith only [mul_nonneg hm (sub_nonneg.mpr clock)])

/-- A cutoff-independent bound along an unbounded sequence of integer times passes to the limiting positive measure.
The regulator threshold may depend on the chosen time. -/
theorem noTransferMassAbove
    (μ : Measure ℝ) [IsFiniteMeasure μ] {r M : ℝ} (hr : 0 ≤ r)
    (t : ℕ → ℕ) (ht : Tendsto t atTop atTop)
    (hpos : ∀ᵐ x ∂μ, 0 ≤ x)
    (hint : ∀ n : ℕ, Integrable (fun x : ℝ => x ^ n) μ)
    (c : ℕ → ℕ → ℝ)
    (hlim : ∀ n, Tendsto (fun k => c k n) atTop (𝓝 (∫ x, x ^ (t n) ∂μ)))
    (hbound : ∀ n, ∀ᶠ k in atTop, c k n ≤ M * r ^ (t n)) :
    μ (Ioi r) = 0 := by
  have tail (s : ℝ) (hrs : r < s) : μ (Ici s) = 0 := by
    have hs : 0 < s := lt_of_le_of_lt hr hrs
    have bound (n : ℕ) : μ.real (Ici s) ≤ M * (r / s) ^ (t n) := by
      have lower := setIntegral_ge_of_const_le (μ := μ) (c := s ^ (t n))
        measurableSet_Ici (measure_ne_top μ _)
        (fun x (hx : s ≤ x) => pow_le_pow_left₀ hs.le hx (t n)) (hint (t n)).integrableOn
      have positive : 0 ≤ᵐ[μ] (fun x : ℝ => x ^ (t n)) := by
        filter_upwards [hpos] with x hx using pow_nonneg hx (t n)
      have upper := (setIntegral_le_integral (s := Ici s) (hint (t n)) positive).trans
        (le_of_tendsto (hlim n) (hbound n))
      rw [div_pow, ← mul_div_assoc, le_div_iff₀ (pow_pos hs (t n))]
      simpa only [mul_comm (μ.real (Ici s))] using lower.trans upper
    have lim : Tendsto (fun n : ℕ => M * (r / s) ^ (t n)) atTop (𝓝 0) := by
      simpa using (tendsto_const_nhds (x := M)).mul
        (tendsto_pow_atTop_nhds_zero_of_lt_one (div_nonneg hr hs.le) ((div_lt_one hs).2 hrs) |>.comp ht)
    exact (measureReal_eq_zero_iff (measure_ne_top μ _)).mp
      (le_antisymm (ge_of_tendsto' lim bound) measureReal_nonneg)
  let s (n : ℕ) : ℝ := r + 1 / (n + 1 : ℝ)
  have cover : Ioi r ⊆ ⋃ n, Ici (s n) := by
    intro x hx
    obtain ⟨n, hn⟩ := exists_nat_one_div_lt (sub_pos.mpr (show r < x from hx))
    exact mem_iUnion.mpr ⟨n, show r + 1 / (n + 1 : ℝ) ≤ x by linarith⟩
  exact measure_mono_null cover (measure_iUnion_null fun n => tail (s n) (lt_add_of_pos_right r (by positivity)))

/-- A continuous spectral projection vanishing on a dense test family vanishes everywhere.
Apply this in the vacuum complement after centering observables. -/
theorem projectionVanishesOfDense
    {X Y : Type*} [TopologicalSpace X] [TopologicalSpace Y] [T1Space Y] [Zero Y]
    {D : Set X} (hD : Dense D) {P : X → Y} (hP : Continuous P)
    (test : ∀ x ∈ D, P x = 0) : ∀ x, P x = 0 :=
  hD.induction test (isClosed_singleton.preimage hP)

/-- Reconstructing a spectral projection and a dense family of test vectors suffices
to turn the scalar estimate into an operator statement. The spectral identity is explicit. -/
theorem denseProjectionOfMomentBounds
    {X Y : Type*} [TopologicalSpace X] [NormedAddCommGroup Y]
    {D : Set X} (hD : Dense D) {P : X → Y} (hP : Continuous P)
    (μ : X → Measure ℝ) (finite : ∀ v ∈ D, IsFiniteMeasure (μ v))
    {r : ℝ} (hr : 0 ≤ r) (M : X → ℝ) (c : X → ℕ → ℕ → ℝ)
    (t : X → ℕ → ℕ) (ht : ∀ v ∈ D, Tendsto (t v) atTop atTop)
    (hpos : ∀ v ∈ D, ∀ᵐ x ∂(μ v), 0 ≤ x)
    (hint : ∀ v ∈ D, ∀ n : ℕ, Integrable (fun x : ℝ => x ^ n) (μ v))
    (hlim : ∀ v ∈ D, ∀ n, Tendsto (fun k => c v k n) atTop (𝓝 (∫ x, x ^ (t v n) ∂(μ v))))
    (hbound : ∀ v ∈ D, ∀ n, ∀ᶠ k in atTop, c v k n ≤ M v * r ^ (t v n))
    (spectral : ∀ v ∈ D, (μ v).real (Ioi r) = ‖P v‖ ^ 2) : ∀ v, P v = 0 := by
  apply projectionVanishesOfDense hD hP
  intro v hv
  letI := finite v hv
  have hnull := noTransferMassAbove (μ v) hr (t v) (ht v hv) (hpos v hv) (hint v hv) (c v)
    (hlim v hv) (hbound v hv)
  have hzero := (measureReal_eq_zero_iff (measure_ne_top (μ v) (Ioi r))).2 hnull
  rw [spectral v hv] at hzero
  exact norm_eq_zero.mp (by nlinarith [norm_nonneg (P v)])

/-- The endpoint can be an atom even when every moment attains its upper bound. -/
theorem endpointAtom (r : ℝ) (n : ℕ) :
    (∫ x : ℝ, x ^ n ∂Measure.dirac r) = r ^ n ∧
      Measure.dirac r (Ici r) = 1 := by simp

/-- Integer numerators for E1's first four polynomial moments and its two Laplace
samples on energies 0,...,6. The denominators for the latter include 2^6 and 4^6. -/
def sixReadings (w : List Nat) : List Nat :=
  let sample (f : Nat → Nat) := (w.zipIdx.map fun (v, j) => v * f j).sum
  (List.range 4).map (fun d => sample (fun j => j ^ d)) ++
    [sample (fun j => 2 ^ (6 - j)), sample (fun j => 4 ^ (6 - j))]

-- BEGIN PCP OS generated finite certificate
def referenceWeights : List Nat := [0, 100, 100, 100, 100, 100, 100]
def alternativeWeights : List Nat := [1, 90, 138, 28, 173, 62, 108]

theorem indistinguishableReadings :
    sixReadings referenceWeights = [600, 2100, 9100, 44100, 6300, 136500] ∧
    sixReadings alternativeWeights = sixReadings referenceWeights ∧
    referenceWeights.head? = some 0 ∧ alternativeWeights.head? = some 1 := by decide

#print axioms decayAtRoundedTime
#print axioms noTransferMassAbove
#print axioms projectionVanishesOfDense
#print axioms denseProjectionOfMomentBounds
#print axioms endpointAtom
#print axioms indistinguishableReadings

end Millennium.YangMills.D4
