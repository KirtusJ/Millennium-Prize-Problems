import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace NavierStokes.PressureAudit

noncomputable def printed (R B : ℝ) : ℝ :=
  (B+1)*B^(1/2:ℝ)/R + R^(-(7/4:ℝ))*B^(3/4:ℝ)

noncomputable def formal (R A B : ℝ) : ℝ :=
  (B^(1/2:ℝ)+1)*(A/R+1/R^2) + R^(-(7/4:ℝ))*B^(3/4:ℝ)

/-- At unit radius and unit localized L6 norm the paper gives a constant. -/
theorem printedUnit : printed 1 1 = 3 := by norm_num [printed]

/-- At the same inputs the comparison envelope grows with dissipation. -/
theorem formalUnit (A : ℝ) :
    formal 1 A 1 = 2*A+3 := by
  simp [formal]
  ring

/-- Even with B ≤ A+1, no constant multiple of the printed unit envelope
dominates the formal one for every possible nonnegative scalar A. -/
theorem noUniformComparison (C : ℝ) (hC : 0 ≤ C) :
    ∃ A : ℝ, 0 ≤ A ∧ 1 ≤ A+1 ∧ C * printed 1 1 < formal 1 A 1 := by
  simp only [printedUnit, formalUnit]
  exact ⟨2*C, by linarith, by linarith, by linarith⟩

/-- An absorption argument may still use the full dissipation in the energy balance. -/
theorem absorb {rate diss growth flux rem : ℝ}
    (budget : rate/2 + diss ≤ growth+flux)
    (control : flux ≤ diss/2+rem) (hd : 0 ≤ diss) :
    rate ≤ 2*growth+2*rem := by linarith

end NavierStokes.PressureAudit

#print axioms NavierStokes.PressureAudit.printedUnit
#print axioms NavierStokes.PressureAudit.formalUnit
#print axioms NavierStokes.PressureAudit.noUniformComparison
#print axioms NavierStokes.PressureAudit.absorb
