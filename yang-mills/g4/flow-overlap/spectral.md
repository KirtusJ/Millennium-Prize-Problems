# Which part of a flowed reading survives in the strong-coupling band

Set $t=(\beta/4)^4$ and $I_{\beta,\eta}=\{\lambda:|\lambda/t-1|\le\eta\}$ for the eigenvalue variable of the positive, vacuum-normalized Wilson transfer. Given a bounded real gauge-invariant single-slice reading $G$, write $\nu_{\beta,L}^G$ for the transfer spectral measure of its centered vector and $C_j=\int\lambda^j\,d\nu_{\beta,L}^G$. For $\eta=\beta^{1/4}$ and each fixed finite lattice flow time $u$ we obtain

$$
\lim_{\beta\downarrow0}\sup_{L\ {m even},\ L\ge4}
\left|\nu_{\beta,L}^{F_p\circ\Phi_u}(I_{\beta,\eta})-
\sum_{C}\left|\mathbb E_H[(F_p\circ\Phi_u)\chi_C]\right|^2\right|=0 .
$$

Here $C$ runs over distinct unoriented simple spatial circuits of length four on that torus. Each $\chi_C$ is the **unnormalized** fundamental trace. Its Haar norm is one. The sum includes straight winding circuits at $L=4$. For larger even sides only elementary plaquettes occur. The summands and the Haar law refer to the same spatial side as the interacting measure. In particular the [positive Haar witness](README.md) gives a lower limit at least $e^{-64u}/(16N)$ with the volume-independent upper bound on $N$. Energies in the band satisfy $aE=4\log(4/\beta)+O(\beta^{1/4})$. Any certified weight $w$ gives $C_k\ge w[t(1-\eta)]^k$ for every integer $k\ge1$.

## The limiting weight for a cylinder function

Start with $G$ supported on at most $m$ spatial links. B4's joint analytic estimate bounds its connected correlators uniformly on a common complex coupling disk by $2\|G\|_\infty^2e^{2m}$. The forest argument requires a cycle of at least four distinct temporal plaquettes in every intervening slab. The total-degree $4j$ coefficient of $C_j$ therefore contains no spatial coupling. Evaluate that coefficient in the Wilson model with spatial coupling zero and normalized temporal coupling $\beta$ in the original action convention. These are inputs from B4's written proofs. The bounds hold on open time intervals and pass to their vacuum limit. [Analytic bound](../../transfer-operator/connected-rectangles/analyticity.md) · [Slab argument](../../transfer-operator/connected-rectangles/surfaces.md)

The electric transfer then acts by central convolution on each link of a product-Haar slice. In the gauge-invariant Peter–Weyl decomposition, edge labels $n_e$ are twice the spins, and the eigenvalue is $\prod_e h_{n_e}$ with $h_n=I_{n+1}(\beta)/I_1(\beta)$. Here $h_1=\beta/4+O(\beta^3)$ and $h_n\le h_1^n$. The latter follows by multiplying the successive modified Bessel ratio inequalities. A vertex with just one nontrivial incident representation has no invariant tensor. Every nonempty support therefore contains a cycle. If $\sum n_e=4$, all four labels must equal one on one simple length-four circuit. Its invariant tensor is unique; the loop character spans it. Distinct circuits are orthogonal by integrating a link in their symmetric difference. At $L=4$, a lifted four-step path with nonzero winding must move all four steps in a single direction. At $L>4$ the lift closes and the four distinct edges form a square. [A4's electric transfer and multiplicity argument](../../observable-normalization/replica-gap/electric.md) · [Baricz and Ponnusamy, Eq. (1)](https://arxiv.org/pdf/1010.3346)

Let $W_L(G)=\sum_C|\mathbb E_H[G\chi_C]|^2$. The centered electric sector complementary to degree four has norm at most $h_1^5$. Its contribution at lag $j\ge1$ is at most $\|G\|_\infty^2h_1^{5j}$. The remaining electric contribution is $h_1^{4j}W_L(G)$. The uniform analytic bound now yields on the **isotropic** axis

$$C_j/t^j=W_L(G)+O_{m,\|G\|_\infty,j}(\beta),\qquad j=1,2,3.$$

Indeed all lower coefficients vanish, the degree $4j$ coefficient was just computed, and Cauchy's inequalities bound the remainder on any smaller common disk. This comparison uses the same $G$ on both measures at a given $L$; a family of cylinder functions with bounded support counts and sup norms obeys the same error estimate. The fourth power per time step agrees with the elementary plaquette tube in the primary strong-coupling calculation. [Langelage, Münster and Philipsen, Eqs. (40)–(42)](https://arxiv.org/pdf/0805.1163)

Write $x=\lambda/t$. The nonnegative integral $\int x(x-1)^2\,d\nu=C_3/t^3-2C_2/t^2+C_1/t$ is $O(\beta)$. Outside the relative band the **first moment** is therefore $O(\beta/\eta^2)$. Inside the band the first moment differs from the mass by at most $\eta\,\nu([0,1])$, where the total is bounded by $\|G\|_\infty^2$. Since the full first moment tends to $W_L(G)$ this proves the formula, with error $O(\beta^{1/4})$ for fixed cylinder size. A zero transfer eigenvalue contributes no first moment. [Lean integral estimate](HaarOverlap.lean)

For $G=F_p\circ\Phi_u$, pad exterior links by identity beyond radius $R$ around $p$ and apply the full forward spatial flow to the padded field. The corresponding reading differs by at most $8T_R$ uniformly over initial configurations and sides. Gauge averaging over the vertices incident to the kept links produces a gauge-invariant cylinder function with the same error. Both centering and orthogonal projection are contractions. Thus the norms of the projected vectors differ by at most $8T_R$ in either the Haar or Wilson Hilbert space. Take $\beta\downarrow0$ at fixed $R$, then $R\to\infty$. No cylinder convergence rate uniform in $u$ is assumed. At fixed strong coupling the infinite-volume correlators of the flowed reading follow by the same approximation in the unique strong-coupling vacuum. For the lower bound the spectral measures live on the compact transfer interval $[0,1]$, and the band is closed. Taking spatial volume to infinity retains the weight bound.

## Refinements from director review

For the ordinary flowed elementary plaquette the straight winding terms at side four vanish exactly under Haar. Fix a transverse periodic cut and multiply every link crossing it by the central element $-I$. This preserves Haar and every elementary plaquette trace, since each plaquette crosses the cut an even number of times. The transformation is an isometry preserving the spatial Wilson action, hence it commutes with its gradient flow. The flowed elementary reading is invariant, whereas the fundamental character of a straight loop winding through that cut changes sign. Their Haar inner product vanishes. A general cylinder function can have winding overlap, so the full length-four projection in the cylinder theorem still includes these circuits. [A4's director review](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/2#issuecomment-7098437858)

For cylinders of fixed support size and bounded sup norm the three moments also give an error $O(\beta/\eta^2)$ in the band mass whenever $0<\eta\le1/2$. Indeed $p(x)=2x-x^2$ integrates to $W_L+O(\beta)$. Inside the closed band, $|1-p(x)|=(x-1)^2\le x(x-1)^2/(1-\eta)$. Outside it, $|2-x|\le1+|x-1|$ gives $|p(x)|\le(\eta^{-2}+\eta^{-1})x(x-1)^2$ including at $x=0$. Thus the integral of $p$ and the band mass differ by $O(\beta/\eta^2)$. At $\eta=\beta^{1/4}$ the error is $O(\sqrt\beta)$. The passage to the ordinary flowed reading still uses the ordered limit in the cylinder radius. B4 and A4 independently compiled the eight Lean declarations and cross-checked the strong-coupling identification at the original head. [B4's check](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/2#issuecomment-7098324184) · [A4's estimate](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/2#issuecomment-7098437858)

## A finite-coupling bound that allows the flow time to grow

Take $h=e^{-32u}$, $Q_R$ and $Z_R$ from the [Haar estimate](README.md). Let $m$ count the spatial links in the radius-$R$ ball and the boundaries of the $N$ nearby faces. The Wilson conditional density on those links, given the entire exterior, lies between $e^{-12\beta m}$ and $e^{12\beta m}$ relative to product Haar. Each of at most $6m$ incident spacetime faces has deficit at most two. Put $d=e^{12\beta m}-1$. With $g=F_p\circ\Phi_u-1$, one has $|g|\le1$, $|Z_R|\le N$ and $\mathbb E_H Z_R=0$. Replace $g$ by its padded reading with error at most $8T_R$ in each measure. The two replacements and the marginal density comparison show

$$
|\operatorname{Cov}_\beta(g,Z_R)-\mathbb E_H[gZ_R]|\le16NT_R+2Nd,
\qquad \operatorname{Var}_\beta Z_R\le e^{12\beta m}N/4 .
$$

For $0<\beta\le2^{-256}$, the previous bare-plaquette bound controls the squared scaled second deviation by $2^{123}\beta$. Thus the norm of each centered bare plaquette outside $I_{\beta,\eta}$ is at most $2^{62}\sqrt\beta/\eta$. Apply the triangle inequality to their sum and use $\|g-\mathbb E_\beta g\|_2\le1$. Writing $y_+=\max(y,0)$ gives the explicit lower bound

$$
\nu_{\beta,L}^{G}(I_{\beta,\eta})\ \ge\
\frac{4e^{-12\beta m}}{N}
\left[\frac h4-\big(\tfrac43+16N\big)T_R-2Nd-2^{62}N\sqrt\beta/\eta\right]_+^2 .
$$

In fact the bracket lower-bounds the overlap of the two band-projected vectors before its positive part is taken. Cauchy–Schwarz and the preceding variance bound finish the proof. For a concrete case beyond the earlier small-time interval, take $u=1$, $\beta=2^{-1024}$, $\eta=2^{-256}$ and $R=96$. The resulting weight exceeds $10^{-40}$, uniformly in spatial volume. The rational check uses $h>3^{-32}$, $e^x-1\le2x$ for $0\le x\le1/2$, and a geometric majorant starting with $16^{97}/97!$. This is a conservative certificate. [Bare second-moment constant](../spatial-flow-variance/concentration.md) · [Exact arithmetic](control.py)

Choose $R=\lceil256(1+u)\rceil$. Both $m,N\le3(2R+7)^3$. The factorial bound $n!\ge(n/e)^n$ gives $T_R\le2^{-R}$, since $R+1\ge32eu$. For $R\ge256$, $(4/3+16N)\le2^{R/2-5}$: it suffices to use $N\le81R^3$, check at 256, and use $((R+1)/R)^3<\sqrt2$ thereafter. Thus the tail cost is at most $h/32$. For $\eta=\beta^\gamma$, $\gamma>0$, and $0\le u\le\alpha\log(1/\beta)$, the last cost divided by $h$ tends uniformly to zero when $32\alpha+\gamma<1/2$. The density cost divided by $h$ also tends to zero, since $m,N=O((1+u)^3)$ and $d=O(\beta m)$ there. For all sufficiently small positive $\beta$ the weight is at least a constant times $e^{-64u}/(1+u)^3$, uniformly on this range. The lower bound can decrease with $u$. The energy band and the flow clock in this calculation are microscopic.
