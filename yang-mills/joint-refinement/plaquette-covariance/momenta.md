# A deterministic large Fourier subspace of unfiltered local readings

Take $N$ divisible by four, $N\ge8$. Mark all $xy$ plaquettes with base in $(4\mathbb Z/N)^3$, and let $n=N/4$. These are individually unfiltered elementary plaquettes. The spacing four permits the [same private two-link pair](README.md) for each marked face simultaneously. For any complex coefficient array $c$ on this $n^3$-site packing, the variance innovation at each endpoint is at least $\delta\|c\|_{\ell^2}^2$. Conditioning on the coarse algebra may mix momentum sectors. The following momentum selection is performed on the **coefficient array of raw readings** before projection.

Choose $0<\kappa<2$. Permit all arrays whose unitary Fourier transform is supported on the preassigned set
$$
 \mathcal K_\kappa=\{q:\ |1-e^{iq_j}|\ge\kappa\text{ for }j=1,2,3\},
 \qquad q_j=2\pi k_j/n .
$$
For the raw covariance on this sublattice the longitudinal sequences for all transverse Fourier tests are subsequences at spacing four of the positive, monotone sequences in the [spatial transfer proof](README.md). Their cyclic total variation is at most twice the contact value. Summation by parts gives
$$
 |1-e^{iq_j}|\,\widehat G(q)\le2c_0(q_\perp).
$$
The contact is the transverse structure factor on a fixed longitudinal section. Iterating in the three coordinates gives $\widehat G(q)\le (2/\kappa)^3K$ on $\mathcal K_\kappa$. Plancherel and contraction by coarse subtraction give this same Gram ceiling for the residuals. In precisely the same coefficient norm the private-pair floor is still $\delta$. Thus the [joint coarse-coupling and transmission inequalities](README.md) hold on this range with $\gamma_\kappa=(\delta/K)(\kappa/2)^3$ at any lag of at least two steps.

This space has exactly $|\mathcal K_\kappa|$ dimensions, by the innovation floor. Its fraction of the packing tends to $[1-(2/\pi)\arcsin(\kappa/2)]^3$. For example, $\kappa=0.1$ retains about 90.7% of the coefficient dimensions with an $N$-independent deficit. The side need not be divisible by eight, but this particular Fourier construction uses divisibility by four. The physical wavelengths tested become short on refinement. The auditor’s fixed-index wave and the zero mode are eventually excluded. Sending $\kappa$ to zero removes the uniform deficit guaranteed by this argument. [Ising countermodel and physical clock](audit.md) · [Raw zero mode and unresolved isotropic bound](pressure.md)
