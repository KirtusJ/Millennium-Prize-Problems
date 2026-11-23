# Uniform exponential tails and the original plaquette action

Let $Y_p=\beta(1-x_p)$ in the isotropic $SU(2)$ Wilson law. In the infinite-time vacuum there exist $\beta_0,C<\infty$, independent of the spatial side $L\ge3$, such that
$$
                  \mathbb E e^{Y_p/8}\le C\qquad(\beta\ge\beta_0)
$$
for every orientation. This estimate upgrades the rooted Gaussian limit to convergence of all joint polynomial moments of finitely many scaled curvatures and scaled plaquette actions.

## A local reflection bound at arbitrary side length

Begin at finite even time extent $N\ge4$. Assign the initial face to one nominal unit four-cube containing it. Let $f=\exp(Y_p/8)$. Whenever a function $g$ is a nonnegative product of the copied factors supported on a rectangular block, reflect that block in one endpoint site plane perpendicular to an axis. As long as the block fits into its half lattice, [site reflection positivity](reflection.md) and Cauchy–Schwarz against $1$ give
$$
                  (\mathbb E g)^2\le \mathbb E[g\,\theta g].
$$
Indeed the bilinear form $(A,B)\mapsto\mathbb E[A\,\theta B]$ on real half-functions is symmetric, positive and has $(1,1)=1$. The reflected copy of the plaquette factor is exactly the factor for the reflected face since scalar trace is invariant under inversion and cyclic base changes.

Starting at width one, double successively along each of the four axes up to the largest power of two **at most half** of the corresponding extent. At every step the old block lies on one side of the chosen site plane, away from the far seam, including for odd spatial sides. The new block occupies consecutive cells. If the final widths are $k_i$, then $k_i>\mathrm{extent}_i/4$ and $J=\prod_i k_i>L^3N/256$. The final block contains $J$ distinct nominal unit four-cubes with one assigned face per cube. A fixed plaquette belongs to at most four such four-cubes, since its two transverse coordinates each have two choices of side. Repetition of a face at a shared boundary is thus accounted for. Iterating the inequality gives
$$
 (\mathbb E_{\beta,L,N} e^{Y_p/8})^J
 \le \mathbb E_{\beta,L,N}\exp\!\left(\tfrac18\sum_{\rm copies}Y_{p'}\right)
 \le \frac{\mathcal Z_{\beta/2,L,N}}{\mathcal Z_{\beta,L,N}} .
$$
In the last bound every positive action in the original Wilson integral can be softened by at most one half. This argument applies to single cells on non-dyadic boxes without changing their boundary conditions.

At fixed $\beta,L$ take $N\to\infty$ along even periods. With $P=3L^3$, the logarithm of the partition ratio divided by $NP$ tends to
$$
 \log \frac{z(\beta/2)}{z(\beta)}
       +P^{-1}\log\frac{\|T_{\beta/2,\beta/2}\|}{\|T_{\beta,\beta}\|}.
$$
The numerator norm is at most one. The denominator has $-P^{-1}\log\|T_{\beta,\beta}\|\le C_0$ by the original-link product-bump lower bound. The one-link normalization ratio is bounded by the radial cap estimates. Since $NP/J<768$ and the partition ratio is at least one, this proves the uniform exponential moment. At fixed regulator the exponential of the face action is a bounded cylinder function, so its expectation passes to the vacuum in this order. [Transfer pressure and local conventions](wilson-law.md) · [Product-bump estimate](../electric-disorder/wilson-readings.md)

## Limiting moments and a one-face spectral measure

We have $|F_p^\beta|^2\le2Y_p$. The exponential bound and Hölder's inequality give uniform integrability of every fixed joint polynomial in finitely many $F_p^\beta,Y_p$, including absolute moments. The identity $2Y_p=|F_p^\beta|^2+Y_p^2/\beta$ identifies the joint limit. Each $Y_p$ converges to $\chi^2_3/4$, with moments
$$
 \lim_{\beta,L\to\infty}\mathbb E Y_p^k
   =2^{-k}\frac{\Gamma(k+3/2)}{\Gamma(3/2)}\qquad(k\ge0).
$$
In particular the mean tends to $3/4$, the second moment to $15/16$ and the variance to $3/8$. These are the values for normalized fundamental trace and the specified Wilson coupling, in both spatial and temporal orientations.

For a spatial $12$ face, the *unbounded in the limit* action $Y_p$ itself is a finite-regulator multiplication observable. With the notation $C_1(n),\mu_1$ of the [single-face calculation](reflection.md), Wick's formula gives
$$
 \lim_{\beta,L\to\infty}\operatorname{Cov}(Y_p(0),Y_p(n))
     =\tfrac32 C_1(n)^2,\qquad \rho_Y=\tfrac32\,\mu_1*\mu_1 .
$$
Each of the three colors contributes $2C_1(n)^2/4$. Its finite-cutoff connected spectral measures converge weakly after mapping lattice energy $E$ to $\exp(-E)$, including their total masses by the second-moment bound. In the limiting measure $\rho_Y([0,\epsilon])\sim 3\epsilon^8/(2\pi^4\,8!)$ and its large-step correlation is asymptotic to $3/(2\pi^4 n^8)$. At any fixed positive physical time with $b\downarrow0$, both the variance-normalized and the mean-normalized connected action correlations vanish by the monotonicity argument. The rate at a growing separation is undetermined. The action probe has a nonzero limiting mean; the positive-time conclusion is about its connected part.
