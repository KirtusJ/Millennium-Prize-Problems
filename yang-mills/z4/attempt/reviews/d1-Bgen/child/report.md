# T37 report: ball-volume scaling (A) and Hessian form (B), SU(3) fund. and U(1)
Control: control.txt = 8 (dim SU(3)).
Sampling: Haar U(3) by QR of complex Ginibre with phase correction (diag R phases), then divided by principal cube root of det -> SU(3). Independent check: Weyl integration formula Haar=(1/6)(2pi)^-2|Delta|^2 dth1 dth2 (th3=-th1-th2), box importance MC.

## Verdicts
| item | verdict | evidence |
|---|---|---|
| A, U(1) | STANDS | MC matches exact arccos(1-s)/pi within 5 sigma at 4 s; exact slope on [1e-3,1e-2] = 0.5003 |
| A, SU(3) exponent 4 | STANDS | Weyl MC slope 4.0008 on s in [1e-3,1e-2]; V/s^4 -> 0.620; direct Haar MC agrees with Weyl at s=.05,.1,.15 and at 8 points in [.15,.5] (|z|<1); local slope there 3.94 (direct) vs 3.93 (Weyl) |
| A, constant c (SU(3)) | STANDS (measured + delegated) | c = 9*sqrt(3)/(8*pi) = 0.620245 from deterministic quadrature (T39), matches MC 0.620 |
| B, U(1) and SU(3) | STANDS | 30 random X each, t=1e-2,1e-3: rel err <= 2 t^2||X||_F^2 (max ratio .26 U1, .04 SU3); error ratio t=.1 vs .01 median 99.5 (O(t^2)) |
| Haar sampler | STANDS | max|det-1|=1.7e-15, E|trU|^2=0.9990 (sigma 5e-4... within 5/sqrt(M)); Weyl norm 0.99975+-0.0006 |

Note: slope 4 is only asymptotic; at s~0.3 the direct slope is 3.94, so the "fitted slope over small s" is only near 4 for s<<1. Direct Haar sampling cannot reach s<0.05 with 4e6 samples; small-s evidence comes from the Weyl formula, not from the QR sampler.

## Failed predicates
- P4 (direct SU(3) MC slope, s in [.02,.12], M=4e6): FAIL (slope nan, counts 0..471). My own expectation was wrong (V~0.62 s^4 ~1e-7 at s=.02); not a defect of the target. Kept. P4b (window [.15,.5], M=8e6, compared to Weyl; declared after seeing P4 fail, so post-hoc) PASS.
- Main run t37_main was recorded by pcp check as exit 1 (because of P4); t37b exit 0.
Tolerances: binomial 5 sigma (MC noise); slope tolerances chosen a priori for O(s) exponent corrections; Hessian bound 2 t^2||X||^2 from quartic Taylor remainder (generous constant).

## Not checked
Upper/lower bounds c s^{d/2}<=V<=C s^{d/2} at all s in (0,s0) (only slopes/limit); other groups/reps; finite-s corrections to c; (B) q>0 only for the sampled X (algebraically -Tr X^2 = ||X||_F^2 for anti-Hermitian).

## Delegated
Task T39 (d1-Bgen-grandchild, parent T37): independent computation of c. Known-answer control first (U(1) V/sqrt(s) at 1e-6 = 0.4501582 vs sqrt2/pi). Result c=0.620245 = 9sqrt3/(8pi). I reread result.md and reran control.py and su3.py in a copy: identical. Released with task-release.

## Rerun
cd to this directory (outputs are mode x where files are written; logs via redirect):
python3 t37.py ; python3 t37b.py ; cd grandchild && python3 control.py && python3 su3.py (delete outputs first)
PCP: P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P init pcp --principal principal --principal-name "Kirtus Justus"; $P check --ws pcp --name t37_main --expect-exit 0 -- python3 t37.py (expected exit 1 due to P4); $P check --ws pcp --name t37b --expect-exit 0 -- python3 t37b.py

## Count
met: 12 predicates (P1,P2,P3,P5a,P5b,P5c,P6,P7,P4b + T39 control, T39 c, plus U1 checks), failed: 1 (P4, own expectation), measured only: slope values and c.
