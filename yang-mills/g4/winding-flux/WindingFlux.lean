import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

open MeasureTheory
open scoped BigOperators

namespace Millennium.G4.WindingFlux

/-- A walk records the additive sum of its edge labels. -/
inductive LabeledWalk {V A : Type*} [AddGroup A] (edge : V → V → Prop) (w : V → V → A) :
    V → V → A → Prop where
  | nil (x : V) : LabeledWalk edge w x x 0
  | snoc {x y z : V} {a : A} (path : LabeledWalk edge w x y a) (step : edge y z) :
      LabeledWalk edge w x z (a + w y z)

theorem join_walks {V A : Type*} [AddGroup A] {edge : V → V → Prop} {w : V → V → A}
    {x y z : V} {a b : A} (left : LabeledWalk edge w x y a)
    (right : LabeledWalk edge w y z b) : LabeledWalk edge w x z (a+b) := by
  induction right with
  | nil => simpa using left
  | snoc path step ih =>
    simpa only [add_assoc] using LabeledWalk.snoc ih step

/-- On an occupied component with return paths, zero holonomy on closed walks
produces a vertex potential. For binary labels this is the gauge sign change. -/
theorem component_potential {V A : Type*} [AddGroup A] (edge : V → V → Prop)
    (w : V → V → A) (root : V)
    (reach : ∀ y, ∃ a, LabeledWalk edge w root y a)
    (back : ∀ y, ∃ a, LabeledWalk edge w y root a)
    (flat : ∀ a, LabeledWalk edge w root root a → a = 0) :
    ∃ s : V → A, ∀ x y, edge x y → s y = s x + w x y := by
  choose s hs using reach
  refine ⟨s, ?_⟩
  intro x y hxy
  obtain ⟨a, ha⟩ := back y
  exact add_right_cancel ((flat _ (join_walks (hs y) ha)).trans
    (flat _ (join_walks (LabeledWalk.snoc (hs x) hxy) ha)).symm)

/-- A translation that reverses the character and preserves the integrated
bond weight kills that subgraph's Fourier coefficient. -/
theorem character_cancellation {I : Type*} [Fintype I] (s : I ≃ I)
    (chi weight : I → ℝ) (flip : ∀ i, chi (s i) = -chi i)
    (inv : ∀ i, weight (s i) = weight i) :
    ∑ i, chi i * weight i = 0 := by
  have h := s.sum_comp (fun i => chi i * weight i)
  simp only [flip, inv, neg_mul, Finset.sum_neg_distrib] at h
  linarith

/-- After cancellation, absolute projected weight is bounded by unprojected
weight on the surviving bond graphs. -/
theorem supported_bond_sum {I : Type*} [Fintype I] (survives : I → Prop)
    [DecidablePred survives] (signed weight : I → ℝ)
    (kill : ∀ i, ¬survives i → signed i = 0)
    (bound : ∀ i, |signed i| ≤ weight i) :
    |∑ i, signed i| ≤ ∑ i, (if survives i then weight i else 0) := by
  apply (Finset.abs_sum_le_sum_abs _ _).trans
  apply Finset.sum_le_sum
  intro i _
  by_cases hi : survives i
  · simpa [hi] using bound i
  · simp [hi, kill i hi]

/-- A mixture of conditional occupation laws obeys their common upper bound. -/
theorem conditional_domination {X : Type*} [MeasurableSpace X] (μ : Measure X)
    (event total : X → ℝ) (p : ℝ) (he : Integrable event μ) (ht : Integrable total μ)
    (h : ∀ x, event x ≤ p * total x) :
    (∫ x, event x ∂μ) ≤ p * ∫ x, total x ∂μ := by
  rw [← integral_const_mul]
  exact integral_mono he (ht.const_mul p) h

-- NATIVE CHILD 1
/-- The charged directions and their parallel cuts use disjoint edge sets. -/
theorem required_length {I : Type*} [Fintype I] (active : Finset I) (steps : I → ℕ)
    (side : ℕ) (lower : ∀ i ∈ active, side ≤ steps i) :
    active.card * side ≤ ∑ i ∈ active, steps i := by
  simpa using Finset.sum_le_sum lower

/-- The positive spatial factors and vacuum normalization preserve a pointwise
comparison of the projected and neutral kernels. -/
theorem magnetic_sandwich (a b c k z : ℝ) (ha : 0 ≤ a) (hb : 0 ≤ b)
    (hz : 0 < z) (h : |k| ≤ c) :
    |a*k*b/z| ≤ a*c*b/z := by
  rw [abs_div, abs_mul, abs_mul, abs_of_nonneg ha, abs_of_nonneg hb, abs_of_pos hz]
  exact div_le_div_of_nonneg_right
    (mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left h ha) hb) hz.le

-- NATIVE CHILD 2
lemma sector_ratio (z n p : ℝ) (hz : 0 < z) (h : |n| ≤ z * p) :
    |n| / z ≤ p := by
  apply (div_le_iff₀ hz).2
  simpa only [mul_comm z p] using h

theorem side_four_two_flux :
    4^2 * Nat.choose 8 4 + 4^4 - 4^3 = 1312 := by decide

#print axioms join_walks
#print axioms component_potential
#print axioms character_cancellation
#print axioms supported_bond_sum
#print axioms conditional_domination
#print axioms required_length
#print axioms magnetic_sandwich
#print axioms sector_ratio
#print axioms side_four_two_flux

end Millennium.G4.WindingFlux
