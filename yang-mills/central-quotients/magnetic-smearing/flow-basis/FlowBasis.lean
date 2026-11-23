import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Data.Real.Sqrt
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace YangMills.FlowBasis

theorem mixedClock (s u E : ℝ) :
    Real.exp (-s*E^2/2)*Real.exp (-u*E^2/2)=Real.exp (-((s+u)/2)*E^2) := by
  rw [← Real.exp_add]
  congr 1
  ring

theorem gramScale {s u : ℝ} (hs : 0<s) (hu : 0<u) :
    (2*Real.sqrt s*Real.sqrt u/(s+u))^2 + ((s-u)/(s+u))^2 = 1 := by
  have h := Real.sq_sqrt hs.le
  have h' := Real.sq_sqrt hu.le
  field_simp [show s+u ≠ 0 by linarith]
  nlinarith [congrArg₂ (fun x y : ℝ => x*y) h h']

theorem entrywiseError {ι : Type*} (I : Finset ι) (c : ι → ℝ) (D : ι → ι → ℝ)
    (e : ℝ) (hb : ∀ i ∈ I, ∀ j ∈ I, |D i j| ≤ e) :
    |∑ i ∈ I, ∑ j ∈ I, c i*c j*(D i j)| ≤ e*(∑ i ∈ I, |c i|)^2 := by
  calc
    _ ≤ ∑ i ∈ I, |∑ j ∈ I, c i*c j*(D i j)| := Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ i ∈ I, ∑ j ∈ I, |c i*c j*(D i j)| := by
      apply Finset.sum_le_sum
      intro i _
      exact Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ i ∈ I, ∑ j ∈ I, |c i| * |c j| * e := by
      apply Finset.sum_le_sum
      intro i hi
      apply Finset.sum_le_sum
      intro j hj
      rw [abs_mul,abs_mul]
      exact mul_le_mul_of_nonneg_left (hb i hi j hj) (by positivity)
    _ = _ := by
      simp only [sq, Finset.mul_sum, Finset.sum_mul]
      apply Finset.sum_congr rfl
      intro i _
      apply Finset.sum_congr rfl
      intro j _
      ring

noncomputable def sg (x : ℝ) : ℝ := if x<0 then -1 else 1

theorem signProduct (x : ℝ) : x*sg x=|x| := by
  by_cases hx : x<0
  · simp [sg,hx,abs_of_neg hx]
  · simp [sg,hx,abs_of_nonneg (le_of_not_gt hx)]

theorem sharpLine {ι : Type*} (I : Finset ι) (c : ι → ℝ) (e : ℝ) :
    (∑ i ∈ I, ∑ j ∈ I, c i*c j*(e*sg (c i)*sg (c j))) = e*(∑ i ∈ I, |c i|)^2 := by
  simp only [sq,Finset.sum_mul,Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  apply Finset.sum_congr rfl
  intro j _
  rw [← signProduct (c i),← signProduct (c j)]
  ring

theorem amplificationBound {h ell chi A qN : ℝ} (hq : 0<qN) (hA : 0<A)
    (hh : h ≤ ell+chi*A*qN) : (h-ell)/(A*qN) ≤ chi := by
  apply (div_le_iff₀ (mul_pos hA hq)).2
  linarith only [hh, mul_assoc chi A qN]

theorem monotoneWeights {l h w₁ w₂ : ℝ} (hl : 0≤l) (hh : 0≤h) (hw : w₁≤w₂) :
    (l*w₁)*h ≤ l*(h*w₂) := by
  nlinarith [mul_nonneg (mul_nonneg hl hh) (sub_nonneg.mpr hw)]


theorem localQuaternionBounds : ((6*3^5,6*5*3^4) : ℕ × ℕ) = (1458,2430) := by decide

theorem recoverBand {X V M A r : ℝ} (hA : 0<A) (h : V ≤ A*X+M*r) :
    (V-M*r)/A ≤ X := by
  apply (div_le_iff₀ hA).2
  linarith only [h, mul_comm A X]
theorem fejerThree (x : ℝ) :
    1-(4*(2*x-1)^3-3*(2*x-1)) = 2*(1-x)*(1-4*x)^2 := by ring

theorem fiveWeights (x : ℝ) :
    (1-4*x)^4=1-16*x+96*x^2-256*x^3+256*x^4 := by ring

theorem signedSum : (1-16+96-256+256 : ℤ)=81 := by decide
theorem absoluteSum : (1+16+96+256+256 : ℕ)=625 := by decide

theorem eighthHarmonics : ((-56*2^3+28*4^3-8*6^3+8^3 : ℚ)/128)=1 ∧
    ((56*2-28*4+8*6-8 : ℚ)/128)=5/16 := by norm_num

theorem limitMomentRatio {g : ℝ} (hg : 0<g) :
    ((5/32:ℝ)/g^7)/((1/12:ℝ)/g^5)=15/(8*g^2) := by
  field_simp
  ring

theorem halfBand {p : ℝ} (h : p≤15/32) : 1/2 < 1-p := by linarith
noncomputable def term (r : ℝ) := (5*r-1)*r^2*Real.sqrt r

theorem sqrtBounds (u lo hi : ℝ) (hl : lo^2 ≤ u) (hh : u ≤ hi^2) (hp : 0 ≤ hi) :
    lo ≤ Real.sqrt u ∧ Real.sqrt u ≤ hi :=
  ⟨Real.le_sqrt_of_sq_le hl, Real.sqrt_le_iff.mpr ⟨hp,hh⟩⟩

noncomputable def comp (f : ℝ → ℝ) :=
    1*f (8/8) -32*f (8/11) +448*f (8/14) -3584*f (8/17) +17920*f (8/20) -57344*f (8/23) +114688*f (8/26) -131072*f (8/29) +65536*f (8/32)

theorem fiveRayleigh : comp term < 0 := by
  have h0 := sqrtBounds (8/8) (10000000000/10000000000) (10000000001/10000000000) (by norm_num) (by norm_num) (by norm_num)
  have h1 := sqrtBounds (8/11) (8528028654/10000000000) (8528028655/10000000000) (by norm_num) (by norm_num) (by norm_num)
  have h2 := sqrtBounds (8/14) (7559289460/10000000000) (7559289461/10000000000) (by norm_num) (by norm_num) (by norm_num)
  have h3 := sqrtBounds (8/17) (6859943405/10000000000) (6859943406/10000000000) (by norm_num) (by norm_num) (by norm_num)
  have h4 := sqrtBounds (8/20) (6324555320/10000000000) (6324555321/10000000000) (by norm_num) (by norm_num) (by norm_num)
  have h5 := sqrtBounds (8/23) (5897678246/10000000000) (5897678247/10000000000) (by norm_num) (by norm_num) (by norm_num)
  have h6 := sqrtBounds (8/26) (5547001962/10000000000) (5547001963/10000000000) (by norm_num) (by norm_num) (by norm_num)
  have h7 := sqrtBounds (8/29) (5252257314/10000000000) (5252257315/10000000000) (by norm_num) (by norm_num) (by norm_num)
  have h8 := sqrtBounds (8/32) (5000000000/10000000000) (5000000001/10000000000) (by norm_num) (by norm_num) (by norm_num)
  unfold comp term
  linarith only [h0.2, h1.1, h2.2, h3.1, h4.2, h5.1, h6.2, h7.1, h8.2]


/-- At fixed flow variable, the moving-momentum energy window has square-root width. -/
theorem windowWidth {lo hi D : ℝ} (hlo : 0 ≤ lo) (hhi : lo ≤ hi)
    (h : hi^2-lo^2 ≤ D) : hi-lo ≤ Real.sqrt D := by
  apply Real.le_sqrt_of_sq_le
  nlinarith [mul_nonneg hlo (sub_nonneg.mpr hhi)]

theorem energyWindow (E δ : ℝ) : (E+δ)^2-E^2=δ*(2*E+δ) := by ring

theorem intervalAverage {num den cap : ℝ} (hd : 0 < den) (hb : num ≤ cap*den) :
    num/den ≤ cap := (div_le_iff₀ hd).2 hb

end YangMills.FlowBasis
open YangMills.FlowBasis
#print axioms mixedClock
#print axioms gramScale
#print axioms entrywiseError
#print axioms signProduct
#print axioms sharpLine
#print axioms amplificationBound
#print axioms monotoneWeights
#print axioms fejerThree
#print axioms fiveWeights
#print axioms signedSum
#print axioms absoluteSum
#print axioms eighthHarmonics
#print axioms limitMomentRatio
#print axioms halfBand
#print axioms sqrtBounds
#print axioms fiveRayleigh
#print axioms localQuaternionBounds
#print axioms recoverBand
#print axioms windowWidth
#print axioms energyWindow
#print axioms intervalAverage
