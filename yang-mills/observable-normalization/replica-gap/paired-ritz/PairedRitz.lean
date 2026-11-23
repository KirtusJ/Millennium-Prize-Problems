import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

namespace YangMills.PairedRitz

/-- A scalar Schur test majorizes the Rayleigh quotient on the split trial space. -/
theorem blockCap (a b t c y w : ℝ) (hy : y < t)
    (hg : w^2 ≤ (t-c)*(t-y)) :
    c*a^2+2*w*a*b+y*b^2 ≤ t*(a^2+b^2) := by
  have h := mul_le_mul_of_nonneg_right hg (sq_nonneg a)
  by_contra hn
  have hp := mul_pos (sub_pos.mpr hy) (sub_pos.mpr (lt_of_not_ge hn))
  nlinarith [sq_nonneg ((t-y)*b-w*a)]

theorem rankTwo (s : ℝ) :
    (s-1)*3-(s+1)=2*(s-2) := by ring

theorem thermalExampleSchur :
    (1/64:ℝ)^2 ≤ (669/2000-(1/3+1/16000+1/4096))*(669/2000-1/64) := by norm_num

theorem ratioEnclosure :
    (333/1000:ℝ) ≤ 1/3-1/4096 ∧
    (669/2000)/(1-1/4096) ≤ 335/1000 := by constructor <;> norm_num

end YangMills.PairedRitz
#print axioms YangMills.PairedRitz.blockCap
#print axioms YangMills.PairedRitz.rankTwo
#print axioms YangMills.PairedRitz.thermalExampleSchur
#print axioms YangMills.PairedRitz.ratioEnclosure
