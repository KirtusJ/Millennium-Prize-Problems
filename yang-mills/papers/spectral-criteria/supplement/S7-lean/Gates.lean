/-
Gates.lean. The algebra of the exceptional projection built from a gate (Corollary "Return bound
in the vacuum representation", last sentence): if `χ` and `P` are commuting self-adjoint idempotent
bounded operators on a real inner product space, then `B = χ (I - P)` is a self-adjoint idempotent
with `B P = 0`, and a bound `‖χ S χ u‖ ≤ p ‖u‖` for an operator `S` passes to `B`.
-/
import Mathlib

namespace Gates
open scoped InnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- A self-adjoint idempotent map does not increase the norm. -/
theorem proj_norm_le (R : E → E) (hsa : ∀ x y, ⟪R x, y⟫_ℝ = ⟪x, R y⟫_ℝ)
    (hid : ∀ x, R (R x) = R x) (x : E) : ‖R x‖ ≤ ‖x‖ := by
  have h : ‖R x‖ ^ 2 = ⟪x, R x⟫_ℝ := by
    rw [← real_inner_self_eq_norm_sq, hsa, hid]
  have h2 := real_inner_le_norm x (R x)
  rcases (norm_nonneg (R x)).eq_or_lt with h0 | h0
  · rw [← h0]; exact norm_nonneg _
  · have : ‖R x‖ * ‖R x‖ ≤ ‖R x‖ * ‖x‖ := by nlinarith
    exact le_of_mul_le_mul_left this h0

/-- the exceptional projection built from a gate: `B = χ (I - P)` -/
def gateB (χ P : E →L[ℝ] E) : E → E := fun x => χ (x - P x)

theorem gate_projection (χ P S : E →L[ℝ] E)
    (hχsa : ∀ x y, ⟪χ x, y⟫_ℝ = ⟪x, χ y⟫_ℝ) (hχid : ∀ x, χ (χ x) = χ x)
    (hPsa : ∀ x y, ⟪P x, y⟫_ℝ = ⟪x, P y⟫_ℝ) (hPid : ∀ x, P (P x) = P x)
    (hcomm : ∀ x, χ (P x) = P (χ x)) (p : ℝ)
    (hS : ∀ u, ‖χ (S (χ u))‖ ≤ p * ‖u‖) :
    (∀ x y, ⟪gateB χ P x, y⟫_ℝ = ⟪x, gateB χ P y⟫_ℝ) ∧
      (∀ x, gateB χ P (gateB χ P x) = gateB χ P x) ∧ (∀ x, gateB χ P (P x) = 0) ∧
      (∀ x, P (gateB χ P x) = 0) ∧ (∀ u, ‖gateB χ P (S (gateB χ P u))‖ ≤ p * ‖u‖) := by
  obtain ⟨B, hBdef⟩ : ∃ B : E → E, B = gateB χ P := ⟨_, rfl⟩
  rw [← hBdef]
  have hBx : ∀ x, B x = χ (x - P x) := fun x => by rw [hBdef]; rfl
  have hB1 : ∀ x, B x = χ x - P (χ x) := fun x => by
    rw [hBx, map_sub, hcomm]
  have hBP : ∀ x, B (P x) = 0 := fun x => by
    rw [hBx, hPid, sub_self, map_zero]
  have hPB : ∀ x, P (B x) = 0 := fun x => by
    rw [hB1, map_sub, hPid, sub_self]
  have hχB : ∀ x, χ (B x) = B x := fun x => by
    rw [hBx, hχid]
  have hBχ : ∀ x, B (χ x) = B x := fun x => by
    rw [hB1, hB1, hχid]
  have hBid : ∀ x, B (B x) = B x := fun x => by
    rw [hB1 (B x), hχB, hPB, sub_zero]
  have hBsa : ∀ x y, ⟪B x, y⟫_ℝ = ⟪x, B y⟫_ℝ := fun x y => by
    rw [hB1, hB1, inner_sub_left, inner_sub_right, hχsa, hPsa, hχsa, hcomm]
  refine ⟨hBsa, hBid, hBP, hPB, ?_⟩
  intro u
  -- B S B u = (I - P) χ S χ (B u), and both outer maps are contractions
  have e1 : B (S (B u)) = χ (S (χ (B u))) - P (χ (S (χ (B u)))) := by
    rw [hχB, hB1 (S (B u))]
  have hIP : ∀ v : E, ‖v - P v‖ ≤ ‖v‖ := fun v => by
    have := proj_norm_le (fun x => x - P x)
      (fun x y => by simp only; rw [inner_sub_left, inner_sub_right, hPsa])
      (fun x => by simp only; rw [map_sub, hPid, sub_self, sub_zero]) v
    simpa using this
  have hBu : ‖B u‖ ≤ ‖u‖ := proj_norm_le B hBsa hBid u
  have hp : 0 ≤ p ∨ B u = 0 := by
    by_cases hz : B u = 0
    · exact Or.inr hz
    · left
      have h := hS (B u)
      have hn : 0 < ‖B u‖ := norm_pos_iff.mpr hz
      by_contra hneg
      push_neg at hneg
      have : p * ‖B u‖ < 0 := mul_neg_of_neg_of_pos hneg hn
      linarith [norm_nonneg (χ (S (χ (B u))))]
  rcases hp with hp | hz
  · calc ‖B (S (B u))‖ = ‖χ (S (χ (B u))) - P (χ (S (χ (B u))))‖ := by rw [e1]
      _ ≤ ‖χ (S (χ (B u)))‖ := hIP _
      _ ≤ p * ‖B u‖ := hS (B u)
      _ ≤ p * ‖u‖ := mul_le_mul_of_nonneg_left hBu hp
  · have : B (S (B u)) = 0 := by
      rw [hz, map_zero, hBx]; simp
    rw [this, norm_zero]
    have h := hS u
    have h0 := hS 0
    simp at h0
    -- p ‖u‖ ≥ ‖χ S χ u‖ ≥ 0
    exact (norm_nonneg _).trans h

end Gates

#print axioms Gates.gate_projection
