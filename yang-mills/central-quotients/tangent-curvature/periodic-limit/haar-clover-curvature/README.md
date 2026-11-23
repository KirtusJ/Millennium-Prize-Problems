# The first strong-coupling correction to the raw odd-clover susceptibility

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)  
Research program directed by Kirtus Justus

For the raw SU(2) pseudoscalar $q_x$ defined by A4, the first departure from the product-Haar covariance is a **negative contact term**. There are constants $b,C>0$ such that for $0\le\beta<b$, every isotropic even-periodic thermodynamic limit and every finitely supported real smearing $f$ satisfy
$$
 \left|\operatorname{Var}\!\left(\sum_x f_x q_x\right)
     -\left(\frac9{256}-\frac3{1024}\beta^2\right)\sum_x f_x^2\right|
       \le C\beta^4\sum_x f_x^2 .
$$
In particular $\chi_{\rm bare}=9/256-3\beta^2/1024+O(\beta^4)$. Through quadratic order the coefficient is the same at every lattice momentum. The result concerns small inverse coupling and the specified bare polynomial. The physical topological susceptibility and the large-$\beta$ continuum limit require other estimates. [A4’s observable and Haar dual](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/6cd8f578f716cd0f5133f9e55d6b554070eaae81/yang-mills/observable-normalization/transfer-increments/local-action/odd-clover/haar-dual/README.md) · [A4’s bulk-limit proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/bdaf179da8833f18fbd7f2ad8b1796833cf53ae3/yang-mills/observable-normalization/transfer-increments/local-action/odd-clover/tiling.md)

## Why the linear and cubic terms vanish

Work first on an even periodic four-cube of sufficiently large side, with positive links $U_i(x)$ and weight proportional to $\exp(\beta\sum_p t_p)$, $t_p=\tfrac12\operatorname{Tr} U_p=\operatorname{Re}U_p$. Write $q_x$ as the sum of its 48 signed terms $h_\alpha$, each equal to $\pm\operatorname{Im}U_A\cdot\operatorname{Im}U_B/16$ for two complementary faces $A,B$ meeting only at $x$. Roots and orientations of the two based words are those of A4’s definition. A coordinate reflection fixes a site and reverses the charge, so each site mean vanishes.

The change of integration variables $U_i(x)\mapsto(-1)^{\sum_{j<i}x_j}U_i(x)$ is periodic for every even side. Its center factor has product $-1$ around every elementary face. Each face trace changes sign and every charge term is invariant. It preserves product Haar measure. All charge covariances, including those with arbitrary spatial phases, are therefore even in $\beta$. This symmetry by itself gives no uniform Taylor remainder in the volume. That bound is established below.

## The connected two-plaquette calculation

At zero coupling, center reversal of any single Haar link kills a product in which that link appears an odd number of times. The edge supports of distinct $h_\alpha$ are distinct. Indeed the shared vertex is the unique degree-four vertex of its support; the two loops and their displacement signs can then be recovered. At order zero only $\alpha=\gamma$ survives in $\langle h_\alpha h_\gamma\rangle$. The two based holonomies on one support are independent Haar quaternions. In particular each imaginary component has variance $1/4$. This gives $v=\langle h_\alpha^2\rangle_0=3/4096$ and $48v=9/256$.

At order two the normalized expectation contributes
$$
 \frac12\sum_{p,p'}\left(
 \langle h_\alpha h_\gamma t_p t_{p'}\rangle_0
 -\langle h_\alpha h_\gamma\rangle_0\langle t_p t_{p'}\rangle_0
 \right).
$$
There is no first-order denominator term since $\langle t_p\rangle_0=0$. Link-center parity requires the six faces (two in each charge and the two trace insertions) to have zero boundary over $\mathbb F_2$. In the multiset of faces cancel equal pairs. The number of remaining faces is even. Two or four distinct faces cannot close: each of the four edges of any one face needs a different neighbor, since distinct elementary faces share at most one edge. Six distinct faces cannot close here either. Take the two complementary faces of the first charge. Their eight edges would have to be covered by the four remaining faces, each touching one edge of both. Edges in these two different coordinate planes can lie in a common elementary face only if they are incident. The only shared vertex of the two charge faces is the root. Their edges opposite the root cannot be covered this way. These elementary incidence arguments apply on all sufficiently large tori without a winding exception.

It follows that every face occurs an even number of times. For $\alpha\ne\gamma$ this requires the two charges to share one face, with $p,p'$ equal to the two unshared faces. (If both charge faces coincide, their common root and prescribed words coincide.) Choose a link of one unshared face absent from all other distinct faces. Such a link exists since each of two other faces shares at most one edge with it. Conditional on all other Haar links, its based holonomy $U$ is Haar. In the remaining integrand it occurs as $\operatorname{Im}U$ from one charge and $\operatorname{Re}U$ from one trace. The real part is unchanged by moving the base or reversing the trace word. The mixed quaternion moment is zero. Thus all distinct charge terms give zero, even when based at the same site.

For $\alpha=\gamma$ one must have $p=p'$. If $p$ is outside the two charge faces it has a link outside their support, so integrating $t_p^2$ in that link gives $1/4$ and cancels the disconnected term. If $p$ is either charge face, put $T=\operatorname{Re}U$ for that holonomy. Haar on the unit three-sphere gives $\mathbb E T^2=1/4$, $\mathbb E T^4=1/8$ (equivalently use the angular density $2\sin^2\theta/\pi$). Integrating the imaginary part of the other independent face yields
$$
 \mathbb E(h_\alpha^2 t_p^2)
   =\frac{\mathbb E[T^2(1-T^2)]}{4\cdot256}
   =\frac1{8192},\qquad
 \mathbb E(h_\alpha^2)\mathbb E(t_p^2)=\frac3{16384}.
$$
The two choices of $p$ cancel the expansion factor $1/2$. Summing the difference over 48 terms gives $-3/1024$ at contact and zero at every nonzero separation. These are coefficients of $\beta^2$, not second derivatives.

## Why the remainder is uniform over all smearings

Let $V$ be the torus volume and $k$ a torus momentum. Couple two independent complex sources $z_+,z_-$ to $\sum_x e^{\pm ikx}q_x$ and let $P_V=V^{-1}\log Z_V$ be the pressure with these sources, normalized by product Haar at the origin. Its mixed source derivative at zero is the covariance eigenvalue $S_V(k,\beta)$. The following finite-range estimate gives a common complex neighborhood of $(\beta,z_+,z_-)=(0,0,0)$, independently of $k$ and $V$. [Kotecký and Preiss, *Cluster Expansion for Abstract Polymer Models*, pp. 492–493](https://www.math.ucla.edu/~biskup/290k.1.24w/PDFs/Kotecky-Preiss.pdf)

Make a graph with one vertex per action plaquette and one per charge site, joining vertices whose link supports intersect. Its maximum degree is bounded by a fixed $\Delta\ge2$ since each support has bounded size and diameter. Use the factors $1+g_i$ obtained by writing each local exponential as one plus its difference from one. One has $\|g_i\|_\infty\le t$ with
$$
 t=\exp\!\left(\max\{|\beta|,\,3(|z_+|+|z_-|)\}\right)-1
$$
because $|q_x|\le3$. A connected nonempty vertex set $P$ is a polymer of activity $\mathbb E_0\prod_{i\in P}g_i$ of absolute value at most $t^{|P|}$. Disjoint components with no graph edge between them involve disjoint Haar links, hence their activities factor. Expanding the product therefore gives precisely the hard-core polymer partition function.

At most $\Delta^{2(n-1)}$ connected $n$-sets contain any specified vertex: a deterministic spanning-tree traversal returns to that vertex in $2(n-1)$ steps and visits the whole set. Incompatible polymers meet the closed graph neighborhood of $P$. Thus
$$
 \sum_{Q\not\sim P}|w(Q)|e^{|Q|}
 \le |P|(\Delta+1)\frac{et}{1-\Delta^2et}\le |P|
$$
on a fixed sufficiently small polydisc. The Kotecký–Preiss criterion with size $|P|$ gives absolute convergence of the log expansion; its pinned-cluster bound, summed over the possible root polymers, bounds $|\log Z_V|$ by a constant times the number of graph vertices. For example $\sum_Q |w(Q)|e^{|Q|}$ is bounded by the vertex count times $et/(1-\Delta^2et)$. There are $7V$ vertices. This controls the analytic pressure branch at the origin uniformly even at the exceptional momenta $k=-k$.

Cauchy bounds on a smaller polydisc now bound $S_V$ uniformly for complex $\beta$ near zero. Evenness and the coefficients already computed imply $|S_V(k,\beta)-(9/256-3\beta^2/1024)|\le C|\beta|^4$ on a smaller disc with constants independent of $k,V$. For real $\beta$ the torus covariance is translation invariant. Fourier diagonalization gives the asserted quadratic-form inequality for every $f$ with the same constant. Pass to any periodic limit first with $f$ fixed. Taking normalized box indicators next gives the result for the bulk variance using its established existence. This order of operations avoids summing a pointwise correlation remainder over an increasing box.

## Verification

A separate host enumeration fixes one figure eight using signed coordinate symmetries and tests all 30,000 translated figure eights whose root is in $[-2,2]^4$. Overlap of at least four edges is necessary for two more plaquettes to pass link parity. The only 30 distinct compatible charge pairs share a full face and require precisely the two unshared traces. The Haar integral above then kills them. A second check tilts the two independent face holonomies by their own traces and integrates over the two class angles. Its difference quotient at $\beta=10^{-3}$ is $-0.002929687255859395$, against $-3/1024=-0.0029296875$. This two-face test verifies the surviving diagram; it is not a simulation of the full Wilson law.

Two three-generation native PCP OS runs checked the periodic center transformation on all 1,536 plaquettes of a side-four torus, the count of site terms, and the rational contact coefficients. Four supporting Lean declarations passed; three altered statements and an invalid guest request failed in each run. The geometric exclusion and the uniform analytic bound are written arguments. [Host checker](check.py) · [Native guest](worker.c) · [Lean declarations](HaarClover.lean) · [Replay](verify.py) · [Receipts](receipts.zip)
