import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Tactic.Linarith

open scoped BigOperators
namespace YangMills.ExteriorTrace

def pairs : List ℝ → ℝ
  | [] => 0
  | a :: s => a*s.sum + pairs s

def triples : List ℝ → ℝ
  | [] => 0
  | a :: s => a*pairs s + triples s

theorem doubleNewton (s : List ℝ) :
    2*pairs s = s.sum^2 - (s.map (fun a => a^2)).sum := by
  induction s with
  | nil => simp [pairs]
  | cons a r ih =>
    simp only [pairs, List.sum_cons, List.map_cons]
    nlinarith only [ih]

theorem tripleNewton (s : List ℝ) :
    6*triples s = s.sum^3 - 3*s.sum*(s.map (fun a => a^2)).sum +
      2*(s.map (fun a => a^3)).sum := by
  induction s with
  | nil => simp [triples]
  | cons a r ih =>
    simp only [triples, List.sum_cons, List.map_cons]
    nlinarith only [ih, congrArg (fun x : ℝ => a*x) (doubleNewton r)]

/-- Apply to permutation products carrying their determinant signs. -/
theorem signedSquare {ι : Type*} (s : Finset ι) (w sign : ι → ℝ)
    (hs : ∀ i ∈ s, (sign i)^2=1) :
    (∑ i ∈ s, sign i*w i)^2 ≤ (s.card : ℝ)*∑ i ∈ s, (w i)^2 := by
  have h := Finset.sum_mul_sq_le_sq_mul_sq s sign w
  have ones : ∑ i ∈ s, (sign i)^2 = (s.card : ℝ) := by
    rw [Finset.sum_congr rfl hs]
    simp
  rwa [ones] at h

theorem splittingUpper {a b c hi lo next : ℝ} (ha : 0 ≤ a) (hc : 0 ≤ c)
    (hlo : 0 < lo) (hb : lo ≤ b) (x : a ≤ hi) (y : c ≤ next) :
    a*c/b^2 ≤ hi*next/lo^2 := by
  apply div_le_div_of_nonneg_right (mul_le_mul x y hc (ha.trans x)) (sq_nonneg b) |>.trans
  exact div_le_div_of_nonneg_left (mul_nonneg (ha.trans x) (hc.trans y))
    (sq_pos_of_pos hlo) (pow_le_pow_left₀ hlo.le hb 2)

theorem positiveSecond {ι : Type*} (s : Finset ι) (p w : ι → ℝ) (b : ℝ)
    (hp : ∀ i ∈ s, 0 ≤ p i) (hw : ∀ i ∈ s, 0 ≤ w i) (hb : ∀ i ∈ s, w i ≤ b) :
    ∑ i ∈ s, p i*(w i)^2 ≤ b*∑ i ∈ s, p i*w i := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  have h := mul_le_mul_of_nonneg_left (mul_le_mul_of_nonneg_right (hb i hi) (hw i hi)) (hp i hi)
  nlinarith only [h]

theorem coincidentRows {ι : Type*} [Fintype ι] (p w : ι → ℝ)
    (hp : ∀ i, 0 < p i) (hw : ∀ i, 0 ≤ w i) (nullMean : ∑ i, p i*w i = 0) :
    ∀ i, w i = 0 := by
  intro i
  have h := Finset.single_le_sum (s := Finset.univ) (f := fun j => p j*w j)
    (fun j _ => mul_nonneg (hp j).le (hw j)) (Finset.mem_univ i)
  rw [nullMean] at h
  by_contra hne
  exact (not_lt_of_ge h) (mul_pos (hp i) (lt_of_le_of_ne (hw i) (Ne.symm hne)))

end YangMills.ExteriorTrace
#print axioms YangMills.ExteriorTrace.doubleNewton
#print axioms YangMills.ExteriorTrace.tripleNewton
#print axioms YangMills.ExteriorTrace.signedSquare
#print axioms YangMills.ExteriorTrace.splittingUpper
#print axioms YangMills.ExteriorTrace.positiveSecond
#print axioms YangMills.ExteriorTrace.coincidentRows
