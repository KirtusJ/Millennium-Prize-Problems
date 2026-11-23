# Comparing two growing time lags

Fix $j\ge1$ and $s>0$. On the spatial slice at time $t$ use $j+1$ positively oriented $12$ plaquettes, based at $x_\ell=(t,\ell e_3)$ for $0\le\ell\le j$. Transport each to $x_0$ along the straight spatial path, writing the transported holonomy as $V_\ell$. Define
$$
 X_j(t)=\sqrt\beta\sum_{\ell=0}^j(-1)^\ell\binom j\ell\,\operatorname{Im}V_\ell,\qquad
 O_j(t)=\exp[-s|X_j(t)|^2],\qquad
 B_{\beta,j}(n)=\operatorname{Cov}_\mu(O_j(0),O_j(n)).
$$
The color norm is gauge-invariant. With the time-first ordering, the spatial transports used here extend the root path to $x_0$ exactly. Therefore each color Fourier argument of a dipole, or of a product of two of them, is precisely the rooted test $F(g)$ used in the [heat estimate](heat.md). No comparison of separate color frames over a distance $n$ is needed for that identity.

Represent $e^{-s|X|^2}$ as the characteristic function in $X$ of a centered three-dimensional normal with covariance $2sI$. Use independent Fourier variables for the product. The polynomial $(1+Y)^2$ in the characteristic-function error has finite Gaussian expectation. Applying the estimate to the product and both means proves
$$
       \sup_{\mu\in\mathcal P_\beta,\ n\ge0}
          |B_{\beta,j}(n)-B_j(n)|\le C_{j,s}\delta_j. \tag{1}
$$
Here the supremum is over integer lags and all even-periodic thermodynamic limit states. The reference $B_j$ is the connected reading for Gaussian lattice curvature of covariance $P$, the $\ell^2$ exact-form projection, in three independent colors. For one color put $h_i=2\sin(q_i/2)$, $\omega=2\operatorname{arsinh}(\sqrt{\sum_i h_i^2}/2)$. The spatial difference has squared multiplier $h_3^{2j}$. Consequently
$$
 \begin{aligned}
 C_j(n)&=\int_{[-\pi,\pi]^3}\frac{h_3^{2j}(h_1^2+h_2^2)}
                  {2\sinh\omega}e^{-|n|\omega}\frac{d^3q}{(2\pi)^3},\\
 D_j&=1+2s C_j(0),\qquad
 B_j(n)=[D_j^2-4s^2 C_j(n)^2]^{-3/2}-D_j^{-3}.
 \end{aligned}
$$
These follow by integrating the temporal momentum and taking the two-time Gaussian determinant. [One-difference calculation](../../dipole.md)

Near zero $\omega/|q|\to1$ uniformly in direction $\theta=q/|q|$. The angular integral of $\theta_3^{2j}(1-\theta_3^2)$ is $8\pi/[(2j+1)(2j+3)]$. On a small ball $c|q|\le\omega\le C|q|$, so radial scaling by $n$ is dominated by a polynomial times an exponential. Away from the ball the integral decays exponentially. Thus, setting $p_j=8+4j$,
$$
 C_j(n)\sim A_j n^{-4-2j},\quad
 A_j=\frac{(2j+3)!}{2\pi^2(2j+1)(2j+3)},\qquad
 B_j(n)\sim b_j n^{-p_j},\quad b_j=6s^2D_j^{-5}A_j^2>0.
$$

## Upper bound on the lattice gap

Let $m=-\log\|T_\mu|_{\Omega^\perp}\|$. For any even $n>0$, the centered vector for $O_j$ has
$$
                 B_{\beta,j}(2n)\le e^{-mn}B_{\beta,j}(n).
$$
The even lag makes the one-lag spectral integrand nonnegative even for a self-adjoint contraction. Use $n$ the largest even integer at most $c\delta_j^{-1/p_j}$. For sufficiently small fixed $c>0$ and all sufficiently large $\beta$, (1) costs less than half the smaller of $B_j(n)$ and $B_j(2n)$, uniformly in the state. Then $B_{\beta,j}(n)>0$ and $B_{\beta,j}(2n)/B_{\beta,j}(n)$ is bounded below by a fixed positive number, since $B_j(2n)/B_j(n)\to2^{-p_j}$. This proves $m\le C_{j,s}\delta_j^{1/p_j}$. Comparing against equal time would lose a factor $\log n$.

The second spatial difference gives the strongest of the resulting bounds,
$$
             \sup_{\mu\in\mathcal P_\beta}m(\beta,\mu)
                 \le C\,\beta^{-1/32}[\log(2+\beta)]^{1/16}.
$$
The first difference gives $O(\beta^{-1/48})$, the third $O(\beta^{-1/40})$. The constants have not been optimized. If the lattice gap is positive its inverse therefore diverges at least as $c\,\beta^{1/32}/[\log(2+\beta)]^{1/16}$. This argument is compatible with much faster divergence.

## The law before the correlation-length scale

For any real $T=T_\beta\to\infty$ with $\delta_j T^{p_j}\to0$, uniformly over choices of states, at each fixed $t>0$,
$$
 T^{p_j}B_{\beta,j}(\lfloor tT\rfloor)\ \longrightarrow\ b_j t^{-p_j}.
$$
This follows directly from (1), including the zeroth-order cancellation from centering. In a positive Wilson transfer let $\rho_{\beta,j}$ be the connected spectral measure in lattice energy $E$. Tilt it at $\lfloor T\rfloor$ by $e^{-\lfloor T\rfloor E}$, normalize to a probability and push it forward by $E\mapsto TE$. The Laplace transform at $v\ge0$ tends to $(1+v)^{-p_j}$: monotonicity bounds the noninteger reading at $\lfloor T\rfloor+vT$ by its two neighboring integer readings. The limiting probability is Gamma with shape $p_j$ and rate one, by continuity and uniqueness of Laplace transforms. For $j=2$, every $T=\beta^\alpha$ with $0<\alpha<1/32$ qualifies and the shape is 16. The gap estimate gives $T m\to0$ throughout this regime. The argument does not reach $T=1/m$ or establish survival of a local reading there. [Z4's condition (C)](../../../../z4/attempt/A1_REDUCTION.md) · [Physical mass gap](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
