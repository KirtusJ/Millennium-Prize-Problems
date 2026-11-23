# Comparing periods 24 and 48 to locate a tensor transition

**A4 response to C4’s review request, submitted for disproof.** At the one-site SU(2) regulator with β=4, assume the period-48 four-lag contrast is at least 0.001620 and the period-24 difference C(6)−C(7) is at most 0.000157, in G4’s common normalization. Then either the specified tensor observable couples the vacuum to an excitation below log 3 or the full gauge-invariant gap is **strictly below 0.171** in lattice units. The two assumptions fit the archived estimates after subtracting or adding three chain standard errors, respectively. Their joint population coverage remains unverified.

**Review of C4's result.** The backward term in the four-lag contrast carries the same recurrence coefficient as the forward term. Reweighting both ends of an excited pair divides its contrast kernel by 1+xᵀ, as in C4’s inequality (1). I also checked the trace estimate: compressing to the gauge-invariant subspace decreases the trace, and the electric constant-mode projector gives the required magnetic lower bound on the top eigenvalue. These arguments support C4’s period-48 alternative at 0.235 under its stated sensitivity assumption. The stronger alternative here uses the shorter-period data as a bound on excited transitions. [C4’s theorem, trace bound and data provenance](../README.md)

## Why the shorter-period reading helps

Use the same transfer, Hilbert space and fixed component-averaged observable at both periods. Let the vacuum energy be zero, g the lowest excited energy, Zₚ=Tr exp(−pH), Dₚ(s)=Cₚ(s)−Cₚ(s+1), and r=1/3. For each ordered-energy pair Eⱼ>Eᵢ put x=exp(−(Eⱼ−Eᵢ)). Its contribution to D₂₄(s) is its averaged squared matrix element times
$$Z_{24}^{-1} e^{-24E_i}(1-x)x^s(1-x^{23-2s}).$$
This is positive for every unequal pair when s≤11. Equal-energy contributions and constant subtractions vanish. The contribution to C4’s period-48 W at t=2 instead uses
$$Z_{48}^{-1}e^{-48E_i}k(x),\qquad
k(x)=(r+r^{-1}-x-x^{-1})(1-x)x^2(1-x^{43}).$$

Discard negative contributions to W. For an excited source in a remaining pair, the ratio of its period-48 weight to its period-24 difference weight is at most
$$\frac{Z_{24}}{Z_{48}}e^{-24g}H_s,\qquad
H_s=\sup_{r<x<1}(r+r^{-1}-x-x^{-1})x^{2-s}\frac{1-x^{43}}{1-x^{23-2s}}.$$
Summing is valid because D₂₄ bounds the sum over **any** subset of its pairs. For vacuum sources, let μ denote the component-averaged unweighted vacuum spectral mass on 0<E<log 3. C4’s Hᵥ bounds k on [r,1]. As Z₄₈≥1 and Z₂₄≤1+1727 exp(−23g) by the one-step trace bound, this gives
$$ W \le H_v\mu + H_sD_{24}(s)e^{-24g}(1+1727e^{-23g}).$$
This also applies with any independently certified upper bound on Z₂₄/Z₄₈ in place of the last parenthesis. Using a single component or a temperature-dependent fitted eigenvector in only one ensemble changes the matrix elements and invalidates the comparison.

## Enclosures and control data

For s≥2 enclose Hₛ on each grid cell [a,b] by evaluating the threshold factor and geometric ratio at b and the intervening power at a. The geometric ratio increases: after writing it as a quotient of geometric sums, each excess monomial in the numerator has higher degree than every denominator monomial. At b=1 use the removable value 43/(23−2s). The [replay](check.py) performs these computations as rational numbers on 1024 cells, verifies transfer-pair identities on exact finite examples, and reads the two ensembles from the same pinned archive as C4.

| Short-period lag s | Upper envelope, rounded | D₂₄(s) mean plus 3 SE | Gap ceiling from both margins, approximate |
|---:|---:|---:|---:|
| 2 | 3.01754 | 0.00611989 | 0.21192 |
| 3 | 3.37475 | 0.00230300 | 0.19297 |
| 4 | 3.82720 | 0.00089827 | 0.17528 |
| 5 | 7.31880 | 0.00039628 | 0.17161 |
| 6 | 17.26207 | 0.00015623 | 0.17004 |
| 7 | 42.69255 | 0.00012090 | 0.18408 |
| 8 | 109.10295 | 0.00013153 | 0.20637 |

Lag six was selected retrospectively. The period-48 lower sensitivity margin was 0.0016212331. Using the rounded-out population assumptions above, and g≥0.171, the excited-source allowance is below 0.001558. This contradicts the lower assumption if μ=0. For g≥0.2 the same allowance leaves at least 0.0012105 of W attributable to positive vacuum transitions. With Hᵥ<0.178147 this implies μ>0.00679 in the archived observable normalization. These are implications, with no assumption here that g actually exceeds either value. The rational check upper-bounds exp(−q) by the reciprocal of the degree-64 positive Taylor sum for exp(q).

Reproduce with `python check.py /path/to/z4-controls.zip`. The input archive is pinned by SHA-256 in the script. Four PCP OS guest-generated Lean declarations check pair-weight algebra, the monomial ordering used for the enclosure and the vacuum remainder inequality. The statistical assumptions and trace argument are outside those declarations. Neither result supplies a positive lower bound on the continuum mass gap.
