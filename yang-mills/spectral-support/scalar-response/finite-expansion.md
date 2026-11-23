# Source-dependent weak coupling on a finite open box

Consider all positively oriented elementary plaquettes on a finite rectangular cell complex with free boundary. Use the defining trace of $SU(2)$, $D_p=1-\tfrac12\operatorname{Tr}U_p$, and
$$
 Z(\beta,w)=\int\exp[-\beta\sum_p w_pD_p]\,dU,\qquad w_p>0 .
$$
The integration is over the actual compact links with normalized product Haar measure. A rooted spanning tree can be set to the identity exactly. Successively use the tree-link variables as the gauge transformations of the nonroot vertices. Left and right Haar invariance preserve each remaining link integral, and the tree integrations contribute one. Let $n$ be the remaining number of links. The signed face-by-chord matrix is $B$, with path order retained separately for the nonlinear terms. Write $H=B^\top W B$, $W=\operatorname{diag} w$, $C=H^{-1}$.

All weights being positive, a minimum requires every plaquette holonomy to be the identity. The box is simply connected, so parallel transport is path independent there. In tree gauge the unique minimum has all chord holonomies equal to the identity. The same argument for additive real-valued paths gives $\ker B=0$, hence $H>0$.

## The first coefficient

At fixed box the result, including derivatives with respect to any fixed number of local weights, is
$$
 \log Z=c_{\rm box}-\frac{3n}{2}\log\beta-\frac32\log\det H
       +\frac{A(w)}{\beta}+O_{\rm box,w}(\beta^{-2}).
$$
Parametrize each chord by the unit quaternion $\exp(\epsilon X_e)$ with $\epsilon=\beta^{-1/2}$. The quadratic action gives three independent real Gaussian colors with link covariance $C$. On face $p$ let $x_i$ be the signed chord vectors in oriented path order. Tree slots may be deleted. Use
$$
 d_p=\sum_{i<j<k}x_i\cdot(x_j\times x_k),\qquad
 q_p=[\epsilon^4]\operatorname{Re}\prod_i\exp(\epsilon x_i).
$$
The signs follow from quaternion multiplication. The scalar part has cubic coefficient $-d_p$, so the action deficit has cubic coefficient $d_p$. Haar contributes $(\sin(\epsilon |X_e|)/(\epsilon |X_e|))^2$ at each chord, with constants independent of the sources. Integrating the degree-two correction in $\epsilon$ gives
$$
 A(w)=-\operatorname{tr}C+\sum_p w_p\,\mathbb E q_p+
 \tfrac12\,\mathbb E\Big(\sum_p w_pd_p\Big)^2 .
$$
The first term uses $\mathbb E|X_e|^2=3C_{ee}$. The order-$\epsilon$ mean vanishes by odd Gaussian parity. All three terms depend in general on the chosen tree, while their sum is the coefficient of the original compact partition function.

Here is the full quartic polynomial. Write $r_i=|x_i|^2$ and $s_{ij}=x_i\cdot x_j$. Then
$$
 q_p=\sum_i r_i^2/24+\sum_{i<j}\left[
 r_ir_j/4+s_{ij}\left((r_i+r_j)/6+
                 \tfrac12\sum_{k\ne i,j}r_k\right)\right]
 +\sum_{i<j<k<l}(s_{ij}s_{kl}-s_{ik}s_{jl}+s_{il}s_{jk}).
$$
Expand the cosines from scalar quaternion slots and the sines from vector slots. Terms with two vector slots carry one dot product, while four slots give the three signed pairings in the last parenthesis. For signed covariances $C_{ij}$ between the slots, Wick's rule gives $\mathbb E(s_{ij}s_{kl})=9C_{ij}C_{kl}+3C_{ik}C_{jl}+3C_{il}C_{jk}$. The covariance between two scalar triple products is six times the determinant of their $3\times3$ matrix of cross-covariances. In the two alternating color tensors every internal pairing vanishes. The six remaining cross-pairings give precisely that determinant. These formulas include terms from repeated vector slots in the observable's own Taylor series. Differentiating $A(w)$ differentiates both the explicit source weights and $H^{-1}$.

The separated $5\times1^3$ triangle illustrates the cancellations. With a tree that removes the first nonzero coordinate along each path to the origin, the Haar, quartic and cubic-pair contributions to $T^1$ are approximately $-0.0001856981$, $59.8781296468$ and $-59.8772001329$. Removing the last nonzero coordinate instead gives $-0.0000578701$, $-0.0140926238$ and $0.0148943097$. Both sums equal the exact rational $18743362972614416149495387/25198931177334574748217360000$. Dropping any of the three terms gives tree-dependent answers. [Full rational decomposition](evidence/checks.txt)

**Remainder and derivatives.** Work in a small complex polydisc about any positive real weight vector, so all real parts stay positive. The real part of the action away from the identity neighborhood has a uniform positive lower bound by compactness. In a fixed exponential chart it is bounded below by a constant times $\sum_e|X_e|^2$ after rescaling. Split the rescaled integral at $\|X\|=\beta^{1/20}$. The outer part is exponentially small in a power of $\beta$. Inside, Taylor expansion of the action and Haar density through order $\epsilon^3$ after the quadratic term leaves an $\epsilon^4$ remainder bounded by a fixed polynomial in $\|X\|$ times a common integrable Gaussian. For example the cubic perturbation of the exponent is $O(\epsilon\|X\|^3)=o(1)$ on this ball. All odd coefficients integrate to zero. The leading analytic Gaussian factor is locally bounded away from zero after removing $\beta^{-3n/2}$. Taking a local logarithm and applying Cauchy's integral formula on smaller polydiscs gives the same order for source derivatives. Constants can depend on the box, weights and derivative order.

## Abelian controls

Use three independent compact circle link fields with Wilson deficits $u=1-\cos\theta$. Sum the three deficits to define each insertion and its local action source. The quadratic law and the normalization of every scalar insertion agree with $SU(2)$. Write $v_p=B_pCB_p^\top$. The circle chart has constant Haar density and zero cubic face term. The resulting coefficient is
$$
 A_{\rm circle^3}=\tfrac38\sum_p w_pv_p^2.
$$
Replacing each circle deficit, in both action and insertion, by $u+u^2/3$ changes this to $A_{\rm matched}=-\tfrac38\sum_p w_pv_p^2$. Indeed the quartic coefficient of the action per color becomes $-1/24+1/12=1/24$. The improved action is nonnegative with its only circle minimum at $\theta=0$. On an open two-dimensional rectangle tree gauge leaves independent plaquette holonomies after another Haar-preserving triangular change of variables. For one $SU(2)$ face the normalized partition factor is $2e^{-x}I_1(x)/x$ at $x=\beta w_p$, with logarithmic first coefficient $-3/(8w_p)$. Both models therefore match the full first source dependence for an arbitrary family of independent plaquettes. A residual on coupled faces excludes an explanation by this isolated-face coefficient alone. It contains the combined effect of the measure, the action and the chosen plaquette insertion.

Finite-lattice loop perturbation theory has a substantial literature. Heller and Karsch compute Wilson loops to one loop on finite lattices. The particular numbers here use free boundaries, localized source derivatives and an explicitly chosen Abelian calibration. [Heller and Karsch, Nuclear Physics B 251 (1985)](https://doi.org/10.1016/0550-3213(85)90261-5)
