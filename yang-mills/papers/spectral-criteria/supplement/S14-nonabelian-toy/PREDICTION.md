# Expectation for the non-abelian toy, written before the main run of `ladder.py`

Seen before writing this: a trial at β = 1 and 2 with the groups 2T and 2O (γ_opt 0.949 and about 0.875; lattice gap 1.005 and 1.009 at β = 1, 0.165 and 0.239 at β = 2, where the two groups already differ by 31 per cent in the gap; weight of the first excited state in the fine detail divided by its energy 0.252 and 0.30).

What I expect, and how sure.
1. The two larger groups, 2O and 2I, agree at β = 1 and 2 to a few per cent or better and part somewhere between β = 3 and 5. This I expect with some confidence; it is the known behaviour of these subgroups as stand-ins for SU(2).
2. Where they agree, the lowest excited state is odd under multiplication of the x-holonomy by −1 (a unit of centre flux), and it is almost a function of the coarse field. Fairly confident.
3. The ratio of its fine-detail weight to its energy. Two possibilities, and I do not know which holds:
   - (stipulation of Path A) it stays bounded, near the abelian value 0.31 to 0.35, because the fine-detail weight and the energy are both controlled by the same small probability of the region between the two centre sectors;
   - it grows with β, because the energy of the centre-flux state falls faster than any power of 1/β (tunnelling between flat connections) while the fine-detail weight falls only like 1/β.
   The trial values, 0.25 at β = 1 and 0.30 at β = 2, are close to the abelian toy's 0.245 and 0.310 and do not decide it. The second possibility, if seen while the two groups still agree, would count against Path A and against statement (i) of the one-step form for coarse variables of this kind.
4. γ_opt stays above about 0.8 in the first case and falls in the second.

## Addendum before the main SU(2) run (`su2run.py` at spin cut-off 6)

Seen before writing this: development runs of the spin-network program at cut-offs 2 to 5 (gap 1.00896, 0.243077, 0.038549, 0.006167, 0.0012285, 0.000298 at β = 1 to 6; weight over gap 0.2518, 0.3076, 0.3535 at β = 1, 2, 3 and upper bounds 0.41 at β = 4), and the trial of `su2run.py` at cut-off 4 for β = 1, 2, 3.

Expectations for the run at cut-off 6.
1. The gaps above are confirmed to four figures up to β = 5 (cut-off 5 against 6).
2. The gap of SU(2) falls more slowly than that of the icosahedral group beyond β = 4, and between β = 3 and 6 its logarithm is closer to linear in √β than in β (slopes against √β from the development runs: −6.84, −6.83, −6.65). So the collapse of the gap is real for SU(2) in this toy, not an effect of the finite group, though its rate is different.
3. Weight over gap for the lowest state: upper bounds decreasing in the coarse degree D, settling near 0.40 at β = 4 and between 0.45 and 0.6 at β = 5 and 6, if D = 12 is enough there; if it is not, the bounds will still be falling at D = 12 and the run will say so.
4. Lower bound for γ_opt above 0.75 up to β = 6.
