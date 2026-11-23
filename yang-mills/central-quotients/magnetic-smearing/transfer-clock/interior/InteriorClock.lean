import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace InteriorClock

theorem twoLegs (E z s t : ℝ) :
    s*((E+z)/2)^2+t*((E-z)/2)^2 =
    (s+t)*(E^2+z^2)/4+(s-t)*E*z/2 := by ring

theorem centeredWindowWidth (E d : ℝ) :
    (E+d)^2-(E-d)^2 = 4*E*d := by ring

theorem geometricRatio (u v : ℝ) (hu : 0 < u) :
    (u-1/2)^2+v^2 < (u+1/2)^2+v^2 := by linarith

theorem windowExample : (5 : ℕ)*20 = 100 := by decide

open MeasureTheory in
theorem finiteWindowTrace {X ι : Type*} [MeasurableSpace X] (μ : Measure X)
    (s : Finset ι) (a : ι → ℝ) (h : ι → X → ℝ)
    (hi : ∀ i ∈ s, Integrable (fun x => (h i x)^2) μ)
    (hf : Integrable (fun x => (∑ i ∈ s, a i * h i x)^2) μ) :
    (∫ x, (∑ i ∈ s, a i * h i x)^2 ∂μ) ≤
      (∑ i ∈ s, (a i)^2) * ∑ i ∈ s, ∫ x, (h i x)^2 ∂μ := by
  have ht : Integrable (fun x => ∑ i ∈ s, (h i x)^2) μ :=
    integrable_finset_sum s hi
  calc
    _ ≤ ∫ x, (∑ i ∈ s, (a i)^2) * ∑ i ∈ s, (h i x)^2 ∂μ :=
      integral_mono hf (ht.const_mul _) (fun x =>
        Finset.sum_mul_sq_le_sq_mul_sq s a (fun i => h i x))
    _ = _ := by rw [integral_const_mul, integral_finset_sum s hi]

theorem shiftedFour (x : ℝ) :
    let y := 2*x-1
    4+3*y-2*(2*y^2-1)-2*(4*y^3-3*y) = 1-14*x+80*x^2-64*x^3 := by
  dsimp
  ring

theorem shiftedSquare (x : ℝ) :
    (1-14*x+80*x^2-64*x^3)^2 =
    1-28*x+356*x^2-2368*x^3+8192*x^4-10240*x^5+4096*x^6 := by ring

theorem shiftedNorm : (1+28+356+2368+8192+10240+4096 : ℕ) = 25281 := by decide

theorem independentProduct (a b x y : ℝ) :
    (a+b)*(x+y)=a*x+a*y+b*x+b*y := by ring

theorem harmonicSeven :
    (8:ℤ)^7-8*6^7+28*4^7-56*2^7 = 309248 := by decide

theorem shiftedMeanSquare :
    (4:ℚ)*(1/12)/(151/630)=210/151 := by norm_num

#print axioms twoLegs
#print axioms centeredWindowWidth
#print axioms geometricRatio
#print axioms windowExample
#print axioms finiteWindowTrace
#print axioms shiftedFour
#print axioms shiftedSquare
#print axioms shiftedNorm
#print axioms independentProduct
#print axioms harmonicSeven
#print axioms shiftedMeanSquare
end InteriorClock
