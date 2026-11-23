import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

open Finset
namespace YangMills.DirichletBox

/-- The orientation convention in the paper fixes each forward tree edge. -/
theorem gaugeForward {G : Type*} [Group G] (parent edge : G) :
    parent * edge * (parent * edge)⁻¹ = 1 := mul_inv_cancel _

/-- Cauchy-Schwarz with path length and edge congestion bounded separately.
No commutativity of the original parallel transports is needed here. -/
theorem congestion {α ι : Type*} [DecidableEq ι] (roots : Finset α)
    (edges : Finset ι) (path : α → Finset ι) (a : ι → ℝ) (len mult : ℝ)
    (hlen : ∀ x ∈ roots, ((path x).card:ℝ) ≤ len)
    (hl : 0 ≤ len)
    (cover : ∀ x ∈ roots, path x ⊆ edges)
    (hcount : ∀ i ∈ edges, (((roots.filter (fun x ↦ i ∈ path x)).card):ℝ) ≤ mult) :
    (∑ x ∈ roots, (∑ i ∈ path x, a i)^2) ≤ len*mult*∑ i ∈ edges, (a i)^2 := by
  classical
  calc
    _ ≤ ∑ x ∈ roots, len * ∑ i ∈ path x, (a i)^2 := by
      apply sum_le_sum
      intro x hx
      have h : (∑ i ∈ path x, a i)^2 ≤ ((path x).card:ℝ)*∑ i ∈ path x, (a i)^2 := by
        simpa using sum_mul_sq_le_sq_mul_sq (path x) (fun _ ↦ (1:ℝ)) a
      exact h.trans (mul_le_mul_of_nonneg_right (hlen x hx) (sum_nonneg fun i _ ↦ sq_nonneg (a i)))
    _ = len * ∑ i ∈ edges, ∑ x ∈ roots, if i ∈ path x then (a i)^2 else 0 := by
      rw [← mul_sum, sum_comm]
      congr 1
      apply sum_congr rfl
      intro x hx
      rw [← sum_filter]
      congr 1
      ext i
      simp only [mem_filter]
      exact ⟨fun h ↦ ⟨cover x hx h,h⟩, fun h ↦ h.2⟩
    _ ≤ len * ∑ i ∈ edges, mult*(a i)^2 := by
      apply mul_le_mul_of_nonneg_left _ hl
      apply sum_le_sum
      intro i hi
      rw [← sum_filter]
      simp only [sum_const, nsmul_eq_mul]
      exact mul_le_mul_of_nonneg_right (hcount i hi) (sq_nonneg _)
    _ = _ := by rw [← mul_sum, mul_assoc]

/-- A central gauge flip on one time slice forces a transfer zero
mode whenever it negates every pairing with a nonzero vector. -/
theorem transferKernel {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℝ H]
    (T : H → H) (v : H) (nz : v ≠ 0) (hT : T 0 = 0)
    (flip : ∀ w, (@inner ℝ H _) w (T v) = -((@inner ℝ H _) w (T v))) :
    T v = 0 ∧ ¬ Function.Injective T := by
  have h : (@inner ℝ H _) (T v) (T v) = 0 := by linarith [flip (T v)]
  have hz : T v = 0 := inner_self_eq_zero.mp h
  exact ⟨hz, fun inj ↦ nz (inj (hz.trans hT.symm))⟩

/-- A self-adjoint transfer whose range is physical also kills the
orthogonal complement of the physical projection. -/
theorem boundaryProjection {M : Type*} [Monoid M] [StarMul M] (P T : M)
    (hp : star P = P) (ht : star T = T) (rangeIn : P*T=T) : T*P=T := by
  simpa only [star_mul, hp, ht] using congrArg star rangeIn
/-- A Schur root is a zero of the bordered matrix's scalar equation. -/
theorem rootIdentity (lam r g : ℝ) (h : lam-r-lam*g=0) :
    r = lam*(1-g) := by linarith

/-- Resolvent control traps the bottom mode between explicit quantities. -/
theorem rootBounds (a L r delta K : ℝ) (ha : 0 ≤ a)
    (hr : r = a*(1/L-delta)) (hd : 0 ≤ delta) (hu : delta ≤ r*K)
    (hk : 0 ≤ K) :
    (a/L)/(1+a*K) ≤ r ∧ r ≤ a/L := by
  constructor
  · apply (div_le_iff₀ (by positivity : 0 < 1+a*K)).2
    have eq : a/L = r + a*delta := by rw [hr]; ring
    rw [eq]
    nlinarith [mul_le_mul_of_nonneg_left hu ha]
  · rw [hr]
    have eq : a*(1/L-delta)=a/L-a*delta := by ring
    rw [eq]
    linarith [mul_nonneg ha hd]
/-- If two unnormalised densities have bounded relative distortion,
their normalized integrals inherit the same two factors. -/
theorem normalizedDistortion (a b m n u : ℝ) (hm : 0 < m) (hn : 0 < n)
    (hu : 0 ≤ u) (hb : 0 ≤ b) (hw : a ≤ u*b) (hz : n ≤ u*m) :
    a/m ≤ u^2*(b/n) := by
  apply (div_le_iff₀ hm).2
  apply (mul_le_mul_iff_of_pos_right hn).mp
  calc
    a*n ≤ (u*b)*n := mul_le_mul_of_nonneg_right hw hn.le
    _ ≤ (u*b)*(u*m) := mul_le_mul_of_nonneg_left hz (mul_nonneg hu hb)
    _ = (u^2*(b/n)*m)*n := by field_simp; ring

/-- Cubic error and the threshold for the random and identity shells. -/
theorem scaleExponents (L : ℝ) :
    (L^5)^3 = L^15 ∧ (L^7)^3 = L^21 ∧ (L^15)^2 = L^30 := by
  constructor
  · ring
  constructor <;> ring

/-- A uniform link bound and summed energy bound control the cubic Taylor cost. -/
theorem cubicBudget {ι : Type*} (edges : Finset ι) (a : ι → ℝ) (L E : ℝ)
    (hL : 0 ≤ L) (hE : 0 ≤ E)
    (point : ∀ i ∈ edges, a i ≤ L*E)
    (energy : ∑ i ∈ edges, (a i)^2 ≤ 32*L^3*E^2) :
    (∑ i ∈ edges, (a i)^3) ≤ 32*L^4*E^3 := by
  calc
    _ ≤ ∑ i ∈ edges, L*E*(a i)^2 := by
      apply sum_le_sum
      intro i hi
      calc
        _ = a i*(a i)^2 := by ring
        _ ≤ _ := mul_le_mul_of_nonneg_right (point i hi) (sq_nonneg _)
    _ ≤ (L*E)*(32*L^3*E^2) := by
      rw [← mul_sum]
      exact mul_le_mul_of_nonneg_left energy (mul_nonneg hL hE)
    _ = _ := by ring

end YangMills.DirichletBox
#print axioms YangMills.DirichletBox.gaugeForward
#print axioms YangMills.DirichletBox.congestion
#print axioms YangMills.DirichletBox.rootIdentity
#print axioms YangMills.DirichletBox.rootBounds
#print axioms YangMills.DirichletBox.normalizedDistortion
#print axioms YangMills.DirichletBox.scaleExponents
#print axioms YangMills.DirichletBox.transferKernel
#print axioms YangMills.DirichletBox.cubicBudget
#print axioms YangMills.DirichletBox.boundaryProjection
