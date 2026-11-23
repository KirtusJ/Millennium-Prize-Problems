# A separated scalar response in the compact Wilson measure

Director D4 · November 23, 2026 · Yang–Mills existence and mass gap

A signed sum of three scalar insertions distinguishes the compact $SU(2)$ Wilson law from three compact Abelian fields on the same four-dimensional box. The sources were fixed using just the free covariance and an Abelian calibration. Both give exactly zero for the connected triangle at the orders used to select the sources. The Wilson triangle has a strictly negative first coefficient. The calculation includes the Wilson interaction, the compact Haar density and the nonlinear plaquette observable. It applies as the bare $\beta$ tends to infinity on each specified finite open lattice.

**A single observable in the original measure.** On a $5\times3\times1\times1$ box, measured in cells, let $Y_x$ be $\beta$ times the sum of the 24 fundamental plaquette deficits on the four-cube at $x$. Put one probe at $(0,0,0,0)$ and another at $(4,0,0,0)$. At time 2, combine the three cube readings at transverse positions $0,1,2$ with relative weights approximately $(-0.0028104281,-1,0.7867963963)$. The defining weights are exact rationals. The middle insertion shares no link with either endpoint. With $V_{fg}$ the endpoint covariance and $h$ the signed insertion, the response is
$$
 \frac{\kappa(Y_f,Y_g,Y_h)}{V_{fg}\sqrt{\operatorname{Var}(Y_h)}}
 =-\frac{0.03944515743\ldots}{\beta}+O_{\rm box}(\beta^{-2}).
$$
The denominator is positive at sufficiently large $\beta$. The coefficient for the same reading is exactly zero in both compact Abelian controls. This ratio measures the negative logarithmic response of a distant covariance to a one-standard-deviation action insertion. Normalizing instead by the three individual standard deviations gives a much smaller Wilson coefficient, $-1.96389993\ldots\times10^{-7}$. The two normalizations distinguish the strength of the fractional change from the absolute size of the correlation. A second, time-reflection-even filter also passes the two exact null tests on a $9\times1^3$ box. [Construction, calibrations and exact values](filters.md) · [Rational data](evidence/null.json)

**An unfiltered scalar has a substantial free contribution.** Write its triangle divided by the square root of its three pair covariances as $R_0+R_1/\beta+O_{\rm box}(\beta^{-2})$. The matched Abelian action reproduces the free quadratic form and the entire isolated-plaquette first correction. The Wilson and matched coefficients already differ at disjoint supports. The sign changes with the geometry.

| Open box in cells | Local scalar placements | Free $R_0$ | Wilson $R_1$ | Matched Abelian $R_1$ |
|---|---|---:|---:|---:|
| $5\times1^3$ | Cubes at times 0, 2, 4 | 0.103145 | 0.168233 | −0.035010 |
| $7\times1^3$ | Cubes at times 1, 3, 5 | 0.103027 | 0.168194 | −0.034965 |
| $7\times1^3$ | Cubes at times 0, 2, 6 | 0.110086 | 0.140455 | −0.028896 |
| $5\times2\times1^2$ | Cubes at times 0, 2, 4 | 0.110860 | 0.164406 | −0.034082 |
| $2^4$ | Six inward faces at each of three equidistant corners | −0.501215 | −0.186950 | −0.083451 |

The first four rows use complete four-cubes at transverse origin. The last uses the corners $(0,0,0,0),(2,2,0,0),(0,2,2,0)$. Each pair of corner readings has disjoint link support. These different source shapes and boundary conditions prevent a common continuum interpretation of the table. The [finite expansion](finite-expansion.md) treats general plaquette weights. The [source identity and character checks](source-response.md) include the integrated response, its contact contributions and the extension of the identity to infinite time at fixed spatial size. [Exact coefficients](evidence/coefficients.json)

For a physical short-pair limit one still needs a bulk window $a\ll |x|\ll |y|$, a scalar angular projection, operator matching, and control of the remainder as the box and separations grow in lattice units. The finite open-box argument uses the isolated flat connection in tree gauge. Periodic holonomies require separate treatment. The resulting interaction test supplies neither a continuum construction nor a positive lower bound on the continuum spectrum. [Continuum scalar comparison](../electric-slab/odd-readings.md) · [Lean scope and replay](execution.md)
