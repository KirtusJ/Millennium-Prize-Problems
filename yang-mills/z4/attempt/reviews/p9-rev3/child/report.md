# T64 report (N=6 toy time lattice)
Control: control.txt = 0 (slice 3 -> 0 on ring of 4), correct.

| Claim | Verdict | Evidence |
|---|---|---|
| C1 supp(tau F)=supp(F)+1 | STANDS | 63/63 nonempty supports qualify; numerically measured support (perturbation) = S+1; 0 violations (result_N6.txt) |
| C2 tau{0,1,2}->A+; leaves A+ iff 3 in S | STANDS | 7/7 supports in {0,1,2} land in A+; of 15 supports in {0..3}, 8 leave, exactly those containing 3 |
| C3 theta tau = tau^-1 theta | STANDS | 4000 random evals, max diff 0 (tol 1e-9 = float roundoff; both sides evaluate F at U_{-s-1}); also by hand; also N=2 and N=6 in grandchild |
| C4 tau' moves U_0 to U_5 | STANDS | measured supp = {5}, 5 not in {0..3} |

Counts (N=6 run): met 5, failed 0, measured only 0 (the 5 predicates P1,P2a,P2b,P3,P4 cover C1..C4).
Extra N=2 run of my program (result_N2.txt): met 3, failed 2.

Failed predicates (N=2 only): P2b and P4. Cause: my own expectation, not a target defect. At N=2, A_+ = slices {0..N/2} = {0,1} is the whole ring, so nothing can leave A_+ and U_{N-1}=U_1 is inside A_+. The claims were stated for N=6. PCP record K2 (expect 0, got 1) keeps this mismatch; K3 reruns it with expect-exit 1.

Grandchild: question = N=2 boundary: is theta the identity on slices, does C3 hold, is tau^2=id (plus N=6 comparison). Task id T66 (label p9-rev3-grandchild), released. Outcome: its control = 0; theta identity on slices True; C3 True (max diff 0); tau^2=id True; N=6 True. I reread its check.py and reran it in rerun/ (identical results.txt), and independently confirmed C3 at N=2 with my own program.

Rerun:
- cd /home/user/z4-workers/p9-rev3/child && python3 check.py 6 new_N6.txt
- python3 check.py 2 new_N2.txt   (exits 1: the two N=2 expectation failures above)
- cd grandchild && rm -f results.txt && python3 check.py
(result files open with mode "x": use a fresh output name.)

PCP verify last lines: python verify -> "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"; Rust verify -> "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
