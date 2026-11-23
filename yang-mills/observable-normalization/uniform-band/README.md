# Uniform isolation of the first Wilson transfer band

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Consider the isotropic four-dimensional $SU(2)$ Wilson regulator on periodic even spatial cubes of side $L\ge8$, in the infinite-time vacuum. Write $S$ for the positive physical transfer divided by its largest eigenvalue, $S_c=S-P_{\rm vac}$, $t=(\beta/4)^4$, and $u=I_2(\beta)/I_1(\beta)$. Write $x$ for a spectral value of $S_c/t$. For small positive $\beta$, **with one coupling range and constants independent of $L$**, every $x$ satisfies
$$
 0\le x\le C\beta^2,\qquad\text{or}\qquad
 \left|x-\left(1-\tfrac7{24}\beta^2\right)\right|\le C\beta^4 .
$$
There are exactly $3L^3$ eigenvalues counted with multiplicity in the upper interval. The same spectral exclusion holds in the infinite-volume vacuum. At finite volume and in the infinite-volume vacuum the full dimensionless mass has the more precise uniform expansion
$$
 \Delta=-4\log u+2u^2-\tfrac{98}{3}u^4+O(u^6).
$$
The [momentum argument](momentum.md) gives the error estimate and the scope of the infinite-volume coefficient. All energies here are lattice energies at the strong end. The mass diverges on approaching this electric limit. A four-dimensional interacting continuum theory with a finite positive physical mass remains open.

Schor obtained isolated one-particle states in the full strong-coupling energy–momentum spectrum, following earlier work on the plaquette correlation. Münster computed the strong-coupling dispersion and mass to higher order. Here the issue is how to obtain a bound simultaneous in all periodic box sizes from the program's fixed-box expansion, whose stated remainder grows with volume. [Full energy–momentum spectrum (1984)](https://www.sciencedirect.com/science/article/pii/055032138490289X) · [Münster, Eqs. (26)–(28)](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf)

## Two distinct inputs

1. At **each fixed box**, B4's compressed physical transfer has three eigenvalues per spatial momentum in its first band. Its logarithm relative to $u^4$ equals $-2u^2 I+O_L(u^4)$. All lower transfer values are $O_L(u^6)$ by the electric tail and vacuum compression. With $u=(\beta/4)(1-\beta^2/24+O(\beta^4))$, this puts the upper scaled values at $b=1-7\beta^2/24$ up to $O_L(\beta^4)$, and the rest at $O_L(\beta^2)$. We use this only arbitrarily close to zero separately for each box. [Finite-box shell](../../transfer-operator/girth-shell/transfer.md) · [Fixed-box Taylor expansion](../../transfer-operator/girth-shell/joint.md)
2. For a bounded gauge-invariant spatial function $G$ on $m$ links let $C_j(z)$ be its connected autocorrelation at lag $j$ with the **same** complex coupling $z$ on all faces. B4's disk estimate gives a holomorphic function on $|z|<1/1024$ with $|C_j(z)|\le M_G=2\|G\|_\infty^2e^{2m}$ independently of $j$. The first observable is conjugated for a complex $G$; the coupling is never conjugated. To pass from open time to the vacuum, the finite-time functions form a bounded normal family. Their limits on positive real couplings follow from the simple transfer vacuum; uniqueness on an interval identifies the holomorphic limit. This is at fixed $j,L$. The common disk and bound survive. At positive real coupling $C_j$ is the $j$th moment on the centered vector $(G-\langle G\rangle)\Omega$. [Holomorphic bound including disconnected subtraction](../../transfer-operator/connected-rectangles/analyticity.md) · [Vacuum passage](../../transfer-operator/connected-rectangles/gap.md)

## All positive lags remove the volume factor

Fix $R=1/2048$, $A=(4/R)^4$. For real $\beta$ let $\nu$ be the transfer measure of that centered vector in the scaled coordinate $x$. For every $j\ge1$, $c_j(z)=C_j(z)/(z/4)^{4j}$ has a removable singularity at zero. Indeed the fixed-box spectral estimate gives $C_j(\beta)=O_{j,L,G}(\beta^{4j})$ on the positive axis, forcing the first $4j$ Taylor coefficients to vanish. On $|z|=R$, $|c_j(z)|\le M_G A^j$.

Use the polynomial $p_z(x)=x^2(x-b(z))$, $b(z)=1-7z^2/24$. It has a double zero near the lower spectral cluster and a simple zero at the predicted upper center. For $s\ge1$ form $F_s(z)$ by expanding $p_z(x)^{2s}$ and replacing $x^j$ by $c_j(z)$. On the positive real axis $F_s(\beta)=\int p_\beta(x)^{2s}d\nu$. Each fixed-box spectral alternative gives $|p_\beta(x)|=O_L(\beta^4)$. Thus $F_s$ has a zero of order at least $8s$. On the circle, $|b(z)|<2$, the powers of $x$ range up to $6s$, and the sum of absolute coefficients is at most $3^{2s}$. Hence $|F_s(z)|\le M_G(3A^3)^{2s}$ there. Apply the maximum modulus principle to $F_s(z)/z^{8s}$:
$$
 0\le F_s(\beta)\le M_G[3A^3(\beta/R)^4]^{2s},\qquad 0<\beta<R .
$$
Neither the fixed-box radius used to prove the Taylor zeros nor its constants enter this estimate. The factor $M_G$ may be enormous and may depend on the whole box. For each $\epsilon>0$, a positive mass at $|p_\beta|>3A^3(\beta/R)^4+\epsilon$ contradicts the bound as $s\to\infty$. Bounded gauge-invariant multipliers of the strictly positive vacuum are dense in the physical slice space. Centering them gives a dense set in its vacuum complement. The spectral projection outside the resulting closed set therefore vanishes on that complement. Zero, the value assigned to the vacuum in $S_c$, also satisfies the bound.

Set $e=3A^3(\beta/R)^4$. For $x\le1/2$, $b\ge3/4$ implies $x^2\le4e$; for $x\ge1/2$, $|x-b|\le4e$. For example $\beta\le2^{-54}$ gives $e\le3\cdot2^{-16}$. Consequently $1/2$ lies uniformly in the gap between the two scaled spectral sets. At each fixed $L$, the compact scaled operator is norm continuous for $\beta>0$, so the rank above $1/2$ stays constant throughout this interval. The fixed-box calculation near zero gives the rank $3L^3$. This argument concerns the entire centered space, including charged winding sectors.

For the infinite-volume vacuum, local reflected half-history tests generate the reconstructed Hilbert space. Their centered positive transfer measures on $[0,1]$ converge weakly from the finite tori at each sufficiently small fixed real $\beta$: all polynomial moments are finite collections of local correlations, which converge in the unique strong-coupling state. The support condition is closed and common to the volumes. It therefore passes also for half-history tests that occupy several time slices and then to their closed span. Nonzero upper-band weight already follows from the centered bare plaquette first moment $C_1/t\to1$ for its unnormalized trace with $C_0\to1$; the low branch alone would give $O(\beta^2)$. The finite-volume multiplicity is stated only before this limit. [Strong-coupling local passage and density](../../transfer-operator/connected-rectangles/gap.md)

[Finite-time projector](projector.md) · [Three-moment resolution bound](three-moments.md) · [Execution record and proof coverage](execution.md)
