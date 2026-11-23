# Shrinking spectral windows for one unbounded local action

Let $\nu_{\beta,\mu}$ be the joint spectral measure of the centered single-face vector $(Y-\mu Y)\Omega$ for the positive time transfer and the three spatial translations. Write $E=-\log T$ in lattice units, including $+\infty$ on its kernel, and choose $k\in[-\pi,\pi)^3$. At each fixed coupling $Y$ is a bounded cylinder; its variance is uniformly bounded even as its pointwise bound grows. The mixed transform of this finite positive measure at integer time and displacement is the connected covariance in [equation (1)](README.md). Fix the sign of $k$ by the transform $e^{-nE+iz\cdot k}$. The laws below are invariant under reversal of this sign. [Joint transfer representation and periodization](../../../central-quotients/tangent-curvature/periodic-limit/joint-momentum/README.md)

For integers $n\to\infty$ satisfying $n^8\beta^{-1/8}\to0$ and every fixed $u>0$,
$$
 n^8\nu_{\beta,\mu}(E\le u/n)\ \longrightarrow\
       \frac{3u^8}{2\pi^4\,8!}. \tag{2}
$$
Under the probability proportional to $e^{-nE}\,d\nu_{\beta,\mu}$, $(nE,nk)$ converges jointly to
$$
 (H_1+H_2,\ H_1\Theta_1+H_2\Theta_2).
$$
The two pairs are independent. Within each pair $H$ has Gamma(shape 4, rate 1), independent of the direction $\Theta$ with density $3(1-\theta_3^2)/(8\pi)$ relative to ordinary area on the unit sphere. The energy marginal thus has Gamma(shape 8, rate 1). Both limits are uniform in the periodic state selection.

## The two free legs

Set $h_i=2\sin(q_i/2)$, $\omega(q)=2\operatorname{arsinh}(|h|/2)$. For integer $l\ge0$, spatial shift $j$ and $n>0$ the free one-color covariance is
$$
 G((l+1)n,j)=\int_{[-\pi,\pi]^3} e^{-(l+1)n\omega(q)+ij\cdot q}
              \frac{h_1^2+h_2^2}{2\sinh\omega(q)}\,\frac{d^3q}{(2\pi)^3}.
$$
This is the $12,12$ projection symbol after integration over time momentum. Set $p=nq$. Then $n\omega(p/n)\to |p|$ and the scaled numerator-over-denominator converges to $(p_1^2+p_2^2)/(2|p|)$. The scaled amplitude is bounded by $|p|/2$, and $n\omega(p/n)\ge c |p|$ on the scaled cube, uniformly in $n$. Dominated convergence of the phase-free densities in $L^1$ proves, uniformly over all $j$,
$$
 n^4 G((l+1)n,j)=J_l(j/n)+o(1),\qquad
 J_l(y)=\int_{\mathbb R^3}e^{-(l+1)|p|+iy\cdot p}
       \frac{p_1^2+p_2^2}{2|p|}\frac{d^3p}{(2\pi)^3}.
$$
At zero displacement $J_l(0)=\pi^{-2}(l+1)^{-4}$, using $\int_0^\infty e^{-r}r^3 dr=6$ and $\int_{S^2}(1-\theta_3^2)d\theta=8\pi/3$. The ratio $J_l(y)/J_0(0)$ is the mixed transform $\mathbb E e^{-lH+iy\cdot H\Theta}$ of one leg as specified above. Wick contraction of the centered action squares the transform. Put $K_0=3/(2\pi^4)$. [Lattice projection and single-face Fourier convention](../../../central-quotients/tangent-curvature/reflection.md) · [C4’s related calculation for a spatially differenced packet](../../../central-quotients/tangent-curvature/periodic-limit/fourier-decay/README.md)

## From covariances to energy and momentum measures

Push $n^8 e^{-nE}d\nu_{\beta,\mu}$ forward by $(E,k)\mapsto(x,P)=(e^{-nE},nk)$. Its zero moment tends to $K_0$. For any fixed $A$ and $|j|_1\le An$, eventually $|j|_1\le\beta^{1/4}$, since $n=o(\beta^{1/64})$. The comparison and the scaled free integrals therefore give its mixed transforms of order $l$ at $j/n$ up to $o(1)$ uniformly on this range. The transforms converge there to $3J_l(j/n)^2/2$.

For $g\in C_c^\infty(\mathbb R^3)$ periodize it with period $2\pi n$ in each spatial coordinate. On the representative cube the periodization equals $g$ for large $n$ and its Fourier coefficients on $k$ are $(2\pi n)^{-3}\widehat g(j/n)$. The sum of their absolute values is uniformly bounded; the part with $|j|_1>An$ tends to zero uniformly as $A\to\infty$ by rapid decrease. Test by $x^l g(P)$, use the bounded masses to discard this tail, and take the Riemann sum on the retained region. This identifies the limit as $K_0$ times the image of the two-leg probability under $(\varepsilon,P)\mapsto(e^{-\varepsilon},P)$. Such tests are dense in $C_0([0,1]\times\mathbb R^3)$, and the total masses converge. This yields weak convergence and momentum tightness. The limit is supported at $x>0$. After normalization and inversion of $x=e^{-\varepsilon}$ one obtains the claimed joint tilted law. This uses all integer translations, so no extra copies of the momentum distribution are folded into the representative cube.

For (2), integrate $e^\varepsilon \mathbf{1}_{0\le\varepsilon\le u}$ against the unnormalized tilted energy measures. This bounded test has a null discontinuity set in the limiting Gamma(8,1) marginal. The tilt cancels, leaving $K_0\int_0^u \varepsilon^7 d\varepsilon/7!=K_0u^8/8!$. This argument includes any zero-energy weight in the actual measure. Also, for every fixed integer $d\ge1$, the covariance ratio at lags $\lfloor n/2^d\rfloor$ and $n$ tends to $2^{8d}$ on this range, directly by (1) and the large-lag free asymptotic. This supplies the corresponding doubling ratios for a fixed local action at these intermediate times.

## Positive weight at the endpoint

Fix a nonempty finite list of open neighborhoods of points $(\varepsilon,P)$ with $\varepsilon>|P|$. There exist $c>0$ and constants $d_i>0$ such that for $n=\lfloor c\beta^{1/64}\rfloor$ each neighborhood receives at least $d_i n^{-8}$ of the original single-plaquette spectral weight in $(nE,nk)$ for all sufficiently large couplings. Likewise, for any fixed bounded interval $(a,b)$ with $0<a<b$, the energy weight in $(a/n,b/n)$ lies between two positive constant multiples of $n^{-8}$ for sufficiently small $c$.

The two-leg law has positive mass in every such neighborhood. For a point in its strict interior choose a vector $v$ orthogonal to $P$ of length $\sqrt{\varepsilon^2-|P|^2}/2$. Momenta $P/2+v,P/2-v$ give the desired sum. The neighborhood has a nonempty open preimage and the one-leg density in momentum space is positive almost everywhere. Choose a smooth nonnegative product bump bounded by one in the image neighborhood, with positive limiting integral. On $[0,1]$, approximate its energy factor uniformly by a fixed polynomial. For $0<c\le1$, total tilted masses after multiplication by $n^8$ are bounded by a common constant from (1) at lag $n$. Thus the polynomial approximation and spatial Fourier tails cost arbitrarily small fixed errors independent of $c$. Fix these choices first. The retained transforms then cost $O(c^8)$ from (1), multiplied by the fixed coefficient sums, plus the vanishing free discretization error. Choose $c$ small and increase the coupling threshold until the bump retains at least half its limiting integral, simultaneously for the finite list. Since $e^{-nE}\le1$, this lower bound passes to the unweighted measure. The upper energy bound follows immediately from $\nu(E\le b/n)\le e^b\int e^{-nE}d\nu$.

The observable is a single spatial plaquette at every coupling. The power $1/64$ comes from comparing the absolute error in (1) with its free $n^{-8}$ action covariance. At all these scales $nm(\beta,\mu)\to0$ by the [seventh-root lattice gap upper bound](../spatial-packet/strip/README.md); regularity of this same observable at one correlation length remains open.
