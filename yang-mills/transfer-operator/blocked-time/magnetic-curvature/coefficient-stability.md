# Stabilization of the magnetic gap coefficients

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For the anisotropic SU(2) Wilson transfer, fix a temporal coupling $g>0$. On the even spatial three-torus of side $L\ge6$, let $m_L(g,b)$ be the physical log gap at spatial coupling $b$. For each integer $r\ge0$, its Taylor coefficient $[b^r]m_L(g,b)$ has **exactly the same value on every even side $L\ge2r+6$**. In particular one box of side 14 suffices for the quartic coefficient. All the odd coefficients vanish. Writing $c_r(g)$ for the stabilized coefficient, there are finite constants $B_g,D_g$ such that
$$
|c_r(g)|\le B_gD_g^r(r!)^3 .
$$
This controls the formal coefficients at each fixed temporal coupling. Convergence of the stabilized series, a volume-uniform Taylor remainder, and continuation to isotropic weak coupling remain open.

Drouffe and Zuber describe connected plaquette diagrams for glueball correlations and the cumulant expansion in §3.1.6. Linked-cluster calculations also exist for the scalar gap of the SU(2) lattice Hamiltonian in three spatial dimensions. Here the unperturbed measure keeps the temporal Wilson coupling exact. The coefficient equality follows before the long-time limit by counting spatial supports, while the identification with the physical gap uses the isolated scalar branch in each fixed box. [Drouffe–Zuber](https://www.lpthe.jussieu.fr/~zuber/MesPapiers/dz_PR83.pdf) · [Hamiltonian linked-cluster calculation](https://www.sciencedirect.com/science/article/pii/0550321386905675) · [G4’s electric spectrum](../../../g4/full-attempt/electric.md) · [B4’s branch selection](spatial-momentum.md)

## Extracting the coefficient from a finite-time covariance

Let $N=3L^3$, $\phi_p=\operatorname{Tr}U_p$, $F=N^{-1/2}\sum_p\phi_p$, $A=\tfrac12\sum_p\phi_p$, and $T_b=e^{bA/2}Ke^{bA/2}$, with the scalar Wilson normalization removed. At $b=0$, $F$ has Haar mean zero and norm one. Its kinetic eigenvalue is $\lambda=q^4$, $q=I_2(g)/I_1(g)$. Work in the gauge-invariant sector fixed by translations and the cubic symmetries. In this sector $\lambda$ is simple because the group acts transitively on elementary squares. The vacuum is simple and the remaining spectrum lies in $[0,\max(q^5,q_2^4)]$ where $q_2=I_3(g)/I_1(g)$. These separations in the scalar sector depend only on $g$. For each fixed $L$, the continued scalar branch gives the full physical gap near zero. Indeed the first-order splitting vanishes, and the second-order splitting on the entire plaquette eigenspace has its simple maximum on the constant vector. This is exactly the branch selected by $F$. [Electric calculation and magnetic splitting](README.md)

Take an open time interval from $-H$ to $M+H$, for integers $H,M\ge1$, with constant boundary vectors. Under the unperturbed law each spatial edge carries an independent stationary Haar Markov chain with transition given by the normalized one-link electric convolution. This representation uses the product kinetic operator before gauge projection. It agrees with the physical transfer for the gauge-invariant insertions and boundary vectors here, since that operator preserves the physical sector. Tilt the path measure by $\exp(b\sum_u w_u A(u))$, with $w_u=1$ on interior slices and $1/2$ at the two ends, as in the product of $T_b$ kernels. Let $C_{L,H,M}$ be the normalized connected covariance of $F(0),F(M)$ in this measure.

Differentiate the logarithm of the finite path integral with two independent sources coupled to $F(0),F(M)$. The coefficient of order $r$ in their covariance is
$$
\frac{1}{N\,2^r r!}
\sum_{p_0,\ldots,p_{r+1}}\ \sum_{u_1,\ldots,u_r}
\left(\prod_{i=1}^r w_{u_i}\right)
\operatorname{cum}_0\!\big(\phi_{p_0}(0),\phi_{p_{r+1}}(M),
                         \phi_{p_1}(u_1),\ldots,\phi_{p_r}(u_r)\big).
$$
Repeated faces and equal times are included. A tuple with disconnected spatial edge support has zero cumulant: form a graph on its labeled face occurrences, joining two whenever they use a common spatial edge at any times. Distinct components depend on independent collections of complete edge chains. The product of the component generating functions becomes a sum after taking its logarithm. This also removes source-independent vacuum contributions.

By translation and cubic symmetry the sum over $p_0$ cancels $N$. Fix that face at the origin. Every surviving tuple lifts uniquely to a rooted tuple in the infinite cubic lattice when $L\ge 2r+6$. To see this, grow along a spanning tree of the overlap graph. Once the shared edge is lifted, the oriented coordinate axes and the position of the edge in the child square fix the child lift. For repeated copies one may use any common edge. Starting from the fixed root, each new unit square extends the coordinate range by at most one in each direction. All vertices lie in $[-(r+2),r+2]^3$. Reduction modulo $L$ is injective there. In particular the tree lift preserves every additional coincidence of edges and does not depend on which tree paths were chosen: alternative candidates in that cube with the same coordinates modulo $L$ coincide. Conversely reducing an infinite rooted connected tuple gives its unique periodic tuple with all incidences intact. The joint distributions agree, because they only use the same orientations of identically distributed independent edge chains. The coefficient of the covariance is therefore volume independent at these sides for **every** $H,M$. At $b=0$ the covariance is $\lambda^M>0$. Composition with the logarithm preserves the equality through order $r$.

## The two time limits

First fix $L,M$. The vacuum eigenvalue $\lambda_0(b)$ has a rank-one analytic spectral projection in the scalar sector near zero. Powers of $T_b/\lambda_0(b)$ converge there to that projection uniformly on a sufficiently small complex disk. This follows by a resolvent contour for the rest inside a circle of radius below one. The constant boundary vector has nonzero vacuum overlap at zero and retains it on a smaller disk. Thus the finite-interval means and correlations, expressed as quotients of matrix elements, converge locally uniformly as $H\to\infty$, together with their Taylor coefficients. Denote the stationary connected correlation by $C_{L,M}$. At real $b$ it is the vacuum matrix element with the vacuum projection removed between the two insertions. Its analytic continuation follows from the same projection formula with fixed boundary vectors.

Next write $\rho(b)=\lambda_1(b)/\lambda_0(b)$ for the analytic scalar plaquette ratio. In this sector the normalized residual spectrum is strictly inside $\lambda$ at zero. Shrink the fixed-box disk so a contour of radius $s<\inf|\rho|$ encloses the residual spectrum, excluding both selected eigenvalues. The spectral expansion then gives
$$
C_{L,M}(b)=d_L(b)\rho(b)^M+O_L(s^M)
$$
uniformly on the disk, where $d_L(0)=1$. The amplitude is analytic and stays away from zero on a smaller disk. Choosing logs from real $b=0$, $-M^{-1}\log C_{L,M}\to -\log\rho=m_L$ locally uniformly as analytic germs. Cauchy's formula gives convergence of each coefficient. Since the finite-$H,M$ coefficients of $\log C$ already agree across the specified boxes, they still agree after these two limits. Each pair of fixed boxes may use the smaller of its two analytic disks. No interchange with a spatial thermodynamic limit is required.

## Coefficient growth

Use the scalar sector again. Choose disjoint circles about $1$ and $\lambda$, bounded away from zero and the remaining electric spectrum by constants depending only on $g$. Since $\|A\|\le N$ and $\|K\|=1$, the exponential series gives $\|T_b-K\|\le e^{N|b|}-1$. For $|b|\le h_g/N$ with $h_g>0$ small enough, the resolvent Neumann series keeps one eigenvalue inside each circle, counted with multiplicity. Each analytic eigenvalue has a bounded log there with a bound depending only on the circles. This controls the analytic scalar germ even if ordering the full spectrum away from zero would require a smaller disk. Cauchy's coefficient estimate now gives $|[b^r]m_L|\le B_g(N/h_g)^r$. Evaluate it at the **single sufficient side** $L=2r+6$. Using $r^r\le e^r r!$ for $r\ge1$ gives the stated factorial bound after absorbing constants. A geometric bound in $r$ would require further information about the connected terms.

## Checks

Three native PCP OS guests ran in a host-relayed parent, child and grandchild sequence. The first compared spatial edge identifications across 24,576 labeled growth histories of four faces. It agreed with the covering lattice at side eight and found a wrap at side four. The second computed exact binary-Haar face cumulants. The six faces of a unit cube have joint cumulant one, while two copies of each of two opposite faces have joint cumulant zero despite product moment one. The third checked vacuum subtraction at 13 lags in a biased two-state chain with centered transfer eigenvalue $1/4$. Each guest exited zero with 47 register events. These finite controls exercise the support and subtraction steps. The Taylor coefficient equality and the spectral limits follow from the proof above. [Guest source](orders/worker.c) · [Expected output](orders/checks.txt) · [Replay driver](../../../observable-normalization/transfer-increments/replay-guests.py)
