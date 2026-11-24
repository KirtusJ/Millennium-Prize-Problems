# T245 report (child of T244)
Control: I_1(1) = 0.565159104 (control.txt; exact series, control.py). mpmath/scipy/sympy are NOT installed: I used numpy, Fractions and decimal (60 digits).

| S | Verdict | Evidence |
|---|---|---|
| S1 | PASS | pi^2 sqrt(e)/4 = 4.068056677368. 3808 grid cases (k in [0,200], theta in [0,pi], incl. theta=(1+k)^-1/2), 3808 qualify, 0 violations of p <= min(1,C(1+k)^1.5 theta^3). max p/bound = 0.065008916 at k=200, theta=0.001. Ratio of the two derivation bounds equals C(1+k)^1.5 theta^3 to 4e-16 (exact algebraically). Side conditions hold for 32/32 k values. |
| S2 | PASS | k=20.398861452: p(0.05)=0.003072388, p(0.2)=0.156180437, p(0.6)=0.934803630. They round to the stated 0.00307, 0.156, 0.935 (tol = half unit of the last stated digit). |
| S3 | PASS | 72 (N,c,beta) cases, max rel diff 1.9e-15; algebra: 3N^3/8 * C * c^3 N^-4 = 3 pi^2 sqrt(e) c^3/(32N). |
| S4 | PASS | Exact Fractions: p-q = 0 + (-1/48)k^2 + (1/384)k^4; p' = -k/16 + (5/384)k^3; w' = k/2 - (1/8)k^3. Identity R'=1-3R/k-R^2 vs termwise-derivative R' at k=0.5,2,6,20: max diff 1.3e-59. |
| S5 | PASS | Exact rational enclosure (33 terms + tail bound, r=9/(34*35)): R'(6) in [0.036885895497642221, same] (width 1e-45), strictly inside (0.036885895, 0.036885896). Decimal-60 direct: 0.0368858954976422227980718751. mpmath not available, so decimal substitutes for mpmath (a deviation from the task). |

Tolerances: S1 slack 1e-12 (Gauss-Legendre float64 error, expected <1e-13); S3 1e-12 (float rounding); S4/S5 decimal 1e-40 / 1e-20 (60-digit working precision); S2 half-unit of last stated digit.

## Failed predicates
None of the S1-S5 predicates failed. One expected non-pass: control.py rerun under `pcp_os check` exits 1 because control.txt already exists (mode "x"); I registered it with --expect-exit 1, and it is a property of the never-overwrite rule, not a defect of the target. mpmath absent: my expectation (tool availability), not a target defect.

## Not checked
No proof of S1 for all k (only a grid up to k=200, not k>200 or beyond the grid); the derivation's inequality steps were checked only numerically on the grid. S4 O(k^4) remainders are shown by the next coefficients only, not bounded. S2's "~" is read as 3-s.f. rounding. No real mpmath run. The "for all" qualifying count for S1 is 3808/3808 cases on the grid.

## Grandchild
Question: independent check of R'(6) enclosure (S5) by a different method (continued fraction + identity, plus Richardson numerical differentiation). Task id T246 (admitted by principal under T245, released by me: event 492). Outcome: control 0.565159104 OK; R'(6)=0.036885895497642 (Richardson 0.036885895495070), P1 and P2 PASS. I reread its script and reran it in a scratch copy: identical output. It agrees with my value to 15 digits.

## PCP OS
`pcp_os.py init` reported "method: not pinned / ACR not in use" (expected). Checks K1..K3 (control, s1_s2_s3, s4_s5) recorded.
- Python verify last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust verify last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## Rerun
```
cd /home/user/z4-workers/g2-fid/child
python3 control.py            # exits 1 if control.txt exists
python3 s1_s2_s3.py <newtag>  # writes results_s123_<newtag>.txt
python3 s4_s5.py <newtag>     # writes results_s45_<newtag>.txt
cd grandchild && mkdir ../gc2 && cp t246.py ../gc2/ && cd ../gc2 && python3 t246.py
```
Counts: met 5 (S1-S5), failed 0, measured only 0 (S1 is grid evidence, not a proof).
