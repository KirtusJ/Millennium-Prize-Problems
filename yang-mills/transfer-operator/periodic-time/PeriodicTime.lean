import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.YangMills.PeriodicTime

/-- The defect-to-derivative multiplier controls one full electric derivative. -/
theorem kineticMultiplier {x a k d : ℝ} (hx : 0 < x) (hk : 0 ≤ k)
    (hd : 0 < d) (rel : k = 1-a*d) (lower : x ≤ (1+a*x)*d) (upper : d ≤ x) :
    0 ≤ x*k/d ∧ x*k/d ≤ 1 ∧ 1-x*k/d ≤ a*x := by
  refine ⟨by positivity, (div_le_iff₀ hd).2 ?_, ?_⟩
  · rw [rel]
    linarith
  · have h : (1-a*x) ≤ x*k/d := by
      apply (le_div_iff₀ hd).2
      rw [rel]
      linarith
    linarith

/-- Squared-norm error, in a finite joint spectral partition. -/
theorem graphError {ι : Type*} (s : Finset ι) (m x w : ι → ℝ) (a : ℝ)
    (unit : ∀ i ∈ s, m i ≤ 1) (loss : ∀ i ∈ s, 1-m i ≤ a*x i)
    (weight : ∀ i ∈ s, 0 ≤ w i) :
    ∑ i ∈ s, (1-m i)^2*w i ≤ a^2 * ∑ i ∈ s, (x i)^2*w i := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  have hs := mul_self_le_mul_self (sub_nonneg.mpr (unit i hi)) (loss i hi)
  calc
    _ ≤ (a*x i)^2*w i := mul_le_mul_of_nonneg_right (by nlinarith only [hs]) (weight i hi)
    _ = _ := by ring

/-- Two independent averages restore a single relative gauge average. -/
theorem gaugeAverage {G X : Type*} [Group G] [Fintype G] [MulAction G X]
    (K : X → X → ℝ) (invK : ∀ s : G, ∀ x y, K (s • x) (s • y) = K x y) (x y : X) :
    ∑ s : G, ∑ t : G, K (s • x) (t • y) =
      (Fintype.card G : ℝ) * ∑ t : G, K x (t • y) := by
  have row (s : G) : ∑ t : G, K (s • x) (t • y) = ∑ t : G, K x (t • y) := by
    symm
    apply Fintype.sum_equiv (Equiv.mulLeft s)
    intro t
    simp only [Equiv.coe_mulLeft, mul_smul, invK]
  simp_rw [row]
  simp

/-- Suppression after a trace-class block, with all excited multiplicities retained. -/
theorem traceTail {ι : Type*} (s : Finset ι) (x : ι → ℝ) (q : ℝ)
    (nonneg : ∀ i ∈ s, 0 ≤ x i) (cap : ∀ i ∈ s, x i ≤ q) (m r : ℕ) :
    ∑ i ∈ s, (x i)^(m+r) ≤ q^r * ∑ i ∈ s, (x i)^m := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  rw [pow_add, mul_comm]
  exact mul_le_mul_of_nonneg_right (pow_le_pow_left₀ (nonneg i hi) (cap i hi) r)
    (pow_nonneg (nonneg i hi) m)

/-- Numerical range after dividing by the full thermal partition. -/
theorem thermalBias {v tail z b ε : ℝ} (hv : |v| ≤ b) (hz : 0 ≤ z) (hε : z ≤ ε)
    (ht : |tail| ≤ b*ε) : |(v+tail)/(1+z)-v| ≤ 2*b*ε := by
  have hb : 0 ≤ b := (abs_nonneg _).trans hv
  have he : 0 ≤ ε := hz.trans hε
  have den : 0 < 1+z := by linarith
  have eqn : (v+tail)/(1+z)-v = (tail-v*z)/(1+z) := by field_simp; ring
  rw [eqn, abs_div, abs_of_pos den]
  apply (div_le_iff₀ den).2
  have prod : |v*z| ≤ b*ε := by
    rw [abs_mul, abs_of_nonneg hz]
    exact mul_le_mul hv hε hz hb
  have tri := abs_sub (a := tail) (b := v*z)
  nlinarith only [tri, ht, prod, mul_nonneg (mul_nonneg hb he) hz]

/-- The last term in the geometric sum bounds the derivative after h positive steps. -/
theorem positiveTimeSmoothing (s : ℝ) (hs : 0 ≤ s) (h1 : s ≤ 1) (j : ℕ) :
    ((j+1 : ℕ) : ℝ) * (1-s) * s^j ≤ 1-s^(j+1) := by
  induction j with
  | zero => simp
  | succ j ih =>
      have shrink := mul_le_mul_of_nonneg_right h1 (pow_nonneg hs j)
      have power : s^(j+1) ≤ s^j := by simpa [pow_succ, mul_comm] using shrink
      have factor : 0 ≤ ((j+1 : ℕ) : ℝ) * (1-s) := mul_nonneg (by positivity) (sub_nonneg.mpr h1)
      have comparison := mul_le_mul_of_nonneg_left power factor
      push_cast at ih comparison ⊢
      rw [pow_succ (n := j+1)]
      linarith

/-- For one changed staple, both quadratic terms have a controlled first difference. -/
theorem scoreVariation {u v H J R δ : ℝ} (hδ : 0 ≤ δ) (hR : 0 ≤ R)
    (hu : |u-v| ≤ 4*R*δ) (hH : |H-J| ≤ 3*R*δ)
    (su : |u+v| ≤ 2*R) (sH : |H+J| ≤ 2*R) :
    |(3*u-H^2+u^2)-(3*v-J^2+v^2)| ≤ (12*R+14*R^2)*δ := by
  have quadU := mul_le_mul hu su (abs_nonneg _) (by positivity)
  have quadH := mul_le_mul hH sH (abs_nonneg _) (by positivity)
  have tri := abs_add_le (3*(u-v) - (H-J)*(H+J)) ((u-v)*(u+v))
  have pair := abs_sub (a := 3*(u-v)) (b := (H-J)*(H+J))
  have eqn : (3*u-H^2+u^2)-(3*v-J^2+v^2) =
      3*(u-v)-(H-J)*(H+J)+(u-v)*(u+v) := by ring
  rw [eqn]
  rw [abs_mul, abs_of_nonneg (by norm_num : (0:ℝ) ≤ 3)] at pair
  rw [abs_mul] at pair tri
  nlinarith only [tri, pair, quadU, quadH, hu]

/-- Dilation budget for a bounded sampling displacement and a mismatch of local coefficients. -/
theorem mixedDilation {M b D A z θ G U w : ℝ} (hb : 0 < b) (hD : 0 < D) (hA : 0 ≤ A)
    (change : |w| ≤ z*b*D*G + 2*θ*U) (energy : M ≤ A*w^2/(b^6*D^3)) :
    M/D ≤ A*(z*G/(b^2*D) + 2*θ*U/(b^3*D^2))^2 := by
  have square := mul_self_le_mul_self (abs_nonneg w) change
  rw [abs_mul_abs_self] at square
  have sq : w^2 ≤ (z*b*D*G+2*θ*U)^2 := by nlinarith only [square]
  calc
    M/D ≤ (A*w^2/(b^6*D^3))/D := div_le_div_of_nonneg_right energy hD.le
    _ ≤ (A*(z*b*D*G+2*θ*U)^2/(b^6*D^3))/D := by gcongr
    _ = _ := by field_simp; ring

-- PCP begin geometry
theorem sphericalScore {h u : ℝ} (rad : |u| ≤ h) :
    |3*u-h^2+u^2| ≤ 3*h+h^2 := by
  have bounds := abs_le.mp rad
  have square := mul_self_le_mul_self (abs_nonneg u) rad
  rw [abs_mul_abs_self] at square
  apply abs_le.mpr
  constructor <;> nlinarith [sq_nonneg u, sq_nonneg h]
-- PCP end geometry

-- PCP begin certificate
theorem threeThermalErrors {u v w b : ℝ} (hu : |u| ≤ 2*b) (hv : |v| ≤ 2*b)
    (hw : |w| ≤ 2*b) : |u-2*v+w| ≤ 8*b := by
  have U := abs_le.mp hu
  have V := abs_le.mp hv
  have W := abs_le.mp hw
  apply abs_le.mpr
  constructor <;> linarith
-- PCP end certificate

#print axioms kineticMultiplier
#print axioms graphError
#print axioms gaugeAverage
#print axioms traceTail
#print axioms thermalBias
#print axioms positiveTimeSmoothing
#print axioms scoreVariation
#print axioms mixedDilation
#print axioms sphericalScore
#print axioms threeThermalErrors
end Millennium.YangMills.PeriodicTime
