# Winding and contractible tensor probes reflected across an open slab

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The smoothed winding and contractible $E^+$ operators in G4’s matched SU(2) ensembles give a **strictly positive two-by-two population matrix at each of the five lattice spacings**, for the reflected insertion defined below. This follows from the Wilson transfer and two explicit gauge configurations. The archived measurements resolve a mixed correlation more readily than the size of the determinant. The two independent probe states can still have nearly parallel propagated components or the same energy. Strict rank at finite cutoff supplies no volume-uniform mass bound. [Matched ensembles and original probe definitions](../../../../g4/full-attempt/physical-refinement/methods.md) · [Lucini, Rago and Rinaldi on combining winding and glueball operators](https://arxiv.org/abs/1010.6101)

## Why reflection works with these time boundaries

Use the slab of $6N$ time intervals with $N=\ell/a$ and midpoint $p=3N$. Its identical boundary vectors are $b=1$. Write $T$ for its one-step Wilson transfer and $Z=\langle b,T^{2p}b\rangle$. Let $X_i$ be the insertion on the left, and $Y_i$ its time reflection on the right. For each spatial tensor component, a left insertion $O_i$ at slice $j\le p$ prepares $T^{p-j}O_iT^jb$. Extend linearly for a weighted sum of insertion times. Then $G_{ik}=\langle X_iY_k\rangle$ is the inner product of the two prepared vectors divided by $Z$. Average over the three cyclic tensor components. Cubic symmetry gives zero one-point means. This construction uses the actual open-slab boundary state. [Lüscher and Schaefer, Eqs. 2.10 and 2.13](https://arxiv.org/pdf/1105.4749#page=6)

For even $N$ the point insertion is at $j=5N/2$ and its reflection. For odd $N$ take equal weights on the floor and ceiling of that slice **in each half**. The four products have separations $N-1,N,N,N+1$ and mean separation $\ell$. Keeping only the two diagonal products would change the Gram matrix. A second filter averages all integer slices in $[3N/2,5N/2]$ on the left and their reflections on the right.

## Strict rank at fixed cutoff

Write $W$ for the adjoint winding-trace differences and $C$ for the difference of squared clover fields, both spatially averaged after the archived spatial APE smearing. Suppose a real combination $O=uW+vC$ gives a zero point-filter norm. Each component then gives a zero prepared vector. On the physical Hilbert space $T$ is injective at positive Wilson coupling. Its electric character coefficients are positive, its magnetic half-weight is strictly positive, and its positive kernel takes the boundary constant to a strictly positive function under every power. [Lüscher, *Construction of a selfadjoint, strictly positive transfer matrix*](https://doi.org/10.1007/BF01614090)

For even $N$, injectivity implies $O T^j b=0$, hence $O=0$ almost everywhere. For odd $N$, put $f=T^j b>0$ at the earlier of the two slices. After removing the common injective transfer power, the condition becomes $T(Of)+O(Tf)=0$. Pair it with $Of$. This gives $\langle Of,T(Of)\rangle+\int O^2 f(Tf)=0$. Positivity of the first term and strict positivity of $f(Tf)$ force $O=0$ almost everywhere. The argument applies componentwise with real multiplication operators.

Two configurations separate the actual probe functions. Both have neighborhoods of positive Haar measure on which the finite smearing and measurements are continuous. [Archived Rust implementation](../../../../g4/full-attempt/physical-refinement/matched.rs)

- Take commuting constant links with full holonomy angle $\pi/2$ along axis 1 and identity along the other two axes. Smearing preserves these links. Every clover vanishes and a winding difference is $4/3$, so $u=0$.
- Next set $U_2(x)=\exp[i\sigma_3(\epsilon/N)\cos(2\pi x_1/N)]$ with all other links equal to the identity. One smearing iteration multiplies this transverse perturbation to first order by $s_N=(3+\cos(2\pi/N))/4$, from four spatial staples. For a clover of side $k$, the two oppositely placed faces on each side of $x_1$ yield a linear field proportional to $(k/N)\sin(2\pi x_1/N)\sin(2\pi k/N)$. Only the 1–2 plane contributes. In a positive cyclic clover difference the coefficient of $\epsilon^2$ is therefore

$$ B_N=\tfrac12 s_N^{2r_N}\sum_k w_k(k/N)^2\sin^2(2\pi k/N),\qquad r_N=\lfloor(N^2+6)/12\rfloor. $$

Here $w_k$ are the archived linear weights on the two integer sides adjoining $N/4$, applied to the completed squared fields. $B_N$ is positive on all five meshes, so $v=0$. The [Rust fixture](check_operators.py) calls the original smearing and probe routines. At $N=5,6,7,8,10$ it reproduces $B_N=0.0095903,0.0116874,0.0139011,0.0146083,0.0134383$. Expanding $s_N$ also gives $B_N\to e^{-\pi^2/12}/32=0.0137296$. This limit concerns a response coefficient on prescribed fields. A lower bound on the probability of their neighborhoods as $N$ grows would require another estimate.

## What the existing streams resolve

The [raw-data reduction](check.py) uses the two smoothed production streams of 192 saved configurations per mesh. Let $A_{ii}=\tfrac12\langle X_i^2+Y_i^2\rangle$, with the same component average as $G$. Write $g_{ij}=G_{ij}/\sqrt{A_{ii}A_{jj}}$. The final column uses one stream for each factor in the determinant numerator, symmetrized over assignments, divided by the pooled $A_{WW}A_{CC}$. Independent, equilibrium stream means make that numerator unbiased. The random normalization can still bias the ratio. [Archive inventory and sampling details](../../../../g4/full-attempt/physical-refinement/checks.md)

| $N$ | $g_{WW}$ | $g_{WC}$ | $g_{CC}$ | Split-stream determinant |
|---:|---:|---:|---:|---:|
| 5 | 0.198 ± 0.072 | 0.074 ± 0.045 | −0.011 ± 0.052 | −0.0060 ± 0.0077 |
| 6 | 0.240 ± 0.046 | 0.065 ± 0.026 | 0.039 ± 0.039 | 0.0067 ± 0.0079 |
| 7 | 0.184 ± 0.053 | 0.082 ± 0.028 | 0.017 ± 0.044 | −0.0041 ± 0.0077 |
| 8 | 0.151 ± 0.055 | 0.047 ± 0.026 | −0.021 ± 0.050 | −0.0054 ± 0.0075 |
| 10 | 0.298 ± 0.083 | 0.100 ± 0.054 | 0.008 ± 0.036 | −0.0065 ± 0.0121 |

Errors use stream-stratified delete-block jackknives of widths 8, 16 and 32, taking the largest. The three matrix entries also use the larger half-difference of the hot- and cold-start estimates when applicable. The archived streams do not resolve a positive determinant on any one mesh. Negative point estimates are retained.

For the equal-weight mean of these five separately normalized matrices, the mixed entry is $0.07346\pm0.01686$, the winding diagonal $0.21399\pm0.02822$ and the clover diagonal $0.00637\pm0.02006$. Errors for this mean assume independent mesh ensembles. The population mean is a Gram matrix, so $\bar g_{CC}\bar g_{WW}\ge\bar g_{WC}^2$. **If** the mixed and winding population entries lie within three displayed errors of their point estimates, then $|\bar g_{WC}|\ge0.02287$, $\bar g_{WW}\le0.29865$, and $\bar g_{CC}>0.00175$. The rectangle has no certified coverage. Its implication concerns the mean over these five meshes. The wider time filter gives $0.05580\pm0.02652$ for the mixed entry and no positive numerical floor at the same margin. None of these open-slab correlations establishes the energy or vacuum overlap of a contractible continuum state.

Run `python check.py` with NumPy for both time filters and `python check_operators.py` with `rustc` available for the field tests. Three recursive PCP OS workers checked the reflected slice indices, a two-component Gram identity, the independent-stream product identity, and the outward-rounded comparison. Lean verified [three declarations](ReflectedProbes.lean). The supervisor rejected a malformed delegation and three altered declarations. [Worker](worker.c) · [Replay](replay.py)
