import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace YangMills.SupportCriterion

/-- The private chords form an identity minor in the cycle Gram bound. -/
theorem privateChords (a b t u : ℝ) :
    a^2+b^2 ≤ a^2+b^2+(a*t+b*u)^2 := by nlinarith [sq_nonneg (a*t+b*u)]

theorem gaussianFloor (m : ℝ) (hm : 0 ≤ m) (hc : m ≤ 12) :
    m+m^2/4 ≤ 48 := by
  nlinarith only [mul_nonneg (sub_nonneg.mpr hc) (show 0 ≤ 12+m by linarith)]

/-- Pointwise L²-versus-L¹ bound for a bounded conditional mean. -/
theorem conditionalSquare (u M : ℝ) (ht : |u| ≤ M) : u^2 ≤ M*|u| := by
  calc
    u^2 = |u| * |u| := by rw [← sq, sq_abs]
    _ ≤ _ := mul_le_mul_of_nonneg_right ht (abs_nonneg u)

theorem centeredPair (joint marginal mean : ℝ) :
    joint - mean*marginal = 0 ↔ joint = mean*marginal := sub_eq_zero

theorem neutralSign (s x y : ℝ) (hs : s^2=1) : (s*x)*(s*y)=x*y := by
  calc
    _=s^2*(x*y) := by ring
    _=_ := by rw [hs,one_mul]

theorem covarianceTail (near far bound t : ℝ) (hk : far ≤ bound)
    (ht : 0 ≤ t) : near+t*far ≤ near+t*bound := by
  nlinarith only [mul_nonneg ht (sub_nonneg.mpr hk)]

end YangMills.SupportCriterion
#print axioms YangMills.SupportCriterion.privateChords
#print axioms YangMills.SupportCriterion.gaussianFloor
#print axioms YangMills.SupportCriterion.conditionalSquare
#print axioms YangMills.SupportCriterion.centeredPair
#print axioms YangMills.SupportCriterion.neutralSign
#print axioms YangMills.SupportCriterion.covarianceTail
