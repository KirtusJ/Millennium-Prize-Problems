import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

namespace YangMills.CornerSpectrum

/-- Moments of four additions/removals, with plaquette amplitude one fourth. -/
noncomputable def evenMoment : ℕ → ℝ
  | 0 => 1
  | n+1 => ((2*(n:ℝ)+1)/4) * evenMoment n

theorem momentsDetermined (m : ℕ → ℝ) (h0 : m 0=1)
    (h : ∀ n : ℕ, m (n+1)=((2*(n:ℝ)+1)/4)*m n) :
    ∀ n, m n=evenMoment n := by
  intro n
  induction n with
  | zero => exact h0
  | succ n ih => rw [h, ih, evenMoment]

theorem secondFourth : evenMoment 1 = 1/4 ∧ evenMoment 2 = 3/16 := by
  norm_num [evenMoment]

theorem twoStepWalks :
    ((4:ℝ)^2+6*2^2+8)/4^4 = 3/16 := by norm_num
/-- D applied to a power of W on the empty state, using [D,W]=4I. -/
theorem lowerPowers {V : Type*} [AddCommMonoid V] (W D : V →+ V) (v : ℕ → V)
    (step : ∀ n, D (v (n+1)) = W (D (v n)) + 4 • v n)
    (zero : D (v 0) = 0) (powers : ∀ n, W (v n) = v (n+1)) :
    ∀ n : ℕ, D (v (n+1)) = (n+1) • (4 • v n) := by
  intro n
  induction n with
  | zero => simp [step, zero]
  | succ n ih =>
    rw [step, ih, map_nsmul, map_nsmul, powers]
    exact (succ_nsmul _ _).symm

/-- Evaluation in the empty state converts the ladder identity into
the unscaled Gaussian moment recurrence. -/
theorem returnRecurrence {V : Type*} [AddCommMonoid V] (W D : V →+ V)
    (v : ℕ → V) (read : V →+ ℝ)
    (step : ∀ n, D (v (n+1)) = W (D (v n)) + 4 • v n)
    (zero : D (v 0) = 0) (powers : ∀ n, W (v n) = v (n+1))
    (empty : ∀ x, read (W x) = read (D x)) (n : ℕ) :
    read (v (n+2)) = 4*((n:ℝ)+1)*read (v n) := by
  rw [← powers (n+1), empty, lowerPowers W D v step zero powers n,
      map_nsmul, map_nsmul]
  simp only [nsmul_eq_mul, Nat.cast_add, Nat.cast_one, Nat.cast_ofNat]
  ring

/-- A bound on the support of a positive measure bounds its moment ratio. -/
theorem supportRatio (v M s h : ℝ) (hv : 0 < v)
    (hs : M = s*v) (hb : M ≤ h^2*v) : s ≤ h^2 := by
  exact (le_of_mul_le_mul_right (hs ▸ hb) hv)

end YangMills.CornerSpectrum
#print axioms YangMills.CornerSpectrum.momentsDetermined
#print axioms YangMills.CornerSpectrum.secondFourth
#print axioms YangMills.CornerSpectrum.twoStepWalks
#print axioms YangMills.CornerSpectrum.supportRatio
#print axioms YangMills.CornerSpectrum.lowerPowers
#print axioms YangMills.CornerSpectrum.returnRecurrence
