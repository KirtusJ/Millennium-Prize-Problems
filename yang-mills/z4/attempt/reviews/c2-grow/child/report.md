# T224 report

**Control:** smallest lambda of det(D - lambda C)=0 is (10 - sqrt28)/6 = **0.784750** (control.txt).

## Results (results.json, from analyze2.py)
- (a) lambda_train = **0.015708940952963**; cond(C(TRAIN)) = **359.25042960** on the range of C (rank 304 of 308). The full 308x308 cond is infinite (numpy gives 2.37e16, pure rounding noise).
- (b) q = w'D(HELD)w / w'C(HELD)w = **0.015427727815759**
- (c) jackknife err (16 held streams, 15 left in each) = **0.00039567334747**. q is below lambda_train by 2.8e-4, which is 0.7 err.
- (d) Top three |w_k|·sqrt(C_kk), with max|w|=1: B.yz204.g01 **0.38237641**, B.yz204.L_no11 **0.35862822**, B.xy200.g00 **0.33472936**
- (e) Smallest single-mark held quotient: **B.yz204.Rv, 0.045581180** (to 8 digits, from results.json: 0.04558118683753429)

## Method
C(TRAIN) is exactly rank-deficient: 4 eigenvalues are about 1e-16, and the 5th is 2.6e-3. The same 4-dimensional null space N belongs to C(TRAIN), C(HELD), D(TRAIN) and D(HELD), because C·N and D·N are all below 1e-12. I did not use Cholesky. I did an eigendecomposition of C, dropped the 4 eigenvalues below 1e-10·emax, and whitened with W = U_r e_r^(-1/2). I took the smallest eigenpair of W'DW and set w = W v, which is the minimum-norm w. The quotients do not depend on the N component, since both C and D vanish on N. The next eigenvalues are 0.03408, 0.03987 and 0.04022, so lambda_train is separated from them.

## Predicates
- **First P1 (C(TRAIN) positive definite): FAILED in run 1** (exit 1, via pcp check K1). This was my own expectation and the target does not meet it: the data have 4 exact linear relations among the marks. I replaced it with a rank and null-space predicate (P1 revised) and kept the original failure on record.
- Run 2 and run 3 crashed because of my own bugs: I had cut out the `ev` line, and I tried to write a numpy array to JSON. I fixed both. Neither run wrote a results file.
- Run 4 (K4, exit 0) met every predicate:
  - P1 revised: rank 304, shared null space.
  - P2: D(TRAIN) symmetric and PSD, min eigenvalue -3e-17.
  - P3: lambda_train is at most every single-mark train quotient. This is a "for all" claim and 308 of 308 marks qualify.
  - P4: generalised residual below 1e-8.
  - P5: q >= lambda - 3 err.
  - P6: cond on the range is below 1e6. The cutoff comes from the 2.8e-3 eigenvalue gap, which predicts a cond of a few hundred.
  - P7: jackknife mean within 3 err of q.
- Tolerances: 1e-8, 1e-10 and 1e-12 are set against float64 eps (about 2e-16) with a margin for 308-dimensional accumulation. The 3 err comes from the task.

## Grandchild (T225, admitted with --parent T224, released)
- Question: the single-mark held quotient of B.xy000.g00, and cond2 of the first 15x15 block of C(TRAIN).
- Control question: smallest lambda of det(A - lambda I)=0 for A=[[3,1],[1,3]]. Its answer was 2.000000, which is correct.
- Result: quotient **0.06056377341**, cond2 **42.67905132**. Its predicates passed (15x15 block symmetric and Cholesky-PD, quotient finite and positive).
- I reread its code and reran it in rerun/ (pcp check K5, exit 0). It reproduced the numbers. My own run gives 0.060563773411 and 42.679051318 for the same two quantities, so they agree.

## PCP OS
- `pcp verify`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- Rust `pcpos verify`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
- The register has 5 checks, K1 to K5. K1 is the expected failure and K2 and K3 are the crashed runs. K4 is the real run. K5 is the grandchild rerun.
- The method was reported as not found, as expected.

## Rerun
```
cd /home/user/z4-workers/c2-grow/child
python3 analyze2.py        # needs results.json removed first (mode "x")
python3 rerun/check.py     # grandchild check; run with results.txt removed
```
