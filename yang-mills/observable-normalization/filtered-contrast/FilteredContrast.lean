import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace YangMills.FilteredContrast

theorem orientationDifference (a x y : ℝ) :
    (3+2*x)*(1-x)*(a-y)-(3+2*y)*(1-y)*(a-x) =
    (x-y)*(3-a-2*a*(x+y)+2*x*y) := by ring

theorem cubicAverage : ((3-1)/(35*108) : ℝ) = 1/1890 := by norm_num

theorem quarticShape (x y z : ℝ) :
    (x^2+y^2+z^2)*(x^2-y^2)-9*(x^4-y^4) =
    -8*x^4+8*y^4+x^2*z^2-y^2*z^2 := by ring

theorem quarticAverage :
    (3*(128*105-128*9+2*9-2*3-32*15+32*3)/(11*945*2*3*216^2) : ℝ)
    = 331/26943840 := by norm_num

end YangMills.FilteredContrast
#print axioms YangMills.FilteredContrast.orientationDifference
#print axioms YangMills.FilteredContrast.cubicAverage
#print axioms YangMills.FilteredContrast.quarticShape
#print axioms YangMills.FilteredContrast.quarticAverage
