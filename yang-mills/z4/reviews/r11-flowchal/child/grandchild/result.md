# Periodic Green function check, N=16

m^2=2-2cos(pi/8)=0.152240934977427, w=0.387747037420558

Derivation: denominator = 2cosh w - 2cos k; infinite-line G=e^{-w|n|}/(2 sinh w); periodic sum over images sum_j e^{-w|n+16j|}/(2 sinh w) = cosh(w(8-|n|))/(2 sinh w sinh 8w) for |n|<=16.

| n | direct | closed | abs diff |
|---|---|---|---|
| 0 | 1.262841355540333 | 1.262841355540334 | 2.22e-16 |
| 1 | 0.8589694298881441 | 0.8589694298881443 | 2.22e-16 |
| 2 | 0.5858678133591527 | 0.5858678133591531 | 3.33e-16 |
| 3 | 0.4019592605091389 | 0.4019592605091396 | 6.66e-16 |
| 4 | 0.2792453613018722 | 0.2792453613018727 | 5.55e-16 |

max abs diff = 6.66e-16
Tolerance 1e-13: float64 eps ~2.2e-16, values O(0.5-1), 16-term sums plus cosh/sinh rounding give errors of a few eps; 1e-13 is a safe margin. Control sum was -9.0e-16, consistent.
Result: PASS
