# A physical-time kernel and an upper test for the physical gap

For a lattice contour $C$, let $J_{C,i}(\theta)=\sum_e\epsilon_e e^{i\theta\cdot x_e}$ over its edges parallel to the positive $i$-axis, using the base of the positively oriented bond also for a reversed edge. Each color has the same circulation covariance. A face filling $S$ obeys $d^*S=J_C$; the closed current has zero lattice divergence. Pair C4's exact-curvature projector with two fillings. Its two exterior derivatives move onto the fillings, leaving $\overline{J_C}\cdot J_D$ over the scalar lattice Laplacian symbol. The temporal Fourier coefficient of $(2\cosh\omega-2\cos q)^{-1}$ is $e^{-|k|\omega}/(2\sinh\omega)$, by summing the geometric series. Thus
$$
 K^{\rm lat}_{CD}(k)=\int_{[-\pi,\pi]^3}
 \overline{J_C(\theta)}\cdot J_D(\theta)\,
 \frac{e^{-|k|\omega(\theta)}}{2\sinh\omega(\theta)}
 \frac{d^3\theta}{(2\pi)^3},\qquad
 \cosh\omega=1+2\sum_{i=1}^3\sin^2(\theta_i/2).
$$
Identical centering of oriented bonds cancels the componentwise phase. Pure connectors from a basepoint cancel in this abelianized current.

**Space and time scaling.** For contours following a fixed dyadic physical polygon and $\theta=bp$, the Riemann sum $b J_{C_b}(bp)$ tends to $j_C(p)=\oint_C e^{ip\cdot x}dx$, with norm at most the polygon length. On the Brillouin cube, $\omega(bp)\ge c b|p|$ by the sine bound and compactness of the argument of $\operatorname{arsinh}$. For $k=\lfloor t/b\rfloor$, $t>0$, the transformed integrand, extended by zero, is bounded by $c_{C,D}e^{-c't|p|}/|p|$ at all sufficiently small meshes. At every $p\ne0$, $\omega(bp)/b\to |p|$. Fourier inversion of the radial exponential and dominated convergence give
$$
 K_{CD}(t)=\int_{\mathbb R^3}\overline{j_C(p)}\cdot j_D(p)
   \frac{e^{-t|p|}}{2|p|}\frac{d^3p}{(2\pi)^3}
  =\frac1{4\pi^2}\oint_C\oint_D\frac{dx\cdot dy}{t^2+|x-y|^2}.
$$
For $C=D$, this is strictly positive whenever the contour defines a nonzero current. Finite Wick contractions across distinct times now have finite limits.

**Exact square.** Let $C$ be a square of side $R$. Perpendicular sides have zero dot product. For parallel sides integrate $2\int_0^R(R-u)/(s^2+u^2)\,du=I_R(s)$, where
$$
 I_R(s)=\frac{2R}{s}\arctan(R/s)-\log(1+R^2/s^2),\qquad
 K_R(t)=\frac{I_R(t)-I_R(\sqrt{t^2+R^2})}{\pi^2}.
$$
The difference under the integral is strictly positive. It gives $K_R(t)\sim R/(\pi t)$ at zero and $K_R(t)\sim R^4/(\pi^2t^4)$ at infinity. The same positive integral has denominator $(t^2+u^2)(t^2+u^2+R^2)$. Replacing $t$ by $\lambda t$, $\lambda\ge1$, enlarges it by at most $\lambda^4$. Thus $K_R(\lambda t)\ge\lambda^{-4}K_R(t)$ for every $t>0$. This comparison does not require fitting a long-time power law.

Write $C_{W,j}(t)=\operatorname{Cov}(W(0),W(\lfloor t/b_j\rfloor))$. Centered quadratic Wick contraction across the times yields
$$
 \beta_j^2 C_{W,j}(t)\to C_2(t)=\tfrac32 K_R(t)^2.
$$
Three choices of normalization now give measurable differences. The mean tends to one, so $C_{W,j}(t)/(\mathbb EW)^2\to0$. Dividing by $C_{W,j}(u)$ at any fixed $u>0$ yields $K_R(t)^2/K_R(u)^2$. The equal-time comparison differs: for every $u>0$, $\liminf_j\beta_j^2 C_{W,j}(0)\ge C_2(u)$ by positivity of the transfer; sending $u\downarrow0$ gives infinity. Thus the sharp-time correlation coefficient tends to zero. These conclusions concern the original signed fundamental trace.

**Low energies.** Use $E=|p|$. The one-color current has scalar spectral density
$$
 r_C(E)=\frac{E}{2(2\pi)^3}\int_{S^2}|j_C(E\omega)|^2\,d\omega .
$$
For a square of oriented area $R^2 n$, the leading current is $i R^2(n\times p)$ up to an overall orientation sign. The integral of $1-(n\cdot\omega)^2$ is $8\pi/3$. Reality of the contour makes the squared norm even, hence $r_R(E)=R^4E^3/(6\pi^2)+O_R(E^5)$. The quadratic density is $(3/2)r_R*r_R$. For the order-sensitive observable of three perpendicular squares below it is $6r_R*r_R*r_R$. Integrating over positive energies up to $\epsilon$ gives respectively
$$
 \frac{3R^8}{2\pi^4\,8!}\epsilon^8(1+O_R(\epsilon^2)),\qquad
 \frac{6R^{12}}{\pi^6\,12!}\epsilon^{12}(1+O_R(\epsilon^2)).
$$
The constants follow by integrating products of monomials on a simplex, with a factor $3!$ per single-current density.

**From a limiting measure to actual regulated excitations.** Center the finite-cutoff observable in its transfer vacuum. Call its spectral measure in physical units $\nu_j$, including the stated bare scaling. Restrict to positive transfer eigenvalues; zero eigenvalues have no contribution after a strictly positive time. For $s>0$ the finite measures $e^{-2sE}\nu_j$ converge weakly. Their total masses converge by the reading at $2s$, and their tails above $M$ are bounded by $e^{-sM}\int e^{-sE}d\nu_j$. Laplace readings at $2s+u$ uniquely identify every subsequential limit as the corresponding tilt of the density above. The physical spectral mass on each bounded positive interval with continuity endpoints therefore converges, also after removing the tilt there. A small interval strictly inside $(0,m)$ has positive limiting weight for every $m>0$. Eventually the finite box has an excited eigenvalue in that interval, so its lowest excited physical energy tends to zero on the chosen sequence. Centering removes the unique vacuum of the positive finite-box kernel. This calculation gives no uniform gap statement on other trajectories.

A second finite-regulator test uses only two late readings of the *unscaled* ordinary trace. If all excited physical energies are at least $m$, the ratio $C_{W,j}(2t)/C_{W,j}(t)$ is at most $e^{-m t}$ for grid-aligned times. The limit of this measured ratio is at least $2^{-8}$. Given any $m>0$, choose a dyadic $t>8\log(2)/m$; for all sufficiently fine members of the sequence the two readings exclude that gap. More generally the effective energy from $t,\lambda t$ is asymptotically at most $8\log(\lambda)/((\lambda-1)t)$. The upper bound is attained to leading order for large $t$ at fixed $\lambda>1$. [Oriented observable](singlet-sector.md) · [Transfer bridge](../positive-time/)
