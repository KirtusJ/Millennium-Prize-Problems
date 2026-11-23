# A two-link identity that resolves all six plaquette orientations

The one-link incidence estimate vanishes for two independent combinations of the six plaquette orientations. On the original four-dimensional isotropic SU(2) Wilson measure, a pair of parallel links on each face gives a weaker universal constant and a lower bound for **every** plaquette weight, including those two combinations.

Let $S=\beta\sum_q x_q$ in the Wilson weight $e^S$ and $m_p=\mathbb E x_p$. For a positively oriented face $p=(x;i,j)$, $i<j$, let $e=(x,i)$ and $e'=(x+\hat j,i)$ be its opposite parallel links. Write $W=U_j(x)$ for the link between their starting sites. For any unit imaginary quaternion $a$, let $X$ act on $U_e$ by left multiplication by $\exp(ta)$. Let $Y$ act on $U_{e'}$ by left multiplication by $\exp(t W^{-1}aW)$. For fixed exterior these are commuting, divergence-free Haar derivatives. Both annihilate the coefficient $W$.

The trace $x_p=\operatorname{Re}(U_e U_j(x+\hat i) U_{e'}^{-1}W^{-1})$ is invariant under the simultaneous variation $X+Y$. Also $X^2x_p=-x_p$. Hence $XYx_p=x_p$. For every other elementary face $q$, $XYx_q=0$ because one selected link is absent. Periods of at least three ensure that $p$ is the unique elementary face containing both parallel links. Define the real observable
$$
 D_p=\frac13\sum_{a\in\{\mathbf i,\mathbf j,\mathbf k\}}(XS)(YS)+\beta x_p .
$$
This contraction is gauge invariant. A gauge transformation rotates the orthonormal basis at the first starting site and the parallel transport rotates the second basis consistently. Two integrations by parts for each $a$ give, for every smooth link function $F$,
$$
 \mathbb E[D_p F]=\frac13\sum_a \mathbb E[XYF],\qquad
 \mathbb E D_p=0,\qquad \mathbb E[D_p x_q]=m_p\,\mathbf1_{p=q}.
$$
The same first equality holds after conditioning on all links except $e,e'$. In particular $D_p$ is orthogonal to every square-integrable observable independent of the pair as a whole (and to any smooth observable missing either member). This calculation uses the full Wilson weight. Removing the $+\beta x_p$ term spoils centering.

## Uniform bound on the dual observables

Unit-speed differentiation twice in one link flips the sign of every incident normalized trace, so $|X^2 S|,|Y^2 S|\le6\beta$. The identity $\mathbb E[X((XS)^k)]=-\mathbb E[(XS)^{k+1}]$ gives $\mathbb E(XS)^2\le6\beta$ and $\mathbb E(XS)^4\le3(6\beta)^2$ using $k=1,3$. The same bounds hold for $Y$. Thus Cauchy–Schwarz gives $\|D_p\|_2\le(1+6\sqrt3)\beta$.

For fixed $p$, a nonzero $\mathbb E[D_pD_q]$ requires that $D_q$ depend on the first link of $p$. Otherwise $XYD_q=0$. The support of $D_q$ lies in the union of the two links' six incident faces each, at most 48 link positions in all, including the parallel transport. There are six choices of oriented face type. For each type and support offset, at most one translated anchor places it at a prescribed link. So each Gram row has at most 288 possible nonzero entries, including the diagonal. This coarse bound works on odd or even tori. By symmetry and $2|c_pc_q|\le c_p^2+c_q^2$,
$$
 \mathbb E\left|\sum_p c_pD_p\right|^2
 \le K\beta^2\sum_p c_p^2,\qquad K=288(1+6\sqrt3)^2 .
$$

For $F=\sum_p w_p x_p$ write $Q=\sum_p w_p^2m_p^2$, $D=\sum_p w_pm_pD_p$. The exact pairing gives $\operatorname{Cov}(F,D)=Q$. For $\beta>0$ the explicit gauge-invariant replacement $F'=F-D/(K\beta^2)$ satisfies
$$
 \operatorname{Var}(F)-\operatorname{Var}(F')\ \ge \frac{Q}{K\beta^2}.
$$
Adding a deterministic constant or reversing the sign of both observables gives the corresponding subtraction for $1-x_p$. All mixed covariances of an original face with a distinct correction vanish exactly. Covariances between two corrected spatial tests at periodic time distance at least two steps equal their original covariance, since one of each pair of score observables is independent of the other pair's differentiated links. More generally their covariance difference has finite support in lattice units. Thus the bound identifies a removable short-distance contribution.

For general fixed smooth spacetime profiles and $S_b=\beta\sum_p f_{ij}(x_p^{\rm center})(1-x_p)$,
$$
 \liminf_{b\downarrow0}b^4\operatorname{Var}(S_b)
 \ \ge\ \frac{1}{K}\int\sum_{i<j}f_{ij}(x)^2\,d^4x
$$
along every $\beta\to\infty$ with the box/test conventions of the [main result](README.md). In fact the same bound holds for the variance loss in this explicit replacement. This follows by Riemann summation and the uniform $m_p\to1$. Both the larger one-link bound when its incidence sum is nonzero and this full-rank bound are available; taking the larger is valid. This construction neither assigns a definite contact counterterm to a continuum theory nor constrains the mass of its separated excitations.
