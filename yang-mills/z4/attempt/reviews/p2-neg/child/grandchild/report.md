# Recompute of the extension table (MATCHED_MEASUREMENT.md)

Control: 1/(3.74*0.25) = 1.0695 (control.txt). Program: recompute.py; output: results.txt.
Inputs: a*sqrt(sigma) = 0.3690, 0.2660, 0.1905; R(0) = 3.751, 3.615, 3.233 (e-2); R(1 step) = 1.012, 1.166, 1.245 (e-2).

| N | q (unrounded) | writer | xi (unrounded) | writer | xi(1-q) (unrounded) | writer |
|---|---|---|---|---|---|---|
| 6 | 0.269795 | 0.270 match | 0.724606 | 0.72 match | 0.529111 | 0.53 match |
| 8 | 0.322545 | 0.323 match | 1.005187 | 1.01 match | 0.680969 | 0.68 match |
| 12 | 0.385091 | 0.385 match | 1.403568 | 1.40 match | 0.863066 | 0.86 match |

All 9 values match at the printed digits. Note: this checks arithmetic only, from the table's central values, not the measurements.
