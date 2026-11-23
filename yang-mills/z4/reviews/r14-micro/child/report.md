# Report

Control: control.txt = 3.25

| item | claimed | computed | verdict |
|---|---|---|---|
| A1 6*0.3690 | 2.214 | 2.214 | MATCH |
| A1 12*0.1905 | 2.286 | 2.286 | MATCH |
| A2 mismatch % | 3.25 | 3.2520325 | MATCH |
| A2 error % | 0.94 | 0.94481992 | MATCH |
| A3 a^2/(8s), s/a^2=0.5 | 0.25 | 0.25 | MATCH |
| A3 sqrt(8s)/a, s/a^2=0.5 | 2 | 2 | MATCH |
| A3 a^2/(8s), s/a^2=2.0 | 0.0625 | 0.0625 | MATCH |
| A3 sqrt(8s)/a, s/a^2=2.0 | 4 | 4 | MATCH |
| A4 sqrt(6s)/l | 0.29 | 0.28867513 | MATCH |
| A4 s/a^2 l=6a | 0.5 | 0.5 | MATCH |
| A4 s/a^2 l=12a | 2.0 | 2 | MATCH |
| A5 R(0) value | 0.913 | 0.91175686 | MISMATCH |
| A5 R(0) error | 0.033 | 0.0335809 | MISMATCH |
| A5 R(l/6) value | 0.494 | 0.49407115 | MATCH |
| A5 R(l/6) error | 0.067 | 0.067062509 | MATCH |
| A5 Q0 value | 0.956 | 0.95661489 | MISMATCH |
| A5 Q0 error | 0.012 | 0.012081076 | MATCH |
| A6 Q0 percent diff | 4.4 | 4.338511 | MISMATCH |
| A6 Q0 nse via ratio | 3.6 | 3.5911629 | MATCH |
| A6 Q0 nse via direct diff | 3.6 | 3.5830888 | MATCH |
| A6 R(0) percent diff | 9 | 8.8243135 | MATCH |
| A6 R(0) nse via ratio | 2.7 | 2.6277776 | MISMATCH |
| A6 R(0) nse via direct diff | 2.7 | 2.603476 | MISMATCH |
| A6 R(l/6) factor | 2 | 2.024 | MATCH |
| A6 R(l/6) nse via ratio | 7.6 | 7.5441385 | MISMATCH |
| A6 R(l/6) nse via direct diff | 7.6 | 6.9803761 | MISMATCH |
| A7 (2.214/2.286)^3 | 0.91 | 0.90845657 | MATCH |
| A8 3.751/0.042 | 88 | 89.309524 | MISMATCH |
| A8 1.012/0.032 | 31 | 31.625 | MISMATCH |
| A8 3.65/0.34 | 11 | 10.735294 | MATCH |
| A9 |x|/err <2 (claimed inside 2se -> 1 true) | 1 | 1 | MATCH |
| A10 1-I2/I1 (0.5) | 0.876282 | 0.87628207 | MATCH |
| A12 | 0.0002806 | 0.00028060488 | MATCH |
| A13 m/0.3690 | 3.01 | 3.0108791 | MATCH |
| A14 points 0..50 | 1001 | 1001 | MATCH |
| A15 configs/block | None | 20 | (no claim; value reported) |
| A6 Q0 nse combined (P3) | | | MATCH |
| A6 R(0) nse combined (P3) | | | MISMATCH |
| A6 R(l/6) nse combined (P3) | | | MISMATCH |
| A9 2.0/1.1 | inside 2 se | 1.8182 se | MATCH |
| A10 (0.875486-0.876282)/0.000760 | - | -1.047 se | (no claim) |
| A11 0.602953(159) vs 0.602934(37) | - | 0.116 se | (no claim) |
| A11 0.652029(160) vs 0.651941(198) | - | 0.346 se | (no claim) |
| A13 m (lattice units), closed form / bisection | - | 1.1110143957 / 1.1110143957 | agree 1e-9 |
| A14 points 3.50..50 | - | 931 | (no claim) |

## Group counts (P5)

- A1: 2/2 rows MATCH
- A2: 2/2 rows MATCH
- A3: 4/4 rows MATCH
- A4: 3/3 rows MATCH
- A5: 3/6 rows MATCH
- A6: 4/9 rows MATCH
- A7: 1/1 rows MATCH
- A8: 1/3 rows MATCH
- A9: 1/1 rows MATCH
- A10: 1/1 rows MATCH
- A12: 1/1 rows MATCH
- A13: 1/1 rows MATCH
- A14: 1/1 rows MATCH
