# The angular energy spectrum on fast trajectories

Use the [ordinary-profile Wilson limit](../ordinary-profile.md) and its [compact-group extension](../../lie-curvature/physical-scale.md) with the first-order box and coupling bounds in the [geometry](README.md). A common time-axis transport of both colors on each slice preserves their angle. The joint linear tests tend to a Gaussian pair $(X_f,X_g)$ with independent copies in each of $d$ orthonormal color coordinates. Write $D>0$ for the packet translation distance and
$$
 q(p)=\frac{|\widehat\psi(p)|^2(p_1^2+p_2^2)}{2(2\pi)^3 |p|},\qquad
 v_t=\int q(p)e^{-|t||p|}dp,\quad
 w_t=\int q(p)\cos(Dp_1)e^{-|t||p|}dp .
$$
The mixed covariance in each color at two times is the matrix with diagonals $v_t$ and off-diagonals $w_t$. The equal-time values are $v,w$. Both $v+w$ and $v-w$ are positive because $\widehat\psi(0)\ne0$ and $1\pm\cos(Dp_1)$ is positive off null sets. The Gaussian marginals give probability zero to each denominator's zero set. The bounded angular readings therefore converge jointly in law and in all joint moments at any fixed finite set of physical times, including time zero.

Use the sum and difference coordinates $P=(X_f+X_g)/\sqrt{2(v+w)}$ and $M=(X_f-X_g)/\sqrt{2(v-w)}$. These are independent standard $d$-vectors at a slice and have cross-time scalar correlations $\lambda_\pm(t)=(v_t\pm w_t)/(v\pm w)$ within their respective modes. Their cross-mode covariances vanish at all times. Each $\lambda_\pm$ is the Laplace transform of a probability $\mu_\pm$, the $|p|$ pushforward of $q(p)[1\pm\cos(Dp_1)]\,dp/(v\pm w)$. At finite positive $t$ both transforms lie strictly between zero and one.

Set $z=(v+w)|P|^2$, $s=(v-w)|M|^2$, and $k=(P\cdot M)^2/(|P|^2|M|^2)$. The limiting angular reading is
$$
 H(P,M)=\frac{z-s}{\sqrt{(z+s)^2-4zs k}} .
$$
It is invariant under joint orthogonal rotations and under changing the sign of either entire vector. Almost surely $s,z>0$ and $k<1$. Holding $s,k$ fixed gives
$$
 \partial_z H=\frac{2s(z+s)(1-k)}{[(z+s)^2-4zs k]^{3/2}}>0 .
$$
The normalized second Hermite coefficient for the sum mode is
$$
 b_+=\mathbb E\!\left[H(P,M)\frac{|P|^2-d}{\sqrt{2d}}\right]>0 .
$$
Conditional on the directions and $|M|$, the variable $|P|^2$ still has its nondegenerate chi-square law. Its covariance with a strictly increasing function of itself is positive by taking two independent copies and averaging half the product of their differences. Its conditional mean is $d$, proving the assertion. Simultaneous radial scaling leaves $H$ unchanged; the direction of a standard $2d$-dimensional Gaussian is independent of its total radius. Thus the corresponding coefficient $b_-$ for $M$ equals $-b_+$. Orthogonal invariance makes the centered radial quadratic the only invariant at pure bidegree $(2,0)$ or $(0,2)$.

Let $h_{ij}$ be the sum of squared coefficients of $H-\mathbb E H$ in the normalized multivariate Hermite basis at degrees $(i,j)$. Only even $i,j$ occur and $h_{20}=h_{02}=b_+^2>0$. Parseval gives $\sum h_{ij}=\operatorname{Var}H$. For two standard normal scalars with correlation $\lambda$, the expectation of their two exponential generating functions for the probabilists' Hermite polynomials is $\exp(\lambda xy)$. Coefficient comparison and tensorization give diagonal weights $\lambda^n$ for normalized Hermites. Truncating the $L^2$ expansion and using Cauchy–Schwarz to pass to the limit gives the connected reading and its physical-energy measure
$$
 C(t)=\sum_{i+j>0} h_{ij}\lambda_+(t)^i\lambda_-(t)^j,\qquad
 \nu=\sum_{i+j>0} h_{ij}\,\mu_+^{*i}*\mu_-^{*j},
$$
where a zeroth convolution is the unit mass at zero. In particular $C(t)\ge b_+^2\lambda_+(t)^2>0$ and $C(t)/C(0)>0$ at each finite $t$. This holds for the actual variance-normalized Wilson readings in the limit. For $SU(2)$ there is an explicit check at $w=0$: $b_+=(\mathbb E\chi_3)^2/(3\sqrt6)=8/(3\pi\sqrt6)$. Indeed then $X_f,X_g$ normalized by $\sqrt v$ are independent isotropic normals; only their dot product in $|P|^2-3$ contributes and the mean squared directional cosine is $1/3$.

The finite-cutoff centered spectral measures at physical energy $-r\log\widehat T$ tend weakly on the compactified energy axis to $\nu$. The bounded readings give convergence of total mass. At integer physical times $j\ge1$, replacing $e^{-jE}$ by $e^{-\lfloor rj\rfloor E/r}$ costs $O(1/(rj))$ uniformly in $E\ge0$. Polynomial approximation after the change $x=e^{-E}$ identifies the full measure, including the endpoints. Its radial ingredients have densities and it has no atoms. [Transfer and Fourier convention](../spectrum.md)

For $J=\int\psi$ put $a=|J|^2/\pi^2$. Spherical integration of $q(p)$ gives density $(a/6)E^3+O(E^5)$ at zero. The plus factor doubles the leading density and the minus factor contributes $O(E^2)$. Therefore $\lambda_+(t)\sim [2a/(v+w)]t^{-4}$ and $\lambda_-(t)=O(t^{-6})$. The pure minus quadratic contributes $O(t^{-12})$, and the terms of total degree at least four together are bounded by $\sum h_{ij}\max(\lambda_+,\lambda_-)^4$. On $[0,\epsilon]$ their analogous measure bound is $\sum h_{ij}\max(\mu_+([0,\epsilon]),\mu_-([0,\epsilon]))^4$. Integrating the leading plus convolution over a simplex yields
$$
 C(t)\sim Kt^{-8},\qquad \nu([0,\epsilon])\sim K\epsilon^8/8!,\qquad
 K=b_+^2\left(\frac{2a}{v+w}\right)^2>0 .
$$
In particular each sufficiently small fixed window $(\epsilon/2,\epsilon)$ retains positive raw weight. These statements concern the fast free branch; the [slow estimate](slow.md) follows from integrating over this same connector in the original Wilson measure.
