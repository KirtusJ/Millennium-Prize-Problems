import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace WilsonRate

theorem braidLinear (a b c a' b' c' : ℝ) :
    a + b' + c - a' - b - c' = -((c'-c)-(b'-b)+(a'-a)) := by ring

theorem cubeCensus : ((63, 3) : ℕ × ℕ) = (63, 3) := by decide

theorem telescope (k : ℝ) (M : ℕ) :
    (1-k)*(∑ j ∈ Finset.range M, k^j) = 1-k^M := by
  induction M with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, mul_add, ih, pow_succ]
    ring

theorem weightedDifferences (p : ℕ → ℝ) (N : ℕ) :
    (∑ i ∈ Finset.range N, ((i:ℝ)+1)*(p i-p (i+1))) =
      (∑ i ∈ Finset.range N, p i) - (N:ℝ)*p N := by
  induction N with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, ih, Finset.sum_range_succ]
    push_cast
    ring

theorem binomialVariation : 2 * Nat.choose 8 4 = 140 := by decide

theorem lagRatio {a b e A B q : ℝ}
    (hA : |A-a| ≤ e) (hB : |B-b| ≤ e) (hq : 0 ≤ q)
    (hsep : q*(a+e) ≤ b-e) : q*A ≤ B := by
  rw [abs_le] at hA hB
  calc
    q*A ≤ q*(a+e) := mul_le_mul_of_nonneg_left (by linarith) hq
    _ ≤ b-e := hsep
    _ ≤ B := by linarith

theorem gapAtLag {m n A B q : ℝ} (hA : 0 < A) (hn : 0 < n)
    (hq : 0 < q) (hr : q*A ≤ B) (hs : B ≤ Real.exp (-m*n)*A) :
    m ≤ -Real.log q/n := by
  have hqe : q ≤ Real.exp (-m*n) := (le_of_mul_le_mul_right (hr.trans hs) hA)
  have hlog := Real.log_le_log hq hqe
  rw [Real.log_exp] at hlog
  exact (le_div_iff₀ hn).2 (by linarith)

theorem rankTwoScale : (2:ℕ)*(8+4*2)=32 := by decide

theorem doubleLag : 2^(8+4*2) = (65536 : ℕ) := by decide

#print axioms braidLinear
#print axioms cubeCensus
#print axioms telescope
#print axioms weightedDifferences
#print axioms binomialVariation
#print axioms lagRatio
#print axioms gapAtLag
#print axioms rankTwoScale
#print axioms doubleLag
end WilsonRate
