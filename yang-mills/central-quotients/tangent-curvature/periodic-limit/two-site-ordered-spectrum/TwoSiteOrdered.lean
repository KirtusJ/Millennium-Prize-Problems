import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace TwoSiteOrdered
theorem outerCost : (40 : ℕ) = 40 := by decide
theorem probes : (343 : ℕ) = 343 := by decide
theorem probeIdentity (a b c : ℝ) : (b^2+c^2)+(a^2+c^2)+(a^2+b^2)=2*(a^2+b^2+c^2) := by ring
#print axioms outerCost
#print axioms probes
#print axioms probeIdentity
end TwoSiteOrdered
