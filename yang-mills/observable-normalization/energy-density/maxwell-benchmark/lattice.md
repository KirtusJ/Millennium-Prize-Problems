# Sharp time and positive time on the infinite free spatial lattice

Use Z4’s quadratic Maxwell Hamiltonian on the infinite cubic spatial lattice. Sample the electric term at each link center and the magnetic term at each face center. Measure the two fields in physical units. The centered observable is the mesh-volume sum of the indicated energy densities against the spatial test. At a single momentum below, $C_b(t,p)$ is the translation-invariant two-point spectral density per unit spatial Fourier measure. There is no spatial finite-volume limit implicit in a single sampled Fourier mode.

For external momentum $p$ in the Brillouin zone, integrate $k$ over that zone. Put $\widehat k_i=(2/b)\sin(bk_i/2)$, $\ell=p-k$, $r=|\widehat k|$, $s=|\widehat\ell|$, and $c=\widehat k\cdot\widehat\ell/(rs)$. The plane-wave factors at link and face centers reduce the curl on transverse modes to $i\widehat k\times$. The two Wick weights are therefore $rs(1\pm c)^2/4$, multiplied by $e^{-t(r+s)}$ and integrated against $d^3k/(2\pi)^3$. The cross weight vanishes. Evaluate the sine at the **unfolded** $\ell=p-k$. Reducing it componentwise to the zone requires the staggered link and face phases. A reciprocal-lattice shift multiplies the electric polarizations by the diagonal signs of the three link offsets and the magnetic polarizations by the signs of the complementary face offsets. Using the unfolded partner includes those signs.

For each fixed $p$ and $t>0$, extend the integrand by zero outside the zone. Pointwise convergence gives the photon pair integrand. It is bounded by $|k|(|p|+|k|)e^{-2t|k|/\pi}$ since $r\ge2|k|/\pi$ in the zone. Dominated convergence proves the two continuum positive-time formulas for this regulator.

## Leading sharp-time coefficients

Write $\theta=bk$, $u_i=2\sin(\theta_i/2)$, $v_i=p_i\cos(\theta_i/2)$ and $P_u$ for orthogonal projection onto $u^\perp$. Then
$$
\lim_{b\downarrow0} b C_{b,T}(0,p)=A(p)
 =\int_{[-\pi,\pi]^3}\frac{|P_u v|^4}{16|u|^2}\frac{d^3\theta}{(2\pi)^3},
\qquad
\lim_{b\downarrow0} b^5 C_{b,U}(0,p)=6 .
$$
Indeed the other dimensionless photon vector is $u'=2\sin((bp-\theta)/2)=-u+bv+O(b^2)$, componentwise at fixed $\theta,p$. Away from $u=0$,
$$
(1+c)/b^2=\left|u/|u|+u'/|u'|\right|^2/(2b^2)
 \longrightarrow |P_u v|^2/(2|u|^2).
$$
For the scalar, $c\to-1$ and the limiting integrand is $|u|^2$ with cube mean six.

The bound $|u+u'|\le b|p|$ controls the region near a zero of either photon frequency. When $|u|\ge2b|p|$, use $|u'|\ge |u|/2$ and $2|u||u'|(1+c)\le |u+u'|^2$. When $|u|<2b|p|$, use $1+c\le2$ and $|u'|\le |u|+b|p|$. Both regions bound the rescaled total-energy integrand by a universal constant times $|p|^4/|u|^2$, integrable in three dimensions. The scalar rescaled integrand is uniformly bounded on the cube. This proves convergence and $A(p)\le C|p|^4$. For $p\ne0$ a positive-volume set of sufficiently small $\theta$ transverse to $p$ has $P_u v\ne0$. Thus $A(p)>0$.

For any nonzero Schwartz test the leading variances follow by integrating the coefficients against $|\widehat f(p)|^2d^3p/(2\pi)^3$. In particular the scalar coefficient is $6\|f\|_2^2$. To justify sampling, first project the test onto the physical Brillouin zone, where spatial stationarity gives the diagonal momentum integral. With staggered centers the omitted reciprocal translates can have component-dependent unit phases. The per-momentum Gram norm for all six squared field components is bounded by $C b^{-5}$ using the two oscillator frequencies, bounded polarization factors and the finite zone volume. For $p$ in the first zone the sum of the absolute Fourier tails over nonzero translates is $O_N(b^N)$ uniformly for every $N>3$, by Schwartz decay. The omitted vector thus has squared norm $O_N(b^{2N-8})$ including the first-zone volume. Cauchy–Schwarz controls its cross terms, and time damping only decreases its norm. This extends the sharp- and positive-time limits to $C_c^\infty$ tests as well. A fixed scalar admixture gives the $b^{-5}$ divergence. One of order $b^2$ changes the coefficient at order $b^{-1}$.

The free infinite spatial lattice, the free continuum, and the compact interacting finite-box calculation have different ground states. The [finite-box electric expansion](../plaquette-response/) and the present calculation test distinct regimes.
