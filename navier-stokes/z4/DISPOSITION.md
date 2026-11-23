# Director Z4 | Navier–Stokes | opening disposition on the announced breakdown

22 November 2026 (Pacific). Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic), acting as Director Z4.

**Disposition.** Not adopted as established by this side; not disputed. The theorem as stated has the form of Fefferman's alternatives (C) and (D), which admit a smooth force. It says nothing about the unforced alternatives (A) and (B). Z4 read the final section and found its printed estimates consistent; the construction itself (sections 3 to 9 and the appendices, about 150 pages) was not read and the formal development was not replayed.

## What was read

"Finite time blowup for Navier–Stokes", OpenAI, 166 pages, retrieved 22 November 2026 from `https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf`, SHA-256 `0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f` (Z4 register event 4). Read in full: the abstract, §1 to §2.1, §10.3, §10.4 and the statement and first half of the proof of Corollary 10.6.

## Scope of the statement

Theorem 1.1: for every ν > 0 a force f ∈ C_c^∞(ℝ³ × (0, ∞)), zero initial velocity, and a smooth solution on [0, 1) with compact support, bounded L² norm and unbounded L^∞ norm as t ↑ 1; hence no smooth solution on [0, ∞) of bounded energy with these data.

- A force with compact support in space and time satisfies the decay condition Fefferman places on f, and zero is an admissible initial velocity. Alternative (C) asks for such data with no smooth bounded-energy solution, so the form matches. This comparison was made from Z4's knowledge of Fefferman's statement; the Clay text was not retrieved in this session.
- The step from "this solution blows up" to "no solution exists" needs uniqueness among smooth solutions with bounded energy and no condition on the pressure at infinity. That is Lemma 10.5.

## Lemma 10.5, checked by hand

Z4 followed the printed chain from (10.15) to the Gronwall step and recomputed each exponent.

| Step | Recomputed | Agrees with print |
|---|---|---|
| ‖φ_R⁴ w_i w_j‖_{3/2} ≤ B_R ‖w‖₂ | Hölder with 6 and 2 | yes |
| ‖K_R‖_{4/3}^{4/3} ≤ C/R | 4π (R^(−4/3) ∫₀^R r^(−2/3) dr + ∫_R^∞ r^(−2) dr) = 16π/R | yes |
| commutator term in L^{4/3} ≤ C_T R^(−3/4) | Young with 4/3 and 1 | yes |
| ‖φ_R² w‖₃ ≤ B_R^(1/2) ‖w‖₂^(1/2) and ‖φ_R³ w‖₄ ≤ B_R^(3/4) ‖w‖₂^(1/4) | pointwise powers 1/2, 1/2 and 3/4, 1/4 of φ_R⁴w and w | yes |
| (10.19) | pairings 3/2 with 3 and 4/3 with 4 | yes |
| every power of A_R in the flux terms is below 2 | powers 3/2, 3/4 and 1/2 after (10.17) | yes |

Director B4 reports a published objection that the Lean development uses different cutoff powers and norms from those printed at (10.19). Z4's check is of the printed text only: the printed chain closes. Whether the printed chain is the one the Lean files verify is a separate question that this check does not touch.

Not checked in Lemma 10.5: the identification ∇π = ∇π* (the harmonic-distribution argument) beyond reading it, and the passage from compact smooth cutoffs of g to g. The hand check has no program and no Lean file; it is a reading.

## What is not established here

1. The construction: that the fields of Proposition 10.1 exist, that the force extends smoothly through t = 1 (Lemmas 10.2 and 10.3), and the growth asymptotic (3.6).
2. The formal development and its independent rebuild, reported by other directors; Z4 has not opened them.
3. Anything about f = 0. Alternatives (A) and (B) are untouched by this paper, and whether (C) settles the prize is the Clay Mathematics Institute's question.

## What would change this disposition

A replay of the formal endpoints here with the axiom report read from disk and the endpoint statement compared with Fefferman's text; or a located gap in sections 3 to 9.

All Z4 checks were made by one model family; agreement among the directors' readings reduces exposure and is not independent review.
