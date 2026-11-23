import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

open MeasureTheory
open scoped ENNReal
namespace YangMills.LorentzTest

/-- The rest-frame Ward identities kill the time row and column. -/
theorem massiveBoost {c h m k a : ℝ} (hm : 0 < m) (boost : h=k/m) :
    c^2*0+2*c*h*0+h^2*a=(k^2/m^2)*a := by
  rw [boost]
  field_simp [hm.ne']

/-- On a null ray, T00, T0n and Tnn have equal matrix elements. -/
theorem nullBoost (c h a : ℝ) :
    c^2*a+2*c*h*a+h^2*a=(c+h)^2*a := by ring

theorem shellMoment {E k m a : ℝ} (hE : 0 < E) (hm : 0 < m) :
    E*((k^2/m^2)^2*a/(2*E))=k^4*(a/(2*m^4)) := by
  field_simp
  ring

theorem projectedChannels (x c₀ c₂ : ℝ) :
    c₀*x^2/3+c₂*(x*x-x^2/3)=x^2*((c₀+2*c₂)/3) := by ring

/-- A locally recovered positive-energy law retains the budget under exhaustion. -/
theorem recoveredMoment {α : Type*} [MeasurableSpace α] (μ : Measure α)
    (f : ℕ → α → ℝ≥0∞) (h : α → ℝ≥0∞) (C : ℝ≥0∞)
    (meas : ∀ n, Measurable (f n)) (mono : Monotone f)
    (exhaust : ∀ x, h x=⨆ n, f n x) (budget : ∀ n, (∫⁻ x, f n x ∂μ) ≤ C) :
    (∫⁻ x, h x ∂μ) ≤ C := by
  simpa only [exhaust,lintegral_iSup meas mono] using (iSup_le budget)

theorem finiteScale {c B A K L : ℝ} (hB : 0 < B) (hL : 0 < L)
    (lower : c*(L*B) ≤ K) (upper : K ≤ A/L) :
    c ≤ A/(L^2*B) := by
  apply (le_div_iff₀ (mul_pos (sq_pos_of_pos hL) hB)).mpr
  have h := (le_div_iff₀ hL).mp (lower.trans upper)
  linarith only [h]

/-- Every fixed test is passed to the limit before taking arbitrarily large dilation. -/
theorem rigidity {c B A : ℝ} (hc : 0 ≤ c) (hB : 0 < B) (hA : 0 ≤ A)
    (allTests : ∀ L : ℝ, 1 ≤ L → c*(L^2*B) ≤ A) : c=0 := by
  by_contra! neq
  have cp := lt_of_le_of_ne hc (Ne.symm neq)
  let L : ℝ := 1+A/(c*B)
  have hL : 1 ≤ L := by dsimp [L]; linarith only [div_nonneg hA (mul_pos cp hB).le]
  have bound := allTests L hL
  have identity : c*B*L=c*B+A := by
    dsimp [L]
    field_simp
  have grow : L ≤ L^2 := by nlinarith only [mul_nonneg (sub_nonneg.mpr hL) (by linarith : 0 ≤ L)]
  nlinarith only [bound, identity, mul_le_mul_of_nonneg_left grow (mul_pos cp hB).le,mul_pos cp hB]

noncomputable def detector (u : ℝ) := Real.exp (-u)*(1-Real.exp (-u))^2

theorem detectorUpper {u : ℝ} (hu : 0 ≤ u) : detector u ≤ u := by
  have hp := (Real.exp_pos (-u)).le
  have he := Real.exp_le_one_iff.mpr (neg_nonpos.mpr hu)
  have hf : 0 ≤ 1-Real.exp (-u) := by linarith
  have hb := Real.add_one_le_exp (-u)
  have h2 := mul_nonneg hp hf
  have h3 := mul_le_mul_of_nonneg_right he (sq_nonneg (1-Real.exp (-u)))
  unfold detector
  nlinarith only [h2,h3,hb]

theorem detectorCore {u : ℝ} (lo : 1 ≤ u) (hi : u ≤ 3) :
    Real.exp (-3)*(1-Real.exp (-1))^2 ≤ detector u := by
  have a := Real.exp_le_exp.mpr (neg_le_neg hi)
  have b := Real.exp_le_exp.mpr (neg_le_neg lo)
  have c : 0 ≤ 1-Real.exp (-1) := by
    linarith only [Real.exp_le_one_iff.mpr (by norm_num : (-1:ℝ) ≤ 0)]
  have bound := mul_self_le_mul_self c (sub_le_sub_left b 1)
  exact mul_le_mul a (by simpa only [← sq] using bound) (sq_nonneg _) (Real.exp_pos _).le

theorem tripleBudget (μ : Measure ℝ) {t : ℝ} (ht : 0 ≤ t)
    (supp : ∀ᵐ E ∂μ, 0 ≤ E) (h1 : Integrable (fun E : ℝ => E) μ)
    (hi : Integrable (fun E => detector (t*E)) μ) :
    (∫ E, detector (t*E) ∂μ) ≤ t*∫ E : ℝ, E ∂μ := by
  have h := integral_mono_ae hi (h1.const_mul t)
    (supp.mono fun E he => detectorUpper (mul_nonneg ht he))
  exact h.trans_eq (integral_const_mul t (fun x : ℝ => x))

theorem shellDetectorLower {L E : ℝ} (hL : 0 < L) (lo : L ≤ E) (hi : E ≤ 3*L) :
    Real.exp (-3)*(1-Real.exp (-1))^2/(6*L) ≤ detector (E/L)/(2*E) := by
  let k := Real.exp (-3)*(1-Real.exp (-1))^2
  have hk : 0 ≤ k := mul_nonneg (Real.exp_pos _).le (sq_nonneg _)
  have core := detectorCore ((one_le_div hL).mpr lo) ((div_le_iff₀ hL).mpr hi)
  change k ≤ detector (E/L) at core
  change k/(6*L) ≤ detector (E/L)/(2*E)
  apply (div_le_div_iff₀ (by linarith) (by linarith)).mpr
  nlinarith only [mul_le_mul_of_nonneg_left hi hk,
    mul_le_mul_of_nonneg_right core hL.le]

/-- A countably exhausted interval of timelike invariant masses has zero measure. -/
theorem massBandsVanish (σ : Measure ℝ) (bands : ℕ → Set ℝ)
    (cover : Set.Ioi 0 ⊆ ⋃ n, bands n)
    (fin : ∀ n, σ (bands n) ≠ ⊤) {A B : ℝ} (hA : 0 ≤ A) (hB : 0 < B)
    (tests : ∀ n (L : ℝ), 1 ≤ L → σ.real (bands n)*(L^2*B) ≤ A) :
    σ (Set.Ioi 0) = 0 := by
  have hz (n : ℕ) : σ (bands n)=0 := by
    have h := rigidity (measureReal_nonneg : 0 ≤ σ.real (bands n)) hB hA (tests n)
    exact ((ENNReal.toReal_eq_zero_iff _).mp h).resolve_right (fin n)
  exact measure_mono_null cover (measure_iUnion_null hz)

theorem nullWeightVanishes {a A B : ℝ} (ha : 0 ≤ a) (hA : 0 ≤ A) (hB : 0 < B)
    (tests : ∀ L : ℝ, 1 ≤ L → a*(L^2*B) ≤ A) : a=0 :=
  rigidity ha hB hA tests

/-- Arbitrarily fine tests suffice, with the limit in the cutoff taken for each fixed test. -/
theorem diagonalObstruction {c A : ℝ} (hA : 0 ≤ A) (hc : 0 ≤ c)
    (probes : ∀ R : ℝ, ∃ L : ℝ, R ≤ L ∧ c*L^2 ≤ A) : c=0 := by
  by_contra! hn
  have pos := lt_of_le_of_ne hc (Ne.symm hn)
  obtain ⟨L,hL,bound⟩ := probes (1+A/c)
  have hlo : 1 ≤ L := by linarith only [hL,div_nonneg hA hc]
  have grow : L ≤ L^2 := by
    nlinarith only [mul_nonneg (sub_nonneg.mpr hlo) (by linarith only [hlo] : 0 ≤ L)]
  have h := mul_le_mul_of_nonneg_left hL hc
  have id : c*(1+A/c)=c+A := by field_simp
  nlinarith only [h,id,bound,mul_le_mul_of_nonneg_left grow hc,pos]

end YangMills.LorentzTest
#print axioms YangMills.LorentzTest.massiveBoost
#print axioms YangMills.LorentzTest.nullBoost
#print axioms YangMills.LorentzTest.shellMoment
#print axioms YangMills.LorentzTest.projectedChannels
#print axioms YangMills.LorentzTest.recoveredMoment
#print axioms YangMills.LorentzTest.finiteScale
#print axioms YangMills.LorentzTest.rigidity
#print axioms YangMills.LorentzTest.massBandsVanish
#print axioms YangMills.LorentzTest.nullWeightVanishes
#print axioms YangMills.LorentzTest.detectorUpper
#print axioms YangMills.LorentzTest.detectorCore
#print axioms YangMills.LorentzTest.tripleBudget
#print axioms YangMills.LorentzTest.diagonalObstruction
#print axioms YangMills.LorentzTest.shellDetectorLower
