# T67 report: Wilson LGT on (Z/1)^3 x (Z/64), Metropolis MC

control.txt = 0.146735 (= -ln(I1(4)/I0(4)), own midpoint quadrature, 20000 pts).

## Verdict table
| item | verdict | evidence |
|---|---|---|
| Control -ln(I1(4)/I0(4)) | STANDS | 0.146735; grandchild's Simpson quadrature gives 0.14673520 |
| (a) U(1) beta=4 decay rate | STANDS | m=0.14690±0.00184 (jackknife, 32 replicas) vs 0.146735; deviation 0.08 sigma |
| (b) SU(2) m_e(16) | STANDS as a window-fit number, DEFECT as a plateau | 1.440±0.024 from t=1..4; C ratios are not a single exponential |
| (b) SU(2) m_e(64) | STANDS as a window-fit number, DEFECT as a plateau | 1.093±0.014 from t=1..6; same drift |
| Ratio m_e(16)/m_e(64) | NOT CHECKED to the asymptotic limit | 1.317±0.027; between 1 and 4^(1/3) but does not match either |
| Grandchild Bessel check (T68) | STANDS | rerun by me, see below |

## Predicates (fixed in docstring of mc.py before the first run)
- P1 (U(1): |m-0.146735|<3 sigma and sigma<0.01): **MET** (0.08 sigma, sigma=0.0018). The tolerance is our own jackknife error. Fit window t=1..12, cosh form, chosen by the rule "last t with C>3 sigma, cap 12".
- P2 (signal C(1)>3 sigma at both betas): **MET** at both betas. C(1)=2.1e-4±1.2e-6 (beta=16) and 1.2e-5±7.7e-8 (beta=64).
- P3-A (ratio closer to 4^(1/3) than to 4, i.e. r<2.794): **MET** (r=1.317).
- P3 additional condition |r-1.5874|<3 sigma_r: **FAILED**. The deviation is 9.9 sigma_r, with sigma_r=0.027 from independent runs added in quadrature. This failure is my own expectation, not a target defect. The data do not match the pure beta^(-1/3) law at the fitted windows.
- P3-B (r>2.794): not met.

## Numbers
- U(1) beta=4, T=64: m = 0.14690 ± 0.00184 (control 0.146735). Metropolis acceptance 0.30. 500 thermalisation sweeps plus 6000 measured sweeps on 32 replicas, 3 chains each.
- SU(2) beta=16, T=64: m_e = 1.4396 ± 0.0236, window t=1..4. Acceptance 0.39, eps=0.19. 1500 thermalisation sweeps (proposal width tuned there only, then frozen), 3000 measured sweeps on 32 replicas, 2 hits per link per sweep.
- SU(2) beta=64, T=64: m_e = 1.0931 ± 0.0139, window t=1..6. Acceptance 0.40, eps=0.096.
- Ratio 1.317 ± 0.027.
- Effective masses ln(C(t)/C(t+1)) for t=0,1,2,3,...:
  - beta=16: 2.05, 1.49, 1.19, 0.98
  - beta=64: 1.46, 1.14, 0.96, 0.93, 0.73, 0.45 (the last two are noisy)

  These keep falling with t, so there is no plateau. The quoted m_e are window averages and are biased high by excited states. They are not asymptotic gaps. The ratio of effective masses at fixed t is about 1.4, 1.3, 1.24 and 1.05, so the ratio is also window-dependent. The result favours 4^(1/3) over 4, but it does not confirm 4^(1/3) quantitatively.
- Errors are jackknife over the 32 replicas, which are independent chains. The fit-window rule was fixed in advance. The error does not include window-choice systematics, which are the dominant uncertainty here.
- U(1) detail: the Polyakov link W cancels from abelian temporal plaquettes, so it is not simulated there. For SU(2), W is updated by Metropolis.

## Not checked
- Asymptotic plateau of m_e (needs a larger T window and more statistics, or a variational or multi-state fit).
- Finite-T effects; only T=64 was used. Detailed balance or Haar tests of the SU(2) updater beyond the U(1) validation. The U(1) test does not exercise the quaternion code.
- Other betas, so there is no scaling exponent fit.
- Whether the center-even correlator has an excited-state contribution from a lower, odd-sector state. Not examined.

## Grandchild
- Question: independent quadrature of -ln(I1(8)/I0(8)) and -ln(I2(8)/I0(8)), with a known-answer control first.
- Task id **T68** (label f1-wild-child-grandchild, parent T67). It was admitted before the work and released after it returned (events 134 and 137).
- It returned control I0(0)=1 and 0.14673520 (both pass). Results: 0.06695692 and 0.26632363, with Simpson N=200/400/800 agreeing to 1e-15 (grandchild/result.md, quad.py).
- My rerun with my own midpoint rule, N=4000, gave 0.0669569167 and 0.2663236278. **STANDS.**

## Rerun commands
```
cd /home/user/z4-workers/f1-wild/child   # result_*.json are opened mode 'x'; remove them (or use a fresh directory) to rerun
python3 mc.py u1
python3 mc.py su2 16
python3 mc.py su2 64
python3 grandchild/quad.py
```
The PCP-checked runs (K1, K3 and the beta=16 run) were launched via `pcp_os.py check --ws pcp --name {u1_b4,su2_b16,su2_b64} --expect-exit 0 -- <cmd above>`. Run times were 7 s, 124 s and 133 s on 1 core.

## PCP OS
- `pcp_os.py init`: method "not pinned" and "ACR is not in use". This was expected.
- `pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
