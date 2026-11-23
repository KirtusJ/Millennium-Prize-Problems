# Conditioning in the original compact Wilson measure

The argument needs three inputs. First, the finite-link Gibbs specification passes to every fixed-coupling periodic limit because its positive finite-dimensional kernel takes continuous cylinder tests to continuous cylinder functions. Second, at each fixed cube the rescaled conditional interior link density tends, uniformly for compact tree-gauged shell data, to the Maxwell–Dirichlet density in Z4's L3. This statement concerns a finite integral independent of the state selecting its boundary. Third, the scaled actions have a uniform exponential tail in the even-periodic thermodynamic states, and a single action converges in distribution to $\chi^2_3/4$. These last two inputs extend the argument across all even sizes; the dyadic family alone suffices if one uses Z4's pressure calculation. The thermodynamic limit precedes weak coupling throughout. [Finite-link specification and compact-shell estimate](../../../../z4/attempt/reviews/a8-BL34/L3_L4.md) · [Even-periodic moment bound](../../../../central-quotients/tangent-curvature/periodic-limit/pressure.md) · [One-face law in that order](../../../../central-quotients/tangent-curvature/periodic-limit/spectral.md) · [External Wilson stability and generating-function estimates](https://arxiv.org/abs/2205.07376)

## Conditional action law in total variation

Fix $R$. Write $I_R$ for links with an interior endpoint. Every plaquette touching $I_R$ lies in the cube. Thus the conditional interior law given $\mathcal B_R$ uses only the shell links. Fix a tree on the shell, rooted at a shell vertex, and the temporal forest of L3 inside. The latter is fixed by transformations that are identity at shell vertices. Let $b_\ell=\sqrt\beta\log V_\ell$ for the unpinned shell links in this gauge. Equivalently $V_\ell$ is the corresponding fundamental loop based at the shell root. All $b_\ell$ transform by a common rotation when the root frame changes. For each fixed $R$ their norms have moments of all orders uniformly in $\beta,\mu$. Indeed every such fixed loop is a finite product of conjugated elementary plaquettes or their inverses. Bi-invariance bounds its class angle by the sum of their class angles, and $\sqrt\beta\,\alpha_p\le(\pi/\sqrt2)\sqrt{Y_p}$. In particular these shell data are uniformly tight.

In the conditional Gaussian link integral let $D$ be the curl on free interior links after forest pinning, and $S$ the curl on the unpinned shell links restricted to faces touching $I_R$. The curvature there is $D\phi+Sb$. Completing the square gives the mean and variance at the central face:
$$
 H_R(b)=\big[(I-\Pi_R)Sb\big]_p,\qquad
 \Pi_R=D(D^*D)^{-1}D^*,\qquad C_R=(\Pi_R)_{pp}>0 .
$$
This acts separately on each color. Positivity at $p$ follows from a free spatial edge of the face, so $D^*\delta_p\ne0$.

Weak convergence of interior links would not on its own identify an optimal predictor based on arbitrarily fine observations. We use a chart in which the measured action is *exactly* the same function at each coupling. Take the first positive spatial link of $p$. It is free and the oriented plaquette word is $U_e B$, with $B$ independent of $U_e$ when the remaining links are fixed. Replace $U_e$ with $U_p=U_e B$ in the compact integral, an exact Haar change of variable. In this gauge parametrize the new coordinate by
$$
 w=2\sqrt\beta\,\sin(\alpha_p/2)\,\mathbf n_p,\qquad Y=|w|^2/2 .
$$
The principal axis is used off the two central elements, a Haar-null exceptional set. In these coordinates normalized Haar is $(2\pi^2)^{-1}\beta^{-3/2}(1-|w|^2/(4\beta))^{1/2}\,d^3w$ on $|w|<2\sqrt\beta$. This follows by substituting the radius in $\sin^2\alpha\,d\alpha\,d\Omega$. All other free links retain their scaled logarithms.

Uniformly on compact sets of $(w,\phi_{\ne e},b)$, the inverse substitution $U_e=U_pB^{-1}$ has scaled logarithm equal to the unique linear solution of $(D\phi+Sb)_p=w$ plus $O_R(\beta^{-1/2})$, with the constant allowed to depend on the compact set. This follows from the finite-product expansion near the identity, since the coefficient of $\phi_e$ is $+1$. The transformed densities, after removing the common Haar scaling constants, therefore converge uniformly on compacts to the Gaussian densities in this affine coordinate system. The limiting coordinate Jacobian has absolute determinant one. The normalizations converge uniformly on compact $b$ by L3. The normalized transformed laws are uniformly tight there: $|w|\le\sqrt\beta\,\alpha_p$ is bounded above by the sum of the norms of the four original scaled link logarithms, including any boundary entries. L3 gives uniform tightness of the old free link variables. The limiting Gaussian family is also uniformly tight on compact $b$. Integrating on a compact set and bounding both tails now proves convergence of the joint densities in $L^1$, uniformly on compact $b$.

Taking the $w$ marginal and pushing forward by $|w|^2/2$ can only decrease total variation. If $K_R(b)$ is the law of $|H_R(b)+\sqrt{C_R}Z|^2/2$, $Z\sim N(0,I_3)$, we have established
$$
 \sup_\mu\,\mathbb E_\mu\,d_{\rm TV}\big(\mathcal L_\mu(Y\mid\mathcal B_R),K_R(b)\big)\longrightarrow0. \tag{1}
$$
Here we first restrict the random shell to a compact set and bound the error off it by its probability. The vector $w$ in the calculation was in the forest gauge; the scalar $Y$ agrees exactly with the original measurement.

## Identifying the random shell mean

Put $L=|H_R(b)|^2$. Every weak-coupling sequence and choice of periodic states admits a subsequence on which $L$ converges in law to some $L_*$. Only this scalar law matters to $K_R$. The known unconditional one-plaquette limit and (1) imply, for every $t>0$,
$$
 (1+Gt)^{-3/2}
   =(1+C_Rt)^{-3/2}\,
       \mathbb E\exp[-tL_*/(2(1+C_Rt))],\qquad G=1/2 .
$$
The Gaussian norm formula follows by completing the square. It identifies $L_*\overset{\rm law}=v_R\chi^2_3$ with $v_R=G-C_R$. Indeed substitution gives the displayed transform for that law, and the Laplace transform of a finite measure is analytic on the positive half-plane, so agreement on this open interval of arguments gives uniqueness. Every extracted limit is the same. This identification does not require convergence of the sigma fields across couplings.

The map $l\mapsto K(l)=\mathcal L(|\sqrt l\, e_1+\sqrt{C_R}Z|^2/2)$ is continuous in total variation by continuity of translates of a Gaussian density in $L^1$. Tightness and weak convergence of $L$ consequently give convergence of its mixture of kernels in total variation. For a direct justification, restrict to a compact $l$ interval and interpolate $K(l)$ there in the norm of finite measures by a finite continuous partition of unity. The coefficients integrate against weakly convergent probabilities and the norm error is arbitrarily small. The tail cost is bounded by its mass. Equation (1) gives the same statement for the actual unconditional law of $Y$. Its limiting law is $(G/2)\chi^2_3$. By the triangle inequality the actual $A_{\beta,\mu}(R)$ then tends to the expectation of $d_{\rm TV}(K(L_*),(G/2)\chi^2_3)$, which equals $A(u_R)$ after rescaling. The arbitrary sequence argument yields uniformity in $\mu$ at each fixed radius.

For the group-valued plaquette itself the fixed-coupling result is exact:
$$
 d_{\rm TV}\big(\mathcal L_\mu(U_p,\mathrm{ext}),\mathcal L_\mu(U_p)\otimes\mathcal L_\mu(\mathrm{ext})\big)
     =A_{\beta,\mu}(R),
$$
where $\mathrm{ext}$ is the countable collection of exterior links. An arbitrary gauge transformation at the interior base vertex fixes every exterior link and conjugates $U_p$. Given its class and the exterior, $U_p$ is therefore uniform on its conjugacy orbit, the same orbit kernel used for its unconditional law. Haar averaging gives this statement also on exceptional singleton orbits. At fixed $\beta$ the action identifies the conjugacy class. Pushing the joint and product measures forward by the class map and lifting both by the orbit kernel gives both inequalities by contraction. Finally the total variation of a joint law against its product is the mean conditional total variation on these standard Borel spaces (equivalently integrate the conditional densities against their sum). [Bradley, §1.1, coefficient of absolute regularity](https://arxiv.org/abs/math/0511078)

## An explicit shell predictor

Let $B_\beta=\mathbb E_\mu[Y\mid\mathcal B_R]$. Truncating $Y$ at $M$ in (1) first shows
$$
 B_\beta-\big(3C_R+|H_R(b)|^2\big)/2\longrightarrow0
 \quad\text{in }L^2(\mu)
$$
at fixed $R$, uniformly over state selection. In detail the bounded conditional means converge in mean absolute difference. For the true means the expected truncation tail is uniformly small by the scaled-action moment bounds; for the Gaussian kernels it is uniformly small by the shell moments. Both untruncated means have uniformly bounded fourth moments, by conditional Jensen and the same bounds, so convergence in $L^1$ implies convergence in $L^2$. Uniform integrability and the identified law of $L_*$ now give $D_{\beta,\mu}(R)\to\operatorname{Var}(v_R\chi^2_3/2)=3v_R^2/2$.

Write the row of $(I-\Pi_R)S$ at $p$ as $c_\ell$. Replace $b_\ell$ by $\sqrt\beta\,\operatorname{Im}V_\ell$ in the predictor. The difference in each vector has norm at most $|b_\ell|^3/(6\beta)$, so at each fixed $R$ the predictor changes by $O_R(\beta^{-1})$ in $L^2$. The quaternion product identities yield a gauge-invariant formula containing only shell loop traces,
$$
 \widehat Y_R=\frac{3C_R}{2}
  +\frac{\beta}{4}\sum_{\ell,k}c_\ell c_k
    \big(\operatorname{Re}(V_\ell V_k^{-1})-\operatorname{Re}(V_\ell V_k)\big).
$$
All loops begin and end at the same shell vertex. This gives $\|B_\beta-\widehat Y_R\|_2\to0$ and the excess squared prediction risk is exactly $\|B_\beta-\widehat Y_R\|_2^2$ by conditional orthogonality. The finite-coupling optimal predictor itself is already a gauge-invariant shell function by the compact conditional integral. The explicit formula is its fixed-radius weak-coupling approximation. [Wilson path products](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2D0B198BB10DB7ACF56252909590DD6C/9781009290388AR.pdf/Quarks__Gluons_and_Lattices.pdf)
