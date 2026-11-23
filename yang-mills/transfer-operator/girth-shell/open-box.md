# A boundary excitation above the bulk transfer coefficient

There is a different comparison at **large** spatial coupling. Take the temporal limit first. On an open, contractible cubic box of $N^3$ cells let $\Gamma_N(b)$ be the covariance of all spatial plaquette traces at $b=\beta_s$. The plaquettes exhaust the girth-four cycles. Let $H_N$ be the oriented cube-by-face incidence and set
$$
 P_N=I-H_N^*(H_NH_N^*)^{-1}H_N,\qquad K_N=6(P_N\circ P_N),
$$
where $\circ$ denotes entrywise multiplication in the real face basis. Then $b^2\Gamma_N(b)\to K_N$ in operator norm at every fixed $N$. The open-box top and the bulk limiting operator obey different bounds:
$$
 \frac{108}{25}\le\|K_N\|\le5\quad(N\ge2),\qquad
 \|K_{\mathrm{bulk}}\|=4.
$$
Thus the leading vacuum-normalized first excitation of the whole box can be closer to the vacuum than the bulk sheet of excitations indicates. The discrepancy persists at arbitrarily large box sizes in this order of limits.

## Static spatial limit

Fix a spanning tree of the one-skeleton. Gauge-transform the tree links to one and integrate their redundant Haar variables. The remaining product-Haar integral has a unique maximum of the Wilson density at identity: flat holonomies on a contractible complex are pure gauge, and every tree-fixed flat link is identity. In exponential coordinates $U_e=\exp(iX_e\cdot\sigma/\sqrt b)$ off the tree, the rescaled Wilson weight approaches $\exp(-\sum_p|(dX)_p|^2/2)$ up to its constant. Here $d$ is the signed plaquette curl on non-tree edges. It is injective because a curl-free one-cochain is a gradient and a gradient vanishing on the tree is zero. This positive Hessian gives an integrable Gaussian bound times any fixed polynomial in a fixed identity neighborhood. The complement is exponentially suppressed by compactness. In particular $b(2-\chi_p)$ converges in joint moments of degree two to $|(dX)_p|^2$ under the Gaussian law. The Taylor estimates needed for dominated convergence follow by bounding the plaquette deficit by a constant times the squared norm of the small link coordinates. Constants here can depend on $N$. [D4's finite-box Laplace expansion](../../spectral-support/scalar-response/finite-expansion.md)

For each of the three independent colors the curvature covariance is the orthogonal projector onto $\operatorname{im}d=\ker H_N$. The last equality is cellular exactness in degree two of the contractible box. The tree gauge removes gradients without changing the image of the curl. Wick contraction gives the factor $2\cdot3=6$ times the entrywise square. This proves the static limit. $K_N$ is positive semidefinite as a Gram matrix of rank-one tensors. In fact it is positive definite: a vanishing combination of squared plaquette curls as a polynomial in edge fields would also vanish before tree fixing by gradient invariance. In that polynomial the cross term from two consecutive perpendicular edges of a specified plaquette occurs in that plaquette alone. Reading its coefficient kills the corresponding weight. This applies to each face, including at the boundary.

## What the first excitation of the box sees

Put $G=(H_NH_N^*)^{-1}$. The inverse matrix is the Green function on dual cube centers with Dirichlet ground outside: the diagonal of $H_NH_N^*$ is six and the off-diagonal entries for adjacent cubes are $-1$. Each missing neighbor is a separate unit link to ground. At a corner cube $c$, the three exterior face columns of $H_N$ are signed copies of $e_c$. If $g=G_{cc}$, the principal block of $K_N$ on these three faces has diagonal $6(1-g)^2$ and off-diagonal $6g^2$. Equal coefficients on just these faces yield the Rayleigh quotient $6[(1-g)^2+2g^2]$.

For $N\ge2$, keep the three direct links from $c$ to ground and the three separate branches from $c$ through its distinct interior neighbors to two ground links each. These are links of the original dual graph, including when $N=2$. For value $x$ at $c$ and values $y_j$ at its three neighbors the retained Dirichlet energy is $3x^2+\sum_j[(x-y_j)^2+2y_j^2]\ge5x^2$. All other energy terms are nonnegative. Consequently $G_{cc}=\sup_f |f(c)|^2/\langle f,H_NH_N^* f\rangle\le1/5$, and the corner quotient is at least $108/25=4.32$. In the reverse direction every face column $h$ has an entry of absolute value one at some cube $c$. Testing the same variational formula with $f=e_c$ gives $h^*Gh\ge1/6$. Thus $(P_N)_{pp}\le5/6$. The row sums of $K_N$ are exactly $6(P_N)_{pp}$ since $P_N^2=P_N=P_N^*$. The symmetric nonnegative matrix has norm at most five. For $N=1$ all six rows have sum five. [Lean inequalities](GirthShell.lean) · [Direct incidence diagonalizations](readback.txt)

## What an observation held in the bulk sees

Center nested boxes at the origin and exhaust $\mathbb Z^3$. Embed face vectors by zero extension. The oriented boundary row of a fixed unit cube is the same finitely supported vector in every larger face space. Extend $P_N$ as identity off its box. Its orthogonal complement projections then increase to the projection onto the closed span of all cube boundaries, hence $P_N\to P$ strongly. On a fixed face column the entrywise squares converge in $\ell^1$ by Cauchy–Schwarz applied to the difference and sum of the columns. Using the uniform row bound (or the bound six for the identity extension) and density, the $K_N$ extended by zero converge strongly to $K_{\mathrm{bulk}}=6(P\circ P)$. Strong convergence does not force convergence of the norms here.

In spatial Fourier variables $P$ projects onto the kernel of the signed divergence row with components $1-e^{ip_j}$ up to phases. It has rank two almost everywhere. Cubic symmetry and Fourier integration yield $P_{pp}=2/3$ on every oriented face. The entrywise squares are absolutely summable in every row and every bulk row sum equals four. The upper norm bound follows by the Schur test. For the lower bound truncate the constant three-orientation vector to a growing cube and normalize. The overlap of each fixed translate tends to one and summability permits passage to the limit in the Rayleigh quotient. This proves $\|K_{\mathrm{bulk}}\|=4$. The three-face corner witness escapes any fixed interior support.

For clarity, at each fixed $N$ the open-box transfer satisfies
$$
 \lim_{b\to\infty}\lim_{\beta_t\downarrow0}
 b^2\frac{\lambda_1}{\lambda_0 u_t^4}=\|K_N\|.
$$
The strong limit above acts on the resulting interior correlation coefficients. Exchanging the spatial-coupling, temporal-coupling and volume limits or inferring a physical mass on the weak-coupling four-dimensional trajectory would require additional estimates. The boundary example is directly relevant to attempts to read a bulk gap from the top excited eigenvalue of an open regulator. [Transfer reduction](transfer.md)
