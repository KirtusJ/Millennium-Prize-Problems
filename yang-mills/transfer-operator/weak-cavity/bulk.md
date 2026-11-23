# A bulk magnetic reading sees the gap closing

Choose odd $N\to\infty$, $M=N+1$, $b=N^{-1/2}$, $a=\eta b$, and $g=N^{-100}$. The isotropic case is $\eta=1$. Choose spatial elementary faces normal to axis 3 within a fixed physical displacement of the center of the box. Use the centered gauge-invariant plaquette
$$
 O_p=\frac{2}{g^2 b^4}\big[(1-\tau(U_p))-\langle1-\tau(U_p)\rangle\big],
$$
where brackets are the infinite-time vacuum of the actual finite-space compact Wilson transfer. For $t>0$, at two such faces a physical displacement $r$ apart and separated by $k$ steps with $ka\to t$, the limit of the connected covariance is
$$
 2D\,W(t,r)^2,\qquad
 W(t,r)=\frac{t^2-r_1^2-r_2^2+r_3^2}{\pi^2(t^2+|r|^2)^3},\qquad D=\dim G .
$$
At coincident spatial positions this gives a positive signal at every positive time even though the six lowest excited box energies above the vacuum converge to zero. No division by a measured rest-energy factor appears.

## The free finite-box reading

In the oscillator vacuum the one-color curvature covariance across the two faces is
$$
 L_{pq}(k)=\sum_{j_1,j_2\ge1,\ j_3\ge0}
 h_j(p)h_j(q)\,\frac{\ell_{j_1}+\ell_{j_2}}{2\nu_j}e^{-k\theta_j},
 \qquad h_j(p)=s_{j_1}(p_1)s_{j_2}(p_2)f_{j_3}(p_3).
$$
Each index is less than $M$. The signed curl row in the product mode is proportional to $(-\sqrt{\ell_{j_2}},\sqrt{\ell_{j_1}},0)$, already transverse. This yields the numerator without a gauge-dependent choice of polarization. The vacuum and the traced insertions are invariant under root conjugation, so inserting the color projection on each time bond gives the same correlation as the anchored Gaussian calculation. The vacuum coordinates at multiple times are jointly Gaussian by the Mehler kernel, or by multiplying the vacuum-normalized kernels between Gaussian end vectors. Wick contraction of the two centered sums of $D$ color squares gives $2D L_{pq}(k)^2$. The [compact transfer and insertion estimates](uniform.md) transfer this formula to the limiting Wilson covariance after the factor $b^{-8}$.

For $p,q$ at bounded physical offsets from the center, put $\xi_i=\pi j_i/(Mb)$. The mesh tends to zero and the lattice upper frequency tends to infinity. For bounded $\xi$,
$$
 \omega_j/b\to |\xi|,\quad \nu_j/b\to|\xi|,\quad
 k\theta_j\to t|\xi|,\quad
 (\ell_{j_1}+\ell_{j_2})/b^2\to\xi_1^2+\xi_2^2
$$
in the sense of convergence along each sequence with convergent rescaled frequencies. To handle the standing-wave factors, take the reference face based at $(M/2-1,M/2-1,M/2-1)$. In the two tangential axes the phase at that face is $j_i\pi/2$; the normal cosine phase differs from $j_3\pi/2$ by $-\pi j_3/(2M)$. Each bounded physical offset adds its usual phase $\xi_i r_i$ up to vanishing rounding errors on compact frequency sets. Average the products on the eight even/odd submeshes separately. Twice a sine product or twice a cosine product averages over the two parities to the cosine of the phase difference. The exceptional normal zero index is one mesh layer and gives a vanishing contribution. The bound $\theta_j\ge c_\eta b|\xi|$ follows from the sine lower bound on $[0,\pi/2]$ and the positive minimum of $\operatorname{arsinh}(x)/x$ on the bounded range here. The remaining frequency factor after rescaling is bounded by $C|\xi|$, yielding uniformly summable Riemann tails with exponential decay at positive physical time. These facts prove
$$
 b^{-4} L_{pq}(k)\ \longrightarrow\
 \int_{\mathbb R^3}\frac{d^3\xi}{(2\pi)^3}
   \frac{\xi_1^2+\xi_2^2}{2|\xi|}\,e^{-t|\xi|+i\xi\cdot r}=W(t,r).
$$
The Fourier transform with numerator one equals $1/[4\pi^2(t^2+|r|^2)]$ by radial integration. Applying $-\partial_1^2-\partial_2^2$ gives the displayed expression. At $r=0$ it is $1/(\pi^2 t^4)$. Thus the vanishing box gap has a local spectral consequence at interior points receding from every wall. A flight time to the boundary grows as $Nb$ on these boxes.

## Limiting positive spectral measure

For the same central face at both ends, interpolate noninteger physical lag by spectral calculus. Monotonicity squeezes the Laplace transform between the neighboring integer-lag readings, which have the same limit. Write $\rho_N$ for the positive measure in physical energy $-a^{-1}\log(\lambda/\lambda_0)$ of $O_p\Omega$. For any fixed $t_0>0$, the tilted finite measures $e^{-t_0 E}\rho_N(dE)$ converge weakly to $e^{-t_0 E}\rho(dE)$ with
$$
             \rho(dE)=\frac{2D}{7!\,\pi^4}E^7\,dE,\qquad E\ge0.
$$
Indeed the tilted masses converge at $t_0$, the tails are bounded by the readings at $t_0/2$ times $e^{-t_0 A/2}$ above $E=A$, and each subsequential limit is uniquely determined by its Laplace transform. The gamma integral is checked in Lean. Every fixed interval $(0,A)$ has positive limiting mass and zero endpoint atoms, so its original compact reading converges to $2D A^8/(8!\pi^4)$. The tilt is the squared-norm measure of a vector propagated by half the positive time $t_0$. This yields a finite-norm reading with spectral support arbitrarily close to zero. The total unweighted mass need not stay finite as the cutoff is removed. [Formal Laplace integral](WeakCavity.lean)

## Higher time-separated moments

Take $g=e^{-N}$ for this statement. At finitely many strictly ordered times and bounded interior displacements, every joint moment of the centered observable converges to the Gaussian Wick-square moment. For each color pair the cross covariance is $W(t_j-t_i,r_j-r_i)$ for $j>i$. Sum all pairings of two legs per insertion with no pair within one insertion, identify the color along each pairing, and sum each independent color from one to $D$. This follows at finite regulator in the Gaussian comparison by Wick's rule; the volume estimate permits the compact-to-Gaussian replacement for each fixed number of insertions. Exact vacuum centering removes the divergent same-point contractions.

For three such faces the result is $8D W_{12}W_{23}W_{13}$. At a common spatial point it is positive. Its square divided by the product of the three pairwise two-point functions is $8/D$ whenever the denominator is nonzero. Thus a separated connected three-point reading survives even for this free-curvature limit. This supplies a control for scalar-interaction tests and fixes both the spacetime dependence and the color factor. The simple-group singlet spectrum, the closing finite-box gap and the continuous interior spectral weight hold in the stated scaling regime. Constructing the interacting continuum limit with positive physical mass requires another trajectory and further estimates.

D4's comparison of cube and dual-star triangles imposes a cancellation of a Gaussian contribution. The same-point magnetic triangle above gives the absolute normalization of one surviving free contribution on an open, growing spatial box. The twist, position and scalar combination enter when comparing the two tests. [D4's compact response and assumptions](../../spectral-support/dual-scalar/)
