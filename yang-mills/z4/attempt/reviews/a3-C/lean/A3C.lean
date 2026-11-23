import Mathlib

/-! Worker a3-C: finite-sum / discrete algebra used in PROOF.md steps 2 and 3. -/

namespace A3C

open Finset Real

/-- Step 2 (discrete form of (C') ⇒ (C)): if one lattice step never loses more than the
factor q of the correlation (consequence of log-convexity, q = C(1)/C(0)), then
q^k · C(n) ≤ C(n+k). -/
theorem step_chain (C : ℕ → ℝ) (q : ℝ) (hq : 0 ≤ q)
    (h : ∀ n, q * C n ≤ C (n + 1)) : ∀ k n, q ^ k * C n ≤ C (n + k) := by
  intro k
  induction k with
  | zero => intro n; simp
  | succ k ih =>
    intro n
    have h1 := ih n
    have h2 := h (n + k)
    calc q ^ (k + 1) * C n = q * (q ^ k * C n) := by ring
      _ ≤ q * C (n + k) := mul_le_mul_of_nonneg_left h1 hq
      _ ≤ C (n + k + 1) := h2
      _ = C (n + (k + 1)) := by rw [Nat.add_assoc]

/-- Termwise bound used in step 3 (spectral weight ⇒ (C)). -/
theorem term_bound (E K : ℝ) (hE : E ≤ K) :
    exp (-E / 2) ≤ exp (K / 2) * exp (-E) := by
  rw [← exp_add]; apply exp_le_exp.mpr; linarith

/-- Step 3, finite-sum version: if the damped weight above K is at most B times the weight
below K at time ξ, then C(ξ/2) ≤ (e^{K/2} + B) C(ξ).  (Energies in units of the gap.) -/
theorem weight_implies_C {ι : Type*} (s : Finset ι) (w E : ι → ℝ) (K B : ℝ)
    (hw : ∀ i ∈ s, 0 ≤ w i)
    (hB : ∑ i ∈ s.filter (fun i => ¬ E i ≤ K), w i * exp (-E i / 2)
          ≤ B * ∑ i ∈ s.filter (fun i => E i ≤ K), w i * exp (-E i))
    (hB0 : 0 ≤ B) :
    ∑ i ∈ s, w i * exp (-E i / 2) ≤ (exp (K / 2) + B) * ∑ i ∈ s, w i * exp (-E i) := by
  rw [← sum_filter_add_sum_filter_not s (fun i => E i ≤ K)]
  rw [← sum_filter_add_sum_filter_not s (fun i => E i ≤ K) (fun i => w i * exp (-E i))]
  have hlo : ∑ i ∈ s.filter (fun i => E i ≤ K), w i * exp (-E i / 2)
      ≤ exp (K / 2) * ∑ i ∈ s.filter (fun i => E i ≤ K), w i * exp (-E i) := by
    rw [mul_sum]; apply sum_le_sum; intro i hi
    rw [mem_filter] at hi
    have := term_bound (E i) K hi.2
    nlinarith [hw i hi.1, exp_pos (-E i)]
  have hhi0 : 0 ≤ ∑ i ∈ s.filter (fun i => ¬ E i ≤ K), w i * exp (-E i) := by
    apply sum_nonneg; intro i hi; rw [mem_filter] at hi
    exact mul_nonneg (hw i hi.1) (exp_pos _).le
  have hlo0 : 0 ≤ ∑ i ∈ s.filter (fun i => E i ≤ K), w i * exp (-E i) := by
    apply sum_nonneg; intro i hi; rw [mem_filter] at hi
    exact mul_nonneg (hw i hi.1) (exp_pos _).le
  have hK : 0 ≤ exp (K / 2) := (exp_pos _).le
  nlinarith [mul_nonneg hK hhi0, mul_nonneg hB0 hhi0]

end A3C

#print axioms A3C.step_chain
#print axioms A3C.weight_implies_C
