# Which Gaussian does a weighted Wilson plaquette see?

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

On a single open Wilson square, the faithful representation $\rho_k(e^{i\theta})=\operatorname{diag}(e^{i\theta},e^{ik\theta})$ has a one-dimensional Lie algebra for every integer $k\ge1$. At weak coupling its projected score sees one Gaussian degree of freedom uniformly in $k$. The **full action** sees one or two degrees of freedom, with an explicit intermediate law when $k$ is of order $\sqrt\beta$. This identifies the scale at which Z4’s fixed-representation Taylor argument loses uniformity. The calculation uses the exact compact integral for the isolated plaquette. Extrapolation to a four-dimensional Wilson state would require a separate argument. [Z4’s weighted-circle example](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/7d69f0c07e901f570b85c4a5a14872526bb6199e/yang-mills/z4/attempt/paper/sec_general.tex#L27) · [Uniform pressure comparison for four-dimensional periodic limits](../block/uniform-pressure.md)

## Exact coordinates and uniform approximation

Under independent Haar links the face holonomy is Haar. With $\theta\in[-\pi,\pi)$ and $\phi$ the principal representative of $k\theta$ in the same interval, the Wilson probability is proportional to $e^{-Y}d\theta/(2\pi)$, where
$$
h=\sqrt{\beta/2},\qquad Y=h^2(2-\cos\theta-\cos\phi).
$$
Set $x=h\theta$, $y=h\phi$, $K=\sqrt{1+k^2}$. Resolve the tangential and normal coordinates by
$$
q=(x+ky)/K,\qquad b=(kx-y)/K,\qquad a=2\pi h/K.
$$
Since $k\theta-\phi=2\pi j$, the normal coordinate is exactly $b=aj$ for $j\in\mathbb Z$. In each branch $d\theta=dq/(hK)$. Every point of every line whose inverse coordinates $(x,y)$ belong to $[-\pi h,\pi h)^2$ occurs once apart from endpoints. This keeps branches that would disappear upon expanding at identity before doing the compact integral.

Write $\Theta(a)=\sum_{j\in\mathbb Z}e^{-(aj)^2/2}$. Let $Q\sim N(0,1)$ and independently let $B$ take the value $aj$ with probability $e^{-(aj)^2/2}/\Theta(a)$. Uniformly over all positive integer windings, as $\beta\to\infty$,
$$
d_{\rm TV}\big(\mathcal L(q,b),\mathcal L(Q,B)\big)=O(\beta^{-1}),
\qquad
Z_{\beta,k}=\frac{\Theta(a)}{\sqrt{2\pi}\,hK}\big[1+O(\beta^{-1})\big].
$$
The approximation holds also in the integral of the absolute density difference against any fixed polynomial weight in $|q|+|b|$, with a weight-dependent constant.

**Proof.** Compare both unnormalized densities against $dq$ times counting measure on the lines. Put $r^2=q^2+b^2=x^2+y^2$. On the square, the elementary cosine bounds give
$$
2r^2/\pi^2\le Y\le r^2/2,\qquad 0\le r^2/2-Y\le r^4/(24h^2).
$$
Thus the density difference there is bounded by $r^4 e^{-2r^2/\pi^2}/(24h^2)$. Outside the square $r\ge\pi h$, so the omitted Gaussian has an equally integrable bound of order $h^{-2}$ after extracting a polynomial factor. For fixed $c>0$ and polynomial weight, integration in $q$ and summation in $j$ against $e^{-c(q^2+(aj)^2)}$ cost $O_c(1+a^{-1})$, with a constant also depending on the weight. To see this, absorb the polynomial into half the Gaussian exponent and compare the decreasing positive half-line sum to its integral. Conversely $\Theta(a)\ge1$ and is bounded below by a constant times $a^{-1}$ for $a\le1$, by counting $|aj|\le1$. Division by the Gaussian mass $\sqrt{2\pi}\Theta(a)$ preserves the order $h^{-2}$ uniformly. Restoring the exact Haar Jacobian gives the stated partition function.

## Energy, score and the three limits

The one real coordinate of the normalized projected score is
$$
S=\frac{h}{K}(\sin\theta+k\sin\phi).
$$
Taylor’s inequality gives $|S-q|\le C r^3/h^2$. The density comparison gives convergence of $S$ to a standard normal along every winding sequence and $\mathbb E S^2=1+O(\beta^{-1})$. As a finite-coupling cross-check, integration by parts on the circle gives the exact identity $\mathbb E S^2=\mathbb E[(\cos\theta+k^2\cos\phi)/(1+k^2)]$. For the action it gives
$$
\mathbb E Y=\tfrac12+\frac{\sum_j(aj)^2 e^{-(aj)^2/2}}{2\Theta(a)}+O(\beta^{-1}),
\qquad
\mathbb E e^{-tY}=(1+t)^{-1/2}\frac{\Theta(a\sqrt{1+t})}{\Theta(a)}+O_t(\beta^{-1}),\quad t\ge0 .
$$
Indeed $Y$ differs from $r^2/2$ by at most $r^4/(24h^2)$ on the square, and the moments needed for that replacement are bounded uniformly. These estimates also identify the joint limit of the score and action by replacing them with $Q$ and $(Q^2+B^2)/2$ in bounded Lipschitz tests.

| Winding scale | Transverse law | Limiting scaled plaquette action |
| --- | --- | --- |
| $k/\sqrt\beta\to0$ | $a\to\infty$ and $B\to0$ | $\chi_1^2/2$, of mean $1/2$ |
| $k/\sqrt\beta\to\kappa\in(0,\infty)$ | Discrete Gaussian of spacing $\sqrt2\pi/\kappa$ | $(Q^2+B^2)/2$ with independent summands before squaring |
| $k/\sqrt\beta\to\infty$ | $a\to0$ and $B\Rightarrow N(0,1)$ by Riemann sums | $\chi_2^2/2$, of mean $1$ |

Thus even the mean full action can differ by order one from its fixed-representation tangent prediction. For the observable projected along the Lie algebra, changing the representation adds no second Gaussian coordinate to that projection.

## Independent controls

Expanding both Wilson factors in Fourier modes gives the independent identity
$$
Z_{\beta,k}=e^{-2h^2}\sum_{n\in\mathbb Z} I_{kn}(h^2)I_n(h^2).
$$
It follows from the modified Bessel generating series and integration on the original circle. Direct angular quadrature and the truncated, exponentially scaled Bessel series agreed to relative error below $10^{-10}$ on all 15 tested parameter pairs. At $\beta=1024$, the measured means for windings $1,32,96,288$ were $0.500122,0.501304,0.998247,1.000489$; the respective predictions were $0.500000,0.501030,0.997781,1.000000$. [NIST DLMF, Eq. 10.35.2](https://dlmf.nist.gov/10.35#E2) · [Numerical checks](check.py)

Three recursively linked PCP OS guests checked the principal-branch convention on 1,024 cyclic inputs and the frame identity on 1,352 integer triples, then emitted its real algebraic form. Hosted Lean 4.19.0 verified four supporting declarations; the verifier rejected one malformed request and three altered declarations. The uniform probability approximation is the analytic argument above. [Guest](worker.c) · [Lean checks](WindingCircle.lean) · [Replay](verify.py)
