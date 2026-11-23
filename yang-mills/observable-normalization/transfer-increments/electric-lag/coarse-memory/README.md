# Memory of three straight coarse Wilson slices

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Three stationary straight coarse slices of electric SU(2) form a Markov chain at zero spatial coupling. For every sufficiently small nonzero magnetic coupling $b$ at fixed volume, conditioning on the **entire middle coarse orbit** leaves measurable dependence between the two end slices. One fundamental coarse-square trace detects it. Its mean conditional covariance starts at order $b^2$ with an explicit positive coefficient. The conditional mutual information between the two full end slices starts at order $b^4$ with a strictly positive coefficient. The quadratic memory estimate below is uniform in spatial volume at the level of its Taylor coefficient. A common nonzero-coupling interval through isotropic refinement and a positive physical mass gap remain open. [Electric coarse transfer](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/660fe73/yang-mills/g4/full-attempt/blocking/README.md)

## Composition through a coarse slice

Fix finite even spatial side $L$, $\ell\ge2$ dividing $L$, $L/\ell\ge4$, positive temporal coupling $g$, and integer lag $n\ge1$. Let $X_j$ be the fine vacuum orbit chain and $Y_j$ its straight spacing-$\ell$ coarse orbit. Write $K_b$ for the reversible fine transfer, $P_b$ for conditional expectation onto a coarse slice, $S_{b,n}=P_b K_b^n$ restricted to coarse functions, and $R_{b,n}=(I-P_b)K_b^n$ on that same domain. In the stationary inner product,

$$
S_{b,2n}-S_{b,n}^2=R_{b,n}^*R_{b,n}.
$$

Indeed insert $I=P_b+(I-P_b)$ between the two self-adjoint transfers. In particular for any bounded real coarse $f$ the quadratic form on the left equals

$$
M_b(f)=\mathbb E_b\operatorname{Cov}_b(f(Y_{-n}),f(Y_n)\mid Y_0)
=\mathbb E_b\operatorname{Var}_b((K_b^n f)(X_0)\mid Y_0).
$$

The past and future are independent given $X_0$ and their conditional means there coincide by reversibility. Further conditioning on $Y_0$ gives the last identity, including nonnegativity within each middle fiber. At the electric point $R_{0,n}=0$. Since $K_0^nf$ is coarse it can be subtracted before applying $I-P_b$ at every coupling. Hence $R'_{0,n}f=(I-P_0)(K_b^n)'_0 f$ and $M_b(f)=b^2\|R'_{0,n}f\|_0^2+O(b^3)$. Changes of both the vacuum and the conditional expectation are included. At even $\ell$ the coarse history law is even in $b$, so the remainder is $O(b^4)$ at fixed $L,g,n$. [Sign symmetry and derivative on the full coarse space](../all-coarse/README.md)

## A single-square witness

Take $f=\operatorname{Tr}U_{\square_\ell}$ with its unnormalized real SU(2) trace. Write $k=4\ell$, $q=I_2(g)/I_1(g)$, $a=I_3(g)/I_1(g)$, $r=q^k$, $\lambda=q^4$. Set
$$
D_n(t)=\frac{t-\lambda r}{1-\lambda}\sum_{j=0}^{n-1}t^jr^{n-1-j},\qquad
u_d=q^{k+4-2d},\qquad v_d=u_da^d.
$$
The exact quadratic coefficient is
$$
A_n(f)=\lim_{b\to0}M_b(f)/b^2
=\frac1{16}\sum_{d=1}^2 M_d\{D_n(u_d)^2+3D_n(v_d)^2\},\qquad
(M_1,M_2)=(4k-8,4).
$$

A magnetic face meeting the loop along $d$ edges contributes two orthonormal fine readings, with amplitudes $D_n(u_d)/4$ and $\sqrt3 D_n(v_d)/4$. Distinct magnetic faces have distinct parity under fine-link center flips. Edge-disjoint insertions cancel in the moving-vacuum derivative. Squaring the residual therefore gives the formula without any spectral defect denominators. At the four inside corners $u_2=r$, $D_n(r)=nr^n$, giving $A_n(f)\ge n^2r^{2n}/4>0$. The positive coefficient rules out a Markov coarse history for every sufficiently small nonzero $b$ at each allowed finite volume. Knowing the entire middle straight orbit gives a weaker prediction than knowing the hidden fine state, even when each endpoint reading uses only this one square. [Shared-path decomposition and proof](../bends/README.md)

For arbitrary centered coarse $F$, the previous result gives
$$
\frac{\|R'_{0,n}F\|_0^2}{\langle F,(I-K_0^n)F\rangle_0}
\le \left[\frac{4\sqrt\ell}{q^{-4\ell n}-1}
             \left(\frac1{1-q^4}+n\right)\right]^2 .
$$
Indeed $0\le K_0^n\le I$ makes the fine defect norm at most the Haar norm. Test the normalized bilinear estimate against $h=R'_{0,n}F$. The resulting upper bound is uniform over spins, coarse readings and allowed volumes. With $b=(1-q)\eta$, $g\to\infty$, $-n\log q\to\tau>0$ at fixed mesh, the largest quadratic coefficient in $\eta$ relative to the coarse defect has large-mesh order $\ell e^{-8\ell\tau}$. For the lower order take the $k$ positive transverse singlet modes alone in the square witness. Their contribution is $kD_n(u_1)^2/16$ and $(1-q)D_n(u_1)\to e^{-k\tau}(1-e^{-2\tau})/4$. The square has coarse defect $1-r^n\to1-e^{-k\tau}$. These are ordered limits of coefficients.

## Information in the hidden middle slice

Use natural logarithms. Let $Q$ be the coarse Haar orbit marginal at zero coupling. Denote by $p_b(z\mid x)$ the density against $Q$ of the future coarse orbit at lag $n$ given the fine state $x$. At $b=0$ this density depends on $x$ only through its coarse orbit $y$; write it as $p_0(z\mid y)$. Let $\nu_b(dx\mid y)$ be the conditional fine vacuum. Define
$$
d(x,z)=\partial_b p_b(z\mid x)|_0,\qquad
C_y(z,w)=\operatorname{Cov}_{\nu_0(\cdot\mid y)}(d(X,z),d(X,w)).
$$
At fixed $L,g,n$ the conditional mutual information is
$$
I_b(Y_{-n};Y_n\mid Y_0)=B_n b^4+O(b^5),\qquad
B_n=\frac12\int \frac{C_y(z,w)^2}{p_0(z\mid y)p_0(w\mid y)}
                  \,Q(dz)Q(dw)Q(dy)\ \ge\ \frac{A_n(f)^2}{32}>0 .
$$
For even mesh the remainder improves to $O(b^6)$. The lower bound uses the particular square above. The integral gives the coefficient for the **whole coarse orbit triple**. No volume-independent upper bound for this information coefficient is claimed.

To see why the expansion is legitimate, work first on compact fine link space with product Haar reference. The fixed-volume electric kernel has a strictly positive continuous density, bounded above and below. Gauge averaging preserves those bounds. The symmetric magnetic weights are bounded analytic functions. The leading eigenvalue is simple, and its eigenfunction, normalized to be one at zero, is analytic locally in the uniform norm by the isolated eigenprojection and the smoothing integral equation. The normalized Markov kernel and its fixed finite powers therefore have a local uniform expansion with a positive lower bound. Conditional integration of the terminal fine link over its **reference Haar** fiber gives $p_b(z\mid x)$ with the same bounds in essential supremum norm. Likewise $\nu_b$ is obtained by tilting the reference fiber by the squared vacuum divided by its conditional average. This denominator stays away from zero. All the bounds in this paragraph may depend on $L,g,n$.

Given the middle coarse value $y$, the true endpoint pair density is the $\nu_b$-average of $p_b(z\mid X)p_b(w\mid X)$; the product of its marginals is the product of the two averages. Their difference is the covariance of the two densities. The common electric terms are constant on the fiber, so this difference is $b^2 C_y(z,w)+O(b^3)$ uniformly in the essential sense. Both joint laws integrate to one. Taylor expansion of relative entropy about the positive product law cancels the linear term and gives the displayed integral after integration over the middle marginal, which is $Q$ at zero. Fixed-volume analyticity and sign symmetry give the improved remainder for even mesh. Finally the joint triplet law and its conditionally independent surrogate differ in the expected test $f(z)f(w)$ by $M_b(f)$. The test has sup norm at most four. Pinsker’s inequality in nats gives $I_b\ge M_b(f)^2/32$. [Conditional mutual information and Markov chains](https://onlinelibrary.wiley.com/doi/10.1002/0471200611.ch2) · [Native PCP replay and numerical controls](checks.md)
