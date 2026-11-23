import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Tactic.Linarith

namespace YangMills.ElectricEndpoint

theorem varianceIdentity (u S : ℝ) :
    4*((1-S)-(1-u)^2)=4*(2*u-u^2-S) := by ring

/-- Keep the kinetic and potential energies in the same trial budget. -/
theorem jointBudget {K u g : ℝ} (hu : 0 ≤ u) (hg : 0 ≤ g)
    (budget : K+g*u ≤ 17*Real.sqrt g/8+3/16) :
    u*K ≤ 289/256+3*u/16 := by
  have h := mul_le_mul_of_nonneg_right budget hu
  have sq : (Real.sqrt g*u)^2=g*u^2 := by rw [mul_pow, Real.sq_sqrt hg]
  nlinarith only [h, sq, sq_nonneg (Real.sqrt g*u-17/16)]

theorem sphereLower {K S : ℝ} (hK : 0 ≤ K) (hS : 0 ≤ S)
    (sphere : 3-4*S ≤ 4*Real.sqrt (K*S)) : 9 ≤ (16*K+24)*S := by
  have h := Real.sq_sqrt (mul_nonneg hK hS)
  by_cases hs : 0 ≤ 3-4*S
  · have p := mul_nonneg (sub_nonneg.mpr sphere)
      (add_nonneg (mul_nonneg (show (0:ℝ) ≤ 4 by norm_num) (Real.sqrt_nonneg (K*S))) hs)
    nlinarith only [p,h,sq_nonneg S]
  · nlinarith [mul_nonneg hK hS]

theorem envelope (u : ℝ) : (2-u)*(289/256+27*u/16) ≤ 99/32 := by
  nlinarith only [sq_nonneg (864*u-575)]

theorem productBound {K u : ℝ} (hu : u ≤ 2)
    (joint : u*K ≤ 289/256+3*u/16) :
    (2*u-u^2)*(K+3/2) ≤ 99/32 := by
  have h := mul_le_mul_of_nonneg_left joint (sub_nonneg.mpr hu)
  linarith only [h,envelope u]

theorem normBound {K S u : ℝ} (hK : 0 ≤ K)
    (sphere : 9 ≤ (16*K+24)*S) (prod : (2*u-u^2)*(K+3/2) ≤ 99/32) :
    4*(2*u-u^2-S) ≤ 18*S := by
  by_contra hn
  have h := mul_pos (sub_pos.mpr (lt_of_not_ge hn))
    (show 0 < K+3/2 by linarith)
  nlinarith only [h,sphere,prod]

theorem endpoint {K S u g κ : ℝ} (hK : 0 ≤ K) (hS : 0 ≤ S)
    (hu : 0 ≤ u) (hu₂ : u ≤ 2) (hg : 0 ≤ g) (hκ : 0 ≤ κ)
    (budget : K+g*u ≤ 17*Real.sqrt g/8+3/16)
    (sphere : 3-4*S ≤ 4*Real.sqrt (K*S)) :
    κ/18*(4*(2*u-u^2-S)) ≤ (4*κ*S)/4 := by
  have hv := normBound hK (sphereLower hK hS sphere)
    (productBound hu₂ (jointBudget hu hg budget))
  nlinarith only [mul_nonneg hκ (sub_nonneg.mpr hv)]

theorem retainWeight {A D U M low band : ℝ} (ha : 0 < A) (hd : 0 < D)
    (hu : U=4*D/A) (first : A ≤ M) (lower : low ≤ M/4)
    (extraction : M ≤ low+D/U+U*band) : A^2/(8*D) ≤ band := by
  have u_pos : 0 < U := by rw [hu]; positivity
  have d_u : D/U=A/4 := by rw [hu]; field_simp; ring
  rw [d_u] at extraction
  have hb : A/2 ≤ U*band := by linarith only [lower,first,extraction]
  calc
    A^2/(8*D)=(A/2)/U := by rw [hu]; field_simp; ring
    _ ≤ band := (div_le_iff₀ u_pos).2 (by simpa [mul_comm] using hb)

/-- Both extractions use the same upper endpoint and guaranteed weight. -/
theorem combinedBand (μ : Set ℝ → ℝ) {a b u m : ℝ}
    (ha : m ≤ μ (Set.Icc a u)) (hb : m ≤ μ (Set.Icc b u)) :
    m ≤ μ (Set.Icc (max a b) u) := by
  rcases le_total a b with h | h
  · simpa [max_eq_right h] using hb
  · simpa [max_eq_left h] using ha

theorem crossover {κ B : ℝ} (hk : 0 < κ) (hB : 0 ≤ B) :
    κ/18 ≤ (9*κ/(8*(1+B)))/16 ↔ B ≤ 17/64 := by
  rw [div_div, le_div_iff₀ (by positivity)]
  constructor
  · intro h
    by_contra! hc
    nlinarith only [h, mul_pos hk (sub_pos.mpr hc)]
  · intro hc
    nlinarith only [mul_nonneg hk.le (sub_nonneg.mpr hc)]

theorem budgetCrossover {g : ℝ} (hg : 0 ≤ g) :
    min g (17*Real.sqrt g/8+3/16) ≤ 17/64 ↔ g ≤ 17/64 := by
  constructor
  · intro h
    by_contra! hn
    have hs : 1/2 < Real.sqrt g := by
      by_contra! hh
      have := mul_self_le_mul_self (Real.sqrt_nonneg g) hh
      nlinarith [Real.sq_sqrt hg]
    exact not_lt_of_ge h (lt_min hn (by linarith))
  · exact fun h => (min_le_left _ _).trans h

end YangMills.ElectricEndpoint
#print axioms YangMills.ElectricEndpoint.varianceIdentity
#print axioms YangMills.ElectricEndpoint.jointBudget
#print axioms YangMills.ElectricEndpoint.sphereLower
#print axioms YangMills.ElectricEndpoint.envelope
#print axioms YangMills.ElectricEndpoint.productBound
#print axioms YangMills.ElectricEndpoint.normBound
#print axioms YangMills.ElectricEndpoint.endpoint
#print axioms YangMills.ElectricEndpoint.retainWeight
#print axioms YangMills.ElectricEndpoint.combinedBand
#print axioms YangMills.ElectricEndpoint.crossover
#print axioms YangMills.ElectricEndpoint.budgetCrossover
