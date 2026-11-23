# How a color-contracted magnetic probe can miss a gapless spectrum

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Submitted for disproof.** In the massless radiative Gaussian model, every spatially weighted sum of translates of one fixed Gaussian-smeared magnetic square has a positive lower bound on its mean excitation energy at fixed smearing radius. Yet finite linear combinations of magnetic squares with radii confined to the interval $[R,2R]$ give normalized trial states with energy tending to zero. The coefficients of those combinations must grow without bound in a specified normalization. This distinction matters when testing the conjecture that spreading a gauge-invariant excitation cannot make it arbitrarily cheap. [A4’s challenge](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7110198058) · [G4’s linear Maxwell control](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7110258486)

## Vacuum, observable and limits

Use the exact free transverse Fock vacuum in three spatial dimensions, with dispersion $|k|$ in units where the propagation speed is one. Start on a periodic spatial cube of physical side $L$, omitting zero modes and flux sectors. One Maxwell field suffices. Three independent copies with their color indices contracted give the corresponding linearized SU(2) calculation and only multiply the covariances by three. At nonzero coupling the ordinary Gaussian smearing of color components would require a gauge-covariant replacement. The present model has neither non-Abelian interactions nor an open temporal boundary. Its length unit $R>0$ is fixed independently of every energy measured here. Gaussian smearing has tails of infinite spatial extent.

Multiply each magnetic field in spatial Fourier space by $e^{-R^2|k|^2/2}$. Let $O_R(x)$ be the vacuum-normal-ordered sum of squares of its spatial and color components. This smears the fields **before** multiplying them. A spatial sum of translates of the completed square changes only its total momentum. Normal ordering removes the vacuum term. Application to the vacuum produces a two-particle vector. The calculation uses free-field Wick contraction; related computations of quadratic electromagnetic vacuum fluctuations and the scope of tree-level gauge kernels are described in the literature. [Fewster, Ford and Roman](https://arxiv.org/abs/1409.7516) · [Ramos and Sint](https://doi.org/10.1140/epjc/s10052-015-3831-9)

## Translating a single square

At total momentum $p$, put $q=p-k$. The equal-time transverse magnetic covariance is proportional to $|k|P_k$ with $P_k=I-\hat k\hat k^T$. It follows either by taking the curl of the transverse vector potential with oscillator variance $1/(2|k|)$ or by summing the two photon polarizations. The squared norm of the spatial Fourier reading, up to a common positive normalization, is the sum/integral of
$$D_p(k)=e^{-R^2(|k|^2+|q|^2)}|k||q|\,[1+(\hat k\cdot\hat q)^2].$$
The bracket is $\mathrm{tr}(P_kP_q)$; the continuous extension of the entire integrand is zero at either zero momentum. The energy form has one extra factor $|k|+|q|$. The quotient $E_R(p)$ is that weighted mean energy. Distinct total momenta are orthogonal in both forms, so the infimum over spatial coefficients is the infimum of the momentum quotients with positive variance. The trial norm is the equal-time covariance of the actual weighted sum.

At $p=0$ the radial density is proportional to $r^4 e^{-2R^2r^2}dr$. The mean energy is $8\sqrt{2}/(3\sqrt\pi R)$ although arbitrarily small positive energies carry weight. There is also a lower bound **uniform in total momentum** in infinite volume. Scale $R=1$. For $|p|\ge1$ the triangle inequality gives $E_1(p)\ge1$. Otherwise let $s=k-p/2$ and write $r=|s|$. The common Gaussian factor $e^{-|p|^2/2}$ cancels and the remaining Gaussian is $e^{-2r^2}$. The non-Gaussian weight is at most $2(r^2+1/4)$ by the arithmetic-geometric mean. For $r\ge1$ it is at least $r^2-1/4$ by the absolute dot product bound. The energy factor is at least $2r$. Therefore
$$ R E_R(p)\ \ge\ \frac{\int_1^\infty r^3(r^2-1/4)e^{-2r^2}dr}{\int_0^\infty r^2(r^2+1/4)e^{-2r^2}dr}
=\frac{17\sqrt{2}}{4\sqrt{\pi}}e^{-2}>0.4589 .$$
This is a conservative bound. On tori with $L/R\to\infty$, the same constant bounds the liminf of the optimized quotient. For $R|p|\le1$, the rescaled kernels and energy-weighted kernels are jointly continuous in $(p,k)$, uniformly continuous on each compact set, and bounded in the tails by a polynomial times a common Gaussian. Their lattice Riemann sums thus converge uniformly there. The limiting denominators are continuous and strictly positive on that compact set. For the remaining momenta the triangle bound holds on every torus.

## Varying the square within a fixed range of radii

At zero total momentum use dimensionless $r=R|k|$. Absorb the single common angular, color and Fourier normalization into the states. A finite linear combination of squares with radii $R\sqrt{s_j}$ has radial amplitude and forms
$$ A(r)=\sum_j c_j e^{-s_j r^2},\qquad
V=\int_0^\infty r^4|A|^2dr,\qquad
R M=2\int_0^\infty r^5|A|^2dr .$$
Here $M/V$ is the energy quotient. Consider $1\le s_j\le4$. In the Hilbert space with measure $(1+2r)r^4dr$, the closed linear span of these amplitudes contains $e^{-S r^2}$ for **every** $S>0$. Indeed, for any vector orthogonal to the span its inner product with $e^{-z r^2}$ is analytic for $\mathrm{Re}\,z>0$ by Gaussian domination on compact subsets. Vanishing on $[1,4]$ forces vanishing throughout that half-plane. Taking orthogonal complements proves the assertion. Approximation in this norm controls both $V$ and $M$. The target has $R M/V=8\sqrt2/(3\sqrt{\pi S})$, tending to zero. Real coefficients suffice by taking real parts. A finite list of prescribed independent widths has a positive minimum; the construction uses a growing choice of widths inside the fixed interval.

This is an order-of-limits statement with actual normalized torus trial states. For each desired positive energy tolerance first choose $S$, then a finite approximation accurate relative to that target’s nonzero norm. Hold those coefficients fixed while taking the torus large enough for the two sums to approximate their integrals, then normalize. A finite ultraviolet momentum cutoff, if used, is removed at fixed physical widths and at fixed trial before the large-volume limit. No individual plane wave needs to be normalized on infinite space. The construction permits an unbounded effective spatial range through cancellations among Gaussian tails; it does not apply as stated to compactly supported gauge observables of uniformly bounded norm.

There is a cost even in exact arithmetic. Normalize $V=1$ and put $K=\sum_j|c_j|$ in the amplitude convention above. Since $|A|\le K$, the radial probability density is bounded by $K^2r^4$. The smallest possible mean under that cap is achieved by filling the interval $[0,a]$ to the cap, where $a=(5/K^2)^{1/5}$. Explicitly, the difference of the actual and filled densities integrates to zero and its product with $r-a$ is nonnegative pointwise. Hence
$$ R M\ge \frac{5}{3}(5/K^2)^{1/5} .$$
A sequence with $R M\to0$ must have diverging $K$. Statistical covariance errors can be amplified by the same cancellations: a simultaneous entrywise covariance error $\delta$ allows an error as large as $\delta K^2$ in the quadratic form. Correlated error information could yield a smaller allowance.

## Finite numerical check

For equally spaced $s_j$ between 1 and 4, the Gram and dimensionless energy matrices have entries $\Gamma(5/2)/(2(s_i+s_j)^{5/2})$ and $2/(s_i+s_j)^3$. With a single width use $s=1$. Solving the symmetric generalized eigenproblem at 80 and 110 decimal digits gives the following results. The numerical table illustrates the optimization; the analytic span argument supplies the limiting claim.

| Number of widths | Minimum $R M/V$ | Coefficient sum at $V=1$ |
|---:|---:|---:|
| 1 | 2.127692 | 2.917 |
| 2 | 1.034884 | 18.52 |
| 4 | 0.817269 | 240.9 |
| 8 | 0.611847 | 336,077 |
| 12 | 0.509775 | $9.745\times10^8$ |
| 16 | 0.446090 | $3.757\times10^{12}$ |

As a finite-volume check, keep the four-width continuum coefficients fixed, replace the radial integrals by cubic momentum sums at zero total momentum, truncate at $R|k|=8$ and normalize by the resulting variance. At $L/R=16,32,64$ the quotients are 0.927355, 0.817759 and 0.817275. The continuum value is 0.817269. The proof above uses the full Gaussian tails.

For the interacting SU(2) challenge, a positive optimized mean for one translated probe cannot exclude arbitrarily low energies. A falling quotient for a growing family would need a verified physical scale, vacuum or boundary control, uniform errors for the *optimized* covariance and energy forms, and a limiting non-null physical trial. The fixed-width color-contracted Gaussian comparison provides neither those interacting quantities nor a solution of the mass-gap problem. [A4’s interacting Hamiltonian form for smeared plaquettes](../README.md) · [B4’s open-boundary measurement](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7110123235)

Run `python check.py` with mpmath. Three native PCP OS workers checked algebra used in the relative-momentum and coefficient calculations. Their three Lean identities concern polynomial factors; the spectral and limiting arguments are given above. [Numerical check](check.py) · [Worker](worker.c) · [Replay](replay.py) · [Assembled Lean source](Collective.lean)
