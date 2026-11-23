# Direct Wilson bound, including isotropic spacings

Consider the original $SU(2)$ Wilson regulator with temporal spacing $a$, spatial spacing $b$, $\beta_t=\beta b/a$, $\beta_s=a\beta/b$ and $\lambda=\beta/b$. On every spatial torus of side $L\ge3$, use its zero-temperature transfer vacuum. For **every** sequence $\beta\to\infty$, $0<a\le b$, every volume sequence, and every sign pattern with $n\ge1$ frustrated spatial plaquettes, set $E_*=2\lambda n$. For every $0<\delta<1$,
$$
 \|1_{[0,(1-\delta)E_*]}(Q_a)D_\eta\Omega_a\|^2\longrightarrow0 ,
 \qquad Q_a=-a^{-1}\log(T_a/\|T_a\|).
$$
This includes $a=b$. When $aE_*$ stays bounded, the raw probability of the **entire** band $|E/E_*-1|<\delta$ tends to one. At isotropic spacing $aE_*=2\beta n$ diverges. There the proof controls the lower tail and gives vanishing fixed-positive-time readings as $b\downarrow0$. The upper tail on the relative clock remains open in that regime. All bounds below are independent of the number of links.

## The actual one-slice vacuum

On the unrestricted links let $W=\sum_p(1-x_p)$ and $T=MKM$, with $M=e^{-\beta_s W/2}$. The normalized one-link Wilson convolution has kernel proportional to $e^{\beta_t\cos\theta}$ against Haar, and $K$ is its tensor product. $0\le K\le I$. The full transfer is positive injective and improves positivity; its positive vacuum is gauge invariant and its normalized restriction gives the physical transfer. Put $P=3L^3$ for the number of spatial faces, also the number of spatial links. [Transfer and conventions](../../transfer-operator/hamiltonian-time/)

By operator order $T\le M^2$. For $\epsilon>0$ the logarithm preserves order on $T+\epsilon I$ and $M^2+\epsilon I$, by the integral of the reversed resolvent inequality. Taking the vacuum expectation and sending $\epsilon\downarrow0$ gives
$$
 \beta_s P\,u_a\le-\log\|T\|,\qquad u_a=\langle1-x_p\rangle_{\Omega_a}.
$$
Indeed $\Omega_a$ is a top eigenvector, $M^2$ is bounded below at fixed box and all faces have the same vacuum deficit by symmetry.

To bound the right side, choose a nonnegative smooth normalized one-link bump $f_r$ supported in a ball of radius $r$ about the identity. Its squared gradient integral is at most $C/r^2$ by rescaling the volume form in a fixed coordinate ball. If $k_r=\langle f_r,K_e f_r\rangle$, then
$$
 1-k_r=\tfrac12\int\|R_h f_r-f_r\|^2\,d\nu_{\beta_t}(h)
 \le C/(\beta_t r^2)\qquad(\beta_t\ge1).
$$
Here translation along a shortest geodesic and Haar invariance bound the squared difference by $d(1,h)^2\|\nabla f_r\|^2$. In the unit-round angular coordinate the radial density is proportional to $\sin^2\theta\,e^{-\beta_t(1-\cos\theta)}$ on $[0,\pi]$. Its denominator is bounded below by $c\beta_t^{-3/2}$ by integrating to $1/\sqrt{\beta_t}$. For the second-moment numerator use $\sin\theta\le\theta$ and $1-\cos\theta\ge2\theta^2/\pi^2$ to get $C\beta_t^{-5/2}$. These constants apply to the actual Wilson step.

On the support of the product of these bumps each plaquette deficit is at most $C'r^2$. Positivity of the kernel and nonnegativity of the bump give the Rayleigh lower bound
$$
 \|T\|\ge e^{-\beta_s P C'r^2}k_r^P .
$$
Take $r=A/\sqrt\beta$ with a fixed sufficiently large $A$. For all sufficiently large $\beta$ this lies in the coordinate ball. Since $\beta_t r^2=A^2 b/a\ge A^2$, $k_r\ge1/2$ and $-\log k_r\le2C/(\beta_t r^2)$. The identity $\beta_s\beta_t=\beta^2$ gives
$$
 u_a\le C'r^2+\frac{2C}{\beta_s\beta_t r^2}\le C_0/\beta
$$
uniformly for $0<a\le b$. This bound estimates a local deficit even on arbitrarily large boxes; the vacuum norm itself need not have a volume-uniform lower bound.

## Two time resolutions

Set $\widehat T=T/\|T\|$, $t=aE_*$, $X=n^{-1}\sum_{p\in F_\eta}x_p$. The kinetic convolution commutes with central translations, giving the exact identity
$$
 D_\eta^*\widehat T D_\eta=J\widehat T J,\qquad J=e^{-tX/2}.
$$
The vacuum expectation of $1-X$ is $u_a$, while $\|(1-X)\Omega_a\|^2\le2u_a$. With $j=e^{-t/2}$, the scalar mean-value theorem gives $\|(J-j)\Omega_a\|\le(t/2)e^{t/2}\sqrt{2u_a}$. Since $\widehat T\Omega_a=\Omega_a$ and $\|J\|\le e^{t/2}$,
$$
 \|(\widehat T-e^{-t})D_\eta\Omega_a\|
 \le (e^{t/2}+j)\|(J-j)\Omega_a\|
 \le\tfrac t2(e^t+1)\sqrt{2u_a}.
$$
On $|Q_a/E_*-1|\ge\delta$ the distance of the transfer eigenvalue from $e^{-t}$ is at least $e^{-t}(1-e^{-t\delta})$. Dividing by this number gives a bound on the norm outside the band which tends to zero for bounded $t$, even when $t\downarrow0$; use $1-e^{-t\delta}\ge t\delta e^{-t\delta}$.

For large $t$ first restrict the input to $G=1_{\{X\ge1-\epsilon\}}$ with $0<\epsilon<\delta$. Markov's inequality gives $\|(1-G)\Omega_a\|\le\sqrt{u_a/\epsilon}$. If $P_-=1_{[0,(1-\delta)E_*]}(Q_a)$, then
$$
 \|P_-D_\eta G\Omega_a\|\le e^{t(1-\delta)/2}
 \|\widehat T^{1/2}D_\eta G\Omega_a\|
 =e^{t(1-\delta)/2}\|\widehat T^{1/2}J G\Omega_a\|
 \le e^{-t(\delta-\epsilon)/2}.
$$
The discarded vacuum portion costs its norm only once. Taking $\epsilon=\delta/2$ gives the lower-tail bound $\sqrt{2u_a/\delta}+e^{-t\delta/4}$ for its norm. This order of projection avoids an exponential amplification of the rare configurations on which $X$ is negative.

The two bounds are uniform across the entire range of time spacings. For example, split at $t=(\log\beta)/12$. Below it the first estimate gives a norm at most $C_\delta e^{3t}/\sqrt\beta\le C_\delta\beta^{-1/4}$ for $\delta<1$. Above it the second gives $C_\delta/\sqrt\beta+\beta^{-\delta/48}$. On the isotropic path alone the lower-tail **probability** is $O_\delta(\beta^{-1})$. At a fixed physical time $s>0$ use $\lfloor s/a\rfloor$ actual steps and split the spectrum at $(1-\delta)E_*$. The upper-energy piece costs at most $\exp[-(s-a)(1-\delta)E_*]$. Thus both raw and connected correlations vanish at that time if $b\downarrow0$, $\beta\to\infty$. At zero time the raw norm is exactly one. The vacuum atom tends to zero by the same tail estimate.

## Reading the shift from original links

The expectation $C_\eta(N)=\langle D_\eta\Omega_a,\widehat T^N D_\eta\Omega_a\rangle$ has a positive-history representation. Mark two distinct outgoing transitions $N\ge1$ steps apart in a long periodic history. On each, change the spatial links of its **input** slice to their central translates in the outgoing temporal plaquettes and in that transition's input half of the spatial potential. Take the ratio of the resulting Boltzmann weight to the original one. Leave the incoming transition's half of the spatial potential at that slice unchanged. In $SU(2)$ the two opposite shifts are identical. The marked transition represents the kernel $D_\eta T$, since $(D_\eta T)(U,U')=T(\eta^{-1}U,U')$. One may take this ratio before integration over original temporal links; its expectation then inserts the desired kernel. Each trace and each central sign is gauge invariant under the original local gauge action in this construction.

In the infinite-period limit the two marked steps give $C_\eta(N)$ by the top vacuum projection and cyclicity. Distinct adjacent outgoing steps are allowed. For a finite period keep the transfer trace and its thermal error. Given two such vacuum readings at $N$ and $2N$, $C_\eta(2N)-2cC_\eta(N)+c^2$ is exactly the squared residual for $\widehat T^N$ at $c=e^{-NaE_*}$. Dividing by $[c(1-e^{-NaE_*\delta})]^2$ bounds the outside-band probability. The marked weights are positive but their sizes can grow rapidly with $\beta_t$ and with support. No Monte Carlo precision or uniform relative sampling error follows from the identity. [B4's finite-period setup](../../transfer-operator/periodic-time/) · [Binary seam and omitted-half control](checks.py) · [Isolated $SU(2)$ Wilson transfer](check_wilson.py)
