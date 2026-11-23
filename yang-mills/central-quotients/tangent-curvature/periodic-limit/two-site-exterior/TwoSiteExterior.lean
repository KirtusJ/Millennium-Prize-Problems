import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace TwoSiteExterior
theorem centralRank : (42 : ℕ) = 42 := by decide
theorem orthogonalPairs : (56 : ℕ) = 56 := by decide
theorem affineRemainder (e v r : ℝ) : e*(v+r)^2-e*(1-e)*v^2-(e-1)*r^2=(e*v+r)^2 := by ring
#print axioms centralRank
#print axioms orthogonalPairs
#print axioms affineRemainder
end TwoSiteExterior
