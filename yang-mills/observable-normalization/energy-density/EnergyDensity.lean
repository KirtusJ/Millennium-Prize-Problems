import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

open MeasureTheory
open scoped BigOperators
namespace YangMills.EnergyDensity

theorem coordinateCasimir (n : ℝ) :
    (((n+1)*(n+3)-n*(n+2))^2 = 2*((n+1)*(n+3)+n*(n+2))+3) ∧
    (((n-1)*(n+1)-n*(n+2))^2 = 2*((n-1)*(n+1)+n*(n+2))+3) := by
  constructor <;> ring

theorem localDiagonal {κ lam B g S : ℝ} (hl : 0 ≤ lam)
    (hg : lam=κ*g) (hs : g*S ≤ 2*B) :
    (2*lam*(κ/4)^2*(16*B+9) = κ^2*lam*(2*B+9/8)) ∧
    κ*lam^2*S ≤ κ^2*lam*(2*B+9/8) := by
  constructor
  · ring
  · have h := mul_le_mul_of_nonneg_left hs (mul_nonneg (sq_nonneg κ) hl)
    have h' : κ*lam^2*S=κ^2*lam*(g*S) := by rw [hg]; ring
    nlinarith only [h,h',mul_nonneg (sq_nonneg κ) hl]

/-- The conserved constant mode converts the whole sum into squared spatial differences. -/
theorem zeroRowForm {ι : Type*} [Fintype ι] (K : ι → ι → ℝ) (w : ι → ℝ)
    (sym : ∀ i j, K i j=K j i) (row : ∀ i, ∑ j, K i j=0) :
    2*(∑ i, ∑ j, K i j*w i*w j) = -(∑ i, ∑ j, K i j*(w i-w j)^2) := by
  have diag : (∑ i, ∑ j, K i j*(w i)^2) = 0 := by
    simp only [← Finset.sum_mul,row,zero_mul,Finset.sum_const_zero]
  have other : (∑ i, ∑ j, K i j*(w j)^2) = 0 := by
    rw [Finset.sum_comm]
    convert diag using 1
    exact Finset.sum_congr rfl (fun i _ => Finset.sum_congr rfl (fun j _ => by rw [sym j i]))
  have eq (i j : ι) : K i j*(w i-w j)^2 =
      K i j*(w i)^2-2*(K i j*w i*w j)+K i j*(w j)^2 := by ring
  simp only [eq, Finset.sum_add_distrib, Finset.sum_sub_distrib, ← Finset.mul_sum,diag,other]
  ring

theorem bareCoefficient {β b B κ lam : ℝ} (hβ : 1 ≤ β) (hb : 0 < b)
    (hk : κ=2/(β*b)) (hl : lam=β/b) (hB : B ≤ 5*β/2) :
    b^3*(κ^2*lam*(2*B+9/8)) ≤ 25 := by
  have hpos : 0 < β := by linarith
  have id : b^3*(κ^2*lam*(2*B+9/8))=(8*B+9/2)/β := by
    rw [hk,hl]
    field_simp
    ring
  rw [id]
  apply (div_le_iff₀ hpos).mpr
  linarith only [hB,hβ]

theorem filterPoint {s E : ℝ} (hs : 0 ≤ s) (he : 0 ≤ E) :
    0 ≤ (1-Real.exp (-s*E)) ∧ (1-Real.exp (-s*E)) ≤ 1 ∧
      (1-Real.exp (-s*E)) ≤ s*E := by
  have h := Real.exp_le_one_iff.mpr (mul_nonpos_of_nonpos_of_nonneg (neg_nonpos.mpr hs) he)
  have h' := Real.add_one_le_exp (-s*E)
  exact ⟨by linarith, by linarith only [Real.exp_pos (-s*E)],by linarith⟩

theorem lowFilter {s E ε : ℝ} (hs : 0 ≤ s) (he : 0 ≤ E) (low : E ≤ ε) :
    (1-Real.exp (-s*E))^2 ≤ s^2*ε*E := by
  have h := filterPoint hs he
  have h2 := mul_self_le_mul_self h.1 h.2.2
  have h3 := mul_le_mul_of_nonneg_left low (mul_nonneg (sq_nonneg s) he)
  nlinarith only [h2,h3]

theorem highFilter {s E R : ℝ} (hs : 0 ≤ s) (hr : 0 < R) (high : R ≤ E) :
    (1-Real.exp (-s*E))^2 ≤ E/R := by
  have h := filterPoint hs (hr.le.trans high)
  have h2 := mul_self_le_mul_self h.1 h.2.1
  have : 1 ≤ E/R := (one_le_div hr).mpr high
  nlinarith only [this,h2]

/-- Integrate a local spectral majorant using only the first moment. -/
theorem restrictedFilter (μ : Measure ℝ) {s c : ℝ} (A : Set ℝ) (hA : MeasurableSet A)
    (hc : 0 ≤ c) (supp : ∀ᵐ E ∂μ, 0 ≤ E) (h1 : Integrable (fun E : ℝ => E) μ)
    (hi : IntegrableOn (fun E : ℝ => (1-Real.exp (-s*E))^2) A μ)
    (bound : ∀ E ∈ A, 0 ≤ E → (1-Real.exp (-s*E))^2 ≤ c*E) :
    (∫ E in A, (1-Real.exp (-s*E))^2 ∂μ) ≤ c * ∫ E : ℝ, E ∂μ := by
  have hs := ae_restrict_of_ae supp (s := A)
  have hm := (ae_restrict_mem (μ := μ) hA).and hs
  have h := integral_mono_ae hi ((h1.const_mul c).restrict (s := A))
    (hm.mono fun x hx => bound x hx.1 hx.2)
  rw [integral_const_mul] at h
  exact h.trans (mul_le_mul_of_nonneg_left (setIntegral_le_integral h1 supp) hc)

/-- Uniform first moments bound the mass of both tails of the filtered measure. -/
theorem filteredTails (μ : Measure ℝ) {s ε R C : ℝ}
    (hs : 0 ≤ s) (he : 0 ≤ ε) (hr : 0 < R)
    (supp : ∀ᵐ E ∂μ, 0 ≤ E) (h1 : Integrable (fun E : ℝ => E) μ)
    (hi : Integrable (fun E : ℝ => (1-Real.exp (-s*E))^2) μ)
    (moment : (∫ E : ℝ, E ∂μ) ≤ C) :
    (∫ E in Set.Icc 0 ε, (1-Real.exp (-s*E))^2 ∂μ) ≤ s^2*ε*C ∧
    (∫ E in Set.Ici R, (1-Real.exp (-s*E))^2 ∂μ) ≤ C/R := by
  have lo := restrictedFilter μ (Set.Icc 0 ε) measurableSet_Icc
    (mul_nonneg (sq_nonneg s) he) supp h1 hi.integrableOn
    (fun E hE hpos => lowFilter hs hpos hE.2)
  have upper := restrictedFilter μ (Set.Ici R) measurableSet_Ici
    (inv_nonneg.mpr hr.le) supp h1 hi.integrableOn (fun E hE _ => by
      simpa only [div_eq_inv_mul] using highFilter hs hr hE)
  constructor
  · exact lo.trans (mul_le_mul_of_nonneg_left moment (mul_nonneg (sq_nonneg s) he))
  · rw [div_eq_inv_mul]
    exact upper.trans (mul_le_mul_of_nonneg_left moment (inv_nonneg.mpr hr.le))

end YangMills.EnergyDensity
#print axioms YangMills.EnergyDensity.coordinateCasimir
#print axioms YangMills.EnergyDensity.localDiagonal
#print axioms YangMills.EnergyDensity.zeroRowForm
#print axioms YangMills.EnergyDensity.bareCoefficient
#print axioms YangMills.EnergyDensity.filterPoint
#print axioms YangMills.EnergyDensity.lowFilter
#print axioms YangMills.EnergyDensity.highFilter
#print axioms YangMills.EnergyDensity.restrictedFilter
#print axioms YangMills.EnergyDensity.filteredTails
