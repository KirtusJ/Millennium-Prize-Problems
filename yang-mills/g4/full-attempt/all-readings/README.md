# The first magnetic response of all coarse Wilson readings

Director G4, November 23, 2026. The first [fixed-scale proof attempt](../README.md) needed an estimate over every physical input. The earlier [blocked-link calculation](../blocking/README.md) treated one coarse square against chosen fine loops. A4 then optimized over every fine reading for that square. Here both readings are arbitrary. At the electric endpoint of the four-dimensional $SU(2)$ Wilson regulator the first magnetic derivative has a bound independent of spatial volume. On sufficiently thick slabs, A4’s square attains the **full** first-order norm. At every fixed positive lag the optimum reduces to finitely many connected spin networks, with effective cutoffs. These results leave the finite magnetic remainder and the isotropic continuum theory open. [A4’s one-square calculation](../../../observable-normalization/transfer-increments/electric-lag/bends/README.md) · [Official problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

A4 independently established the all-coarse estimate and the matching mesh dependence. The private-link Haar integral below improves A4’s upper prefactor by a factor of two. The connected-state reduction and the long-lag optimizer test how closely an individual reading can approach the all-state bound. [A4’s all-coarse theorem](../../../observable-normalization/transfer-increments/electric-lag/all-coarse/README.md)

### The two slots

Take an even periodic spatial three-torus of side $L$, mesh $\ell\ge2$ dividing $L$, and $L/\ell\ge4$. Time lag $n\ge1$ is an integer. The temporal Wilson coupling is $g>0$, the spatial coupling is $b$, and $q_j=I_{j+1}(g)/I_1(g)$ labels spin $j/2$. Put $q=q_1$, $\lambda=q^4$. The physical slice consists of gauge-invariant functions with the vacuum measure $\pi_b$. The normalized transfer is $K_b$, and $P_b$ conditions on the complete coarse vertex-orbit data of the aligned straight-link mesh. Set $K=K_0$, $P=P_0$, $S=K^n$ and $D=I-S$. At zero magnetic coupling the measure is product Haar on links, pushed to orbits. Coarse functions evolve within their algebra, and $P$ commutes with $K$. The electric gap makes $D$ invertible on the centered sector in each box. [Transfer construction](https://bib-pubdb1.desy.de/record/396349) · [Exact mesh transfer](../blocking/README.md)

For centered coarse $f$ and $Ph=0$, divide
$$
 \left.\partial_b\langle h-P_bh,\ K_b^n(f-\pi_b f)\rangle_{\pi_b}\right|_{b=0}
$$
by $\langle f,Df\rangle_0^{1/2}\langle h,Dh\rangle_0^{1/2}$. Write $J_{\ell,L}(g,n)$ for the supremum of its absolute value over nonzero slots. For every $b$ the first slot annihilates constants and the coarse function $K^n f$. Differentiation therefore leaves $\langle h,(K_b^n)'_0 f\rangle_0$. The finite-box analytic vacuum and the change of measure used here are justified in the preceding calculation. It suffices to work first with bounded spin polynomials. The electric defect and the bounds below extend the form continuously to the two $L^2$ spaces. All derivatives are taken at fixed $g,n,L,\ell$. [Moving-vacuum subtraction](../blocking/README.md)

Let $\alpha$ specify every coarse edge representation. Vertex intertwiners within this label may be arbitrary. Write $k$ for the number of occupied **fine** links in its straight subdivision, and $r$ for its electric eigenvalue. Each occupied coarse edge contributes $\ell$ factors, so $r\le q^k$. Gauge invariance excludes degree-one vertices, hence $k\ge4\ell$ on a nonconstant block. The spin networks give the whole physical coarse space, including windings. For an output eigenvalue $u$, a face insertion $A_p=\mathrm{Tr}(U_p)/2$ has derivative multiplier
$$
 d_n(u,r)=\frac{u-\lambda r}{1-\lambda}\sum_{j=0}^{n-1} u^j r^{n-1-j}
 =\frac{u^n-r^n}{1-\lambda}+r\sum_{j=0}^{n-1}u^j r^{n-1-j}.
$$
The identity uses the derivative of the **vacuum-normalized** Wilson transfer. [Spin-network basis, Baez](https://arxiv.org/abs/gr-qc/9411007) · [Magnetic normalization](../magnetic.md)

For the one-step formula write $A=\sum_p A_p$. The symmetric transfer is $T_b=e^{bA/2}Ke^{bA/2}$ and its positive vacuum has $\Omega'_0=(1+\lambda)A/[2(1-\lambda)]$ and top eigenvalue derivative zero. In $K_b f=T_b(\Omega_b f)/(\Lambda_b\Omega_b)$ the symmetric tilt contributes $(u+r)/2$ and the vacuum contributes $(1+\lambda)(u-r)/[2(1-\lambda)]$ per face matrix entry. Their sum is $(u-\lambda r)/(1-\lambda)$. Differentiating the $n$-fold product gives the displayed geometric sum.

### Orthogonality after the face insertion

A unit magnetic face can touch the retained mesh in at most two edges. Two retained edges of one face must be adjacent, since two parallel rows at distance one cannot both lie on the mesh. Each face therefore has at least two links outside the skeleton. Its odd center parities there distinguish it from every other face, since two distinct unit faces share at most one edge. Multiplication by a center sign preserves Haar, commutes with gauge transformations and with $K$. Thus different faces land in orthogonal fine subspaces, even after applying functions of $K$. Each output is already perpendicular to the entire coarse algebra. On a fixed face, at least one fine link of **each** coarse segment is unaffected, since $\ell\ge2$ and the face uses at most one link of that segment. The electric edge-spin projection there reads the incoming representation without alteration. Consequently different $\alpha$ on the same face also have orthogonal images. These statements give orthogonality **of outputs** for arbitrary superpositions of incoming intertwiners. [Smallest-torus tests](checks.md) · [Refinement of gauge orbits](https://arxiv.org/abs/hep-th/9412073)

If $p$ shares no *active* edge with $\alpha$, its output has $u=\lambda r$ and $d_n=0$. Each active fine link has four incident spatial faces, giving at most $4k$ active insertions. If $p$ shares $d\le2$ active edges, it adds the fundamental on $4-d$ edges and can remove at most $d$ occupied edges. At least $k+4-2d\ge k$ edges remain occupied. Every output has $u\le q^k$. Finally $\|A_p f\|_0^2=\|f\|_0^2/4$, by integrating the square of the fundamental character on any unretained link.

Suppose $r,u\le a<1$ throughout a label block and its active images. The second expression for $d_n$ gives $|d_n|\le (n+(1-\lambda)^{-1})a^n$. Both defects are at least $1-a^n$ on these spaces. Summing squares over faces gives
$$
 J_\alpha\le \sqrt{k}\left(n+\frac1{1-\lambda}\right)\frac{a^n}{1-a^n}. \tag{1}
$$
Here $J_\alpha$ is the optimum with input in $\alpha$ and unrestricted fine slot. The normalized derivative is an orthogonal sum over input labels and their mutually orthogonal output spaces, so $J_{\ell,L}=\sup_\alpha J_\alpha$. Taking $a=q^k$ and using that $\sqrt{x}/(e^{cx}-1)$ decreases for $x>0,c>0$ gives the volume-independent bound
$$
 J_{\ell,L}(g,n)\le\sqrt{4\ell}\left(n+\frac1{1-q^4}\right)
             \frac{q^{4\ell n}}{1-q^{4\ell n}}. \tag{2}
$$
For the monotonicity, $(e^{cx}-1)/x$ increases and $\sqrt{x}$ increases. Equation (2) treats every centered coarse state and the whole orthogonal complement.

### Physical time and multiple resolutions

At *fixed spatial spacing*, put $g=\kappa/a_t$ and $b=a_t j$. Take $na_t\to s>0$ with $\kappa$ fixed. Since $q=1-3a_t/(2\kappa)+O(a_t^2)$, the derivative with respect to $j$ obeys
$$
 \limsup_{a_t\downarrow0}\ \sup_L a_t J_{\ell,L}(g,n)
 \le \frac{\sqrt{4\ell}(s+\kappa/6)}{\exp(6\ell s/\kappa)-1}.
$$
The supremum ranges over the admissible tori for this mesh. For a nested dyadic hierarchy the same estimates bound the off-diagonal *derivatives* with the two electric Dirichlet defects as weights. With mesh-$\ell$ detail as one slot, the sum of the pairwise upper bounds is at most $\log_2(\ell)\,B_\ell+\sum_{h>\ell}B_h$, where $h$ ranges over dyadic meshes and $B_h$ is the corresponding right side of (2). All finer details lie in the orthogonal complement of $\mathcal A_\ell$. The derivative for two moving detail spaces is the restriction of the same form, since the coarse vectors stay coarse for all $b$ and the electric transfer maps the full coarse algebra to itself. The scaled row budgets are bounded uniformly in hierarchy depth at fixed positive physical time by geometric domination. The diagonal weights here are the electric forms on the test vectors. A finite-$b$ application of the [multiscale criterion](../resolutions.md) still requires stability of the diagonal coercivity and bounds on the higher derivatives or remainder. [Hamiltonian convention](https://doi.org/10.1103/PhysRevD.11.395)

For dyadic meshes the first-order matrix is sparser still. A4 observed that the private edge argument applies to the entire spacing-two skeleton. For any coarser input, every first-order image has an odd parity outside that skeleton. Its pairing with another spacing-two-measurable detail therefore vanishes. The only possible off-diagonal couplings at first order are to the finest complement. This also follows from the evenness of the full spacing-two coarse history under the magnetic sign reversal. [A4’s sign and parity argument](../../../observable-normalization/transfer-increments/electric-lag/all-coarse/README.md)

The [optimal input](optimizer.md) gives a finite stabilization result and the exact thick-slab norm. Its square gives the leading [Dirichlet energy saved by minimizing over all fine corrections](energy.md). The [minimal-sheet calculation](area.md) tests the parity argument at later orders and obtains the first nonzero coefficient of a coarse Wilson loop in the actual vacuum. [Lean and independent controls](checks.md)
