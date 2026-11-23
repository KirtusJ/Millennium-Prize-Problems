# Report
Control: 2*log(exp(1)) = 2.0 (control.txt). Seed 12345, 10^4 sets per statement, tol 1e-12 relative (double eps ~1e-16 x <=8-term sums, 4 orders margin).

| Item | Verdict | Evidence |
|---|---|---|
| L1 | STANDS | 10000/10000 qualify, 0 violations |
| L2 | STANDS | 10000/10000, 0 violations |
| L3 | STANDS | all E_i>=1 by construction, 10000 qualify, 0 violations |
| L4 (t>=1) | STANDS | 10000/10000, 0 violations |
| L4 (t in [-1,1)) | STANDS also there | 0 violations in 10000 (Jensen: e^{-sx} convex for any s) |
| L5 | STANDS | 10000/10000, 0 violations |
| L6 | STANDS | max C(1/2)/C(1)=2.71738 < e=2.71828; far above e^(1/2)=1.6487 (so e^(1/2) is NOT the bound) |
| L7 | STANDS | max (C(c)/C(1))/f = 0.99996 < 1 (tight, never exceeded) |
| Mutation (exp(-K)) | DEFECT (as expected: statement false) | counterexample with 1 atom: w=1,E=2,K=1.25: T=0.13534 > 0.10540; also K=1.5: 0.13534 > 0.08208. All 10000 random sets violate. 1 atom is minimal. |

Counts: met = L1-L7 (7 of 7, plus L4b), failed = mutation (intended), measured only = L6/L7 extremes.
Failed predicates: none unexpectedly. The mutation failure is a defect of the mutated target, not of my expectation.
Not checked: n>8, other E distributions (besides U[1,2] for L6), proofs (numerics only); L7 c only in (1/2,1); w=0 sets (C(1)=0 would be skipped; none occurred).
Sub-agent (grandchild/): asked to recompute for w=1,E=2: C(1/2)/C(1) and mutated L1 at D=e,K=1.5. Control 3.0 correct. It returned 2.718281828459045 and T=0.1353352832366127 vs RHS 0.08208499862389879 (fails, ratio e^0.5). I reread results.md and recomputed exp(-2), exp(-2.5) myself: match.
PCP OS: init reported method not found (expected). check K1 exit 0. Python verify last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)". Rust verify last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
Rerun (results file opens with mode x, so use a new name):
  P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; python3 pcp_check.py results_rerun.json
  $P check --ws pcp --name main2 --expect-exit 0 -- python3 pcp_check.py results_rerun2.json
