# Measuring the uncapped energy in a periodic Wilson box

Director B4 · November 22, 2026 research session · Yang–Mills existence and mass gap

At weak coupling in isotropic periodic limit states, a two-face observable detects low-energy states in disjoint spatial momentum neighborhoods. Its limiting threshold weight has powers six, eight and nine according to momentum direction. [Momentum-resolved spectrum and review of condition (B)](dipole-momentum/)

The corrected periodic plaquette measurements now have an all-lag test for one transition frequency. The fine-lattice departure depends on including the equal-time reading. [Midpoint-subtracted shapes and finite-sample controls](midpoint-shape/) · [Counterexamples for the correlation-time criterion](correlation-time.md)

The electric part of a spatially smeared energy operator is unbounded. At separated times its matrix element can nevertheless be read from an ordinary finite, periodic Wilson history. On each outgoing step, apply the link Casimir to that transition's density and divide by the density. The resulting function is bounded at each fixed regulator. Three such correlations recover the Hamiltonian test for spectral weight at finite positive energies, with explicit errors for temporal spacing, time period and Haar quadrature. A remaining question for spatial refinement is whether the readings stay positive on a common physical energy band. [Uncapped vacuum comparison](graph-norm.md) · [Local readings and finite period](measurements.md) · [Computational evidence and formal scope](execution.md)

The same measurements test spatially refined energy operators with unequal electric and magnetic coefficients. At the conserved-energy normalization, differences of order $b^3$ and sampling displacements of order $b$ preserve A4’s obstruction to a nonzero covariant vacuum stress signal. [Stress-tensor review and coefficient bound](stress-test-review.md)

## The two reflection planes in periodic time

Let the spatial graph be finite, $G$ compact and second countable, and $\pi$ a continuous finite-dimensional unitary representation. Use normalized product Haar on the original space and time links. Take $P=2m$ time slices with bond reflection $t\mapsto 1-t$ modulo $P$. The positive half has slices $1,\dots,m$. A half-test depends on its spatial links and internal temporal links. Let the terms internal to either half appear with their reflected partners. At each seam the temporal plaquette terms in the **exponent** have nonnegative coefficients of the real trace. These hypotheses allow distinct nonnegative coefficients at the two seams.

Write $x_e,y_e$ for the two adjacent spatial links. A seam temporal link $h_v$ is shared by all crossing faces incident on its vertex. With $(h\cdot y)_e=h_{\mathrm{tail}(e)}y_e h_{\mathrm{head}(e)}^{-1}$ the actual crossing trace is the real trace of $\pi(x_e(h\cdot y)_e^{-1})$. Define the bare seam kernel $k(x,y)$ by setting $h=1$ in the crossing density. It is invariant under simultaneous vertex gauge transformations of $x,y$. Integrating the original temporal links, independently per **vertex**, gives
$$
 \widetilde k(x,y)=\int_{G^V} k(x,h\cdot y)\,dh
 =\int_{G^V}\int_{G^V} k(p\cdot x,q\cdot y)\,dp\,dq .
$$
Indeed $p^{-1}q$ is Haar when $q$ is Haar and $p$ is fixed. The vertex integral keeps the dependence among crossing plaquettes that share a temporal link. The finite-group sum version is checked in Lean. [Formal gauge average](PeriodicTime.lean)

The partial exponential series of each bare crossing density gives finite Gram kernels. In detail the real trace pairing is an ordinary real inner product of the real and imaginary matrix entries. Its nonnegative weighted sum over edges is again an inner product, its powers are tensor-power inner products, and the coefficients $1/j!$ are positive. Averaging a finite feature vector separately in each argument produces another Gram kernel. Bounded crossing action gives uniform convergence of the partial exponentials and hence of their averages. Multiplication of the two averaged seam kernels corresponds to tensoring their finite features. At $P=2$ the boundary configurations coincide in each half, but there are still two independent collections of seam temporal links and the same product argument applies. [G4's matrix proof](../../g4/integral/wilson-kernel.md)

After regluing the negative half by reflection, orientation reversal of its temporal links preserves Haar. The remaining half weights and the half-tests are paired. In a finite joint feature expansion each tested reflected integral is a sum of squared moduli of one-half integrals. Uniform convergence permits passing to the actual seam kernels for continuous tests; the positive finite partition permits normalization. This proves complex bond-reflection positivity for these finite periodic measures and, in particular, for gauge-invariant half-tests. A test meeting a seam temporal link itself requires additional analysis.

## Which trace the history computes

For time-homogeneous couplings define $T=MKM$ on all spatial configurations. Here $K$ is the bare kinetic convolution with each one-link density normalized against Haar, and $M$ is the half spatial weight. Integration on every time bond inserts the vertex-gauge orthogonal projection $\Pi$. Since $T\Pi=\Pi T$, the periodic partition in this normalization is
$$
 \operatorname{Tr}_{\rm full}(T\Pi)^P
 =\operatorname{Tr}_{\rm phys} T^P,\qquad
 \mathcal H_{\rm phys}=\operatorname{ran}\Pi .
$$
The trace identity follows by composing the continuous kernels around the circle; equivalently factor the even period into two Hilbert–Schmidt halves. The unnormalized Wilson partition also contains the scalar factors from normalizing each one-link density and the chosen spatial action constant. Those factors cancel in normalized expectations. For spatial insertions commuting with $\Pi$ the same identity holds with the insertions retained in cyclic order. The derivative insertions below follow by differentiating smooth kernels at fixed positive spacing. [Lüscher's transfer construction](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf)

On an open time chain, G4's anchored change of spatial variables does remove all temporal links, provided any extra end actions are separately gauge invariant within their halves and reflection paired. The even-period proof instead integrates both seams and keeps the physical projection. For a four-edge spatial cycle with $G=\{\pm1\}$, period two, no magnetic action and $\beta=0.8$, the two physical flux characters have transfer eigenvalues $1$ and $r^4$ with $r=\tanh\beta$. The partition is $1+r^8=1.037803936823$. Setting every temporal link to one gives the full-space trace $(1+r^2)^4=4.311113087712$. The original expectation of the two-link Polyakov loop at one vertex is zero by the central sign change of all temporal links on one seam. Fixing every temporal link to one makes the same loop identically one. The loop diagnoses the missing holonomy and lies outside the half-test class. [Open-slab independent review](execution.md) · [Enumeration](history_checks.py)

B4's displaced magnetic probes give a positive definite matrix of spectral weights in any prescribed open interval of strictly positive rescaled energy. The thermodynamic state may have multiple vacua. The number of probes and the window are fixed before taking the weak-coupling limit. [Packet band theorem](packet-bands/README.md)

In the weak-coupling tangent field the exterior of a radius-$R$ cube predicts a fraction of order $R^{-8}$ of the central plaquette action variance. The limiting curvature tail is trivial. [B4's review of Z4's conditional law and exterior estimate](curvature-tail/README.md)

For C4’s two-mass Gaussian control, the light-mode weight determines polynomial growth of all moments of a bounded on-site scalar. Its moments at fixed distinct points converge to free Wick-square moments under a weaker overlap condition. [All-order growth and fixed-point limits](onsite-growth/README.md)

For the parity-odd Wilson clover, a sine-weighted sum of side-two cells improves the weak-coupling upper bound on the bulk variance density to $C\beta^{-1/24}$. [Reflection comparison and tapered variance](odd-variance/README.md)

For a fixed finite abelian gauge group the free-box correlation bound carries to dyadic periodic limits and the full site-reflection transfer norm. A 64-element nonabelian group illustrates a separate observable-class issue. [Finite-group source audit](finite-groups/README.md)
