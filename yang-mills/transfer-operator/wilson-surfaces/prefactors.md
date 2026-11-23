# The full four-dimensional prefactor on a faster strong-coupling trajectory

The logarithmic rate alone leaves open whether a normalized correlation tends to one or to a nontrivial constant. The ordinary SU(2) rectangle has an explicit answer on a smaller, sufficient family of trajectories. Keep $nb\to X>0$, $mb\to Y>0$, $kb\to T>0$ as in the [rate theorem](README.md). Suppose also
$$\frac{|\log\beta|}{b^{-2}\log(1/b)}\longrightarrow\infty.$$
For example $\beta=e^{-b^{-3}}$ satisfies this. Put $z=\beta/4$ and $d=\min(2A,Pk)$. In the infinite-volume four-dimensional Wilson state,
$$
\begin{aligned}
 w &=2 z^A(1+o(1)),\\
 J_k &= z^d\big(4\,1_{2A=d}+1_{Pk=d}\big)(1+o(1)).
\end{aligned}
$$
These formulas use the **integer** areas. The relative errors are uniform along each trajectory satisfying the displayed condition. They supply the first nonzero coefficient after simultaneously growing the observables and taking the volume limit.

| Integer area comparison | Mean-normalized correlation $J_k/w^2$ |
|---|---|
| $Pk<2A$ | Asymptotic to $z^{Pk-2A}/4$ |
| $Pk=2A$ | Tends to $5/4$ |
| $Pk>2A$ | Tends to $1$ |

In the middle case the connected reading tends to $1/4$. It occurs, for example, on a square of side $n=2k$. Merely tending to equality in physical units does not fix the comparison of the integer areas. In the positive-time spectral probability of the main note, the vacuum contribution is $w^2/J_k$. It therefore tends to zero below crossover, to $4/5$ at exact equality, and to one above. At equality the complementary contribution is $1/5$; its energy distribution within the permitted scaled band remains unresolved. The strong-coupling gap ensures that the centered part has no vacuum atom.

## Minima and their coefficients

For a single rectangle the unique minimum is the planar disk. For the parallel pair the minimum consists of the two planar disks when $2A<Pk$ and the four lateral walls when $Pk<2A$. At equality precisely both occur. To verify uniqueness, first project to the rectangular prism. Any face collapsed by that projection reduces the face count. A minimal component meets its assigned boundary and, without such a collapsed face, cannot change the unused coordinate or extend beyond the prism. Components with zero boundary can be discarded. The same reasoning applies to the single disk after planar projection.

In the prism, equality in the row and column bound for $0<|S|<A$ is impossible. Every occupied row would have to be filled across all $n$ columns and every occupied column across all $m$ rows, forcing all of $Q$ from any occupied cell. In the slicing proof, the chosen minimum-perimeter slice must therefore be empty or full. If it is empty, the horizontal cost already exhausts $2A$; equality requires every vertical section empty. If it is full, all vertical perimeters are at least $P$; equality requires zero horizontal cost, hence every section is $Q$. Each case uniquely fixes the horizontal and vertical faces.

In a free box expand the original Boltzmann exponential around independent Haar links. A face multiset contributing to a coefficient of the trace observable must have mod-two boundary equal to the contour incidence vector; this follows by changing the sign of a single link. Thus all numerator terms below the minimum face count vanish. A term at the minimum uses each face of a minimum filling exactly once. The factorial in the exponential cancels the number of orders of these faces.

Orient each disk or annulus coherently. The SU(2) traces of a word and its inverse agree, so choose boundary orientations and face orientations to pair each link once with its conjugate. Haar integration gives $\int U_{ab}\overline{U_{cd}}\,dU=\delta_{ac}\delta_{bd}/2$. At each surface vertex the incident face corners, including the boundary trace when present, form one connected cyclic sequence of identified indices, contributing two choices. Thus the coefficient for a surface with $V_s$ vertices, $E_s$ edges and $F_s$ faces is
$$2^{V_s-E_s-F_s}=2^{\chi}4^{-F_s}.$$
Each face supplied one normalized trace in the Wilson exponent; the observed boundary traces have no divisor of two. The disk, disjoint disks and annulus have Euler characteristics one, two and zero. This gives the coefficients $2,4,1$ respectively. Off-surface links integrate to one. [Four-dimensional finite controls](bulk_control.py)

## Uniform remainder and infinite volume

Enclose the loops in a free box padded by $D=10(A+P+k+1)$ lattice cells in every direction. Write $N$ for the number of plaquettes. Then $N=O((A+P+k+1)^4)$ along the trajectories here. The exponent without $\beta$ is a real sum $V$ with $|V|\le N$. For a trace or a product of traces $O$ with $\|O\|_\infty\le4$, the absolute remainder in the unnormalized numerator after its first nonzero coefficient at degree $h$ is at most
$$4e^{\beta N}(\beta N)^{h+1}/(h+1)!.$$
Here $h=A$ or $h=d\le2A$. The coefficient in absolute value is at least $4^{-h}$. Hence the relative error is bounded by $4e^{\beta N}\beta N(4N)^h$. The partition denominator is between $e^{-\beta N}$ and $e^{\beta N}$. Since $h=O(b^{-2})$, $\log N=O(\log(1/b))$ and the displayed coupling condition dominates $h\log(4N)$, both errors vanish.

For completeness the surrounding Gibbs state can change the answer in this box by at most $C P\alpha^{D-2}/(1-\alpha)$ in absolute value, $\alpha=18\tanh\beta$. Compare its boundary-conditioned specification on the box with the free box. Only edges in the boundary collar have different conditionals; their direct total-variation discrepancies are at most one. A chain of face adjacencies from any observed link to that collar has at least $D-2$ steps, and the sum over chains of a fixed length is at most $\alpha$ to that power. There are at most $2P$ observed links with uniformly bounded oscillations. This comparison is uniform in every external configuration. Since $D-2\ge 2h$ and $\alpha\le18\beta$, division by $(\beta/4)^h$ still gives a vanishing error. This establishes the prefactors for the original infinite-volume law. The strong restriction on $\beta$ above controls the crude absolute Taylor remainder. Its optimal relaxation remains open.
