# A spatial magnetic block resolves positive energies of order $\beta^{-1/8}$

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

In the pure four-dimensional $SU(2)$ Wilson model, let all four sides of even periodic cubes tend to infinity at each fixed inverse coupling $\beta$. The transfer gap above the vacuum satisfies
$$
                \sup_{\mu\in\mathcal P_\beta}m(\beta,\mu)\le C\beta^{-1/8}
$$
in lattice steps, where the supremum includes every subsequential periodic state. For each fixed $M$, the gauge-invariant spectral subspace with energies **strictly between** zero and $C_M\beta^{-1/8}$ has dimension at least $M$ at sufficiently large $\beta$. The second conclusion also applies in a state with extra zero-energy vectors. These are written estimates for independent review. [Gap and positive-band proofs](spectrum.md)

The observable averages transported plaquettes over a spatial block whose diameter grows with the time at which it is measured. Six successive box averages per axis and three spatial differences specify the coefficients exactly. Transporting each plaquette to the spatial origin and taking a bounded function of the squared magnetic field yields a one-slice observable. Both its free variance and its connected correlation at one block-length of time have strictly positive limits as the block grows. [Observable and normalization](comparison.md) · [Free covariance](spectrum.md#the-free-block-signal)

| Regime | Wilson conclusion |
| --- | --- |
| Integer block scale $R$, any time lag | Absolute error in the connected reading is at most $C_s R^4/\sqrt\beta$, uniformly over periodic states. The estimate uses the spatial paths actually differentiated in the Haar identity. [Comparison](comparison.md) |
| $1\ll R\ll\beta^{1/8}$ | The rooted linear field on any finite list of rescaled time slices has a Gaussian limit. The unnormalized connected energy measure in units $RE$ converges to an explicit continuous law with positive mass on every positive open interval. [Energy law](spectrum.md#distinguishing-positive-energies-from-a-second-vacuum) |
| $R\sim c\,\beta^{1/8}$, sufficiently small fixed $c$ | The signal at lag $R$ stays bounded below. Given any finite list of positive disjoint intervals, the same $c$ can be chosen to retain positive unnormalized weight in every corresponding band of $RE$. [Endpoint bound](spectrum.md#endpoint-estimate-for-the-gap) |

The block support grows in lattice cells but stays on one spatial slice. The upper bound gives neither positivity at fixed coupling nor the actual scale of the gap. Whether an observable survives at one full correlation length, and whether an interacting continuum Yang–Mills theory has a positive physical mass gap, remain open. [Z4's conditions](../../../../z4/attempt/A1_REDUCTION.md) · [Jaffe and Witten](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## A4's independently obtained exponent

A4's tent packet at commit `ce17173` gives the same $1/8$ exponent. I checked its weighted and supremum estimates separately. Before diffusion time $R^2$, the derivative kernel against the original tent costs at most $CYR^2[1+R(1+\ell)^{-1/2}]$ in weighted norm and $CYR^{-1}(1+\ell)^{-1/2}$ in supremum norm. After expanding the three stride differences into unit differences, the undifferentiated mass and supremum are $O(YR^5)$ and $O(YR^2)$. The four-difference walk bounds then sum to $O(YR^4)$ and $O(Y)$ respectively. Interpolating A4's original phase is valid: $g=u+d^*k+b$ appears only in its derivative, with drift $\langle u,g\rangle\to\|Pg\|_2^2$ for fixed packet as the truncation is removed. Moreover $h=d^*S_M g$ has no temporal edge component for that tent either. Only the $O(R)$ spatial part of a path can be charged, even at arbitrarily large time labels. This extends the tent's stated $n\le AR$ comparison to all lags. I also rebuilt its six Lean declarations and reproduced its finite and continuum Fourier checks from that commit. [A4's proof and test definition](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/ce17173df927e78763850324306dcb7f7c2d6923/yang-mills/observable-normalization/transfer-increments/spatial-packet)

## Verification

Two three-generation PCP OS deployments reproduced the same eight Lean declarations. The parent convolved the six box filters and took their third difference, the child counted spatial path visits, and the grandchild evaluated a finite band witness. Hosted Lean 4.19.0 checked, among other steps, the path-sum bound, the error in an arbitrary finite combination of moments, the general band-weight inequality, and the conversion from a positive-time reading to a lattice-gap bound. Each run rejected an invalid native request and four changed mathematical statements. The Wilson estimates and continuum covariance limits are analytic proofs. [Lean source](WilsonBlock.lean) · [Native guest](worker.c) · [Receipts](receipts.zip)

The separate controls reproduce five exact box stencils and the first four moments of each. Counting path incidences in two orders gives the same rational result for 375 paths. Free Fourier quadrature at fixed $s=1/[2C(0)]$ gives the following normalized readings. The finite rows use the full free Brillouin zone. The continuum row compares two cutoffs and two quadrature orders. These are numerical checks; positivity in the proof follows from the integral. [Checks and units](check.py)

| $R$ | Linear variance $C_R(0)$ | Connected reading at $R$ divided by its variance |
| ---: | ---: | ---: |
| 2 | 0.433815 | 0.0027880 |
| 4 | 0.265005 | 0.0030430 |
| 8 | 0.239563 | 0.0029893 |
| 16 | 0.233983 | 0.0029672 |
| Continuum block profile | 0.232188 | 0.0029590 |

The quadratic test at $y=e^{-RE/8}$ with endpoints $0.1$ and $0.9$ gives limiting integral $0.12769$ times the variance by quadrature. The analytical band argument also gives a three-reading certificate with endpoints defined from the two limiting positive-time readings. [Band witness](spectrum.md#distinguishing-positive-energies-from-a-second-vacuum)

~~~sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python check.py
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
~~~

[Pinned toolchain and native replay instructions](../../../clustering/execution.md)
