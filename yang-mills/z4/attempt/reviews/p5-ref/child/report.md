# T33 report — tests A, B, C (all programs in this directory; results in results/)

Control: control.txt = 0.006333 (1/(pi^2·2^4)). Grandchild control gave the same.

| Claim | Result | Numbers | Tolerance (source) |
|---|---|---|---|
| A1a pointwise 3-d residue formula = k0 trapezoid | PASS | max diff 2.2e-16 (2000 pts, n=0,1,3) | 1e-11 (periodic trapezoid is exponentially convergent) |
| A1b 4-d midpoint grid vs 3-d | PASS | G0 diff 3e-16, G1 diff 7.7e-10 (N=40; N=24 gives same 6 digits) | 1e-3 (fixed in advance; observed far smaller) |
| A2 G(0)=1/2 | PASS | 0.500000000000 | 10·Eq+1e-10, Eq=8.9e-16 (R1 vs R2 quadrature) |
| A3 G(1)=0.0688747 | PASS | 0.0688747458 | 5e-8 (7-decimal rounding) |
| A4 0<G(n+1)<G(n), n=0..15 | PASS | 16/16 n qualify; G(15)=2.05e-6, G(16)=1.58e-6 | margins > quadrature error |
| A5a pi²8⁴G(8)=1.092 | PASS | 1.092437 | 5e-4 (3 decimals) |
| A5b pi²n⁴G→1 | PASS | fit n=8..20: c0=1.00061 (c2=4.72, c4=73); value at n=20 is 1.01277 | \|c0−1\|<5e-3 (my choice; the limit is an extrapolation, not a proof) |
| A6 n⁶\|G−1/(pi²n⁴)\| bounded, n=2..20 | PASS | 0.308, 0.737, 0.859 (n=4 max), then falling to 0.5177 at n=20; quad error ≤3e-13 | max(n≥11) ≤ 1.5·max(n≤10) and all ≤ 14400/pi² |
| A7 bound, n=1..20 | PASS | 20/20 hold; rhs/lhs between 1895 (n=4) and 44978 (n=1) | LHS ≤ RHS + quadrature error. Bound is very loose. |
| A8 \|g−g0\| ≤ 3\|k\|³, \|k\|≤1 | PASS | max ratio 0.0834 over 500000 pts (seed 12345) | limit 3. The max ratio occurs at \|k\|=2e-6, where it is probably roundoff, not signal |
| B1 C¹=7/24 | PASS | 0.291666666667 (8 links, 24 plaquettes, kernel dim 1) | 1e-9 |
| B2 C²=0.49267 | PASS | 0.4926748 | 5e-6 (5 decimals) |
| B3 C³=0.49916 | PASS | 0.4991560 | 5e-6 |
| B4 monotone, <1/2 | PASS | 0.291667 ≤ 0.492675 ≤ 0.499156 < 0.5 (N=1..3 only) | exact comparison |
| B5 N=1 min eig of Q | PASS | 0.8377223 (7 links) | 5e-7 (6 decimals) |
| B5 N=2 min eig of Q | PASS | 0.1471218 (351 links); N=3 unclaimed: 0.054070 | 5e-7 |
| C1 P(O_p>t) ≤ P(all)^(1/V) | PASS | 144/144 grid points (L=2,4,8; β=.5,1,2,4; 12 t-values each). Smallest margin −2.2e-16 | 1e-9 + difference between two resolutions (Nmax, GL nodes halved) |
| C2 P(O_p>t) ≤ exp(f(β/2)−f(β)−t/2) | PASS | 144/144; min margin 0.0254 (β=4). Non-vacuous (rhs<1) at 106 points, all hold | same |

Counts: 18 table rows PASS, 0 FAIL (A: 10 rows, B: 6 rows, C: 2 rows).

Hypothesis counts for "for all" claims: A4 16/16 cases qualify; A7 20/20; C1 144/144 and C2 144/144 grid points.
Notes on strength: C1 is an equality up to rounding at 26 of 144 points (24 of them at L=8, where V=64 and the plaquettes are nearly independent). Those points pass through the 1e-9 tolerance and do not show strict inequality. C2 is vacuous (rhs ≥ 1) at 38 points.

## Failed predicates / defects
No claim predicate failed. Failures that were mine: (1) testA first run crashed on an n=0 division in my A6 code (no result file written; A1–A5 had already passed in that run); I fixed it and reran as tag r2. (2) testC was too slow twice (the first copy was recomputing Bessel coefficients per point, the second was recomputing Gauss–Legendre nodes). I killed both, with no result files, and added caching. They were performance defects, not predicate failures. Results come from C r2. (3) A BLAS thread pin was missing on A/B runs. Both are short, and the user CPU time was above wall time.
Files results/A_parentrerun.json and results/B_parentrerun.json appeared in my results directory. I did not write them; they look like a rerun by the parent. A is byte-identical to A_r2; B differs only at the 1e-15 level.

## Grandchild
Question: independently recompute G(1) by Schwinger parameter and Bessel functions, with no 3-d sinh formula. Task id T34 (label p5-ref-child-grandchild, parent T33), released with task-release. Outcome: 0.0688747458 (its error estimate about 1e-10). Its own control was 0.006333. It left no script, so I reran the method with my own code (rerun_grandchild.py, Richardson in the cutoff over 250/500/1000, tail ratio 4.0008 consistent with S^-2): 0.06887474584, difference 4e-11 from my 3-d value 0.0688747458. Agrees.

## Not checked
B for N≥4 (dense eigh too big for budget); B4 monotonicity is for N=1..3 only. A5 limit is an extrapolation, not a proof. A6/A7 only n≤20. C is for the stated grid only, and the 2-d law is taken as given (the Haar-normalised Z_L(b)=Σ_n (e^{-b}I_n(b))^{L²} is my normalisation for f). No other β, L or off-grid t. Quadrature error estimates come from self-convergence, apart from A1b and the grandchild's independent method. No proof of any claim.

## Rerun
cd /home/user/z4-workers/p5-ref/child; P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"   (fresh dir)
$P check --ws pcp --name testA --expect-exit 0 -- python3 testA.py <newtag>
$P check --ws pcp --name testB --expect-exit 0 -- python3 testB.py <newtag>
OMP_NUM_THREADS=1 $P check --ws pcp --name testC --expect-exit 0 -- python3 testC.py <newtag>
python3 rerun_grandchild.py
$P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
(result files open with mode "x", so use a new tag each time)

## PCP OS verification (last lines)
- Python: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
Register contains checks K1 (testA), K2 (testB), K3 (testC), all exit 0 as expected. Not in the register: the rerun of the grandchild method, and the earlier killed runs.
