# T57 report
Control: control.txt = 6 (faces of a cube), written first.

## Verdicts
| Item | Verdict | Evidence |
|---|---|---|
| A: g_y=g_x U_xy gives identity tree links | STANDS | max Frobenius dev 6.3e-16 over 20 draws (< 1e-12); algebra g_x U g_x^{-1}... = U U^{-1}=1 (result_A2.json) |
| A: printed g_y=U_yx^{-1}g_x not identity in general | STANDS | max dev 2.45, 20/20 draws > 1e-12. Note: first link (x0,x1) is identity under both (g_0=1); failure only on (x1,x2) (commutator) |
| B1: m_c!=0 => some abs(theta)>=pi/3 | STANDS | 5000 qualifying (m!=0) cases of 88920 draws, 0 violations, min of max abs angle 1.379 > 1.047; proof: all <pi/3 => abs(sum)<2pi => m=0 |
| B1: => s>=1/2 => O_p>=beta/2 | STANDS | 1-cos monotone on [0,pi]; min s over cases 0.81 |
| B1: union bound 6 exp(D-beta/16) | STANDS (with strict/non-strict step) | exponent t=beta/2, /8 = beta/16; 6 faces; see note |
| B1 example all six = pi/3 | STANDS exactly, DEFECT in raw floats | exact: sum 2pi, s=1/2 (70-digit check, sub-agent). Double: s=0.4999999999999999 so `s>=0.5` evaluates False; 1-ulp artifact |
| B2: exponent beta*eta/(8K^2) | STANDS | rel err 1.1e-15 over 1000 random params; each face: O_q>=beta eta/K^2, divide by 8 |
| B2: chi(V)<=K max chi, s(V)>=eta => max s>=eta/K^2 | STANDS | 0 violations in 10000 cases; proof: sqrt(eta)<=chi(V)<=K max chi, square (all nonneg) |
| Hypothesis that angle vectors satisfy sum=2 pi m_c (given geometry) | NOT CHECKED | taken as given; only sampled vectors with that property |
| The tail estimate mu(O_p>t)<=exp(D-t/8) itself | NOT CHECKED | assumed |

Strict vs non-strict: the estimate is for O_p>t; we have O_p>=beta/2. For every t<beta/2, {O_p>=beta/2} is inside {O_p>t}, so Pr<=exp(D-t/8); let t increase to beta/2 (continuity of the right side) gives Pr(O_p>=beta/2)<=exp(D-beta/16). Same for B2. The pi/3 example sits exactly on this boundary, so the non-strict form is needed.

Tolerance sources: 1e-12 = ~3 orders above double eps (2.2e-16) times the few operations in 2x2 products/cos sums; observed errors 6e-16, 1.1e-15, 8.9e-16.

## Failed predicates
1. First run of prog_A.py failed: numpy int64 not JSON serialisable. My own bug, not the target. Left a partial result_A.json (never overwritten); predicates unchanged, rerun wrote result_A2.json.
2. PB5 (raw float `1-cos(pi/3)>=0.5`) was recorded as an expectation of mine to fail; it did return False. That is a float rounding artifact, not a defect of the claim.
No predicate of the claim itself failed. Note PB1 sampling counts: qualifying 5000 / 88920 draws (half of draws forced to m!=0, many rejected for wrap).

## Not checked
Real SU(2) gauge field on larger forests; U(1) cubes beyond sampled vectors (sampling, not proof; proof is by the sum argument above); SU(N) other than SU(2); the register's ACR method (not pinned, expected).

## Delegated question
Task T60 (label p8-rev2-grandchild, parent T57): independent 70-digit recomputation of the pi/3 boundary. Control (cube faces=6) passed. Returned: sum-2pi = 0 (to 1e-69), s-0.5 ~ -1e-69, double s=0.4999999999999999, smallest double theta with s>=0.5 is 1 ulp above math.pi/3. I reread and reran check.py in rerun/g: identical output. T60 released. Caveat: numeric (not symbolic) exactness; sympy/mpmath absent.

## Rerun
cd child; python3 prog_A.py (needs a fresh dir; result files open with "x"); python3 prog_B.py; python3 grandchild/check.py
Register: P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; $P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl

Counts: met 8 items (+ 1 exact-only), failed 0 claim predicates (2 own-side failures above), measured only: all numerical evidence is sampling.

## Addendum: register check K3
K3 (grandchild_check) exited 1: my own error — rerun/g already held results.txt from my earlier manual rerun and check.py opens it with mode "x" (FileExistsError). Kept in the register as a failed check; K4 (fresh dir rerun/g2) passed.
