/-
OneSeparation.lean. The test at one time separation (Proposition "A test at one time separation")
on a finite-dimensional real inner product space: for a symmetric linear map `S` and a real `r`,
with `r ≤ 1`, `S` has no eigenvalue in the open interval `(r, 1)` if and only if
`(1 + r) ⟪v, S v⟫ - ⟪v, S (S v)⟫ ≤ r ⟪v, v⟫` for every `v`.
(In the paper `S = e^{-τH}`, so eigenvalues of `S` in `(r,1)` are eigenvalues of `H` in `(0, Δ)`.)
The definitions `Apow`, `Apow_quad`, `map_eigsum`, `pow_eq_Apow` are copied from Discrete.lean.
-/
import Mathlib

namespace OneSeparation
open Real
open scoped BigOperators InnerProductSpace

set_option linter.unusedSectionVars false
variable {ι E : Type*} [Fintype ι] [DecidableEq ι] [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- `A^n` defined from spectral data: `A^n w = Σ_i mu_i^n ⟪e_i, w⟫ e_i`. -/
noncomputable def Apow (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (n : ℕ) (w : E) : E :=
  ∑ i, (mu i ^ n * ⟪e i, w⟫_ℝ) • e i

theorem Apow_quad (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ) (n : ℕ) (w : E) :
    ⟪w, Apow e mu n w⟫_ℝ = ∑ i, mu i ^ n * ⟪e i, w⟫_ℝ ^ 2 := by
  unfold Apow; rw [inner_sum]; refine Finset.sum_congr rfl fun i _ => ?_
  rw [inner_smul_right, real_inner_comm]; ring

theorem map_eigsum (A : E →ₗ[ℝ] E) (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ)
    (hAe : ∀ i, A (e i) = mu i • e i) (c : ι → ℝ) :
    A (∑ i, c i • e i) = ∑ i, (mu i * c i) • e i := by
  rw [map_sum]; refine Finset.sum_congr rfl fun i _ => ?_
  rw [map_smul, hAe, smul_smul, mul_comm]

theorem pow_eq_Apow (A : E →ₗ[ℝ] E) (e : OrthonormalBasis ι ℝ E) (mu : ι → ℝ)
    (hAe : ∀ i, A (e i) = mu i • e i) (n : ℕ) (w : E) :
    (A ^ n) w = Apow e mu n w := by
  induction n with
  | zero =>
    unfold Apow; simp only [pow_zero, one_mul]
    exact (e.sum_repr' w).symm
  | succ n ih =>
    rw [pow_succ']; show A ((A ^ n) w) = _
    rw [ih]; unfold Apow
    rw [map_eigsum A e mu hAe]
    refine Finset.sum_congr rfl fun i _ => ?_
    rw [pow_succ, ← mul_assoc, mul_comm (mu i) (mu i ^ n)]


theorem one_separation [FiniteDimensional ℝ E] (S : E →ₗ[ℝ] E) (hS : S.IsSymmetric) (r : ℝ)
    (hr : r ≤ 1) :
    (∀ i, ¬ (r < hS.eigenvalues rfl i ∧ hS.eigenvalues rfl i < 1)) ↔
      ∀ v : E, (1 + r) * ⟪v, S v⟫_ℝ - ⟪v, S (S v)⟫_ℝ ≤ r * ⟪v, v⟫_ℝ := by
  classical
  set e := hS.eigenvectorBasis (n := Module.finrank ℝ E) rfl with he
  set mu : Fin (Module.finrank ℝ E) → ℝ := fun i => hS.eigenvalues rfl i with hmu
  have hSe : ∀ i, S (e i) = mu i • e i := fun i => by
    have := hS.apply_eigenvectorBasis (n := Module.finrank ℝ E) rfl i
    simp only [he, hmu]; exact this
  have hpow : ∀ n u, (S ^ n) u = Apow e mu n u := fun n u => pow_eq_Apow S e mu hSe n u
  -- the three quadratic forms in the eigenbasis
  have q0 : ∀ v : E, ⟪v, v⟫_ℝ = ∑ i, ⟪e i, v⟫_ℝ ^ 2 := fun v => by
    have := Apow_quad e mu 0 v
    rw [← hpow] at this; simpa using this
  have q1 : ∀ v : E, ⟪v, S v⟫_ℝ = ∑ i, mu i * ⟪e i, v⟫_ℝ ^ 2 := fun v => by
    have := Apow_quad e mu 1 v
    rw [← hpow] at this; simpa using this
  have q2 : ∀ v : E, ⟪v, S (S v)⟫_ℝ = ∑ i, mu i ^ 2 * ⟪e i, v⟫_ℝ ^ 2 := fun v => by
    have := Apow_quad e mu 2 v
    rw [← hpow] at this
    have e2 : (S ^ 2) v = S (S v) := by rw [pow_two]; rfl
    rw [e2] at this; exact this
  have key : ∀ v : E, r * ⟪v, v⟫_ℝ - ((1 + r) * ⟪v, S v⟫_ℝ - ⟪v, S (S v)⟫_ℝ)
      = ∑ i, (r - mu i) * (1 - mu i) * ⟪e i, v⟫_ℝ ^ 2 := fun v => by
    rw [q0, q1, q2, Finset.mul_sum, Finset.mul_sum, ← Finset.sum_sub_distrib,
      ← Finset.sum_sub_distrib]
    refine Finset.sum_congr rfl fun i _ => ?_
    ring
  constructor
  · intro h v
    have hnn : 0 ≤ ∑ i, (r - mu i) * (1 - mu i) * ⟪e i, v⟫_ℝ ^ 2 := by
      refine Finset.sum_nonneg fun i _ => ?_
      have hi := h i
      have : 0 ≤ (r - mu i) * (1 - mu i) := by
        by_cases h1 : mu i ≤ r
        · by_cases h2 : mu i ≤ 1
          · exact mul_nonneg (by linarith) (by linarith)
          · exfalso; push_neg at h2; linarith
        · push_neg at h1
          have h2 : 1 ≤ mu i := by
            by_contra! hc; exact hi ⟨h1, hc⟩
          exact mul_nonneg_of_nonpos_of_nonpos (by linarith) (by linarith)
      exact mul_nonneg this (sq_nonneg _)
    have := key v
    linarith
  · intro h i hi
    have hk := key (e i)
    have hv := h (e i)
    have hsum : ∑ j, (r - mu j) * (1 - mu j) * ⟪e j, e i⟫_ℝ ^ 2 = (r - mu i) * (1 - mu i) := by
      rw [Finset.sum_eq_single i]
      · rw [real_inner_self_eq_norm_sq, e.orthonormal.1 i]; ring
      · intro j _ hj; rw [e.orthonormal.2 hj]; ring
      · simp
    rw [hsum] at hk
    have hneg : (r - mu i) * (1 - mu i) < 0 :=
      mul_neg_of_neg_of_pos (by linarith [hi.1]) (by linarith [hi.2])
    linarith

end OneSeparation

#print axioms OneSeparation.one_separation
