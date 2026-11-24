# S14: a non-abelian toy with finite subgroups of SU(2)

Lattice gauge theory in 2+1 dimensions on a spatial torus of 2 × 1 sites, gauge group the binary octahedral (48 elements) or binary icosahedral (120 elements) subgroup of SU(2), blocked by two in the long direction. Four links; the gauge-invariant functions live on 4,888 or 29,288 orbits. A toy, and a stand-in: a finite subgroup is not SU(2), and the two groups are compared to see where it stops behaving like one. Nothing here bears on the open hypotheses.

| File | Content |
|---|---|
| `ladder.py`, `ladder_result.txt` | program and output; controls L0, L1, L2 met. Command: `python3 ladder.py ladder_result.txt 2O:1.0,2.0,3.0,4.0,5.0 2I:1.0,2.0,3.0,4.0,5.0,6.0,8.0` |
| `PREDICTION.md` | expectation committed before the run |

## Result

| β | group | lattice gap | weight of the lowest state in the fine detail | weight / energy | γ_opt |
|---|---|---|---|---|---|
| 1 | 2O / 2I | 1.00891 / 1.00896 | 0.2541 / 0.2541 | 0.2518 / 0.2518 | 0.94892 / 0.94892 |
| 2 | 2O / 2I | 0.2390 / 0.2431 | 0.0737 / 0.0748 | 0.308 / 0.308 | 0.8773 / 0.8780 |
| 3 | 2O / 2I | 0.0240 / 0.0384 | 0.0091 / 0.0138 | 0.379 / 0.358 | 0.8375 / 0.8453 |
| 4 | 2O / 2I | 5.3e-4 / 5.9e-3 | 3.0e-4 / 2.5e-3 | 0.561 / 0.424 | 0.7796 / 0.8222 |
| 5 | 2O / 2I | 1.2e-5 / 9.2e-4 | 8.0e-6 / 4.5e-4 | 0.673 / 0.494 | 0.7480 / 0.7998 |
| 6 | 2I | 9.9e-5 | 5.7e-5 | 0.574 | 0.7758 |
| 8 | 2I | 2.4e-7 | 1.7e-7 | 0.697 | 0.7413 |

For 2O the constant `κ = ‖GH⁻¹G‖` was computed by full diagonalisation: 0.631, 0.782, 0.784, 0.857, 0.915 at β = 1 to 5.

## Reading

- **Where the stand-in holds.** The two groups agree to 5e-5 in the gap at β = 1 and to 1.7 per cent at β = 2; at β = 3 they differ by 37 per cent in the gap and 0.9 per cent in γ_opt, and beyond that the gaps differ by an order of magnitude. So only β ≤ 2, and with reservations β = 3, say anything about SU(2). The collapse of the gap at larger β is at least in part an effect of the finite group (a discrete set of flat configurations between which the system tunnels) and its size must not be attributed to SU(2).
- **What is the same in both groups at every coupling.** The lowest excited state is, to 99 per cent, the function `Tr c + Tr d` times the vacuum: one unit of centre flux through the short direction (identified by overlaps for 2O at β = 2 and 4; a script in the session, not deposited). Its weight in the fine detail follows its energy down through six orders of magnitude: the ratio rises only from 0.25 to 0.70 while the energy falls from 1 to 2e-7. γ_opt decreases slowly, to 0.74 at β = 8, and κ stays below 1 for 2O up to β = 5.
- **Against `PREDICTION.md`.** Item 1 (the groups part between β = 3 and 5): they part at 3, slightly earlier. Item 2 was wrong in its detail: the slow state is flux through the short direction, carried by the two y-links, not through the long one; it is almost a function of the coarse field, as expected. Item 3: neither alternative as stated. The ratio is not bounded over the range, and it does not blow up with the collapse of the energy either; it grows slowly, roughly linearly in β. Item 4: γ_opt stays above 0.74 and falls slowly.
- **What this suggests and does not show.** In these models an exponentially small gap does not make the fine-detail constant exponentially large, because the slow state's fine-detail weight is small for the same reason its energy is. A slow growth of the constant, like β, would still be harmless for the summability that the refinement needs. Whether SU(2) itself behaves this way at weak coupling is not shown: the groups stop agreeing before the regime of interest.

## SU(2) itself, in a spin-network basis (added later the same day)

| File | Content |
|---|---|
| `su2core.py`, `su2net.py`, `su2ladder.py` | Clebsch–Gordan and Wigner matrices; intertwiner bases at the two vertices and the multiplication matrices; the model |
| `su2validate.py`, `su2validate_result.txt` | validation independent of the physics: V1 to V5 met, all errors below 1e-14 (basis functions gauge invariant at random group elements; the five multiplication matrices reproduce pointwise multiplication) |
| `su2run.py`, `su2run_J6_result.txt` | main run at spin cut-off 6 against 5; R1 to R4 met. Command: `python3 su2run.py su2run_J6_result.txt ladder_result.txt 6 1.0,2.0,3.0,4.0,5.0,6.0 g` |
| `su2cluster.py`, `su2cluster_result.txt` | checks asked for by reviewers: weights across cut-offs, centre sectors, weights of spectral clusters; C1 to C3 met |

**What kind of numbers these are.** The model is truncated at spin J, and its magnetic factor is the exponential of the truncated multiplication operator, which is not the truncation of the exact factor. Agreement between cut-offs is a numerical convergence diagnostic; nothing here is a rigorous bound for the untruncated model. Within the truncated model, enlarging the coarse polynomial space can only lower the computed weight and raise nothing, so the weights are upper values and the rate a lower value, in that sense only.

| β | gap (J = 6) | change from J = 5 | icosahedral / SU(2) | weight / gap at D = 8, 10, 12 | rate, lower value |
|---|---|---|---|---|---|
| 1 | 1.00896024 | 2e-13 | 1.0000 | 0.2518, 0.2518, 0.2518 | 0.948922 |
| 2 | 0.24308283 | 2e-9 | 1.0000 | 0.3076, 0.3076, 0.3076 | 0.878035 |
| 3 | 0.03854941 | 5e-7 | 0.997 | 0.3561, 0.3543, 0.3539 | 0.846686 |
| 4 | 0.00616713 | 1e-5 | 0.955 | 0.4304, 0.4079, 0.4020 | 0.829676 |
| 5 | 0.00122860 | 9e-5 | 0.749 | 0.5571, 0.4697, 0.4455 | 0.815661 |
| 6 | 0.00029786 | 1e-3 | 0.333 | 0.7713, 0.5582, 0.4952 | 0.799847 |

- **The collapse of the gap is there for SU(2).** The icosahedral group follows SU(2) to 0.3 per cent at β = 3 and 4.5 per cent at β = 4 and then falls faster. So the sentence in the reading above that put the collapse down, in part, to the finite group was too cautious about its existence and right only about its rate.
- **Its rate.** Between β = 3 and 6 the logarithm of the gap has slopes −6.84, −6.83, −6.64 against √β and −1.83, −1.61, −1.42 against β. It is closer to linear in √β. This is a description of four numbers, not a law.
- **Sectors (`su2cluster_result.txt`).** The collapsing state is odd under multiplication of the y-links by −1 and even under the corresponding flip of the x-link: one unit of centre flux through the short direction. The lowest states odd under the x-flip have energy 0.67 to 0.94 at β = 3 to 5 and fine-detail weight below 0.01. The lowest excited state in the sector even under both flips has energy 0.92 to 0.94 at β = 3, 4, 5, which does not fall, and fine-detail weight 0.24. So in this toy only the centre-charged state becomes light.
- **Weight over energy.** For the lowest state the values at D = 12 are 0.2518, 0.3076, 0.3539, 0.402, 0.446, 0.495 at β = 1 to 6; at β = 5 and 6 they are still falling with D (by 5 and 11 per cent from D = 10 to 12), so the true ratios there are lower by an amount not determined. The weight itself changes by 2e-6, 6e-5, 2e-3, 7e-3 between cut-offs 4 and 5 at β = 2 to 5. For the clusters of the five lowest states the compressed weight divided by the energy is at most 0.51 at every coupling computed.
- **Against the addendum of `PREDICTION.md`.** Items 1, 2 and 4 held. Item 3 gave "near 0.40" at β = 4 (0.402 found) and "between 0.45 and 0.6" at β = 5 and 6: at β = 5 the upper value is already 0.446, below the band, and still falling; at β = 6 it is 0.495 and still falling.
- **What it adds.** For SU(2) on this ladder the gap falls by a factor 3,400 between β = 1 and 6 while the weight of the slow state in the fine detail falls with it, the ratio rising from 0.25 to at most 0.5, and the rate stays at or above 0.80. The mechanism stated for the finite groups is therefore present for the group itself, in this toy, over this range.
