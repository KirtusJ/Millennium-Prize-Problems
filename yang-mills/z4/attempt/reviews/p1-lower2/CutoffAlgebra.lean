import Mathlib

/-- Cut-off algebra of Lemma S4 (TUNNEL_LOWER2.md): with G = c1 + gt, E = c2 + et,
lower bound A1 for T(GE)/(GE), upper bounds A2 for T(E), A3 for T(G),
(A1*G*E - A2*c1*E - A3*c2*G) - lam*(G-c1)*(E-c2) equals the four-term expansion. -/
theorem cutoff_identity (gt et c1 c2 A1 A2 A3 lam : ℝ) :
    (A1 * (c1 + gt) * (c2 + et) - A2 * c1 * (c2 + et) - A3 * c2 * (c1 + gt))
      - lam * gt * et
    = gt * et * (A1 - lam) + c1 * et * (A1 - A2) + c2 * gt * (A1 - A3)
      + c1 * c2 * (A1 - A2 - A3) := by
  ring

/-- Positivity consequence used in the three regimes. -/
theorem cutoff_pos (gt et c1 c2 A1 A2 A3 lam : ℝ)
    (h : 0 ≤ gt * et * (A1 - lam) + c1 * et * (A1 - A2) + c2 * gt * (A1 - A3)
      + c1 * c2 * (A1 - A2 - A3)) :
    lam * gt * et ≤ A1 * (c1 + gt) * (c2 + et) - A2 * c1 * (c2 + et) - A3 * c2 * (c1 + gt) := by
  have := cutoff_identity gt et c1 c2 A1 A2 A3 lam
  linarith

/-- Valley energy increment bound used for D: for 0 ≤ s ≤ S, S - s ≤ (S^2 - s^2)/(2 s) when s > 0. -/
theorem sqrt_increment (s S : ℝ) (hs : 0 < s) (hS : s ≤ S) :
    S - s ≤ (S ^ 2 - s ^ 2) / (2 * s) := by
  rw [le_div_iff₀ (by linarith)]
  nlinarith [sq_nonneg (S - s)]

#print axioms cutoff_identity
#print axioms cutoff_pos
#print axioms sqrt_increment
