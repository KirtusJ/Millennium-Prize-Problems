import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Tactic.Linarith

open scoped BigOperators
namespace YangMills.Staggered

/-- Move a nearest-neighbor pair of faces from a link sum onto the test
function. The permutation can be a shift on any finite periodic lattice. -/
theorem moveShift {α : Type*} [Fintype α] (e : α ≃ α) (w f : α → ℝ) :
    (∑ x, w x*(f x+f (e.symm x))) = ∑ x, (w x+w (e x))*f x := by
  simp_rw [mul_add, add_mul]
  rw [Finset.sum_add_distrib, Finset.sum_add_distrib]
  congr 1
  simpa using (Equiv.sum_comp e.symm (fun y => w (e y)*f y))

theorem alternatingFace {α : Type*} [Fintype α] (e : α ≃ α) (χ ψ f : α → ℝ)
    (flip : ∀ x, χ (e x) = -χ x) :
    (∑ x, χ x*ψ x*(f x+f (e.symm x))) = ∑ x, χ x*(ψ x-ψ (e x))*f x := by
  rw [moveShift e (fun x => χ x*ψ x) f]
  apply Finset.sum_congr rfl
  intro x _
  rw [flip]
  ring

theorem uniformZero {α : Type*} [Fintype α] (e : α ≃ α) (χ f : α → ℝ)
    (flip : ∀ x, χ (e x) = -χ x) : (∑ x, χ x*(f x+f (e.symm x)))=0 := by
  simpa using alternatingFace e χ (fun _ => 1) f flip

theorem secondStencil (x j k : ℝ) :
    x^2-(x+j)^2-(x-k)^2+(x+j-k)^2=-2*j*k := by ring

theorem mixedStencil (x y j k l m : ℝ) :
    x*y-(x+j)*(y+l)-(x-k)*(y-m)+(x+j-k)*(y+l-m)=-(j*m+k*l) := by ring

theorem coefficient (v : ℝ) : (-1/2:ℝ)*((-2)*v/1536)=v/1536 := by ring

theorem compensateReciprocal {β S : ℝ} (hβ : β ≠ 0) (h : 6*β-S ≠ 0) :
    β^3*(-3/(4*(6*β-S))+1/(8*β)+S/(48*β^2))+S^2/288 =
    -S^3/(288*(6*β-S)) := by field_simp; ring

end YangMills.Staggered
#print axioms YangMills.Staggered.moveShift
#print axioms YangMills.Staggered.alternatingFace
#print axioms YangMills.Staggered.uniformZero
#print axioms YangMills.Staggered.secondStencil
#print axioms YangMills.Staggered.mixedStencil
#print axioms YangMills.Staggered.coefficient
#print axioms YangMills.Staggered.compensateReciprocal
