# A uniform quartic mass coefficient in the spatial thermodynamic limit

The leading band has three orientations at each lattice momentum $k$. The possibility of different momenta coalescing as $L$ grows matters even for a rest mass. The following argument bounds the top of the *whole* spectrum, then shows that a bulk scalar field actually detects transfer values that high. It gives the same $O(u^6)$ accuracy for the mass in infinite spatial volume as in all even periodic cubes $L\ge8$. The time step and spatial mesh remain fixed.

## Keeping the three branches

Use the [positive-lag moment argument](README.md) with the Fourier projection of a bounded slice test at any allowed momentum. The test can occupy every link of the box: its prefactor drops out when the moment order tends to infinity. The covariance uses the complex conjugate at its first end. Translation sectors are orthogonal to one another, and the vacuum is removed in the zero sector.

From the fixed-box joint expansion define the real symmetric matrix
$$
 B(k)=(50/3-\widehat k^2)I+2A,\quad
 A_{ij}=4\cos(k_i/2)\cos(k_j/2)\ (i\ne j),\quad A_{ii}=0,\qquad
 \widehat k^2=\sum_i4\sin^2(k_i/2).
$$
Let $\theta_1(k)\ge\theta_2(k)\ge\theta_3(k)$ be its eigenvalues and put
$$
 b_i(z,k)=1-7z^2/24+z^4\left(23/384+\theta_i(k)/256\right).
$$
These polynomials in the coupling have bounded coefficients uniformly in momentum. At fixed $L$ every upper spectral value $x$ equals one of $b_i(\beta,k)+O_L(\beta^6)$. Indeed the logarithm relative to $u^4$ has eigenvalues $-2u^2+u^4\theta_i(k)+O_L(u^6)$. Use $u=(\beta/4)(1-\beta^2/24+\beta^4/384+O(\beta^6))$, exponentiate, and multiply by $u^4/t$. This uses the joint result only in its fixed-box Taylor domain. [B4's joint expansion](../../transfer-operator/girth-shell/joint.md) · [Münster's published matrix](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf)

Take the degree-ten polynomial
$$
 p_{z,k}(x)=x^7\prod_{i=1}^3(x-b_i(z,k)).
$$
At fixed box, $p_{\beta,k}(x)=O_L(\beta^{14})$ on the entire centered spectrum in this sector. In the lower cluster $x=O_L(\beta^2)$. In the upper cluster one factor costs $O_L(\beta^6)$ and the other two each cost $O_L(\beta^4)$, including at degeneracy. On $|z|=R=1/2048$, let $B_0=(1+\max_{|z|=R,k,i}|b_i(z,k)|)^3$. The coefficient absolute sum of $p_{z,k}^{2s}$ is at most $B_0^{2s}$ and its degree is $20s$. The holomorphic moment function built from this polynomial has a zero of order at least $28s$ at zero. The same maximum principle, positivity and large-order argument now give
$$
 |p_{\beta,k}(x)|\le B_0 A^{10}(\beta/R)^{14},
 \qquad A=(4/R)^4 ,
$$
uniformly in $L,k$ and all the centered spectral values. In particular, on $x\ge1/2$ the distance to the nearest $b_i$ is $O(\beta^{14/3})$, with a constant independent of momentum. At repeated roots this estimate by itself does not give sixth-order accuracy for each individual energy.

This also bounds the discrepancy of the *ordered* three levels by a constant times $\beta^{14/3}$ for all allowed momenta. At a specified small $\beta$ join neighboring root intervals of radius $K\beta^{14/3}$ whenever they overlap, with $K$ the uniform nearest-root constant. Any gap between components remains open all the way down to zero: root differences scale exactly as $\beta^4$, whereas interval widths scale as $\beta^{14/3}$. Continuity of the spectral projections therefore preserves the count in each component from the fixed-box expansion. A component has at most three centers and diameter at most six interval radii. This supplies both inclusions and handles exact crossings without choosing eigenvectors.

## Upper edge of the full spectrum

Write $b_*(z)=b_1(z,0)$, so $\theta_1(0)=98/3$. Since the row sums of absolute values of $A$ are at most eight, $\theta_1(k)\le98/3-\widehat k^2$. Outside any fixed small neighborhood of zero the latter is below $98/3$ by a fixed positive amount. The resulting $\beta^4$ separation from $b_*$ dominates the $O(\beta^{14/3})$ nearest-root error for sufficiently small $\beta$, uniformly in volume. Inside a sufficiently small neighborhood the top matrix eigenvalue is simple, separated from both others by a constant, since at zero its separation is 24. A point near either lower root is again below $b_*$ for small enough $\beta$. At a point near the top root the two remaining factors $|x-b_i|$ are at least a constant times $\beta^4$ each. Dividing the product estimate by these factors improves the top-branch error to $O(\beta^6)$. Thus every centered spectral value in every momentum sector satisfies $x\le b_*(\beta)+O(\beta^6)$.

For the matching finite-volume lower bound restrict to the zero-momentum, rotation-invariant subspace. All elementary faces occur in a single orbit under translations and cubic rotations, and the fundamental character is unchanged by reversing its orientation. Only the scalar direction of the electric first band lies in this subspace. At each fixed box it continues to the simple branch with center $b_*$; the other two orientations at zero momentum transform as the nontrivial two-dimensional representation. Apply the polynomial $x^3(x-b_*(z))$ to this symmetry sector. It is $O_L(\beta^6)$ on both fixed-box clusters. Repeating the moment proof yields a uniform $O(\beta^6)$ bound on this polynomial; every value there above $1/2$ is therefore $b_*+O(\beta^6)$. The scalar upper projection has rank one throughout the small interval by the continuous-rank argument. This proves the claimed finite-volume mass by taking $-\log(tx)$.

At zero momentum the same one-root polynomial on the two-dimensional cubic representation uses $\theta_2(0)=\theta_3(0)=26/3$. Its rank in the upper cluster is two; cubic symmetry keeps these two eigenvalues equal. Consequently the zero-momentum tensor and scalar masses differ by $24u^4+O(u^6)$ uniformly in the periodic boxes. This concerns the two specified representations at zero momentum.

## A bulk witness, without assuming convergence of global eigenvectors

Let $g_y$ be the sum of the three elementary fundamental traces anchored at site $y$, divided by $\sqrt3$. In a torus of $V=L^3$ sites the scalar wave packet $G_L=V^{-1/2}\sum_y g_y$ has centered lag-$j$ correlation
$$
 D_{j,L}(z)=\sum_y \operatorname{Cov}_z(g_0(0),g_y(j)).
$$
At zero coupling its variance is one by Haar orthogonality. At fixed box the leading coefficient of $D_{1,L}/t$ is also one since $G_L$ is a unit vector in the electric first band at zero. Both statements admit errors $O(\beta)$ independent of volume, as follows.

The individual summands are bounded on the disk $|z|\le R$ by a common constant for every $L,y,j$: each end uses a bounded number of links. Their Taylor coefficients of degree less than $\max(0,\operatorname{dist}_\infty(0,y)-3)$ vanish on the periodic spatial metric. In an open-time finite Haar integral a coefficient of connected covariance is a joint cumulant of the two fixed readings and the selected face insertions (with repetitions allowed). A partition of its variables into two independent groups kills the cumulant by factorization of the generating integral and taking its logarithm. Thus a nonzero term requires a chain of shared links connecting the supports. The base sites of two cofacial links differ by at most one in the spatial sup norm. An endpoint contributes at most one additional site displacement. This proves the stated conservative distance bound, independent of time separation. Holomorphic convergence from open time preserves these zeros. At $|z|\le R/2$ the maximum principle bounds the summand by the common constant times $2^{-\max(0,\operatorname{dist}_\infty(0,y)-3)}$. The sum of these bounds is uniform in dimension-three tori. Consequently $D_{0,L}$ is uniformly bounded on this smaller disk, as is $D_{1,L}/t$ by removability and its boundary bound. Their values at zero and Cauchy's estimate give the claimed $1+O(\beta)$ for both.

In particular the centered scalar measures of $G_L$ have mass $1+O(\beta)$ and scaled first moment $1+O(\beta)$. For sufficiently small fixed positive $\beta$, they carry mass bounded below by a positive constant in the closed interval $b_*(\beta)\pm C\beta^6$. Otherwise the first moment could not have this size: on the lower cluster $x=O(\beta^2)$, and on the upper cluster $x\le2$. Here and in the limit one can, for example, take a weight floor of $1/4$ after reducing the coupling interval.

For each fixed $j,\beta$, the summable spatial tail and convergence of local Wilson correlators give $D_{j,L}\to\sum_{y\in\mathbb Z^3}\operatorname{Cov}_\beta(g_0(0),g_y(j))$. In the infinite-volume vacuum use the centered sum of $g_y$ over a growing lattice cube divided by the square root of its site count. Its lag-$j$ moments converge to the same sum: the normalized count of pairs of sites at displacement $y$ tends to one and is at most one. At fixed $\beta$ both families of transfer measures are supported on the compact interval $[0,1]$ before scaling. The common limiting moments, including total mass, identify their weak limit. The closed scalar interval retains the finite-torus weight floor by Portmanteau. Every finite packet in the infinite-volume vacuum has support in the closed spectrum of the centered bulk transfer; the weak limit does too. Hence the bulk spectrum meets this interval even if the spatial averages have no strong Hilbert-space limit. The common full-spectrum upper bound passes from the tori on dense local half-history vectors as in the [main proof](README.md). Combining them gives
$$
 \Delta_\infty=-4\log u+2u^2-\tfrac{98}{3}u^4+O(u^6)
 \quad(\beta\downarrow0).
$$
This is a statement about the bottom of excited spectral support. No normalizable zero-momentum eigenstate in infinite space is required.

## Fixed anisotropy

The argument also applies on rays $\beta_t=\beta$, $\beta_s=\alpha\beta$ for fixed $\alpha>0$, uniformly when $\alpha$ stays in a compact subset of $(0,\infty)$. Shrink the complex disk by $\max(1,\sup\alpha)$ so that both couplings lie in the input disk. Put $s=I_2(\alpha\beta)/I_1(\alpha\beta)$. For the bottom mass in finite periodic or infinite spatial volume the conclusion is
$$
 \Delta=-4\log u+2s^2-\tfrac{26}{3}s^4-24s^2u^2+O_\alpha(\beta^6)
$$
To see the separation used in the proof, write $s/u=\alpha+O_\alpha(\beta^2)$. The quartic orientation matrix multiplying $u^4$ is now $\alpha^4(A_c-\tfrac43I)+\alpha^2(12I+A_e)$ in B4's notation. For the cube incidence, $A_c=tt^T-2I$ and its top is $10-\widehat k^2$; the edge-sharing adjacency has top at most twelve. The constant orientation attains both maxima at zero, with a simple top separated there from the transverse pair. Off a neighborhood of zero the strict deficit is at least $\alpha^4\widehat k^2$. Use as centers the degree-four Taylor polynomials of $(u^4/t)\exp[-2s^2+u^4\theta_i(k,\alpha)]$. Their coefficients, fixed-box zero orders, disk bounds and top-root separation give the same proof. The normalized scalar spatial sum again has unit leading variance and first scaled moment. This is a lattice anisotropy estimate. It does not supply a physical scale prescription for the weak end.
