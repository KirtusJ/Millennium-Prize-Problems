# Vortex free energy F(L,beta), 4D Z2 LGT

**Control (2D, N=4 torus, beta=0.5):** F = 0.091272 (control.txt; brute force 2^8, equals analytic -ln[(c^4-s^4)/(c^4+s^4)]).

## Results (heat bath, GL 8 nodes in s, 2 chains (hot/cold) x 20000 sweeps after 2000 therm., 20-bin errors)
| beta | L | F (n=8) | err | F (n=5) |
|---|---|---|---|---|
| 0.30 | 2 | 0.0774 | 0.0024 | 0.0776 |
| 0.30 | 3 | 0.0041 | 0.0038 | -0.0009 |
| 0.30 | 4 | 0.0061 | 0.0051 | -0.0074 |
| 0.60 | 2 | 3.205 | 0.025 | 3.214 |
| 0.60 | 3 | 8.244 | 0.127 | 8.098 |
| 0.60 | 4 | 15.84 | 0.25 | 15.67 |

**Answer to the question.**
- beta=0.60: **No**, F strongly *increases* with L (2->3: +5.04+-0.13; 3->4: +7.60+-0.28), roughly ~L^2 (F/L^2 = 0.80, 0.92, 0.99). This is robust against any plausible underestimate of the errors.
- beta=0.30: **Consistent with non-increasing**: 2->3 drops by 0.073+-0.005 (16 sigma); 3->4 is +0.002+-0.006 (0.3 sigma), i.e. F is compatible with 0 (flat, vanishing) for L=3,4. I cannot distinguish "decreasing" from "zero" at L=3,4.
- Overall: F is not non-increasing in L for both beta; only the confined side (0.30) is.

## Predicates (fixed in vortex.c docstring before the first run)
- C1 (control analytic = brute force, 1e-12): MET.
- C2 (MC code on D=2,L=2,beta=.5 reproduces 0.091272 within 3 sigma): MET (0.091759+-0.00197, 0.25 sigma).
- C3 (declared later, after reading the delegate's numbers, before running): MC D=3,L=2 vs exact enumeration: beta=.3 0.03199+-0.00175 vs 0.032524 (0.3 sigma); beta=.6 0.6862+-0.0054 vs 0.691279 (0.95 sigma). MET.
- P1 (hot/cold agree within 3 sigma at each node, "for all nodes" hypothesis tested per case): 6/6 cases qualify (all 8/8 nodes). BUT the test is weak: at beta=0.6 nodes s>=0.76 for L=4 have errors of 1-2 (hot chain err 1.2-2.4) i.e. tunnelling/metastability between flux-sector states; their bin errors are themselves unreliable. Passing there reflects large errors, not good statistics.
- P2 (n=5 vs n=8 agree within 3 sigma): 6/6 MET (largest 1.66 sigma, L=4 beta=.3).
- P3 (F>=0 within 3 sigma): 6/6 MET (beta=.3 L=3,4 are ~0 +- 0.004-0.005).
- P4 (non-increasing, step <= 1 sigma): beta=.3: both steps met (as noted, 3->4 is just "flat"); beta=.6: FAILED both steps. The failure is a property of the physics (my expectation was open), not a code defect.
- Failed/odd: none of the predicates failed except P4 at 0.6. Measured only: error bars (bin-based, 20 bins).

## Not checked
- No autocorrelation time measurement; no larger-statistics or seed repeat (single seed base 1); beta=0.6 errors at s near 1 likely underestimated (tunnelling). The beta=0.6 F values carry larger systematic uncertainty than quoted but the L-trend conclusion doesn't depend on it.
- No reversed-direction / Metropolis cross-check; no check at beta near 0.44; no L>4; stack coupling interpolation only linear in s (GL 5 vs 8 compared, no higher).
- Stack = plaquettes in plane (0,1) at x0=x1=0 for all x2,x3 (L^2 plaquettes) in code indexing.
- out/test_trash.dat is an early smoke test (D=4,L=4,b=.3,n=5, same seeds as production n=5), not an extra result.

## Delegation
Asked a sub-agent (grandchild/) for: control first (it got 0.091272, no analytic comparison) and exact 2^24 enumeration of the 3D L=2 analogue plus a check of the identity F=2*beta*Int<sum_stack>ds. Returned: F(0.3)=0.0325242683, F(0.6)=0.6912790067; quadrature differs by 1.4e-15 / -1.9e-9. I reread grandchild/results.md (matches) but did not rerun its code; I did use its numbers as an independent check of my own C code (C3). Caveat: its 3D stack has 2 plaquettes by my specification; not 4D.

## Rerun
```
cd /home/user/z4-workers/a3-Avort/child
gcc -O2 -o vortex vortex.c -lm        # output files use mode wx: move out/ and control.txt aside first
python3 control.py write
./run_all.sh                           # ~53 s
```
PCP records: see below (appended).

## PCP verify (last lines)
- Python `verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- Rust `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
- Note: `init` reported the method packet as not found (expected). Checks recorded: control_py (K1), run_all (K2); the grandchild's programs were not run through `check`.
