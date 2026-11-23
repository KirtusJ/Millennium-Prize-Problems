import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

namespace SlabReview
theorem ringSums : (14096 : Nat) = 10^4 + 8^4 ∧ (5904 : Nat) = 10^4 - 8^4 := by decide
theorem denominator : (256 : Nat)*9^4 < 625*8^4 ∧ 369*8^4 < 256*9^4 := by decide
theorem liftedEdges : 8*3*(4^3+6^3+8^3) = (19008 : Nat) := by decide
theorem lostSeams : 4*3*(4^2+6^2+8^2) = (1392 : Nat) := by decide
theorem interpolation : (480 : Nat)*5 = 3*800 := by decide
theorem interpolationSquare (x g : ℝ) : (1+x^2)*(1-4*x*g+2*(1+x^2)*g^2) - (1-x^2) = 2*((1+x^2)*g-x)^2 := by ring
theorem windowMass {low central high : ℝ} (a : low ≤ 1/512) (b : high ≤ 71/12800) (c : 3/200 ≤ low+central+high) : 3/400 ≤ central := by linarith
theorem endpointRatio : (1-(12729:ℚ)/12871)/(1+12729/12871) = 71/12800 := by norm_num
#print axioms interpolationSquare
#print axioms windowMass
#print axioms endpointRatio
#print axioms ringSums
#print axioms denominator
#print axioms liftedEdges
#print axioms lostSeams
#print axioms interpolation
end SlabReview
