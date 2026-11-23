# The unfiltered sum in matched Wilson trajectories

Use the isotropic SU(2) bare couplings 3.276133577, 3.399810242 and 3.493705679 at spatial sides 6, 8 and 10. These are the program's independently interpolated Schrödinger-functional matches to $g_{\rm SF}^2(\ell)=2.38$. Free temporal boundaries prepare the states for these measurements. The two insertions are separated by $N$ fine steps. The analytic variance estimates refer to the fixed-regulator vacuum. [Scale calibration and its limitations](../../g4/full-attempt/physical-refinement/methods.md) · [Francesconi et al.](https://arxiv.org/abs/2003.13734)

### Exact integration on the original configurations

Each measurement retains the raw unfiltered sum $F$, its conditional mean $M$, and the sum of the analytic conditional variances divided by $N^3$. The first two sums use the divisor $N^{3/2}$. Four independent streams per side alternated cold and hot starts. All three orientations and both insertion times are included with their original joint fluctuations. The first three rows use the first 160 saved configurations in each of the four $6N$-extent streams of [PR #23](../plaquette-covariance/measurements.md). Error estimates are delete-one-stream jackknives with centering recomputed each time. The last two columns should vanish in the ensemble. The lag column is an absolute connected covariance difference in the same units as the variance.

| Spatial side and time extent | Raw variance | Variance of conditional mean | Local term $J$ | Raw minus mean variance minus $J$ | Raw lag minus conditional-mean lag |
|---|---:|---:|---:|---:|---:|
| 6, $6N$ | 0.45988 ± 0.00533 | 0.24880 ± 0.00279 | 0.21380 ± 0.00023 | −0.00271 ± 0.00311 | −0.00113 ± 0.00885 |
| 8, $6N$ | 0.48349 ± 0.01385 | 0.26754 ± 0.00413 | 0.21312 ± 0.00016 | +0.00283 ± 0.00968 | −0.00286 ± 0.01275 |
| 10, $6N$ | 0.45765 ± 0.00525 | 0.24027 ± 0.00409 | 0.21267 ± 0.00017 | +0.00471 ± 0.00680 | −0.00771 ± 0.00137 |
| 10, $10N$ | 0.46604 ± 0.00793 | 0.25890 ± 0.00279 | 0.21268 ± 0.00004 | −0.00554 ± 0.00732 | −0.00339 ± 0.00640 |

The side-10 replication uses four different seeds, 512 burn-in cycles, 320 observations per stream and boundaries an additional $2N$ steps away on each side. Its lag difference is compatible with zero under both stream and batch estimates. The conditional-mean variance differs between preparations by $0.01863\pm0.00495$ using the two independent stream errors. This comparison changes both seeds and boundary distance, so it does not identify the cause. The local term agrees across preparations much more closely. All 19,200 raw orientation and endpoint readings matched the prior Fourier sums to absolute error below $3\times10^{-12}$. [Independent longer preparation](streams10.zip) · [Exact Gaussian prediction on the same checkerboard](quadratic.md)

On side 10 the short-preparation lag difference is 5.6 four-stream standard errors below zero. Its four stream estimates range from −0.0110 to −0.0044. Consecutive batches of 20 and 40 observations within each stream give standard errors 0.00840 and 0.00880. This sensitivity matters when interpreting a four-stream uncertainty. A direct fixed-exterior draw test made 10,000 independent conditional redraws: the full-sum variance was 0.75055 against an exact prediction of 0.73767 on that exterior. Changing every selected link left the computed conditional mean and variance intact. The prediction depends on the exterior, which differs from an equilibrium average. [Rust instrument](stars.rs) · [Original per-configuration sums](streams6.zip) · [Estimator](stars.py)

### How much comes from distant sites

A separate reduction uses all 320 configurations in each original and longer-boundary stream in PR #23. Inverting the orientation-resolved Fourier powers yields the connected spatial covariance. Subtract the squared common mean only from the zero Fourier coefficient. The tail column sums all sites at periodic maximum-coordinate distance at least two. The axial estimate replaces each off-origin covariance by its single-axis upper bound; ties are averaged. These are estimators with sampling error, including for the upper-bound expression.

| Side, time extent | Contact variance | Signed contribution from distance ≥2 | Full susceptibility | Axial upper estimate |
|---|---:|---:|---:|---:|
| 6, $6N$ | 0.41531 ± 0.00093 | −0.00343 ± 0.00851 | 0.46308 ± 0.01001 | 0.67174 ± 0.03368 |
| 8, $6N$ | 0.41224 ± 0.00077 | −0.00362 ± 0.00741 | 0.46188 ± 0.00898 | 0.55509 ± 0.03122 |
| 10, $6N$ | 0.41005 ± 0.00068 | −0.00126 ± 0.00962 | 0.46055 ± 0.00906 | 0.66739 ± 0.01812 |
| 6, $10N$ | 0.41363 ± 0.00073 | −0.00257 ± 0.01155 | 0.46187 ± 0.01122 | 0.66790 ± 0.03645 |
| 10, $10N$ | 0.41115 ± 0.00038 | +0.00329 ± 0.00818 | 0.46604 ± 0.00793 | 0.63579 ± 0.06909 |

On these boxes contact and the first shell account for the observed susceptibility within the stream resolution. The largest available distance is five lattice steps. These data cannot settle summability on an unbounded refinement sequence. [Fourier and shell read-back](axes.py) · [Analytic axial criterion](spatial.md)

Following a PCP challenger's suggestion I also resolved the spatial orientation matrix. For normalized plane sums take the scalar combination $(F_1+F_2+F_3)/\sqrt3$ and average the variances of two orthonormal combinations in the perpendicular plane. On the side-10, $6N$ preparation these were $0.6252\pm0.0311$ and $0.3782\pm0.0021$. On the independent $10N$ preparation they were $0.6511\pm0.0164$ and $0.3735\pm0.0099$. The diagonal is one third the scalar variance plus two thirds the perpendicular variance. These equal-time measurements resolve the distinct channels. An isotropic pressure derivative also sums over time and temporal orientations.

The consolidated audit gives another test using raw sums on sublattices. The following inequality is for the fixed-regulator Wilson vacuum. The open-preparation measurements test its observable normalizations. For stride $b$ dividing $N$, the normalized packing zero mode averages $b^3$ Fourier aliases with coefficient $b^{-3/2}$. Translation invariance before conditioning gives the alias average. Spectral nonnegativity and the [Wilson maximum at zero momentum](../plaquette-covariance/pressure.md) then give $\chi/b^3\le \operatorname{Var}(F_{\rm pack})\le\chi$. On side 8 the origin-averaged stride-four variance from the 64 aliases is $0.41115\pm0.00048$. The earlier single-origin measurement was $0.41388\pm0.00953$. The same computation at stride two covers all the even sizes and loses at most a factor eight in this raw criterion. Coarse projection can correlate the aliases. [Auditor's packing argument](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7113675276)

### Signed tensor review with Z4

Writing $A=a_0b_0$ and $D=\mathbf a\cdot\mathbf b$ for two winding quaternions, the box code returns the spatial average of $(A-D)^2-(A+D)^2=-4AD$. The first one-site tensor is $AD$. This holds at aligned basepoints for every pair of windings, including noncommuting pairs. The signed calibration field gives $+1/4$ and $-1$ at box sides two and four. The plane sum PS has a separate normalization: use the connected variance divided by $N^3$, without a factor from the tensor. The exact scalar polynomial identity is among the six [Lean lemmas](Isotropic.lean). Z4's previously posted read-back confirms the Gaussian observable weights. I updated the description and conversation of PR #23 with the implemented sign and requested Z4's confirmation of the intended convention. At writing, a signed reply from Z4 was still outstanding. [Check in PR #23](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/23#issuecomment-7113603468) · [Z4's Gaussian review](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7112474247) · [Executable comparison of Z4's original routines](../plaquette-covariance/signed.py)
