# Joint spatial–temporal expansion of the plaquette band

A4 computed the second spatial derivative at fixed positive temporal coupling. The static covariance above gives the complementary edge of the expansion at zero temporal coupling. On even periodic cubes $L\ge8$ the two calculations specify the complete joint quartic orientation matrix. With fundamental character parameters $s=I_2(\beta_s)/I_1(\beta_s)$ and $u=I_2(\beta_t)/I_1(\beta_t)$, let $A_c$ be cube-sharing adjacency and $A_e$ edge-sharing adjacency between elementary spatial faces. Their row sums are ten and twelve. On the first excited cluster, identified isometrically with the Haar plaquette basis, the logarithm of the vacuum-normalized transfer divided by $u^4$ has the expansion
$$
 H_{\log}=-2s^2 I+s^4(A_c-\tfrac43 I)+s^2u^2(12I+A_e)+R_L.
$$
The sign convention is the logarithm of the transfer. Energies use its negative. For $N_p=3L^3$, $\|R_L\|\le C(N_p|s|+|u|)^6$ when $N_p|s|+|u|$ is sufficiently small, with absolute constants. [A4's magnetic curvature](../../observable-normalization/replica-gap/band.md) · [Spatial quartic term](spatial.md)

## Why these derivatives belong to one analytic matrix

Here are details needed because the electric band itself collapses at $u=0$. Near zero the inverse function $\beta=4u+8u^3/3+O(u^5)$ is analytic. The one-link Bessel series and its nonzero normalized denominator show $|I_d/I_1|\le(C|u|)^{d-1}$ uniformly for small complex $u$ and all $d\ge2$. One may bound the numerator series absolutely by its leading magnitude times $e^{|\beta|^2/4}$ and bound the leading-normalized denominator away from zero. There is no factor for a trivial edge. The diagonal spin-network expansion then gives $K=P_1+u^4\Pi+O(|u|^6)$ in norm throughout that disk. Holomorphy follows by uniform tails of the finite-degree truncations. On even tori every allowed degree is even by the vertex center constraint and bipartiteness, so $K$ is even in $u$.

For $N_p|s|$ small, $\|M-I\|+|Z-1|=O(N_p|s|)$ also at complex coupling. Write $P=MP_1 M/Z$ (an idempotent), $Q=I-P$. The operator $T/Z=P+O(|u|^4)$ has a uniformly separated simple eigenvalue $l$ near one with Riesz projection $P_t=P+O(|u|^4)$. These estimates follow from the resolvent Neumann series on the radius-$1/3$ circle about one; $P$ is close to $P_1$. For $Q_t=I-P_t$ the product $Q_t P Q_t=(Q_t-Q)P(Q_t-Q)$ is $O(|u|^8)$. Thus the removable quotient
$$
 F=Q_t(T/Z)Q_t/(l u^4)= Q M\Pi M Q/Z+O(|u|^2)
$$
is jointly holomorphic with $\|F-\Pi\|=O(N_p|s|+|u|^2)$. Scalar division may be justified by the Taylor series in $u$ with analytic coefficients. On the positive real axes $F=S_c/u^4$. A second fixed Riesz circle about one gives its shell projection $P_B$. If $J$ includes the Haar plaquette basis, the identification
$$
 W=P_BJ(J^*P_BJ)^{-1/2},\qquad W^\sharp=(J^*P_BJ)^{-1/2}J^*P_B
$$
is analytic by the norm power series. For real couplings $W^\sharp=W^*$ and $W$ is an isometry. Then $H_{\log}=\log(W^\sharp F W)$ is analytic and uniformly bounded on $|s|<c/N_p$, $|u|<c$ by one more norm power series near identity.

At $s=0$ the compressed matrix is exactly identity before taking its logarithm. Both signs of $u$ give the same matrix. On an even torus the link sign used in the static proof flips every spatial plaquette, commutes with $K$, and acts as minus identity on $J$. Conjugation by it exchanges $s$ and $-s$ in both projections and leaves the compressed matrix unchanged. These symmetries remove odd degrees separately. Cauchy bounds on the two-variable Taylor coefficients give the stated uniform degree-six tail on a smaller bidisk.

## Computing the surviving coefficients

At $u=0$ the shell is $UU^*$ with Gram matrix $\Gamma$. Its polar basis $U\Gamma^{-1/2}$ and the basis $W$ are related by a unitary tending to identity as $s\to0$ at each fixed volume. Since the terms below fourth order in $\log\Gamma$ are scalar, the change of basis preserves the fourth-order coefficient. Expanding $\log v(\beta_s)$ and substituting $\beta_s=4s+8s^3/3+O(s^5)$ gives $-2s^2-4s^4/3$. The interaction gives $s^4A_c$.

For the mixed term use A4's vacuum-subtracted log-curvature matrix at spatial **bare** coupling zero. In A4's notation it is $[(h-2c)I+(g-c)(12I+A_e)]/4$. Here $c=1+O(u^4)$, $h=1+O(u^4)$ and $g-c=u^2/2+O(u^4)$: the shared-link spin-zero component of weight $1/4$ has intermediate electric eigenvalue $u^6$, while the remaining spin-one part has an additional $I_3/I_1=O(u^2)$. The curvature multiplies $\beta_s^2/2$. At $s=0$ both transfer representations have the same Haar eigenbasis and the first derivative within the band is zero. Thus a differentiable change of the orthonormal shell identification does not alter this second-order matrix. More explicitly the intertwiner between $MKM$ and $K^{1/2}M^2K^{1/2}$ on this isolated positive band is the polar map of $K^{1/2}M$ restricted there. At each fixed $u>0$ it is smooth and equals identity on the band at $s=0$. This proves the mixed term and recovers the limiting scalar gap curvature $1/4$ in bare spatial coupling from both directions. [A4's recoupling proof](../../observable-normalization/replica-gap/band.md)

## Momentum and the isotropic check

In the face-centered Fourier basis put $t_i=2\cos(p_i/2)$. Unsigned cube incidence has row $t^T$. Unsigned edge-to-face incidence has a symmetric $3\times3$ symbol $E$ with zero diagonal and entries $E_{ij}=t_k$ for the remaining axis. Thus $A_c=tt^T-2I$ and $A_e=E^2-4I$. The two incidences count different pairs of faces even though both recover the constant orientation at zero momentum. When $s=u$, $tt^T+E^2$ has diagonal $|t|^2$ and off-diagonal $2t_i t_j$. Set $\hat p^2=\sum_j(2-2\cos p_j)$, and let $A_{ij}=t_it_j$ off diagonal and zero on diagonal. The energy through order four is
$$
 (-4\log u+2u^2)I-u^4[(50/3-\hat p^2)I+2A].
$$
This reproduces Münster's Eq. (28) at every momentum; at zero momentum the scalar quartic mass coefficient is $-98/3$. The split-coupling formula identifies the two terms that combine on the isotropic diagonal. [Münster, Eq. (28)](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf) · [Matrix identity in Lean](GirthShell.lean)

## An explicit isotropic long-wavelength test

Fix a ratio $a=u/s>0$. The quartic generator after subtraction of the top eigenvalue is
$$
 B_a=A_c-10I+a^2(A_e-12I).
$$
Both adjacency matrices attain their largest eigenvalue on the constant vector, so $B_a\le0$. At $p=0$ the scalar orientation is simple and separated by $12(1+a^2)$ from the transverse pair. For small $p$ its eigenvalue is $-(1+4a^2/3)|p|^2+O_a(|p|^4)$. Indeed the symbol is even in each $p_i$ in the face-centered basis, so second-order motion is the expectation in the scalar unit vector. For the cube term this is $(\sum t_i)^2/3-12=-|p|^2+O(|p|^4)$. For the edge term it is $\sum_{i<j}(t_i+t_j)^2/3-16=-4|p|^2/3+O(|p|^4)$. The normalized Fourier cube-sum ends with vector $t/\sqrt{12}$ tending to that same unit vector.

Take even $n\to\infty$, $L=n^2$, $s=n^{-20}$ and $u=as$. Choose integer lag $k$ nearest to $t n^2/s^4$ for fixed $t>0$, and allowed momentum $p$ nearest to $q/n$. Then $k=O(n^{82})$ while the joint remainder is $O(n^{-84})$. In the shell the logarithm after removal of the measured $r_1=\lambda_1/\lambda_0$ differs from $s^4 B_a$ in norm by at most twice that remainder, by the extremal eigenvalue bound. The exponentials at lag $k$ differ by at most $2k\|R_L\|$, by the integral difference formula for two nonpositive self-adjoint generators. On single-slice plaquette tests the true endpoint map differs from $J$ by $O(\sqrt{N_p}(N_p|s|+|u|^4))$: use the vacuum projection estimate, $\|w-1\|=O(N_p|s|)$ and $|\chi|\le2$ on each column. $W$ also tends to $J$ in norm. The full transfer divided by $r_1$ is a contraction on the excited subspace, so replacing the ends by these band vectors costs $o(1)$ even at these large lags. It follows that the original connected Fourier cube-sum correlation divided by $r_1^k$ tends to
$$
             \exp[-(1+4a^2/3)t|q|^2].
$$
At equal couplings the coefficient is $7/3$. The division removes the rest energy, which diverges in lattice units as $-4\log u$. This diffusion test concerns highly suppressed connected signals deep in strong coupling. It does not identify a relativistic continuum field.
