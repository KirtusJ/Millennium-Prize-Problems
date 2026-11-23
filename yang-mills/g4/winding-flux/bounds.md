# Winding costs and their volume dependence

Write $d=L|h|_1$ for a nonzero charge and $q=5(1-e^{-2\beta_t})$. Suppose first that $q<1$. An occupied Eulerian subgraph representing $h$ decomposes into edge-disjoint simple cycles. Delete zero winding classes and subcollections whose binary sum is zero until the remaining classes are linearly independent. There are between one and three. They still sum to $h$. In each charged coordinate the sum of the integer winding displacements of these cycles, in any orientations, is odd in units of $L$. The aggregate number of steps in that coordinate is at least $L$. Thus their total length $n$ is at least $d$.

A nonzero-winding simple cycle can be rooted on a representative seam edge perpendicular to a direction in which its winding is odd. Orient it to traverse that edge positively. There are at most $3L^2$ such choices, followed by at most five choices per step. For any specified charged direction $i$, at least one cycle has odd winding in $i$, and one may use only its $L^2$ seam starts. Union bounding this cycle already gives
$$
\|T|_h\|\le \frac{L^2 q^L}{5(1-q)} .
$$
A second count retains all the charged directions. For each ordered length list of $k\le3$ edge-disjoint cycles, the count is bounded by $(3L^2/5)^k5^n$. The occupation probability of a given disjoint list is $p^n$. Using the larger count of all candidate lists only after bounding the count of the disjoint ones preserves this exponent. There are at most $(n+1)^2$ compositions for each $k$. Thus the sum over lists is bounded by $3L^6\sum_{n\ge d}(n+1)^2q^n$, and
$$
\|T|_h\|\le 3L^6(d+1)^2 q^d\,\frac{1+q}{(1-q)^3}.
$$
Here $(d+j+1)^2\le(d+1)^2(j+1)^2$. Taking negative logs and dividing by $d$ proves the stated uniform large-volume lower slope. For $q\le1/2$ the log of the prefactor divided by $d$ is bounded by an absolute constant on all $L\ge4$. As $\beta_t\downarrow0$ this yields $E_h/d\ge\log(1/\beta_t)-O(1)$. For $\beta_t\le1/40$ one has $q\le1/4$, so the single-seam count gives the numerical table and $\|T|_h\|\le(4/15)2^{-L}$ because $L^2\le2^L$ for integers $L\ge4$. [Rational checks](control.py)

For the isotropic strong-coupling calculation on $L\ge8$, this gives a direct charge check on the first band. If $q\le1/2$ then $L^2q^L$ is decreasing for $L\ge8$, so every charged transfer norm is at most $64q^8/[5(1-q)]=O(\beta_t^8)$. A4's first band is of order $\beta_t^4$. It is entirely neutral for sufficiently small coupling, uniformly in those boxes. At side four an axial winding loop costs just four temporal faces, the same electric order as an elementary plaquette. [A4's uniform isolation theorem](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/9dbe75c6a9c1eb18c74f4b695d3640fd855c899b/yang-mills/observable-normalization/uniform-band/README.md)

## The subcritical independent-bond range

Fix $p<p_c(\mathbb Z^3)$ for nearest-neighbor bond percolation. An odd winding in direction $i$ supplies a simple cycle through a seam start. Its lift reaches sup-norm distance $r=L/2-1$ from that vertex before completing a net displacement of at least $L$ in coordinate $i$. Up to the first hit of that boundary the path is inside an embedded cube. For even $L\ge4$ the cube and its internal edges have exactly their infinite-lattice law. By the subcritical exponential decay theorem and a union bound over seam starts,
$$
\|T|_h\|\le L^2\,\mathbb P_p^{\mathbb Z^3}(0\leftrightarrow\partial[-r,r]^3)
\le C(p)L^2 e^{-c(p)r}.
$$
Thus $E_h/L$ has a positive lower bound for all sufficiently large $L$, independently of $\beta_s$ and $h\ne0$. For the finitely many remaining sides use the positive empty-graph probability. This proves the uniform linear lower bound at each fixed subcritical $p$. [Duminil-Copin and Tassion, Theorem 1.1](https://arxiv.org/pdf/1502.03051)

One can also let $q$ approach one from below in the explicit count. For example, $1-q_L\ge3\log L/L$ for all sufficiently large $L$ gives $\|T|_h\|\le1/(15\log L)$ by the single-seam bound. No estimate on the percolation correlation length is needed for this particular schedule.

## Every finite temporal coupling

For SU(2) an additional deterministic estimate at finite $L$ is $\|T|_h\|\le\tanh(\beta_t L^2)^d$. In the kernel projection average independently over the signs of **all** $3L$ parallel cuts. In each direction the character of the product of these flips is the product of their individual characters. Moving a cut only changes a site gauge transformation, so after the Haar integration this average equals the original three-cut projection. Each edge belongs to one cut. At fixed endpoint fields and temporal group variables, let $S_P$ be the sum of the $L^2$ plaquette scalar parts on cut $P$. Averaging its sign produces $\cosh(\beta_t S_P)$ for a neutral cut and $\sinh(\beta_t S_P)$ for a charged one. Divide the absolute projected integrand by the all-neutral integrand. Each of the $d$ charged cuts contributes at most $\tanh(\beta_t L^2)$, since $|S_P|\le L^2$. Integrate against the positive neutral weight and apply the same operator comparison. As $L$ increases at fixed coupling this particular lower energy bound can approach zero.

## Finite central subgroups

For a compact group with a finite central subgroup $Z$, the single-seam argument only needs a nontrivial character of $Z^3$ in a chosen direction, a positive transfer with center-invariant magnetic endpoint weights, and a temporal bond weight in $[e^{-b},e^b]$ with the usual central gauge covariance. Expand that weight divided by $e^{-b}$ as one plus a nonnegative factor. Occupations are dominated by $p=1-e^{-2b}$. If every occupied cycle has zero integer winding in the chosen direction, a twist in that direction is a site coboundary on each occupied component. Choose a twist whose character differs from one. Translating by it cancels that graph term, also for complex characters. Here the neutral comparison kernel is the average over all twists in $Z^3$ at the same two endpoints. Conditional on any twist and the integrated site variables, the independent occupation probabilities are bounded by $p$. The triangle inequality bounds the surviving terms by the sum of their positive weights, divided by the sum of all weights in that same mixture. The single-seam and subcritical bounds therefore hold for each such nonzero sector. The binary multidirection count, trial state and multiplicities in this release use SU(2). Groups with trivial center have no sectors of this type.
