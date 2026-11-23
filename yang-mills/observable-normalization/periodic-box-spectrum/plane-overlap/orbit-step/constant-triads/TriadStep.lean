import Mathlib.Data.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
namespace YangMills.TriadStep

theorem isotropicTrace (w x y z : ℝ) (norm : w^2+x^2+y^2+z^2=1) :
    (w^2+x^2-y^2-z^2)+(w^2-x^2+y^2-z^2)+(w^2-x^2-y^2+z^2)=4*w^2-1 := by
  linarith

theorem tracelessMean (s : ℝ) (h : s=1/4) : 4*s-1=0 := by linarith

theorem thirdMoment :
    64*(5/64 : ℝ)-48*(1/8 : ℝ)+12*(1/4 : ℝ)-1=1 := by norm_num

theorem signedLogCubic (c2 c3 : ℝ) :
    (c2+c3/6)-(c2-c3/6)=c3/3 := by ring

theorem signedMaximum (x y z : ℝ) :
    (x+y+z)-(x+y-z)=2*z := by ring

end YangMills.TriadStep
#print axioms YangMills.TriadStep.isotropicTrace
#print axioms YangMills.TriadStep.tracelessMean
#print axioms YangMills.TriadStep.thirdMoment
#print axioms YangMills.TriadStep.signedLogCubic
#print axioms YangMills.TriadStep.signedMaximum
