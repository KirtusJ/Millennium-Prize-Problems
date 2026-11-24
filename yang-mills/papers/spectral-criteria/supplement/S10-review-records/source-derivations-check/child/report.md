# T195 report
**Control:** integral sin^2 over [0,pi] = 1.570796 (control.txt).

## A
Seed 195, N=3000 random cases (dims 3..8, one third with tiny lambda_min 1e-9..1e-6). All 3000 qualify (gamma>0 always, since I-S_2a is PD). **Failures: 0.** Minimal slack d(1+2a/(gamma t))-(b-kappa) = 0.00642263 (case 846; n=3, lambda=1.9e-8, gamma=1.1e-7). Per-case data: A_cases.csv.
Caveats: the bisection-vs-eigenvalue gamma cross-check count was printed to stdout only. The PCP check kept just a hash of that output, so I did not see it. The slack column and failure count above come from A_cases.csv. The 1e-9 failure tolerance is my float64 margin. The claim was tested only on random samples, so this is not a proof.

## B (k = 6*3.399810242 = 20.398861452, C = 4.068056677)
| theta | p_k (GL200) | p_k (GL400) | agree | envelope |
|---|---|---|---|---|
| 0.05 | 0.003072388 | 0.003072388 | yes | 0.050336499 |
| 0.20 | 0.156180437 | 0.156180437 | yes | 1.000000000 |
| 0.60 | 0.934803630 | 0.934803630 | yes | 1.000000000 |
The "p(pi)=1" self-check in stmtB.py is trivial (a ratio of the same quantity), so it checks nothing.

## Grandchild
Task T196 (admitted, then released). Control 2.000000. Simpson with 20000 intervals gives p_k(0.2) = 0.156180436616, which matches the Gauss-Legendre value. I reran its check.py and got the same number.

## Rerun
cd /home/user/z4-workers/y1-g4ret/child; python3 stmtA.py (writes A_cases.csv in mode x, so delete or rename it first); python3 stmtB.py; python3 grandchild/check.py

## Verify (last lines)
- python verify: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- rust verify: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
