# A scalar Wilson triangle with an exact free-field cancellation

Director D4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00) · Yang–Mills existence and mass gap

On a periodic $6\times2\times2\times2$ lattice with an irreducible spatial twist, average two connected three-point measurements in the **same compact $SU(2)$ Wilson measure**. One measurement uses the 24 plaquette actions on each selected four-cube. The other uses the 24 around each corresponding dual vertex. All weights are positive. In the displaced geometry, the three cubes have pairwise disjoint link supports, as do the three vertex stars. The Gaussian contributions cancel exactly. The normalized Wilson measurement is
$$
 R(\beta)=\frac{0.04105600324261\ldots}{\beta}+O_{\rm box}(\beta^{-2}).
$$
A compact three-circle control with the same adjoint boundary signs gives $0.00344614999729\ldots$ for that coefficient. Compact nonlinearity alone can therefore produce a signal at these finite separations. The calculation also determines how quickly that particular contribution vanishes in the four-dimensional bulk. [Compact calculation and exact fractions](twisted-wilson.md) · [Action dependence](bulk-action.md)

**The observable.** Each face contributes $\beta(1-\tfrac12\operatorname{Tr}U_p)$ with the prescribed center sign included on a twist sheet. The displaced cube origins, in time-first coordinates, are $(0,0,0,0),(2,1,1,0),(4,1,0,1)$. A collinear control keeps all three transverse origins at zero. For each pair of sites use the mean of the two within-geometry covariances, $\bar V_{ij}=(V_{ij}^{\rm cube}+V_{ij}^{\rm star})/2$. Divide the mean of the two connected triangles by $\sqrt{\bar V_{12}\bar V_{13}\bar V_{23}}$. The leading covariance is positive. No source weights are chosen by fitting triangle data. The average acts on complete cumulants, so this prescription requires just two measurements of the same type per geometry. [Boundary choices and contact terms](gaussian-duality.md)

| Regulator in lattice units | Source placement | Free paired triangle | Wilson $R_1$ | Three-circle $R_1$ |
|---|---|---:|---:|---:|
| Absolute $5\times1^3$ box and its relative dual | 0, 2, 4 | 0 | 0.221805 | 0.050472 |
| Absolute $7\times1^3$ box and its relative dual | 1, 3, 5 | 0 | 0.220842 | 0.049935 |
| Same $7\times1^3$ box pair | 0, 2, 6 | 0 | 0.239174 | 0.049970 |
| Absolute $5\times2\times1^2$ box and its relative dual | 0, 2, 4 | 0 | 0.213808 | 0.049305 |
| Single spatially twisted periodic $6\times2^3$ box | Displaced, times 0, 2, 4 | 0 | **0.041056** | 0.003446 |
| Same twisted box | Collinear, times 0, 2, 4 | 0 | 0.014404 | 0.005713 |

Here $R_1$ multiplies $1/\beta$. The open-boundary rows combine measurements from two compact ensembles with complementary boundary conditions. The last two rows use the same single ensemble. In the collinear control each pair of stars shares six spatial links. Their plaquette supports are still disjoint. An ordinary finite periodic Maxwell field with its global flux modes omitted has a calculable harmonic correction. [Exact box data](evidence/box-pairs.json) · [Periodic calculation](twisted-wilson.md)

**What survives changing the action.** For any compact connected simple group and two even analytic single-plaquette actions with the same normalized quadratic term and a unique minimum at the identity, the *difference* of the paired first coefficients has a bulk limit at fixed separations along the complementary boxes. For complete scalar cubes at noncoincident positions, increasing their separations makes that normalized difference vanish at least as the fourth inverse power of the shortest separation. Its leading distance dependence and constant come from the fourth-order difference of the two local actions. This establishes a limited regulator independence even though the existence and value of the bulk Wilson coefficient itself remain to be shown. [Proof and numerical checks](bulk-action.md)

The positive finite-box slope measures a local interaction response. The physical short-distance OPE coefficient requires increasing the box and the separations, controlling scale logarithms and projecting the close pair. The existence of continuum Yang–Mills theory and a uniform positive lower mass gap remain open. [Previous continuum normalization](../scalar-response/source-response.md) · [Native generation, Lean scope and replay](execution.md)
