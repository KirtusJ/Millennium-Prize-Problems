# T240 report: accumulation recursion (C)
Control: (1+1)(1+1/2)(1+1/3)(1+1/4) = 5 (control.txt).

## Verdicts
- (C) M_{i-1}: STANDS. 4000/4000 exact cases hold, min slack 0 (exact Fractions); equality d_n = RHS in all 506 'eq' cases with RHS>0. Also provable by induction: with equality, d_i = ((d_{i-1}-e_i-k_i))_+/K_i and the M_{i-1} weights are exactly the unrolling.
- (C') M_i: STANDS (weaker than C, since it subtracts more). 4000/4000, min slack 0.
- (C'') M_{i-2}: DEFECT (false, stronger than C). 3505/4000 hold, 495 fail; min slack -5367/39250. Counterexample: seed 6, mode eq, n=2, K=(1.801,1.447), d_n=0.1439 < RHS 0.1927. Hand n=2 case: d_2=13/300 < 4/75.
- Min slack of (C) over my cases: 0 (exact).

## Counts (met, failed, measured only)
- Hypotheses per case: 4000 cases generated (2000 seeds x modes eq/slack), 4000 qualify (by construction, checked per case).
- Predicates: met = C 4000, C' 4000, equality-of-C 506/506, C'' expected-failure confirmed (495 fails); failed = 0 unexpected; measured only = min slacks.
- Tolerance: none, exact rational arithmetic, so no float tolerance needed.

## Failed predicates
C'' failing is my own expectation (it was predicted before running in the docstring), not a defect of the target statement (C). No unexpected failures.

## Not checked
n>8, K huge/degenerate real values, irrational reals (rationals with denominator 1000 only), cases where hypotheses are non-extremal in adversarial ways beyond the random slack. Formal proof only sketched, not machine-verified.

## Sub-agent
Question: n=2, K=(2,3), eps=(.1,.05), kappa=(.02,.01), d0=.5, all equality; compare d_2 with RHS of C, C', C''. Task id T241, admitted and released (task-release OK). Answer: d_2=13/300 = RHS(C); RHS(C')=0; RHS(C'')=4/75 (fails). Its control gave 5. I reread check.py, reran it from a scratch copy (same output) and checked by hand (d1=0.19, d2=13/300).

## Rerun
cd /home/user/z4-workers/f2-lean/child; (result files are mode "x": delete results_test_c.txt first)
python3 test_c.py
python3 grandchild/check.py   (delete grandchild/result.txt first)
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P check --ws pcp --name test_c --expect-exit 0 -- python3 test_c.py

## Verify (last lines)
- python: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- rust: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
Note: ACR method packet not found at init/check (expected per task).
