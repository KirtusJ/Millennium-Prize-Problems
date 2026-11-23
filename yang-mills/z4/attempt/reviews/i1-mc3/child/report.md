# T100 report: center-even gap, 1 site, 3 dirs, SU(2), beta=2

## Verdict table
| Item | Verdict | Evidence |
|---|---|---|
| Control (1/2pi)∫exp(cos x)dx | STANDS | control.txt = 1.266066 (grandchild's control: same) |
| Code known answer, beta=0: <Q>=1/4 | STANDS | 0.24968 ± 0.00020 (P1 met); connected C_S(1) = 0.00012 ± 0.00021 (P2 met) |
| m_e at beta=2 | STANDS (statistical error only) | 1.620 ± 0.013 (tau=1); tau=2 gives 1.63 ± 0.06, consistent |
| 2-fold degeneracy of A=Q1-Q2, B=Q1+Q2-2Q3 | STANDS | m_A−m_B = −0.005 ± 0.022 (tau=1), −0.10 ± 0.11 (tau=2); cross C_AB(1) = 0.0003 ± 0.0002 |
| Q1+Q2+Q3 channel effective mass | measured | 1.897 ± 0.023 (tau=1), 1.91 ± 0.16 (tau=2) |
| "2-fold is the lowest level" (m_2f < m_S) | STANDS at tau=1 only; predeclared tau=2 test DEFECT | tau=1: 1.620 vs 1.897 (diff 0.28, ~12 sigma, not predeclared); tau=2: diff 0.28 ± 0.17, below my 2-sigma bar. Own-statistics failure, not a target defect |
| Commutator identity and center-evenness (grandchild) | STANDS | max dev 1.2e-15 / 0 / 1.7e-15, 20000 random samples |
| Systematic errors (T, finite step, excited-state at tau=1) | NOT CHECKED | only T=16, one beta, one seed |

## Result
**m_e(beta=2) = 1.620 ± 0.013** (statistical, jackknife over 128 chains).
It is the log-ratio effective mass of (C_AA+C_BB)/2 at tau=1, using the plateau predicate P7 (tau=1 vs tau=2 within 2 sigma).
The tau=2 value (1.63 ± 0.06) is consistent. Excited-state contamination at tau=1 is not excluded, because tau>=3 is lost in noise (C ~ 2e-4 noise floor). A conservative quote is m_e ≈ 1.62 ± 0.02.
Channel S = Q1+Q2+Q3, vacuum-subtracted: m ≈ 1.90 ± 0.02 (tau=1).

Method: Metropolis Monte Carlo, numpy, quaternion SU(2), Haar-reversible left-multiplication proposals (eps=0.6, acceptance 0.46). Gauge W=1 for t<T-1 with W(T-1) dynamic. T=16 periodic, 128 independent chains, 300 thermalisation sweeps, 9000 measurement sweeps. Connected correlators averaged over t, errors by jackknife over chains. Seeds are fixed: `default_rng(12345+int(beta*1000))`.
Not yet done: an independent method (transfer-matrix diagonalisation) was not attempted in the budget.

## Predicate counts
Met 11 (P1, P2 at beta=0; P3 at beta=2; P4, P5, P6, P7 at beta=2; grandchild 4/4). Failed 2. Measured only: m_e, m_S, acceptance, plateau tau.
- Failed P3 at beta=0: acceptance is 1.0 by construction when beta=0. This was my own expectation misapplied, not a target defect. At beta=2 the acceptance is 0.46 and P3 is met.
- Failed P8 (m_S − m_2f > 2 sigma at tau=2): the difference is 0.28 ± 0.17. Statistical power at tau=2 was too low (my threshold). It is not a physics defect.
Tolerances: 5 sigma for the beta=0 known-answer checks (false alarm ~1e-6), 3 sigma for degeneracy and orthogonality, 2 sigma for plateau (conventional), 1e-12 for the roundoff checks (float64, observed ~1e-15), and acceptance 0.2–0.8 (Metropolis rule of thumb).
Rule 4 ("for all ..."): no universal predicate was used. P5 was tested for each of 2 taus (both qualify).

## Grandchild
Question: verify numerically on random SU(2) that (1/2)Tr(UiUjUi^-1Uj^-1) = 1 − 2(|ui|²|uj|² − (ui·uj)²), and that Q_i and P_ij are center-even.
Task id T103, admitted under parent T100, released (event 205). Outcome: 4/4 predicates met, control 1.266066. I reread check.py and reran it; the output was identical. The first results.txt was kept as grandchild/results_first.txt.

## PCP OS verify (last lines)
- Python verify: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust verify: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
The `init` reported the method as not found, as expected. The register recorded checks K1–K4.

## Rerun
```
cd /home/user/z4-workers/i1-mc3/child; export OMP_NUM_THREADS=1   # result files open with "x": use new names or delete old ones
python3 mc3.py 0 64 10 1500 res_beta0.json && python3 analyze.py res_beta0.json an_beta0.json
python3 mc3.py 2 128 300 9000 res_beta2.json && python3 analyze.py res_beta2.json an_beta2.json   # ~106 s
cd grandchild && rm -f results.txt && python3 check.py
```
