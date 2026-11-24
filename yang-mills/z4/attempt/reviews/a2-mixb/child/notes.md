# notes
- control: P=(1.2 - sin(2.4)/2)/pi = 0.274469 (theta=pi-chi, chi density (2/pi) sin^2). control.txt written.
- lat.py, test_checks.py written; v1 run (test_results_v1.json): P1,P2,P3,P5 pass, P4 FAILED: my predicate expected theta=0 for cold start, but theta=arccos(-W0)=pi for W=I (distance from -I). Own expectation error, not a code defect. v2 predicate: cold theta == pi.
- grandchild T213 returned: control 0.5 ok, P(theta<1.2) quad 0.27446856, MC 0.274334+-0.000315; single-link <a0> exact 0.5965322, KP 0.596413+-0.000313. Released T213.
- reran grandchild link.py (copy writing link_result_rerun.txt): see rerun output; matches.
- tests_v2 passed all P1-P5 (pcp check K1). production run.py: 6 chains, therm 300, 150 cfg/chain, sep 10 sweeps
A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
