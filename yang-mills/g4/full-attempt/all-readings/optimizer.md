# Which coarse states attain the first derivative?

Use $J_{\ell,L}$, $J_\alpha$, $k$, $q$, $\lambda$ and $d_n$ from the [all-reading bound](README.md). At fixed $g,\ell,n$ the optimization has a finite size bound independent of the side of the torus. At long lags one elementary square attains the optimum. These claims concern the derivative at $b=0$.

### Removing disconnected spectators

Split the nonempty coarse spin support into its connected components using shared coarse vertices. Gauge intertwiners at disjoint vertex sets factor, so the label space is a tensor product. An elementary magnetic face can meet active edges of only one component. Indeed two retained edges on that face meet at a coarse vertex. Write $r_i$ for the component eigenvalues, $x_i=r_i^n$, $R_i=\prod_{j\ne i}x_j$, and $x=\prod_jx_j$. A change $r_i\mapsto u_i$ in component $i$ multiplies the single-component derivative by $R_i$, by homogeneity of degree $n$ of $d_n$. The full output defect $1-R_i u_i^n$ dominates $1-u_i^n$. Face images belonging to distinct components have different private parities. The unchanged components carry the identity on their intertwiner spaces, so the corresponding operator bound holds for entangled input vectors as well. Summing squared norms gives
$$
 J_\alpha^2\le\sum_i\frac{R_i^2(1-x_i)}{1-x}\,J_{\alpha_i}^2
 \le\max_i J_{\alpha_i}^2 .
$$
The last inequality follows because $\sum_iR_i(1-x_i)$ is the probability of exactly one failure in independent Bernoulli trials with success probabilities $x_i$, at most the probability $1-x$ of any failure. Distinct components can lie close to one another in space. The proof uses absence of shared active links in each insertion and the product-Haar inner product, which also applies when the inserted face meets a spectator at an inactive vertex. [Scalar budget in Lean](AllReadings.lean) · [Two-component transfer test](checks.md)

### Finite reduction for any lag

Fix $g>0$, $\ell\ge2$, $n\ge1$. The fundamental square with $k_0=4\ell$ and $r_0=q^{k_0}$ gives a positive witness
$$
 W=\frac{n r_0^n}{2(1-r_0^n)} .
$$
There are four distinct inside-corner faces. Their singlet deformations keep the perimeter, each has amplitude $1/4$, and $d_n(r_0,r_0)=nr_0^n$. In the input and these four output slots the defect is $1-r_0^n$. Taking their normalized sum proves the bound. The winding cycles at coarse period four do not remove this square. [A4’s full decomposition](../../../observable-normalization/transfer-increments/electric-lag/bends/README.md)

Choose a fine edge count cutoff $K\ge k_0$ with the right side of (1), evaluated at $k=K+1$, $a=q^k$, strictly below $W$. It then excludes every larger $k$ by monotonicity. For a remaining label with maximal spin index $j$, at least $\ell-1$ fine links in a segment carrying $j$ survive each insertion unchanged. Thus $r,u\le q_j^{\ell-1}$. Choose $J$ so that (1) with $\sqrt K$ and $a=q_{J+1}^{\ell-1}$ is below $W$. Since $q_j$ decreases strictly to zero these two cutoffs exist and can be computed. Only connected supports of at most $\lfloor K/\ell\rfloor$ coarse edges and indices $1,\ldots,J$ need be considered. Matrices of the normalized form in their finite intertwiner spaces give their exact squared optima by their largest eigenvalues.

Set $M=\lfloor K/\ell\rfloor$. A sufficient coarse side for exact volume independence is $L/\ell\ge 2M+5$. Lift a rooted connected support along a spanning tree. Its vertices lie in a coarse cube of radius $M$, and the incident fine faces and the link segments needed to read the labels lie inside the cube of radius $M+1$ in coarse units. Reduction modulo the side introduces no identifications there. An extra edge or a cycle closing modulo the side also closes in this lift because its endpoints and their unit neighbors lie in that injective cube. Conversely every retained finite rooted type embeds in these boxes. Electric spectra, local Haar matrix entries and vertex intertwiner spaces for the type agree. This proves equality of the all-state derivative norm across all such tori, at each fixed lag. The cutoff can be very conservative. It gives neither a spatial continuum limit nor equality of a finite magnetic remainder.

### A square wins on sufficiently thick slabs

When the coarse side exceeds four, a four-edge physical support is an elementary square. All higher-spin labels on it are constant around the cycle, by the degree-two invariant constraint. A nonsquare support has at least five coarse edges. For a higher-spin four-cycle put $\rho=q_2/q<1$. All but at most two of its $k_0$ active high-spin fine edges survive. Counting the extra fundamental edges on the inserted face gives $r,u\le q^{k_0}\rho^{k_0-2}$. Thus every competitor is strictly below the square if
$$
 2\left(1+\frac1{n(1-q^4)}\right)\max\left\{
   \frac{\sqrt{5\ell}\,q^{\ell n}}{1-q^{5\ell n}},
   \frac{\sqrt{k_0}\,\rho^{(k_0-2)n}}{1-(q^{k_0}\rho^{k_0-2})^n}
 \right\}<1. \tag{3}
$$
Here (1) has been compared with the weaker witness $n r_0^n/2$. The left side decreases to zero as $n\to\infty$. Any certified lag works at all longer lags. Different fundamental square inputs have orthogonal images, including when their supports share edges; arbitrary superpositions therefore attain the same norm as a single square.

The extra straight winding four-cycles at coarse side four are also covered. Define $t=q_2$ and
$$
 u_d=q^{k_0+4-2d},\qquad v_d=u_dt^d,\qquad
 B_d=\frac{d_n(u_d,r_0)^2}{1-u_d^n}
       +3\frac{d_n(v_d,r_0)^2}{1-v_d^n}.
$$
For either loop, a touching face sharing a path of $d$ consecutive edges supplies orthogonal singlet and triplet projections with amplitudes $1/4,\sqrt3/4$. This follows by integrating the shared fundamental holonomy and resolving $2\otimes2=1\oplus3$. A straight winding has $4k_0$ single-edge faces and no corners. The square has $4k_0-8$ single-edge faces and four corners. In fact $B_2>2B_1$ for all $g,n$. To see this write $u_d=r_0 z_d$, $v_d=r_0 z_dt^d$, where $z_1=q^2$ and $z_2=1$. The singlet multiplier at $d=2$ exceeds twice that at $d=1$, since $(1-q^4)/(q^2-q^4)>2$ and the geometric sum increases with $z$. Its output defect is smaller. At $d=1$ the magnitude of the triplet multiplier is less than one half of the singlet multiplier. The ratio is bounded by $|t-q^2|/(1-q^2)<1/2$. The lower bound $t>(4q^2-1)/3$ follows from $\mathrm{Var}(\mathrm{Tr}U/2)>0$ in the one-link Wilson law, and $t<q$ gives the upper bound. The triplet output defect at $d=1$ is larger than the singlet defect. Hence $B_1$ is less than $7/4$ times its singlet term while $B_2$ exceeds four times that term. Winding sectors retained by the physical projection can never outperform the square among these two four-cycle choices.

It follows under (3), uniformly in all admissible volumes, that the full norm is exactly
$$
 J_{\ell,L}^2=\frac{(4k_0-8)B_1+4B_2}{16(1-r_0^n)} .
$$
In particular $J_{\ell,L}\sim n q^{4\ell n}/2$ as $n\to\infty$ at fixed $g,\ell$. Only the four resonant corner singlets have $u=r_0$; the other multipliers are $O_g(r_0^n)$ at fixed mesh. [A4’s single-input formula](../../../observable-normalization/transfer-increments/electric-lag/bends/README.md) · [Effective examples of (3)](checks.md)

For a spin-index $j$ four-cycle, the same path calculation gives squared face weights $(j+2)/(8(j+1))$ and $j/(8(j+1))$ at spins $(j+1)/2$ and $(j-1)/2$. To obtain them, couple the shared path matrix to the fundamental. The squared Haar masses of the two orthogonal summands are proportional to their dimensions in the tensor product; they sum to $1/4$ by the private-edge integral. The unshared parts of the two loops are independent Haar holonomies, so their matrix entries contract to identities in this trace. For $d$ shared edges the corresponding electric eigenvalues are $q_j^{k_0-d}q^{4-d}q_{j\pm1}^{d}$ with $q_0=1$. These give the entire one-dimensional input Gram block for each such labeling. [Smallest-torus enumeration](spectrum.py)

There is also a positive physical-time regime in which the optimum is known. With $g=\kappa/a_t$ and $n/g\to y=s/\kappa>0$, the two numerators inside the maximum in (3) tend to $\sqrt{5\ell}\,e^{-3\ell y/2}$ and $\sqrt{k_0}\,e^{-5(k_0-2)y/2}$. The corresponding denominators tend to $1-e^{-15\ell y/2}$ and $1-e^{-[3k_0+5(k_0-2)]y/2}$. The outside factor tends to $2(1+1/(6y))$. For $y\ge1,\ell\ge2$ both comparisons are strict; their largest bounds occur at $y=1,\ell=2$, giving a maximum below $0.37$ after the outside factor. Thus at fixed mesh and fixed spatial spacing (3) eventually holds along these time refinements. The limiting norm for the Hamiltonian magnetic coupling $j$ follows by taking $a_t J_{\ell,L}$ in the displayed formula. This concerns the derivative at $j=0$. [Original Hamiltonian formulation](https://doi.org/10.1103/PhysRevD.11.395)
