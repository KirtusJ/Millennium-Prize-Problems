# T114 report

Control: 1+...+100 = 5050 (control.txt). Grandchild control 6*7 = 42 (grandchild/control.txt).

## Verdicts (grid beta {50,100,400,1000,4000,10000} x m {0.05,0.1,0.25,0.5}; measured only, not proved for all beta, m, n)
- **LOW: STANDS on the grid.** 5337 pairs met, 0 failed, 24 trivial (n1=n2=0, both sides 0). Smallest ratio/theta = 1.0028 (beta=10000, m=0.05, n1=n2=M=5).
- **HIGH: STANDS on the grid.** 47154 pairs met, 0 failed. Tightest at (0, M+1): min L/c = 1.00070 (beta=10000, m=0.05: L=0.0023972 vs c=0.0023956).
- **K1: STANDS on the grid.** 18006 values (n=0..3000, 6 betas) met, 0 failed. Smallest relative slack 2.0e-4 (lower bound) and 1.7e-3 (upper bound), both at beta=10000.
- Counts as met / failed / measured only: LOW 5337/0/24 trivial; HIGH 47154/0/0; K1 18006/0/0. Nothing NOT CHECKED inside the stated grid. Statements for all n beyond 3000, or off-grid beta/m, are NOT CHECKED.

## Hypothesis test (rule 4)
LOW is non-trivial only when M>=1. M=0 in 3 of 24 (beta,m) cells ((50,.05), (50,.1), (100,.05)); 21 cells qualify. HIGH and K1 apply in all 24 cells.

## Smallest ratio (1-kk)/((l1+l2)/(2beta)) on LOW set
Attained at n1=n2=M in every qualifying cell (see results_run1.txt). Compare with theta and 1/(1+m^2):
- ratio >= theta in all 21 cells; ratio/theta ranges 1.0028 to 1.363. The margin shrinks as beta grows and m shrinks.
- ratio vs 1/(1+m^2): ratio is BELOW 1/(1+m^2) in 2 cells: beta=100, m=0.1 (0.990012 vs 0.990099) and beta=400, m=0.05 (0.997501 vs 0.997506). So 1/(1+m^2) is not a valid constant without the correction; theta's 3m/sqrt(beta) term and beta/(beta+M+1/2) factor are needed. This is a statement about my own comparison, not a claim in the task.
- Examples: beta=10000, m=.5: ratio 0.88061, theta 0.78654, 1/(1+m^2)=0.8. beta=50, m=.25: 0.98005 vs theta 0.83083.

## Tolerances
Relative 1e-9 on every inequality (lhs >= rhs(1-1e-9)). Source: 1-kk computed as -expm1(-(a1+a2)) with a_n=-ln kappa_n from the cumulative sum of logs of recurrence ratios; double rounding ~1e-16 per step, <=1e-13 relative worst case, so 1e-9 is loose and does not hide a failure (smallest margins: K1 2e-4, HIGH 7.0e-4, LOW 2.8e-3, all far above 1e-13). Quadrature cross-check tolerance 1e-10 (trapezoid on a smooth periodic even integrand converges geometrically); observed worst 1.2e-15 over 36 cases (beta x n in {1,2,3,5,10,20}). kappa_1(100)=0.9850378800081571.

## Failed predicates / own mistakes
- No claim predicate failed. One own process error: I first ran check.py directly, outside `pcp check`, producing results_prelim_outside_pcp.txt (identical outcome, 0 fails). I then changed only the output filename (argv) and reran under pcp check as results_run1.txt. Also an earlier draft of this report mis-stated the comparison with 1/(1+m^2); corrected above after tabulating all cells.

## Grandchild
Task id T115 (admitted by principal, parent T114, released after return: "RELEASED T115", event 230). Outcome: control 42; kappa_1(100) = 0.985037880008157 by recurrence and by quadrature (diff <1e-15); LOW at beta=10000, m=0.5, n1=n2=M=50: LHS 0.22895800407325, RHS 0.20450086745729, ratio 1.11959, PASS. I reread gc.py and reran it in rerun_gc/: output byte-identical (cmp) to grandchild/gc_result.txt. This agrees with my ratio 0.880608/theta 0.786542 = 1.1196.

## PCP OS
- `pcp init`: method reported not found (expected).
- checks: K1 check_run1 exit 0 (expected 0), K2 grandchild_rerun exit 0 (expected 0).
- `pcp_os.py verify --ws pcp` last line: "A pass is a fact about these bytes... " preceded by "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)".
- `pcpos verify pcp/register.jsonl` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." (before it: "guards replayed: 0 problem(s)").

## Rerun commands (from this directory)
    python3 -I check.py results_rerun.txt              # new filename; results files are mode "x"
    mkdir -p rr && cd rr && python3 -I ../grandchild/gc.py
