# Positive spectral weight at inverse block size

Let $B_{\beta,\mu,R}(n)$ be the connected autocorrelation of the [bounded spatial block](comparison.md) in the selected periodic Wilson state. The same observable is used at both ends for every lag at a given $R$. Let $C_R(n)$ be the one-color covariance of its linear argument in the free projected curvature. If $D_R=1+2s C_R(0)$, the corresponding connected Gaussian reading is
$$
 B_R(n)=\left[D_R^2-4s^2 C_R(n)^2\right]^{-3/2}-D_R^{-3}.
$$
This is the two-time Gaussian determinant in three colors. Integrate (1) of the [block comparison](comparison.md) against independent three-dimensional $N(0,2sI)$ Fourier variables for the two insertions; do the same for their means. The integrable error gives
$$
 \sup_{\mu,\ n\ge0}|B_{\beta,\mu,R}(n)-B_R(n)|\le C_s R^4/\sqrt\beta. \tag{1}
$$
The supremum is over integer lags and all even-periodic thermodynamic limit states at fixed coupling. The bound is absolute.

## The free block signal

The temporal Fourier integral of the projected $12$ curvature gives
$$
 C_R(n)=\int_{[-\pi,\pi]^3} |\widehat g_R(q)|^2
       \frac{h_1^2+h_2^2}{2\sinh\omega}\,e^{-|n|\omega}
       \frac{d^3q}{(2\pi)^3},\quad
 h_i=2\sin(q_i/2),\quad \omega=2\operatorname{arsinh}(|h|/2).
$$
The square modulus of the Fourier transform is the spatial one. Set $p=Rq$ and $\operatorname{sinc} u=\sin(u)/u$ with its continuous value at zero. Up to a phase the single-box transform is $\sin(p_i/2)/[R\sin(p_i/(2R))]$. The third difference gives $|R(1-e^{-ip_3/R})|^3$ after dividing $\widehat g_R$ by $R^2$. If $n/R\to t\ge0$, then
$$
 C_R(n)\ \longrightarrow\
 C(t)=\int_{\mathbb R^3} p_3^6\prod_{i=1}^3\operatorname{sinc}(p_i/2)^{12}
       \frac{p_1^2+p_2^2}{2|p|}e^{-t|p|}
       \frac{d^3p}{(2\pi)^3}. \tag{2}
$$
Indeed $R^{-2}|\widehat g_R(p/R)|\le C |p_3|^3(1+|p|)^{-6}$ throughout the rescaled zone by using the largest coordinate for decay. The other three powers of $R$ are precisely consumed by the integration volume and one further power by the magnetic symbol. More explicitly, $R(h_1^2+h_2^2)/(2\sinh\omega)\le |p|/2$ and converges almost everywhere to $(p_1^2+p_2^2)/(2|p|)$. Thus an integrable radial upper bound for the rescaled integrand is $C |p|^7(1+|p|)^{-12}$, also at $t=0$. The integrand is positive on open sets at every finite $t$. Writing $D=1+2sC(0)$ gives the limiting connected reading
$$
 B(t)=[D^2-4s^2 C(t)^2]^{-3/2}-D^{-3}>0 .
$$

As $R\to\infty$ with $R=o(\beta^{1/8})$, (1) and (2) give both $B_{\beta,\mu,R}(0)\to B(0)>0$ and $B_{\beta,\mu,R}(\lfloor tR\rfloor)\to B(t)$ for every finite $t>0$, uniformly over states. The same characteristic functions identify the joint laws of any fixed finite list of the rooted block vectors at $t_i R$ (integer parts) with a Gaussian limit having covariance $C(|t_i-t_j|)I_3$. Finite lists of the scalar readings follow by continuity. The spatial support here grows with the lag. These are explicitly smeared observables in a microscopic weak-coupling regime.

## Endpoint estimate for the gap

Let $R$ be the largest even integer at most $c\,\beta^{1/8}$. Choose fixed $c>0$ so small that $C_s c^4<B(1)/4$. For sufficiently large $\beta$, (2) gives $B_R(R)>3B(1)/4$ and hence $B_{\beta,\mu,R}(R)>B(1)/2$. If $m=-\log\|T_\mu|_{\Omega^\perp}\|$, the centered transfer reading at this even lag obeys
$$
 B_{\beta,\mu,R}(R)\le e^{-mR} B_{\beta,\mu,R}(0)\le e^{-mR},
 \qquad
 \sup_{\mu}m(\beta,\mu)\le C\,\beta^{-1/8}.
$$
The variance bound uses $0\le O_R\le1$. At fixed $c$ the comparison error stays bounded by $C_s c^4$; exact convergence was used only for the free reading as $R\to\infty$. The exponent is an upper bound in lattice units. The actual gap and the coupling-dependent constant needed for physical scale setting are separate questions. [Qualitative criticality](../README.md) · [Earlier fixed-stencil rate](../rate/README.md)

## Distinguishing positive energies from a second vacuum

Write $\kappa$ for the pushforward of the measure in (2) at $t=0$ under $p\mapsto |p|$. It has finite mass $C(0)$ and a positive density at every strictly positive radius: the directions where a magnetic factor or any sinc vanishes have zero angular measure. The proof needs only strict positivity on each open interval. The limiting energy measure $\nu$ of the bounded connected reading is
$$
 \nu=D^{-3}\sum_{m\ge1}\frac{(3/2)_m}{m!}
           (4s^2/D^2)^m\,\kappa^{*2m}.
$$
The series converges in total mass since $2sC(0)/D<1$. Its Laplace transform equals $B(t)$, its total is $B(0)$, and it is absolutely continuous with positive mass in every interval in $(0,\infty)$. The first convolution already gives that positivity.

In the positive Wilson transfer, let $\rho_{\beta,\mu,R}$ denote the *unnormalized* spectral measure of the centered block, with $E$ the lattice energy. When $1\ll R\ll\beta^{1/8}$ its pushforward by $E\mapsto RE$ converges weakly to $\nu$. Indeed under $y=e^{-RE}$ every polynomial moment converges, including degree zero, by the preceding time limits. Polynomials are dense on $[0,1]$, and the limiting measure puts no mass at either endpoint. This handles an actual zero-energy contribution or a possible transfer nullspace without assuming uniqueness of the vacuum. [Wilson transfer positivity](https://doi.org/10.1016/0003-4916(78)90039-8)

There is a stronger endpoint conclusion for a prescribed finite list of disjoint intervals $(u_i,v_i)\subset(0,\infty)$. Some $c>0$ and $d_i>0$ give, for the same even $R\sim c\beta^{1/8}$ in every sufficiently weakly coupled state,
$$
              \rho_{\beta,\mu,R}\big((u_i/R,v_i/R)\big)\ge d_i
              \quad\text{for every }i. \tag{3}
$$
For each interval in the $y$ coordinate take a continuous bump $0\le f_i\le1$ supported strictly inside $(e^{-v_i},e^{-u_i})$ with positive $\nu$-integral $a_i$ (using the pushforward to $y$). Choose a polynomial $P_i$ approximating $f_i$ uniformly within $\epsilon_i$. Both the Wilson and free measures have mass at most one. Comparing their $P_i$ integrals costs at most $\|P_i\|_{\rm coeff,1}C_s c^4$ by (1) at the finitely many required integer multiples of $R$. The free lattice polynomial integrals approach the limiting ones by (2). Choose $2\epsilon_i<a_i/4$, then $c$ so the moment error is below $a_i/4$ for all $i$. After increasing $\beta$ if necessary this gives the stated positive lower bounds, for example $d_i=a_i/4$.

For one broad band just three time readings suffice. In $y=e^{-RE/8}$, take $R$ divisible by eight and $Q_\epsilon(y)=(y-\epsilon)(1-\epsilon-y)=y-y^2-\epsilon(1-\epsilon)$. Its limiting integral divided by $B(0)$ is $d-\epsilon(1-\epsilon)$, with $d=[B(1/8)-B(1/4)]/B(0)>0$. Taking $\epsilon=d/2$ makes this positive. The polynomial is nonpositive outside $(\epsilon,1-\epsilon)$ and bounded by $(1/2-\epsilon)^2$ inside, which directly lower-bounds the mass there. The [quadrature](check.py) also evaluates this certificate for the fixed choice $\epsilon=0.1$.

Projecting the *same vector* onto disjoint intervals in (3) gives orthogonal, nonzero gauge-invariant vectors. For every fixed $M$ there are at least $M$ orthogonal spectral vectors in $(0,C_M\beta^{-1/8})$ uniformly over states for sufficiently large $\beta$. In particular the dimension of the positive-energy spectral subspace below any $E_\beta$ with $E_\beta\beta^{1/8}\to\infty$ tends to infinity in this uniform sense. This argument uses disjoint energies; a positive spectral matrix for several displaced probes in one prescribed band is B4's separate question. The estimates do not determine the ratio of these energies to the actual gap. [B4's momentum-channel analysis](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7101711447) · [Clay problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
