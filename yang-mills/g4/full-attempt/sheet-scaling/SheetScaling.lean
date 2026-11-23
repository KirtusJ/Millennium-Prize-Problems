import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

noncomputable section
namespace Millennium.G4.SheetScaling

lemma edge_rounding (x y a b : ℝ) :
    abs (|x - y| - |a - b|) ≤ |x - a| + |y - b| := by
  calc
    abs (|x - y| - |a - b|) ≤ |(x - y) - (a - b)| :=
      abs_abs_sub_abs_le_abs_sub _ _
    _ = |(x - a) - (y - b)| := by
      congr 1
      ring
    _ ≤ |x - a| + |y - b| := by
      simpa only [sub_eq_add_neg, abs_neg] using abs_add_le (x-a) (-(y-b))

-- NATIVE CHILD 1
theorem finite_edges {ι V : Type*} (edges : Finset ι) (u v : ι → V) (x a : V → ℝ) :
    abs ((∑ e ∈ edges, |x (u e)-x (v e)|) - (∑ e ∈ edges, |a (u e)-a (v e)|)) ≤
      ∑ e ∈ edges, (|x (u e)-a (u e)| + |x (v e)-a (v e)|) := by
  rw [← Finset.sum_sub_distrib]
  refine (Finset.abs_sum_le_sum_abs _ _).trans ?_
  exact Finset.sum_le_sum fun e _ => edge_rounding _ _ _ _

theorem tile_budget (inside boundary tiles eps err : ℝ)
    (degree : 2*inside+boundary=4*tiles)
    (bound : err ≤ inside*eps+boundary*(eps/2)) :
    err ≤ 2*tiles*eps := by
  nlinarith only [congrArg (fun t : ℝ => t*eps) degree, bound]

-- NATIVE CHILD 2
theorem signed_runs (h : ℝ) (hh : h ≠ 2) :
    1+2*((h-1)/(2-h))=h/(2-h) := by
  have he : 2-h ≠ 0 := sub_ne_zero.mpr (Ne.symm hh)
  field_simp [he]
  ring

theorem bessel_residue (v : ℝ) (h : v^2 ≠ 1) (hv : v ≠ 0) :
    ((2/v^2) / (1-1/v^2)) = 2/(v^2-1) := by
  have hs : v^2-1 ≠ 0 := sub_ne_zero.mpr h
  have hv2 : v^2 ≠ 0 := pow_ne_zero _ hv
  have ha : 1-1/v^2 ≠ 0 := by
    intro bad
    apply hs
    field_simp [hv2] at bad
    linarith
  field_simp [hv2, ha, hs]

#print axioms edge_rounding
#print axioms finite_edges
#print axioms tile_budget
#print axioms signed_runs
#print axioms bessel_residue

end Millennium.G4.SheetScaling
