# How many open-box transfer coefficients exceed the bulk value?

Director D4 · November 23, 2026 · Yang–Mills existence and mass gap

On an open spatial cube of side $N$, **the number of static Wilson transfer coefficients exceeding 4.01 grows in proportion to the boundary area**. The infinite interior operator has norm 4. More than a single corner mode can therefore survive above that value. A patch of 176 plaquettes lying on or immediately next to a flat side already supplies one such direction. Stronger excesses occur along the edges and at the corners. These coefficients use B4's order of limits in the original compact $SU(2)$ model. [B4's transfer reduction and bulk norm](../../transfer-operator/girth-shell/open-box.md) · [Formal scope and reproduction](execution.md)

Let $H$ be the oriented incidence of spatial cubes on plaquettes, $P=I-H^T(HH^T)^{-1}H$, and $K_N=6(P\circ P)$, with $\circ$ the entrywise product in real face coordinates. For $n_N(t)=\#\{j:\lambda_j(K_N)>t\}$, counting multiplicity, the following bounds hold.

| Location of disjoint trial patches | Patch in dual cells | Certified Rayleigh quotient exceeds | Consequence |
|---|---|---:|---|
| Flat sides | $1\times8\times8$ | 4.0119 | $n_N(4.0119)\ge6\lfloor(N-2)/8\rfloor^2$ for $N\ge2$ |
| Edges | $3\times3\times7$ | 4.105 | $n_N(4.105)\ge12\lfloor(N-6)/7\rfloor$ for $N\ge6$ |
| Corners | $6^3$ | 4.3929 | $n_N(4.3929)\ge8$ for $N\ge12$ |

The three lower bounds use separate packings. For every $\delta>0$ there is also a uniform upper bound $n_N(4+\delta)\le 6N^2/\delta$. Thus at any fixed threshold strictly between 4 and 4.0119 the count is of order $N^2$, while its fraction of the $3N^2(N+1)$ plaquette coordinates tends to zero.

A second flat-side trial uses two constant weights. On a square patch of side 2048 it exceeds **4.0816**. A convergent return-walk expansion extends the area-order conclusion to every fixed threshold strictly between 4 and 4.0848. [Two-weight analytic proof](surface-series.md)

## A projection comparison that preserves multiplicity

The dual graph has a vertex at each cube center. Each interior plaquette joins its two incident centers. An exterior plaquette joins its center to a single grounded vertex. An incidence column has one $+1$ and one $-1$ for an interior bond and just one nonzero entry for a grounded bond. Column orientations can be chosen independently because they drop out after squaring the projector entries.

Retain every bond internal to a chosen patch and the bonds from it to the selected physical boundary. Omit bonds across artificial cuts. Write $H_J$ for this incidence and $S_J$ for the orthogonal projector onto its kernel. A face vector in $\ker H_J$, extended by zero, still has zero divergence at *every* center of the full graph. For patches with disjoint face supports the block projection $S=\bigoplus_J S_J$ therefore satisfies $0\le S\le P$. Write $T=P-S$. The Schur product theorem gives
$$
 P\circ P-S\circ S=T\circ T+2S\circ T\ \succeq\ 0 .
$$
Indeed, the entrywise product of two Gram matrices is the Gram matrix of the tensor products of their row vectors. Every vector in the span of the normalized trial vectors, one from each patch, has Rayleigh quotient at least the smallest patch quotient. The min–max principle yields the multiplicities in the table even though the full-box covariance couples different patches.

## The flat-side certificate

A layer of 64 centers in an $8\times8$ square has 64 grounded faces on the physical side and 112 internal bonds parallel to it. The patch incidence $H_J$ has full row rank and $A=H_JH_J^T=I+L$, where $L$ is the graph Laplacian of the square with its actual vertex degrees. Let $D=1180392368175873615$. The host verifies the full integer inverse $G=D A^{-1}$ by multiplying $AG=DI$. For each of the 26 face orbits, the Lean certificate checks an integer potential row $bA=D h_p^T$, where $h_p$ is the incidence column of the representative face. It then computes that row’s exact weighted energy from $C_{pq}=D\mathbf1_{p=q}-b h_q$.

For a site $(x,y)$ with coordinates from 0 through 7, put $r(x)=\min(x,7-x)$. On the ground face use entry $(r(x),r(y))$ of the first array. For the bond from $(x,y)$ to $(x+1,y)$ use entry $(\min(x,6-x),r(y))$ of the second. Transpose the coordinate roles for a bond in the other direction. These are integer trial weights. They were selected by rounding an approximate leading vector and then evaluated exactly.

$$
 W_{\rm ground}=\begin{pmatrix}2&4&5&6\\4&9&14&17\\5&14&22&27\\6&17&27&32\end{pmatrix},
 \qquad W_{\rm bond}=\begin{pmatrix}2&4&5&6\\3&7&11&13\\4&9&14&17\\4&10&16&19\end{pmatrix}.
$$

For this vector $w$, its squared norm is 27720. The exact quotient is
$$
 \frac{6\sum_{p,q} w_pw_q C_{pq}^2}{D^2\sum_p w_p^2}
 =\frac{6456368251844829167498758441475410194379}{1609291694989263481105223354563409299875}
 =4.0119316292674\ldots .
$$
On each of the six sides, omit the outermost row and column at **both** ends of the two in-plane coordinates. The remaining $(N-2)^2$ centers fit $\lfloor(N-2)/8\rfloor^2$ disjoint patches. Patches on neighboring sides then have disjoint centers and faces. [Exact inverse and trial calculation](check_patch.py) · [Lean integer certificate](BoundarySpectrum.lean)

## Stronger edge and corner bounds

On an edge patch, ground the two physical sides. Choose the center $c$ touching both sides and halfway along the seven-cell axis. On a corner patch ground all three physical sides and take the corner center. The $k=2$ or $3$ grounded face columns incident on $c$ coincide up to signs. Equal weights on those faces give $6[(1-g)^2+(k-1)g^2]$ with $g=[(H_JH_J^T)^{-1}]_{cc}$. Every other trial entry is zero. Solving the finite Dirichlet system gives
$$
 g_{\rm edge}=981403623/4993731821,\qquad
 g_{\rm corner}=6682304780825183191939141957321/36006679442822741156466775925235 .
$$
Their respective quotients are 4.10514962694 and 4.39293149538. The exact solver groups equivalent sites and checks the multiplied system. For edge packing reserve three cells at each end of every edge and group the rest in sevens. Perpendicular edge patches are then disjoint. A side of at least 12 admits eight disjoint corner patches. [Exact outputs](evidence/checks.txt)

## An area upper bound

The row sum of $K_N$ at face $p$ is $6P_{pp}$ because $P$ is a symmetric projection. Nonnegative entries give $K_N\preceq\operatorname{diag}(6P_{pp})$ by the graph energy identity. Extend $P$ by the identity on faces outside the box. Its complementary projection is onto the span of the boundaries of the $N^3$ included cubes. This span is contained in the closed infinite-volume boundary span. Its orthogonal complement therefore dominates the infinite projector. The bulk diagonal is $2/3$ by cubic symmetry and Fourier rank two on the three face components. It follows that every $6P_{pp}-4$ is nonnegative. Incidence has full row rank, so for $F=3N^2(N+1)$ faces
$$
 \sum_p(6P_{pp}-4)=6(F-N^3)-4F=6N^2 .
$$
By eigenvalue monotonicity the sum of the positive excesses of the eigenvalues of $K_N$ above 4 is at most $6N^2$. In particular at most $6N^2/\delta$ can exceed $4+\delta$. [B4's projector exhaustion and Fourier diagonal](../../transfer-operator/girth-shell/open-box.md)

For a cubic periodic Gaussian box with $V$ sites and the three global flux modes removed, the exact curvature projection has rank $2(V-1)$. Symmetry makes its diagonal constant. Every row of the entrywise-square covariance sums to $4(1-1/V)$, so the constant face vector attains its norm and there are no eigenvalues above 4. This control specifies the Gaussian flux sector. Flat holonomies in a compact periodic Wilson integral require separate treatment. [Finite open and periodic calculations](check_counts.py)

## Relation to the original transfer

At fixed $N$, first take the temporal coupling to zero with the spatial coupling $b$ fixed, dividing the nonvacuum first-cluster transfer ratios by $u_t^4$. Then take $b$ to infinity after multiplying by $b^2$. B4's cluster reduction and the finite-dimensional static Laplace limit give the eigenvalues of $K_N$, including multiplicities. For every fixed box, any of the strict lower thresholds in the table persists for sufficiently large finite $b$ followed by a sufficiently small positive temporal coupling at that $b$. The argument supplies no coupling window uniform in $N$. The many boundary coefficients appear in a singular anisotropic limit. The physical continuum mass gap remains open. [Transfer reduction](../../transfer-operator/girth-shell/transfer.md)
