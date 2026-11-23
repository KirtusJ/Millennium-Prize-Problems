# T138 report: Barta ratio sup, SU(2)

Control: Z(1) = 1.130318 (control.txt; also equals 2 I_1(1) to 2e-16).

## Table (results: res3.csv; finer grid of the doubling pair)
| beta | s | Bsup | -log Bsup | 2asinh(s) | difference | argmax rho | B(0) |
|---|---|---|---|---|---|---|---|
| 64 | 0.01 | 1.00714573 | -0.00712032 | 0.01999967 | -2.712e-02 | 1.000000 | 0.98064656 |
| 64 | 0.03 | 0.97104860 | 0.02937877 | 0.05999100 | -3.061e-02 | 0.735514 | 0.94300700 |
| 64 | 0.1 | 0.84127710 | 0.17283419 | 0.19966816 | -2.683e-02 | 0.405180 | 0.82207007 |
| 64 | 0.3 | 0.56475874 | 0.57135665 | 0.59134610 | -1.999e-02 | 0.239114 | 0.55769526 |
| 64 | 0.6 | 0.32548969 | 1.12242450 | 1.13764980 | -1.523e-02 | 0.177664 | 0.32340041 |
| 64 | 1.0 | 0.17375186 | 1.75012709 | 1.76274717 | -1.262e-02 | 0.150306 | 0.17308314 |
| 256 | 0.01 | 0.98780843 | 0.01226649 | 0.01999967 | -7.733e-03 | 0.628195 | 0.98031114 |
| 256 | 0.03 | 0.94880202 | 0.05255512 | 0.05999100 | -7.436e-03 | 0.363507 | 0.94208176 |
| 256 | 0.1 | 0.82438205 | 0.19312120 | 0.19966816 | -6.547e-03 | 0.200707 | 0.81976704 |
| 256 | 0.3 | 0.55631104 | 0.58642772 | 0.59134610 | -4.918e-03 | 0.118907 | 0.55460149 |
| 256 | 0.6 | 0.32178140 | 1.13388283 | 1.13764980 | -3.767e-03 | 0.088539 | 0.32127193 |
| 256 | 1.0 | 0.17211067 | 1.75961760 | 1.76274717 | -3.130e-03 | 0.074952 | 0.17194690 |
| 1024 | 0.01 | 0.98208213 | 0.01808034 | 0.01999967 | -1.919e-03 | 0.313187 | 0.98022705 |
| 1024 | 0.03 | 0.94351329 | 0.05814483 | 0.05999100 | -1.846e-03 | 0.181259 | 0.94185021 |
| 1024 | 0.1 | 0.82033623 | 0.19804099 | 0.19966816 | -1.627e-03 | 0.100133 | 0.81919348 |
| 1024 | 0.3 | 0.55426008 | 0.59012125 | 0.59134610 | -1.225e-03 | 0.059376 | 0.55383605 |
| 1024 | 0.6 | 0.32087281 | 1.13671046 | 1.13764980 | -9.393e-04 | 0.044235 | 0.32074622 |
| 1024 | 1.0 | 0.17170690 | 1.76196634 | 1.76274717 | -7.808e-04 | 0.037452 | 0.17166616 |
| 4096 | 0.01 | 0.98066860 | 0.01952069 | 0.01999967 | -4.790e-04 | 0.156482 | 0.98020601 |
| 4096 | 0.03 | 0.94220703 | 0.05953025 | 0.05999100 | -4.608e-04 | 0.090569 | 0.94179231 |
| 4096 | 0.1 | 0.81933524 | 0.19926196 | 0.19966816 | -4.062e-04 | 0.050040 | 0.81905023 |
| 4096 | 0.3 | 0.55375099 | 0.59104018 | 0.59134610 | -3.059e-04 | 0.029679 | 0.55364519 |
| 4096 | 0.6 | 0.32064679 | 1.13741511 | 1.13764980 | -2.347e-04 | 0.022113 | 0.32061519 |
| 4096 | 1.0 | 0.17160635 | 1.76255206 | 1.76274717 | -1.951e-04 | 0.018722 | 0.17159618 |

Case beta=64, s=0.01: sup is at the boundary rho=1 (B(1)=1.0071 > 1; -log Bsup is negative), not an interior max.

## Predicates
- P0 (own, fixed before run): own i0e/i1e vs periodic-trapezoid representation, rel 1e-11 at x in {0.5,5,30,31,200,4096}: PASS. Tolerance: series truncation + roundoff ~1e-15. (scipy is not installed and there is no network, so I wrote the Bessel functions.)
- P1 doubling all grids (chi panels 64->128 with 16 GL nodes each, rho grid 400->800): change in -log Bsup < 1e-6: PASS in 24/24 cases (max change 2.3e-13). Tolerance from the task.
- P2 measured only: -log Bsup - 2 asinh(s) is negative in 24/24 cases, positive in 0/24. Magnitude shrinks as beta grows (about 1/beta: beta=4096 gives -2e-4 to -4.8e-4, s=1 to s=0.01).
- P3 Z(beta) by trapezoid vs 2 I1(beta)/beta, rel 1e-10: PASS at all 4 beta (error below 1e-15; the printed 0.00e+00 is real double-precision equality).
- P4 (own expectation: B finite and positive, Bsup >= B(0)): holds in all cases.
- Failed attempts, kept: run1 (res1.csv, empty) was OOM-killed because of my vectorised series (my defect, not the target). run2 (res2.csv, one row) exceeded the 170 s timeout (my slow log/exp series; my defect). run3 is the reported run. The "for all" rule 4 applied to P1 and P2: counts are given above.

## Grandchild (task T139, admitted and released)
Question: recompute B(rho) at beta=64, s=0.3, rho=0 and 0.2 by direct quadrature over S^3 in Hopf coordinates, with no phi' reduction. Its known-answer control Z(1)=1.130318 passed.
Outcome: B(0)=0.5576952560, B(0.2)=0.5641050417, identical to 10 digits on grids (n_eta, n_p=n_q) = (40,64), (80,128), (160,256). I reread grandchild/report.txt and reran grandchild/run.py under pcp check (exit 0). My own reduced formula gives 0.55769526 and 0.56410504 at M=64 and M=128, so the two agree. Note: grandchild's run.py opens its outputs in mode "w", so its rerun overwrote its own report.txt with the same values (it is not bound by my "x" rule, which I did not pass on).

## Rerun commands
    cd /home/user/z4-workers/n1-lemF/child
    python3 ctrl.py            # fails if control.txt exists (mode x); delete first to rerun
    python3 barta.py res_new.csv
    cd grandchild && python3 run.py
    P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P verify --ws pcp

## PCP OS verification (last lines)
- `pcp_os.py verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
- Register checks: barta-run3 (K2, exit 0), grandchild-rerun (K3, exit 0); the aborted run2 check was stopped, and the first no-op "control" check was a pointless placeholder call of mine. Init reported "method not pinned" as expected.
