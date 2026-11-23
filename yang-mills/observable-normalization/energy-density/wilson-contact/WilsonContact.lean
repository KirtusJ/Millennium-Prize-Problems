import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Tactic.Linarith

open Real Set MeasureTheory

namespace YangMills.WilsonContact

/-- Centering an exterior estimate does not change its conditional innovation. -/
theorem projectionLoss {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    (v p : H) (orthogonal : @inner ℝ H _ (v-p) p = 0) :
    ‖v‖^2 = ‖p‖^2 + ‖v-p‖^2 := by
  have h := norm_add_sq_real (v-p) p
  rw [orthogonal, sub_add_cancel] at h
  linarith

theorem separation {x y z b : ℝ} (removed : b ≤ x-y) (separated : |z| ≤ y) :
    b ≤ x-|z| := by linarith

/-- A scaling of 1+R sends the polar coordinate to a gamma limit. -/
theorem polarScaling {R z : ℝ} (h : 0 ≤ R) :
    let y := (1+R)*(1-z)
    1-z^2=y*(2-y/(1+R))/(1+R) := by
  dsimp
  have hn : 1+R ≠ 0 := by linarith
  field_simp
  ring

theorem gammaVariance : (15/4:ℝ)-(3/2)^2=3/2 := by norm_num

private theorem momentExpansion {ι : Type*} (S : Finset ι) (w x : ι → ℝ) (c : ℝ) :
    ∑ i ∈ S, w i*(x i-c)^2 =
      (∑ i ∈ S, w i*(x i)^2)-(∑ i ∈ S, w i*x i)*(2*c)+(∑ i ∈ S, w i)*c^2 := by
  simp only [Finset.sum_mul, ← Finset.sum_sub_distrib, ← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i _
  ring

theorem conditionalFiberLoss {ι : Type*} (S : Finset ι) (w x : ι → ℝ)
    (normalized : ∑ i ∈ S, w i=1) (c : ℝ) :
    let m := ∑ i ∈ S, w i*x i
    (∑ i ∈ S, w i*(x i-c)^2)=(m-c)^2+∑ i ∈ S, w i*(x i-m)^2 := by
  dsimp only
  rw [momentExpansion, momentExpansion, normalized]
  ring

/-- Integrating the derivative of the Gibbs density times a score power
around a closed link orbit. Both endpoint values are explicitly matched. -/
theorem orbitIBP (S d d₂ : ℝ → ℝ) (P : ℝ) (k : ℕ)
    (h₁ : ∀ x, HasDerivAt S (d x) x) (h₂ : ∀ x, HasDerivAt d (d₂ x) x)
    (hc : Continuous d₂) (hs : S P=S 0) (hd : d P=d 0) :
    (∫ x in (0:ℝ)..P, exp (S x)*((k:ℝ)*(d x)^(k-1)*d₂ x+(d x)^(k+1)))=0 := by
  have cs : Continuous S := continuous_iff_continuousAt.mpr (fun x => (h₁ x).continuousAt)
  have cd : Continuous d := continuous_iff_continuousAt.mpr (fun x => (h₂ x).continuousAt)
  have h (x : ℝ) : HasDerivAt (fun y => (d y)^k*exp (S y))
      (exp (S x)*((k:ℝ)*(d x)^(k-1)*d₂ x+(d x)^(k+1))) x := by
    convert ((h₂ x).pow k).mul (h₁ x).exp using 1
    rw [pow_succ]
    ring
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => h x)
    ((by fun_prop : Continuous (fun x => exp (S x)*((k:ℝ)*(d x)^(k-1)*d₂ x+
      (d x)^(k+1)))).intervalIntegrable _ _), hs, hd]
  ring

theorem orbitFourthBound (S d d₂ : ℝ → ℝ) {P M : ℝ} (hP : 0 ≤ P) (hm : 0 ≤ M)
    (h₁ : ∀ x, HasDerivAt S (d x) x) (h₂ : ∀ x, HasDerivAt d (d₂ x) x)
    (hc : Continuous d₂) (hs : S P=S 0) (hd : d P=d 0) (lower : ∀ x, -M ≤ d₂ x) :
    (∫ x in (0:ℝ)..P, exp (S x)*(d x)^4) ≤ 3*M^2*(∫ x in (0:ℝ)..P, exp (S x)) := by
  have cs : Continuous S := continuous_iff_continuousAt.mpr (fun x => (h₁ x).continuousAt)
  have cd : Continuous d := continuous_iff_continuousAt.mpr (fun x => (h₂ x).continuousAt)
  let A := fun x => exp (S x)*(d₂ x+(d x)^2)
  let B := fun x => exp (S x)*(3*(d x)^2*d₂ x+(d x)^4)
  have ca : Continuous A := by dsimp [A]; fun_prop
  have cb : Continuous B := by dsimp [B]; fun_prop
  have za : (∫ x in (0:ℝ)..P, A x)=0 := by
    simpa [A] using orbitIBP S d d₂ P 1 h₁ h₂ hc hs hd
  have zb : (∫ x in (0:ℝ)..P, B x)=0 := by
    simpa [B] using orbitIBP S d d₂ P 3 h₁ h₂ hc hs hd
  calc
    _ ≤ ∫ x in (0:ℝ)..P, (B x+3*M*A x)+3*M^2*exp (S x) := by
      apply intervalIntegral.integral_mono_on hP
        ((by fun_prop : Continuous (fun x => exp (S x)*(d x)^4)).intervalIntegrable _ _)
        ((by fun_prop : Continuous (fun x => (B x+3*M*A x)+3*M^2*exp (S x))).intervalIntegrable _ _)
      intro x _
      dsimp [A,B]
      have hp := mul_nonneg (exp_pos (S x)).le (mul_nonneg (add_nonneg (sq_nonneg (d x)) hm)
        (show 0 ≤ d₂ x+M by linarith only [lower x]))
      linarith only [hp]
    _ = _ := by
      rw [intervalIntegral.integral_add ((by fun_prop : Continuous
          (fun x => B x+3*M*A x)).intervalIntegrable _ _)
        ((by fun_prop : Continuous (fun x => 3*M^2*exp (S x))).intervalIntegrable _ _),
        intervalIntegral.integral_add (cb.intervalIntegrable _ _)
        ((by fun_prop : Continuous (fun x => 3*M*A x)).intervalIntegrable _ _)]
      simp only [intervalIntegral.integral_const_mul, za, zb, mul_zero, zero_add]

theorem orientEnergy (a b c : ℝ) :
    (a+b)^2+(a+c)^2+(b+c)^2 = a^2+b^2+c^2+(a+b+c)^2 := by ring

theorem threeMasks (a b c : ℝ) :
    ((a+b)^2+(a+c)^2+(b+c)^2)/6 =
      ((a+b)^2/2+(a+c)^2/2+(b+c)^2/2)/3 := by ring

theorem physicalConstant : (1/6:ℝ)*(3/2)/6^2*4=1/36 := by norm_num

/-- The variance floor for every real temporal linear combination also
bounds an alternating sequence of even length. -/
theorem alternatingBudget {ι : Type*} (S : Finset ι) (a : ι → ℝ)
    (signs : ∀ i ∈ S, (a i)^2=1) (d : ℝ) :
    ∑ i ∈ S, d*(a i)^2 = S.card*d := by
  calc
    _ = ∑ _i ∈ S, d := Finset.sum_congr rfl (fun i hi => by rw [signs i hi, mul_one])
    _ = _ := by simp

theorem spacetimeConstant : (1/8:ℝ)*(3/2)/6^2*4=1/48 := by norm_num

theorem electricMagnetic (m d : ℝ) :
    3*(2*m+d)^2+(3*d)^2=6*(m^2+d^2)+6*(m+d)^2 := by ring

/-- For a linear combination with diagonal score pairing q and Gram
upper bound cap*q, subtracting the scaled score removes q/cap variance. -/
theorem scoreRemoval {cap q old altered scoreSq : ℝ} (hc : 0 < cap)
    (pairing : altered=old-2*q/cap+scoreSq/cap^2)
    (upper : scoreSq ≤ cap*q) : q/cap ≤ old-altered := by
  rw [pairing]
  have h : scoreSq/cap^2 ≤ q/cap := by
    rw [div_le_div_iff₀ (sq_pos_of_pos hc) hc]
    nlinarith [mul_nonneg (sub_nonneg.mpr upper) hc.le]
  rw [mul_div_assoc]
  linarith only [h]

/-- Fourth moments from integration by parts with a bounded second derivative. -/
theorem scoreFourth {four two M : ℝ} (hm : 0 ≤ M)
    (first : two ≤ M) (second : four ≤ 3*M*two) : four ≤ 3*M^2 := by
  nlinarith [mul_nonneg hm (sub_nonneg.mpr first)]

theorem sparseGramPair (x y : ℝ) : 2 * |x| * |y| ≤ x^2+y^2 := by
  nlinarith only [sq_nonneg (|x|-|y|), sq_abs x, sq_abs y]

/-- Each new time adds one diagonal entry and two copies of every previous lag. -/
def toeplitzTotal (x : ℝ) (N : ℕ) : ℝ :=
  ∑ i ∈ Finset.range N, (1+2*∑ k ∈ Finset.range i, x^(k+1))

private theorem lagSum (x : ℝ) (N : ℕ) :
    (1-x)*(∑ k ∈ Finset.range N, x^(k+1))=x*(1-x^N) := by
  induction N with
  | zero => simp
  | succ n ih =>
    rw [Finset.sum_range_succ, pow_succ x n]
    linarith only [ih]

theorem toeplitzFormula (x : ℝ) (N : ℕ) :
    (1-x)^2*toeplitzTotal x N=N*(1-x^2)-2*x*(1-x^N) := by
  induction N with
  | zero => simp [toeplitzTotal]
  | succ n ih =>
    simp only [toeplitzTotal, Finset.sum_range_succ, Nat.cast_succ, pow_succ x n] at ⊢
    change (1-x)^2*(toeplitzTotal x n+(1+2*∑ k ∈ Finset.range n, x^(k+1)))=_
    have h := congrArg (fun v : ℝ => (1-x)*v) (lagSum x n)
    dsimp only at h
    linarith only [ih,h]

/-- An alternating Toeplitz sum permits the zero energy endpoint r=1. -/
theorem fejerIdentity {N r B : ℝ} (hN : 0 < N) (hr : 0 ≤ r)
    (power : ℝ) (relation : (1+r)^2*B=N*(1-r^2)+2*r*(1-power)) :
    B/N=(1-r)/(1+r)+2*r*(1-power)/(N*(1+r)^2) := by
  have h : 1+r ≠ 0 := by linarith
  have hb : B=(N*(1-r^2)+2*r*(1-power))/(1+r)^2 := by
    apply (eq_div_iff (pow_ne_zero 2 h)).2
    simpa [mul_comm] using relation
  rw [hb]
  field_simp
  ring

theorem fejerError {N r power : ℝ} (hN : 0 < N) (hr : 0 ≤ r)
    (hl : 0 ≤ power) (hh : power ≤ 1) :
    0 ≤ 2*r*(1-power)/(N*(1+r)^2) ∧
    2*r*(1-power)/(N*(1+r)^2) ≤ 1/N := by
  have hp : 0 < N*(1+r)^2 := by positivity
  constructor
  · exact div_nonneg (by nlinarith [mul_nonneg hr (sub_nonneg.mpr hh)]) hp.le
  · rw [div_le_div_iff₀ hp hN]
    have h : 2*r*(1-power) ≤ (1+r)^2 := by nlinarith [mul_nonneg hr hl, sq_nonneg r]
    nlinarith [mul_nonneg (sub_nonneg.mpr h) hN.le]

theorem highEnergyBudget {total low high floor decay reading : ℝ}
    (budget : floor ≤ total) (split : total ≤ low+high)
    (observed : low ≤ decay*reading) : floor-decay*reading ≤ high := by linarith

end YangMills.WilsonContact
#print axioms YangMills.WilsonContact.projectionLoss
#print axioms YangMills.WilsonContact.separation
#print axioms YangMills.WilsonContact.polarScaling
#print axioms YangMills.WilsonContact.gammaVariance
#print axioms YangMills.WilsonContact.orientEnergy
#print axioms YangMills.WilsonContact.threeMasks
#print axioms YangMills.WilsonContact.physicalConstant
#print axioms YangMills.WilsonContact.alternatingBudget
#print axioms YangMills.WilsonContact.fejerIdentity
#print axioms YangMills.WilsonContact.fejerError
#print axioms YangMills.WilsonContact.highEnergyBudget
#print axioms YangMills.WilsonContact.toeplitzFormula
#print axioms YangMills.WilsonContact.conditionalFiberLoss
#print axioms YangMills.WilsonContact.spacetimeConstant
#print axioms YangMills.WilsonContact.electricMagnetic
#print axioms YangMills.WilsonContact.scoreRemoval
#print axioms YangMills.WilsonContact.scoreFourth
#print axioms YangMills.WilsonContact.sparseGramPair
#print axioms YangMills.WilsonContact.orbitIBP
#print axioms YangMills.WilsonContact.orbitFourthBound
