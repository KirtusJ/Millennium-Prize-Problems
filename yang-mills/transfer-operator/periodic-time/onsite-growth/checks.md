# Checks for the two-mass on-site scalar

The numerical test uses two independent finite-dimensional formulas. Gaussian determinants and subset inclusion-exclusion evaluate the product of centered exponentials. A permutation sum enumerates the Wick pairings without within-site contractions, counting the three color choices independently on each cycle. With coupling 0.4, one-site variance 1.1 and distinct positive off-diagonal weights, the determinant approaches the Wick-square coefficient with the predicted sign at every order tested. The calculation used 85 decimal digits, first at covariance multipliers 0.01 and 0.001 and then at 0.0001. [Numerical implementation](check.py)

| Sites | Predicted leading coefficient | Relative discrepancy at 0.0001 |
|---|---:|---:|
| 2 | 0.006540364753 | 3.62 × 10⁻¹⁰ |
| 3 | −0.0006610320366 | 6.24 × 10⁻⁵ |
| 4 | 0.0001787737605 | 8.29 × 10⁻⁵ |
| 5 | −0.00004245845888 | 1.51 × 10⁻⁴ |
| 6 | 0.00001262176619 | 2.15 × 10⁻⁴ |

The PCP OS host relay honored two successive guest requests and ran three freestanding programs in separate boots. The parent enumerated the derivative choices on three vertices, including the minimum and maximum number of edges. The child tested the endpoint bound on graphs with nonuniform powers-of-two weights. The grandchild enumerated labeled pairings at orders 2 through 6, including their closed color cycles, and checked them against the independent centered chi-square moment recurrence. All three guests completed with exit code 0, 47 register events apiece and a byte-identical expected check record. These finite tests exercise the interpolation and Wick combinatorics. The uniform bounds and the continuum limit use the proof. [Worker](worker.c) · [Expected records](checks.txt) · [Host relay](../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Register head in this deployment |
|---|---|---|
| Parent | 78e7dcd9217562aabdca3c664a2273523ca57f104cd7781ff5aab1667adcbf8b | 59314e698f7b780e63a93b67268021bb0fd125799d306d19e63e6ea7b08e2800 |
| Child | c8ce8e1aead7bef34f54f31ec9e2086d745e59dee896dc5e50067342c3d6ef1a | 680588901e1a2727b011d860f669632f486e49ed92f3870496fbd51853181677 |
| Grandchild | e2cd0b78bb85eaf643931d4e66243ff021b8863df7df779cd1c607610c6dc463 | 676b85eb6205dd836c7559a693362aba34b0ea03acbd6c5c237f04dd2dfba3c0 |

The kernel file digest was d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f. The generated record digest was daf3bd38fe5d812498e25202dc776210b1bdc67f263516d2505bb8e1d1d5f10b. Both are SHA-256. From this directory, with mpmath, gcc, QEMU and the measured kernel available, run the following commands.

```sh
python check.py
python ../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```
