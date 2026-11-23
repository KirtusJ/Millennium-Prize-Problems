# Particles in other representations

Let $G$ be a fixed compact connected Lie group with a chosen smooth Wilson action function $\chi(g)=\operatorname{ReTr}\rho(g)/\dim\rho$ from a finite-dimensional unitary representation. Use the Wilson law of that group on its own link variables. Let $\pi$ be the particle representation on $\mathbb C^d$. Its invariant vectors give a free scalar heat trace with their multiplicity. Restrict to their orthogonal complement, and assume it has positive dimension, still denoted by $d$. All constants and exponents below may depend on $G,\rho,\pi$.

## Several loops at one vertex

Choose $k$ group elements whose fixed subspaces in $\pi$ have intersection zero. Such a finite list exists because the intersection over $G$ is zero and each strict intersection lowers a finite dimension. It uses at most $d$ elements. On $G^k$ put
$$
 M(g)=\sum_{j=1}^k(I-\pi(g_j))^*(I-\pi(g_j)),\qquad f(g)=\det M(g).
$$
This real analytic function is positive at the chosen tuple. It is nonnegative everywhere, and compactness and connectedness imply that for some $C,\alpha>0$ and all $0<u\le1$,
$$
 {\rm Haar}^{\otimes k}\{\lambda_{\min}(M)\le u\}\le C u^\alpha .
$$
Indeed $\|M\|\le4k$, so the event implies $f\le(4k)^{d-1}u$. In analytic coordinate charts about each zero, a finite-order derivative of $f$ is nonzero, by the identity principle on the connected manifold. An appropriate line direction has a nonvanishing derivative of that order, by polarization. Shrink to a rectangular chart where that directional derivative stays bounded away from zero. In each such fiber the one-dimensional sublevel bound is $C\varepsilon^{1/j}$ for derivative order $j$. One proof picks $j+1$ points separated by a constant times the measure of the one-dimensional sublevel set and applies the divided-difference mean value formula. Integrate transversely, bound the smooth Haar density there, and take a finite cover of the compact zero set. Its complement away from these neighborhoods has a positive minimum. [One-dimensional sublevel estimate, Carbery–Christ–Wright](https://doi.org/10.1090/S0894-0347-99-00309-4)

Choose a fixed small cube with at least $k$ edges outside a spanning tree, and take $k$ distinct such edges. Use the corresponding fundamental cycles based at the same root, traversing the tree in both directions as required. After fixing the tree and all other links except the $k$ selected ones, each cycle holonomy is $a g_j^{\pm1} b$ with its own marked edge variable. Independent Haar on the marked variables therefore gives product Haar on the rooted holonomies.

Let $B=1+4\beta_s+2\beta_t$. For one marked spatial link, its conditional log density is a finite sum of left/right translates and inverses of the Wilson character. Its Hessian is bounded by $C B$ in a bi-invariant metric. At a maximum its first derivative is zero, so a ball of radius $c/\sqrt B$ around the maximum contributes at least a constant times $B^{-\dim G/2}$ times the maximal density to the normalizer. The normalized one-link density is bounded by $C B^{\dim G/2}$, uniformly in every other link. Conditioning on the exterior of all marked edges gives a joint law dominated by $(C B^{\dim G/2})^k$ times product Haar. To see this, integrate any nonnegative test over one link with its full conditional law, dominate by Haar, then iterate on the remaining variables, whose conditional bounds follow by conditioning down. The marked edges may interact through the action.

It follows that $\Pr\{\lambda_{\min}(M)<u\mid\text{exterior}\}\le C' B^{k\dim G/2}u^\alpha$. Fix $q=k\dim G/(2\alpha)$ and take $u=c B^{-q}$ with $c>0$ small enough to make the probability at most $1/16$. On the good event, telescoping each cycle gives
$$
 u\,\|f(o)\|^2\le \sum_j\|(I-\pi(U_j))f(o)\|^2\le C_{\rm cell} E_{\rm cell}.
$$
The cycle lengths and repeated edges are bounded since this cell is fixed. Paths from its root to all its sites give total squared norm at most $C_{\rm cell}' u^{-1}E_{\rm cell}$. Tile a large block by disjoint copies of this cell. The conditional bound on distinct bad cells iterates as in the fundamental case. With probability at least $1-2^{-n}$, at least half its sites belong to good cells, where $n$ is the number of small cells. The scalar cube Poincaré estimate then gives the lower potential $[C b^2(m^2+B^q)]^{-1}$ on good large blocks. The free diagonal bound is unchanged up to the color multiplicity $d$.

In particular at fixed physical diffusion time, setting $x=s/b^2$ and taking $m$ a suitable multiple of the small-cell side of order $x^{1/5}$ gives
$$
 \mathbb E F_s/V\ \le\ C s^{-3/2}
      \exp[-c\min(x^{3/5},x/B^q)] .
$$
For polylogarithmic $B$ this beats every power of the spacing. No uniformity over choices of group or representation is required. Quantitative sharpness of $q$ is open. Groups with a finite center can be treated directly in their own global form under the same connectedness hypothesis. An inherited measure on quotient links is covered by applying the result upstairs to a pulled-back particle representation, when the upstairs measure has the hypotheses above. [Block argument](wilson-law.md) · [Program's distinction between a quotient law and a new Wilson law](../../central-quotients/)

## Explicit adjoint control

One rotation in the adjoint representation of SU(2) always fixes a real axis. For two independent Haar rotations $R_1,R_2$ and a fixed unit real vector $v$, the images $R_jv$ are uniform on $S^2$. A cap with chordal radius $2\sqrt u$ has probability $u$ for $0<u\le1$. If $\lambda_{\min}\sum_j(I-R_j)^*(I-R_j)\le u$, a real unit eigenvector has both defects at most $\sqrt u$. A net with spacing $\sqrt u/2$ and at most $C/u$ points contains a vector with both defects at most $2\sqrt u$. The product-Haar event therefore has probability at most $C u$. On the original SU(2) fundamental Wilson law the conditional density comparison costs at most $C B^3$ for these two marked links. This gives the explicit choice $u=cB^{-3}$ for the adjoint. For two half-turns about orthogonal axes the summed defect Gram has smallest eigenvalue four, while one half-turn gives zero. [Numerical controls](execution.md)
