# From the electric transfer to static covariances

Use normalized Haar measure $dx$ on a finite spatial graph, SU(2) on each edge and the vertex-gauge-invariant Hilbert space. Assume a loopless spatial multigraph containing a cycle of girth $g\ge2$. Opposite positive lattice links on a two-site periodic direction are distinct edges. The spatial potential is $V=\sum_p\chi_p/2$, where $\chi_p=\operatorname{Tr}_{\mathbf2}U_p$ is real and unnormalized. Set
$$
 M=e^{\beta_s V/2},\quad Z=\int M^2 dx,\quad d\mu=M^2 dx/Z,\quad
 w=M/\sqrt Z,\quad Q=I-|w\rangle\langle w|,\quad D=\|M\|_\infty^2/Z.
$$
Multiplication by $M$ is bounded and invertible at fixed regulator. The same transfer reduction works for any strictly positive bounded gauge-invariant multiplier bounded away from zero. Integrating one temporal link per vertex gives $T=MK_tM$ on the invariant space. Each one-link temporal kernel has been divided by its scalar Haar integral. The normalized transfer and its connected part are $S=T/\lambda_0$ and $S_c=S-P_t$, with $P_t$ its vacuum projection. For positive temporal coupling the strictly positive continuous configuration kernel gives a simple positive vacuum $\Omega_t$. [Periodic Wilson construction](../periodic-time/) · [Lüscher](https://doi.org/10.1007/BF01614090)

Let $z=\beta_t/4$, $u=I_2(\beta_t)/I_1(\beta_t)$. A spin network of edge dimensions $d_e$ diagonalizes $K_t$ with eigenvalue $\prod_e I_{d_e}(\beta_t)/I_1(\beta_t)$. Indeed character expansion diagonalizes central convolution, and the commuting vertex projection retains the intertwiner multiplicities. In the two positive Bessel series the factorial comparison $(j+1)!/(j+d)!\le 1/d!$ gives $I_d/I_1\le (\beta_t/2)^{d-1}/d!\le z^{d-1}$. Also $u/z=1+O(z^2)$. [Baez, finite-graph spin-network basis](https://arxiv.org/abs/gr-qc/9411007) · [Parent compact-group transfer calculation, §1](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/blob/aca29276aa180af3c81ccc9f3aa06b4e2ae4d404/edition/PAPERS/E2_Compact_Group_Transfer_Spectra_and_Ultraviolet_Operator_Limits/source/01_editable_Compact_Group_Transfer_Operators.md)

The support of a nonconstant invariant spin network has no leaf, since an isolated nontrivial representation at a vertex has no invariant vector. It contains a cycle. Its total degree $\sum_e(d_e-1)$ is at least $g$. At equality its entire support is a single simple girth cycle with fundamental labels. Each bivalent intertwiner there has dimension one. The unnormalized trace $\chi_i$ has Haar norm one, since the loop holonomy is Haar. Distinct unoriented girth cycles are orthogonal by integration over an edge in their difference. Write $\Pi$ for the resulting finite-rank projection. For $0<z<1$,
$$
 K_t=P_{\mathbf1}+u^g\Pi+R,\qquad 0\le R,\quad \|R\|\le z^{g+h}.
$$
One can always take $h=1$. On cubic tori with $L\ge6$ take $g=4,h=2$. The edges with odd $d_e-1$ have even incidence at every vertex by the central sign of SU(2), hence decompose into circuits. No odd circuit of length at most five exists on these tori. This excludes total degree five. The electric remainder bound costs no volume factor.

Define $U:\mathbb C^r\to\mathcal H$ by $Ue_i=Q(w\chi_i)$, one column per shortest cycle. Then $U^*U=\Gamma=(\operatorname{Cov}_\mu(\chi_i,\chi_j))_{ij}$. This matrix is positive definite. A zero-variance linear combination would be constant $\mu$-almost surely, hence Haar-almost surely since the density is strictly positive. Haar orthogonality to constants and among the traces forces all coefficients to vanish.

For small $z$ with $Dz^g\le1/4$, the following bound holds with a constant independent of the volume for $2\le g\le4$:
$$
 \left\|S_c/u^g-UU^*\right\|\le C\left(Dz^h+D^2 z^g\right)=:\delta.
$$
To see it, $T/Z=P_w+E$ with $0\le E\le Dz^g I$. Its top eigenvalue $l$ lies in $[1,1+Dz^g]$. Applying $Q$ to the eigenvector equation gives $\|Q\Omega_t\|\le Dz^g$. Choose the positive phase. The two rank-one projections differ in norm by $\|Q\Omega_t\|$, and $\|\Omega_t-w\|\le2Dz^g$. Sandwich $T/Z$ between $Q_t=I-P_t$ and divide by $l$. The vacuum term costs at most $(Dz^g)^2$. Replacing $Q_t$ by $Q$ on either side of $M\Pi M/Z$ costs at most $2D^2z^g$ before multiplication by $u^g$. Its centered compression is exactly $UU^*$. Replacing $1/l$ by one there costs at most $D^2z^g$. The remaining kinetic term costs $Dz^{g+h}$. Divide by $u^g$ and use the Bessel estimate near zero. In particular for $L\ge8$, $\delta=O(Dz^2+D^2z^4)$. Here and below a bound denoted $\delta$ may be increased by an absolute constant. For the cubic action $Z\ge1$ by Jensen and the Haar mean of every plaquette trace is zero, so $D\le e^{3|\beta_s|L^3}$.

By the min–max principle the first $r$ excited eigenvalues divided by $u^g$ differ from the ordered eigenvalues of $\Gamma$ by at most $\delta$. All subsequent scaled eigenvalues are at most $\delta$. These comparisons hold on each translation sector if the potential is invariant. At fixed volume and fixed spatial coupling they resolve the entire first cluster. For $L=2,3$ the $3L^2$ coordinate windings exhaust the shortest cycles. At $L=4$ they join the $3L^3$ plaquettes. At $L\ge5$ only the plaquettes remain. Indeed a noncontractible cycle of length at most $L$ must be a straight winding, and a lifted contractible simple cycle of length four is a unit square. On the fixed-volume isotropic path $\Gamma\to I$, giving $-\log(\lambda_1/\lambda_0)-g\log(4/\beta)\to0$. Volume-uniform bounds with a less precise prefactor were obtained by the earlier temporal forest argument. [Rectangle gap result](../connected-rectangles/gap.md)

For bounded gauge-invariant slice tests $F,G$ define $c(F)_i=\int (\chi_i-\mu\chi_i)F\,d\mu$. At each fixed positive integer $k$, the infinite-time vacuum correlation at separation $k$ obeys
$$
 \lim_{z\downarrow0}u^{-gk}\operatorname{Cov}(\overline F_0,G_k)
 =c(F)^*\Gamma^{k-1}c(G).
$$
Indeed the vectors $F\Omega_t,G\Omega_t$ tend in norm to $Fw,Gw$. The scaled transfer converges in norm to $UU^*$ and $(UU^*)^k=U\Gamma^{k-1}U^*$. The use of vacuum subtraction matters even at fixed $\beta_s$; ordinary uncentered spatial moments would introduce an extra rank-one form.
