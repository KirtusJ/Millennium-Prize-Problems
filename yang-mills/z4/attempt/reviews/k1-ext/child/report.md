# T120 report — Gaussian transfer operator
Control: arsinh(1)=0.881374 (control.txt).

## Verdicts
- A STANDS: grid top eig matches exp(-asinh s) to <=2e-16 for s=0.25,1,√2,√3,3; eigenvector positive, log-quadratic to 4e-14 (alpha(1)=1/√2).
- B STANDS (measured): free-convolution box of total length 2L gives lam<1, increasing: L=5,10,20,40 -> 0.88034,0.96154,0.98910,0.99710; 1-lam(L=40)=2.9e-3 vs Dirichlet-box estimate 2π²/(2L)²=3.1e-3 (estimate is my heuristic, only roughly matched). Truncation to a box is a Dirichlet-like cutoff of the spectrum edge, so the sup of 1 is approached as L->inf, never attained.
- C STANDS: sigma=1, b=0.7, 3: diff <=3.3e-16 (centred and fixed box).
- D STANDS (with caveat): dense 2D (h=0.35,L=7, s=(1.3,0.6), c in range, rotated A) = 0.192574 = exact, diff 1.1e-10. Rank-one: orth. factor ratio = exp(-|c|^2/2) to 1e-10; large-box product 0.185193 < claim 0.185732 (approach from below, free direction is claim-B-like, within 0.3%). Rank-one claim's "norm" is a supremum, not attained.

## Tolerances
A,C: 1e-6 / 1e-9 predicted from midpoint-rule on Gaussian integrand (error exp-small in 1/h^2) and box tails e^{-L^2 s^2/4}; observed ~1e-16 (roundoff). D1 tol 2e-3 was loose, h=0.35; observed 1e-10. B: box truncation (L), not h, controls the gap.

## Failed predicates
None failed. One own-process issue: the first-run "B estimate" formula in the docstring was left vague (printed to stdout, not saved); I only report it from the results above. Also the run took 104 s wall / 4m51 CPU: numpy BLAS used multiple threads, violating the 1-core limit (my defect; I did not set OMP_NUM_THREADS=1).

## Counts
met 20, failed 0, measured only 1 (B scaling estimate; plus the 2D-vs-product calibration print).

## Sub-agent
Task id T121 (admitted, released). Question: independently derive lambda for sigma=1 via Gaussian ansatz. Outcome: alpha=1/√2, lambda=√2-1=0.414213562373, grid agrees ~1e-14 (L 10-14, h 0.05-0.2). Its control.txt = 0.693147. I reread result.md and check_output; my rerun of check.py failed only because it opens check_output.txt with mode "x" (file already exists) — not a defect; the output file was read instead. Its tolerance (1e-12) was argued, not measured separately.

## Verify (last lines)
- python: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- rust: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
(ACR method not found at init: expected.)

## Rerun
cd /home/user/z4-workers/k1-ext/child; rm -f results_gauss.json (mode x); OMP_NUM_THREADS=1 python3 check_gauss.py
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P verify --ws pcp; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
