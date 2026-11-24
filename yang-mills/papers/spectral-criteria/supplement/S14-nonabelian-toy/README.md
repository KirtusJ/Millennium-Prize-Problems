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
