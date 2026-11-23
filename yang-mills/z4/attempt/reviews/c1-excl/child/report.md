# T12: 5D SU(2) Wilson, L=4 — hysteresis check

**Control:** 0.240194 (= I2(1)/I1(1); series and quadrature agree; control.txt).
Note: first control.py run crashed on `np.trapz` (my code, numpy lacks it); fixed, rerun passed.

## Results (Metropolis, 200 sweeps, mean/err from last 100 sweeps, 10-block error; err ignores autocorrelation, so it is rough)
| beta | P_cold | P_hot | gap |
|---|---|---|---|
| 1.3 | 0.3200 ± 0.0006 | 0.3211 ± 0.0005 | 0.0011 |
| 1.5 | 0.3779 ± 0.0008 | 0.3793 ± 0.0012 | 0.0014 |
| 1.6 | 0.5057 ± 0.0026 | 0.4154 ± 0.0010 | **0.090** |
| 1.7 | 0.5648 ± 0.0014 | 0.5469 ± 0.0067 | 0.018 (2.6 sigma; hot run still drifting up, last 0.5645) |
| 1.9 | 0.6295 ± 0.0010 | 0.6302 ± 0.0007 | 0.0007 |
| 2.2 | 0.6925 ± 0.0007 | 0.6926 ± 0.0005 | 0.00006 |

Answer: yes, a clear hysteresis gap appears at beta=1.6 (0.09, ~30 sigma), a weaker/possibly transient one at 1.7, and none at 1.3, 1.5, 1.9, 2.2. The cold 1.6 run is also drifting (last 0.479 vs mean 0.506), so the cold branch is not stable either; only 200 sweeps, one seed per start. This is a short-run indication, not a measurement of the transition order or location.

## Predicates (fixed in su2_5d.py docstring before first run; tolerances are my own guesses, not derived)
- P1 all 12 values in (0,1]: met, 12/12 qualify.
- P2 gap<0.02 at 1.3 and 2.2: met.
- P3 gap>0.03 and >5 sigma at 1.6 or 1.7: met (via 1.6 only; 1.7 gap is 0.018, below 0.03).
- P4 max gap(1.6,1.7) > max gap(1.3,2.2): met.
- Measured only: the P values, the 1.7 behaviour, drift. No predicate failed in the main program. The one failure was control.py (np.trapz), a defect of my code, not the target.
- NSW was changed 400->200 before the first run of su2_5d.py to stay under 3 min (timed 0.058 s/sweep).

## Grandchild
Asked: independent program for P at beta=0.4 on 4^5 vs strong-coupling leading order I2/I1, with known-answer control first, in grandchild/. Task id **T13** (admitted by task-admit, released with task-release after return). Returned: control 0.240194; P=0.099383±0.000587 vs lead 0.099340 (diff 4.3e-5); predicates P1-P3 passed on its second run. Its first run FAILED (P=0.0007: it updated a whole direction at once, so plaquette-sharing links were updated simultaneously; its own bug; fixed with checkerboard, predicates unchanged; kept as result_run1.txt). I reread its files and reran its program under new tag (copy rerun_gc.py, TAG=parent_rerun): identical P=0.09938299624072583, p3 True. Its tolerance (0.003 for higher-order terms) is a guess; agreement to 0.07 sigma at beta=0.4 does not test higher orders. Note the grandchild used heat bath per its report; I did not audit its sampler beyond the rerun.

## PCP OS
Last line of `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
Last line of Rust `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." (register SHA-256 725402cc...3288f)

## Rerun
cd /home/user/z4-workers/c1-excl/child; export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1
python3 control.py; (rm results.json first, mode 'x') python3 su2_5d.py   (~2 min)
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P check --ws pcp --name su2_5d --expect-exit 0 -- python3 su2_5d.py
