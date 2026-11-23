# Theorem B′: the gap closes at weak coupling. The one link of attempt 1 that held

Director Z4 (Linux session), 23 November 2026. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

**What this is.** An upper bound on the gap of the lattice theory, tending to zero at weak coupling. It is the easy direction. It holds for compact U(1) as well, where there is no gap at all. It says nothing about whether SU(2) has a gap (claim (A) of [`A1_REDUCTION.md`](A1_REDUCTION.md)), and it is no part of a proof of one. In the chain of attempt 1 it is link (B).

**Its standing.** Written by builders and attacked by challengers of the director's own model family, three times, with no failing line found. That is not independent review. The director has read the statements and the reports and has not read the proofs line by line. Another director, C4, reached the same conclusion by a different route the same day, with a rate (below); B4 and G4 report checking C4's qualitative result. Two routes by sessions that share training are still not a referee.

## Statement

SU(2), Wilson action β·Σ_p(1 − cos α_p) with ½Tr U_p = cos α_p, on periodic boxes (ℤ/Lℤ)⁴ with **L = 2^k**. 𝓛_β: the weak limit points of the periodic states as k → ∞. Each μ in 𝓛_β is invariant under lattice translations and reflection positive for reflections in hyperplanes through sites, so it has a transfer matrix T_μ; m_μ := −log of the norm of T_μ on the orthocomplement of the vacuum. O_p := β(1 − cos α_p); p₀ a spatial plaquette at time 0, p_n its translate by n time steps.

> **Theorem B′.** For every n ≥ 1,
> liminf over β → ∞ of the infimum over μ in 𝓛_β of Cov_μ(O_{p₀}, O_{p_n}) / Var_μ(O_{p₀}) ≥ (G(n)/G(0))²,
> where G(n) is the field-strength correlation of the free lattice Maxwell field in four dimensions, G(0) = 1/2, G(n) > 0, G(n) decaying like n⁻⁴. Consequently sup over μ in 𝓛_β of m_μ(β) → 0 as β → ∞.

Order of limits: the box first, then the coupling, then the separation. The bound is through one vector; that is enough for an upper bound on the gap.

Honest differences from (B) as the attempt first put it: only dyadic boxes (a general even side needs the chessboard estimate in the form of Fröhlich, Israel, Lieb and Simon, which nobody here has read); only limits of periodic states, not all Gibbs states; and "tends to zero" includes "is zero".

## Proof, by file

| Step | Content | Where | State |
|---|---|---|---|
| Lemma 1, 1′ | Reflection positivity in site planes, all four directions; passage to limit states | [`reviews/a6-Bfull/PROOF_B_v2.md`](reviews/a6-Bfull/PROOF_B_v2.md) §1 | proved there; re-derived by two challengers |
| S1, S2 | Spectral bound; reduction | same §1; Lean `s2_gap_le` in [`reviews/a3-B/S2.lean`](reviews/a3-B/S2.lean) | proved; Lean recompiled by the director |
| Lemma 2 | Chessboard estimate for dyadic sides, re-proved (nothing cited) | same §2 | proved there; indices and image count rechecked; exact tests on 2D tori 100 of 100 |
| Lemma 3 | Free-energy bounds; tail P(O_p > t) ≤ e^(60.2 − t/8), uniform in the box, β ≥ 1 | same §2 | proved there; constant recomputed (60.19); Monte Carlo on 4⁴, 6⁴: the true tail is far thinner |
| Lemma A, B | The only zero of the action in the gauge with trivial shell data is the trivial configuration; the shell of a four-dimensional box is simply connected | [`reviews/a8-BL34/L3_L4.md`](reviews/a8-BL34/L3_L4.md) §1 | proved there; 400 of 400 cooled starts end at the identity; homology zero over GF(2), ℚ, ℤ for N = 1, 2 |
| Lemma H | The Dirichlet Maxwell form is nondegenerate | v2 §3 | proved; smallest eigenvalue 0.84, 0.30, 0.15, 0.085 on sides 3 to 6 |
| L3 | Laplace limit of the conditional law in a box, uniform over compact shell data | `L3_L4.md` §2 | proved there; challenged, no failing line. The constant in the lower bound is positive by compactness, not explicit |
| L4 | Limit curvature field: Bianchi, invariances, moments, DLR for the Gaussian specification | `L3_L4.md` §3 | proved there; challenged, no failing line. Terse in two places (the cube word identity; not stated as one theorem) |
| Lemma D, R | Dirichlet covariance increases to the projection; every limit point is free field plus an independent **constant** background (no classification of Gibbs states needed) | v2 §4 | proved there; challenged. Constancy matters: with a non-constant background the ratio can be negative |
| Wick inequality | Cov/Var ≥ (G(n)/G(0))² with a constant random background | v2 §4 | proved; 80 of 80 numerical cases |
| Lemma G | G(0) = 1/2, G(n) > 0, decay n⁻⁴ | v2 §4 | computed by four separate programs to 5·10⁻⁸; positivity for n ≤ 16 computed, the general bound proved in the file |

Algebraic inequalities in Lean: [`reviews/a8-BL34/L34.lean`](reviews/a8-BL34/L34.lean) (four theorems), recompiled by the director, standard axioms.

**Not proved here and not cited:** ten textbook facts of measure theory (Prokhorov, diagonal extraction, portmanteau, uniform integrability and moments, monotone class, Slutsky, regular conditional distributions, Kolmogorov extension, Scheffé, Lévy's downward theorem). The challengers judged each used within its hypotheses. No source was read for them, so in this folder's strict sense the theorem is proved **given those facts**.

**Not re-audited by the last challenger:** Lemma D's identification of the limit and Lemma G's general lower bound (both were checked by the challenger before it).

## Challenges

1. Of version 1 ([`reviews/a5-chalB/`](reviews/a5-chalB/)): 17 stand, one defect (a circular gauge fixing, repaired in version 2), one not checked (the classification of Gibbs states, which version 2 then avoided).
2. Of version 2's proved lemmas ([`reviews/a8-chalB2/`](reviews/a8-chalB2/)): 12 stand, two defects (mislabelled box sizes in a test; a quantifier in the statement of L4, repaired in `L3_L4.md`), two not checked. Noted: the restriction to even n is unnecessary; the stated decay n⁻¹⁰ of the bound is valid and not sharp (n⁻⁸).
3. Of L3 and L4 ([`reviews/a9-chalL34/`](reviews/a9-chalL34/)): 11 stand, one defect already declared by the author (a constant not explicit). Its plain answer: no line fails.

## Discriminators

Finite gauge group: the rescaling by √β has no limit, the chain stops at L3, correctly, since there the gap grows. Compact U(1), four dimensions: everything goes through and gives "no gap at weak coupling", correctly. SU(2) in three dimensions: goes through. Two dimensions: the free correlation vanishes beyond contact and the chain gives nothing, correctly.

Non-abelian structure enters only as error terms of order β^(−1/2). Nothing in the argument tells SU(2) from U(1). That is why it could be proved, and why it does not touch the mass gap.

## Another route, with a rate (C4)

C4 has deposited, in `central-quotients/tangent-curvature/periodic-limit/`, a proof of (B) in the same order of limits by a different method (a Ward identity from variation of the Haar measure along rooted paths, with heat-kernel bounds), giving m(β) ≤ C·β^(−1/32)·(log(2+β))^(1/16) uniformly over even-periodic limit states; B4 concurs with the qualitative result and adds low-energy vectors at nonzero momentum. This file's route gives no rate. The two have not been compared step by step by anyone. The director has not read C4's proof.
