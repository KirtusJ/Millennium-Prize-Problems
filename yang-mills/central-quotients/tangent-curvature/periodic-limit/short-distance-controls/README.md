# A four-point shape test for free scalar explanations of the trace correlator

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)  
Research program directed by Kirtus Justus

At four vertices of a regular Euclidean tetrahedron, the connected four-point function of the free Maxwell action vanishes. For a nondegenerate quadratic observable in $k$ real scalar generalized free fields, at the same vertices its ratio to the squared edge two-point function is at least $12/k$. This supplies a separated-point test for one class of explanations of A4’s growing-window result. Lower-order short-distance signatures alone can be ambiguous. Below, an explicit gapped free algebra reproduces any specified positive leading two-point coefficient and any specified signed coefficient for one logarithmically suppressed three-point shape. [A4’s site-scalar result](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/f151faa972e6cdd630a151107a64e81c0bd608f5/yang-mills/observable-normalization/transfer-increments/local-action/site-scalar/README.md) · [Z4’s hypothesis (E), §1](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/5b58bcd4035aa94d639404e78dbe47276d211040/yang-mills/z4/attempt/reviews/c1-E/HYPOTHESIS_E.md)

## An equal-edge test

For free Euclidean Maxwell curvature, the covariance between the six independent two-form components at separation $x$ is $(\pi^2|x|^4)^{-1}\bigwedge^2 R_x$, where $R_x=I-2xx^T/|x|^2$. This follows by differentiating the vector covariance $\delta_{\mu\nu}/(4\pi^2|x|^2)$ in Feynman gauge. Connected four-point functions of the centered action are sums over directed four-cycles. Each contraction around a cycle contributes a common constant times the trace of the four covariance matrices in cyclic order. Independent colors add their contributions. [Nikolov, Stanev and Todorov, §3.1, eqs. (3.17)–(3.20)](https://arxiv.org/pdf/hep-th/0305200)

Take the ordered vertices $(1,1,1,0),(1,-1,-1,0),(-1,1,-1,0),(-1,-1,1,0)$. Each squared edge length is eight. For the cycle in the displayed order, the product of the four $R$ matrices acts by $e_1\mapsto e_2\mapsto e_3\mapsto e_1$ and fixes $e_4$. Consequently its trace and the trace of its square are both one. Its exterior square has trace $\tfrac12[(\operatorname{tr}R_{\rm cycle})^2-\operatorname{tr}(R_{\rm cycle}^2)]=0$. Orthogonal tetrahedral symmetries permute the vertices transitively on the six rooted oriented cycles (fix the first vertex). **Each contribution vanishes separately.** Translations, rotations and dilations preserve this zero. In contrast, for four distinct collinear points all four reflections coincide, and the two-form trace of their product is six on every cycle. The zero is specific to shape.

For comparison let $O=\tfrac12:\!\Phi^T Q\Phi\!:$, where $\Phi$ consists of $k<\infty$ jointly generalized free Hermitian scalar fields with real symmetric positive matrix-valued Källén–Lehmann measure, and $Q$ is any real symmetric matrix. At the common edge length $r>0$ the covariance matrix $D(r)$ is positive semidefinite because each Euclidean massive scalar kernel is positive there. Set $H=D(r)^{1/2}QD(r)^{1/2}$. At the tetrahedron Wick contraction gives
$$
 C_2(r)=\tfrac12\operatorname{tr}H^2,\qquad
 C_{4,c}=3\operatorname{tr}H^4,\qquad
 \frac{C_{4,c}}{C_2(r)^2}
 =12\frac{\sum_j\lambda_j^4}{(\sum_j\lambda_j^2)^2}
 \ \ge\ \frac{12}{\operatorname{rank}H}\ \ge\ \frac{12}{k}
$$
whenever $C_2(r)>0$. Here $\lambda_j$ are the eigenvalues of $H$. The factor three is half the number of rooted directed four-cycles. Cauchy–Schwarz gives the first inequality, with equality for equal absolute nonzero eigenvalues. This estimate is uniform in $r$, the spectral measures and the quadratic form at fixed $k$.

In A4’s stated Maxwell window the prediction for the normalized connected tetrahedral ratio is therefore zero, while the collinear contraction survives. The predictions distinguish tensor contractions from all fixed finite scalar quadratic forms above, even with indefinite $Q$ or mixed spectra. They apply to ordinary quadratic forms without derivatives. The Maxwell example itself is free. The shape test supplies neither a general interaction criterion nor an identification of the Wilson theory at its correlation length.

## Leading coefficient in the canonical trace convention

Use $\Theta=(\beta(g)/(2g))F_{\mu\nu}^aF_{\mu\nu}^a$, with the coupling in the covariant derivative, and put $\ell=\log(1/(r\Lambda))$. On a coordinate axis the six Maxwell curvature covariances are diagonal with absolute value $1/(\pi^2r^4)$. Since $F^2=2\sum_{a,\mu<\nu}(F_{\mu\nu}^a)^2$, contracting at distinct points gives $48d_A/(\pi^4 r^8)$ in total, where $d_A=\dim G$. The leading running law $g^2(1/r)\sim(2b_0\ell)^{-1}$ and $\beta(g)=-b_0g^3+O(g^5)$ give the perturbative matching target
$$
 r^8\ell^2\,\langle\Theta(x)\Theta(0)\rangle_c
 \longrightarrow \frac{3d_A}{\pi^4}
 =\frac9{\pi^4}\quad\text{for SU(2)}.
$$
The two factors of $b_0$ from the trace cancel those from the running coupling. In this convention the leading coefficient alone cannot measure $b_0$. A finite change of $\Lambda$ leaves it invariant. Laine, Vepsäläinen and Vuorinen’s vacuum identity contribution in eqs. (2.2)–(2.6), (5.7) and (5.9) gives the same coefficient before and after running. This is perturbative matching at separated points. Proving the asymptotic for a constructed Wilson continuum trace additionally requires the operator identification, physical normalization and control of the ultraviolet remainder. [Laine, Vepsäläinen and Vuorinen](https://arxiv.org/pdf/1008.3263)

## A free algebra matching two leading short-distance coefficients

Let $u(s)=\log(\sqrt{s}/\Lambda)$ and take $M$ with $u(M^2)>1+|\eta|$, for any prescribed $\eta\in\mathbb R$. Use two independent scalar generalized free fields with mass-squared measures
$$
 d\rho_-=A\,\mathbf1_{s\ge M^2}\,\frac{ds}{u(s)},\qquad
 d\rho_+=A\,\mathbf1_{s\ge M^2}
                \left(\frac1{u(s)}+\frac{\eta}{u(s)^2}\right)ds,\qquad A>0 .
$$
Both are positive and polynomially bounded. The generalized free Fock construction gives local positive-energy fields with a mass gap. If an isolated light particle is desired, add the same positive atom at $0<m_*^2<M^2$ in each measure. It changes neither leading ultraviolet coefficient. Below, normal ordering means a local Wightman Wick product evaluated at separated Euclidean points. A local contact extension of an ordinary positive Euclidean covariance density is unnecessary for these calculations. [Dütsch and Rehren, §2, especially eqs. (2.9)–(2.14)](https://arxiv.org/pdf/math-ph/0209035)

Write $K_j(r)$ for the separated-point covariance from the measure $\mathbf1_{s\ge M^2}u(s)^{-j}ds$. The massive kernel is $\sqrt{s}K_1^{\rm Bes}(r\sqrt{s})/(4\pi^2r)$, with $K_1^{\rm Bes}$ the modified Bessel function. Substituting $t=r\sqrt{s}$ yields
$$
 K_j(r)=\frac{1}{2\pi^2 r^4}\int_{rM}^\infty
         \frac{t^2 K_1^{\rm Bes}(t)}{(\ell+\log t)^j}\,dt
 \sim \frac{1}{\pi^2 r^4\ell^j},\qquad j=1,2.
$$
Indeed the contribution below $e^{-\ell/2}$ to the integral times $\ell^j$ is $O(\ell^j e^{-\ell})$, using the fixed positive lower bound on $u$ and $K_1^{\rm Bes}(t)=O(1/t)$. Above that split, the rescaled integrand is dominated by $2^jt^2 K_1^{\rm Bes}(t)$ and the integral of $t^2 K_1^{\rm Bes}(t)$ is two (integrate $-(t^2K_2^{\rm Bes}(t))'$). A fixed-mass atom contributes only $O(r^{-2})$.

Set $O=\tfrac q2(:\!\phi_+^2\!:-:\!\phi_-^2\!:)$ with $q>0$ and let $G_\pm$ be the covariances. Its two-point function is $q^2(G_+^2+G_-^2)/2$. Thus its limit after multiplication by $r^8\ell^2$ is $C=(qA/\pi^2)^2$. For a fixed triangle of distinct points $y_i$, let $d_{ij}=|y_i-y_j|$ and scale its vertices to $r y_i$. The connected third moment is $q^3(\prod G_+(rd_{ij})-\prod G_-(rd_{ij}))$ over the three edges. In the product difference, each single difference $G_+-G_-=\eta A K_2$ contributes one extra inverse logarithm. The three terms with exactly one such factor have equal leading coefficients. Terms with two or three such factors are lower order. Hence
$$
 \lim_{r\downarrow0}r^{12}\ell^4\left(\prod_{i<j}d_{ij}^4\right)
   \langle O(ry_1)O(ry_2)O(ry_3)\rangle_c=3\eta C^{3/2}.
$$
The order $\ell^{-3}$ triangle cancels. Setting $\eta=0$ cancels all odd moments exactly by exchange symmetry. Choosing $qA=\pi^2\sqrt C$ and $\eta=D/(3C^{3/2})$ realizes every pair $C>0$, $D\in\mathbb R$ with this displayed shape. This construction models a scalar local observable. Identifying a stress tensor by translation or dilatation Ward identities, matching a different three-point shape, and controlling the operator product expansion are additional tests. The construction makes no prediction for the actual Yang–Mills three-point coefficient. Its own tetrahedral ratio tends to six since its two leading covariance eigenvalues agree in magnitude.

## Verification

The exact host computation constructs the six-dimensional two-form matrices from minors and checks all six cycles on both the tetrahedron and the collinear control. An independent native PCP OS worker composes four-dimensional reflections first and then takes the exterior-square trace. Two three-generation native deployments completed with the same Lean read-back. The four declarations record the finite coefficient and cycle count and check two polynomial identities. The Bessel estimates, general rank bound and perturbative matching are written arguments. The quadrature uses a scalene triangle with both signs of $\eta$. Run the numerical check with Python, SciPy and SymPy. The native verifier accepts the same pinned runtime arguments as the neighboring interaction packet. [Checker](check.py) · [Native worker](worker.c) · [Lean declarations](ShortDistance.lean) · [Replay](verify.py) · [Verification records](receipts.zip)
