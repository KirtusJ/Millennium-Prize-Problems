import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.List.Defs
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace YangMills.SiteScalar

/-- A bound on two adjacent edge distances supplies one half of the
singularity at each endpoint in the nearest-neighbor estimate. -/
theorem edgeSplit {d a b : ℝ} (ha : 0 < a) (hb : 0 < b)
    (had : a ≤ d) (hbd : b ≤ d) : (1/d)^4 ≤ (1/a)^2*(1/b)^2 := by
  have hd := ha.trans_le had
  have h1 := one_div_le_one_div_of_le ha had
  have h2 := one_div_le_one_div_of_le hb hbd
  have hd' : 0 ≤ 1/d := (one_div_pos.mpr hd).le
  calc
    (1/d)^4 = (1/d)^2*(1/d)^2 := by ring
    _ ≤ _ := mul_le_mul (pow_le_pow_left₀ hd' h1 2)
      (pow_le_pow_left₀ hd' h2 2) (sq_nonneg _) (sq_nonneg _)

/-- Four neighboring face bases per orientation recover unit total weight. -/
theorem cloverCenter (b w μ : ℝ) :
    b/4*((24-w)-(24-μ)) = -(b/4)*(w-μ) := by ring

/-- Products of pairs of sign-reversing curvature kernels are fixed by
Hodge conjugation even when their multiplication is noncommutative. -/
theorem fixedPairs {A : Type*} [Ring A] (σ : A →+* A)
    (l : List (A × A))
    (h : ∀ p ∈ l, σ p.1 = -p.1 ∧ σ p.2 = -p.2) :
    σ (l.map (fun p => p.1*p.2)).prod = (l.map (fun p => p.1*p.2)).prod := by
  induction l with
  | nil => simp
  | cons p l ih =>
    have hp := h p (List.mem_cons_self)
    have hl : ∀ q ∈ l, σ q.1 = -q.1 ∧ σ q.2 = -q.2 :=
      fun q hq => h q (List.mem_cons_of_mem _ hq)
    simp only [List.map_cons, List.prod_cons, map_mul, hp.1, hp.2,
      neg_mul_neg, ih hl]

/-- The invariant trace of one more sign-reversing factor is zero. -/
theorem oddCycle {A : Type*} [Ring A] (σ : A →+* A)
    (trace : A →+ ℝ) (invariant : ∀ x, trace (σ x) = trace x)
    (a b : A) (ha : σ a = -a) (hb : σ b = b) : trace (a*b) = 0 := by
  have h := invariant (a*b)
  rw [map_mul, ha, hb, neg_mul, map_neg] at h
  linarith

/-- The three colors and the six orthogonal two-form channels yield nine
in the action covariance with the half-squared Gaussian normalization. -/
theorem scalarPair (c : ℝ) : (3:ℝ)*6*2*(1/2)^2*c^2 = 9*c^2 := by ring

/-- Sixteen Wick assignments on each four-cycle yield the normalized
trace coefficient for arbitrary quadrilateral geometry. -/
theorem fourthCycle (v : ℝ) :
    3*16*(1/2:ℝ)^4*v/3^4 = v/27 := by ring

/-- A positive ratio at one stride propagates to all later strides of a
log-convex transfer correlation. The first entry is the reading at r. -/
theorem strideFloor (c : ℕ → ℝ) (q : ℝ) (hq : 0 ≤ q)
    (pos : ∀ j, 0 < c j) (first : q ≤ c 1 / c 0)
    (convex : ∀ j, c (j+1)*c (j+1) ≤ c j*c (j+2)) (n : ℕ) :
    c 0*q^n ≤ c n := by
  have step (j : ℕ) : c (j+1)/c j ≤ c (j+2)/c (j+1) := by
    apply (div_le_div_iff₀ (pos _) (pos _)).2
    simpa only [mul_comm (c (j+2))] using convex j
  have hr (j : ℕ) : q ≤ c (j+1)/c j := by
    induction j with
    | zero => exact first
    | succ j ih => exact ih.trans (step j)
  induction n with
  | zero => simp
  | succ n ih =>
    rw [pow_succ, ← mul_assoc]
    exact (mul_le_mul_of_nonneg_right ih hq).trans (by
      simpa only [mul_comm q] using (le_div_iff₀ (pos n)).mp (hr n))

end YangMills.SiteScalar
#print axioms YangMills.SiteScalar.edgeSplit
#print axioms YangMills.SiteScalar.cloverCenter
#print axioms YangMills.SiteScalar.fixedPairs
#print axioms YangMills.SiteScalar.oddCycle
#print axioms YangMills.SiteScalar.scalarPair
#print axioms YangMills.SiteScalar.fourthCycle
#print axioms YangMills.SiteScalar.strideFloor
