# T212 report (a2-mixb child)

## Control
P(theta<1.2) = (1.2 - sin(2.4)/2)/pi = **0.274469** (control.txt). Derivation: chi=arccos(a0) has density (2/pi) sin^2 chi and theta = pi - chi. Own MC (4e5): 0.27469 +- 0.00071.

## Setup
4D SU(2) Wilson, 6^3 x 12, beta=3.276133577, Kennedy-Pendleton heat bath, checkerboard by site parity x direction (valid). No over-relaxation.
6 independent hot-start chains (seeds 100-105), 300 thermalisation sweeps, 150 configurations per chain, separated by 10 sweeps (900 configurations total). Statistics are reduced: no autocorrelation study of the separation. Errors are delete-one-chain jackknife over 6 chains.
Each configuration gives 27 squares x 12 time slices = 324 marks. Normalisation C(t)/C(0) uses the pooled mean <m>, with the same spatial square at both times.

## Numbers (analysis_v1.txt)
| mark | C(1)/C(0) | C(2)/C(0) | gate fraction |
|---|---|---|---|
| ungated m1 | 0.0130 +- 0.0011 | -0.0008 +- 0.0010 | 1 |
| gate 1.2 (theta<1.2) | 0.0021 +- 0.0027 | 0.0005 +- 0.0027 | 0.0402 +- 0.0005 |
| clear (theta>1.2) | 0.0122 +- 0.0013 | -0.0016 +- 0.0008 | 0.9598 +- 0.0005 |
| gate 0.6 | -0.0003 +- 0.0000 | -0.0011 +- 0.0008 | 0.0020 +- 0.0000 |

- Average plaquette 0.750028 +- 0.000080 (chain-to-chain SE).
- Gate 0.6: the +-0.0000 for C(1)/C(0) comes from the 6-chain jackknife on a rare gate (0.2% of squares). It is probably an underestimate, so do not trust that error.
- Verdict: ungated and clear C(1)/C(0) are small but positive (~12 sigma). Gate 1.2 and gate 0.6 are consistent with 0 at their errors. C(2)/C(0) is consistent with 0 everywhere.
- Gate 1.2 holds only about 4% of squares, so the gated autocorrelations are noisy.
- Comparison with the Haar fraction 0.2745: the lattice gate-1.2 fraction is 0.040, so W_c is far from Haar. That is not a failure, just the physics at this beta.

## Predicates (test_checks.py docstring, fixed before the first run)
- v1 run (test_results_v1.json): P1, P2, P3, P5 passed. **P4 failed.** My predicate expected theta=0 for a cold start. For W=I, theta=arccos(-1)=pi, so this was my own expectation error, not a code defect.
- v2 (test_results_v2.json, pcp check K1) passed all five:
  - P1: heat-bath single-link <w0>, <w0^2> within 4 SE of exact quadrature. Tolerance: 4 sigma of the sample mean.
  - P2: hot and cold start plaquettes agree within 4 sigma (batch-means SE). Hot 0.74944, cold 0.74987.
  - P3: gauge invariance of marks, max difference 8e-15, tolerance 1e-10.
  - P4: cold start plaquette 1, theta=pi, unitarity error 2e-16.
  - P5: Haar MC control within 4 SE.
- Chains >= 4: satisfied (6).

## Not checked
- Autocorrelation time of the chain (separation of 10 sweeps was not tested for independence; C(1) is small, which suggests configs are decorrelated, but this is not shown).
- Thermalisation beyond the hot/cold test (150 sweeps).
- Finite-size and lattice-orientation effects. Only one beta was run.
- Over-relaxation, and a second independent code for the marks (only gauge invariance was tested, and no known-answer check of marks beyond the cold start).
- Jackknife with 6 chains is a crude error estimate, especially for the rare gate 0.6.

## Grandchild (T213, label a2-mixb-grandchild)
- Question: known-answer control P(theta<pi/2)=0.5, then an independent recomputation of the Haar probability P(theta<1.2) and an exact single-link check of KP heat bath.
- Outcome: control 0.500000; quadrature 0.27446856; MC 0.274334 +- 0.000315; single-link <a0> exact 0.59653220, own KP 0.596413 +- 0.000313 (-0.38 sigma).
- I re-read its link.py and reran it (rerun_link.py writes link_result_rerun.txt). The numbers are identical. My own P1 gives <a0> exact 0.5965322, matching.
- Released: T213.

## PCP OS
- `init` reported the ACR method not found (expected).
- Checks: K1 tests_v2, K2 production, K3 analyze, all exit 0 as expected.
- `pcp_os.py verify --ws pcp` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." The line before it is "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)".
- `pcpos verify pcp/register.jsonl` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." (preceded by the register SHA-256 285f378b...6526).

## Rerun
```
cd /home/user/z4-workers/a2-mixb/child; export OMP_NUM_THREADS=1
python3 test_checks.py test_results_v3.json
python3 run.py prod_v2.json        # about 130 s
python3 analyze.py prod_v2.json analysis_v2.txt
```
(Result files open with mode 'x', so use new names.)
