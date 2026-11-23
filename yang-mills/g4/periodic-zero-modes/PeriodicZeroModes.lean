import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

noncomputable section
namespace Millennium.G4.PeriodicZeroModes

/-- A filling by plaquette words bounds the length of the boundary word. -/
theorem word_length_bound {G : Type*} [Monoid G] (len : G → ℝ) (unit : len 1 = 0)
    (triangle : ∀ a b, len (a*b) ≤ len a + len b) (words : List G) :
    len words.prod ≤ (words.map len).sum := by
  induction words with
  | nil => simp [unit]
  | cons a rest ih =>
    simpa only [List.prod_cons, List.map_cons, List.sum_cons] using
      (triangle a rest.prod).trans (add_le_add_left ih _)

/-- The residual flux sheet differs from its harmonic mean by two differences. -/
theorem sheet_decomposition (u v t : ℝ) : u*v-t^2 = (u-t)*v+t*(v-t) := by ring

-- NATIVE CHILD 1
theorem transverse_gram (a b c x y z : ℝ) :
    x^2+y^2+z^2+(a*y-b*x)^2+(a*z-c*x)^2+(b*z-c*y)^2 =
      (1+a^2+b^2+c^2)*(x^2+y^2+z^2)-(a*x+b*y+c*z)^2 := by
  ring

/-- Determinant of the rank-one modification in a transverse color direction. -/
theorem transverse_det (a b c : ℝ) :
    Matrix.det !![1+b^2+c^2, -a*b, -a*c;
                  -a*b, 1+a^2+c^2, -b*c;
                  -a*c, -b*c, 1+a^2+b^2] = (1+a^2+b^2+c^2)^2 := by
  rw [Matrix.det_fin_three]
  simp
  ring

-- NATIVE CHILD 2
/-- Fourier and tree-gauge determinant factors on a four-torus. -/
theorem tree_determinant (V τ : ℝ) (hV : V ≠ 0) (ht : τ ≠ 0) :
    (V*τ)^3/(τ*V^2) = V*τ^2 := by
  field_simp
  ring

theorem coefficient_per_face (V : ℝ) (hV : V ≠ 0) :
    ((9*V-3)/2)/(6*V) = 3/4-1/(4*V) := by
  field_simp
  ring

/-- Two fixed different box volumes have a positive finite-step coefficient. -/
theorem step_sign (p q : ℝ) (hp : 0 < p) (hpq : p < q) : 0 < 1/p-1/q := by
  exact sub_pos.mpr (one_div_lt_one_div_of_lt hp hpq)

#print axioms word_length_bound
#print axioms sheet_decomposition
#print axioms transverse_gram
#print axioms transverse_det
#print axioms tree_determinant
#print axioms coefficient_per_face
#print axioms step_sign

end Millennium.G4.PeriodicZeroModes
