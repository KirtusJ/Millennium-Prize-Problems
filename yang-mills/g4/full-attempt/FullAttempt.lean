import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

noncomputable section
open scoped BigOperators
namespace Millennium.G4.FullAttempt

lemma slab_centering (p q eps mass : ℝ) (hp : eps ≤ p + mass)
    (hq : mass ≤ q) : eps ≤ p + q := by
  linarith

/-- A common submeasure is bounded by the two errors of any decision region. -/
theorem common_mass_test {ι : Type*} (s : Finset ι) (test : ι → Bool)
    (r p q : ι → ℝ) (hrp : ∀ i ∈ s, r i ≤ p i) (hrq : ∀ i ∈ s, r i ≤ q i) :
    ∑ i ∈ s, r i ≤ ∑ i ∈ s, (if test i then p i else q i) := by
  apply Finset.sum_le_sum
  intro i hi
  split <;> first | exact hrp i hi | exact hrq i hi

/-- A physical slab bound converted into an energy bound at an independent length. -/
theorem slab_energy (s E q : ℝ) (hs : 0 < s) (h : Real.exp (-s*E) ≤ q) :
    -Real.log q / s ≤ E := by
  have hlog := Real.log_le_log (Real.exp_pos _) h
  rw [Real.log_exp] at hlog
  apply (div_le_iff₀ hs).2
  linarith [mul_comm E s]

-- NATIVE CHILD 1
/-- The form of the leakage estimate used between resolution levels.
    Both marginal budgets are explicit, so the statement also covers a nonsymmetric matrix. -/
theorem weighted_leakage {ι : Type*} [Fintype ι] (w : ι → ι → ℝ) (z : ι → ℝ)
    (η : ℝ) (hw : ∀ i j, 0 ≤ w i j) (rows : ∀ i, ∑ j, w i j ≤ η)
    (cols : ∀ j, ∑ i, w i j ≤ η) :
    ∑ i, ∑ j, w i j * (z i * z j) ≤ η * ∑ i, (z i)^2 := by
  have one (i j : ι) :
      2 * (w i j * (z i * z j)) ≤ w i j * (z i)^2 + w i j * (z j)^2 := by
    nlinarith [mul_nonneg (hw i j) (sq_nonneg (z i - z j))]
  have byRow : (∑ i, ∑ j, w i j * (z i)^2) ≤ η * ∑ i, (z i)^2 := by
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro i _
    rw [← Finset.sum_mul]
    exact mul_le_mul_of_nonneg_right (rows i) (sq_nonneg _)
  have byCol : (∑ i, ∑ j, w i j * (z j)^2) ≤ η * ∑ i, (z i)^2 := by
    rw [Finset.sum_comm, Finset.mul_sum]
    apply Finset.sum_le_sum
    intro j _
    rw [← Finset.sum_mul]
    exact mul_le_mul_of_nonneg_right (cols j) (sq_nonneg _)
  have both : 2 * (∑ i, ∑ j, w i j * (z i * z j)) ≤
      (∑ i, ∑ j, w i j * (z i)^2) + ∑ i, ∑ j, w i j * (z j)^2 := by
    simp only [Finset.mul_sum, ← Finset.sum_add_distrib]
    exact Finset.sum_le_sum fun i _ => Finset.sum_le_sum fun j _ => one i j
  linarith

/-- Lower bounds on the diagonal forms survive a relative off-diagonal loss. -/
theorem resolution_floor (diagonal leak energy mass η : ℝ)
    (hη : η ≤ 1) (hdiag : mass ≤ diagonal) (hbudget : leak ≤ η * diagonal)
    (henergy : diagonal - leak ≤ energy) : (1-η)*mass ≤ energy := by
  nlinarith [mul_nonneg (sub_nonneg.mpr hη) (sub_nonneg.mpr hdiag)]

-- NATIVE CHILD 2
def response (r x : ℝ) := (r+x)/(r-x)

/-- The vacuum channel cancels the disjoint double-plaquette channel. -/
theorem remote_cancellation (r : ℝ) (hr : 0 < r) (hr' : r < 1) :
    response r 1 + response r (r^2) = 0 := by
  have h1 : r-1 ≠ 0 := ne_of_lt (sub_neg.mpr hr')
  have h2 : 0 < r-r^2 := by nlinarith [mul_pos hr (sub_pos.mpr hr')]
  unfold response
  field_simp [h1, ne_of_gt h2]
  ring

/-- Second-order spectral kernel after eliminating an intermediate energy. -/
theorem magnetic_resolvent (r x : ℝ) (h : r ≠ x) :
    (r+x) / 4 + (r+x)^2/(4*(r-x)) = r/2 * response r x := by
  unfold response
  field_simp [sub_ne_zero.mpr h]
  ring

/-- Alias-mode covariance forces the two checkerboard readings to align. -/
theorem checkerboard_defect (w m : ℝ) (h : w + m ≠ 0) :
    1 - (w-m)/(w+m) = 2*m/(w+m) := by
  field_simp
  ring

#print axioms slab_centering
#print axioms common_mass_test
#print axioms slab_energy
#print axioms weighted_leakage
#print axioms resolution_floor
#print axioms remote_cancellation
#print axioms magnetic_resolvent
#print axioms checkerboard_defect

end Millennium.G4.FullAttempt
