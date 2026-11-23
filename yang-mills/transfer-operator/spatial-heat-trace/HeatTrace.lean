import Mathlib.Topology.MetricSpace.IsometricSMul
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

namespace Millennium.YangMills.SpatialHeatTrace
open Finset

/-- Product of the transports on an oriented walk, starting at its initial vertex. -/
def transport {G : Type*} [Monoid G] (g : ℕ → G) : ℕ → G
  | 0 => 1
  | n+1 => transport g n * g n

/-- Telescoping after transport to a common fiber, for an arbitrary isometric action. -/
theorem pathDefect {G X : Type*} [Monoid G] [PseudoMetricSpace X]
    [MulAction G X] [IsIsometricSMul G X] (g : ℕ → G) (f : ℕ → X) (n : ℕ) :
    dist (f 0) (transport g n • f n) ≤
      ∑ i ∈ range n, dist (f i) (g i • f (i+1)) := by
  induction n with
  | zero => simp [transport]
  | succ n ih =>
    rw [sum_range_succ, transport, mul_smul]
    refine (dist_triangle _ (transport g n • f n) _).trans ?_
    rw [dist_smul]
    exact add_le_add_right ih _

/-- Iterate the one-coordinate probability estimate without assuming product law. -/
theorem dependentEvents (p : ℝ) (hp : 0 ≤ p) (mass : ℕ → ℝ) (initial : mass 0 ≤ 1)
    (step : ∀ n, mass (n+1) ≤ p*mass n) (n : ℕ) : mass n ≤ p^n := by
  induction n with
  | zero => simpa using initial
  | succ n ih =>
    exact (step n).trans (by simpa [pow_succ, mul_comm] using mul_le_mul_of_nonneg_left ih hp)

/-- The two components of (I-U)(z,w), for U = ((a,b),(-conj b,conj a)). -/
theorem su2HolonomyDefect (a b z w : ℂ)
    (unit : Complex.normSq a + Complex.normSq b = 1) :
    Complex.normSq ((1-a)*z-b*w) + Complex.normSq ((star b)*z+(1-star a)*w) =
       (2-2*a.re)*(Complex.normSq z+Complex.normSq w) := by
  simp only [Complex.normSq_apply, Complex.add_re, Complex.add_im, Complex.sub_re,
    Complex.sub_im, Complex.mul_re, Complex.mul_im, Complex.one_re, Complex.one_im,
    Complex.star_def, Complex.conj_re, Complex.conj_im] at unit ⊢
  linear_combination (z.re*z.re+z.im*z.im+w.re*w.re+w.im*w.im) * unit

/-- Sum the individual derivatives without replacing all edge energies by the total. -/
theorem derivativeSum {ι : Type*} (edges : Finset ι) (v energy : ι → ℝ) (c : ℝ)
    (edge : ∀ i ∈ edges, v i ^ 2 ≤ c * energy i) :
    ∑ i ∈ edges, v i ^ 2 ≤ c * ∑ i ∈ edges, energy i := by
  rw [Finset.mul_sum]
  exact Finset.sum_le_sum edge

/-- The physical clock removes one power of spatial spacing from the form estimate. -/
theorem physicalMoment {b β V s grad M c : ℝ} (hb : 0 < b) (hβ : 0 < β) (hs : 0 < s)
    (bound : grad ≤ c*V*b/s^2) (form : M ≤ grad/(2*β*b)) :
    M ≤ c*V/(2*β*s^2) := by
  calc
    M ≤ (c*V*b/s^2)/(2*β*b) := form.trans (div_le_div_of_nonneg_right bound (by positivity))
    _ = _ := by field_simp; ring

/-- Energy in a positive band costs at least its lower endpoint times its mass. -/
theorem positiveBand {ι : Type*} (s : Finset ι) (w E : ι → ℝ) (ε : ℝ)
    (hle : ∀ i ∈ s, ε ≤ E i) (hw : ∀ i ∈ s, 0 ≤ w i) :
    ε * ∑ i ∈ s, w i ≤ ∑ i ∈ s, E i * w i := by
  rw [Finset.mul_sum]
  exact Finset.sum_le_sum (fun i hi => mul_le_mul_of_nonneg_right (hle i hi) (hw i hi))

/-- Pulling a root spinor around a four-edge cycle costs at most four edge energies. -/
theorem fourEdge {a b c d t : ℝ} (ht : 0 ≤ t) (path : t ≤ a+b+c+d) :
    t^2 ≤ 4*(a^2+b^2+c^2+d^2) := by
  have h := mul_self_le_mul_self ht path
  linarith only [h, sq_nonneg (a-b), sq_nonneg (a-c), sq_nonneg (a-d),
    sq_nonneg (b-c), sq_nonneg (b-d), sq_nonneg (c-d)]

/-- Average on a cube with at least half its sites controlled. -/
theorem goodFraction {norm var mean good energy l u : ℝ}
    (dec : norm = var+mean) (many : mean ≤ 4*good+4*var)
    (poincare : var ≤ l*energy) (anchor : good ≤ u*energy) :
    norm ≤ (5*l+4*u)*energy := by linarith

/-- Union bound over possible bad small cubes, allowing dependent events. -/
theorem badMajority (n k : ℕ) (many : n ≤ 2*k) :
    (2:ℝ)^n * (1/16:ℝ)^k ≤ (1/2:ℝ)^n := by
  have ex : 2*n ≤ 4*k := by omega
  have p := pow_le_pow_right₀ (a := (2:ℝ)) (by norm_num) ex
  rw [pow_mul, pow_mul] at p
  norm_num at p
  rw [div_pow, div_pow, one_pow, one_pow, mul_one_div, div_le_div_iff₀ (by positivity) (by positivity)]
  rw [← mul_pow]
  norm_num
  exact p

/-- Scalar spectral step for a heat-trace bound. -/
theorem eigenCount {ι : Type*} (modes : Finset ι) (E : ι → ℝ) (s R : ℝ)
    (hs : 0 ≤ s) (hR : ∀ i ∈ modes, E i ≤ R) :
    (modes.card : ℝ) * Real.exp (-s*R) ≤ ∑ i ∈ modes, Real.exp (-s*E i) := by
  simpa using Finset.sum_le_sum (s := modes) (fun i hi =>
    Real.exp_le_exp.mpr (mul_le_mul_of_nonpos_left (hR i hi) (neg_nonpos.mpr hs)))

/-- Balancing the cost of the rare cube and of confining a trial state to it. -/
theorem rareBalance {x m u L : ℝ} (hm : 0 < m) (hu : 0 ≤ u) (hL : 0 ≤ L)
    (small : m ≤ u) (large : u ≤ 2*m) (scale : x = u^5*L) :
    x/m^2 + m^3*L ≤ 5*u^3*L := by
  have sq := mul_self_le_mul_self hu large
  have square : u^2 ≤ 4*m^2 := by nlinarith only [sq]
  have weighted := mul_le_mul_of_nonneg_left square (show 0 ≤ u^3*L by positivity)
  have first : x/m^2 ≤ 4*u^3*L := by
    apply (div_le_iff₀ (sq_pos_of_pos hm)).2
    rw [scale]
    linarith only [weighted]
  have cube := pow_le_pow_left₀ hm.le small 3
  linarith only [first, mul_le_mul_of_nonneg_right cube hL]

/-- A rare event carrying the mean costs inverse event probability in the second moment. -/
theorem rareSecondMoment {ι : Type*} (event : Finset ι) (prob Y : ι → ℝ)
    (hp : ∀ i ∈ event, 0 ≤ prob i) :
    (∑ i ∈ event, prob i * Y i)^2 ≤
      (∑ i ∈ event, prob i) * ∑ i ∈ event, prob i * (Y i)^2 := by
  apply Finset.sum_sq_le_sum_mul_sum_of_sq_eq_mul event hp
  · exact fun i hi => mul_nonneg (hp i hi) (sq_nonneg _)
  · intro i hi
    ring

/-- Taking logarithms of the matching upper and lower costs exposes the 3/5 exponent. -/
theorem logSandwich {x L cost c C : ℝ} (hx : 1 < x) (hL : 0 < L)
    (hc : 0 < c) (hC : 0 < C)
    (lower : c*x^((3:ℝ)/5) ≤ cost)
    (upper : cost ≤ C*x^((3:ℝ)/5)*L^((2:ℝ)/5)) :
    (3:ℝ)/5 + Real.log c/Real.log x ≤ Real.log cost/Real.log x ∧
    Real.log cost/Real.log x ≤ (3:ℝ)/5 + Real.log C/Real.log x +
      ((2:ℝ)/5)*(Real.log L/Real.log x) := by
  have xp := lt_trans zero_lt_one hx
  have logx := Real.log_pos hx
  have yp : 0 < c*x^((3:ℝ)/5) := by positivity
  have lo := Real.log_le_log yp lower
  have hi := Real.log_le_log (yp.trans_le lower) upper
  rw [Real.log_mul hc.ne' (Real.rpow_pos_of_pos xp _).ne', Real.log_rpow xp] at lo
  rw [Real.log_mul (by positivity) (Real.rpow_pos_of_pos hL _).ne',
    Real.log_mul hC.ne' (Real.rpow_pos_of_pos xp _).ne', Real.log_rpow xp, Real.log_rpow hL] at hi
  constructor
  · calc
      _ = (Real.log c + 3/5*Real.log x)/Real.log x := by field_simp; ring
      _ ≤ _ := div_le_div_of_nonneg_right lo logx.le
  · calc
      _ ≤ (Real.log C + 3/5*Real.log x + 2/5*Real.log L)/Real.log x :=
        div_le_div_of_nonneg_right hi logx.le
      _ = _ := by field_simp; ring

/-- The small conditional event probability can be charged to any squared outside test. -/
theorem outsideBudget {ι κ : Type*} [Fintype ι] [Fintype κ]
    (p bad : ι → κ → ℝ) (Z : ι → ℝ) (q : ℝ)
    (row : ∀ i, ∑ j, p i j*bad i j ≤ q * ∑ j, p i j) :
    ∑ i, ∑ j, (p i j*bad i j)*(Z i)^2 ≤ q * ∑ i, (∑ j, p i j)*(Z i)^2 := by
  rw [Finset.mul_sum]
  apply Finset.sum_le_sum
  intro i _
  rw [← Finset.sum_mul, ← mul_assoc]
  exact mul_le_mul_of_nonneg_right (row i) (sq_nonneg _)

-- PCP begin geometry
theorem cellAnchor {r mass E : ℝ} (unit : r ≤ 4)
    (hE : 0 ≤ E) (v : r*mass ≤ 64*E+48*r*E) : r*mass ≤ 256*E := by
  have h := mul_le_mul_of_nonneg_right unit hE
  linarith
-- PCP end geometry

-- PCP begin certificate
theorem coarseCell {n v w E m B : ℝ} (decomp : n ≤ 5*v+4*w)
    (hv : v ≤ m^2*E) (hw : w ≤ 16384*B*E) :
    n ≤ (5*m^2+65536*B)*E := by linarith
-- PCP end certificate

#print axioms pathDefect
#print axioms dependentEvents
#print axioms su2HolonomyDefect
#print axioms derivativeSum
#print axioms physicalMoment
#print axioms positiveBand
#print axioms fourEdge
#print axioms goodFraction
#print axioms badMajority
#print axioms eigenCount
#print axioms rareBalance
#print axioms logSandwich
#print axioms rareSecondMoment
#print axioms outsideBudget
#print axioms cellAnchor
#print axioms coarseCell
end Millennium.YangMills.SpatialHeatTrace
