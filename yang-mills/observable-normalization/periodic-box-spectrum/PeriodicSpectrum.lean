import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FieldSimp

namespace YangMills.PeriodicSpectrum

theorem meanVariance (s h n : ℝ) (hh : h ≠ 0) (hn : n ≠ 0) (scale : s^2=h^3) :
    s^2/(n*h^2)=h/n := by
  rw [scale]
  field_simp
  ring

theorem volumeDilation (l k v : ℝ) (hl : l ≠ 0) :
    l^2*k/(2*l^3) + 2*l^3*v/l^4=(k/2+2*v)/l := by
  field_simp
  ring

/-- Absorb an off-diagonal coupling into the complementary spectral gap. -/
theorem blockCost (d b x y : ℝ) : d*(2*b*x*y-d*y^2) ≤ b^2*x^2 := by
  nlinarith only [sq_nonneg (d*y-b*x)]

theorem colorAverage (x y z : ℝ) :
    (x+y+z)+(x-y-z)+(-x+y-z)+(-x-y+z)=0 := by ring

/-- Lift a first-order quasimode across a separated hard channel. -/
theorem corrector (g l b : ℝ) (sep : g-l ≠ 0) :
    l*(b/(g-l))+b-g*(b/(g-l))=0 := by
  field_simp
  ring

/-- The paired shifts cancel in the mean while producing a transverse component. -/
theorem pairedSlope (a x y : ℝ) : a*x^2+(-a)*y^2=a*(x^2-y^2) := by ring

/-- A positively weighted winding with a nontrivial phase strictly lowers a heat trace. -/
theorem windingDeficit (a phase rest : ℝ) (ha : 0 < a) (hp : phase < 1)
    (hr : 0 ≤ rest) : 0 < a*(1-phase)+rest :=
  add_pos_of_pos_of_nonneg (mul_pos ha (sub_pos.mpr hp)) hr

theorem shellAbsorption (g b r err : ℝ) (he : err ≤ g*b*r/2) :
    g*(1-b*r)+err ≤ g*(1-b*r/2) := by linarith only [he]

end YangMills.PeriodicSpectrum
#print axioms YangMills.PeriodicSpectrum.meanVariance
#print axioms YangMills.PeriodicSpectrum.volumeDilation
#print axioms YangMills.PeriodicSpectrum.blockCost
#print axioms YangMills.PeriodicSpectrum.colorAverage
#print axioms YangMills.PeriodicSpectrum.corrector
#print axioms YangMills.PeriodicSpectrum.pairedSlope
#print axioms YangMills.PeriodicSpectrum.windingDeficit
#print axioms YangMills.PeriodicSpectrum.shellAbsorption
