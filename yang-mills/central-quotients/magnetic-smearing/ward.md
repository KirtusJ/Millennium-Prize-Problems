# A quantitative Ward estimate for rooted faces on a growing box

Use the original four-dimensional isotropic $SU(2)$ Wilson vacuum, normalized trace $x_p$ and $F_p=\sqrt\beta\,\operatorname{Im} U_p$ in a common root frame. At each fixed spatial side $L$ and $\beta$ the time period tends to infinity first. For sufficiently large $\beta$ the prior reflection bound gives $\sup_p\mathbb E\exp[\beta(1-x_p)/8]\le C$ uniformly in $L$. It implies, for each fixed $q<\infty$,
$$
 \sup_p\|F_p\|_{L^q}\le C_q,\qquad
 \sup_p\|d(1,U_p)\|_{L^q}\le C_q/\sqrt\beta .
$$
The latter follows from $d(1,U)^2\le\pi^2(1-\operatorname{Re}U)/2$. These estimates refer to faces in any orientation, including temporal ones. [Original Wilson moment bound](../tangent-curvature/moments.md)

Use a coordinate cube of radius $R\ge1$ in the lifted lattice with a fixed number of extra layers. It embeds when $L>10(R+2)$; constants below permit increasing this factor. Root at zero. Use ordered coordinate paths, moving in time first, then through the three spatial axes. Let $P_x$ denote the product on the path to $x$. For $e=(x,y)$ the gauged edge $U'_e=P_x U_e P_y^{-1}$ satisfies
$$
 \|d(1,U'_e)\|_{L^q}\le C_q R/\sqrt\beta .
$$
In the closed walk defining this edge one commutes the single step in its own axis past the later-coordinate steps of the path and cancels backtracks. This uses at most $4R+4$ elementary squares. The bound follows by the bi-invariant triangle inequality, Minkowski and the face estimate, irrespective of correlations. Ordered paths in this patch form a tree.

For a finite real three-color two-cochain $g$ write $F(g)=\sum_p g_p\cdot F_p$, where now every $F_p$ is rooted. The $\ell^1,\ell^\infty$ norms below use Euclidean color lengths. Let $F(de)$ denote the signed sum at an edge with any one fixed unit color. For real $|t|\le1$ and $f=\exp(itF(g))$ we claim
$$
 \left|\mathbb E[F(de)f]-it\langle g,de\rangle\mathbb E f\right|
 \le C\{R(1+\|g\|_\infty)+\|g\|_1\}/\sqrt\beta . \tag{1}
$$
The variation here acts on the same rooted observable on both sides; this avoids a loss proportional to the number of perturbed paths times the box radius.

To see this, choose an endpoint of $e$ whose tree path omits $e$. There is always one since the two paths are simple paths in a tree. If the tail $x$ is available, multiply the original link on the left by $P_x^{-1}\exp(sX/\sqrt\beta)P_x$. Otherwise use right multiplication by $P_y^{-1}\exp(sX/\sqrt\beta)P_y$ at the head. The generator is independent of the selected link given its exterior, and left and right Haar invariance give the exact integration-by-parts identity. Either choice inserts $X$ with positive first-order sign for the positive edge. The fixed-frame derivative of the action score, after the scale factor from the Boltzmann weight, is the sum of six projections of the scaled imaginary plaquettes onto $X$ with incidence signs. In each projection there is a conjugation by at most four gauged links. Replacing the projection by the corresponding component of the rooted face costs at most $C R/\sqrt\beta$ in $L^1$ by Hölder, the fourth-moment bounds and the Lipschitz bound for quaternion conjugation. The spatial and temporal plaquettes of the original action both enter.

In differentiating $F(g)$ split the derivative for each face into variation of its oriented plaquette word with its base path held fixed, and variation of that base path. In a face containing $e$ the first derivative differs from its signed incidence times $X$ by $O_{L^1}(R/\sqrt\beta)$, since the remaining gauged links differ from one by this amount. An inverse occurrence inserts the negative generator. A face away from $e$ has zero direct derivative. In the frame derivative the two occurrences of the base transport combine into a commutator. A simple tree path uses $e$ at most once, and its logarithmic derivative has norm at most $|X|/\sqrt\beta$. Thus the derivative of the conjugation of the scaled imaginary face is bounded pointwise by $2|F_p|/\sqrt\beta$ for **every** face. Summing the at-most-six direct contributions with weights bounded by $\|g\|_\infty$ and the frame contributions against $\|g\|_1$ proves (1). At fixed regulator one can first differentiate the finite periodic original Haar integral, then take the time-period limit on its bounded cylinder observables. The estimate uses the moments of the resulting vacuum.

There is also a quantitative Bianchi estimate in the same coordinate frame,
$$
                        \sup_{\rm cubes}\|(dF)_c\|_{L^1}\le C R/\sqrt\beta . \tag{2}
$$
For a particular cube, work first in its own tree gauge rooted at one of its vertices, in the color frame inherited there. There are only finitely many edges. Each non-tree chord loop fills with a bounded number of the cube's faces, so all its local links differ from one by $O_{L^2}(1/\sqrt\beta)$. For a product of four unit quaternions the error after its linear term is at most the sum of the six products of distances of factors from one; this follows by telescoping and unit norms. Imaginary parts of inverse links have opposite signs. Consequently $F^{\rm loc}=d(\sqrt\beta\,\operatorname{Im}U^{\rm loc})+O_{L^1}(1/\sqrt\beta)$ on the cube and $d^2=0$ cancels the leading terms. Returning each based face to the original common frame conjugates it by a product of at most a fixed number of the original **gauged** cube links. The resulting difference is $O_{L^1}(R/\sqrt\beta)$ by Hölder. This establishes (2) without requiring smallness of an entire growing surface.

For compact one- and three-cochains $h,k$, and $g=dh+d^*k+w$ with all terms supported in the patch, (1), (2), and $\mathbb E|F(w)|\le C\|w\|_1$ give
$$
 \left|\mathbb E[F(g)f]-it\langle g,dh\rangle\mathbb E f\right|
 \le C\left[\|w\|_1+
 \frac{\|h\|_1\{R(1+\|g\|_\infty)+\|g\|_1\}+\|k\|_1 R}{\sqrt\beta}\right].
$$
Let $P$ be the $\ell^2$ projection onto exact two-forms on $\mathbb Z^4$ (closure of finite gradients), $v=\|Pg\|_2^2$. Since $dh$ is exact and $d^*k$ is orthogonal to that subspace, $|v-\langle g,dh\rangle|\le\sqrt v\,\|w\|_2$. The characteristic function then satisfies $\phi'(t)=-tv\phi(t)+e(t)$ with $|e(t)|$ bounded by the last display plus $\sqrt v\|w\|_2$. Its solution at one differs from $e^{-v/2}$ by at most this error: each integrating-factor weight $e^{-v(1-t^2)/2}$ on $0\le t\le1$ is at most one. [Compactly supported decomposition and choice of scales](smoothing.md)
