# A weak-coupling rate for the Wilson gap in lattice steps

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For pure four-dimensional $SU(2)$ Wilson theory, take all four sides of even periodic cubes to infinity at each fixed $\beta$. The gap $m$ above the vacuum, measured in lattice time steps, obeys
$$
       \sup_{\mu\in\mathcal P_\beta} m(\beta,\mu)
       \ \le\ C\,\beta^{-1/32}[\log(2+\beta)]^{1/16}
$$
at sufficiently large $\beta$, where $\mathcal P_\beta$ includes every subsequential periodic state. The observable that gives this upper bound uses just three parallel spatial plaquettes with coefficients $(1,-2,1)$, transported to the same site. Its bounded autocorrelation can be compared to the free lattice curvature **at every time lag** with a uniform absolute error. This is a quantitative extension of the [fixed-lag argument](../README.md), submitted for independent review. [Transfer estimate](spectrum.md#upper-bound-on-the-lattice-gap)

| Spatial difference | Error in the connected reading, uniformly in the lag | Large-lag free reading | Consequence for the lattice gap |
| --- | --- | --- | --- |
| First | $O(\beta^{-1/4})$ | $b_1 n^{-12}$ asymptotically | $O(\beta^{-1/48})$ |
| Second | $O(\log(2+\beta)/\sqrt\beta)$ | $b_2 n^{-16}$ asymptotically | $O(\beta^{-1/32}[\log(2+\beta)]^{1/16})$ |
| Third | $O(1/\sqrt\beta)$ | $b_3 n^{-20}$ asymptotically | $O(\beta^{-1/40})$ |

The color paths move in time first. Adding one edge to such a path requires commuting it through spatial steps only, even when the measurements are very far apart in time. The exact six-face cube identity then bounds the error in ordinary additive closedness by one power of spatial distance. The Haar variation also differentiates the paths used to transport the field. Keeping this term is necessary. [Original-link estimates](ward.md)

A truncated inverse of the lattice Hodge Laplacian separates the observable into an exact test, a coexact test and a heat-kernel remainder. Absolute first moments of spatially differentiated walk kernels keep the resulting estimates independent of the time coordinates. Comparing connected readings at $n$ and $2n$, where both are resolved to relative accuracy, gives the gap bound. [Heat estimates](heat.md) · [Spectral argument](spectrum.md)

For every $0<\alpha<1/32$, the second difference also has a positive-time limiting law at $T=\beta^\alpha$ lattice steps. Its connected reading divided by its value at $T$ tends to $t^{-16}$ at time $tT$ for fixed $t>0$. The spectral probability tilted at $T$ converges in units $TE$ to Gamma with shape 16 and rate one. In these units the lattice gap tends to zero. Positivity of the gap at fixed coupling, the actual correlation-length scale and a positive interacting continuum mass gap remain open. [Time and energy limits](spectrum.md#the-law-before-the-correlation-length-scale) · [Clay formulation](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Verification

Two three-generation PCP OS replays returned identical Lean source. The parent enumerated all six cube faces and their orientations, the child computed the total variation of the four-update lazy binomial kernel, and the grandchild computed the second-difference doubling factor. Hosted Lean 4.19.0 verified nine supporting declarations, including weighted summation by parts, the heat-polynomial telescope, and the implication from two perturbed readings to a gap bound. Each replay rejected an invalid native request and four altered declarations. The Wilson comparison and rate have written analytic proofs. [Lean source](WilsonRate.lean) · [Native worker](worker.c) · [Receipts](receipts.zip)

The separate calculations checked 144 noncommuting cube cycles, five derivatives involving a root path, and 36 Hodge decompositions. Omitting path differentiation changed one derivative by 1.47. Including it gave maximum discrepancy $7.7\times10^{-11}$ against finite differences. Two quadrature orders reproduced nine reference covariances. The finite free checks do not estimate the unknown constant in the gap bound. [Numerical checks](check.py) · [Replay driver](verify.py) · [Pinned toolchain](../../../clustering/execution.md)

~~~sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 python check.py
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
~~~
