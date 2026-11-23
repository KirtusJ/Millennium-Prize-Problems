# A nonzero signal between disjoint gauge-invariant probes

Let $F,B$ be smooth scalar multipliers supported on disjoint link sets $I,J$. The first two derivatives at zero of $[\tau_t(F),B]$ vanish on smooth vectors. Its third derivative on that core is the bounded multiplier
$$
 4i\kappa^2
 \sum_{e\in I,a\in J}\sum_{i,j}
 (D_{ei}F)(D_{aj}D_{ei}V)(D_{aj}B).
$$
Indeed $[K,F]$, $K=-\kappa\sum D^2$, differentiates only links of $I$. The pure electric iterates also have support there. The first magnetic commutator $[V,[K,F]]=2\kappa\sum (D_{ei}F)(D_{ei}V)$ is multiplication. Commuting its electric derivative with $B$ gives the displayed coefficient after multiplication by $i^3$. The other possible term, $[V,[K,[K,F]]]$, differentiates only links in $I$ even when its coefficients depend on $J$, hence commutes with $B$. The principal symbol of $[K,[K,F]]$ has order at most two because $K$ is scalar. All derivatives here are strong on smooth vectors. A nonzero coefficient yields a nonzero order-three matrix element between suitable smooth vectors by ordinary Taylor expansion.

Take the bottom and top oriented horizontal plaquettes of one cube as $F,B$. Use the fundamental $SU(2)$ real normalized traces. Set the same one base link on each of these two faces to $\mathrm{diag}(e^{i\theta},e^{-i\theta})$ and all other cube links to the identity. The two plaquette holonomies have the same angle $\theta$; all four intervening vertical holonomies are the identity. This computation also applies inside a larger cubic box or torus of side at least three. Only the four vertical faces contain a link of each probe.

In the frame $T_j=i\sigma_j/2$ only $j=3$ contributes to the horizontal first derivatives. Each contributes $-\epsilon\sin(\theta)/2$, where $\epsilon$ is the oriented incidence on its horizontal loop. On a vertical face the two corresponding links are oppositely traversed, and have equal incidences on the horizontal loops. Their mixed derivative of $V=\lambda\sum(1-x_p)$ is $-\lambda/4$ in this frame. Thus the fundamental third derivative equals $-i\kappa^2\lambda\sin^2\theta$. For both probes replaced by the normalized adjoint trace, multiply by $(8\cos\theta/3)^2$. At $\theta=\pi/4$, the two coefficients in units of $i\kappa^2\lambda$ are $-1/2$ and $-16/9$. At $\theta=0$ both vanish. At $\theta=\pi/2$ only the adjoint coefficient vanishes. The nonzero multiplier is gauge invariant. Acting on a constant smooth gauge-invariant vector detects it in the physical Hilbert space as well. The Taylor coefficient is the third derivative divided by six.

An independent matrix calculation uses all three generators and differentiates each actual oriented word, including inverse letters. It repeats the same calculation after independent noncommuting gauge rotations at the eight vertices. A second check evaluates nested commutators with exact integer coefficients on unrestricted Fourier modes of an abelian chain. It confirms the time order $2d+1$ at the first three distances. The abelian model uses the potential $2\sum_j(1-\cos(\theta_j-\theta_{j+1}))$ and electric coefficient 2. The table gives the output on its constant vector for $ [\operatorname{ad}_H^n e^{i\theta_0},e^{i\theta_d}]$. [Executable controls](checks.py)

| Distance $d$ | First nonzero order $n$ | Distinct output modes | Sum of absolute integer coefficients |
|---|---:|---:|---:|
| 1 | 3 | 2 | 32 |
| 2 | 5 | 4 | 256 |
| 3 | 7 | 8 | 2048 |

These tests address finite-volume propagation. As a check on the gap inference, take the magnetic coefficient zero and electric coefficient $\kappa=b$ on a fixed finite cubic graph. Disjoint equal-time multiplication algebras on distinct links have exactly zero propagated commutator at every time. The fundamental plaquette applied to the constant vacuum nevertheless has energy $3b$ in the half-speed $SU(2)$ convention. A finite propagation bound alone cannot give a uniform positive mass.
