import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Finite estimates used in the Hamiltonian time limit at fixed spatial mesh. -/
namespace Millennium.YangMills.HamiltonianTime

/-- The first correction in the normalized Bessel quotient, from the two fixed orders. -/
theorem casimirCoefficient (n : ℝ) :
    ((4*(n+1)^2-1) - (4*1^2-1))/8 = n*(n+2)/2 := by ring

/-- The product of edge transfer factors on a spin network with at least g active edges. -/
theorem cycleProduct {ι : Type*} (S : Finset ι) (b : ι → ℝ) {r : ℝ} {g : ℕ}
    (hb : ∀ e ∈ S, 0 ≤ b e) (hbr : ∀ e ∈ S, b e ≤ r)
    (hr : 0 ≤ r) (hr1 : r ≤ 1) (hg : g ≤ S.card) :
    ∏ e ∈ S, b e ≤ r^g := by
  calc
    ∏ e ∈ S, b e ≤ ∏ _e ∈ S, r := Finset.prod_le_prod hb hbr
    _ = r^S.card := Finset.prod_const r
    _ ≤ r^g := pow_le_pow_of_le_one hr hr1 hg

-- PCP begin range
/-- Sum over the four translations of the anchored sites. Each shift is a permutation. -/
theorem rangeSum {ι : Type*} [Fintype ι] (A : ι → ℝ) (p q r : Equiv.Perm ι) :
    ∑ i, (A i + A (p i) + A (q i) + A (r i)) = 4 * ∑ i, A i := by
  simp only [Finset.sum_add_distrib, Equiv.sum_comp]
  ring
-- PCP end range

/-- Rescaling the physical Hamiltonian gives the local normalization in Yarotsky's theorem. -/
theorem rescale {κ : ℝ} (h : 0 < κ) (A V coupling : ℝ) :
    (8*κ/3)*(A/(2*κ) - coupling*V) = 4*A/3 - (8*κ/3)*coupling*V := by
  field_simp [ne_of_gt h]
  ring

/-- A block excitation at any one site costs at least one unit after rescaling. -/
theorem blockUnitGap {ι : Type*} [Fintype ι] (A : ι → ℝ)
    (hA : ∀ i, 0 ≤ A i) (excited : ∃ i, 3 ≤ A i) : 1 ≤ (∑ i, A i)/3 := by
  obtain ⟨j, hj⟩ := excited
  have bound : A j ≤ ∑ i, A i :=
    Finset.single_le_sum (f := A) (fun i _ => hA i) (Finset.mem_univ j)
  linarith

/-- The same product-vacuum leakage estimate works at every spatial volume. -/
theorem faceLeak {z p first second third fourth ε : ℝ} (budget : 3*p ≤ 2*z)
    (edges : first ≤ p ∧ second ≤ p ∧ third ≤ p ∧ fourth ≤ p)
    (unionBound : ε ≤ first+second+third+fourth) :
    ε ≤ 8*z/3 := by
  obtain ⟨h₁,h₂,h₃,h₄⟩ := edges
  linarith

/-- A local state close to Haar yields positive variance and a finite excitation energy. -/
theorem localWitness {z d m s v κ E : ℝ} (hk : 0 < κ)
    (small : z ≤ 1/384) (overlap : d^2 ≤ 8*z/3)
    (mean : |m| ≤ 4*d) (second : 1-4*d ≤ s)
    (variance : v = s-m^2) (energy : κ*E = 2*(4-s)) :
    5/9 ≤ v ∧ E/v ≤ 12/κ := by
-- PCP begin witness
  have radius : d ≤ 1/12 := by nlinarith only [small, overlap]
  obtain ⟨lo, hi⟩ := abs_le.mp mean
  have sq : m^2 ≤ 1/9 := by
    nlinarith only [mul_nonneg (show 0 ≤ m+1/3 by linarith) (show 0 ≤ 1/3-m by linarith)]
  have hv : 5/9 ≤ v := by linarith
  refine ⟨hv, (div_le_div_iff₀ (by linarith : 0 < v) hk).2 ?_⟩
  linarith [mul_comm κ E]
-- PCP end witness

/-- A fixed mass and first moment give a quantitative lower Laplace envelope by the tangent line. -/
theorem tangentPoint (t x c : ℝ) :
    Real.exp (-t*c)*(1+t*(c-x)) ≤ Real.exp (-t*x) := by
  have id : -t*x = -t*c + t*(c-x) := by ring
  rw [id, Real.exp_add]
  apply mul_le_mul_of_nonneg_left _ (Real.exp_pos _).le
  linarith only [Real.add_one_le_exp (t*(c-x))]

/-- Electric energy and magnetic defect from the polarized product trial at h=4u, u=√z. -/
theorem polarTrial {u r K d : ℝ} (hu : 0 < u) (hr : 0 ≤ r) (hr1 : r ≤ 1)
    (hK : 0 ≤ K) (hd : 0 ≤ d) (gammaBound : 8*u*(1-r) ≤ 3)
    (trial : K/2 + u^2*d ≤ 3*(4*u)*r/8 + u^2*(1-r^4)) :
    K ≤ 6*u ∧ u*d ≤ 3 := by
  have powers : 1-r^4 ≤ 4*(1-r) := by
    nlinarith only [mul_nonneg (sq_nonneg (1-r))
      (show 0 ≤ r^2+2*r+3 by nlinarith [sq_nonneg r])]
  have kinetic := mul_le_mul_of_nonneg_left hr1 hu.le
  have magnetic := mul_le_mul_of_nonneg_left powers (sq_nonneg u)
  have tail := mul_le_mul_of_nonneg_left gammaBound hu.le
  have total : K/2 + u^2*d ≤ 3*u := by linarith only [kinetic, magnetic, tail, trial]
  constructor
  · nlinarith only [total, mul_nonneg (sq_nonneg u) hd]
  · apply le_of_mul_le_mul_left _ hu
    nlinarith only [total, hK]

/-- The block integration-by-parts inequality prevents faster plaquette concentration. -/
theorem weakLower {u K d A : ℝ} (hu : 6 ≤ u) (hd : 0 ≤ d) (hA : 0 ≤ A)
    (defect : u*d ≤ 3) (kinetic : K ≤ 6*u) (gradient : A ≤ 2*d)
    (score : 9*(1-d)^2 ≤ 4*K*A) :
    3/32 ≤ u*A ∧ 3/64 ≤ u*d := by
  have dh : d ≤ 1/2 := by linarith only [defect, mul_nonneg (sub_nonneg.mpr hu) hd]
  have square := mul_nonneg (show 0 ≤ 1/2-d by linarith) (show 0 ≤ 3/2-d by linarith)
  have sq : 1/4 ≤ (1-d)^2 := by nlinarith only [square]
  have ka := mul_le_mul_of_nonneg_right kinetic hA
  have ag := mul_le_mul_of_nonneg_left gradient (show 0 ≤ u by linarith)
  constructor <;> linarith only [sq, score, ka, ag]

/-- Smearing a strictly site-diagonal temporal correlator leaves the spatial inner product. -/
theorem electricSmearing {ι : Type*} [Fintype ι] [DecidableEq ι]
    (q : ℝ) (f g : ι → ℝ) :
    ∑ i, ∑ j, f i * (if i = j then q else 0) * g j = q * ∑ i, f i * g i := by
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i _
  rw [Finset.sum_eq_single i]
  · simp [mul_assoc, mul_left_comm, mul_comm]
  · intro j _ h
    simp [Ne.symm h]
  · simp

#print axioms electricSmearing
#print axioms polarTrial
#print axioms weakLower
#print axioms casimirCoefficient
#print axioms cycleProduct
#print axioms rangeSum
#print axioms rescale
#print axioms blockUnitGap
#print axioms faceLeak
#print axioms localWitness
#print axioms tangentPoint
end Millennium.YangMills.HamiltonianTime
