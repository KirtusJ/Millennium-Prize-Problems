# Which electric levels a spatial clock selects on an open square

Use the gauge theory of an open spatial square with four links, positive temporal Wilson coupling $\beta_t$, and zero spatial coupling in the **measure**. Evolve the observable by the spatial gradient of the single unit-coupling plaquette deficit. These choices allow independent exact calculations of both the observable and its spectrum. The Haar vacuum on the four links reduces to Haar measure on the plaquette $P$. Gauge-invariant functions are class functions. Write $P=\cos\theta+\mathbf n\sin\theta$, $x=\cos\theta$. The real orthonormal character $\chi_\ell=\sin((\ell+1)\theta)/\sin\theta$ has transfer eigenvalue $\lambda_\ell=[I_{\ell+1}(\beta_t)/I_1(\beta_t)]^4$. Indeed convolution on each of the four links contributes the same representation multiplier and at the bivalent vertices there is a single contraction for each spin. The eigenvalues decrease strictly to zero. This also follows from the one-link ratios and their strict Turán inequalities. [A4's electric transfer calculation](../../../observable-normalization/replica-gap/electric.md) · [Baricz and Ponnusamy, modified Bessel inequalities](https://arxiv.org/abs/1010.3346)

The raw magnetic target is $H=(1-x^2)/2=(3-\chi_2)/8$. Its centered vector lies entirely in the adjoint channel. The nonlinear spatial flow at the four links induces $\dot\theta=-4\sin\theta$ and keeps the axis fixed. For a bi-invariant metric the derivative of the product map in any one link is an isometry of tangent spaces, also for an inverse link. Summing its four products with their adjoints gives four times the identity on the holonomy tangent. The radial equation follows by differentiating $1-\cos\theta$. It gives $\tan(\theta_u/2)=e^{-4u}\tan(\theta/2)$. Thus the predictor for $\mu=\operatorname{law}(T_n)$ in the [preceding construction](wilson.md) is
$$
 J_n(x)=\tfrac12(1-x^2) A_n(x)^2,\qquad
 A_n(x)=\int_0^\infty\frac{k_n(u)\,du}{\cosh(4u)+x\sinh(4u)}\quad(-1<x<1).
$$
Define the endpoint values using the fixed center elements, where $J_n=0$.

### A nonzero lower-energy component for every clock index

Put $m_j=E[\operatorname{sech}(4T_n)\tanh(4T_n)^j]$. For $0<x<1$, geometric expansion gives $A_n(-x)-A_n(x)\ge2x m_1$ and $A_n(-x)+A_n(x)\ge2m_0$. Both $m_0,m_1$ are positive. Write $c_\ell(n)=\langle\chi_\ell,J_n\rangle_{\rm Haar}$. Haar symmetry and $\chi_1=2x$ give
$$
 -c_1(n)\ \ge\ 4m_0m_1\!\int_{x>0} x^2(1-x^2)d{\rm Haar}
 =m_0m_1/4
 \ \ge\ q(4)^n\,[q(4)^n-q(12)^n]/8 .
$$
The Haar moments are $E x^2=1/4$ and $E x^4=1/8$ from the unit three-sphere. For the final bound use $\operatorname{sech}z\ge e^{-z}$ and $\operatorname{sech}z\tanh z\ge e^{-z}(1-e^{-2z})/2$. Consequently $J_n^c$ puts at least the square of this explicit bound in the fundamental eigenvalue. At every fixed $n$ the connected long-lag autocorrelation has leading term $c_1(n)^2\lambda_1^j$ as the measured lag $j\to\infty$. The target's centered autocorrelation equals $\lambda_2^j/64$. The two operators therefore give different leading transfer energies even in a gauge model where both are computed exactly.

### Escape from bounded energies as the clock index grows

Write $a=q(4)$. For $x>-1$, tilting $T_n$ by $e^{-4u}/a^n$ gives
$$
 A_n(x)/a^n=E_{\rm tilt}\!\left[\frac{2}{1+x+(1-x)e^{-8T_n}}\right]\ \longrightarrow\ \frac{2}{1+x}.
$$
Indeed $E_{\rm tilt}e^{-8T_n}=(q(12)/a)^n\to0$. Hence $J_n/a^{2n}\to4/(1+x)-2$ pointwise in the interior. The functions are bounded above by this limit, which is integrable for the Haar density $2\sqrt{1-x^2}/\pi$. It has infinite squared integral near $x=-1$. To integrate a character against $(1+x)^{-1}$, expand $(1+2rx+r^2)^{-1}=\sum_{\ell\ge0}(-r)^\ell\chi_\ell(x)$ for $r<1$. For $r\ge1/2$ the denominator is at least $1+x$; dominated convergence gives $E[\chi_\ell/(1+x)]=2(-1)^\ell$. It follows that $c_0(n)/a^{2n}\to6$ and $c_\ell(n)/a^{2n}\to8(-1)^\ell$ for each fixed $\ell\ge1$. [Character-integral check](check_square.py)

There is also a sharp asymptotic for the squared norm. Set $b=q(3)>a$, $\sigma^2=80/21^{3/2}$, and
$$
 C=\frac4\pi\left(\frac{\pi}{\cos(3\pi/8)}\right)^4
       \frac{\sqrt{\pi\sigma^2/2}}{(2\pi\sigma^2)^2}.
$$
Then $\|J_n^c\|^2\sim C n^{-3/2} b^{4n}$. For a fixed set of $m>0$ positive character labels, the fraction of its normalized squared weight is therefore
$$
 \frac{64m}{C}\ n^{3/2}(a/b)^{4n}(1+o(1)).
$$
At fixed $\beta_t$ every bounded energy window contains only finitely many positive character labels, since $-\log\lambda_\ell\to\infty$. The loss of normalized weight in such a window as $n$ increases is compatible with fundamental dominance when the **measurement lag** increases at fixed $n$.

To derive the norm put $r=\log\tan(\theta/2)$. Haar has density $(2/\pi)\operatorname{sech}^3 r\,dr$ and the flowed sine is $\operatorname{sech}(r-4u)$. Let $F_n$ be the distribution of $4T_n$ under tilt $e^{-3T_n}/b^n$, $g(r)=e^{-3r/4}\operatorname{sech}r$, and $w(r)=(e^r\operatorname{sech}r)^3$. Then the exact formula is
$$
 b^{-4n} E J_n^2=\frac1{2\pi}\int w(r)[F_n*g(r)]^4\,dr.
$$
The weight satisfies $0\le w\le8$ and $w(+\infty)=8$. By integration after substituting $e^{2r}$, the mass of $g$ is $G=\pi/\cos(3\pi/8)$. The tilted increments are independent. Each $4T_1$ has mean $d=4/\sqrt{21}$ and variance $\sigma^2$ by differentiating $\log q(v)=-2\operatorname{arsinh}(\sqrt v/2)$ at $v=3$. Its density is bounded, square integrable and positive throughout the positive half-line. The characteristic function $\phi$ has modulus strictly below one away from zero and tends to zero at infinity.

For completeness, the densities of $(4T_n-nd)/\sqrt n$ in the tilted law converge uniformly to the centered normal density $\varphi_\sigma$. In Fourier inversion, the centered integrand at frequency $t$ converges to $e^{-\sigma^2t^2/2}$ and is bounded by $e^{-c t^2}$ on $|t|\le\delta\sqrt n$ for a small fixed $\delta$. On the complement its absolute integral is at most $\sqrt n\,\|\phi\|_2^2\sup_{|s|\ge\delta}|\phi(s)|^{n-2}$. This tends to zero. Uniform convergence together with nonnegative unit mass gives $L^1$ convergence by integrating the minimum of the two densities. Convolving the normalized densities with the law of an independent variable of density $g/G$ divided by $\sqrt n$ preserves both convergences, by translation continuity of the normal density. In particular $\sqrt n(F_n*g)(nd+\sqrt n\,y)\to G\varphi_\sigma(y)$ in $L^4(dy)$ by interpolation. The transformed weight converges pointwise to 8 and is bounded by 8, so the fourth integral after rescaling tends to $8G^4\int\varphi_\sigma^4$. This gives $C$ above. Subtracting the mean square has exponentially smaller order since $a<b$. [Independent Fourier computation](check_escape.py)

All rates here concern one electric square and a precisely specified family of operators. The isotropic spatial-box result is the positive discrepancy proved separately. Neither construction gives a continuum mass gap. [Wilson comparison](wilson.md) · [Official Yang–Mills problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
