import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace MovingThreshold

theorem excess (k d : ℝ) : (k+d)^2-k^2 = d*(2*k+d) := by ring

theorem fiberWidth {x d z lo : ℝ} (hz : z^2=x) (hl : lo^2=x-d)
    (hn : 0≤lo) (ho : lo≤z) : (z-lo)*z ≤ d := by
  nlinarith [mul_nonneg (sub_nonneg.mpr ho) hn]

theorem sparseFiber {inside outside fraction η : ℝ}
    (hi : inside ≤ fraction) (ho : outside ≤ η/2)
    (ht : η ≤ inside+outside) : η/2 ≤ fraction := by linarith

theorem conditionalConstant :
    (40:ℕ)^2*81 < 160^2*6 ∧ 160^2*6 ≤ 48^2*81 := by decide

theorem mixedMass {a b m : ℝ} (h : m ≤ a+b) : m/2 ≤ a ∨ m/2 ≤ b := by
  by_contra! hn
  linarith

theorem spinWeight {z : ℝ} (h : z^2 ≤ 1/4) : 9/16 ≤ (1-z^2)^2 := by
  nlinarith [sq_nonneg (1/4-z^2)]

theorem fejerFour (x : ℝ) :
    (x*(2*x-1)^2)^2 = x^2-8*x^3+24*x^4-32*x^5+16*x^6 := by ring

theorem fourClockNorm : (1+8+24+32+16 : ℕ) = 81 := by decide

theorem harmonicFive :
    (56:ℤ)*2^5-28*4^5+8*6^5-8^5 = 2560 := by decide

theorem movingMean : (2/3:ℚ)*(1/12)/(20/240)*4 = 8/3 := by norm_num

#print axioms excess
#print axioms fiberWidth
#print axioms sparseFiber
#print axioms conditionalConstant
#print axioms mixedMass
#print axioms spinWeight
#print axioms fejerFour
#print axioms fourClockNorm
#print axioms harmonicFive
#print axioms movingMean
end MovingThreshold
