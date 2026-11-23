import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace YangMills.TailCertificate

theorem lowEndpoint (x q : ℝ) (hx : 0 ≤ x) (hq : x ≤ q) :
    x*(x-q) ≤ 0 := mul_nonpos_of_nonneg_of_nonpos hx (sub_nonpos.mpr hq)

theorem highEndpoint (x q : ℝ) (hx : x ≤ 1) (hq : q ≤ x) :
    x*(x-q) ≤ 1-q := by
  nlinarith only [mul_nonneg (sub_nonneg.mpr hx) (sub_nonneg.mpr hq), hx]

theorem lowSquare (x q b : ℝ) (hx : x ≤ q) (hb : q ≤ b) :
    (b-q)^2-(b-x)^2 ≤ 0 := by
  nlinarith only [mul_nonneg (sub_nonneg.mpr hx) (show 0 ≤ (b-q)+(b-x) by linarith)]

theorem highSquare (x q b : ℝ) : (b-q)^2-(b-x)^2 ≤ (b-q)^2 := by
  linarith only [sq_nonneg (b-x)]

theorem cornerMoments (a w q : ℝ) :
    (a*q^2+w)-q*(a*q+w)=(1-q)*w := by ring

theorem twoPoint (q b w : ℝ) :
    (b-q)^2-(b^2-2*b*((1-w)*q+w*b)+((1-w)*q^2+w*b^2))=w*(b-q)^2 := by ring

end YangMills.TailCertificate
#print axioms YangMills.TailCertificate.lowEndpoint
#print axioms YangMills.TailCertificate.highEndpoint
#print axioms YangMills.TailCertificate.lowSquare
#print axioms YangMills.TailCertificate.highSquare
#print axioms YangMills.TailCertificate.cornerMoments
#print axioms YangMills.TailCertificate.twoPoint
