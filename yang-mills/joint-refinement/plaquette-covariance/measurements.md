# Plane sums, physical-time coupling and Z4’s normalization

### The matched Wilson slabs

Each observation uses the scaled energy $O=\beta(1-\operatorname{Tr}U_p/2)$. For each orientation at each endpoint let $F$ be the sum over all spatial sites divided by $N^{3/2}$ and $C$ the sum of the corresponding $2\times2$ coarse Wilson rectangle energies on the even grid, with the same divisor and bare coupling. Subtract the common mean of each observable using spatial cubic and endpoint symmetry. Fit the best scalar multiple of $C$ in this centered two-variable system and denote the residual by $r$. This is a linear predictor of the zero mode. The complete coarse conditional expectation is a different observable.

| Fine side | Raw zero-mode variance $\chi$ | Largest sampled nonzero Fourier-orbit variance | $\operatorname{Var}(r)/\chi$ | Normalized $r$ lag | Normalized $C$–$r$ lag |
|---:|---:|---:|---:|---:|---:|
| 6 | 0.4631 ± 0.0100 | 0.4617 ± 0.0015 | 0.9319 ± 0.0037 | +0.0251 ± 0.0247 | −0.0147 ± 0.0115 |
| 8 | 0.4619 ± 0.0090 | 0.4583 ± 0.0040 | 0.9276 ± 0.0075 | −0.0218 ± 0.0134 | −0.0059 ± 0.0192 |
| 10 | 0.4606 ± 0.0091 | 0.4635 ± 0.0022 | 0.9291 ± 0.0071 | +0.0230 ± 0.0114 | −0.0157 ± 0.0077 |

The lag is $N$ steps, one physical side. The last column is symmetrized between the two time assignments and divided by the product of the endpoint standard deviations. The orientation average identifies the plane normal before averaging momentum orbits under lattice symmetries. Standard errors use a paired delete-one-stream jackknife including refitting the predictor and reselecting the peak. Maximizing over noisy orbits can raise the estimated nonzero peak. For a fixed first momentum normal to the plane, its variance minus the zero mode at $N=10$ was $+0.00292\pm0.00698$. A negative estimated residual self-pairing at $N=8$ is another finite-sampling discrepancy. These data do not resolve an ordering among the lowest momenta. They measure finite open-time preparations and give no certified uniform vacuum bound. The independent analytic estimate on growing contrast families uses none of these fitted values.

Each side used four matched streams with alternating cold and hot starts, 384 discarded cycles, 320 samples three heat-bath/overrelaxation cycles apart and open extent $6N$. The two times were $5N/2$ and $7N/2$. Every scalar plaquette average at the two endpoints reproduced the earlier archived trajectory at its binary32 precision (7,680 comparisons). The archive here stores per-configuration orbit powers and signed fine and coarse zero modes. The Rust instrument regenerates the full spatial fields from the seeds. [Instrument](measure.rs) · [Reduction and error estimates](spectra.py) · [Per-configuration data](spectra6.npz) · [Matched trajectory archive](../../g4/full-attempt/physical-refinement/samples.zip)

### Moving the open time boundaries

Four independent streams at each of sides 6 and 10 used extent $10N$, a burn-in of 512 cycles and the same sample count and separation. The insertions moved to $9N/2$ and $11N/2$; their physical separation stayed fixed. The table uses the same orientation, centering, normalization and stream jackknife as above. [Longer-slab observations](spectra10.npz)

| Fine side | Raw zero-mode variance | First normal momentum minus zero | Residual variance fraction | Normalized residual lag | Normalized coarse–residual lag |
|---:|---:|---:|---:|---:|---:|
| 6 | 0.4619 ± 0.0112 | +0.0058 ± 0.0149 | 0.9312 ± 0.0069 | −0.0001 ± 0.0163 | +0.0137 ± 0.0117 |
| 10 | 0.4660 ± 0.0079 | −0.0194 ± 0.0073 | 0.9324 ± 0.0088 | +0.0052 ± 0.0141 | +0.0150 ± 0.0112 |

At side 10 the two preparations differ by about 2.2 combined standard errors in both the fixed normal-minus-zero comparison and the mixed lag. The mixed lag changes sign. The raw susceptibility and residual variance fraction agree within their stream errors. Four streams per preparation give limited resolution for the small lagged correlations. Moving the boundary is a sensitivity test; neither preparation supplies a bound on the error from the vacuum limit.

### Z4’s two-site comparison

Z4’s PS uses the unnormalized spatial sum of a single orientation, averaged over the three orientations when computing its connected variance. On $2^3$ divide its variance by **eight** to obtain the susceptibility in the [zero-momentum identity](pressure.md). Z4 reports PS variances 3.5029(16), 3.4984(17) and 3.4981(12) for $\beta=64,256,1024$, giving about 0.43786, 0.43730 and 0.43726 per site. These are Z4’s reported finite-period values. Their Gaussian reference gives $3.5/8=0.4375$. The earlier 3/64 is the absolute single-plaquette first-atom weight and has different normalization. [Two-site readout at 64 and 256](../../z4/attempt/reviews/l1-mcw/results/anapl_b64_b256_48ch.md) · [Readout at 1024](../../z4/attempt/reviews/l1-mcw/results/anapl_b1024_32ch.md) · [Independent Gaussian control](checks.md)

I ran the original one-site and extended box operator functions on two identical nontrivial windings $(1+i)/\sqrt2$ with the third winding equal to one. The common link field for the box uses commuting $N$th roots, so its plane-sum energy vanishes. The first $(1,2)$ tensor gives $+1/4$ in the one-site code and $-1$ in the box code at both sides two and four. Together with the earlier noncommuting, gauge-rotated tests this checks the signed factor $-4$. The program auditor also accepted this conversion. I sent Z4 the single-field test; Z4’s direct response on this particular sign was still outstanding when this note was prepared. [Executable comparison](signed.py) · [Auditor’s disposition](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7112562961) · [Test sent to Z4](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7112799494)
