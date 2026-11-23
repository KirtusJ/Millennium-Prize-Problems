import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity

open MeasureTheory Set
open scoped BigOperators

namespace YangMills.Momentum

/-- Squaring a bound on the extremal ground-state amplitudes gives the density bound. -/
theorem densityComparison {lo hi r x normal : ℝ}
    (hr : 0 ≤ r) (hx : lo ≤ x) (hu : hi ≤ r*lo)
    (hh : 0 ≤ hi) (hn : normal ≤ hi^2) : normal ≤ r^2*x^2 := by
  have h : hi ≤ r*x := hu.trans (mul_le_mul_of_nonneg_left hx hr)
  have hsq := mul_self_le_mul_self hh h
  nlinarith

/-- Private Haar integrations remove cross terms if their means vanish. -/
theorem privateIntegrals {ι α : Type*} [MeasurableSpace α] (μ : Measure α) (s : Finset ι)
    (term : ι → ι → α → ℝ) (a : ι → ℝ) (j : ℝ)
    (hi : ∀ i ∈ s, ∀ k ∈ s, Integrable (term i k) μ)
    (diag : ∀ i ∈ s, ∫ x, term i i x ∂μ = j*a i)
    (off : ∀ i ∈ s, ∀ k ∈ s, i ≠ k → ∫ x, term i k x ∂μ = 0) :
    (∫ x, ∑ i ∈ s, ∑ k ∈ s, term i k x ∂μ) = j * ∑ i ∈ s, a i := by
  classical
  rw [integral_finset_sum s (fun i hi' => integrable_finset_sum _ (fun k hk => hi i hi' k hk)),
      Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i hi'
  rw [integral_finset_sum s (fun k hk => hi i hi' k hk)]
  exact (Finset.sum_eq_single_of_mem i hi' (fun k hk hki => off i hi' k hk (Ne.symm hki))).trans (diag i hi')


theorem haarFloor {α : Type*} [MeasurableSpace α] (μ : Measure α) (ρ f : α → ℝ)
    (r : ℝ) (floor : ∀ᵐ x ∂μ, 1 ≤ r^2 * ρ x) (pos : ∀ᵐ x ∂μ, 0 ≤ f x)
    (hf : Integrable f μ) (hp : Integrable (fun x => ρ x * f x) μ) :
    (∫ x, f x ∂μ) ≤ r^2 * ∫ x, ρ x * f x ∂μ := by
  rw [← integral_const_mul]
  apply integral_mono_ae hf (hp.const_mul _)
  filter_upwards [floor, pos] with x h hx
  simpa only [one_mul, mul_assoc] using mul_le_mul_of_nonneg_right h hx

/-- Sites are encoded as x+n*(y+n*z). An edge uses its direction, a face its normal. -/
private def shiftSite (n site axis : ℕ) (forward : Bool) : ℕ :=
  let stride := n^axis
  let u := site / stride % n
  site - u*stride + ((u + (if forward then 1 else n-1)) % n)*stride

private def faceEdges (n face : ℕ) : List ℕ :=
  let x := face / 3
  let i := (face%3+1)%3
  let j := (face%3+2)%3
  [3*x+i, 3*shiftSite n x i true+j, 3*shiftSite n x j true+i, 3*x+j]

private def edgeFaces (n edge : ℕ) : List ℕ :=
  let x := edge / 3
  let i := edge % 3
  [1,2].flatMap fun k =>
    let j := (i+k)%3
    let normal := 3-i-j
    [3*x+normal, 3*shiftSite n x j false+normal]

private def nearFaces (n face : ℕ) : List ℕ :=
  ((faceEdges n face).flatMap (edgeFaces n)).eraseDups

def nearCounts (n : ℕ) : ℕ × ℕ :=
  let first := nearFaces n 0
  (first.length, (first.flatMap (nearFaces n)).eraseDups.length)

def privateEdgeCount (n : ℕ) : ℕ :=
  (((edgeFaces n 0).map fun face =>
      let es := faceEdges n face
      es[(es.idxOf 0 + 2) % 4]!).eraseDups).length

theorem privateEdges : privateEdgeCount 3 = 4 ∧ privateEdgeCount 2 = 2 := by decide +kernel

/-- A real spectral energy is dominated by the low, window and cubic terms. -/
theorem cubicWindowPoint {e l R : ℝ} (he : 0 ≤ e) (hl : 0 ≤ l) (hR : 0 < R) :
    R^2 * e ≤ R^2*l + R^3 * (Icc l R).indicator (fun _ => (1:ℝ)) e + e^3 := by
  by_cases low : e < l
  · rw [indicator_of_not_mem (show e ∉ Icc l R from fun h => (not_lt.mpr h.1) low)]
    have t := mul_le_mul_of_nonneg_left (le_of_lt low) (sq_nonneg R)
    nlinarith [pow_nonneg he 3]
  by_cases upper : e ≤ R
  · rw [indicator_of_mem (show e ∈ Icc l R from ⟨le_of_not_gt low,upper⟩)]
    have t := mul_le_mul_of_nonneg_left upper (sq_nonneg R)
    nlinarith [mul_nonneg (sq_nonneg R) hl, pow_nonneg he 3]
  · rw [indicator_of_not_mem (show e ∉ Icc l R from fun h => upper h.2)]
    have t := mul_nonneg (sub_nonneg.mpr (le_of_not_ge upper)) (by positivity : 0 ≤ e*(e+R))
    nlinarith [mul_nonneg (sq_nonneg R) hl]

/-- Window estimate for an actual finite Borel measure, allowing an atom at zero. -/
theorem cubicWindowMeasure (μ : Measure ℝ) [IsFiniteMeasure μ] {l R : ℝ}
    (hl : 0 ≤ l) (hR : 0 < R) (he : ∀ᵐ e ∂μ, 0 ≤ e)
    (h1 : Integrable (fun e : ℝ => e) μ) (h3 : Integrable (fun e : ℝ => e^3) μ) :
    R^2 * (∫ e, e ∂μ) ≤ R^2*l*μ.real univ + R^3*μ.real (Icc l R) + ∫ e, e^3 ∂μ := by
  let band := (Icc l R).indicator (fun _ : ℝ => (1:ℝ))
  have hb : Integrable band μ := (integrable_const 1).indicator measurableSet_Icc
  have hv : (∫ e, band e ∂μ) = μ.real (Icc l R) := integral_indicator_one measurableSet_Icc
  have h := integral_mono_ae (h1.const_mul (R^2))
    (((integrable_const (R^2*l)).add (hb.const_mul (R^3))).add h3)
    (he.mono fun e ho => cubicWindowPoint ho hl hR)
  change (∫ x, R^2*x ∂μ) ≤ (∫ x, (R^2*l + R^3*band x) + x^3 ∂μ) at h
  have hab : Integrable (fun x : ℝ => R^2*l + R^3*band x) μ :=
    (integrable_const (R^2*l)).add (hb.const_mul (R^3))
  rw [integral_add hab h3, integral_add (integrable_const (R^2*l)) (hb.const_mul (R^3)),
      integral_const, integral_const_mul, integral_const_mul, hv] at h
  simpa only [smul_eq_mul, mul_comm (μ.real univ)] using h

theorem positiveWindow {a M l R mass window : ℝ} (hr : 0 < R)
    (low : 4*l*mass ≤ a) (tail : 4*M ≤ a*R^2)
    (control : R^2*a ≤ R^2*l*mass + R^3*window + M) :
    a ≤ 2*R*window := by
  have ht := mul_le_mul_of_nonneg_left low (sq_nonneg R)
  by_contra! h
  have contra := mul_lt_mul_of_pos_left h (sq_pos_of_pos hr)
  nlinarith

/-- Counts exceptional momenta through the trace of the static structure factor. -/
theorem exceptionalCount {ι : Type*} (all bad : Finset ι) (sub : bad ⊆ all)
    (mass : ι → ℝ) (h0 : ∀ k ∈ all, 0 ≤ mass k) {a l C : ℝ} (hl : 0 ≤ l)
    (badMass : ∀ k ∈ bad, a ≤ 4*l*mass k)
    (parseval : ∑ k ∈ all, mass k ≤ (all.card : ℝ)*C) :
    (bad.card : ℝ)*a ≤ 4*l*((all.card : ℝ)*C) := by
  have first := Finset.sum_le_sum badMass
  have second := Finset.sum_le_sum_of_subset_of_nonneg sub (fun i hi _ => h0 i hi)
  simpa only [Finset.sum_const, nsmul_eq_mul, ← Finset.mul_sum] using
    first.trans (by rw [← Finset.mul_sum]; exact mul_le_mul_of_nonneg_left (second.trans parseval) (by positivity))


private def spectralAtoms : List (ℕ × ℕ) := [(0,100), (1,6), (4,3), (8,1)]
private def atomicMoment (n : ℕ) := (spectralAtoms.map fun (e,m) => m*e^n).sum
private def atomicWindow := (spectralAtoms.map fun (e,m) => if 1 ≤ e ∧ e ≤ 4 then m else 0).sum

theorem closedWindowFixture : (atomicMoment 1, atomicMoment 3, atomicWindow) = (26,710,9) := by decide +kernel

/-- Sum of squared derivatives for the adjoint gradient map q ↦ x Im(q). -/
theorem adjointDifferentialFloor (x : ℝ) :
    (3/4 : ℝ) ≤ 1-2*x^2+4*x^4 := by
  nlinarith [sq_nonneg (2*x^2-1/2)]

theorem shiftedResidual {k s : ℝ} (parts : 3/4 ≤ (4+4*k)*s) :
    9 ≤ 256*(1+k)^2*s^2 := by
  have h := mul_self_le_mul_self (by norm_num : (0:ℝ) ≤ 3/4) parts
  nlinarith

/-- D4's quadratic window majorant, including both endpoints. -/
theorem quadraticWindowPoint {l R : ℝ} (ordered : l ≤ R) (e : ℝ) :
    (e-l)*(R-e) ≤ (R-l)^2/4 * (Icc l R).indicator (fun _ => (1:ℝ)) e := by
  by_cases h : e ∈ Icc l R
  · rw [indicator_of_mem h]
    nlinarith [sq_nonneg (e-(R+l)/2)]
  · rw [indicator_of_not_mem h, mul_zero]
    by_cases he : e < l
    · exact mul_nonpos_of_nonpos_of_nonneg (by linarith) (by linarith)
    · have hu : R < e := lt_of_not_ge (fun le => h ⟨le_of_not_gt he, le⟩)
      exact mul_nonpos_of_nonneg_of_nonpos (by linarith) (by linarith)

/-- A uniform row and column sum bounds the spatial moment form on coefficient norms. -/
theorem finiteSchur {ι : Type*} (s : Finset ι) (w : ι → ι → ℝ) (x : ι → ℝ) (K : ℝ)
    (nonnegative : ∀ i ∈ s, ∀ j ∈ s, 0 ≤ w i j)
    (row : ∀ i ∈ s, ∑ j ∈ s, w i j ≤ K) (col : ∀ j ∈ s, ∑ i ∈ s, w i j ≤ K) :
    (∑ i ∈ s, ∑ j ∈ s, w i j * (x i*x j)) ≤ K * ∑ i ∈ s, x i^2 := by
  have diagonal (a : ι → ι → ℝ) (b : ∀ i ∈ s, ∑ j ∈ s, a i j ≤ K) :
      (∑ i ∈ s, ∑ j ∈ s, a i j * x i^2) ≤ K * ∑ i ∈ s, x i^2 := by
    rw [Finset.mul_sum]
    apply Finset.sum_le_sum
    intro i hi
    rw [← Finset.sum_mul]
    exact mul_le_mul_of_nonneg_right (b i hi) (sq_nonneg _)
  have other : (∑ i ∈ s, ∑ j ∈ s, w i j * x j^2) ≤ K * ∑ i ∈ s, x i^2 := by
    rw [Finset.sum_comm]
    exact diagonal (fun j i => w i j) col
  have both : (∑ i ∈ s, ∑ j ∈ s, 2*(w i j*(x i*x j))) ≤
      ∑ i ∈ s, ∑ j ∈ s, (w i j*x i^2 + w i j*x j^2) := by
    apply Finset.sum_le_sum
    intro i hi
    apply Finset.sum_le_sum
    intro j hj
    nlinarith [mul_nonneg (nonnegative i hi j hj) (sq_nonneg (x i-x j))]
  simp only [← Finset.mul_sum, Finset.sum_add_distrib] at both
  linarith [diagonal w row]

set_option maxRecDepth 25000 in
set_option maxHeartbeats 0 in
theorem periodicSupport : nearCounts 3 = (13,51) ∧ nearCounts 5 = (13,63) := by decide +kernel

/-- A bounded first/third moment permits an exceptional Fourier mode with divergent mass. -/
theorem softAtom (x : ℝ) (hx : 1 ≤ x) : x*(1/x) = 1 ∧ x*(1/x)^3 ≤ 1 := by
  have pos : 0 < x := by linarith
  have h : x*(1/x) = 1 := by field_simp
  have small : 1/x ≤ 1 := (div_le_one pos).mpr hx
  have u : 0 ≤ 1/x := by positivity
  constructor
  · exact h
  · calc x*(1/x)^3 = (x*(1/x)) * ((1/x)*(1/x)) := by ring
         _ ≤ 1 := by rw [h, one_mul]; exact (mul_le_mul_of_nonneg_right small u).trans (by simpa using small)

end YangMills.Momentum

open YangMills.Momentum
#print axioms densityComparison
#print axioms privateIntegrals
#print axioms cubicWindowPoint
#print axioms cubicWindowMeasure
#print axioms positiveWindow
#print axioms exceptionalCount
#print axioms periodicSupport
#print axioms softAtom
#print axioms haarFloor
#print axioms closedWindowFixture
#print axioms privateEdges
#print axioms finiteSchur
#print axioms adjointDifferentialFloor
#print axioms shiftedResidual
#print axioms quadraticWindowPoint
