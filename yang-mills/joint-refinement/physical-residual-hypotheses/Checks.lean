import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith

namespace Millennium.G4.PhysicalResidual

theorem endpoint_loss {b d lam w eta : ℝ}
    (hb : b ≤ d + lam*w) (hq : lam*w ≤ eta*d) :
    b ≤ (1+eta)*d := by nlinarith

theorem inherited_step {alpha prev b eta d : ℝ}
    (h : alpha*prev ≤ b) (hr : b ≤ (1+eta)*d) (he : 0 ≤ eta) :
    alpha*prev/(1+eta) ≤ d := by
  apply (div_le_iff₀ (by linarith : 0 < 1+eta)).2
  nlinarith

-- NATIVE CHILD 1
theorem late_step {b d loss lam w : ℝ}
    (hb : b ≤ d+lam*w) (hc : lam*w ≤ loss) : b-loss ≤ d := by linarith

theorem clipped_lower {x y h : ℝ} (hy : y ≤ h) (hx : y ≤ x) :
    y ≤ min h x := le_min hy hx

-- NATIVE CHILD 2
theorem critical_equality {lam w d b eta : ℝ}
    (hb : b=d+lam*w) (he : eta*d=lam*w) :
    b=(1+eta)*d := by nlinarith

#print axioms endpoint_loss
#print axioms inherited_step
#print axioms late_step
#print axioms clipped_lower
#print axioms critical_equality
end Millennium.G4.PhysicalResidual
