# Report: K(n), tau=6, 16^4 lattice via periodic-chain Green function

Control: sum cos^2(2 pi l/16) = 8.0 (control.txt).

## Closed form (derived)
G(n;m2) = cosh(w(8-|n|)) / (2 sinh w sinh 8w), cosh w = 1+m2/2 (image sum of e^{-w|n|}/(2 sinh w) over n+16j; checked numerically).

## Verdicts
| Predicate | Result |
|---|---|
| P1 closed form vs direct 16-term sum, 128 distinct nonzero m2 x n=0..4 = 640 cases (all 4095 nonzero spatial momenta map onto these 128 values; the rest are repeats) | PASS, max abs diff 9.0e-49 (tol 1e-35, 50-digit Decimal) |
| P2 independent plain-float direct 4-fold sum (65535 terms) vs Green K | PASS, max rel diff 1.6e-14 (tol 1e-11: double roundoff accumulation) |
| P3 K(0)>0, |K(n)|<=K(0) | PASS |
| Sub-agent: G closed vs direct at m2=2-2cos(pi/8), n=0..4 | PASS, max abs diff 6.66e-16 (tol 1e-13), control sum cos = -9.0e-16 ~ 0; I reran it (scratch copy) and got the same 6.66e-16 |

## Results (50-digit Decimal, 30 digits shown)
K(0) = 4.59711720810075987680612797526e-5
K(1) = 2.95053418892087773534077950338e-5
K(2) = 1.91229675153985667565436979283e-5
K(3) = 1.25407275612970961687866633600e-5
K(4) = 8.36761198729685332197301080076e-6
R = [K2^2 - 2K3^2 + K4^2]/K0^2 = 0.0573332378047662315959012113343

Float direct 4-fold sum agrees to ~14 digits (K(0) 4.5971172081007e-5).

## Failed predicates
None failed in the final run. No earlier failed runs. (Note: my first-run stdout was piped through `tail` inside the PCP check and not kept; I re-ran the script in a scratch directory to read the P1-P3 lines, identical numbers.)

## Not checked
No independent high-precision (>float) direct 4-fold sum; the exact m2=0 handling is by omission (prefactor q1^2+q2^2 = 0 there); the sub-agent used floats only; 6-minute budget, no convergence/tau scan.

## Delegated question
Closed-form G at m2=2-2cos(pi/8) vs direct sum, with known-answer control: PASS (above); files in grandchild/.

## Rerun
cd <this dir> (K_result.json is write-once; run in an empty copy):
  python3 k_green.py
  python3 grandchild/check.py   (also write-once; copy first)
PCP: P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P check --ws pcp --name k_green --expect-exit 0 -- python3 k_green.py
