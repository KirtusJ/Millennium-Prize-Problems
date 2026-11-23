import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic
namespace CurvedWall
theorem edge (v u l : ℝ) : (2*v-l*u)^2+4*v*u=4*v^2+4*v*u*(1-l)+l^2*u^2 := by ring
theorem potential (z b u : ℝ) : 2*(z-b*u)^2*u-2*z^2*u= -4*z*b*u^2+2*b^2*u^3 := by ring
theorem correction (l : ℝ) : 1/4+1/4-1+l-3*l= -1/2-2*l := by ring
#print axioms edge
#print axioms potential
#print axioms correction
end CurvedWall
