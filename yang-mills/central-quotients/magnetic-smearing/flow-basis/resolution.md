# Energy resolution and its cost at zero momentum

Fix two **physical spatial flow times** $0<a<b<\infty$ and a target fraction $0<\eta<1$. At zero external spatial momentum the free two-gluon magnetic channel has measure $dE\,E^4$ times $d/(256\pi^2)$ for $d$ colors. Divide out this common positive factor. A reading at time $s$ is the vector $g_s(E)=e^{-sE^2/2}$ in $\mathcal H=L^2(E^4\,dE)$. For two different flow times $s,v$, each curvature leg receives one multiplier from each insertion. The cross spectrum therefore has filter $e^{-(s+v)E^2/2}$. This gives the full Gram matrix, including its off-diagonal entries. [Single-clock normalization](../flow-momentum/spectrum.md)

For a nonzero finite sum $F=\sum_j c_j g_{s_j}$, $s_j\in[a,b]$, define
$$
 \chi(F;c)=\frac{\sum_j |c_j|\|g_{s_j}\|}{\|F\|}.
$$
This number measures cancellation among the chosen readings. It is unchanged by a common rescaling. Let $\chi_{\min}(\epsilon,\eta)$ be its infimum over sums with at least fraction $\eta$ of their squared norm in $0<E\le\epsilon$. In fixed energy units, for all sufficiently small $\epsilon$ there exist positive constants depending only on $a,b,\eta$ such that
$$
 C_1\,\epsilon^{-2}\ \le\ \log\chi_{\min}(\epsilon,\eta)\ \le\ C_2\,\epsilon^{-2}.
$$
The estimate is for the free, zero-momentum magnetic sector with independent coefficients of either sign. The upper bound is constructive. It uses $O(\epsilon^{-2})$ flow times in the *same* interval. The proof gives no optimal leading constant.

### Why the interval spans the sector

If $h\in\mathcal H$ is perpendicular to every $g_s$ in the interval, the integral $\int\overline h(E)e^{-sE^2/2} E^4\,dE$ is holomorphic for $\operatorname{Re}s>0$ by exponential domination and Cauchy–Schwarz. Analytic uniqueness makes it zero throughout that half-plane. Tilt by any $s_*>0$ and push the resulting finite complex measure forward by $x=e^{-E^2/2}$. Vanishing at $s_*+n$ gives all polynomial moments zero. Polynomial density on $[0,1]$ and injectivity give $h=0$. In particular a narrow band at *any* energy can be approached in norm at rest. This statement concerns the radial sector of this operator. Positivity changes what can be achieved with a restricted set of coefficients: for $c_j\ge0$ the ratio $F/g_b=\sum_j c_j e^{(b-s_j)E^2/2}$ is nondecreasing. Reweighting the $g_b$ law by the square of this ratio can only decrease its cumulative probability at a lower threshold. This follows by integrating the ordered cross products over the two sides of the threshold. The single reading at $b$ attains the low-energy maximum in the positive cone.

### Lower bound for every signed combination

Set $p=5/2$, $s_*=\sqrt{ab}$, $x=s_*E^2$, and use the orthonormal Laguerre functions proportional to $e^{-x/2}L_n^{p-1}(x)$ with ambient density $x^{p-1}dx$. The Jacobian is a common constant. In this basis the unit vector $w_s=g_s/\|g_s\|$ has coefficients
$$
 \langle e_n,w_s\rangle=(1-r_s^2)^{p/2}
       \sqrt{(p)_n/n!}\ r_s^n,\qquad r_s=(s-s_*)/(s+s_*).
$$
Here $(p)_n$ is the rising factorial. Integrating the Laguerre generating function against $x^{p-1}e^{-(1+s/s_*)x/2}$ gives this formula. The sum of squared coefficients is one by the binomial series, which also checks normalization. [NIST DLMF, Eq. 18.12.13](https://dlmf.nist.gov/18.12.E13) · [Orthogonality and weights](https://dlmf.nist.gov/18.3)

Write $r=(\sqrt b-\sqrt a)/(\sqrt b+\sqrt a)<1$. For any $r<q<1$, the norm in degrees $n\ge N$ of each $w_s$ is at most $A q^N$, $A=(1-r^2/q^2)^{-p/2}$. This follows by extracting $q^{2N}$ from the squared tail and summing the binomial series. For $F/\|F\|$ the same tail is bounded by $\chi A q^N$.

Let $\Pi_N$ project onto the first $N$ Laguerre functions and $P_u$ restrict to $0\le x\le u=s_*\epsilon^2$. Cauchy–Schwarz gives $\|P_u\Pi_N\|^2\le\sum_{n<N}\|P_u e_n\|^2$. The finite Laguerre expansion gives $|L_n^{p-1}(x)|\le L_n^{p-1}(0)e^{nx/p}$ for $x\ge0$, since the $j$th coefficient relative to the constant is bounded in absolute value by $n^j/(p^j j!)$. Also $(p)_n/n!\le e^{p-1}(n+1)^{p-1}$ from the harmonic sum bound. Integrating yields
$$
 \|P_u\Pi_N\|^2\le
 e^{2Nu/p+p-1}(Nu)^p/\Gamma(p+1).
$$
For clarity, the individual summand before the harmonic bound is at most $e^{2Nu/p} u^p (p)_n/[n!\Gamma(p+1)]$. [Finite Laguerre sum, Eq. 18.5.12](https://dlmf.nist.gov/18.5.E12)

Choose $c>0$ so that $D=(e^{2c/p+p-1}c^p/\Gamma(p+1))^{1/2}<\sqrt\eta$. For $N=\lfloor c/u\rfloor\ge1$, the triangle inequality gives $\sqrt\eta\le D+\chi A q^N$. Thus $\chi\ge(\sqrt\eta-D)q^{-N}/A$, establishing the lower bound. It applies to any number and placement of flow times in the interval.

### A finite family attaining the exponential order

Let $m\ge2$, $N=2(m-1)$, $s_j=a+(b-a)j/N$, and $X=e^{-(b-a)E^2/(2N)}$. For the Chebyshev polynomial $T_m$, put
$$
 K_m(X)=\frac{1-T_m(2X-1)}{2m^2(1-X)},\qquad
 F_m(E)=e^{-aE^2/2}K_m(X)^2 .
$$
The quotient is a degree-$m-1$ polynomial with $K_m(1)=1$. Thus expanding the square realizes $F_m$ with exactly the specified available times (some coefficients can vanish). For $\sin(\theta/2)=\sqrt{1-X}$, the kernel is $[\sin(m\theta/2)/(m\sin(\theta/2))]^2$, the normalized Fejér kernel. In particular $0\le K_m\le\min(1,[m^2(1-X)]^{-1})$. [Chebyshev trigonometric representation](https://dlmf.nist.gov/18.5.E1)

Normalize the energy measure of $F_m$ and set $y=\sqrt m\,E$, $\gamma=\sqrt{b-a}/2$. Its density converges in $L^1(dy)$ to the normalized $y^4\operatorname{sinc}^8(\gamma y)$, where $\operatorname{sinc}(z)=\sin(z)/z$. Its second moment also converges. In fact $m\sqrt{1-X}\to\gamma y$ at fixed $y$. In the region $(b-a)y^2/(2Nm)\le1$, $1-X$ is at least half that exponent, so the rescaled squared filter is bounded by $C(1+y)^{-8}$. This is integrable against both $y^4dy$ and $y^6dy$. On the complement $K_m^4\le C m^{-8}$ and the integrals against $y^j e^{-a y^2/m}$, $j=4,6$, are $O(m^{(j+1)/2-8})$. This also proves $\|F_m\|^2\sim m^{-5/2}\pi/(12\gamma^5)$.

The two integrals needed for the scaled second moment are $\int_0^\infty\sin^8 v\,dv/v^4=\pi/12$ and $\int_0^\infty\sin^8 v\,dv/v^2=5\pi/32$. Expand $128\sin^8 v=35-56\cos(2v)+28\cos(4v)-8\cos(6v)+\cos(8v)$. Integrating twice or using the Dirichlet integral gives $\int(1-\cos tv)\,dv/v^2=\pi t/2$ and $\int(\cos tv-1+(tv)^2/2)\,dv/v^4=\pi t^3/12$ for $t\ge0$ over the positive half-line. The constant and quadratic subtractions cancel in the combined expression. Hence
$$
 m\,\langle E^2\rangle_{F_m}\longrightarrow \frac{15}{2(b-a)}.
$$
For example, eventually more than half the probability is below $4/\sqrt{(b-a)m}$ by Markov's inequality. For any fixed $\eta<1$, increasing this constant yields the required fraction.

All $m-1$ roots of $K_m$ counted with multiplicity are the nonnegative numbers $\cos^2(\pi j/m)$, $1\le j<m$, by the trigonometric expression (the endpoint zero for even $m$ is simple). Consequently the coefficients of $K_m^2$ have alternating signs on their nonzero support and their absolute sum is $K_m(-1)^2=[(1-(-1)^m\cosh(m\operatorname{arcosh}3))/(4m^2)]^2$. The individual norms $\|g_{s_j}\|$ are between two positive constants. Therefore $\log\chi(F_m;c)/m\to2\operatorname{arcosh}3$. Taking $m$ proportional to $\epsilon^{-2}$ gives the upper bound for $\log\chi_{\min}$. At $m=3$, $K_m(X)^2=(1-4X)^4/81$. For $[a,b]=[1,4]$ these five readings have $\langle E^2\rangle<1/2$, while the best single reading has $5/8$. The strict five-reading comparison reduces to nine radicals and is proved in Lean. [Formal certificate](FlowBasis.lean) · [Larger finite tests](execution.md)
