import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace YangMills.TensorLine
open scoped RealInnerProductSpace
variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]

/-- Three cyclically related differences sum to zero and have equal lengths. -/
theorem contrastGram (u v : H) (equal : ‖v‖ = ‖u‖) (third : ‖u+v‖ = ‖u‖) :
    2*⟪u,v⟫ = -‖u‖^2 := by
  have base := norm_add_sq_real u v
  rw [third, equal] at base
  linarith

/-- The two projected differences have positive Gram determinant whenever one is nonzero. -/
theorem contrastRank (s k : ℝ) (hs : 0 < s) (off : 2*k = -s) :
    0 < s*s-k*k := by
  have h : k = -s/2 := by linarith
  rw [h]
  nlinarith [mul_pos hs hs]

/-- The two weighted polynomial inequalities used for an isolated spectral point. -/
theorem templeFactors (a b μ root variance : ℝ) :
    variance+(μ-a)*(μ-root) = variance+μ^2-(a+root)*μ+a*root ∧
    variance+(μ-b)*(μ-root) = variance+μ^2-(b+root)*μ+b*root := by
  constructor <;> ring

theorem templeUpper (a μ root variance : ℝ) (gap : 0 < μ-a)
    (moment : 0 ≤ variance + (μ-a)*(μ-root)) :
    root ≤ μ+variance/(μ-a) := by
  have h : root-μ ≤ variance/(μ-a) := (le_div_iff₀ gap).2 (by nlinarith)
  linarith

/-- A ratio of positive spectral weights gives a lower fraction after reweighting. -/
theorem fractionFromOdds (w tail d : ℝ) (hw : 0 < w) (hr : 0 ≤ tail)
    (hd : 0 ≤ d) (bound : tail ≤ d*w) : 1/(1+d) ≤ w/(w+tail) := by
  apply (div_le_div_iff₀ (by linarith : 0 < 1+d) (by linarith : 0 < w+tail)).2
  nlinarith

theorem varianceDegree : 2*6+2*25 ≤ 2*32-1 := by decide

/-- Both orientations of the four-lag filter have the same spectral crossing. -/
theorem contrastKernel (x reversed : ℝ) :
    x*(-1+x*(13/3+x*(-13/3+x)))+reversed*(1+x*(-13/3+x*(13/3-x))) =
      (x-reversed)*(1-x)*(3-x)*(x-1/3) := by ring

end YangMills.TensorLine
#print axioms YangMills.TensorLine.contrastGram
#print axioms YangMills.TensorLine.contrastRank
#print axioms YangMills.TensorLine.templeFactors
#print axioms YangMills.TensorLine.templeUpper
#print axioms YangMills.TensorLine.fractionFromOdds
#print axioms YangMills.TensorLine.varianceDegree
#print axioms YangMills.TensorLine.contrastKernel
