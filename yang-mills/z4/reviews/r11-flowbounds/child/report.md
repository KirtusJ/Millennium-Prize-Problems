# Report, child run1

**Control:** lowest nonzero khat at N=16 = 32 sin(pi/16) = **6.2429** (control.txt).

## Numbers (l=1, s=0.005; results_child_run1.json)
| N | C(0) | M1/M0 |
|---|---|---|
| 16 | 574.67958 (574.6795784492) | 21.956692 (21.9566922730) |
| 32 | 542.73368 (542.7336835571) | 21.711833 (21.7118325851) |

Methods: position space (FFT of the mode sum for D0 = sum a e^{ikr}, D1 = sum a*khat e^{ikr}; the x,y sum is an FFT convolution; M1 = 2b^6 sum f f * 2 D0 D1) and momentum form (cyclic autoconvolution of a, weighted by |fhat_b|^2). The two agree to roundoff.

## Predicates (fixed in compute.py docstring before the first run)
- P1 position vs momentum, rel diff < 1e-10 (tolerance: double roundoff ~1e-13 on sums of <=3e4 terms): MET. N=16: C0 diff 0.0, M1 diff 1.4e-16. N=32 also met (values in json).
- P2 N=16 brute-force double sum over k,k' agrees with the momentum form, rel < 1e-10: MET (C0 = 574.6795784492074 vs 574.6795784492108, about 6e-15).
- P3 control min khat = 32 sin(pi/16) within 1e-12: MET.
- P4 C0, M1 positive and finite: MET.
- P5 f > 0 on the grid: MET (min 0.108). This is true by construction.
- Failed predicates: none. No "for all" predicate was used, so no per-case qualification count.
- Measured only: sub-agent finite-difference values (below).

## Sub-agent (grandchild/)
Asked: control first (it wrote 6.2429, correct), then an independent N=16 recomputation of M1/M0 by finite difference of C(t) from direct mode sums. It was told not to use the analytic moment. It returned C(0)=574.6795784492 (matches mine). Central difference at h=1e-4 gave 21.9567152 (error ~2.3e-5, shrinking as h^2: 2.3e-3 at h=1e-3). The one-sided fwd3 estimate (t>=0 only) at h=1e-4 gave 21.9566922, agreeing with the analytic 21.9566923 to ~1e-7. I reran grandchild/run.py myself (also under pcp check K2) and got identical numbers.
Caveats it reported, which I confirmed by reading the output: the "richardson" rows in results.txt use a wrong combination (4a-b)/3, so ignore them. results.txt was written with tee, not mode 'x', so my rerun overwrote it with identical content. This was the sub-agent's slip, not a defect in the target.

## Rerun
cd /home/user/z4-workers/r11-flowbounds/child
python3 compute.py   # fails if results_child_run1.json exists (mode "x"); delete it to rerun
(cd grandchild && python3 run.py)
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name compute --expect-exit 0 -- python3 compute.py

## Verify, last lines
- `$P verify --ws pcp`: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- `pcpos verify pcp/register.jsonl`: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
(PCP init reported the method as not pinned, as expected. Checks K1 compute and K2 grandchild_rerun both exited 0.)
