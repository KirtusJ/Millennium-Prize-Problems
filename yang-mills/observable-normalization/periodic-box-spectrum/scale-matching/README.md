# Matching the periodic small-box spectrum to an independently measured scale

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The published small-box scalar coefficient is **2.2696390**. The leading tensor gap extracted from the published energy table is **about 1.8978**. These are coefficients of vacuum-subtracted energies in a periodic spatial cube. A4’s fixed-regulator calculation and the small-volume continuum calculation agree in their leading normalization. Whether the periodic spectrum approaches these energies at fixed physical size is a separate test. Published measurements of the running coupling at four resolutions provide starting values for that test.

## Comparison requested by Z4

Van Baal and Koller give the scalar result explicitly on printed page 352, Eq. (9.1). For a physical spatial side $\ell$ and a renormalized coupling $g$ at the box scale,
$$\ell M_{0^+}=2.2696390\,g^{2/3}-0.7975278\,g^{4/3}+O(g^2).$$
They attribute this equation to Lüscher and Münster. Van Baal’s later Table 2 gives absolute leading energies, including the vacuum. Its columns describe different cubic symmetry sectors. Equation (24) shows that the leading coefficient is independent of the number of fermion flavours. This permits using the leading row even though the example printed in the table has three flavours. The scalar second coefficient above comes from the pure-gauge Eq. (9.1). I verified both pages against the scans. I could verify the original 1984 article’s bibliographic record and abstract only. [Van Baal and Koller, Eq. (9.1)](https://www.ilorentz.org/research/vanbaal/DECEASED/HOME/JOUR/APNY174_299.pdf#page=54) · [Van Baal, Eqs. (24)–(26) and Table 2](https://www.lorentz.leidenuniv.nl/research/vanbaal/DECEASED/HOME/JOUR/NPB307_274.pdf#page=10) · [Lüscher and Münster (1984)](https://doi.org/10.1016/0550-3213(84)90038-5)

| Channel | Leading energy less vacuum, from printed entries | Z4’s value in the same units | What the comparison resolves |
|---|---:|---:|---|
| Excited scalar $A_1^+$ | $6.386359-4.116720=2.269639$ | 2.2696457 | Z4 is higher by 0.0000067. Agreement to five significant digits. |
| Tensor $E^+,T_2^+$ | $6.0145-4.116720\simeq1.8978$ | 1.8977806 | Both columns have the same printed leading energy. The four decimals in 6.0145 limit the comparison. |

The lowest tensor and first excited scalar are distinct. A scalar correlator cannot establish the tensor gap. With Wilson $\beta=4/g_0^2$, the lattice matrix gap $e$ in $N m_{\rm lat}\sim e\beta^{-1/3}$ converts to the quoted coefficient $\epsilon=e/4^{1/3}$ multiplying $g_0^{2/3}$. This conversion compares the leading matrix Hamiltonians. Replacing the bare coupling by a running coupling at fixed physical volume requires control along the refinement trajectory. [Z4’s normalization and values](../../../z4/attempt/reviews/h2-ground/report.md) · [A4’s fixed-box expansion](../full-neutral.md)

## One coupling, two ensembles

Use the pure SU(2) isotropic Wilson action. Fix the physical side by the target $u=g_{\rm TGF}^2(\ell)=0.55$ at $c=0.3$ on Ramos’s twisted four-torus, with $\sqrt{8t}=c\ell$. At each spatial lattice size $N=\ell/a$, tune $\beta_N$ using that observable alone. This identifies a common finite-volume scale in the continuum if the running coupling locally determines $\ell$ uniquely. The two ensembles share the bare regulator. The spectral measurement uses **periodic** spatial boundary conditions and an independently long temporal extent, with control of finite-time effects. The twist belongs to the scale setting. Using the twisted spectrum would change the zero-mode problem. [Ramos, Eqs. (4.2), (4.4), Sec. 5 and Table 3](https://arxiv.org/pdf/1409.1445#page=25)

All four rows below bracket the target between $\beta=8$ and $10$, including when the endpoint measurements are moved three published standard errors toward the target. Interpolating $1/u$ linearly in $\beta$ gives the first estimate of $\beta_N$. The second assumes $u$ is linear in $\beta$. As a separate check of curvature, I removed the $\beta=10$ datum and predicted it from $8$ and $12$ with the inverse-coupling interpolation. The last column gives predicted minus measured coupling divided by its propagated standard error, assuming independent ensembles at different $\beta$. These four comparisons use the same source, and neither interpolation provides a systematic-error bound. The published analysis uses global fits. A periodic run intended to distinguish percent-level effects needs its own verified tuning. [Raw measurements, Table 3](https://arxiv.org/pdf/1409.1445#page=25) · [Calculations and input errors](check.py)

| Sites per side | $\beta_N$ from $1/u$ | $\beta_N$ from $u$ | Held-out residual, standard errors |
|---:|---:|---:|---:|
| 10 | 9.07320 | 9.21032 | +0.05 |
| 18 | 9.27566 | 9.40477 | +1.16 |
| 20 | 9.33082 | 9.45401 | −0.05 |
| 36 | 9.55111 | 9.64664 | −0.69 |

## What the periodic measurement can decide

Measure $z_N=N m_{\rm lat}$ separately in the scalar and tensor channels. For the first interpolation, extending the bare fixed-box leading formula to these endpoints predicts $z_{36}/z_{10}=(9.07320/9.55111)^{1/3}=0.98304$. A common nonzero continuum energy at matched $u$ gives an asymptotic ratio of one when both sizes tend to infinity at fixed size ratio. Its value at 10 and 36 sites can carry cutoff effects. A 1.7% difference across those endpoints alone cannot discriminate the two limits without independent control of scale tuning, discretization, temporal extent and spectral extraction. Table 3 contains no periodic transfer energies.

The scalar expansion also illustrates the danger of a leading-order fit. A regular perturbative scheme change $g^2=u+O(u^2)$ preserves the first two powers $u^{1/3}$ and $u^{2/3}$ and their coefficients. At this target the scalar terms give $1.85956-0.53537=1.32419$. The correction is about 29% of the leading term, and the remainder has no bound here. A comparison across progressively smaller physical couplings can separately test the coefficient and the sign of the correction after extrapolation in $a/\ell$ at each coupling. [Ramos, Eq. (4.4)](https://arxiv.org/pdf/1409.1445#page=16) · [Pure-gauge expansion](https://www.ilorentz.org/research/vanbaal/DECEASED/HOME/JOUR/APNY174_299.pdf#page=54)

Follow the vacuum-subtracted spectral weight in the same channel as each energy, using a fixed physical operator prescription across resolutions. A4’s submitted analysis finds that the centered elementary plaquette loses its soft spectral weight at fixed $N$ while certain winding probes retain it. A winding signal alone leaves the local continuum question open. The matched periodic energies, local overlaps, infinite-volume limit and a gap on four-dimensional Euclidean space remain open. [A4’s observable analysis](../observable-weights/README.md) · [Jaffe and Witten, problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

Three recursive PCP OS workers checked the four central-value brackets and both vacuum subtractions. Lean 4.19.0 accepted the three finite arithmetic declarations without axioms. The supervisor rejected a malformed delegation and three altered declarations. These controls cover arithmetic and worker readback. The interpolations and held-out residuals are reproduced independently with `python check.py` using the printed data. [Native worker](worker.c) · [Recursive replay](replay.py) · [Lean declarations](ScaleMatching.lean)
