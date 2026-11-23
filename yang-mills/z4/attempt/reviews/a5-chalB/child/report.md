# Report: Claim S3a(2D), P_beta(O_p>t) <= C exp(-t/8), beta>=2

Control (step 0): control.txt = 0.240194 (= I_2(1)/I_1(1); asserted against power series to 1e-9).

## Verdict table
| Item | Verdict | Evidence |
|---|---|---|
| S3a(2D) on the tested grid (8 betas, t<=min(40,2beta)) | STANDS | 888 cases, all P e^{t/8} <= 2; C_emp = 1.000000, attained at t=0 (P=1) for every beta |
| (b) tail rate r(beta) >= 1/8 | STANDS | r = 1.664 (b=2, t=3.8), 1.226 (4), 1.058 (8), 0.943 (16), 0.927 (32), 0.922 (64), 0.920 (128), 0.919 (256); all >> 0.125 |
| (c) Gamma(3/2,1) limit | STANDS (measured) | sup_t in [0,20] abs(P-Q): 1.109e-1, 3.819e-2, 1.630e-2, 7.652e-3, 3.716e-3, 1.832e-3, 9.096e-4, 4.533e-4 (b=2..256); roughly halves per doubling, i.e. O(1/beta) |
| (d) mean of O vs beta(1-I2/I1) | STANDS | rel. diff <= 3e-13 for all 8 betas (1.133745147 at b=2 ... 1.498529405 at b=256) |
| Sub-agent P_8(O>4) | STANDS | mine 0.03988840; agent GL 0.03988840; MC 0.039959 +- 0.000138 (0.5 SE) |
| Claim for beta<2, t>40, beta>256, other C | NOT CHECKED | outside grid |

Note: the claim is far from tight on this grid: true decay rate ~0.92 (approaching 1 as in Gamma(3/2)) vs 1/8. t grid is 0..40 at step 0.25; for beta=2 only t<=4 exist, P=0 at t=4 (counted as a met case).

## Counts (met, failed, measured only)
- P1 quadrature convergence (2000 vs 4000 nodes, rel 1e-9; tolerance = 3 orders below 6-digit reporting): 888 met, 0 failed.
- P2 mean (1e-9 rel; exact via series recurrence, independent of quadrature): 8 met, 0 failed.
- P3 per-case H: P e^{t/8} <= 2 (C=2 my own test constant; claim gives none): 888 met, 0 failed (per beta: 17,33,65,129,161x4).
- P4 rate >= 1/8: 8 met, 0 failed.
- P5 sup|P-Q| strictly decreasing in beta (my expectation): met (7/7 steps).
- P6 monotone in t: 888 met, 0 failed.
- Measured only: C_emp, r(beta), sup|P-Q|, means.
- Control (step 0): met. Sub-agent control: met.

## Failed predicates / run defects (all my own, none of the target)
- Run 1 (tail.py) exceeded the 1-minute limit: Gauss nodes recomputed in every call; killed, results_tail.csv empty. My defect (performance), not a predicate on the target.
- tail2.py ran (exit 0) but pcp check did not retain stdout; reran identical code as tail3.py with redirect (csv byte-identical, cmp same). Output in out_tail3.txt.
- Cosmetic: csv numbers are written as "np.float64(...)" text; values are intact.
- My mental recall of I_2(1)/I_1(1) before computing (~0.136) was wrong; the computed 0.240194 matches the series, so it was my expectation, not a defect.

## Not checked
Anything outside grid; rigorous (interval) error bounds; t-grid between steps (sup could lie off-grid, but P e^{t/8} is maximal at t=0 by monotone P and 1 = P(0), and e^{t/8} growth is dominated by observed decay r~0.9, so a sup between grid points exceeding 1 is implausible but not proven); 2D free-boundary/axial-gauge independence of plaquettes taken as given.

## Delegation
Question to sub-agent (own dir grandchild/): control "integral of sin^2 over [0,pi] to six decimals", then P_8(O>4) by MC (rejection, seed 12345, 2e6) plus Gauss-Legendre in a different variable. Control answer 1.570796: correct (pi/2 = 1.5707963), graded before use. Returned MC 0.039959 +- 0.000138, GL 0.03988840. I reran nothing of its script (it lives at /tmp/claude-0/mc.py, outside my dir) but recomputed the number myself: 0.039888399 from results_tail3.csv, agreement to 8 digits with its GL value; MC consistent within 0.5 SE. grandchild/result.txt and control.txt present.

## PCP OS
- python verify: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- rust verify last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
- init reported method not found, as expected. Checks: K1 control, K2 tail2, K3 tail3 (all exit 0). tail run 1 was killed and has no check record.

## Rerun
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name control --expect-exit 0 -- python3 control.py
$P check --ws pcp --name tail3 --expect-exit 0 -- sh -c "python3 tail3.py > out_tail3.txt 2>&1"
$P verify --ws pcp; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
(result files open with mode "x": run in a fresh directory or rename outputs.)
