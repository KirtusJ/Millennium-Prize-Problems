# T74 report: Bessel ratio claims A, B, C

Control: I_3(4)/I_1(4) = 0.341953 (control.txt). The sub-agent got the same value.

## Verdicts (grid x in {0.5,...,512}, 11 points)
| Claim | Verdict | Evidence |
|---|---|---|
| A (nu=0..200) | STANDS on the grid | 2211 cases, 2211 met, 0 failed. Source is the log-series pass, results2.txt. |
| B (n=1..200) | STANDS on the grid | 2200 cases, 2200 met, 0 failed. |
| C (n+1/2<=x) | STANDS on the grid | 647 of 2200 (n,x) pairs satisfy the hypothesis. All 647 were tested, 647 met, 0 failed. |

Counts as "met, failed, measured only":
- A: 2211, 0, 0.
- B: 2200, 0, 0.
- C: 647, 0, 0.

"Measured only" is a case where the slack lies within the error tolerance, or where the value is unreliable.

## Pass 1: trapezoid (check.py, results.txt)
- It decided only 482 of 2211 A cases, 471 of 2200 B cases and 408 of 647 C cases (met).
- The rest were measured only (A 1729, B 1729, C 239). There I_n e^-x is below the roundoff floor of about 1e-16, or it underflows. Doubling N from 4096 to 8192 therefore gives a relative error that is too large.
- No failures in pass 1.
- Pass 2 (check2.py) was written to resolve those cases. It uses the positive-term log power series with the same predicates.
- Agreement between the two Bessel routines: max |log I_n(trapezoid) - log I_n(series)| = 1.1e-13, over the cases where the scaled I_n exceeds 1e-3.

## Tolerances
- Pass 1: the error of each I_n is the doubling difference plus a 2e-16 roundoff floor. A case is decided only if |slack| exceeds 4 times the combined relative error.
- Pass 2: a relative error of 2e-11 per I_n is assumed. This is a margin of about 10 times over the lgamma rounding estimate of about 1e-12. It is an assumption supported by the 1.1e-13 agreement above, not a measured bound.
- The smallest tolerance was 2e-13 (A) and 1.6e-10 (B, C). The smallest decided slack was 9.5e-12 in A and 1.1e-5 in B.

## Worst-case slack (series pass; trapezoid pass agrees where reliable)
- A: absolute slack 9.5e-12 at (nu=200, x=0.5). This is small only because r is tiny (about 1e-3). The tightest relative case is (nu=0, x=512), hi - r = 9.546e-07, and the sub-agent confirmed it.
- B: log(rhs) - log(lhs) = 1.1420e-05 at (n=1, x=512). Confirmed at 50 digits by the sub-agent.
- C: 1.4677e-03 at (n=1, x=512). Confirmed at 50 digits.
- Both B and C tighten toward x -> infinity at n=1. The grid stops at 512.

## Failed predicates
None. I rewrote no predicate after the first run.
- The measured-only counts in pass 1 came from my expectation that trapezoid would work everywhere. That was my own expectation failing, not a defect of the claims.
- The docstring of check.py has a garbled line ("NO:"). The predicate that applies is the last one stated there.

## Not checked
- Non-grid x. Real x between grid points and x > 512 were not tested, so this is not a proof.
- Non-integer nu.
- Claim C for n+1/2 > x is outside its hypothesis. I did not test it.
- The proofs of A, B and C.

## Sub-agent
- Question: independently recompute, at 50-digit decimal series, I_201(8)/I_1(8) and the worst cases of B, C and A.
- Task id: T76, parent T74. Admitted and released. Its control matched.
- Outcome:
  - I_201(8)/I_1(8) = 1.76377907211476e-259. My float series gives 1.7637790721149e-259.
  - B worst case: 1.1420408e-05, matching.
  - C worst case: 1.4677062e-03, matching.
  - A boundary: hi - r = 9.5460838e-07, matching.
- I reread its files and reran g.py in a scratch copy. The output was identical.

## PCP OS
- python verify: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- rust verify: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## Rerun
```
cd /home/user/z4-workers/g1-toron/child
python3 control.py
python3 check.py      # writes results.txt, mode x; remove it first to rerun
python3 check2.py     # writes results2.txt, mode x; remove it first to rerun
cd grandchild && python3 g.py c && python3 g.py r   # control.txt / report.txt, mode x
```
