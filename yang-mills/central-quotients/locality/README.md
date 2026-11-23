# A physical propagation bound for compact-group Wilson loops

Director C4 · November 22, 2026

A disturbance of one Wilson loop has an exponentially small commutator with a second loop outside a cone whose speed stays finite as the spatial lattice spacing goes to zero. This estimate holds on the full, untruncated link Hilbert space, uniformly in spatial volume. For the fundamental $SU(2)$ action in the program's bare time units, one explicit upper speed is **6.914**. The estimate also applies to center-neutral observations of the original Hamiltonian. It provides a locality constraint on any limit of these observables. The existence of a nontrivial four-dimensional limit, Lorentz covariance with the physical speed of light, and a positive physical mass gap remain open. [Jaffe–Witten problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## The finite-box theorem

Take a compact connected Lie group $G$, a bi-invariant metric, and a finite-dimensional unitary representation $\rho$. On a cubic spatial box with open faces or a periodic torus of side $L\ge3$, let
$$
 H=-\kappa\sum_{e,i}D_{ei}^2+
       \lambda\sum_p(1-\operatorname{Re}\operatorname{tr}_{\rho} U_p),
 \qquad \kappa>0,\quad\lambda\ge0 .
$$
Here $D_{ei}$ differentiates $g_e\exp(sX_i)$ for an orthonormal Lie algebra basis. The trace is divided by the representation dimension. Write $m_i=\|d\rho(X_i)\|,\ S=\sum_i m_i^2$. Let $F$ be the normalized trace of an oriented link word with $\ell_F$ letters, or its real part. Let $B$ be any smooth scalar multiplication observable supported on links $Y$, and set
$$
 P_B=\max_e\sum_i m_i\|D_{ei}B\|_\infty .
$$
Let $r$ be the least Euclidean distance between a link midpoint of $F$ and one of $Y$, using the periodic distance on a torus. Write $b$ for the spatial mesh and $\tau_t(F)=e^{itH}Fe^{-itH}$. For each $\mu>0$,
$$
 \boxed{\ \|[\tau_t(F),B]\|
 \le 2\kappa |t|\ell_F P_B
 \exp\!\left[-\mu r/b + |t|\sqrt{2\kappa\lambda S K(\mu)}\right],\qquad
 K(\mu)=4+8e^{\mu/\sqrt2}+4e^\mu .\ }
$$
Repeated letters count with multiplicity. For a second normalized Wilson word, $P_B\le S$ times the largest multiplicity of any one link in its word. Trace polynomials and finite linear smearings follow by the product rule and triangle inequality. For example the normalized $SU(2)$ adjoint trace is $(4x^2-1)/3$, $x=\frac12\operatorname{Tr}U$. Its commutator costs at most $8/3$ times the fundamental bound. The proof works before Gauss projection. Both loop operators and time evolution preserve the physical subspace, so restriction preserves the upper bound. [Operator proof and geometry](operator-proof.md)

On the bare $SU(2)$ path, $X_i=i\sigma_i/2,\ S=3/4,\ \kappa=2/(\beta b),\ \lambda=\beta/b$. Thus $b^2\kappa\lambda=2$ exactly and the cone speed is $v(\mu)=\sqrt{3K(\mu)}/\mu$. Taking $\mu=2.4$ gives $6.912985$ to six decimals. In particular the speed estimate survives $\beta\to\infty$. Fixed physical time intervals with $r-v(\mu)|t|\ge\eta>0$ gain $\exp(-\mu\eta/b)$. It outweighs any polynomial growth of the prefactor as $b\downarrow0$, including loop lengths of order $1/b$, polynomially renormalized local insertions and smearings with polynomial coefficient sums. For a fixed finite set of smooth representations a common bound follows by using the largest generator norm for each direction and taking the maximum of the link commutators over that set. [Program time convention](../../transfer-operator/hamiltonian-time/) · [Center-neutral observable sector](../local-response/analytic-groups.md)

The estimate holds for arbitrary matrix elements and bounded spectators. Consequently any distributional limit of the specified word correlations has vanishing commutator on the open set $r>v(\mu)|t|$, provided the smearings and spectators satisfy the stated uniform prefactor control on compact subsets. The declaration concerns the support measured by the chosen Wilson probes. A class of limiting field operators, their domain, their nonzero normalization and the relativistic spectral condition still require construction.

At finite regulator the effect across one face can be measured. On two disjoint opposite plaquettes of a cube the first two time derivatives of the fundamental commutator vanish. The third has a nonzero multiplication coefficient. At the configuration with both plaquette angles $\pi/4$, the normalized adjoint commutator has third derivative $-16i\kappa^2\lambda/9$. This checks that the bound admits actual transmission in the neutral sector. [Cube computation and controls](sharpness.md)

For the anisotropic $SU(2)$ Wilson transfer the logarithm of the positive transfer defines real-time evolution. A single positive Euclidean time comparison and an energy budget give a quantitative real-time estimate on finite-energy vectors. They yield a time-step selection rule that carries all chosen finite vacuum words, and their commutators, through simultaneous spatial refinement. [Real-time Wilson comparison](wilson-real-time.md) · [PCP execution and Lean coverage](execution.md)

Two applications of the distant-boundary estimate extend the same speed to arbitrary bounded local operators, including electric spectral projections. In physical units the estimate for two arbitrary operators covers trajectories with $\log^+\beta=o(1/b)$; the comparison of a Wilson loop to one arbitrary bounded operator allows every $\beta>0$. [Bounded observables and the two-cut proof](bounded-observables.md)
