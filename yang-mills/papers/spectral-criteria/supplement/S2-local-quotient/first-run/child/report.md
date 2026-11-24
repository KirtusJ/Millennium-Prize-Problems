# T221 report
**Control:** 0.929632 (control.txt).

## Key caveat
C(TRAIN) is exactly singular (rank 11 of 14): B.L_no00/10/01 are exact duplicates of B.g00/10/01. D annihilates the same 3 null directions (|D N|<1e-17), so the eigenproblem is 0/0 there. Cholesky fails; full numerical cond(C(TRAIN)) = 2.58e17 (true value infinite). I solved on the 11 independent marks (w = 0 on the 3 duplicates; adding null vectors changes neither lambda nor q, checked). This is a deviation from the literal statement.

## Results (reduced 11-mark problem)
- lambda_min = 0.02691319 (next 0.05173, 0.06930)
- w (largest = +1): B.g00 -0.568319, g10 -0.805731, g01 -0.546735, g11 0.049551, Rv -0.517439, Rh -0.630043, L_no00 0, L_no10 0, L_no01 0, L_no11 -0.811886, n00 +1, n10 0.661133, n01 0.924056, n11 0.122737
- q(HELD) = 0.02674971 ± 0.00069346 (jackknife n=16; LOO mean 0.02675119)
- Smallest single-mark quotient on HELD: B.Rh = 0.04807613 (all 14 in an3.result.txt)
- cond(C(TRAIN)): full 14x14 numerically 2.58e17 (singular); reduced 11x11 = 43.44

## Predicates
- an.py (P3: C(TRAIN) positive definite): FAILED — my expectation was wrong; target defect (duplicate marks). Kept (pcp K1, expected exit 1).
- an2.py diagnostic: null space dim 3, D vanishes on it: met (K2).
- an3.py P1–P7 (reduced cond<1e8 [43.4], symmetry 1e-12, residual<1e-10 [1e-15], eigen gap, null-shift invariance, positive denominators, lambda<=single-mark quotients): all met (K3). Tolerances: 1e-12/1e-10 = float64 roundoff scale; 1e-12 null threshold vs observed ~1e-17 vs 1.5e-2 gap.
- No "for all" predicate needing per-case qualification (P7 was checked over all 11 marks: 11/11 qualify).

## Grandchild
Task T222 (parent T221), released. Question: B.g00 single quotient on HELD, and cond(C(TRAIN)). Control (diag(2,5), I -> 2.000000) correct. Returned 0.06172628688 and cond 2.582863546e17 (3 sv < 1e-12); reread and rerun (K4): identical, agrees with mine.

## PCP
`pcp_os.py verify --ws pcp` last line: "A pass is a fact about these bytes..." — preceding line "result: PASS". Rust `pcpos verify pcp/register.jsonl` last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right." (ACR method packet not found at init; expected.)

## Rerun
cd child; python3 -I an.py (exits 1); python3 -I an2.py; rm an3.result.txt; python3 -I an3.py; cd grandchild && python3 -I t222.py
