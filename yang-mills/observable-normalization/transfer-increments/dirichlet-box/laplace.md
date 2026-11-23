# Total variation for the conditional link variables on growing boxes

Let $K_\beta(\cdot\mid\psi)$ be Z4’s conditional law in the forest gauge, in the coordinates $\varphi=\sqrt\beta\log U$ on free links, identifying each copy of the Lie algebra with $\mathbb R^3$. Rescale the principal exponential chart only; chart boundaries have conditional Haar probability zero. Let $\Gamma_\psi$ on the same Euclidean space have density proportional to $\exp(-\|d\varphi+d\psi\|^2/2)$. Positivity of the [Dirichlet form](spectrum.md) makes this Gaussian well defined for all boundary data. Write $d=3\nu_R=O(L^4)$ for the number of real interior coordinates and $M=\|\psi\|$. All constants below are independent of $\beta\ge1,L$ and $\psi$.

After dropping constant Jacobian factors the two unnormalized densities are
$$
 f_\beta=\exp(-\beta S_R)\prod_{e\ {\rm free}}
    \left(\frac{\sin(|\varphi_e|/\sqrt\beta)}{|\varphi_e|/\sqrt\beta}\right)^2
            \mathbf1_{\{|\varphi_e|<\pi\sqrt\beta\}},\qquad
 f_\infty=\exp(-\|d\varphi+d\psi\|^2/2).
$$
Both normalizers are at least $\exp[-C(d+M^2)]$: integrate over the cube of coordinate half-width $1/4$. The Haar density per link there is bounded below, while $\beta(1-\cos\alpha_p)$ and the linearized face action are each bounded above by half the square of the sum of the four scaled link norms. Each link is used at most six times. The [rectangle estimate](coercivity.md) bounds both densities above by $\exp(CM^2-c\|\varphi\|^2/L^3)$. Integration outside $\|\varphi\|\le R$, reserving half that quadratic term for the tail, gives for either normalized law
$$
 \Pr(\|\varphi\|>R)\le
 \exp[C(d\log(2L)+M^2)-c'R^2/L^3].
 \tag{1}
$$

On the ball of radius $R$, suppose $(R+M)/\sqrt\beta$ is sufficiently small. Expanding each ordered four-factor exponential product in the plane algebra gives a scaled face logarithm equal to its linear curl plus an error bounded by $C s_p^2/\sqrt\beta$, with $s_p$ the sum of the four scaled link norms. Indeed the degree-two and higher terms are bounded by $C s_p^2/\beta$ before rescaling, and the local logarithm has bounded second derivative. The quadratic approximation to $1-\cos\alpha_p$ adds at most $C s_p^4/\beta$ after rescaling. Thus the difference of the two log densities obeys
$$
 \sup_{\|\varphi\|\le R}|\log f_\beta-\log f_\infty|
 \le C\left(\frac{(R+M)^3}{\sqrt\beta}+
            \frac{(R+M)^4}{\beta}+\frac{R^2}{\beta}\right).
 \tag{2}
$$
The last term bounds the logarithm of the product Haar Jacobian. There is no additional factor counting faces: $\sum_p s_p^2\le24(R^2+M^2)$ and $\|s\|_k\le\|s\|_2$ for $k\ge2$. If the two tail probabilities are at most $\delta$ and (2) is at most $\epsilon$, their normalized restrictions to the ball have density ratio between $e^{-2\epsilon}$ and $e^{2\epsilon}$. Their full total variation distance, in the supremum-over-events convention, is at most $2\delta+e^{2\epsilon}-1$.

For the **identity shell** take $M=0$ and $R=A L^{7/2}\log(2+\beta)$ for a sufficiently large absolute $A$. For $L=O(\beta^\eta)$ with $0\le\eta<1/21$, (1) tends to zero and (2) tends to zero: the cubic error is $O(L^{21/2}\log^3(2+\beta)/\sqrt\beta)$. The same proof handles fixed scaled boundary norm.

For an **actual Wilson shell** choose a breadth-first spanning tree of the shell graph rooted at a bottom corner. Shell distances from that root are at most $5L$: reach the bottom face along a spatial boundary column, using a top-face path to the side first when the starting point is in the top face interior. A gauge-fixed shell edge is a loop word with at most $10L+1$ traversals. It has a filling of at most $C L^2$ plaquettes in the whole four-box. To see this, join each path vertex to the root by the same coordinate order. Comparing those two ordered paths across one edge uses at most $3L$ swaps of unit steps. Telescoping along the loop gives the stated filling, allowing conjugations and multiplicities. Unconditional moment estimates may use a filling through the interior even though the shell gauge itself is exterior-measurable.

B4 independently gives an explicit shell tree and an $O(L^2)$ reconstruction by shell plaquettes alone. That sharper geometric construction can replace the full-box filling in this moment estimate for B4’s tree. [Shell-only reconstruction](../../../transfer-operator/periodic-time/curvature-tail/shell-frame/README.md)

Z4’s dyadic-state one-face tail gives $\|\sqrt\beta\,\alpha_p\|_{L^2(\mu)}\le C$ uniformly. Bi-invariance and Minkowski now give $\|\psi_e\|_{L^2(\mu)}\le CL^2$ for each shell link. There are $O(L^3)$ of them, so $\mathbb E_\mu M^2\le C L^7$. With probability at least $1-C/\log^2(2+\beta)$ one has $M\le L^{7/2}\log(2+\beta)$. On that event take $R=A L^5\log(2+\beta)$, with $A$ large enough in (1). If $L=O(\beta^\eta)$ and $0\le\eta<1/30$, (1) vanishes and the cubic error in (2) is $O(L^{15}\log^3(2+\beta)/\sqrt\beta)=o(1)$. The distance is at most one on the exceptional event. Therefore
$$
 \sup_{\mu\in\mathcal L_\beta}
 \mathbb E_\mu\, d_{\rm TV}\big(K_\beta(\cdot\mid\psi),\Gamma_\psi\big)\longrightarrow0.
$$

The comparison takes place in the same finite-dimensional chart at each coupling and takes the same realized boundary data in both laws. It does not compare the boundary marginal to a Gaussian. For nonlinear plaquette observables, total variation controls a common measurable function of the two chart vectors; replacing a nonlinear curvature map by its linear curl requires a separate observable estimate.

Using cubic moments under both conditional sampling rules gives the stronger averaged range $L=o(\beta^{1/20})$. [Proof using Wilson face moments](mean-shell.md)
