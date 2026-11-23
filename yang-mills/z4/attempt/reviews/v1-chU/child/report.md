# T181 report
Control: control.txt = 9.000000 / 1.762747 (8-pt Gauss-Legendre; 2asinh1). No scipy/mpmath installed: numpy + stdlib only (Bessel by periodic trapezoid, checked against power series ~1e-16).

| item | verdict | evidence |
|---|---|---|
| 1 c* | MET | 4.6054131945 (GL100/200/400 agree 3e-14, substitution a=(pi/2)v^2); claim diff -5.5e-9 < 5e-8 |
| 2 L | MET | 1.8776299817 |
| 3 D(1), D increasing | MET | D(1)=0.0389315; D'>0 at 2000 log pts in [1,1e8] + analytic D'>0 for b>=1/2 |
| 4 | MET | 40000/40000 grid cases qualify, 0 violations, min margin/t^2 = 2.6e-7 (tol 1e-16 t^2, rounding) |
| 5 | MET | 600 pts z in [0.01,700], min margin 2.69e-6 at z=700, quad err 2e-16 (tol 1e-12); grandchild agrees |
| 6 | MET | 30000 cases, 0 violations, min margin 8.7e-7 (delta=1/15, z=1e4) |
| 7 | MET | 11110 (r,c) cases, 0 violations; min margin -0.0 at r=0,c=0 (equality, expected) |
| 8 | MET | 1.58422 > 1.3 |
| 9 | MET | A(1)=5.828427<5.83; A(s)-(1+2s)>=0 on 10001 pts (equality at s=0) |
| 10 | MET | 2000 pts beta in [1,1e12], min rel margin 2.1e-5 |
| 11 | MET | rel err 3.4e-16, abs err 2.8e-16 |
| 12 | MEASURED ONLY | see below |

Item 12 findings (log-domain; Min needs beta>64 since 1-4tau>0):
- deficit(0.1,1e12)=24.935 (claim 24.9: reproduced); deficit(1,1e11)=5.39e-4 (claim 5e-4: reproduced).
- max over s in [0.1,1] (91 s-pts) first <0.2 scanning upward at beta=2.03e13 (worst s=0.1). Claim "near 2.2e13": NOT reproduced exactly (~8% lower). Deficit drops steeply: 8.84 at 1e13, 5e-5 at 1e14.
- beta<=4096: over beta in [100,4096], s in [0.1,1]: 7.33..14.23 (min at beta=100,s=0.1; max at beta=4096,s=1). Claim 8.6..14 only roughly: lower end holds for beta>~200, upper end slightly exceeded (14.23). At beta=4096 alone: 12.88..14.23.
Failed predicates: none (no own-expectation failures; item 12 differences are claim-vs-measurement, no predicate was set to PASS/FAIL).
Control-integral caveat: grandchild's sin control by trapezoid N=2000 gave 1.9999996, written rounded as 2.000000.

Counts (met, failed, measured only): 11, 0, 1.

Grandchild: task T184 (label v1-chU-grandchild, parent T181). Question: independent check of item 5 at z->0 (1e-6) and large z (to 700) with own quadrature + series cross-check. Outcome: MET, min margin 2.69e-6 at z=700 (91 pts); control 2.000000. Released (event 367). I reread results.txt and reran check.py in rerun_gc/ (pcp check K2): same verdict.

PCP: `pcp verify`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)". Last line of Python verify: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." Rust: last line of `pcpos verify pcp/register.jsonl` was the same "A pass is a fact about these bytes..." line (output tail -1; the PASS line is the one above it in each).

Rerun:
  python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name main2 --expect-exit 0 -- python3 t181_main.py results_main2.txt
  (grandchild) mkdir r && cp grandchild/check.py r/ && cd r && python3 check.py
  python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
Files: t181_main.py, results_main1.txt, notes.md, grandchild/.
