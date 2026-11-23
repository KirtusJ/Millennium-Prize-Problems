import Mathlib.Topology.Instances.Real.Lemmas
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Ring
open Filter Topology
namespace YangMills.Observable
theorem separatedTimeWitness {C : Nat → ℝ} {c lo hi : ℝ}
    (lim : Tendsto C atTop (𝓝 c)) (pos : 0 < lo)
    (lower : ∀ᶠ n in atTop, lo ≤ C n) (upper : ∀ᶠ n in atTop, C n ≤ hi) :
    lo ≤ c ∧ c ≤ hi ∧ 0 < c := by
  have hlo : lo ≤ c := ge_of_tendsto lim lower
  have hhi : c ≤ hi := le_of_tendsto lim upper
  exact ⟨hlo, hhi, lt_of_lt_of_le pos hlo⟩
theorem momentLowerBound {ι : Type*} (s : Finset ι) (w E : ι → ℝ) (t : ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i) :
    (∑ i ∈ s, w i) - t * (∑ i ∈ s, w i * E i) ≤
      ∑ i ∈ s, w i * Real.exp (-t * E i) := by
  rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
  apply Finset.sum_le_sum
  intro i hi
  calc
    w i - t * (w i * E i) = w i * ((-t * E i) + 1) := by ring
    _ ≤ _ := mul_le_mul_of_nonneg_left (Real.add_one_le_exp _) (hw i hi)
end YangMills.Observable
#print axioms YangMills.Observable.separatedTimeWitness
#print axioms YangMills.Observable.momentLowerBound
