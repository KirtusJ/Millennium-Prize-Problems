# Conversion check h_3 -> van Baal/Luscher normalisation

Control: -ln tanh 3 = 0.004958 (control.txt).
Inputs read: only inputs/grounding.md and inputs/A3_NOTES.md. Program: check.py (predicates and tolerance sources in its docstring, written before the first run). Output: results.txt (mode 'x').

## Item 1: conversion factor. Verdict: STANDS
h_3 = -1/2 Lap + 2 S, vB = -1/2 Lap + 1/2 S, S = sum_{i<j}|x_i x x_j|^2. With x = a y, Lap -> a^-2 Lap_y and S -> a^4 S(y), so h_3 = a^-2 [ -1/2 Lap_y + 2a^6 S(y) ]. Setting 2a^6 = 1/2 gives a = 4^(-1/6) and h_3 = 4^(1/3) h_vB, so e_vB = 4^(-1/3) e_h3 = 0.629960525 e_h3. This agrees with A3_NOTES (Y = 4^(-1/6) c) and grounding.md (h_3 = 4^(1/3) h_vB). The sum is read as i<j, as in grounding.md. C1 numerically: 2a^6 = 0.5 and a^-2 = 4^(1/3) to 1e-14.

## Item 2: ground energy. Verdict: STANDS, within rounding
6.534885 * 4^(-1/3) = 4.1167195851. Published value 4.116719735. Difference (ours - published) = -1.4993e-7.
Tolerance from rounding 6.534885 to 6 decimals: 5e-7 * 4^(-1/3) = 3.155e-7. The |difference| is 0.475 of the tolerance, so it is within it. The claim "difference 1.5e-7" is correct (magnitude 1.4993e-7; sign negative).

## Item 3: the two gaps. Verdict: STAND, within rounding
| input | converted | quoted | diff | tol |
|---|---|---|---|---|
| 3.012539 | 1.8977806499 | 1.89778 | +6.5e-7 | 5.3e-6 |
| 3.012539 | 1.8977806499 | 1.8977806 | +5.0e-8 | 3.6e-7 |
| 3.602838 | 2.2696457178 | 2.26965 | -4.3e-6 | 5.3e-6 |
| 3.602838 | 2.2696457178 | 2.2696457 | +1.8e-8 | 3.6e-7 |

Tolerances: the quoted value's own rounding (5e-6 for 5 decimals, 5e-8 for 7 decimals) plus 3.155e-7 from the input rounding. The 2.26965 comparison uses 83% of its tolerance, which is expected, since 2.2696457 rounds to 2.26965 at 5 decimals.
Caveat: these compare our converted numbers with each other's quoted numbers. None is an independent literature value. The Luscher-Muenster digits were never obtained (grounding.md Q1c/Q1d, NOT CHECKED).

## Predicates
Met: C1, P1, P2, P3a, P3b, P3c, P3d (7). Failed: none. Measured only: the differences above, and the textual agreement of both files on the factor (read by hand, not coded).
Tolerances are chosen from the number of printed digits, an assumption about rounding, not a measured error.

## Rerun
```
cd /home/user/z4-workers/i1-sec/child/grandchild && rm -f results.txt && python3 check.py
```
