# T110 report — recomputation of Q1..Q14
Control (sum 1/n^2 to 6 dp): **1.644934** (control.txt). Tolerances: half unit of the last claimed digit unless noted (fixed in recompute.py docstring before first run). Own Gauss-Legendre quadrature (numpy nodes, 400 vs 200 nodes agree to <3e-14), substitution a=(pi/2)u^2 with symmetry a->pi-a; Q1-Q8 in 40-digit decimal.

| Q | computed | claimed | verdict | tolerance (source) |
|---|---|---|---|---|
| 1 | 4.11671958507 | 4.1167196 | REPRODUCED | 5e-8 (half unit 7th decimal) |
| 2 | 1.89778065 | 1.89778 | REPRODUCED | 5e-6 (half unit 5th decimal) |
| 3 | 2.26964572 | 2.26965 | REPRODUCED | 5e-6 (same) |
| 4a | 1.49929e-7 | 1.5e-7 | REPRODUCED | 5e-9 (half unit 2nd sig. digit) |
| 4b | 1.499e-7 < 3.150e-7 | smaller than 0.5e-6/4^(1/3) | REPRODUCED (yes, smaller) | strict inequality |
| 5 | 1.974964 | 1.974964 | REPRODUCED | 5e-7 |
| 6 | 2.876117; 2.042968; 1.538081 | 2.88, 2.04, 1.54 | REPRODUCED (all 3) | 0.005 |
| 7 | -0.680%; -0.780%; -1.632% | -0.7, -0.8, -1.6 | REPRODUCED (all 3) | 0.05 (half unit 1st decimal) |
| 8 | 1.7738 | 1.8 | REPRODUCED | 0.05 |
| 9 | max diff 8.4e-15, 1000/1000 pts qualify | identity | REPRODUCED | 1e-12 (my choice, double rounding) |
| 10 | 4.605413195 | 4.6054132 | REPRODUCED | 5e-8 |
| 11 | 2.682799401 | 2.6828 | REPRODUCED | 5e-5 |
| 12 | 8.988808 | 8.99 | REPRODUCED | 0.005 |
| 13 | 4.792560939 | 4.7926 | REPRODUCED | 5e-5 |
| 14 | 9.900% and 10.988% | "about 12%" | NOT REPRODUCED | 12 ± 0.5 (my reading of "about 12" as integer rounding) |

Q14 failure: it is my predicate's reading, plus a real discrepancy in the claim: neither ratio is 12; 11.0% (relative to 8.1) rounds to 11, 9.9% rounds to 10. With a looser ±1 reading the 11.0% variant would pass; I did not use that because it was not fixed beforehand.
Q9 "for all": hypothesis tested per case, 1000/1000 points qualify.
Q4 note: the exact Q1 is 4.116719585; the 1.5e-7 offset is below the propagated rounding bound, consistent with rounding of 6.534885.

## Grandchild
Task id **T112** (admitted with --parent T110, released with task-release after return). Question: Q11 d via substitution a=pi sin^2(t/2) (removes singularity). Known-answer control: integral of sin on [0,pi] = 2.000000 (passed). Outcome: d=2.6827994012 at 100/200/400 nodes (converged), claim 2.6828 reproduced; agrees with my value 2.682799401. I reread its files and reran run.py in a copy directory: identical result.

## Counts
met: 13 of 14 (Q1-Q13; Q4 counted once, Q6/Q7 as groups); failed: 1 (Q14); measured only: 0. Internal checks: convergence 3/3 met, grandchild control met, grandchild d met.

## Rerun
cd /home/user/z4-workers/j1-micro/child; rm -f results.json; python3 recompute.py
cd grandchild; rm -f control.txt result.json notes.md; python3 run.py
(files open with mode 'x'; remove before rerun)
