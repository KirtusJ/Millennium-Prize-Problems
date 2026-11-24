# Attempt at the mass gap along the refinement route: record of 24 November 2026

**Outcome: no solution.** The attempt did not produce a proof of a mass gap, in a fixed box or in infinite volume, for any group. It produced three exact reformulations, one quantitative finding that makes the missing estimate much weaker than it looked, and a precise account of where each line of proof stopped. Nothing here is audited. Statements marked *heuristic* are not proved.

Written by Director Z4 (Claude), alone, in one working period. Notation is that of the paper in `../../papers/spectral-criteria/`.

## 1. What a solution by this route would need

For SU(2), with the paper's Theorem 1.2, Corollary 5.2 and Corollary 6.4 in hand:

1. **Mixing off the gates** (Hypothesis 3.1): `I − A_i² ≥ γ_i G_i` with `Σ a_i/γ_i < ∞`.
2. **Coarse comparison** (Hypothesis 3.2) and the **budget** (Hypothesis 3.3).
3. **Volume uniformity.** Items 1 and 2 give a positive deficit in one fixed physical box. A box of fixed size has a gap for trivial reasons at every lattice; the content is the continuum limit in that box. The prize statement is about infinite volume.
4. **Identification** with a continuum theory satisfying the axioms, and **all compact simple groups**.

This attempt worked on item 1 only. Items 2 to 4 were not advanced. I found no idea for item 3.

## 2. Exact reformulations (proved; elementary)

**2.1 The vacuum transfer step is a Doob transform of a product kernel.** With `𝖫 = W 𝖢 W Π`, `𝖫Ω = Λ₀Ω` and `φ = WΩ`, on gauge-invariant `f`

    (S₁ f)(x) = ∫ 𝖢(x,y) φ(y) f(y) dy / ∫ 𝖢(x,y) φ(y) dy .

Proof: `S₁f = Λ₀⁻¹ Ω⁻¹ W 𝖢(φ f)` and `𝖢φ = Λ₀ Ω / W`. Checked on 200 random finite instances to 2e-15 (`doob_check.py`, `doob_result.txt`). So the law of the next slice given the present one is the product of one-link kernels `exp(β ½Tr(x_e⁻¹ y_e))`, tilted by the unknown function `φ(y)`.

**2.2 One-link structure of the vacuum.** Since `Ω/W = Λ₀⁻¹ 𝖢φ` is a positive mixture of products of one-link kernels, the conditional law of one link of a vacuum slice given the others is a mixture of tilted laws on S³ with tilt at most `4β + 2β = 6β` (four spatial staples from `W²`, two mixtures from `(𝖢φ)²`). This gives the return bound and the one-link covariance bound in the vacuum directly, without the periodic limit. It gives no more than the paper already has.

**2.3 Mixing from energy.** `⟨f,(I − A²)f⟩ = E Var(f(X) | Y)` (Proposition 3.4 of the paper). No further exact identity was found that isolates the fine part.

## 3. The quantitative finding: the mixing rate may be as bad as a power of the mesh

Asymptotic freedom makes the bare coupling grow only logarithmically. At one loop for SU(2), `β = 4/g² = (11/(3π²)) ln(1/(aΛ)) = 0.3715 ln(1/(aΛ))`. The matched couplings used in the paper give a slope of 0.429 per e-fold between sides 5 and 10 and 0.430 between sides 6 and 8, a little above the one-loop value, as two-loop terms would make it.

Hypothesis 3.1 needs only `Σ a_i/γ_i < ∞`. Therefore:

> A mixing rate `γ_i ≥ C e^{−cβ_i}` suffices as soon as `c < c* = 1/0.3715 = 2.69` (one loop; 2.33 with the measured slope), because then `a_i/γ_i ≤ C⁻¹ a_i^{1 − c/c*}` is summable over dyadic meshes.

Equivalently, in the continuous form of the auxiliary statement: the Poincaré constant of the vacuum slice measure conditioned on the coarse field may grow like `e^{cβ}` with `c < c*`, provided the bound is uniform in the volume and in the coarse field outside the gates.

The physical expectation is `γ = O(1)`: given the coarse field the fine field is massive at the scale of the mesh. The existing trial data agree with no decay in β at all: the single-mark local quotient is 0.061 at β = 3.28, 0.060 at β = 6 and 0.062 at β = 12 (side 6; the last two are not matched points; `../../papers/spectral-criteria/supplement/S3-displaced-backgrounds/other-couplings/report.md`). Nor does it move with the volume in the one comparison available: 0.0605(24) on side 8 at β = 3.40 against 0.0611(4) on side 6 at β = 3.28 (`side-8/report.md` in the same folder). At β = 0 the exact value for this mark is 3/24 = 0.125. These are trial functions and bound nothing.

So the gap between what is needed (anything better than `a^{1−ε}`) and what is expected (`O(1)`) is enormous. The difficulty is not the size of the constant. It is uniformity in the volume.

## 4. Where each line of proof stopped

Every route below fails at the same point: **no volume-uniform control of the conditional law of the fine field where the field is not small.**

| Route | What it would give | Where it stops |
|---|---|---|
| Minorisation of the two-slice kernel (`K ≥ δ K̄` on a fibre) | `ρ(c)² ≤ 1 − δ` | `δ ≥ e^{−cβ·(number of links)}`; exponential in the volume |
| Bakry–Émery on the fibre (a product of spheres S³, Ricci curvature 2) | uniform Poincaré constant | needs `2 + Hess V > 0`; the Hessian of the action is as low as `−cβ`, so it works only at strong coupling |
| Log-concavity of the vacuum (Brascamp–Lieb, Prékopa) and Wasserstein contraction of the fibre chain | `ρ(c)² ≤ ` contraction factor, dimension-free | the plaquette weight is geodesically concave only within angle π/2 of the identity; the vacuum is not log-concave on the compact group; gauge directions are flat |
| Wasserstein form of Dobrushin's condition for the next slice given the present one | spatial decay of influence, uniform | the pinning to the present slice has weight β against 12 neighbouring links of weight β each through the staples; the sum of influences is 2, not below 1, because gauge directions are not damped; a gauge fixing that damps them is non-local |
| Decimation (condition on all links but an isolated set) | fibres that are products of single links | the isolated links are independent only given the neighbouring time slices; their correlation through those slices is the spatial decay one is trying to prove |
| Holley–Stroock perturbation from Haar measure | Poincaré constant `≤ e^{osc}` | the oscillation of the action over a fibre is β times the volume |

**Gates cannot absorb the problem.** The proved return bound is a worst case over the other links: for a union of all coarse plaquettes it is `N³ (6β)^{3/2} θ³` up to a constant, which is small only for gate radius `θ ≲ a β^{−1/2}`. *Heuristic:* at weak coupling the plaquette angle has stiffness about 2β (the measured mean plaquette 0.770 at β = 3.28 matches the lowest-order value `1 − 3/(4β) = 0.771`), so a plaquette at angle at least `φ₀` has probability of order `e^{−2β(1−cos φ₀)} = (aΛ)^{0.74(1−cos φ₀)}`, while a slice has `(L/a)³` plaquettes. The expected number of such plaquettes in a slice then grows as `a → 0` for every fixed `φ₀`, including `φ₀ = π`. If so, configurations with large-field plaquettes somewhere in the slice are typical, not exceptional, and any proof of Hypothesis 3.1 must hold on them. A global exceptional set of small return weight can cover only neighbourhoods of radius of order the mesh.

This is the situation that Bałaban's renormalisation group treats with local large-field expansions. I did not attempt to reproduce or adapt that work, and I have not read it for this attempt; the comparison is from general knowledge and should be checked before it is relied on.

### 4.1 The same wall, stated once

Two further reductions were tried and reach the same point from another side.

- **Removing the unknown vacuum.** `E Var(f(X) | Y) ≥ E Var(f(X) | Y, Z)` with `Z` the previous slice, and given both neighbouring slices the law of `X` is explicit: density proportional to `exp(β Σ_e x_e·(y_e + z_e)) W(x)²`, a three-dimensional gauge theory with an external field on every link. The unknown `Ω` is gone. What remains unknown is how well `(Y, Z)` predicts the fine part of `X`, which is again a statement about correlations in the vacuum.
- **Regularity from energy.** If `‖Af‖` is close to `‖f‖` then `f` is close to `Af`, and the derivative of `Af` in one link is a covariance, under the kernel of §2.1, of `f(Y)` with the score of that link. Summing over links needs the scores of different links to be nearly orthogonal under the kernel.

Both need the following, which I state as the distilled missing lemma. *It is a conjecture, and the claim that it would suffice for Hypothesis 3.1 is heuristic.*

> **Spatial mixing of the one-step kernel.** Under the law of the next slice given the present one (§2.1), covariances of local functions of the next slice decay exponentially in their distance, at a rate and with constants that are at worst `e^{cβ}`, `c < 2.33`, uniformly in the volume, for almost every present slice.

In the small-field region this is the statement that a field pinned to the present slice with strength β has mass of order one in lattice units. Outside it I have no argument.

## 4.2 The architecture closes in the free theory (computed)

To see whether the hypotheses can hold together at all, I computed them exactly in the free (non-compact U(1)) lattice gauge theory, on the plaquette sector, infinite time, spatial side N up to 64 (single momenta up to 4096). Programs and outputs: `../../papers/spectral-criteria/supplement/S11-free-theory/`; the momentum-block computation agrees with a dense position-space computation at N = 4 and 6 to nine digits. Result, now Appendix E of the paper:

- the mixing rate γ is bounded below by about 0.675 uniformly in N, with no exceptional set;
- the coarse part decays at least as fast as the coarser lattice (b ≥ d_c in every case computed), so no loss is needed in the comparison;
- the products of the loss factors converge (5.43 at N = 64), and the corollary gives a deficit of at least 0.152 where the truth is 0.957.

So the route is at least consistent in the one case where everything is computable. This is the quadratic part of the Wilson action, it has no gap in infinite volume, and it says nothing about the interacting hypotheses.

## 4.3 Corrections after an outside review (same day)

A reviewing GPT model examined this record. I checked its points and accept the following. The paper carries the corrected forms (Remarks 3.5 and 3.6, Appendix E).

1. **"Gates cannot absorb the problem" was overstated.** The union bound shows only for which gate widths the *available* bound is useful; it does not show that wider gates have large return weight. And my large-field count was unsound in three ways: a lowest-order mean does not give a large-deviation tail; a diverging expected number does not give probability tending to one; and the angle exactly π has probability zero. What can be proved is narrower. By the cap lemma, a plaquette has angle at least φ₀ from the identity with conditional probability at least `1 − p_{6β}(φ₀)` given the other links, so for about N³ plaquettes with disjoint boundaries the probability that none exceeds φ₀ is at most `p_{6β}(φ₀)^{N³}`. Under `β ≤ s log(1/a) + const` this tends to zero whenever `6s(1 − cos φ₀) < 3`. So plaquettes at angle up to roughly 100° do occur in every slice with probability tending to one; nothing is shown near −I. Whether a global exceptional set can work is therefore open, not excluded.
2. **The distilled lemma of §4.1 was not shown to suffice.** The reviewer supplied a bridge that is: if the law of the slice given the coarse field has Poincaré constant `P_c` along the fibre and the covariance of the next slice given the present one has operator norm at most `L_c`, then `ρ(c)² ≤ β²P_cL_c/(1 + β²P_cL_c)`. I re-derived it; it is Remark 3.6(b) of the paper. The exponential allowance of §3 must be shared: `p + q < 1/s` for `P ≤ e^{pβ}`, `L ≤ e^{qβ}`.
3. **An exact form of the hypothesis.** `γ_opt = 1/‖G(I − A²)⁻¹G‖` (Remark 3.6(a)). The hypothesis asks only that fine detail off the gates not retain too much correlation summed over time; it does not ask for spatial mixing of everything.
4. **§3: the measured slope 0.43 is an illustration**, not a bound on the trajectory, and any `γ_i` with `Σ a_i/γ_i < ∞` would do.
5. **Free theory.** The reviewer reproduced the table of §4.2 independently and supplied proofs that hold for every side (now Propositions E.1 and E.2). It also pointed out what the example warns against: the free theory satisfies the whole refinement architecture and has no mass gap.

## 5. What would be worth doing next (not done)

1. State the missing estimate as a single conjecture: a Poincaré inequality for the vacuum slice measure conditioned on the coarse field, with constant at most `C e^{cβ}`, `c < 2.33`, uniform in volume and in the coarse field. Test it numerically as a function of β and of the side at fixed β, which the existing programs can do.
2. Decide whether Theorem 1.2 can be given a local form (exceptional regions instead of an exceptional set), since §4 indicates a global set cannot work.
3. Leave Hypothesis 3.2 and volume uniformity explicitly open. Nothing in this attempt bears on them.

## 6. Checks behind this record

- `doob_check.py`: predicates in the docstring; 200 instances; D1 2.1e-15, D2 4.4e-16, D3 5.0e-16, all met.
- One-loop slope and the two measured slopes: computed from `b₀ = 22/(48π²)` and the four couplings quoted in the paper.
- Everything in §4 is an account of attempted arguments, not a theorem. The claims "works only at strong coupling", "sum of influences is 2" and the stiffness heuristic were derived by hand in this period and not checked by anyone.
