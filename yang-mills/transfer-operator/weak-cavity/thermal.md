# Periodic Wilson time, the free pressure, and the cost of the global singlet

The **physical** finite-temperature partition function with vacuum energy removed is $Z_g^{\rm phys}(k)=\operatorname{Tr}_{\rm phys}(T_g/\lambda_g)^k$. Closing the original temporal Wilson bonds gives this trace after the per-step vacuum normalization. For comparison let $Z_g^{\rm anch}(k)$ retain the root color before the last Haar projection. At small $g$ on the joint trajectories both traces agree to relative $o(1)$ with their corresponding finite-box Gaussian traces whenever $k\ge2$ grows at most polynomially and $k(gN^{18}+e^{-cN^5})\to0$. This controls the whole thermal spectrum. Operator-norm convergence by itself would not suffice for the trace. [Original Wilson integral](../periodic-time/) · [Kernel bounds used below](uniform.md)

To prove the trace comparison, truncate the kernels to $|x|,|y|,|z|\le N^4$ before integration in the tree noises. With each operator divided by its own vacuum eigenvalue, both truncated and untruncated operators have norm at most one: dominate the absolute value of the truncated kernel by the full positive kernel. The Hilbert–Schmidt norm of the discarded part is at most $e^{-cN^5}$, and that of a full or retained factor is at most $e^{C N^3\log N}$. Telescoping $k$ factors, estimating the discarded factor and one other in Hilbert–Schmidt norm, bounds the absolute trace error by $k e^{-c'N^5}$. Inserting the last invariant projection costs at most one in this estimate. On a closed path the retained compact normalized kernel is pointwise between $e^{-C\epsilon}$ and $e^{C\epsilon}$ times the retained Gaussian normalized kernel, with $\epsilon=gN^{18}+e^{-cN^5}$. This applies to every factor including a bond closing on an adjoint rotation of the initial configuration. Multiply on the path and integrate, then average the rotation for the physical trace. Both untruncated reference traces include a vacuum term one, so the discarded absolute errors are also harmless in the relative comparison.

Put $q_j=e^{-k\theta_j}$ with one factor per transverse spatial mode and define
$$
 Z_N(h)=\prod_j\det(I-q_j\operatorname{Ad}h)^{-1}.
$$
This is positive since complex eigenvalues of the real orthogonal adjoint action come in conjugate pairs, and all real factors are positive. The anchored Gaussian trace is $Z_N(1)$; the physical one is its Haar integral. On $Mb=R_0$ fixed and $ka\to T>0$, the full physical heat trace therefore converges to the same group integral with $q_j=e^{-T\pi|j|/R_0}$, retaining exactly $l(j)-1$ modes at each index with at least two positive entries. The product converges uniformly in $h$ by $q_j\le e^{-c_{T,R_0}|j|}$. This is the singlet Fock heat trace on the finite physical cavity. Here $T$ denotes the Euclidean time period, or inverse temperature.

In this fixed physical cavity the first two thermal corrections as $T/R_0\to\infty$ are $6e^{-2\sqrt2\pi T/R_0}$ and $6e^{-(\sqrt2+\sqrt3)\pi T/R_0}$. Each coefficient counts a different six-dimensional singlet space. This gives a multiplicity check with closed-time histories independently of the six local probes. [First two singlet shells](spectrum.md)

## Growing physical boxes

Now let $R=Mb\to\infty$ on $b=N^{-1/2}$ with $ka\to T>0$. Then
$$
 R^{-3}\log Z_g^{\rm phys}(k)\longrightarrow\frac{D\pi^2}{45 T^3},\qquad
 T^{-1}R^{-3}\log Z_g^{\rm phys}(k)\longrightarrow\frac{D\pi^2}{45 T^4}.
$$
The second expression is vacuum-subtracted pressure. The two transverse polarizations give the free gluon Stefan–Boltzmann coefficient. The bare coupling here is fixed by the explicit weak trajectory. Continuum thermal results at physical Yang–Mills couplings address a different scale-setting question. [Boyd et al., SU(3) equation of state](https://doi.org/10.1103/PhysRevLett.75.4169)

There is also a multiplicative asymptotic for the cost of imposing the last Gauss law. Write $J(0)d^D X$ for the tangent density of normalized Haar in orthonormal coordinates for the trace metric, and $\mathcal Q(X)=-\operatorname{Tr}_{\mathfrak g}(\operatorname{ad}_X^2)$. For the two **original compact** traces,
$$
 \frac{Z_g^{\rm phys}(k)}{Z_g^{\rm anch}(k)}
 \ \sim\ |Z(G)|\,J(0) R^{-3D/2}
          \int_{\mathfrak g}e^{-\mathcal Q(X)/(6T^3)}\,d^D X .
$$
Elze, Greiner and Rafelski treated global color singletness by exact group projection in a finite quark–glue partition function. Here the comparison starts with original Wilson history traces and computes the limiting prefactor for a compact simple gauge group with the stated Haar convention. [Elze, Greiner and Rafelski](https://doi.org/10.1016/0370-2693(83)91564-2)

Only the finite center has identity adjoint action. In SU(2) with the ordinary Wilson half-trace, $J(0)=1/(2\pi^2)$ and $\mathcal Q(X)=8|X|^2$. The coefficient of $R^{-9/2}$ is $3\sqrt3\,T^{9/2}/(8\sqrt\pi)$. Thus retaining charged root states gives the correct extensive pressure but an incorrect subextensive term, even on this free trajectory.

For the proof let $w_j=q_j/(1-q_j)^2$, $S_N=\sum_j w_j$. In the positive octant the rescaled frequencies have mesh $\pi/R$, and the multiplicity is two away from the coordinate planes. The same bounds as for the bulk covariance give
$$
 R^{-3}S_N\to 2\int\frac{d^3p}{(2\pi)^3}\frac{e^{-T|p|}}{(1-e^{-T|p|})^2}=\frac1{3T^3}.
$$
The integrand has an integrable $|p|^{-2}$ singularity. Uniformly below $|p|<u$, summing in radial shells of index width one bounds the normalized sum there by $Cu+C/R$. The lower-dimensional coordinate planes give a vanishing contribution, also at zero by this bound. At high frequencies the tails decay exponentially. The same argument with $-\log(1-e^{-T|p|})$ gives the stated limit for $R^{-3}\log Z_N(1)$; its singularity at zero is only logarithmic. Expanding the positive series and integrating $r^2 e^{-nTr}$ gives respectively $\zeta(2)$ and $\zeta(4)$ with the displayed constants.

If the adjoint eigenphases of $h$ are $\phi_\alpha$, the log of the anchored integrand loss is
$$
 \log[Z_N(1)/Z_N(h)]=\tfrac12\sum_{j,\alpha}\log(1+2w_j(1-\cos\phi_\alpha)).
$$
At $h=\exp(X/R^{3/2})$, this tends to $\mathcal Q(X)/(6T^3)$ because $\max w_j=O(R^2)$ and $S_N=O(R^3)$. The quadratic Taylor remainder is bounded by the maximum of the small summands times their sum. For domination, a fixed nonempty physical momentum annulus contains at least $cR^3$ modes whose $w_j$ stay within fixed positive bounds. On these terms the log is bounded below by $c\sum_\alpha (1-\cos\phi_\alpha)$. This last sum controls the squared distance to the center by its positive Hessian there and compactness elsewhere. Thus center neighborhoods of radius $O(R^{-3/2})$ account for the integral; dominated convergence in scaled normal coordinates gives the constant. The compact-to-Gaussian trace comparison already gives relative error $o(1)$ for both traces. No hypothesis about symmetry breaking or a chemical potential is needed.
