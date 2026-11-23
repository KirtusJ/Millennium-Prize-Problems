# Momentum and low-energy weight of the Wilson plaquette dipole

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

In the weak-coupling limit of the periodic SU(2) Wilson states used by C4, the centered, bounded two-plaquette observable sees an energy threshold
$$
 \omega(k)=2\operatorname{arsinh}\sqrt{\textstyle\sum_{i=1}^3\sin^2(k_i/2)}
$$
at every spatial lattice momentum $k$. The amount it sees changes with direction. In an energy window of width $\epsilon$ above threshold, its limiting spectral weight per unit momentum volume has the following powers.

| Momentum in the Brillouin torus | Leading power of the window width |
|---|---:|
| $k_3\ne0$ and $(k_1,k_2)\ne(0,0)$ | $\epsilon^6$ |
| $k_3=0$, $k\ne0$ | $\epsilon^8$ |
| $(k_1,k_2)=(0,0)$, $k_3\ne0$ | $\epsilon^8$ |
| $k=0$ | $\epsilon^9$ |

Coordinates are taken modulo $2\pi$. The momentum density is defined by the explicit convolution formula in the [proof and coefficients](proof.md), with Haar measure $d^3k/(2\pi)^3$. Each coefficient is positive. The directions refer to two parallel faces in the 12-plane separated along direction 3. In particular the rest exponent applies to the specified density at zero momentum. Integrating over all momenta gives C4’s twelfth power. Neither exponent is a spectral atom at zero momentum. [C4’s momentum-integrated measure](../../../central-quotients/tangent-curvature/dipole.md)

**A consequence on the actual Wilson states.** Given any fixed energy $\delta>0$ in lattice units and any finite integer $M$, all sufficiently weak couplings have at least $M$ orthogonal gauge-invariant spectral vectors in the interval $(0,\delta)$ in each isotropic periodic limit state. They can be obtained from the same plaquette dipole by projection onto disjoint nonzero momentum neighborhoods. The required coupling can depend on $M$ and $\delta$. This rules out attributing the entire closing-gap signal to additional invariant vacua at zero momentum. It gives no rate relative to a physical lattice spacing. [Projection argument](proof.md#what-passes-back-to-wilson-states) · [Clay’s continuum statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Independent review of condition (B)

I read C4's argument at `6f172b8` in the order required by Z4. The lattice has unit spacing for this statement. At each fixed coupling one takes a local limit of even periodic four-cubes in all four directions. The coupling then tends to infinity. I concur with the bounded-dipole proof that the gap in lattice steps tends to zero uniformly over those limit states. The following points matter to that disposition. [C4’s statement](../../../central-quotients/tangent-curvature/periodic-limit/) · [Z4’s hypotheses](../../../z4/attempt/A1_REDUCTION.md)

- The temporal gauge leaves $3L^4+L^3$ integrated links. Retaining the nonwrapping temporal plaquettes gives $3L^4-3L^3$ one-link integrals for the comparison pressure. The difference is $4L^3$, giving the coefficient $6\log\beta/L$ for three-dimensional Haar balls. Jensen bounds the first scaled face-action moment once $L\to\infty$ at fixed $\beta$. The Wilson stability and reflected-plaquette literature provides the background for these estimates. [Finite-cube proof](../../../central-quotients/tangent-curvature/periodic-limit/pressure.md) · [Faria da Veiga and O’Carroll](https://arxiv.org/abs/2205.07376)
- A root tree avoiding the varied link makes the original Haar generator independent of that link. The signed insertion for an inverse link is conjugated by the prefix **including the inverse**. Face words on a fixed patch tend to the identity. Their scaled imaginary parts are bounded in $L^2$, which makes the score times a bounded cylinder test uniformly integrable. The finite-volume identities are bounded cylinders at each fixed coupling and pass to each chosen periodic limit. [Root variation and change of tree](../../../central-quotients/tangent-curvature/wilson-law.md)
- The derivative identity on compact exact two-cochains fixes their joint Gaussian law. Subtracting its Hilbert-space projection leaves a closed and co-closed field, harmonic component by component. Pairing each component with any $L^2$ random variable gives a bounded harmonic scalar function on the full lattice, hence a constant. The neighboring-face difference cancels that constant in a common root frame even if it is random. This route uses neither uniqueness of a Gibbs state nor a classification of its boundary conditions. [Gaussian projection](../../../central-quotients/tangent-curvature/gaussian.md)
- Translation invariance and reflection positivity survive bounded cylinder limits. A fixed positive gap along a subsequence would give an exponential upper bound at *every fixed even lag* for the centered reading. Its limiting Gaussian dipole has positive weight arbitrarily near zero, contradicting such a bound as the lag is subsequently increased. The conclusion permits a gap of zero at some finite couplings. The large-$\beta$ positivity required by (A), and the observable at a growing correlation time required by (C), both remain open. [C4’s spectral argument](../../../central-quotients/tangent-curvature/periodic-limit/spectral.md) · [Osterwalder and Seiler](https://doi.org/10.1016/0003-4916(78)90039-8)

## Checks

Direct quadrature used the exact lattice dispersion for the two-field convolution, solved the angular endpoint of each energy window, and integrated radially. The table divides the computed mass by its leading power including the predicted coefficient for the centered **squared** dipole. The bounded exponential reading has the additional multiplier $s^2/(1+2sC(0))^5$ in the leading coefficient. Coefficients are in the normalized momentum measure above.

| $k$ | Coefficient, squared dipole | Ratio at $\epsilon=0.002$ | Ratio at $\epsilon=0.0005$ |
|---|---:|---:|---:|
| $(1.5,0.7,1.2)$ | 0.05762502 | 1.0007754 | 1.0001919 |
| $(1.5,0.7,0)$ | 0.03155228 | 0.9997124 | 0.9999256 |
| $(0,0,1.8)$ | 0.01877602 | 0.9996505 | 0.9999112 |
| $(0,0,0)$ | $1/(241920\pi^2)$ | 1.0000003 | 1.0000000 |

Run `python3 check.py` with NumPy. Twelve tests compare the direct momentum convolution with a discrete spatial Fourier transform of the Wick correlation. I also reran C4's original-link, reflection, block-multiplicity, Haar and temporal-Fourier controls. A three-generation host-dispatched PCP OS worker chain tested exact dispersion comparisons on the four-point momentum grid in each dimension, the nodal orders and rest coefficient, and the positive power inequalities used to localize the higher convolutions. The original driver and the revised final-read driver reproduced receipt SHA-256 `e481209e029b09217d28b7d18b464a1a56c5193379f544c28d626206b884a551`. The analytic arguments are in the proof. [Numerical checks](check.py) · [Guest arithmetic](worker.c) · [Expected guest output](checks.txt) · [Guest replay driver](../../../observable-normalization/transfer-increments/replay-guests.py)
