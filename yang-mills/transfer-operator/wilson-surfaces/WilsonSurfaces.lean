import Mathlib.Analysis.Convex.Integral
import Mathlib.Analysis.Convex.Mul
import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.YangMills.WilsonSurfaces
open Finset MeasureTheory
open scoped InnerProductSpace

/-- A free sign change pairs the two values of a center character. -/
theorem centerCancellation {X : Type*} [Fintype X] (s : X → ℝ) (flip : X ≃ X)
    (changes : ∀ x, s (flip x) = -s x) : ∑ x, s x = 0 := by
  have h := Equiv.sum_comp flip s
  simp only [changes, Finset.sum_neg_distrib] at h
  linarith

/-- A nonnegative active-constraint probability is bounded by its largest allowed odds. -/
theorem activeOdds {u w : ℝ} (hu : 0 ≤ u) (hw : u ≤ w) :
    u/(1+u) ≤ w/(1+w) := by
  apply (div_le_div_iff₀ (by linarith) (by linarith)).2
  linarith

/-- A path of planar slices controls its change between endpoints. -/
theorem sliceWalk {E : Type*} [PseudoMetricSpace E] (s : ℕ → E) (n : ℕ) :
    dist (s 0) (s n) ≤ ∑ i ∈ range n, dist (s i) (s (i+1)) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [sum_range_succ]
    exact (dist_triangle (s 0) (s n) (s (n+1))).trans (add_le_add_right ih _)

/-- The least-perimeter slice gives a flat competitor in a return path. -/
theorem flatCompetitor {outward inward dist wall k p : ℝ}
    (ho : dist ≤ outward) (hi : dist ≤ inward) (hw : k*p ≤ wall) :
    2*dist+k*p ≤ outward+inward+wall := by linarith

/-- Count occupied rows and columns of a rectangle before multiplying by lengths. -/
theorem rectangleRatio {n m rows cols z p : ℝ} (hn : 0 ≤ n) (hm : 0 ≤ m)
    (hr : z ≤ n*rows) (hc : z ≤ m*cols) (hp : 2*(rows+cols) ≤ p) :
    2*(n+m)*z ≤ (n*m)*p := by
  have r := mul_le_mul_of_nonneg_left hr hm
  have c := mul_le_mul_of_nonneg_left hc hn
  have h := mul_le_mul_of_nonneg_left hp (mul_nonneg hn hm)
  linarith only [r,c,h]

/-- Exact lower envelope after slicing a cylinder joining parallel rectangular contours. -/
theorem surfaceMinimum {A P z k cost : ℝ} (hA : 0 < A) (hz : 0 ≤ z) (hza : z ≤ A)
    (budget : 2*A*(A-z)+k*P*z ≤ A*cost) : min (2*A) (k*P) ≤ cost := by
  by_cases h : 2*A ≤ k*P
  · rw [min_eq_left h]
    have q := mul_le_mul_of_nonneg_right h hz
    apply le_of_mul_le_mul_left (a := A) _ hA
    linarith only [q,budget]
  · rw [min_eq_right (le_of_not_ge h)]
    have q := mul_le_mul_of_nonneg_right (le_of_not_ge h) (sub_nonneg.mpr hza)
    apply le_of_mul_le_mul_left (a := A) _ hA
    linarith only [q,budget]

/-- A nonempty cell set filling all of its occupied rows and columns is the whole rectangle. -/
theorem fullRectangle {X Y : Type*} (s : Set (X × Y)) (nonempty : s.Nonempty)
    (row : ∀ x y, (x,y) ∈ s → ∀ u, (u,y) ∈ s)
    (col : ∀ x y, (x,y) ∈ s → ∀ v, (x,v) ∈ s) : s = Set.univ := by
  rcases nonempty with ⟨⟨x,y⟩,h⟩
  apply Set.eq_univ_iff_forall.mpr
  rintro ⟨u,v⟩
  exact col u y (row x y h u) v

/-- Quantitative control on division by the square of the leading ordinary loop mean. -/
theorem relativeRemainder {a b δ : ℝ} (hδ : 0 ≤ δ) (small : δ ≤ 1/2)
    (ha : |a| ≤ δ) (hb : |b| ≤ δ) :
    |(1+b)/(1+a)^2-1| ≤ 14*δ := by
  have aa := abs_le.mp ha
  have ab := abs_le.mp hb
  have hpos : 0 < (1+a)^2 := sq_pos_of_pos (by linarith)
  have denom : 1/4 ≤ (1+a)^2 := by
    have h := mul_self_le_mul_self (show (0:ℝ) ≤ 1/2 by norm_num) (show 1/2 ≤ 1+a by linarith)
    nlinarith only [h]
  have weight := mul_le_mul_of_nonneg_left denom (show 0 ≤ 14*δ by positivity)
  have aa2 : a^2 ≤ δ/2 := by
    have h := mul_self_le_mul_self (abs_nonneg a) ha
    have j := mul_le_mul_of_nonneg_left small hδ
    nlinarith only [h,j,sq_abs a]
  rw [abs_le]
  constructor
  · apply (le_sub_iff_add_le).2
    apply (le_div_iff₀ hpos).2
    linarith only [weight,aa2,aa.2,ab.1]
  · apply (sub_le_iff_le_add).2
    apply (div_le_iff₀ hpos).2
    linarith only [weight,sq_nonneg a,aa.1,ab.2,hδ]

/-- Positivity after subtracting a known eigenline from a symmetric real operator. -/
theorem eigenlineFloor {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
    (K : E →ₗ[ℝ] E) (v e : E) (r : ℝ) (unit : ⟪e,e⟫_ℝ = 1)
    (eigen : K e = r • e) (symm : ∀ x y, ⟪x,K y⟫_ℝ = ⟪K x,y⟫_ℝ)
    (pos : ∀ x, 0 ≤ ⟪x,K x⟫_ℝ) : r * ⟪e,v⟫_ℝ^2 ≤ ⟪v,K v⟫_ℝ := by
  have h := pos (v - ⟪e,v⟫_ℝ • e)
  have ev : ⟪e,K v⟫_ℝ = r*⟪e,v⟫_ℝ := by rw [symm,eigen,real_inner_smul_left]
  rw [map_sub, map_smul, eigen] at h
  simp only [inner_sub_left, inner_sub_right, real_inner_smul_right, real_inner_smul_left,
    unit, ev, real_inner_comm v e] at h
  rw [real_inner_comm v e]
  linarith only [h]

/-- A probability spectral measure gives a lower bound at every integer time. -/
theorem spectralMoment {X : Type*} [MeasurableSpace X] (μ : Measure X) [IsProbabilityMeasure μ]
    (f : X → ℝ) (hf : ∀ᵐ x ∂μ, 0 ≤ f x) (hi : Integrable f μ)
    (k : ℕ) (hk : Integrable (fun x => f x ^ k) μ) :
    (∫ x, f x ∂μ)^k ≤ ∫ x, f x^k ∂μ :=
  (convexOn_pow k).map_integral_le (continuous_id.pow k).continuousOn isClosed_Ici hf hi hk

/-- A pointwise lower comparison propagates through a nonnegative exterior kernel. -/
theorem positiveSandwich {ι : Type*} (s : Finset ι) (K : ι → ι → ℝ) (u w : ι → ℝ)
    (c : ℝ) (hc : 0 ≤ c) (hw : ∀ i, 0 ≤ w i) (hk : ∀ i j, 0 ≤ K i j)
    (floor : ∀ i, c*w i ≤ u i) :
    ∑ i ∈ s, ∑ j ∈ s, K i j*((c*w i)*(c*w j)) ≤ ∑ i ∈ s, ∑ j ∈ s, K i j*(u i*u j) := by
  apply Finset.sum_le_sum
  intro i _
  apply Finset.sum_le_sum
  intro j _
  exact mul_le_mul_of_nonneg_left (mul_le_mul (floor i) (floor j) (mul_nonneg hc (hw j))
    ((mul_nonneg hc (hw i)).trans (floor i))) (hk i j)

-- PCP begin geometry
theorem surfaceCount (n : ℕ) : 6+36*n ≤ 42*(n+1) := by omega
-- PCP end geometry

-- PCP begin certificate
theorem animalRate {p : ℝ} (hp : 0 ≤ p) (small : 384*p ≤ 1/4) :
    0 ≤ 768*p ∧ 768*p ≤ 1/2 := by constructor <;> linarith
theorem threeSquare (k : ℕ) (hk : 0 < k) :
    min 18 (12*k) = if k = 1 then 12 else 18 := by split <;> omega
-- PCP end certificate

/-- Pass the extreme surface estimates to the logarithmic scale. -/
theorem normalizedRate {A T D j m err : ℝ}
    (area : D = min (2*A) T) (single : |m+A| ≤ err) (joint : |j+D| ≤ err) :
    |(j-2*m)-max 0 (2*A-T)| ≤ 3*err := by
  rw [abs_le] at single joint ⊢
  by_cases h : 2*A ≤ T
  · rw [min_eq_left h] at area
    rw [max_eq_left (by linarith)]
    constructor <;> linarith
  · rw [min_eq_right (le_of_not_ge h)] at area
    rw [max_eq_right (by linarith)]
    constructor <;> linarith

/-- Tilting towards the future exponentially penalizes energy below a proposed slope. -/
theorem lowBand {ι : Type*} (s : Finset ι) (w E : ι → ℝ) {R h : ℝ}
    (hh : 0 ≤ h) (hw : ∀ i ∈ s, 0 ≤ w i) (he : ∀ i ∈ s, E i ≤ R) :
    Real.exp (-h*R)*(∑ i ∈ s, w i) ≤ ∑ i ∈ s, w i * Real.exp (-h*E i) := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  rw [mul_comm]
  exact mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr
    (mul_le_mul_of_nonpos_left (he i hi) (neg_nonpos.mpr hh))) (hw i hi)

/-- Tilting back towards time zero controls the upper band. -/
theorem highBand {ι : Type*} (s : Finset ι) (w E : ι → ℝ) {R h : ℝ}
    (hh : 0 ≤ h) (hw : ∀ i ∈ s, 0 ≤ w i) (he : ∀ i ∈ s, R ≤ E i) :
    Real.exp (h*R)*(∑ i ∈ s, w i) ≤ ∑ i ∈ s, w i * Real.exp (h*E i) := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i hi
  rw [mul_comm]
  exact mul_le_mul_of_nonneg_left (Real.exp_le_exp.mpr
    (mul_le_mul_of_nonneg_left (he i hi) hh)) (hw i hi)

/-- Oscillation bounds on a joint relative density control signed test integrals. -/
theorem densityBias {X : Type*} [MeasurableSpace X] (μ : Measure X) (f d : X → ℝ)
    (ε : ℝ) (hi : Integrable f μ) (hid : Integrable (fun x => f x*(d x-1)) μ)
    (bound : ∀ x, |d x-1| ≤ ε) :
    |∫ x, f x*(d x-1) ∂μ| ≤ ε * ∫ x, |f x| ∂μ := by
  rw [← integral_const_mul]
  refine (abs_integral_le_integral_abs).trans ?_
  apply integral_mono hid.abs (hi.abs.const_mul ε)
  intro x
  change |f x*(d x-1)| ≤ ε*|f x|
  rw [abs_mul, mul_comm ε]
  exact mul_le_mul_of_nonneg_left (bound x) (abs_nonneg _)

/-- Multiplying pointwise near-independence bounds preserves positive insertion ratios. -/
theorem positiveRatio {a b F G J : ℝ} (hF : 0 < F) (hG : 0 < G)
    (lo : a*(F*G) ≤ J) (hi : J ≤ b*(F*G)) : a ≤ J/(F*G) ∧ J/(F*G) ≤ b :=
  ⟨(le_div_iff₀ (mul_pos hF hG)).2 lo, (div_le_iff₀ (mul_pos hF hG)).2 hi⟩

#print axioms fullRectangle
#print axioms relativeRemainder
#print axioms threeSquare
#print axioms lowBand
#print axioms highBand
#print axioms densityBias
#print axioms centerCancellation
#print axioms activeOdds
#print axioms sliceWalk
#print axioms flatCompetitor
#print axioms rectangleRatio
#print axioms surfaceMinimum
#print axioms eigenlineFloor
#print axioms spectralMoment
#print axioms positiveSandwich
#print axioms surfaceCount
#print axioms animalRate
#print axioms normalizedRate
#print axioms positiveRatio

end Millennium.YangMills.WilsonSurfaces
