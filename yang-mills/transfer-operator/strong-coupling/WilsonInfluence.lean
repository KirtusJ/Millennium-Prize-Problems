import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Data.Real.Pi.Bounds
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Finite parts of the Wilson-link comparison argument. The Gibbs comparison
theorem, incidence formulas and transfer representation are identified in the note. -/
noncomputable section
namespace Millennium.YangMills.WilsonInfluence

/-- Algebra behind the sharp total-variation upper bound when the likelihood
ratio has endpoints a and b = a*k². The chord inequality is applied before this step. -/
theorem likelihoodBound {a k : ℝ} (ha : 0 < a) (hk : 1 < k) :
    ((a*k^2-1)*(1-a))/(a*k^2-a) ≤ (k-1)/(k+1) := by
  have hb : 0 < a*k^2-a := by
    nlinarith only [mul_pos ha (mul_pos (sub_pos.mpr hk) (show 0 < k+1 by linarith))]
  apply (div_le_div_iff₀ hb (by linarith : 0 < k+1)).2
  nlinarith only [mul_nonneg (show 0 ≤ k+1 by linarith) (sq_nonneg (a*k-1))]

/-- One additional application of a finite influence matrix. -/
def step {ι : Type*} [Fintype ι] (C : ι → ι → ℝ) (f : ι → ℝ) (i : ι) : ℝ :=
  ∑ j, C i j * f j

/-- The action of the first N+1 terms of the Neumann series, starting at the identity. -/
def green {ι : Type*} [Fintype ι] (C : ι → ι → ℝ) (f : ι → ℝ) : ℕ → ι → ℝ
  | 0 => f
  | n + 1 => fun i => f i + step C (green C f n) i

/-- A positive supersolution bounds every partial Green sum, on every finite link set. -/
theorem greenBound {ι : Type*} [Fintype ι] (C : ι → ι → ℝ) (b w : ι → ℝ)
    (k : ℝ) (hk : 1 ≤ k) (hw : ∀ i, 0 ≤ w i) (hC : ∀ i j, 0 ≤ C i j)
    (hb : ∀ i, b i ≤ w i)
    (hrow : ∀ i, k * step C w i ≤ (k-1) * w i) :
    ∀ n i, green C b n i ≤ k * w i := by
  intro n
  induction n with
  | zero =>
    intro i
    exact (hb i).trans (le_mul_of_one_le_left (hw i) hk)
  | succ n ih =>
    intro i
    have bound : step C (green C b n) i ≤ step C (fun j => k*w j) i :=
      Finset.sum_le_sum fun j _ => mul_le_mul_of_nonneg_left (ih j) (hC i j)
    have pull : step C (fun j => k*w j) i = k * step C w i := by
      unfold step
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j _
      ring
    change b i + step C (green C b n) i ≤ k * w i
    linarith only [hb i, bound, pull, hrow i]

/-- Time is anchored at the starting vertex of each positive-oriented link. -/
-- PCP begin stencil
def spatial (s t R h : ℝ) : ℝ := 12*s + t*(R+1/R) + 2*t*(1+1/R)*h
def temporal (t R h : ℝ) : ℝ := 6*t*(1+R) + 6*t*h
-- PCP end stencil

-- PCP begin witness
def height : ℝ := 26/15

/-- R = 3 works for all s,t up to 1/20. The second row is unnormalized. -/
theorem rowsThree {s t : ℝ} (hs : s ≤ 1/20) (ht : t ≤ 1/20) :
    450*spatial s t 3 height ≤ 449 ∧ 450*temporal t 3 height ≤ 449*height := by
  unfold spatial temporal height
  constructor <;> linarith only [hs, ht]
-- PCP end witness

/-- Open certificate boundary: a fourfold tilt fails at the endpoint of that rectangle. -/
theorem noRowsFour : ¬ ∃ h : ℝ, 0 < h ∧ spatial (1/20) (1/20) 4 h < 1 ∧
    temporal (1/20) 4 h < h := by
  rintro ⟨h, _, h₁, h₂⟩
  unfold spatial at h₁
  unfold temporal at h₂
  linarith

/-- If the elementary integral estimate holds for an adjacent link, summing
eighteen genuine influences is already too large at beta = 2/15. -/
theorem obstructionAtTwoFifteenths {d : ℝ}
    (hlower : (2/15 : ℝ) * (4/(3*Real.pi)) * (1-(2/15 : ℝ)^2/2) ≤ d) :
    1 < 18*d := by
  have hpi : 0 < 3*Real.pi := by positivity
  have hnum : (1/18 : ℝ) * (3*Real.pi) <
      (2/15 : ℝ)*4*(1-(2/15 : ℝ)^2/2) := by linarith only [Real.pi_lt_d4]
  have h : (1/18 : ℝ) < (2/15 : ℝ)*4*(1-(2/15 : ℝ)^2/2)/(3*Real.pi) :=
    (lt_div_iff₀ hpi).2 hnum
  have heq : (2/15 : ℝ)*4*(1-(2/15 : ℝ)^2/2)/(3*Real.pi) =
      (2/15 : ℝ)*(4/(3*Real.pi))*(1-(2/15 : ℝ)^2/2) := by ring
  linarith only [h, heq, hlower]

/-- Positive diagonal weights cannot restore strict contraction if every unweighted row exceeds one. -/
theorem noDiagonalContraction {ι : Type*} [Fintype ι] [Nonempty ι]
    (C : ι → ι → ℝ) (hC : ∀ i j, 0 ≤ C i j) (hsum : ∀ i, 1 < ∑ j, C i j)
    (w : ι → ℝ) (hw : ∀ i, 0 < w i) : ∃ i, w i < step C w i := by
  obtain ⟨i, hi⟩ := Finite.exists_min w
  refine ⟨i, ?_⟩
  calc
    w i = 1 * w i := (one_mul _).symm
    _ < (∑ j, C i j) * w i := mul_lt_mul_of_pos_right (hsum i) (hw i)
    _ = ∑ j, C i j * w i := Finset.sum_mul ..
    _ ≤ step C w i := Finset.sum_le_sum fun j _ => mul_le_mul_of_nonneg_left (hi j) (hC i j)

open Filter Topology

/-- A fixed transfer contraction loses every uniformly bounded connected
correlation at a positive physical separation when the number of steps diverges. -/
theorem continuumVanishes (C : ℕ → ℝ) (N : ℕ → ℕ) (B : ℝ)
    (hN : Tendsto N atTop atTop) (hC : ∀ j, |C j| ≤ B*(1/3 : ℝ)^(N j)) :
    Tendsto C atTop (𝓝 0) := by
  have hdec : Tendsto (fun j => B*(1/3 : ℝ)^(N j)) atTop (𝓝 0) := by
    simpa using (tendsto_const_nhds (x := B)).mul
      ((tendsto_pow_atTop_nhds_zero_of_lt_one (by norm_num : 0 ≤ (1/3 : ℝ)) (by norm_num)).comp hN)
  exact (tendsto_zero_iff_abs_tendsto_zero C).mpr (squeeze_zero (fun _ => abs_nonneg _) hC hdec)

#print axioms likelihoodBound
#print axioms greenBound
#print axioms rowsThree
#print axioms noRowsFour
#print axioms obstructionAtTwoFifteenths
#print axioms noDiagonalContraction
#print axioms continuumVanishes
end Millennium.YangMills.WilsonInfluence
