# A winding-loop upper bound at finite coupling

Let $0<\beta_t<\infty$, $0\le\beta_s<\infty$, and $h\ne0$. In a fixed order of the $m=|h|_1$ active positive coordinate directions, take one step in each direction and repeat this block $L$ times. This staircase closes after $d=mL$ steps. Between two visits to a vertex a nonempty segment that closes modulo $L$ must use each active coordinate either zero or $L$ times. Counts of different active directions along a contiguous segment differ by at most one. For $L\ge4$ this forces every direction to occur $L$ times, giving the entire route. For $m=1$ the same conclusion follows directly along the straight line. Thus the cycle is simple.

Put $f(U)=\tfrac12\operatorname{Tr}U_{\rm cycle}$. It transforms by $\chi_h$, has sup norm at most one, and has mean zero since the vacuum is center invariant. Given all spacetime links except one of its spatial links, $f$ is a unit linear functional on the unit quaternion of this link. The link is in four spatial and two temporal plaquettes. Its conditional density relative to normalized Haar is bounded below by $e^{-8\beta_s-4\beta_t}$, by the range of the corresponding plaquette action. The Haar second moment of a unit quaternion coordinate is $1/4$. This gives the lower norm bound
$$
w=\|f\Omega\|^2\ge e^{-8\beta_s-4\beta_t}/4 .
$$
It holds in open finite time for an interior slice and passes to the infinite-time vacuum in each finite spatial box. [Creutz, compact one-link Wilson law](https://doi.org/10.1103/PhysRevD.21.2308)

For the normalized electric convolution kernel let $k_{\min}=e^{-\beta_t}/Z_t$ with $Z_t=2I_1(\beta_t)/\beta_t$, and $a_n=I_{n+1}(\beta_t)/I_1(\beta_t)$. Define $A_1=\sum_{n\ge0}(n+1)a_n/\sqrt{a_{n+1}}$. The finite-patch estimate gives
$$
\|T^{-1/2} f\Omega\|^2\le (A_1^2/k_{\min})^d .
$$
Indeed the loop is degree one on each of its $d$ distinct links. The proof uses $\beta_t$ only in the kinetic convolution. The magnetic multiplier can be any strictly positive bounded invertible spatial Wilson multiplier in each finite box. Its volume-dependent inverse norm cancels before the patch estimate. A4 checked the inverse domain and the exterior cancellation in the base PR. [Inverse-form proof](../transfer-inverse-moment/inverse-form.md) · [A4's review](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/3#issuecomment-7099028696)

On the energy support of this vector $E\ge E_h$. Therefore $e^{E_h}w\le\int e^E\,d\nu_{f\Omega}\le(A_1^2/k_{\min})^d$, and
$$
E_h\le d\log(A_1^2/k_{\min})+8\beta_s+4\beta_t+\log4 .
$$
A nonzero trial vector gives an **upper** bound for the sector bottom even when it misses the actual ground state of that sector.

As $\beta_t\downarrow0$, the term $n=0$ in $A_1$ is $a_1^{-1/2}\sim\sqrt{4/\beta_t}$. The remainder is $O(1)$: for $x=\beta_t/2\le1$, bound its $n\ge1$ terms by $e^{3/2}x^{(n-1)/2}\sqrt{(n+2)!}/n!$ and use summability at $x=1$. Also $a_1=(\beta_t/4)(1+O(\beta_t^2))$ and $k_{\min}=1+O(\beta_t)$. Consequently $\log(A_1^2/k_{\min})=\log(4/\beta_t)+O(\sqrt{\beta_t})$. Together with the multidirection lower bound this proves the uniform leading logarithm at bounded magnetic coupling. It leaves the constant term undetermined away from the electric axis. [Modified Bessel series](https://dlmf.nist.gov/10.25.E2) · [Winding lower bound](bounds.md)
