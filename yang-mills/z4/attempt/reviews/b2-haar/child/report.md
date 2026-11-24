# T216 report: R=I2/I1, w=k^2 R'

Control: sum 1/n^2 = 1.644934 (control.txt).

## Verdict
- **(A) CORRECT** at zeros of w'. General identity: w'' = p(3-2w) + w/k^2 - w'(2R+1/k), so (A) holds exactly when w'=0. Numerics confirm the general identity (P3 residual 7.7e-8).
- **(B) CORRECT** at zeros of w' (y=w). With w'=0 we have p=w/k^2, so (A) = w(3-2w)/k^2 + w/k^2 = (4-2w)w/k^2 = (B). (P6: |A-B| < 3e-14.)
- Caveat: w' has no zero for k>0 on the grid I scanned (k in (0.05,60), step 0.05; min w' = 2.2e-4, w->3/2), so the at-zero formulas are vacuous there. I tested the general identity instead. Away from a zero, A and B do NOT equal w'' (residual 0.58 at k=1,2,5, P7). That is expected. It is not a failure of the formulas. A grid scan does not prove there is no zero anywhere.

## Derivation
p=R'=1-3R/k-R^2. p' = -3p/k + 3R/k^2 - 2Rp.
(i) w' = 2kp + k^2 p' = -kp + 3R - 2R k^2 p = **R(3-2w) - w/k**.
(ii) w'' = p(3-2w) - 2R w' - w'/k + w/k^2 (using w/k = kp... derivative of -w/k is -w'/k + w/k^2) = p(3-2w) + w/k^2 - w'(2R+1/k). At w'=0: (A). Substituting p=w/k^2: (B).
No sympy installed, so the symbolic check is by hand plus an exact-Fraction power-series check (P4: coefficients of w' equal those of R(3-2w)-w/k through k^13; R = k/4 - k^3/96 + k^5/1536 ...).

## Grandchild
Task T220 (b2-haar-grandchild, parent T216), released. Control 1.644934 OK. w(1,2,5) = 0.221726, 0.650838, 1.273619; w' = 0.39234, 0.41017, 0.07097, all > 0.
Its predicate (c) (FD vs formula within 1e-6) failed at k=5 (4.6e-6). The cause was my tolerance, not the target: the FD noise from two nested differences at h=1e-5/1e-4 was underestimated. I reran independently (regrand.py, outer h=1e-3): w matches within 1e-7, FD vs formula agrees to ~5e-9 at k=5. PASS.

## Failed predicates
- check.py exit 1: OverflowError in my own Bessel series (factorial division). It was my code defect. Fixed in check2.py with predicates unchanged. The failed run stays in the register.
- grandchild (c) at k=5: my expectation (tolerance), see above.
- Tolerance sources: FD truncation h^2 and roundoff eps/h (noted in the check.py docstring).

## Rerun
cd /home/user/z4-workers/b2-haar/child
python3 check2.py   # check2_out.txt kept
python3 regrand.py
(grandchild: cd grandchild && python3 grandchild.py; its results.txt is opened with mode 'x', so delete it first)

## Verify (last lines)
result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
