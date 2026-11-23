import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

open MeasureTheory Set
namespace Millennium.YangMills.D4.GraphHolonomies

/-- The pointwise density estimate uses the reciprocal against a common reference. -/
theorem reciprocalSecant (w δ : ℝ) (hw : 0 < w)
    (h : |w-1| ≤ δ) : (1-δ^2)/w ≤ 2-w := by
  apply (div_le_iff₀ hw).2
  rw [abs_le] at h
  nlinarith only [mul_nonneg (show 0 ≤ δ-(w-1) by linarith)
    (show 0 ≤ δ+(w-1) by linarith)]

/-- Integrating the secant gives the sharp single-channel reverse weight. -/
theorem reciprocalMean {X : Type*} [MeasurableSpace X] (μ : Measure X)
    [IsProbabilityMeasure μ] (w : X → ℝ) (δ : ℝ)
    (hp : ∀ x, 0 < w x) (h : ∀ x, |w x-1| ≤ δ)
    (hw : Integrable w μ) (hr : Integrable (fun x => 1/w x) μ)
    (mass : ∫ x, w x ∂μ = 1) :
    (1-δ^2)*(∫ x, 1/w x ∂μ) ≤ 1 := by
  rw [← integral_const_mul]
  have hh := integral_mono (hr.const_mul (1-δ^2)) ((integrable_const (2:ℝ)).sub hw)
    (fun x => (show (1-δ^2)*(1/w x) ≤ 2-w x by
      rw [mul_one_div]
      exact reciprocalSecant _ _ (hp x) (h x)))
  norm_num [integral_sub (integrable_const (2:ℝ)) hw, integral_const, mass] at hh ⊢
  exact hh

/-- For a finite channel the factors of these two arrays are the square-root
density residual and the weighted centered reading. -/
theorem reverseTest {X : Type*} (s : Finset X) (a b : X → ℝ) :
    (∑ x ∈ s, a x*b x)^2 ≤ (∑ x ∈ s, (a x)^2)*(∑ x ∈ s, (b x)^2) :=
  Finset.sum_mul_sq_le_sq_mul_sq s a b

/-- Total variance converts the reverse bound into lost exterior predictability. -/
theorem explainedVariance (P D W : ℝ) (h : P*D ≤ (1-P)*W) :
    D ≤ (1-P)*(D+W) := by nlinarith only [h]

theorem independentChannels (p : List ℝ) (h : ∀ x ∈ p, 0 ≤ x ∧ x ≤ 1) :
    1 - (p.map (fun x => 1-x)).prod ≤ p.sum := by
  induction p with
  | nil => simp
  | cons a p ih =>
    have ha := h a (by simp)
    have hp := ih (fun x hx => h x (List.mem_cons_of_mem a hx))
    simp only [List.map_cons,List.prod_cons,List.sum_cons]
    have hsum : 0 ≤ p.sum := List.sum_nonneg (fun x hx => (h x (List.mem_cons_of_mem a hx)).1)
    nlinarith only [mul_nonneg (show 0 ≤ 1-a by linarith) (sub_nonneg.mpr hp),
      mul_nonneg ha.1 hsum]

/-- Same-variance normalization of a positive transfer law gives its one-step tail. -/
theorem spectralThreshold (p corr t r : ℝ) (hr : 0 < r) (h : r*p ≤ corr)
    (hc : corr ≤ t) : p ≤ t/r := (le_div_iff₀ hr).2 (by linarith)

/-- The overlap argument bounds a representation's mean contraction in each
generator direction. Summation uses the Casimir lower estimate. -/
theorem casimirLoss (d : ℕ) (v : ℕ → ℝ) (q K : ℝ)
    (h : ∀ j < d, v j ≤ 8*(1-q^2))
    (hc : K ≤ ∑ j ∈ Finset.range d, v j) :
    K ≤ (d:ℝ)*8*(1-q^2) := by
  have hh := Finset.sum_le_sum (s := Finset.range d)
    (g := fun _ => 8*(1-q^2)) (fun i hi => h i (Finset.mem_range.mp hi))
  simp at hh
  nlinarith only [hc,hh]

/-- A staple of normalized length x at least one-half costs at most twice
its missing length in the reciprocal clock. -/
theorem goodClock (x : ℝ) (hx : 1/2 ≤ x) (h1 : x ≤ 1) :
    0 ≤ 1/x-1 ∧ 1/x-1 ≤ 2*(1-x) := by
  have hp : 0 < x := by linarith
  constructor
  · have hh : 1 ≤ 1/x := (le_div_iff₀ hp).2 (by linarith)
    linarith
  · have hh : 1/x ≤ 2*(1-x)+1 := (div_le_iff₀ hp).2 (by
      nlinarith only [mul_nonneg (show 0 ≤ 2*x-1 by linarith) (sub_nonneg.mpr h1)])
    linarith

theorem discardedClock (x : ℝ) (h : x ≤ 1/2) : (1:ℝ) ≤ 2*(1-x) := by linarith

/-- For a Lie-group heat factor or a transfer eigenvalue, one-step errors
accumulate additively when the remaining factors are contractions. -/
theorem productError (a b : ℕ → ℝ) (n : ℕ) (ha : ∀ i, |a i| ≤ 1)
    (hb : ∀ i, |b i| ≤ 1) :
    |(∏ i ∈ Finset.range n, a i)-(∏ i ∈ Finset.range n, b i)| ≤
       ∑ i ∈ Finset.range n, |a i-b i| := by
  induction n with
  | zero => simp
  | succ n ih =>
    let A := ∏ i ∈ Finset.range n, a i
    let B := ∏ i ∈ Finset.range n, b i
    have hbprod : |B| ≤ 1 := by
      dsimp [B]
      rw [Finset.abs_prod]
      exact Finset.prod_le_one (fun _ _ => abs_nonneg _) (fun i _ => hb i)
    simp only [Finset.prod_range_succ,Finset.sum_range_succ]
    change |A*a n-B*b n| ≤ _
    calc
      _ = |(A-B)*a n+B*(a n-b n)| := by ring_nf
      _ ≤ |(A-B)*a n|+|B*(a n-b n)| := abs_add_le _ _
      _ ≤ |A-B|+|a n-b n| := by
        rw [abs_mul,abs_mul]
        exact add_le_add (mul_le_of_le_one_right (abs_nonneg _) (ha n))
          (mul_le_of_le_one_left (abs_nonneg _) hbprod)
      _ ≤ _ := add_le_add_right ih _

/-- Finite multichannel variance accounting includes rare functions via a
reverse change of measure instead of an unweighted L1 test. -/
theorem varianceBudget (D W P : ℝ) (hp : 0 < P)
    (h : D ≤ (1/P-1)*W) : D ≤ (1-P)*(D+W) := by
  apply explainedVariance
  have hh := mul_le_mul_of_nonneg_left h hp.le
  have he : P*((1/P-1)*W)=(1-P)*W := by
    field_simp
  exact hh.trans_eq he

/-- Successive site reflections square the previous bad-event probability. -/
theorem reflectionDoubling (p : ℕ → ℝ) (hp : ∀ n, 0 ≤ p n)
    (step : ∀ n, (p n)^2 ≤ p (n+1)) (n : ℕ) : (p 0)^(2^n) ≤ p n := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ (2:ℕ),pow_mul]
    calc
      _ ≤ (p n)^2 := pow_le_pow_left₀ (pow_nonneg (hp 0) _) ih 2
      _ ≤ _ := step n

theorem sixStapleTime (β x : ℝ) (hb : β ≠ 0) (hx : x ≠ 0) :
    β/(2*(6*β*x)) - 1/12 = (1/x-1)/12 := by
  field_simp
  ring

theorem survivalAtMostOne (p : List ℝ) (h : ∀ x ∈ p, 0 ≤ x ∧ x ≤ 1) :
    (p.map (fun x => 1-x)).prod ≤ 1 := by
  induction p with
  | nil => simp
  | cons a p ih =>
    have ha := h a (by simp)
    have hp := ih (fun x hx => h x (List.mem_cons_of_mem a hx))
    simp only [List.map_cons,List.prod_cons]
    calc
      _ ≤ (1-a)*1 := mul_le_mul_of_nonneg_left hp (sub_nonneg.mpr ha.2)
      _ ≤ 1 := by linarith

/-- Second Bonferroni estimate for the attenuation of a path, including
  non-identical losses. The losses need no stochastic independence. -/
theorem lossExpansion (p : List ℝ) (h : ∀ x ∈ p, 0 ≤ x ∧ x ≤ 1) :
    0 ≤ p.sum-(1-(p.map (fun x => 1-x)).prod) ∧
    p.sum-(1-(p.map (fun x => 1-x)).prod) ≤ p.sum^2/2 := by
  induction p with
  | nil => simp
  | cons a p ih =>
    have ha := h a (by simp)
    have hp := ih (fun x hx => h x (List.mem_cons_of_mem a hx))
    have hP := survivalAtMostOne p (fun x hx => h x (List.mem_cons_of_mem a hx))
    simp only [List.sum_cons,List.map_cons,List.prod_cons]
    constructor
    · nlinarith only [hp.1,mul_nonneg ha.1 (sub_nonneg.mpr hP)]
    · nlinarith only [hp.2,mul_nonneg ha.1 hp.1,sq_nonneg a]

theorem stapleDispersion (x : ℝ) : (1-x)-(1-x^2)/2=(1-x)^2/2 := by ring

theorem reciprocalDispersion (x : ℝ) (hx : 1/2 ≤ x) :
    0 ≤ (1/x-1)-(1-x^2)/2 ∧ (1/x-1)-(1-x^2)/2 ≤ 3*(1-x)^2 := by
  have hp : 0 < x := by linarith
  have he : (1/x-1)-(1-x^2)/2=(1-x)^2*((2+x)/(2*x)) := by
    field_simp
    ring
  rw [he]
  have hr : (2+x)/(2*x) ≤ 3 := (div_le_iff₀ (by linarith)).2 (by linarith)
  have hpos : 0 ≤ (2+x)/(2*x) := div_nonneg (by linarith) (by linarith)
  constructor
  · exact mul_nonneg (sq_nonneg _) hpos
  · simpa [mul_comm] using mul_le_mul_of_nonneg_left hr (sq_nonneg (1-x))

theorem limitingBias (face noise bulk : ℝ) (a : face=3/4) (b : noise=1/4)
    (c : face=bulk+noise) : bulk=1/2 := by linarith

/-- Dihedral coordinates for the permutations of three symbols: r^i s^j. -/
def compose (a b : Nat) : Nat :=
  ((a%3 + (if a/3 == 0 then b%3 else 3-b%3))%3) + 3*((a/3+b/3)%2)

def inverse (a : Nat) : Nat := if a < 3 then (3-a)%3 else a

def commutator (a b : Nat) : Nat := compose (compose (compose a b) (inverse a)) (inverse b)

-- BEGIN PCP OS generated shared-path control
def table : List Nat := [0, 1, 2, 3, 4, 5, 1, 2, 0, 4, 5, 3, 2, 0, 1, 5, 3, 4, 3, 5, 4, 0, 2, 1, 4, 3, 5, 1, 0, 2, 5, 4, 3, 2, 1, 0]

def histogram : List Nat := [18, 9, 9, 0, 0, 0]

theorem tableComposes : table = (List.range 6).flatMap (fun a => (List.range 6).map (compose a)) := by decide

theorem sharedWord : histogram = [18,9,9,0,0,0] ∧ histogram = (List.range 6).map (fun g => ((List.range 6).flatMap (fun a => (List.range 6).map (commutator a))).count g) := by decide

#print axioms reciprocalSecant
#print axioms reciprocalMean
#print axioms reverseTest
#print axioms explainedVariance
#print axioms independentChannels
#print axioms spectralThreshold
#print axioms casimirLoss
#print axioms goodClock
#print axioms discardedClock
#print axioms varianceBudget
#print axioms reflectionDoubling
#print axioms sixStapleTime
#print axioms survivalAtMostOne
#print axioms lossExpansion
#print axioms stapleDispersion
#print axioms reciprocalDispersion
#print axioms limitingBias
#print axioms productError
#print axioms tableComposes
#print axioms sharedWord

end Millennium.YangMills.D4.GraphHolonomies
