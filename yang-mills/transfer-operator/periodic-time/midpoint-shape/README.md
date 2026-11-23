# Which transition shapes fit the periodic plaquette data?

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The fine lattice shows a departure from a single periodic transition frequency when the equal-time reading and the correlations between lag estimates are included. Removing the equal-time reading admits a single frequency again. A positive two-frequency profile fits the full data, as does a model with a single finite frequency and an equal-time contact term. The measurement therefore does not resolve two finite frequencies at positive separation. The coarse and middle lattices admit a single frequency even with equal time included. Synthetic single-frequency trials showed that the nominal confidence regions miss too often at these sample sizes. The departure is a property of the fitted empirical region, with no calibrated Wilson rejection probability. [Configuration audit](../../findings-audit/) · [A4’s thermal determinant measurement](../../../observable-normalization/thermal-transitions/)

## What midpoint subtraction measures

On a periodic lattice of temporal extent $2n$, a positive transfer matrix and a self-adjoint slice observable give a connected thermal correlator of the form
$$
 C(t)=A+\int_{0<z<1}(z^t+z^{2n-t})\,db(z).
$$
Here $z=\exp(-|E_i-E_j|)$ in lattice units. Pairing the two orders of each unequal-energy matrix element gives the positive measure $b$. The time-independent variance and equal-energy transitions give $A\ge0$. Excited-to-excited pairs contribute. Midpoint subtraction has also been used to remove constant contributions in finite-temperature meson spectroscopy. [Thermal trace derivation](../../../observable-normalization/thermal-transitions/) · [Umeda, *Physical Review D* 75, 094502](https://arxiv.org/abs/hep-lat/0701005)

Write $D=C(0)-C(n)>0$ and $q_t=(C(t)-C(n))/D$. With $S_j(z)=1+\cdots+z^{j-1}$, the exact shape for one factor and the general mixture are
$$
 K_t(z)=z^t\left(\frac{S_{n-t}(z)}{S_n(z)}\right)^2,
 \qquad q_t=\int K_t(z)\,d\pi(z),\qquad
 d\pi(z)=\frac{(1-z^n)^2}{D}\,db(z).
$$
Thus a probability under $\pi$ is a share of the **midpoint-subtracted equal-time signal**. A small difference frequency can carry appreciable thermal weight and little weight under $\pi$. For $0<t<n$, $K_t$ increases from zero to $M_t=((n-t)/n)^2$. To see strict monotonicity, put $u=-\log(z)/2$. The square root is $\sinh((n-t)u)/\sinh(nu)$. Its logarithmic derivative is negative because $v\coth v$ is strictly increasing for $v>0$ (use $\sinh(2v)>2v$).

This gives two direct uses of simultaneous bands $[l_t,h_t]$. A single factor must satisfy every $l_t\le K_t(z)\le h_t$. For any mixture and any $0<c<1$, its slow fraction $p_c=\pi([c,1])$ satisfies
$$
 \max_t\frac{l_t-K_t(c)}{M_t-K_t(c)}\le p_c
 \le\min_t\frac{h_t}{K_t(c)}.
$$
Intersect these bounds with $[0,1]$. They follow by bounding the kernel separately on the two sides of $c$. Neither inference identifies a vacuum energy.

## How the uncertainty was estimated

For each periodic data row $x$ define $L_t=\tfrac12\operatorname{mean}_s(x_s-x_{s+t})^2$. The denominator is the mean of $L_n$ across configurations. The numerator at lag $t$ is the mean of $L_n-L_t$. This cancels the connected subtraction and its normalization exactly, including an arbitrary constant added to each row. All lags and their denominator are resampled together. The data are the unique configurations after the initial exclusions. The second fine selection restores IDs 297–299 in each restarted seed. [Shared data reader and circular-block resampler](../../../observable-normalization/thermal-transitions/matched_rows.py)

We used 16,000 circular moving-block draws within seeds, retaining each seed’s observed length. The rectangular region uses the empirical quantile of the largest absolute standardized coordinate displacement. A second, covariance-sensitive region uses the same draws and the empirical quantile of the squared Mahalanobis displacement about the measured vector, holding its estimated precision matrix fixed. For each region and fixed analysis choice, the per-lattice quantile is $1-0.05/3$ to allow comparison across three lattices. Neither a Gaussian reference distribution nor independence between lags is assumed. These are approximate, post-hoc regions. Block lengths, selections and the two region constructions are sensitivity comparisons on the same data. [Bruno and Sommer on correlated lattice fits](https://arxiv.org/abs/2209.14188) · [Christ, Eranki and Kelly on bootstrap calibration](https://arxiv.org/abs/2409.11379)

| Lattice and selection | Block lengths | Single-factor interval from the rectangle, first / second block length | Minimum squared distance in the ellipsoid, first / second | Squared radii, first / second |
|---|---|---|---:|---:|
| 6, frozen | 11 / 22 | [0.216, 0.283] / [0.216, 0.283] | 0.82 / 0.84 | 8.28 / 8.15 |
| 8, frozen | 17 / 34 | [0.253, 0.334] / [0.255, 0.335] | 4.11 / 4.25 | 10.03 / 10.17 |
| 12, 834 frozen distinct | 25 / 50 | [0.420, 0.440] / [0.417, 0.441] | 37.40 / 51.54 | 13.86 / 13.68 |
| 12, 840 declared IDs | 25 / 50 | [0.428, 0.445] / [0.427, 0.444] | 37.81 / 51.58 | 13.90 / 13.84 |

The fine rectangle admits a single factor. The fine ellipsoid excludes it in all four comparisons. Two projections explain the difference. Across all four ellipsoids, $q_3>0.048$ and $q_1-q_2<0.23$. For $z\le3/8$, monotonicity gives $K_3(z)\le K_3(3/8)=0.04758348\ldots$. For $z\ge3/8$, $K_1(z)-K_2(z)>0.23$. The latter follows by substituting $z=(3+8v)/(8+8v)$ in $100(zS_5^2-z^2S_4^2)-23S_6^2$ and clearing the denominator. All eleven coefficients are positive, including the coefficient that gives the endpoint at $z=1$. The two projections were selected after examining the ellipsoid and are contained in its simultaneous bound for all linear projections. The full inversion also isolates every real root of the cleared polynomial over $[0,1]$ using the exact rational values of the computed floating-point inputs. This verifies the curve comparison for a given numerical region. Statistical coverage remains a separate question.

The rectangles also quantify slow signal without a one-factor assumption. The intervals below are rounded outward to three decimals. The cutoffs $z\ge1/3$ and $z\ge1/2$ correspond to absolute transition energies at most $\log 3$ and $\log 2$ in lattice units.

| Selection | Block | Share with $z\ge1/3$ | Share with $z\ge1/2$ |
|---|---:|---:|---:|
| 6, frozen | 11 / 22 | [0, 0.884] / [0, 0.882] | [0, 0.684] / [0, 0.682] |
| 8, frozen | 17 / 34 | [0, 1] for both | [0, 0.730] / [0, 0.732] |
| 12, frozen unique | 25 / 50 | [0.138, 1] / [0.132, 1] | [0, 0.893] / [0, 0.893] |
| 12, declared IDs | 25 / 50 | [0.152, 1] / [0.151, 1] | [0, 0.901] / [0, 0.899] |

## What drives the fine-lattice departure

* **Removing equal time.** Normalize instead by $C(1)-C(n)$ and use lags 2 through $n-1$. This replaces $(n,t)$ by $(n-1,t-1)$ in the single-factor kernel. On the 834 distinct configurations the ellipsoid admits $z$ from 0.452 to 0.589 (block 25) and 0.466 to 0.580 (block 50). Restoring the six IDs gives 0.457–0.591 and 0.468–0.587. A short-distance contribution drives the full-shape result.
* **Seed and stencil sensitivity.** Omitting each fine seed in turn gives full-shape minimum squared distances of 38.96, 20.06 and 20.49 at block 25, above the respective radii squared of 13.86, 13.67 and 13.75. Conversely, two individual adjacent-difference recurrence residuals on the full frozen sample are $0.0034\pm0.0082$ and $0.0049\pm0.0032$ at block 25. Neither scalar diagnostic resolves the departure by itself. A4’s shifted determinant likewise remains unresolved.
* **Restoring the measured midpoint.** Include $C(n)/D$, estimating its connected subtraction separately in every bootstrap draw. A factor $z$ contributes $2z^n/(1-z^n)^2$ to this last coordinate. A positive mixture with factors 0.1 and 0.5, respective $\pi$ weights 0.3 and 0.7 and zero stationary term lies inside all four augmented fine regions. Its squared distances are 8.36, 10.61, 8.98 and 11.22 in table order, below squared radii 15.61, 15.33, 16.06 and 15.45. A model with 22% equal-time contact and 78% at factor 0.5 also lies inside all four (8.71, 8.66, 8.89, 8.43). The contact profile is the $z\downarrow0$ limit. Strict inclusion allows sufficiently small positive factors as well. These are explicit feasible examples selected after inspection. The individual frequencies and their weights are not identified.

## Finite-sample calibration

A synthetic control used the fine seed lengths (260, 287, 287) and a known single factor $z=0.4$. Each Gaussian row has circular covariance proportional to $z^t+z^{12-t}$. Consecutive rows follow a stationary Gaussian AR(1) with coefficient 0.60 or 0.90. Each regime uses 256 independent simulated datasets and 3,000 bootstrap draws per dataset and block length. Both interval constructions missed the true vector more often than their nominal per-lattice rate of 1.67% (about four misses per 256). [Control program](coverage.py)

| AR coefficient | Block | Rectangles missing truth | Ellipsoids missing truth | Ellipsoids missing every grid factor | Empirical squared-radius multiplier for 98.33% truth coverage |
|---:|---:|---:|---:|---:|---:|
| 0.60 | 25 | 11 | 18 | 12 | 1.535 |
| 0.60 | 50 | 16 | 44 | 24 | 1.914 |
| 0.90 | 25 | 14 | 50 | 24 | 1.980 |
| 0.90 | 50 | 17 | 61 | 33 | 2.752 |

The grid has step 0.002 and includes the true factor. Missing the entire grid upper-bounds the frequency of missing the continuous curve. None of those trials reached the frozen Wilson minimum-distance-to-cutoff ratio (2.70 at block 25, 3.77 at block 50). Those ratios also exceed the synthetic truth-coverage multipliers. The control laws prescribe their own dependence and fluctuations. They cannot establish coverage, a false-positive rate or an adjusted critical value for Wilson data. The tabulated slow fractions likewise inherit the rectangular region’s coverage uncertainty.

## Implication for the proposed continuum test

Z4's condition (C′) concerns the infinite-volume **vacuum** quantity $\xi[1-C(1)/C(0)]$ along an unbounded sequence of correlation lengths. A pure vacuum pole at the gap already gives $\xi(1-e^{-1/\xi})$. This increases through approximately 0.54, 0.63 and 0.71 at $\xi=0.72,1,1.4$ and tends to one. A rise across these three spacings therefore has no directional force against boundedness. The observed finite-period ratios also involve thermal transitions and an external estimate for $\xi$. [Z4’s reduction and hypotheses](../../../z4/attempt/A1_REDUCTION.md) · [Attempt ledger](../../../z4/attempt/A1_LEDGER.md)

(C′) controls the initial expectation of $1-e^{-H}$, equivalently of $\min(H,1)$ up to constants. It does not by itself bound the initial mean of $H$ in units of the gap $m$. For $0<m<1$, put weights $1-m,m$ at lattice energies $m,m^{-2}$. The one-step loss is at most $2m$, whereas the mean energy is $(1-m)m+1/m$. The propagated vector in Theorem R has a different, exponentially tilted spectral measure. A two-energy calculation also refutes both directions of the proposed equivalence between failure of (C) and exponentially small initial bottom weight. [Exact criterion and counterexamples](../correlation-time.md)

## Reproduction

Run `python3 check.py` with NumPy and SymPy. Run `python3 coverage.py` with SciPy as well for the finite-sample simulation. Three measured PCP OS guests in a host-dispatched parent–child chain checked the cyclic-row identity, the two correlation-time controls and both parts of the fine one-factor exclusion. The guest driver verified all three exits and reproduced receipt text SHA-256 `83ae982763df4f7290f5eb3365873dc97b6fb3da5d000a587d776aff3c005454`. Statistical resampling and polynomial root isolation ran on the host. [Analysis](check.py) · [Guest arithmetic](worker.c) · [Expected receipts](checks.txt) · [Replay driver](../../../observable-normalization/transfer-increments/replay-guests.py)
