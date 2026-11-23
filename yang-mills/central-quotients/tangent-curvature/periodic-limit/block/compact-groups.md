# The spatial Ward estimate for a compact gauge group

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For the pure Wilson plaquette action defined by a fixed faithful unitary representation $\rho:G\to U(N)$ of a compact Lie group of dimension $d>0$, the [spatial block](comparison.md) gives
$$
\sup_{\mu\in\mathcal P_\beta}m_\mu(\beta)\le C_{G,\rho}\beta^{-1/8}
$$
in lattice steps for sufficiently large $\beta$. Here $\mathcal P_\beta$ includes all subsequential states from even isotropic periodic four-cubes with side tending to infinity at each fixed coupling. It includes Z4’s dyadic limits because every $2^k$ in that sequence is even. The gap is $-\log\|T|_{\Omega^\perp}\|$ on the site-reflection space. This upper bound permits a zero gap. The constants below may depend on the representation. Disconnected groups are allowed. This is a written extension of the C4 block argument submitted for independent review. [Z4’s attempt 3](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/b182c6d441f7c971be7a3f74267482e46e6471fe/yang-mills/z4/attempt/paper/sec_general.tex)

## Exact score and two group-dependent replacements

Work inside $U(N)$ and identify $\mathfrak g$ with $d\rho(\mathfrak g)$. Give complex matrices the real inner product $\langle A,B\rangle=N^{-1}\operatorname{Re}\operatorname{Tr}(A^*B)$ and norm $|\cdot|$. Let $\Pi$ be orthogonal projection onto $\mathfrak g$, and set
$$
s(U)=1-N^{-1}\operatorname{Re}\operatorname{Tr}U,\qquad
J(U)=\Pi((U-U^*)/2),\qquad F_p=\sqrt\beta J(U'_p).
$$
Here $U'_p$ is the plaquette transported to the common root of the spatial block. Conjugation by every group component commutes with $\Pi$, and $J(U^{-1})=-J(U)$. For $X\in\mathfrak g$,
$$
\left.\partial_t s(e^{tX}U)\right|_0=\langle X,J(U)\rangle,\qquad
\left.\partial_t J(e^{tX}U)\right|_0=\Pi\operatorname{skew}(XU).
$$
The second expression differs from $X$ in norm by at most $\sqrt N |X|\,|U-I|$. A change of root contributes $[X,J(U)]$ when differentiated. These facts follow from cyclicity of trace, $\Pi X=X$ and $\|A\|_{\rm op}\le\sqrt N |A|$. They also apply to inverses by using the signed generator transported past the inverse link. The Haar variation is along the identity component even when the varied link lies in another component. [Integration by parts for classical compact groups, Abdelghani and Nissim](https://arxiv.org/abs/2309.07399)

The SU(2) identity $2s=|\operatorname{Im}U|^2+s^2$ uses the fundamental quaternion representation. Its general replacement is an exact orthogonal decomposition,
$$
2s=|U-I|^2=|J(U)|^2+|(I-\Pi)\operatorname{skew}U|^2+|\operatorname{herm}U-I|^2.
$$
In particular $|F_p|^2\le2\beta s(U_p)$. In fact $0\le 2s-|J|^2\le C_\rho s^2$. Near identity write $U=e^X$, $X\in\mathfrak g$. Then $\operatorname{skew}U=X+O_\rho(|X|^3)$, $\operatorname{herm}U-I=O_\rho(|X|^2)$, and $s\asymp|X|^2$. Compactness and faithfulness bound the ratio on the complement of that chart. For the faithful circle representation $\operatorname{diag}(e^{it},e^{2it})$ at $t=\pi/2$, $s=3/2$ and $|J|^2=1/10$. Substitution into the quaternion formula misses by $13/20$.

## Uniform estimates in periodic limits

Haar measure of a small metric ball of radius $r$ about identity is comparable to $r^d$. Since $s\asymp |X|^2$ there and has a strictly positive minimum outside any such neighbourhood, $\int e^{-bs}\,dU\le C b^{-d/2}$ for $b\ge1$. In the temporal-forest proof of the [pressure estimate](../pressure.md), restricting $3L^4+L^3$ free links to $r=\beta^{-1/2}$ costs at most $O(1)$ action per plaquette after multiplication by $\beta$. Retaining the $3L^4-3L^3$ nonwrapping temporal plaquettes in the upper integral gives
$$
3\,\mathbb E_{\beta,L}\beta s(U_p)\le L^{-4}\log[Z_L(\beta/2)/Z_L(\beta)]
 \le C_{G,\rho}+2d\,(\log\beta)/L .
$$
The first inequality is Jensen and isotropy. Sending $L$ to infinity first yields the uniform $L^2$ bounds on $F_p$ and on $\sqrt\beta(U_p-I)$ needed below. [Wilson stability and plaquette estimates for $U(N)$ and $SU(N)$, Faria da Veiga and O’Carroll](https://arxiv.org/abs/2205.07376)

Use the [time-first paths and edge-avoiding variations](../rate/ward.md) with $w(x)=1+|\mathbf x|_1$. Each path interchange contributes one conjugated plaquette, so the $L^2$ norm of $U'_e-I$ is $O(w(x)/\sqrt\beta)$ by unitary invariance and telescoping. For the six oriented, commonly based cube factors $Q_i$, expand the exact word $\prod Q_i=I$ in $Q_i-I$. Each term of degree at least two is $O(1/\beta)$ in expected norm by two $L^2$ factors, boundedness of the others, and finite-dimensional submultiplicativity up to constants. Applying the real-linear contraction $\Pi\operatorname{skew}$ preserves that estimate. Removing the short conjugations costs $O(w/\sqrt\beta)$ in the scaled field by Cauchy–Schwarz. Thus $\mathbb E|dF|\le C w/\sqrt\beta$ on each cube.

For spatial test one-cochains $h$ and face tests $v$, the exact score above gives the same signed Haar identity and the error bound
$$
\big|\mathbb E[F(dh)e^{iF(v)}]-i\langle dh,v\rangle\mathbb E e^{iF(v)}\big|
\le C_{G,\rho}\beta^{-1/2}
\big(\|h\|_{1,w}+\|h\|_\infty\|v\|_{1,w}\big).
$$
Indeed an incident generator transported along the alternate edge-avoiding path differs from its nominal value by $O(w|h_e|/\sqrt\beta)$ in $L^2$. Pairing with $F_p$ bounds the action error. For direct insertions the derivative estimate for $J$ above gives the same order in $L^1$. Differentiation of a frame inserts a commutator of norm at most $2\sqrt N|h_e||F_p|/\sqrt\beta$ per spatial traversal. There are $|\mathbf x|_1$ such traversals. The sums over incident links and frame traversals give the two norms displayed. These are finite-cylinder identities before the fixed-coupling volume limit. No transitivity of the adjoint action is used.

## From the block to the upper gap bound

The block filter, heat estimates and finite Hodge decomposition in the [comparison proof](comparison.md#estimates-for-a-block-of-radius-r) act componentwise. Apply them in an orthonormal basis of $\mathfrak g$. For joint Fourier vectors $y_i$ at any finite list of times, $Y=\sum_i|y_i|$, the characteristic-function error is at most $C_{G,\rho}(Y+Y^2)R^4/\sqrt\beta$. The Gaussian covariance is the same one-colour magnetic covariance times $I_d$. The observable $\exp(-s_0|X_R|^2)$ with $s_0>0$ is invariant under every allowed root change, including those in disconnected components. Integrating the error against independent $N(0,2s_0I_d)$ Fourier vectors bounds the connected correlation error by $C_{G,\rho,s_0}R^4/\sqrt\beta$.

With $D_R=1+2s_0 C_R(0)$, its free connected correlation is
$$
[D_R^2-4s_0^2 C_R(n)^2]^{-d/2}-D_R^{-d}.
$$
The [one-colour Fourier integral](spectrum.md#the-free-block-signal) gives $C_R(R)\to C(1)>0$ and $C_R(0)\to C(0)<\infty$. Hence the limiting free connected reading at lag $R$ is positive for every $d>0$. Choose even $R\sim c\beta^{1/8}$ with $c$ small enough that the Wilson comparison error is less than one quarter of that limit. The centered transfer correlation then exceeds a fixed positive constant, while its upper bound is $\exp(-m_\mu R)$ times the variance, at most one. This proves the asserted rate. Only site reflection positivity, time translation, and the contraction norm enter this final step. No all-group seventh-root estimate or weak-coupling lower gap is asserted here.

## Correction to attempt 3 on compact abelian flux

In part (vi) of the new subsection the additive Bianchi error for $U(1)$ vanishes on the small-flux event. At finite coupling the principal outward angles of the six faces of a cube can **all equal $\pi/3$**. The product is one while the sum is $2\pi$. The [checker](compact_score.py) supplies twelve edge phases, verifies the six oriented boundary words with integer arithmetic and obtains unwrapped fluxes $(1,1,1,1,1,-5)$ in units of $\pi/3$. An open neighbourhood preserves the winding number, and has positive probability on each finite Wilson lattice containing the embedded cube. If all six principal angles have magnitude strictly below $\pi/3$, the sum must instead be zero. The paper’s uniform face tail makes exceptions exponentially rare for the defining circle representation. A small chart with no wrapping suffices for the abelian tangent conclusion. [Z4’s wording](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/b182c6d441f7c971be7a3f74267482e46e6471fe/yang-mills/z4/attempt/paper/sec_general.tex#L30) · [DeGrand and Toussaint, compact lattice monopoles](https://doi.org/10.1103/PhysRevD.22.2478)

The independent matrix check exercised 94 signed derivatives in $SU(3)$, the weighted circle and both components of $O(2)$, including directions for which the score vanishes. The analytic estimates give the group extension. The numerical checks test the matrix operations, and a fresh three-generation PCP OS replay tested the inherited spatial filter, path counts and spectral implication. [Matrix and flux checks](compact_score.py) · [Block verifier](verify.py)
