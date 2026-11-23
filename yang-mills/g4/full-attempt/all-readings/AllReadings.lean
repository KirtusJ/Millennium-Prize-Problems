import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

noncomputable section
namespace Millennium.G4.AllReadings

theorem normalized_channel (u r z s : ℝ) (n : ℕ) (hz : z < 1)
    (hs : (u - r) * s = u^n - r^n) :
    (u - z*r) * s / (1-z) = (u^n-r^n)/(1-z) + r*s := by
  have hd : 1-z ≠ 0 := ne_of_gt (sub_pos.mpr hz)
  field_simp [hd]
  nlinarith only [hs]

lemma split_budget (x y : ℝ) (hx₀ : 0 ≤ x) (hx₁ : x ≤ 1)
    (hy₀ : 0 ≤ y) (hy₁ : y ≤ 1) :
    y ^ 2 * (1 - x) + x ^ 2 * (1 - y) ≤ 1 - x * y := by
  have hx' : 0 ≤ 1 - x := sub_nonneg.mpr hx₁
  have hy' : 0 ≤ 1 - y := sub_nonneg.mpr hy₁
  have hx_sq : x ^ 2 ≤ x := by
    nlinarith only [mul_nonneg hx₀ hx']
  have hy_sq : y ^ 2 ≤ y := by
    nlinarith only [mul_nonneg hy₀ hy']
  calc
    y ^ 2 * (1 - x) + x ^ 2 * (1 - y) ≤
        y * (1 - x) + x * (1 - y) :=
      add_le_add (mul_le_mul_of_nonneg_right hy_sq hx')
        (mul_le_mul_of_nonneg_right hx_sq hy')
    _ ≤ 1 - x * y := by
      nlinarith only [mul_nonneg hx' hy']

-- NATIVE CHILD 1
def spectatorMass : List ℝ → ℝ
  | [] => 0
  | x :: xs => xs.prod^2 * (1-x) + x^2 * spectatorMass xs

theorem product_interval (xs : List ℝ) (h : ∀ x ∈ xs, 0 ≤ x ∧ x ≤ 1) :
    0 ≤ xs.prod ∧ xs.prod ≤ 1 := by
  induction xs with
  | nil => simp
  | cons x xs ih =>
    have hx := h x (List.mem_cons_self ..)
    have ht := ih (fun y hy => h y (List.mem_cons_of_mem _ hy))
    rw [List.prod_cons]
    exact ⟨mul_nonneg hx.1 ht.1, (mul_le_mul_of_nonneg_left ht.2 hx.1).trans (by simpa using hx.2)⟩

theorem spectator_budget (xs : List ℝ) (h : ∀ x ∈ xs, 0 ≤ x ∧ x ≤ 1) :
    spectatorMass xs ≤ 1-xs.prod := by
  induction xs with
  | nil => simp [spectatorMass]
  | cons x xs ih =>
    have hx := h x (List.mem_cons_self ..)
    have htail : ∀ y ∈ xs, 0 ≤ y ∧ y ≤ 1 := fun y hy => h y (List.mem_cons_of_mem _ hy)
    have ht := product_interval xs htail
    rw [spectatorMass, List.prod_cons]
    calc
      _ ≤ xs.prod^2 * (1-x) + x^2 * (1-xs.prod) :=
        add_le_add_left (mul_le_mul_of_nonneg_left (ih htail) (sq_nonneg x)) _
      _ ≤ _ := split_budget x xs.prod hx.1 hx.2 ht.1 ht.2

-- NATIVE CHILD 2
theorem snapped_area (l a f : ℝ) (hl : 0 < l) (h : l^3*a ≤ l*f) :
    l^2*a ≤ f := by
  apply (le_of_mul_le_mul_left _ hl)
  calc
    l*(l^2*a) = l^3*a := by ring
    _ ≤ l*f := h

theorem peel_level (v z rest : ℝ) (hz : z < 1) (h : v = z*(v+rest)) :
    v = z/(1-z)*rest := by
  have hd : 1-z ≠ 0 := ne_of_gt (sub_pos.mpr hz)
  field_simp [hd]
  nlinarith only [h]

theorem fine_completion (a b c f h : ℝ) (hc : c ≠ 0) :
    a*f^2 + 2*b*f*h + c*h^2 = (a-b^2/c)*f^2 + c*(h+b*f/c)^2 := by
  field_simp [hc]
  ring

#print axioms normalized_channel
#print axioms split_budget
#print axioms product_interval
#print axioms spectator_budget
#print axioms snapped_area
#print axioms peel_level
#print axioms fine_completion

end Millennium.G4.AllReadings
