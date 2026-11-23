# Magnetic energy at positive flow time

Let $B_i$ be the spatial magnetic curvature of a free Maxwell field in four Euclidean dimensions. Use $d$ independent real color components with propagator normalization one, equivalent to dividing the leading perturbative two-point field by its $g_0^2$. Put $H_s=\frac12\sum_{i,a}(B^a_{i,s})^2$ at flow time $s>0$. Distinguish flow time, with units of length squared, from physical Euclidean separation $t$. These explicit continuum computations serve as controls. The nonlinear Wilson statement with ordered limits is proved [separately](wilson.md).

### Four-dimensional diffusion

At linear order curvature evolves by the scalar heat equation. The doubly flowed scalar propagator in Feynman gauge is $(1-e^{-|x|^2/(8s)})/(4\pi^2|x|^2)$, obtained by integrating the heat kernel over Schwinger parameters from $2s$ to infinity. Longitudinal terms cancel from curvature. At zero spatial displacement, cubic symmetry makes the magnetic covariance diagonal. For $B_3=F_{12}$ apply $-(\partial_1^2+\partial_2^2)$ to the scalar propagator, obtaining the per-component covariance
$$
 c_4(t)=\frac{1-(1+u)e^{-u}}{\pi^2t^4},\qquad u=\frac{t^2}{8s},\qquad c_4(0)=\frac1{128\pi^2s^2}.
$$
Wick contraction yields $C_4(t)=\operatorname{Cov}(H_s(t),H_s(0))=3d\,c_4(t)^2/2$. The profile $c_4(t)/c_4(0)=\int_0^1 2y e^{-uy}dy$ is removable at $t=0$. Thus $C_4(t)/C_4(0)=\mathbb E e^{-A t^2/(8s)}$, where $A$ is the sum of two independent variables with density $2y$ on $[0,1]$. For $0\le t\le\sqrt{2s}$ its second derivative is strictly negative: each integrand has second derivative with the sign of $A(2Au-1)$ and $0<A<2$ almost surely. In particular for $s=1$ at separations $1/2,3/4,1$ the normalized second difference is $-0.0150600460497\ldots$. The support of the two original positive-time test functions can be strictly separated from the plane. Narrow positive-time temporal mollifications also preserve the strict sign by continuity. [Eller and Moore, Sections 2–3, thermal correlators and the flowed propagator](https://arxiv.org/pdf/1802.04562)

A positive spectral measure on $E\ge0$, tested at three equally spaced positive separations $t,t+h,t+2h$, instead gives the integral of $e^{-tE}(1-e^{-hE})^2\ge0$. Finiteness of these three readings suffices. In fact there is **no open real time interval** on which this exact $C_4$ equals any Laplace transform of a positive energy measure. Choose an interior $t_0$ there. The transform is holomorphic for $\operatorname{Re}z>t_0$ by exponential domination and obeys $|L(x+iy)|\le L(x)$ for each $x>t_0$. The explicit $C_4(z)$ is entire after removing its zero-denominator singularity. Equality on the interval implies equality throughout the half-plane by analytic uniqueness. At fixed $x>t_0$, the term $(1+z^2/(8s))e^{-z^2/(8s)}$ grows in modulus as $|y|\to\infty$, and $|C_4(x+iy)|$ grows as a positive constant depending on $x,s$ times $e^{y^2/(4s)}|y|^{-4}$. This contradicts the vertical-line bound.

At large *real* time, $C_4(t)$ is nevertheless extremely close to the unflowed free answer: the relative change is bounded by $2(1+u)e^{-u}$. Fitting finitely many long-time readings can work numerically. Such a fit has different logical force from an exact physical spectral representation. In an original reflection-positive measure a flowed reading $F$ within $L^2$ distance $\eta$ of a genuine half-space observable $G$ obeys $\langle\theta F,F\rangle\ge -2\|G\|_2\eta-\eta^2$ by expanding $F=G+(F-G)$. This approximate inequality is consistent with the signed examples. It requires an actual approximation estimate.

### Spatial diffusion

Sakai and Sasaki retain spatial links and spatial plaquette staples only in the flow equation. The finite-lattice vector field is smooth, gauge equivariant and evolves separately on each time slice. For an original finite-volume Wilson vacuum the resulting bounded real gauge-invariant energy is still multiplication by a function of the slice. Its centered correlation at any positive integer separation is $\langle v,\widehat T^n v\rangle$, $v=(H_s-\langle H_s\rangle)\Omega$, with the same positive transfer as before. The statement is exact for the nonlinear compact lattice evolution. On a finite positive periodic history the reflected form also retains the underlying half-space positivity. [Sakai and Sasaki, Eq. (3) and Figs. 4–6](https://arxiv.org/pdf/2211.15176)

For the free benchmark, frequency integration gives covariance $(|p|/2)(I-\hat p\hat p^T)e^{-2s|p|^2-|t||p|}$ in spatial momentum space. The $2/3$ angular average of a diagonal transverse projector gives
$$
 c_3(t)=\frac1{6\pi^2}\int_0^\infty p^3 e^{-2sp^2-|t|p}\,dp,\qquad
 c_3(0)=\frac1{48\pi^2s^2}.
$$
The local point-energy reading has $C_3(t)=3d\,c_3(t)^2/2$. Its positive measure is the self-convolution of the measure in $c_3$, multiplied by $3d/2$. At large time $C_3(t)\sim3d/(2\pi^4t^8)$ and the low-window mass is asymptotic to $3d\,\epsilon^8/(2\pi^4\,8!)$. The spatial-flow magnetic mean is $3d\,c_3(0)/2=d/(32\pi^2s^2)$. In the usual gauge-field convention multiply this leading mean by $g_0^2$. Its ratio to the full four-dimensional-flow *magnetic* mean is $8/3$; its ratio to the standard four-dimensional-flow *total* action mean $3d/(128\pi^2s^2)$ is $4/3$. These factors have distinct denominators. The comparison concerns infinite-volume tree normalization. Finite-volume schemes and nonlinear renormalization need separate matching. [Lüscher, Eq. (2.32)](https://arxiv.org/pdf/1006.4518)

For the zero-spatial-momentum operator, integrate the connected two-point function over one relative spatial displacement. Equivalently use the variance per unit volume of the spatial integral in the infinite-volume limit. Parseval fixes the two internal momenta to be opposite; the squared transverse projector has trace two. The connected law is
$$
 G_s(t)=\frac d{8\pi^2}\int_0^\infty p^4e^{-4sp^2-2p|t|}dp,\qquad
 \rho_s(dE)=\frac d{256\pi^2} E^4 e^{-sE^2}\,dE .
$$
Thus $\rho_s([0,\epsilon])\sim d\epsilon^5/(1280\pi^2)$ and $G_s(t)\sim3d/(32\pi^2|t|^5)$. At zero $G_s(0)=3d/(2048\pi^{3/2}s^{5/2})$. A localized point reading integrates two momenta independently; replacing it by a volume-integrated zero-momentum reading changes the threshold power. The endpoint behavior is a **free** control. A positive mass obtained by spectroscopy in an interacting ensemble is a different physical claim.
