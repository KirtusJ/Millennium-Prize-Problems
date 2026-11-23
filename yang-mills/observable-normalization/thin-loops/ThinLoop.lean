import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
namespace YangMills.ThinLoop

/-- Haar integration by parts and 1-x² ≤ 2(1-x) give the premises. -/
theorem conditionalContraction {r h b : ℝ} (hh : 0 ≤ h) (hmax : h ≤ 6*b)
    (hr : r ≤ 1) (score : 3*r ≤ 2*h*(1-r)) :
    r ≤ 1-1/(4*b+1) := by
  have hb : 0 < 4*b+1 := by linarith
  have h := mul_le_mul_of_nonneg_right hmax (sub_nonneg.mpr hr)
  rw [le_sub_iff_add_le, ← le_sub_iff_add_le', div_le_iff₀ hb]
  linarith only [h,score]

/-- A selected edge incurs a fixed contraction and at least L/19 edges are selected. -/
theorem loopEnvelope {q d : ℝ} {k L : ℕ} (hq : 0 ≤ q) (hd : 0 ≤ d)
    (factor : q ≤ 1-d) (count : L ≤ 19*k) :
    q^k ≤ Real.exp (-((L : ℝ)/19)*d) := by
  have edge : q ≤ Real.exp (-d) := by linarith only [factor, Real.add_one_le_exp (-d)]
  have size : (L : ℝ) ≤ 19*(k : ℝ) := by exact_mod_cast count
  calc
    q^k ≤ (Real.exp (-d))^k := pow_le_pow_left₀ hq edge k
    _ = Real.exp ((k : ℝ)*(-d)) := (Real.exp_nat_mul _ _).symm
    _ ≤ _ := Real.exp_le_exp.mpr (by linarith only [mul_le_mul_of_nonneg_right size hd])

theorem varianceFloor {mean variance second eps : ℝ} (hm : |mean| ≤ 2*eps)
    (hs : 1-3*eps ≤ second) (hv : variance = second-mean^2) :
    1-3*eps-4*eps^2 ≤ variance := by
  have h := mul_self_le_mul_self (abs_nonneg mean) hm
  rw [← sq, sq_abs] at h
  linarith only [h,hs,hv]

/-- The one-step loss after physical rescaling cannot stay bounded under these premises. -/
theorem singlePlaquetteLoss {a V D b : ℝ} (ha : 0 < a) (hv : 0 < V)
    (cap : V ≤ 4) (hb : 0 ≤ b) (innovation : b ≤ 2*D) :
    b/(8*a) ≤ D/(a*V) := by
  apply (div_le_div_iff₀ (by linarith : 0 < 8*a) (mul_pos ha hv)).mpr
  have h := mul_le_mul_of_nonneg_left cap hb
  have h' : b*V ≤ 8*D := by linarith only [h,innovation]
  linarith only [mul_le_mul_of_nonneg_left h' ha.le]

end YangMills.ThinLoop
#print axioms YangMills.ThinLoop.conditionalContraction
#print axioms YangMills.ThinLoop.loopEnvelope
#print axioms YangMills.ThinLoop.varianceFloor
#print axioms YangMills.ThinLoop.singlePlaquetteLoss
