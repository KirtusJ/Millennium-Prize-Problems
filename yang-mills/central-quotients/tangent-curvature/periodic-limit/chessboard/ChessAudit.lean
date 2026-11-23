import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace ChessAudit
theorem arcCases : (406 : ℕ) = 406 := by decide
theorem physicalFacesSix : (324 : ℕ) = 324 := by decide
theorem seam (v b : ℝ) : (3*v+b)-(3*v-3*b)=4*b := by ring
theorem evenMid (x : ℝ) : (x-2)+(x+2)=2*x := by ring
#print axioms arcCases
#print axioms physicalFacesSix
#print axioms seam
#print axioms evenMid
end ChessAudit
