import Mathlib.Tactic.NoncommRing
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Analysis.SpecialFunctions.Exp

open scoped BigOperators
open Filter Topology

namespace YangMills.Locality

/-- Product rule for the commutator of a word. -/
theorem wordStep {R : Type*} [Ring R] (u v b : R) :
    u*v*b-b*(u*v) = u*(v*b-b*v)+(u*b-b*u)*v := by noncomm_ring

/-- The derivative and inverse derivative cancel the homogeneous transport. -/
theorem conjugateForce {R : Type*} [Ring R] (u z b v : R) :
    (u*z)*b*v + u*b*(-z*v) = u*(z*b-b*z)*v := by noncomm_ring

theorem inverseCommutator {R : Type*} [Ring R] (u v b : R)
    (h : v*u=1) (k : u*v=1) :
    v*b-b*v = -(v*(u*b-b*u)*v) := by
  have a : v*(u*b)*v = b*v := by simp [← mul_assoc, h]
  have c : v*(b*u)*v = v*b := by simp [mul_assoc, k]
  rw [mul_sub, sub_mul, a, c]
  abel

/-- Squared-distance classes in doubled midpoint coordinates for the faces incident to an x link. -/
private def pattern : List (ℤ × ℤ × ℤ) :=
  [(-1,-1,0),(1,-1,0),(-1,1,0),(1,1,0),
   (-1,0,-1),(1,0,-1),(-1,0,1),(1,0,1),
   (0,2,0),(0,-2,0),(0,0,2),(0,0,-2)] ++ List.replicate 4 (0,0,0)

private def countDist (n : ℤ) : ℕ :=
  (pattern.filter fun v => v.1^2 + v.2.1^2 + v.2.2^2 == n).length

theorem midpointCounts : (countDist 0, countDist 2, countDist 4) = (4,8,4) := by decide

/-- Successive weighted face-incidence steps, beginning with a source on links. -/
def walks {ι : Type*} [Fintype ι] (A : ι → ι → ℝ) (g : ι → ℝ) : ℕ → ι → ℝ
  | 0 => g
  | n+1 => fun i => ∑ j, A i j * walks A g n j

theorem tiltedWalks {ι : Type*} [Fintype ι] (A : ι → ι → ℝ) (g v : ι → ℝ)
    (K M : ℝ) (ha : ∀ i j, 0 ≤ A i j) (hk : 0 ≤ K) (hm : 0 ≤ M)
    (hrow : ∀ i, (∑ j, A i j * v j) ≤ K * v i) (hg : ∀ i, g i ≤ M*v i)
    (n : ℕ) (i : ι) : walks A g n i ≤ (M * K^n) * v i := by
  induction n generalizing i with
  | zero => simpa [walks] using hg i
  | succ n ih =>
    have hn : 0 ≤ M*K^n := mul_nonneg hm (pow_nonneg hk n)
    calc
      walks A g (n+1) i ≤ ∑ j, A i j * ((M*K^n)*v j) :=
        Finset.sum_le_sum fun j _ => mul_le_mul_of_nonneg_left (ih j) (ha i j)
      _ = (M*K^n) * ∑ j, A i j * v j := by
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro j _
        ring
      _ ≤ (M*K^n) * (K*v i) := mul_le_mul_of_nonneg_left (hrow i) hn
      _ = _ := by ring

theorem noShortPaths {ι : Type*} [Fintype ι] (A : ι → ι → ℝ) (g : ι → ℝ)
    (d : ι → ℕ) (hstep : ∀ i j, A i j ≠ 0 → d i ≤ d j + 1)
    (hsource : ∀ i, 0 < d i → g i = 0) (n : ℕ) (i : ι) (hlt : n < d i) :
    walks A g n i = 0 := by
  induction n generalizing i with
  | zero => exact hsource i hlt
  | succ n ih =>
    apply Finset.sum_eq_zero
    intro j _
    by_cases h : A i j = 0
    · simp [h]
    · have := hstep i j h
      rw [ih j (by omega), mul_zero]

private def diagonalTwo : ℕ := 4^2 + 8*1^2 + 4*1^2
theorem twoStepReturn : diagonalTwo = 28 := by decide

private noncomputable def term (x : ℝ) (n : ℕ) : ℝ := x^n / (n.factorial : ℝ)

/-- The twice-integrated Volterra kernel occupies only the even Taylor indices
after factoring out the initial time. This bound holds for every truncation. -/
theorem evenMajorant (x : ℝ) (hx : 0 ≤ x) (N : ℕ) :
    (∑ n ∈ Finset.range N, x^(2*n) / ((2*n+1).factorial : ℝ)) ≤ Real.exp x := by
  have H (k : ℕ) : (∑ n ∈ Finset.range k, x^(2*n) / ((2*n+1).factorial : ℝ))
      ≤ ∑ n ∈ Finset.range (2*k), term x n := by
    induction k with
    | zero => simp
    | succ k ih =>
      rw [show 2*(k+1)=2*k+1+1 by omega, Finset.sum_range_succ, Finset.sum_range_succ]
      rw [Finset.sum_range_succ] at *
      have df : ((2*k).factorial : ℝ) ≤ ((2*k+1).factorial : ℝ) := by
        exact_mod_cast Nat.factorial_le (by omega : 2*k ≤ 2*k+1)
      have hd : (0:ℝ) < (2*k).factorial := by positivity
      have hbase : x^(2*k) / ((2*k+1).factorial : ℝ) ≤ term x (2*k) :=
        div_le_div_of_nonneg_left (pow_nonneg hx _) hd df
      have hpos : 0 ≤ term x (2*k+1) := by unfold term; positivity
      linarith
  exact (H N).trans (Real.sum_le_exp_of_nonneg hx _)


/-- Integration from zero shifts the factorial kernel by one degree, including across zero. -/
theorem integrateTerm (n : ℕ) (t : ℝ) : (∫ x in (0:ℝ)..t, term x n) = term t (n+1) := by
  unfold term
  rw [intervalIntegral.integral_div, integral_pow]
  simp only [zero_pow (Nat.succ_ne_zero n), sub_zero, Nat.factorial_succ, Nat.cast_mul,
    Nat.cast_add, Nat.cast_one]
  rw [div_div]

theorem twoIntegrations (n : ℕ) (t : ℝ) :
    (∫ s in (0:ℝ)..t, ∫ x in (0:ℝ)..s, term x n) = term t (n+2) := by
  simp_rw [integrateTerm]

/-- For a real-time phase error bounded by 2 and y²/2, its squared error costs
at most 2y; this is the energy-tail interpolation in the Wilson comparison. -/
theorem phaseInterpolation {r y : ℝ} (hr : 0 ≤ r) (hy : 0 ≤ y)
    (h2 : r ≤ 2) (hquad : r ≤ y^2/2) : r^2 ≤ 2*y := by
  by_cases h : y ≤ 2
  · have h1 : y^2 ≤ 2*y := by nlinarith [mul_nonneg hy (sub_nonneg.mpr h)]
    have hle : r ≤ y := by linarith
    nlinarith [mul_nonneg hr (sub_nonneg.mpr h2)]
  · nlinarith [mul_nonneg (sub_nonneg.mpr h2) (add_nonneg hr (by norm_num : (0:ℝ) ≤ 2))]

theorem bareClock (beta b : ℝ) (hbeta : 0 < beta) (hb : 0 < b) :
    b^2 * (2/(beta*b)) * (beta/b) = 2 := by field_simp; ring

theorem scaledCone (n : ℕ) {x : ℕ → ℝ} (hx : Tendsto x atTop atTop) :
    Tendsto (fun j => x j ^ n * Real.exp (-x j)) atTop (𝓝 0) :=
  (Real.tendsto_pow_mul_exp_neg_atTop_nhds_zero n).comp hx

private def twiceIntegrated (n : ℕ) : ℕ := (2*n+1).factorial
theorem separatedDenominators :
    (twiceIntegrated 1, twiceIntegrated 2, twiceIntegrated 3) = (6,120,5040) := by decide

#print axioms wordStep
#print axioms conjugateForce
#print axioms inverseCommutator
#print axioms midpointCounts
#print axioms tiltedWalks
#print axioms noShortPaths
#print axioms twoStepReturn
#print axioms evenMajorant
#print axioms integrateTerm
#print axioms twoIntegrations
#print axioms phaseInterpolation
#print axioms bareClock
#print axioms scaledCone
#print axioms separatedDenominators
end YangMills.Locality
