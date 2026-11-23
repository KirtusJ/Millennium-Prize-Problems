import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith

namespace Millennium.G4.SparseCoarse
open scoped BigOperators

theorem variance_comparison (v v' j j' m M g : ℝ)
    (hg : 0 ≤ g) (hv : m*v ≤ v') (hj : j' ≤ M*j) (hclear : g*v' ≤ j') :
    g*(m*v) ≤ M*j := (mul_le_mul_of_nonneg_left hv hg).trans (hclear.trans hj)

theorem cap_room (big small excluded : ℝ) (h : excluded ≤ 4*small)
    (hbig : 4*small < big) : 0 < big-excluded := by linarith

-- NATIVE CHILD 1
theorem many_faces (hits : Fin 13 → ℕ) (r : ℕ)
    (h : 13*r ≤ ∑ i, hits i) : ∃ i, r ≤ hits i := by
  by_contra! hsmall
  have hs : ∑ i, hits i < ∑ _ : Fin 13, r :=
    Finset.sum_lt_sum_of_nonempty Finset.univ_nonempty fun i _ => hsmall i
  simp at hs
  omega

theorem geometric_tail (q : ℝ) (r : ℕ) (hq : 0 ≤ q) (hh : q ≤ 1/2) :
    13*q^r ≤ 13*(1/2:ℝ)^r := by
  exact mul_le_mul_of_nonneg_left (pow_le_pow_left₀ hq hh r) (by norm_num)

-- NATIVE CHILD 2
theorem per_link_oscillation (upper lower b dist : ℝ)
    (hi : upper ≤ 6*b*dist) (lo : -(6*b*dist) ≤ lower) :
    upper-lower ≤ 12*b*dist := by linarith

#print axioms variance_comparison
#print axioms cap_room
#print axioms many_faces
#print axioms geometric_tail
#print axioms per_link_oscillation
end Millennium.G4.SparseCoarse
