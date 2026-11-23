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

/-- Row and column control of a nonnegative Green kernel bounds its quadratic form. -/
theorem schurForm {ι : Type*} [Fintype ι] (D : ι → ι → ℝ) (v : ι → ℝ) (K : ℝ)
    (hD : ∀ i j, 0 ≤ D i j) (hr : ∀ i, ∑ j, D i j ≤ K)
    (hc : ∀ j, ∑ i, D i j ≤ K) :
    ∑ i, ∑ j, D i j * (v i * v j) ≤ K * ∑ i, (v i)^2 := by
  let sq := fun i => (v i)^2
  have row : ∑ i, ∑ j, D i j * sq i ≤ K * ∑ i, sq i := by
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro i _
    rw [← Finset.sum_mul]
    exact mul_le_mul_of_nonneg_right (hr i) (sq_nonneg _)
  have col : ∑ i, ∑ j, D i j * sq j ≤ K * ∑ j, sq j := by
    rw [Finset.sum_comm, Finset.mul_sum]
    apply Finset.sum_le_sum
    intro j _
    rw [← Finset.sum_mul]
    exact mul_le_mul_of_nonneg_right (hc j) (sq_nonneg _)
  have both : ∑ i, ∑ j, (D i j * (v i * v j) + D i j * (v i * v j)) ≤
      ∑ i, ∑ j, (D i j * sq i + D i j * sq j) := by
    apply Finset.sum_le_sum
    intro i _
    apply Finset.sum_le_sum
    intro j _
    dsimp [sq]
    nlinarith only [mul_nonneg (hD i j) (sq_nonneg (v i - v j))]
  simp only [Finset.sum_add_distrib] at both
  change _ ≤ K * ∑ i, sq i
  linarith only [row, col, both]

/-- The squared one-edge oscillation bound for two incident smeared traces. -/
theorem pairOscillation (c d : ℝ) :
    (4*(|c|+|d|))^2 ≤ 32*(c^2+d^2) := by
  nlinarith only [sq_nonneg (|c|-|d|), sq_abs c, sq_abs d]

/-- At an earlier positive time the correlator itself controls the late moment. -/
theorem laterMomentPoint {x r : ℝ} (hx : 0 ≤ x) (hr : x ≤ r) (n k : ℕ) :
    x^(n+k) ≤ r^k * x^n := by
  rw [pow_add, mul_comm (x^n)]
  exact mul_le_mul_of_nonneg_right (pow_le_pow_left₀ hx hr _) (pow_nonneg hx _)

/-- Eliminate the weight h between the two strictly contracting rows. -/
theorem twoRowWeight {a b c d : ℝ} (hb : 0 < b) (hc : 0 < c) (hd : d < 1) :
    (∃ h : ℝ, 0 < h ∧ a+b*h < 1 ∧ c+d*h < h) ↔ b*c < (1-a)*(1-d) := by
  have h₀ : 0 < 1-d := sub_pos.mpr hd
  have interval : c/(1-d) < (1-a)/b ↔ b*c < (1-a)*(1-d) := by
    rw [div_lt_div_iff₀ h₀ hb, mul_comm c b]
  constructor
  · rintro ⟨h, _, hs, ht⟩
    apply interval.mp
    apply lt_trans (b := h)
    · exact (div_lt_iff₀ h₀).2 (by linarith)
    · exact (lt_div_iff₀ hb).2 (by linarith)
  · intro ok
    obtain ⟨h, hl, hu⟩ := exists_between (interval.mpr ok)
    have pos := (div_pos hc h₀).trans hl
    have left := (div_lt_iff₀ h₀).1 hl
    have right := (lt_div_iff₀ hb).1 hu
    exact ⟨h, pos, by linarith, by linarith⟩

/-- Exact criterion for the spatial/temporal influence majorant at a positive time tilt. -/
theorem wilsonTiltIff {s t R : ℝ} (ht : 0 < t) (h6 : 6*t < 1) (hR : 0 < R) :
    (∃ h : ℝ, 0 < h ∧ spatial s t R h < 1 ∧ temporal t R h < h) ↔
      (t+6*t^2)*(R+1/R) < (1-12*s)*(1-6*t)-24*t^2 := by
  unfold spatial temporal
  rw [twoRowWeight (by positivity) (by positivity) h6]
  have det : (1-(12*s+t*(R+1/R)))*(1-6*t) - (2*t*(1+1/R))*(6*t*(1+R)) =
      (1-12*s)*(1-6*t)-24*t^2 - (t+6*t^2)*(R+1/R) := by
    field_simp [ne_of_gt hR]
    ring
  constructor <;> intro h <;> linarith only [h, det]

/-- The sharp comparison threshold on the isotropic endpoint. Strictness is necessary. -/
theorem isotropicTiltEnd {R : ℝ} (hR : 1 ≤ R) :
    (∃ h : ℝ, 0 < h ∧ spatial (1/20) (1/20) R h < 1 ∧ temporal (1/20) R h < h) ↔
      R < (22+3*Real.sqrt 35)/13 := by
  have pos : 0 < R := by linarith
  rw [wilsonTiltIff (by norm_num) (by norm_num) pos]
  have cancel : (R+1/R)*R = R^2+1 := by
    field_simp [ne_of_gt pos]
    ring
  have square := Real.sq_sqrt (by norm_num : 0 ≤ (35 : ℝ))
  have root : 5 < Real.sqrt 35 := by nlinarith only [square, Real.sqrt_nonneg 35]
  have plus : 0 < 13*R-22+3*Real.sqrt 35 := by linarith
  have factor : (13*R-22+3*Real.sqrt 35)*(13*R-22-3*Real.sqrt 35) =
      13*(13*R^2-44*R+13) := by nlinarith only [square]
  calc
    _ ↔ R+1/R < 44/13 := by constructor <;> intro h <;> linarith only [h]
    _ ↔ 13*R^2-44*R+13 < 0 := by
      rw [← mul_lt_mul_iff_of_pos_right pos]
      constructor <;> intro h <;> linarith only [h, cancel]
    _ ↔ (13*R-22+3*Real.sqrt 35)*(13*R-22-3*Real.sqrt 35) < 0 := by
      rw [factor]
      constructor <;> intro h <;> linarith only [h]
    _ ↔ _ := by
      constructor
      · intro h
        linarith only [Left.neg_of_mul_neg_right h plus.le]
      · intro h
        exact mul_neg_of_pos_of_neg plus (by linarith only [h])

/-- The rational interior tilt supplied at rendezvous gives two strictly subunit ratios. -/
theorem rationalInteriorRows :
    spatial (1/20) (1/20) (61/20) (869/500) = 609803/610000 ∧
    temporal (1/20) (61/20) (869/500) / (869/500) = 4341/4345 := by
  norm_num [spatial, temporal]

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

#print axioms rationalInteriorRows
#print axioms twoRowWeight
#print axioms wilsonTiltIff
#print axioms isotropicTiltEnd
#print axioms likelihoodBound
#print axioms greenBound
#print axioms rowsThree
#print axioms noRowsFour
#print axioms obstructionAtTwoFifteenths
#print axioms noDiagonalContraction
#print axioms schurForm
#print axioms pairOscillation
#print axioms laterMomentPoint
#print axioms continuumVanishes
end Millennium.YangMills.WilsonInfluence
