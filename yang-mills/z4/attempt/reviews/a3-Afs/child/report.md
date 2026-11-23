# Report: 2D gauge theory flux-mass formula m_L = -L ln a, beta=2.3

Control: I_2(2)/I_1(2) = 0.433127 (control.txt; sub-agent's independent power series: 0.43312743).

## Verdict table
| Item | Verdict | Evidence |
|---|---|---|
| a_U(1)=I1/I0(2.3) | STANDS | quadrature 0.7413754154; power series (sub-agent, rerun by me) 0.74137542 |
| a_SU(2)=I2/I1(2.3) | STANDS (number only) | 0.4792790783 vs power series 0.47927908 |
| z(L)=-L^2 ln a, L=1..8, increasing | STANDS (arithmetic) | table.txt; U(1) z=0.299,1.197,2.693,...,19.152; SU(2) z=0.735,2.942,...,47.070; strictly increasing, z/L^2 const. "Unbounded" is analytic (a<1), not shown by 8 points |
| U(1) m_eff = -L ln a, L=2, t=1..3 | STANDS | mc_L2.txt: 0.59812(39), 0.59926(108), 0.60081(168) vs 0.59850; pulls -0.97,+0.71,+1.38 |
| U(1) m_eff = -L ln a, L=3, t=1..3 | STANDS | mc_L3.txt: 0.89724(49), 0.89466(114), 0.89629(315) vs 0.89774; pulls -1.04,-2.71,-0.46 |
| Hint: plaquettes ~independent (periodic 2D) | STANDS | <cos p>, and nearest-neighbour <cos p cos p'> (time and space) match a, a^2 within 3 sigma for L=2,3 (6/6); sigma ~1e-4 so correlations < ~3e-4 |
| Exact finite-T C(t)=1/2 sum_n lam_n^(T-t) lam_(n+1)^t / sum lam_n^T, lam_n=I_n^L (my own derivation) | STANDS | C(0..4) within 3 sigma for both L (10/10); exact-T m_eff differs from formula by <1e-4 |
| SU(2) m_L formula by simulation | NOT CHECKED | only tabulated; no SU(2) MC run |

## Predicates: met / failed / measured only
- Met: T1-T3 (both groups); P1 6/6 cases; P2 10/10; P3 6/6; P4 6/6 (sigma_jk < 0.25 m, so the test has power).
- Failed: none. (No failed predicates to keep.)
- Measured only: the exact finite-T C(t) formula (not a stated target, just a reference); SU(2) values.
- Tolerance origin: 3 jackknife sigma (about 99.7% Gaussian, ~99.2% with 20 blocks). With ~22 pull comparisons, one near 3 sigma would not be surprising. Two pulls are beyond 2.5 (C(2) L=3 +2.62; m_eff(2) L=3 -2.71). They pass, but I did not rerun with another seed, so I cannot say whether these are noise.
- Block count G=20 is small, so sigma_jk is itself noisy.

## Not checked
SU(2) MC; beta other than 2.3; T other than 16; other seeds; L>3 by MC; large-T limit beyond T=16; whether metropolis thermalisation (300 sweeps from hot start) is fully sufficient beyond the agreement observed; the cosh form was not fitted, only m_eff at t=1..3.

## Delegated question
Sub-agent (grandchild/): independent power-series I_1/I_0(2.3) etc. Control I_0(0)=1 passed first. Outcome: values agree with my quadrature to 8 decimals. I reread series.py and result.txt and reran a copy of the script outside the work dir (its files are mode 'x' so an in-place rerun fails): identical output.

## PCP OS
Register in pcp/ ("method not found" as expected). Programs run via `pcp_os.py check`: control (re-run, expected exit 1 since control.txt exists), table, mc_L2, mc_L3. Verify lines below were appended after the runs.

## Rerun (from a clean directory, since result files use mode 'x')
python3 control.py; python3 prog1_table.py; python3 prog2_mc.py 2; python3 prog2_mc.py 3
(L=2 about 63 s, L=3 about 93 s, one core; sub-agent: copy grandchild/series.py to an empty dir and run it)

Last line of `$P verify --ws pcp`: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
Last line of `pcpos verify pcp/register.jsonl`: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
(The sub-agent rerun differs from result.txt only by a trailing blank line from print.)
