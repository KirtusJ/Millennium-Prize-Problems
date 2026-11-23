import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.Ring

open MeasureTheory Set

namespace Millennium.YangMills.D4.Adjoint

/-- For x in [-1,1], the squared vector-field multiplier is at most one. -/
theorem scoreMultiplier (u : ℝ) (hu : 0 ≤ u) (h1 : u ≤ 1) :
    (1 - 4*u/3)^2 ≤ 1 := by
  have h := mul_nonneg hu (show 0 ≤ 3/2 - u by linarith)
  nlinarith only [h]

/-- Denote sqrt(J) by y and sqrt(B) by k. The integrated one-link
divergence gives the score premise, and J ≤ 1/4 gives y ≤ 1/2. -/
theorem adjointFirstMoment {J y k κ : ℝ} (hκ : 0 < κ) (hy : 0 ≤ y)
    (hk : 0 ≤ k) (hhalf : y ≤ 1/2) (square : y^2 = J)
    (score : 1 ≤ 8*J + 4*k*y) :
    4*κ/(1+k)^2 ≤ 64*κ*J := by
  have h : 1 ≤ 4*y*(1+k) := by
    nlinarith only [score, square, mul_nonneg hy (sub_nonneg.mpr hhalf)]
  have hh := mul_self_le_mul_self (by norm_num : (0:ℝ) ≤ 1) h
  have h' : 1 ≤ 16*J*(1+k)^2 := by rw [← square]; nlinarith only [hh]
  apply (div_le_iff₀ (sq_pos_of_pos (by linarith : 0 < 1+k))).mpr
  nlinarith only [mul_nonneg hκ.le (sub_nonneg.mpr h')]

/-- The equal-time adjoint variance and the two first spectral moments
obey a common normalization identity. S=E(1-x²) and Z=E((1-x²)²). -/
theorem crossCharacterIdentity (S Z : ℝ) :
    16*(Z-S^2) + 16*(S-Z) = 4*(4*S)-(4*S)^2 := by ring

/-- The algebraic step in the square-observable commutator, in any real operator algebra. -/
theorem squareCommutator {R : Type*} [Ring R] (H F : R) :
    H*(F*F)-(F*F)*H = F*(H*F-F*H)+F*(H*F-F*H)+((H*F-F*H)*F-F*(H*F-F*H)) := by
  noncomm_ring

/-- The multiplication-operator bounds for the fundamental plaquette and its
gradient give the adjoint second moment after the product rule. -/
theorem adjointGraphNorm {X : Type*} [SeminormedAddCommGroup X] [NormedSpace ℝ X]
    (state inserted fund grad : X) {κ C : ℝ} (hκ : 0 ≤ κ)
    (identity : state = (2:ℝ) • inserted - (κ/2) • grad)
    (multiplier : ‖inserted‖ ≤ 2*‖fund‖) (gradient : ‖grad‖ ≤ 16)
    (cap : ‖fund‖ ≤ κ*C) : ‖state‖ ≤ κ*(4*C+8) := by
  rw [identity]
  have h := norm_sub_le ((2:ℝ) • inserted) ((κ/2) • grad)
  have hhalf : 0 ≤ κ/2 := by positivity
  simp only [norm_smul, Real.norm_eq_abs, abs_of_nonneg (by norm_num : (0:ℝ) ≤ 2),
    abs_of_nonneg hhalf] at h
  nlinarith only [h, multiplier, cap, mul_le_mul_of_nonneg_left gradient hhalf]

/-- Four target links and twelve one-link neighbors yield the total coefficient
in the fundamental magnetic double commutator in the unit-round metric. -/
theorem magneticCount (S : ℝ) : 128*S + 12*(4*S+16*S) = 368*S := by ring

/-- Polynomial minorant of the closed-band indicator; no support condition on E. -/
theorem quadraticMinorant (E L U : ℝ) (hL : 0 ≤ L) (hLU : L ≤ U) :
    (U+L)*E-E^2-L*U ≤ (Icc L U).indicator (fun _ => U^2/4) E := by
  by_cases inside : E ∈ Icc L U
  · rw [indicator_of_mem inside]
    nlinarith only [sq_nonneg (2*E-U), mul_nonneg hL (sub_nonneg.mpr inside.2)]
  · rw [indicator_of_not_mem inside]
    rcases le_total E L with h | h
    · nlinarith only [mul_nonneg (sub_nonneg.mpr h) (sub_nonneg.mpr (h.trans hLU))]
    · have eU : U ≤ E := le_of_not_ge (fun hU => inside ⟨h,hU⟩)
      nlinarith only [mul_nonneg (sub_nonneg.mpr h) (sub_nonneg.mpr eU)]

/-- Integrating the quadratic certificate controls the window by two moments and total mass. -/
theorem quadraticBand (μ : Measure ℝ) [IsFiniteMeasure μ] {L U : ℝ}
    (hL : 0 ≤ L) (hLU : L ≤ U) (h₁ : Integrable (fun E : ℝ => E) μ)
    (h₂ : Integrable (fun E : ℝ => E^2) μ) :
    (U+L)*(∫ E, E ∂μ) - (∫ E : ℝ, E^2 ∂μ) - L*U*μ.real univ
      ≤ (U^2/4)*μ.real (Icc L U) := by
  have hlin := h₁.const_mul (U+L)
  have hc := integrable_const (L*U) (μ := μ)
  have hind := (integrable_const (U^2/4) (μ := μ)).indicator (measurableSet_Icc (a := L) (b := U))
  have h := integral_mono ((hlin.sub h₂).sub hc) hind (fun E => quadraticMinorant E L U hL hLU)
  have split := integral_sub (hlin.sub h₂) hc
  simp only [Pi.sub_apply] at h split
  rw [split, integral_sub hlin h₂, integral_const_mul, integral_const,
    integral_indicator_const _ measurableSet_Icc] at h
  simpa only [smul_eq_mul, mul_comm (μ.real univ) (L*U), mul_comm (μ.real (Icc L U)) (U^2/4)] using h

/-- A smaller static variance permits a larger lower endpoint at the same weight.
The caller chooses L with L times the total mass at most A/4. -/
theorem massCapBand (μ : Measure ℝ) [IsFiniteMeasure μ] {L A D : ℝ}
    (hA : 0 < A) (hD : 0 < D) (hL : 0 ≤ L) (ordered : L ≤ 2*D/A)
    (lowMass : L*μ.real univ ≤ A/4)
    (h₁ : Integrable (fun E : ℝ => E) μ) (h₂ : Integrable (fun E : ℝ => E^2) μ)
    (first : A ≤ ∫ E, E ∂μ) (second : (∫ E : ℝ, E^2 ∂μ) ≤ D) :
    A^2/(2*D) ≤ μ.real (Icc L (2*D/A)) := by
  let U := 2*D/A
  have hU : 0 < U := by dsimp [U]; positivity
  have hUA : U*A = 2*D := by dsimp [U]; field_simp
  have c := quadraticBand μ (L := L) (U := U) hL ordered h₁ h₂
  have b : D/2 ≤ (U^2/4) * μ.real (Icc L U) := by
    have f := mul_le_mul_of_nonneg_left first (add_nonneg hU.le hL)
    have v := mul_le_mul_of_nonneg_left lowMass hU.le
    nlinarith only [c,f,v,second,hUA,mul_nonneg hL hA.le]
  calc
    A^2/(2*D) = (D/2)/(U^2/4) := by dsimp [U]; field_simp; ring
    _ ≤ _ := (div_le_iff₀ (by positivity : 0 < U^2/4)).mpr (by linarith only [b])

/-- At mass ≤ 4, halve the former upper endpoint and quadruple the guaranteed mass. -/
theorem improvedBand (μ : Measure ℝ) [IsFiniteMeasure μ] {A D : ℝ}
    (hA : 0 < A) (hD : 0 < D) (cap : μ.real univ ≤ 4)
    (h₁ : Integrable (fun E : ℝ => E) μ) (h₂ : Integrable (fun E : ℝ => E^2) μ)
    (first : A ≤ ∫ E, E ∂μ) (second : (∫ E : ℝ, E^2 ∂μ) ≤ D) :
    A^2/(2*D) ≤ μ.real (Icc (A/16) (2*D/A)) := by
  let L := A/16
  let U := 2*D/A
  have hL : 0 < L := by dsimp [L]; positivity
  have hLA : 16*L = A := by dsimp [L]; ring
  have comp : A^2/4 ≤ D := by
    have linear := h₁.const_mul (A/2)
    have constTerm := integrable_const (A^2/16) (μ := μ)
    have v := integral_mono linear (h₂.add constTerm)
      (fun E => show A/2*E ≤ E^2 + A^2/16 by nlinarith only [sq_nonneg (E-A/4)])
    simp only [Pi.add_apply] at v
    rw [integral_const_mul, integral_add h₂ constTerm, integral_const] at v
    simp only [smul_eq_mul] at v
    nlinarith only [v, second, mul_le_mul_of_nonneg_left first (by positivity : 0 ≤ A/2),
      mul_le_mul_of_nonneg_right cap (by positivity : 0 ≤ A^2/16)]
  have ordered : L ≤ U := by
    dsimp [L,U]
    apply (le_div_iff₀ hA).mpr
    nlinarith only [comp, hD]
  apply massCapBand μ hA hD hL.le ordered _ h₁ h₂ first second
  nlinarith only [mul_le_mul_of_nonneg_left cap hL.le, hLA]

open Filter
open scoped Topology

/-- Choose a temporal refinement at each volume for countably many measured
correlations. Every eventually finer choice reproduces all the same limits. -/
theorem jointSelection (raw : ℕ → ℕ → ℕ → ℝ) (model : ℕ → ℕ → ℝ) (target : ℕ → ℝ)
    (fixed : ∀ n i, Tendsto (fun j => raw n j i) atTop (𝓝 (model n i)))
    (volume : ∀ i, Tendsto (fun n => model n i) atTop (𝓝 (target i))) :
    ∃ cut : ℕ → ℕ, (∀ n, n ≤ cut n) ∧
      ∀ j : ℕ → ℕ, (∀ᶠ n in atTop, cut n ≤ j n) →
        ∀ i, Tendsto (fun n => raw n (j n) i) atTop (𝓝 (target i)) := by
  have row (n : ℕ) : ∃ J : ℕ, ∀ j ≥ J, ∀ i ∈ Finset.range (n+1),
      dist (raw n j i) (model n i) < 1 / ((n:ℝ)+1) := by
    apply eventually_atTop.mp
    apply (eventually_all_finset _).mpr
    intro i _
    exact (Metric.tendsto_nhds.mp (fixed n i) _ (by positivity))
  choose J hJ using row
  refine ⟨fun n => max n (J n), fun n => le_max_left _ _, ?_⟩
  intro j fine i
  apply Metric.tendsto_nhds.mpr
  intro ε hε
  have small := (tendsto_one_div_add_atTop_nhds_zero_nat.eventually_lt_const (half_pos hε))
  have close := Metric.tendsto_nhds.mp (volume i) (ε/2) (half_pos hε)
  filter_upwards [fine, eventually_ge_atTop i, small, close] with n hcut hni hn hc
  have a := hJ n (j n) ((le_max_right _ _).trans hcut) i (Finset.mem_range.mpr (Nat.lt_succ_of_le hni))
  exact (dist_triangle _ (model n i) _).trans_lt (by linarith only [a,hn,hc])

/-- A prescribed diagonal can miss every fixed-volume limit, even if each
cell is the unit-time observation of a positive one-atom transfer measure. -/
theorem prescribedDiagonalFails :
    (∀ n : ℕ, Tendsto (fun j : ℕ => if n < j then (1:ℝ)/2 else 1) atTop (𝓝 (1/2))) ∧
    (∀ n : ℕ, (if n < n then (1:ℝ)/2 else 1) = 1) := by
  constructor
  · intro n
    apply Tendsto.congr' _ (tendsto_const_nhds (x := (1:ℝ)/2))
    filter_upwards [eventually_gt_atTop n] with j hj
    simp [hj]
  · intro n
    simp

-- BEGIN PCP OS generated spherical divergence
theorem sphericalDivergence (x : ℝ) :
    (1-x^2)*(1-12*x^2/3) - 3*x*(x-4*x^3/3) = 1-8*x^2*(1-x^2) := by ring

#print axioms scoreMultiplier
#print axioms adjointFirstMoment
#print axioms crossCharacterIdentity
#print axioms squareCommutator
#print axioms adjointGraphNorm
#print axioms magneticCount
#print axioms quadraticMinorant
#print axioms quadraticBand
#print axioms massCapBand
#print axioms improvedBand
#print axioms jointSelection
#print axioms prescribedDiagonalFails
#print axioms sphericalDivergence

end Millennium.YangMills.D4.Adjoint
