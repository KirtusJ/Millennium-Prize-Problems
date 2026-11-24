# What survived a factor of two in resolution

The independently measured coupling stays within 1.3 quoted standard errors of 2.38 at all five lattice spacings. A neutral winding reading still has a positive finite-time decay slope at the same physical separation after halving the lattice spacing. Its normalized bare correlation loses much of its amplitude. Spatial smearing recovers signal in both winding channels. The contractible tensor data and the all-state lower-bound test do not establish a positive physical spectral gap.

### Scale and winding signal

Let $R(t)=C(t\ell)/C(0)$. The slope is $2\log[C(\ell/2)/C(\ell)]$, in units of $1/\ell$ when interpreted as a rate. For $N=5,7$ the half-time correlation is the arithmetic mean at $(N-1)/2$ and $(N+1)/2$ time steps, before taking the logarithm. At $t=1$ all five meshes have an exact time slice. The source and sink are at least $\ell$ from either end of a $6\ell$ slab. Each entry shows the estimate and one reblocking/stream standard error. The Dirichlet scale check uses separate gauge configurations. [Definitions and sampling](methods.md)

| $N$ | Independent $g_{\rm SF}^2$ | Bare $E^+$, $R(1)$ | Bare $E^+$ slope | Smoothed $E^+$ slope | Smoothed $T_2^+$ slope |
| --- | --- | --- | --- | --- | --- |
| 5 | 2.397 ± 0.028 | 0.118 ± 0.009 | 1.57 ± 0.11 | 1.44 ± 0.18 | 2.17 ± 0.32 |
| 6 | 2.409 ± 0.029 | 0.094 ± 0.011 | 1.58 ± 0.18 | 1.19 ± 0.13 | 2.75 ± 1.43 |
| 7 | 2.338 ± 0.033 | 0.064 ± 0.006 | 1.67 ± 0.18 | 1.57 ± 0.31 | 2.61 ± 0.56 |
| 8 | 2.388 ± 0.038 | 0.050 ± 0.006 | 1.28 ± 0.21 | 1.98 ± 0.28 | 2.45 ± 0.74 |
| 10 | 2.343 ± 0.039 | 0.020 ± 0.005 | 1.15 ± 0.46 | 1.54 ± 0.36 | 1.87 ± 0.43 |

The first short SF run gave 2.266 ± 0.049 at $N=5$. Two fresh, longer hot/cold streams give the entry above. Both runs are retained. The nearest tabulated input, not any spectroscopic energy, sets the interpolation. [Original calibration](https://arxiv.org/pdf/2003.13734#page=12)

### Which probes retain a signal?

All entries here use $R(1)$. The last column is the within-trajectory difference between smoothed and bare winding ratios using the same two streams and 192 configurations per stream. Comparing the full bare sample with the smoothed subset would give a different error.

| $N$ | Bare $T_2^+$ winding | Smoothed $T_2^+$ winding | Smoothed $E^+$ clover | Smoothed $T_2^+$ clover | Paired gain, $E^+$ winding |
| --- | --- | --- | --- | --- | --- |
| 5 | 0.011 ± 0.004 | 0.073 ± 0.020 | 0.045 ± 0.016 | -0.001 ± 0.012 | 0.085 ± 0.015 |
| 6 | -0.002 ± 0.004 | 0.052 ± 0.035 | 0.041 ± 0.008 | -0.001 ± 0.006 | 0.142 ± 0.012 |
| 7 | 0.002 ± 0.004 | 0.053 ± 0.017 | 0.024 ± 0.013 | 0.008 ± 0.007 | 0.142 ± 0.041 |
| 8 | 0.002 ± 0.005 | 0.061 ± 0.023 | 0.005 ± 0.018 | -0.003 ± 0.005 | 0.105 ± 0.023 |
| 10 | 0.001 ± 0.003 | 0.085 ± 0.023 | 0.023 ± 0.010 | 0.007 ± 0.007 | 0.174 ± 0.044 |

For the unsmeared $E^+$ winding reading, the equal-time variance changes from 0.02028 ± 0.00023 at $N=5$ to 0.00257 ± 0.00001 at $N=10$. With spatial smearing the corresponding estimates are 0.1367 ± 0.0043 and 0.1358 ± 0.0039. Variance and normalized propagation both matter when identifying a disappearing signal. The smoothed clover $T_2^+$ ratio remains within two errors of zero at every size. Several bare clover log slopes have nonpositive inputs. They are retained as undefined in the full table. No tensor reading here establishes a uniform minimum weight on the slowest state. [Reading definitions](methods.md) · [Full reductions and raw observations](checks.md)

### Time boundaries and extrapolation

| $N$ | Production, margin $\ell$ | Production, margin $2\ell$ | Long slab, margin $\ell$ | Long slab, margin $2\ell$ |
| --- | --- | --- | --- | --- |
| 5 | 1.57 ± 0.11 | 1.68 ± 0.19 | 1.65 ± 0.17 | 1.67 ± 0.25 |
| 10 | 1.15 ± 0.46 | 0.80 ± 0.60 | 1.06 ± 0.46 | 1.19 ± 0.55 |

At $N=10$ the pooled bare slope on the later window from $\ell$ to $1.5\ell$ is 1.92 ± 1.36. The earlier-window estimates from the hot and cold production starts at that resolution are 1.35 ± 0.67 and 0.95 ± 0.68. Repetition at two slab lengths cannot bound the error relative to the vacuum. A4's fixed-exterior numerator and B4's fidelity measurement would supply information absent from this ensemble. [A4’s denominator control](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7110080647) · [B4’s fidelity requirement](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7110123235)

The following fits use all five bare $E^+$ slopes from $\ell/2$ to $\ell$ and diagonal weights from their statistical errors. The first two fit one amplitude. The last two report the intercept of a two-parameter fit. The bare-power shape tests the naive substitution of $g_0$ into the fixed-box small-volume law, which changes by only about 3% over these endpoints. A renormalized, matched-scale prediction needs the chosen channel and scheme. Finite data do not distinguish these shapes or establish a continuum vacuum mass. The fit errors condition on the calibration and form of each fit. [Fit calculation](fits.py) · [Lüscher’s periodic small-volume analysis](https://doi.org/10.1016/0550-3213(83)90436-4)

| Trial dependence | Amplitude or intercept | Weighted $\chi^2$ | Degrees of freedom |
| --- | --- | --- | --- |
| Constant | 1.54 ± 0.08 | 2.94 | 4 |
| Bare $(\beta/\beta_5)^{-1/3}$ | 1.55 ± 0.08 | 2.65 | 4 |
| $A+B/N$ | 1.17 ± 0.43 | 2.19 | 3 |
| $A+B/N^2$ | 1.36 ± 0.24 | 2.33 | 3 |

### Collective scalar trials

For a contractible scalar square of target side $\ell/4$, the last three columns show $C(\ell/4,p)/C(0,p)$. The first nonzero momentum has $|p|=2\pi/\ell$ at all spacings. The absolute variance uses the $N^{-3}$ Fourier average. Contact profiles, all retained lags and the corresponding one-cell readings are in the archive.

| $N$ | First-shell equal-time variance | Zero momentum | First axial shell | Second axial shell |
| --- | --- | --- | --- | --- |
| 5 | 0.000122 ± 1e-06 | 0.053 ± 0.011 | 0.039 ± 0.008 | 0.026 ± 0.005 |
| 7 | 0.000119 ± 6.1e-07 | 0.024 ± 0.010 | 0.019 ± 0.004 | 0.012 ± 0.006 |
| 10 | 7.47e-05 ± 4e-07 | 0.003 ± 0.007 | 0.005 ± 0.002 | 0.008 ± 0.003 |

The measured first-shell state has nonzero equal-time variance on each sampled mesh. None of the three retained shells exhibits a correlation ratio approaching one at this fixed physical lag. A true vacuum variational bound needs vacuum preparation. A test for collective softening as physical volume increases also needs a sequence with $|p|\to0$. The exact electric and Maxwell trials give controls for these two distinct limits. [Collective trial and normalization](collective.md)

### Disposition

The actual isotropic lower bound is already below the resolving power of spectroscopy. Its simpler certified floor $N/U_N$ decreases from about $10^{-393}$ to $10^{-3507}$ over this refinement. A4 independently derived an upper bound on the stronger lower-bound expression which also tends to zero. The remaining proof obligation is a uniform upper bound strictly below one on the neutral transfer at physical time $\ell$, including the states newly introduced at each refinement and their mixing with coarse states. The electric counterexample shows why successful matching and a visible fixed-scale excitation alone cannot supply it. Infinite physical volume and the construction and identification of the continuum theory are further obligations. [Isotropic inequality](isotropic.md) · [A4’s independent check](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7110102562) · [Exact control](electric.md)
