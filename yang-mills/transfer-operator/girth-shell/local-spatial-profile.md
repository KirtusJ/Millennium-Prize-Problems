# Spatial profile of the long-lag scalar plaquette correlation

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Consider the isotropic strong-coupling Wilson regulator on the even periodic spatial cubes $L\ge8$ of G4's [local scalar estimate](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/ad1206de753e3a6aea7aeb71d388db506782d9aa/yang-mills/g4/local-scalar-edge). Use the exact infinite-time vacuum and the centered sum $g_y$ of the three elementary traces at site $y$, divided by $\sqrt3$. Write $q_j(y)=\langle g_0\Omega,S^j g_y\Omega\rangle$, $a=j\beta^4$, and $D=7/768$. The mesh is fixed. Both $j$ and $y$ are in lattice units.

With the Fourier weight and branch estimates of G4's pinned momentum proof, the following **absolute error on the spatial ratio** is uniform in the displacement and the side of the cube. For sufficiently small $\beta$, $a\ge1$ and $j\beta^6\le1$,
$$
\sup_{y\in(\mathbb Z/L)^3}\left|
\frac{q_j(y)}{q_j(0)}
-\frac{\sum_{n\in\mathbb Z^3} e^{-4\pi^2Da|n|^2/L^2}\cos(2\pi n\cdot y/L)}
       {\sum_{n\in\mathbb Z^3} e^{-4\pi^2Da|n|^2/L^2}}
\right|
\le C(\beta+a^{-1/2}+j\beta^6).
$$
The error is relative to the on-site correlation scale. It does not provide relative precision in a distant tail where the spatial ratio is small.

## Curvature and the Fourier normalization

For momentum $(s,0,0)$ the diagonal of Münster's quartic orientation matrix is $50/3-4\sin^2(s/2)$. Its off-diagonal part on vectors $(u,v,v)$ has characteristic equation $\lambda^2-8\lambda-128\cos^2(s/2)=0$. At $\lambda(0)=16$ the derivative with respect to $s^2$ is $-32/(32-8)=-4/3$. The diagonal contributes $-1$. Cubic symmetry and independent axis reflections then give the isotropic coefficient $-7/3$ for $|k|^2$. The transfer expansion multiplies this by $\beta^4/256$. This also follows from the equal-coupling limit of the two incidence operators in B4's fixed-box calculation. [Joint expansion](joint.md) · [Münster, Eqs. (26)–(28)](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf)

Use the normalized slice modes $L^{-3/2}\sum_y e^{ik\cdot y}g_y$. Translation invariance separates their spectral measures. The correlation at displacement $y$ is the inverse Fourier sum with divisor $L^3$. Reflection of all momenta, or the reality of the correlation, permits the cosine in place of the phase after summing. In particular a single unit-weight zero mode contributes $L^{-3}$ locally.

## A bound before taking the Fourier transform

Divide each mode's lag moment by $(tb_*)^j$, where $t=(\beta/4)^4$ and $b_*$ is the quartic zero-momentum center in G4's statement. Call the resulting nonnegative weight $W_j(k)$ and let $G_a(k)=e^{-Da|k|^2}$ on the principal momentum grid. Put $Z_a=\sum_k G_a(k)$.

On a fixed small neighborhood of zero, the top weight is $1+O(\beta+|k|)$. Every spectral value $x$ in that branch satisfies
$$
|j\log(x/b_*)+Da|k|^2|
\le C(j\beta^6+a|k|^4+\beta^2a|k|^2).
$$
Indeed $x=b_*-D\beta^4|k|^2+O(\beta^4|k|^4+\beta^6)$, $b_*=1+O(\beta^2)$, and the quadratic remainder of the logarithm is absorbed by the displayed terms. The global bound on $x$ gives $(x/b_*)^j\le C e^{-ca|k|^2}$ when $j\beta^6\le1$. The Gaussian has this bound too, possibly with a different $c$. Apply $|e^u-e^v|\le |u-v|\max(e^u,e^v)$ before integrating over the top spectral weight. The other branches on this neighborhood have total lag contribution at most $C e^{-c'a}$ by their fixed quartic separation or their lower transfer scale. Outside the neighborhood the global bound gives $C e^{-c'a}$ for all branches, using the uniformly bounded total mass per mode. [Mode weights and global bound](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/ad1206de753e3a6aea7aeb71d388db506782d9aa/yang-mills/g4/local-scalar-edge/momentum.md)

For any of the fixed exponents $r=0,1,2,4$,
$$
\sum_k |k|^r e^{-ca|k|^2}\le C_r a^{-r/2}\max(1,L^3 a^{-3/2}),\qquad
Z_a\ge c_0\max(1,L^3 a^{-3/2}).
$$
For the upper bound absorb the power into a wider Gaussian and compare the one-dimensional grid sum with an integral in each coordinate. For the lower bound count the zero mode and the grid points in an inscribed cube of radius proportional to $a^{-1/2}$. Thus $L^3e^{-c'a}/Z_a\le C a^{3/2}e^{-c'a}$. Summation of the preceding mode errors gives
$$
Z_a^{-1}\sum_k |W_j(k)-G_a(k)|
\le C(\beta+a^{-1/2}+j\beta^6).
$$
Normalizing both positive arrays by their own sum costs at most twice this bound in $\ell^1$, by the triangle inequality. Extending the Gaussian to all integer frequency indices costs $O(e^{-c''a})$ after normalization: outside the principal cube reserve half the Gaussian exponent using $|k|_\infty\ge\pi$, and sum the wider Gaussian over the whole grid. The Fourier phases of these added terms have modulus one, including after reduction modulo $L$. This proves the uniform spatial estimate. It gives the same error bound for normalized momentum averages of any test bounded in absolute value by one.

## Three box-size limits

Take $a\to\infty$ and $j\beta^6\to0$. When $L/\sqrt a\to\infty$ and $y/\sqrt a\to\xi$ in shortest periodic coordinates, the ratio tends to $\exp[-|\xi|^2/(4D)]$ by the Gaussian Fourier integral. The unnormalized on-site factor after division by $(tb_*)^j$ is asymptotic to $(4\pi Da)^{-3/2}$. When $L/\sqrt a\to\ell\in(0,\infty)$ and $y/L\to v$ modulo the torus, the ratio tends to the displayed quotient of theta sums with $a/L^2$ replaced by $\ell^{-2}$ and $y/L$ by $v$. The on-site factor is asymptotic to $L^{-3}\sum_n e^{-4\pi^2D|n|^2/\ell^2}$. When $L/\sqrt a\to0$, the ratio tends to one uniformly in the site and the on-site factor is asymptotic to $L^{-3}$. The first limit also applies in the spatial thermodynamic vacuum by fixed-parameter convergence of each local correlation, choosing arbitrarily large tori separately at each parameter value. These are lattice dispersion tests of a vacuum correlator. They give no physical continuum gap.

## Independent checks

Numerical diagonalization of the full three-orientation quartic symbol included all three eigenvalues and the phase offsets of the face centers. For $a=65536$ the displaced-to-on-site ratios for $(L,y_1)=(1024,32),(128,16),(8,2)$ were $0.65138817$, $0.90189992$ and $1.00000000$, respectively, with $y_2=y_3=0$. The Gaussian predictions were $0.65143906$, $0.90191755$ and $1.00000000$. These are effective-symbol checks, separate from the analytic Wilson estimates.

Three measured PCP OS guests checked the one-axis eigenvalue derivative, all 512 inversion identities for a nearest-neighbor symbol on an eight-cube using an eighth root in the prime field of order 97, and the alternating theta ratio at half a period when the one-dimensional Gaussian base is $1/2$. For the last case, summing through $|n|\le6$ and bounding each remaining bilateral tail by $2^{-36}$ gives $0.056894<q_{\rm theta}(1/2)/q_{\rm theta}(0)<0.056895$. The post-exit aggregate check-text SHA-256 was `59418a8a098bcc8a19fc6563a558bc452834f8f399ec013b3260b72a1c78ae8b`.
