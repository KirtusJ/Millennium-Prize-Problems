# T109 report: constant-mode mass in abelian quadratic lattice gauge theory
Control: arcosh(2) = 1.316958 (control.txt; grandchild got the same).

## Method
box.py builds d, the curl and M = curl^T curl as explicit matrices. The slice is ker d^T = range(d)^perp. A = U c + N a, where U holds the three constant-direction vectors and N is an orthonormal basis of the nonconstant slice. The exponent A^T M A/4 + A'^T M A'/4 + |A'-A|^2/(2s^2) is Schur-complemented over (a,a'), which gives Q(c,c'). On the slice, P(A'-A) = A'-A (checked to 7e-15).
Result file: result_box.txt (contains the full 6x6 Qm for every case).

## Verdicts (all 6 cases: 3 boxes x s in {0.3, 0.1}, 6/6 qualify)
| box | n | (d) slice dim (2n+1) | (b) Q depends only on c-c' | kappa | (c) kappa/n |
|---|---|---|---|---|---|
| (2,2,2) | 8 | 17 = 2n+1 | yes (dev 0) | 8 | 1 |
| (3,2,2) | 12 | 25 = 2n+1 | yes | 12 | 1 |
| (3,3,3) | 27 | 55 = 2n+1 | yes | 27 | 1 |

(a) The coefficient matrix is Qm = (kappa/s^2) [[I3, -I3],[-I3, I3]] in v = (c,c'), with no off-diagonal direction mixing (rel. dev < 1e-30). Example for (3,2,2): the diagonal entries are 133.333 = 12/0.09 at s=0.3 and 1200 = 12/0.01 at s=0.1. kappa is s-independent to 1e-15.
(b) Yes: Q depends only on c-c'. kappa = n.
(c) kappa/n = 1 to about 1e-16, so the prediction holds. There is no magnetic mass term, because M annihilates the constants and the constants are orthogonal to the nonconstant slice. The a,a' integrals therefore decouple and only contribute a c-independent factor. M is positive definite on the nonconstant slice (min eig 4 for 2x2x2, 3 for the others), so the integral converges.
(d) Slice dim = 2n+1 in all three boxes. This is 3 constants plus 2n-2 nonconstant modes.

## Predicates
Fixed in the box.py docstring (P1..P6). None failed. Tolerances: 1e-9 relative and 1e-10 absolute, which sit well above the observed double-precision error of ~1e-13 and below any physical effect.
The "failed" check K2 (box_rerun, expect-exit 1) was a deliberate negative control. Rerunning box.py exits 1 because result_box.txt exists and is opened with mode 'x'. The exit code came from that rule, not from a defect in the target.

## Grandchild T111 (j1-box-grandchild), released
It recomputed (3,2,2) with Fourier modes. Slice dim 25, kappa = 12 for s = 0.3 and 0.1, and the real-space and Fourier slice spectra of M agree. I reread its files and reran kappa.py in a scratch copy; result.md was identical.
Caveat: its kappa comes from the Gram norm of the constants. It relies on the decoupling argument, so it is a consistent check but not an independent integral. My Schur complement is the one that tests the decoupling numerically.

## Not checked
- Non-cubic or other boxes, and boxes with an N_i = 1 or 2 degeneracy. In an N=2 direction, x+e_i = x-e_i, so some links and plaquettes coincide; the matrices still carry them as written.
- The overall normalisation (the c-independent prefactor).
- Any gauge-orbit measure other than Lebesgue on L.
- The norm convention. kappa = n assumes the Euclidean norm on R^(3n) and the per-direction constant vector with entries 1.

## PCP record
Init: the method packet was reported not found, as expected.
`python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." (the preceding line is "result: PASS").
`pcpos verify pcp/register.jsonl` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## Rerun
cd /home/user/z4-workers/j1-box/child && rm -f result_box.txt && python3 box.py
Grandchild: copy grandchild/kappa.py to an empty directory and run python3 kappa.py there.
