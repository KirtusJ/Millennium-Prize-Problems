import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace SpectralAudit
theorem clockCases : (630 : ℕ) = 630 := by decide
theorem signCases : (288 : ℕ) = 288 := by decide
theorem parityDefect (p n s : ℝ) : (p+n)*s-(p-n)*s=2*n*s := by ring
theorem kernelAtom (z e : ℝ) : z*0+e*1=e := by ring
#print axioms clockCases
#print axioms signCases
#print axioms parityDefect
#print axioms kernelAtom
end SpectralAudit
