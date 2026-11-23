# Report — free U(1) lattice gauge theory, spatial flow, L=16

**Control answer:** mean of 4 sin²(k/2) over 64 momenta = **2.000000** (control.txt; exact identity).

## Numbers (L=16, explicit 4x4/6x4 matrix covariance, Σ=I/A, k≠0)
| tau | e(tau) | m(tau) | tau²·m |
|---|---|---|---|
| 1  | 1.0111277555 | 6.5664481334e-03 | 6.5664481334e-03 |
| 4  | 1.0016304900 | 3.6234145385e-04 | 5.7974632616e-03 |
| 16 | 1.0004608860 | 4.4066867511e-06 | 1.1281118083e-03 |

Closed forms (matched): per mode p≠0: e = 1 + 2 q4² e^{-2τp²}/A; p=0: e = 3; m = 2p² e^{-2τp²}/A.
(15 p=0 modes with k≠0 contribute 3 each.)

## Verdict table
| Predicate | Verdict |
|---|---|
| P1 control = 2 | met |
| P2 single mode n=(3,5,1,7), longitudinal sum = 1, tau=1,4,16 | met (dev 2.2e-16, tol 1e-12 from float64 rounding) |
| P3 "for all k, p≠0": hypothesis tested per case first: 65520 modes with p≠0, 65520 qualify (max dev 8.9e-16) at each tau | met. Claim holds exactly; analytic reason: a_4 independent of a_i, P_L a is longitudinal with norm² 1/A, so (p²+q4²)/A=1 |
| P4 e matrix = closed form (tol 1e-10) | met (diff 0) |
| P5 m matrix = closed form with factor 1 | **failed — my own expectation error** (docstring said "one transverse"; there are two transverse polarizations → factor 2). Not a target defect. |
| P5' m matrix = closed form with factor 2 (tol 1e-12), fixed in m_check.py before run | met (diff ≤2.5e-14) |
| Sub-agent MC e(4), L=8 vs exact, <4 SE | met (measured by sub-agent; reproduced by me) |

Note: the longitudinal part is exactly 1 but total e(tau)>1 because transverse a_T also contributes; the claim concerns only the longitudinal piece. e→1 as tau→∞ (except the p=0 modes).
Also failed attempt: check K2 (m_check.py) exited 2 because my file had not been written (a command was aborted before the heredoc ran) — my slip; K4 is the rerun.

## Sub-agent
Asked (in grandchild/): known-answer control first, then an independent Monte Carlo of e(tau=4) at L=8 from Gaussian a_μ(k), fixed seed, 2000 samples, building θ_{i4} directly, vs exact tr(TΣT†)/L⁴; predicate |MC−exact|<4 SE.
Returned: MC 1.00326752 ± 0.00035587, exact 1.00331441, z=−0.132, predicate True. I read run.py output and reran a copy in gc_rerun/ (K3): identical. I did not independently audit run.py line by line beyond the output and its result line.

## Rerun
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
# result files open with mode "x": remove results_flow.txt results_m.txt first
python3 flow.py ; python3 m_check.py
cd grandchild && python3 control.py && python3 run.py   # remove its results.txt/control.txt first
$P verify --ws pcp
```
Register `pcp` (K1 flow, K2 failed m_check, K3 gc_rerun, K4 m_check2). Last verify line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)". Method was reported not found at init (expected).
