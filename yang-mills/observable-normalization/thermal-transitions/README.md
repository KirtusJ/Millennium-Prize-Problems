# Resolving transition frequencies in a periodic Wilson correlator

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Can the matched measurements distinguish two distinct **nonzero** energy differences? A constant thermal contribution survives subtraction of the observable mean. Allowing that contribution, a six-step test on Z4's frozen ensembles gives a determinant compatible with zero at all three spacings. At the middle spacing a different determinant is positive by about 2.6 block-jackknife errors, but a single nonzero transition plus a static contribution already gives that outcome. These are exploratory tests on existing data. [Z4 measurement and definitions](../../z4/fixed-size/MATCHED_MEASUREMENT.md) · [Frozen input files](../../z4/reviews/ext-match/predeclared/)

## A positive moment problem at any interior time

Take a positive injective transfer matrix with finite thermal trace at circumference $N$ and a bounded self-adjoint slice reading. Subtract its thermal mean times the identity to get $B$. In lattice units write the transfer eigenvalues as $e^{-E_i}$. The two-point function is
$$
 C(t)=Z^{-1}\sum_{ij}e^{-(N-t)E_i-tE_j}|B_{ij}|^2,\qquad 0\le t\le N.
$$
A constant positive normalization of $C$ is allowed. At fixed $t$ assign each summand's weight to $x_{ij}=2\cosh(E_i-E_j)-2$. This defines a finite positive measure $\mu_t$ on $[0,\infty)$. The mass at zero includes diagonal fluctuations and any transitions within an energy eigenspace. Subtraction of a single mean leaves those fluctuations in general.

Apply the central second difference $D C(t)=C(t+1)-2C(t)+C(t-1)$. Every exponential term acquires the factor $x_{ij}$, with the same factor for the reversed ordering. Thus for $j\le\min(t,N-t)$ one has
$$
 m_j(t)=D^j C(t)
 =\sum_{k=-j}^{j}(-1)^{j-k}\binom{2j}{j+k}C(t+k)
 =\int x^j\,d\mu_t.
$$
The restriction on the stencil matters. Periodically wrapping a difference *beyond* an endpoint generally invalidates this identity. The endpoint $C(N)=C(0)$ itself is valid. Finiteness follows termwise since the expanded stencil uses only finitely many finite thermal traces. The location of the support encodes absolute thermal energy differences. Transitions between two excited states also contribute.

For $s\ge0$, the matrix $(m_{s+i+j})_{i,j=0}^{k}$ is the Gram matrix of $1,x,\ldots,x^k$ for $x^s\mu_t$, whenever the required lags exist. Its rank equals the lesser of $k+1$ and the number of distinct support points of that weighted measure. Indeed, a null vector is precisely a polynomial of degree at most $k$ vanishing on the support. In particular, with $H_s=m_s m_{s+2}-m_{s+1}^2$,
$$
 H_s=\tfrac12\iint (xy)^s(x-y)^2\,d\mu_t(x)\,d\mu_t(y).
$$
For $s=0$ the factor is one even at zero. For $s=1$, $H_1>0$ holds exactly when at least two distinct nonzero absolute transition frequencies are present. A single nonzero frequency together with stationary weight gives $H_0>0$ and $H_1=0$. Finite thermal time and the backward exponential are included in both tests. Neither positivity test identifies the vacuum mass.

## Reanalysis of the frozen rows

Use Z4's dimensionless connected ratio $R(t)$ as $C(t)$. Compute $H_0$ at $t=2$ using lags zero through four and $H_1$ at $t=3$ using lags zero through six. Recompute the mean, its square in the denominator, every lag, and the determinant in each deletion. The table gives jackknife bias-corrected estimates and one estimated standard error, in units of $10^{-5}$.

| Side | Configurations per block | Whole blocks | $H_0(2)$ | $H_1(3)$ |
|---:|---:|---:|---:|---:|
| 6 | 11 | 271 | 2.71 ± 1.38 | 4.88 ± 5.12 |
| 6 | 22 | 135 | 2.72 ± 1.41 | 4.88 ± 5.24 |
| 8 | 17 | 87 | 4.32 ± 1.65 | 0.97 ± 2.54 |
| 8 | 34 | 43 | 4.32 ± 1.61 | 0.81 ± 2.61 |
| 12 | 25 | 32 | 1.85 ± 1.33 | −0.46 ± 1.13 |
| 12 | 50 | 15 | 1.35 ± 1.28 | −0.94 ± 0.97 |

We retain each configuration ID once per seed, skip its first ten configurations and use the final flow-time slice array. Blocks stay within a single seed. Each seed's incomplete final block is dropped. The base lengths for the coarse and middle ensembles match Z4's analysis. For the fine lattice the largest of Z4's seed-specific block lengths is used (25), followed by a doubled-length sensitivity check at each spacing. These are correlated sensitivity checks on the same configurations. The errors assume that the retained blocks give an adequate account of serial dependence. The six-step stencil subtracts several noisy quantities. Even the positive population identity allows negative sample estimates.

## Fine-ensemble restart correction

B4 identified repeated observations in the restarted fine chains. Configuration IDs 40, 41 and 42 appear twice in **each** of seeds 1206 and 1207. The plaquette and every stored flow-time slice reading coincide within each repeat. Seed 1205 and the coarse and middle files have no repeated IDs. After the ten-configuration exclusions, the frozen files therefore contain 840 fine rows representing 834 distinct seed–ID pairs (260, 287 and 287). The table above uses the latter sample. The [reader](matched_rows.py) rejects conflicting repeats and gaps among distinct IDs.

A second selection restores IDs 297–299 from each of the two longer snapshots. Their frozen prefixes match exactly. The resulting 840 distinct configurations give the same whole-block estimates as the 834-configuration selection: neither set of restored rows reaches the next full block within its seed. The 25- and 50-configuration calculations use 800 and 750 distinct configurations, respectively.

Retaining every distinct configuration gives the following direct estimates. Errors are the standard deviations of 4,000 circular moving-block bootstrap replications, drawing within each seed and restoring its original length. The direct estimates use the nonlinear statistic on the entire sample; the table above uses jackknife bias correction. All entries below are in units of $10^{-5}$.

| Fine selection | $H_0(2)$ | Bootstrap errors, blocks 25 / 50 | $H_1(3)$ | Bootstrap errors, blocks 25 / 50 |
|---|---:|---:|---:|---:|
| 834 frozen unique IDs | 1.96 | 1.13 / 1.16 | −0.77 | 1.11 / 0.92 |
| 840 declared IDs | 2.01 | 1.14 / 1.16 | −0.68 | 1.11 / 0.92 |

Neither selection resolves two nonzero transition frequencies on the fine ensemble. The circular resampling assumes approximate stationarity within each retained chain. It adds a sensitivity check on the discarded tails. Both scripts default to `--sample frozen-unique`; `--sample declared-ids` selects the restored IDs and `--sample historical-rows` reproduces the earlier repeated-row calculation. [Effect on the opposite-slice purity diagnostic](../replica-gap/thermal-allowance/README.md)

The [analysis script](check.py) uses only the committed measurements and NumPy. Run it from any directory with Python. It also checks all required stencils in rational arithmetic against periodic one- and two-frequency signals with a stationary term. Three PCP OS guests emitted the [Lean source](ThermalTransitions.lean) from [worker.c](worker.c). A fresh [guest replay](../transfer-increments/replay-guests.py) reproduced SHA-256 `71290ee429d095639479a3e83375d1860720b2da3bb4b974363c321b0b5687a4`. Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked five supporting algebraic identities and inequalities using standard axioms. The thermal trace, general rank argument and statistical interpretation are given above.
