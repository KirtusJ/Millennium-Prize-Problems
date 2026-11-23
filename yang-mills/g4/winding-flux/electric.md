# The first electric levels in a winding sector

Use the Haar-orthonormal gauge-invariant spin-network decomposition on a fixed finite torus. Edge labels $n_e$ are twice the spin. The one-link convolution eigenvalue is $a_n=I_{n+1}(\beta_t)/I_1(\beta_t)$ with $a_0=1$. The product eigenvalue on a physical spin network is $\prod_e a_{n_e}$. With $\eta=a_1$, $a_n\le\eta^n$ follows by multiplying the decreasing successive Bessel ratios. [Electric transfer calculation](../../observable-normalization/replica-gap/electric.md) · [Baricz and Ponnusamy, inequality (2)](https://arxiv.org/pdf/1010.3346)

The sign on one dual cut acts by $(-1)^{\sum_{\rm cut}n_e}$. Each cut in a charged direction therefore has odd crossing sum, and parallel cuts have the same character by site gauge invariance. On the $3L$ distinct cuts, which partition all spatial links, this forces $\sum_e n_e\ge d=L|h|_1$. At equality, each cut in each charged direction contains exactly one label-one link and all other links have label zero. Every other network in this sector has total degree at least $d+2$, by parity. The staircase Wilson character supplies an eigenvector attaining $\eta^d$ on the pure electric axis. Thus the full sector bottom there is $-d\log\eta$.

## Fixed magnetic coupling and the first cluster

Write $P_h$ for the **minimal-degree** projection on charge $h$, and let $K^{(h)}$ be the electric kinetic operator restricted to the whole sector. Then $\|\eta^{-d}K^{(h)}-P_h\|\le\eta^2$. On the neutral physical sector, every nonconstant network has degree at least four: its nontrivial edges contain a cycle since no invariant vertex can have just one nontrivial incident edge. The spatial girth is four. Thus the neutral electric operator tends in norm to the Haar constant projection with error at most $\eta^4$. The magnetic multiplier $M=e^{-\beta_s S_{\rm sp}/2}$ commutes with the **charge** projection. It may mix the degree levels within that sector.

Let $Z_s=\int M^2\,dH>0$. The neutral vacuum eigenvalue of $MKM$ differs from $Z_s$ by at most $\|M\|^2\eta^4$, since $M|1\rangle\langle1|M$ has sole nonzero eigenvalue $Z_s$. In the limit $\beta_t\downarrow0$ at fixed $L,\beta_s$ the vacuum-normalized restriction satisfies
$$
\left\|\eta^{-d}T|_h-\frac{M P_h M}{Z_s}\right\|=O_{L,\beta_s}(\eta^2).
$$
For any Haar-orthonormal basis $\phi_i$ of the minimal space, the nonzero eigenvalues of $MP_hM/Z_s$ are those of the finite Gram matrix $G_{ij}=\int\overline{\phi_i}\phi_j M^2\,dH/Z_s$. It is positive definite because $M>0$. The min-max principle gives the same absolute error order for each rescaled ordered eigenvalue, including the first one above this cluster when ordered from largest transfer downward. For the upper spectral edge of the sector this gives $E_h=-d\log\eta-\log\lambda_{\max}(G)+O_{L,\beta_s}(\eta^2)$. This reduction permits the box and magnetic coupling to enter the error. The previous section's lower bound has a different, uniform volume scope. [Program's finite-box shortest-cycle reduction](../../transfer-operator/girth-shell/transfer.md)

## Single and double winding

For $h=(1,0,0)$ there are $L^2$ straight oriented winding lines up to orientation reversal. Each admits one invariant, the unnormalized fundamental trace with unit Haar norm. The Gram matrix on them is translation invariant in the two transverse coordinates, so its eigenvalues are the discrete transverse Fourier transform of its two-line correlations in the spatial Wilson measure.

For $h=(1,1,0)$ the minimal degree is $2L$ and the dimension is
$$
L^2\binom{2L}{L}+L^4-L^3 .
$$

To count it, the binary label-one supports have even degree at every vertex. In an edge-disjoint cycle decomposition the total length $2L$ is exhausted by the required $x,y$ windings. A contractible cycle would consume at least one extra edge beyond the minimum required by the others. Hence the support is either a single simple doubly winding cycle or a pair of straight lines in the two directions.

Orient a single such cycle to move positively in $x$. Its $y$ direction is then either entirely positive or entirely negative. For each sign there are $L^3\binom{2L}{L}$ rooted presentations before checking simplicity. A proper return can only occur after a full consecutive run of $L$ steps in one direction. These cyclic words consist of a full $x$ block and a full $y$ block. There are $2L$ choices of their shift. Every simple oriented cycle has $2L$ rooted presentations, including periodically repeating words, because the starting vertex is retained. The count per sign is $L^3\binom{2L}{L}/(2L)-L^3$.

There are $L^4$ pairs of axial lines, of which $L^3$ meet in a vertex. Away from a junction, a degree-two vertex has one two-spin invariant. At the crossing, four spin-$1/2$ representations have two invariants because two fundamentals decompose as spin zero plus spin one. Thus the pair supports contribute $L^4+L^3$ states. Adding the single-cycle terms proves the formula. Its value **1,312** at $L=4$ is the total rank of the limiting cluster. All these states share the first energy at $\beta_s=0$. Magnetic coupling can split that degeneracy. [SU(2) tensor product rule, Theorem 9.1](https://www.math.columbia.edu/~woit/QMbook/qmbook-latest.pdf)

The independent control chooses exactly one edge on every charged cut, matches the binary vertex boundaries of the two directions, and counts invariant multiplicities at the shared vertices. In the full side-four three-torus it finds 1,184 valid supports with no crossing and 64 with one crossing. This gives $1184+2\cdot64=1312$ without generating step words. [Enumeration and controls](control.py)
