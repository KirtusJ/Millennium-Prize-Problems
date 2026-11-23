# The first center-even excitation of the one-site SU(2) Wilson cylinder

Director A4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Disposition on Z4’s M1, submitted for independent review.** Fix one spatial site and $k=2$ or $3$ spatial directions with the isotropic Wilson transfer and normalization of [Z4’s question](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/627b3e45833abc14e9a889c4f0c40cac43bd84a0/yang-mills/z4/attempt/reviews/g1-toron/TORON_GAP.md). Restrict to gauge-invariant functions even under each link’s independent center flip. Write $\lambda_0\ge\lambda_1\ge\cdots$ for the transfer eigenvalues in this sector, counted with multiplicity. With $h=\beta^{-1/3}$, for each fixed index $j$,
$$
\frac{1-\lambda_j}{h}\longrightarrow e_j,\qquad
\frac{\log(\lambda_0/\lambda_1)}{h}\longrightarrow e_1-e_0>0 .
$$
Here $e_j$ are the ordered eigenvalues on the simultaneous-rotation-invariant subspace of $L^2((\mathbb R^3)^k)$ of
$$
H=-\tfrac12\sum_i\Delta_i+2\sum_{i<j}|x_i\times x_j|^2 .
$$
The proof gives separation via simplicity and compactness, without a numerical value for $e_1-e_0$. Its volume is fixed at one spatial site, and the center-odd sectors are outside its scope. Controlling the gap on a refining spatial lattice at an independently fixed physical scale remains open. Small-volume $g^{2/3}$ energy expansions in Yang–Mills theory on a spatial torus have a classical precedent in Lüscher’s work. Here the kinetic operator is the discrete-time Wilson convolution of the one-site regulator. [Lüscher, 1983](https://doi.org/10.1016/0550-3213(83)90436-4)

## 1. Confinement away from the centers

Use the product kinetic convolution $K=\prod K_i$ on unit quaternions, the potential $V=2\beta\sum_{i<j}|\mathbf u_i\times\mathbf u_j|^2$, and $T=e^{-V/2}K e^{-V/2}$. Bold letters denote the imaginary three-vector. Simultaneous gauge averaging acts as identity on the sector in the theorem. The scalar factors $K_i$ are positive commuting contractions. The center-even space can equivalently be treated on the product of $S^3/\{\pm1\}$ with its probability Haar measure.

Fix $i$ and choose $j\ne i$. Freeze all variables except $U_j$ and let $r=|\mathbf u_i|\ge h$. The pair potential in this fiber is $V_{ij}=2\beta r^2\rho^2$, where $\rho$ is the perpendicular imaginary component’s length relative to the axis of $U_i$. We claim, **uniformly in the frozen variables**, the fiber form inequality
$$ I-K_j+V_{ij}\ \ge\ c r I. \tag{1}$$
Use a block of $m=\lceil8/r\rceil$ steps and set $d=(m/\beta)^{1/2}$. Now $8\le m\le9/h$ and $d\to0$ uniformly. At every integer $m/2\le t<m$ the one-link walk from an arbitrary start has density at most $Cd^{-3}$ and expected squared chord displacement at most $8d^2$. The proof of the [M0 smoothing estimate](../README.md) bounds the density by $C[1+(\beta/t)^{3/2}]$ for every $1\le t\le\beta$; it therefore applies at these varying block lengths. The same tube argument bounds $\Pr(\rho<\epsilon d)$ by $8/R^2+CR\epsilon^2$ with absolute constants. Fix $R$, then $\epsilon$ so this is at most one half. On the complementary event $m V_{ij}\ge 2\epsilon^2(mr)^2\ge128\epsilon^2$. Counting late visits as in M0 gives $B^m1\le1-\kappa$ for $B=(1+V_{ij})^{-1}K_j$ with $\kappa>0$ independent of the fiber, $\beta$ and $m$. The finite sum $\sum_{a<m} B^a1$ gives $I-K_j+V_{ij}\ge\kappa/m$ by the symmetric-kernel ground-state identity. Since $m\le9/r$, this proves (1).

For $r<h$ use positivity. On the whole product $I-K\ge I-K_j$ and $V\ge V_{ij}$. Consequently
$$ c\int |\mathbf u_i|\,|g|^2\le\langle g,(I-K+V)g\rangle+ch\|g\|^2. \tag{2}$$
This step uses the exact product walk, so it also holds on slices of a gauge-invariant function that individually break that symmetry.

## 2. Compactness of scaled low-energy states

For any unit vector $F$ of scaled energy $\langle F,(I-T)F\rangle/h\le C$, put $g=e^{-V/2}F$. The numerator is exactly $\langle g,(I-K)g\rangle+\langle g,(e^V-1)g\rangle$. Both terms are nonnegative. Also $\|F-g\|^2\le\|F\|^2-\|g\|^2\le Ch$. From (2) each $\int |\mathbf u_i||g|^2=O(h)$. In center-identified exponential coordinates let $\theta_i\in[0,\pi/2]$ be the distance to the nearer center. Since $\sin\theta_i\ge2\theta_i/\pi$, the mass of $g$ outside $\max_i\theta_i\le Rh$ is at most $C'/R$. This controls escape along the commuting valley on the rescaled space.

Let $D$ be the product round-sphere positive Laplacian. Its eigenvalue in a representation block with dimensions $n_i$ is $D_{\bf n}=\sum_i(n_i^2-1)$. On that block we have, with a uniform $c'>0$,
$$1-K\ge c'\min(D_{\bf n}/\beta,1).\tag{3}$$
For one factor with $n\ge8$, the M0 recurrence gives $I_n/I_1\le (1+n/\beta)^{-n/8}$. For $n\le\beta$ this is at most $e^{-n^2/(16\beta)}$; for $n>\beta$ it is at most $2^{-n/8}$. For the finitely many $2\le n<8$, the fixed-order expansion gives $I_n/I_1=1-(n^2-1)/(2\beta)+O(\beta^{-2})$. Dimension one has no kinetic cost. Use the factor with the largest Casimir and $k\le3$ to obtain (3). [Bessel expansion](https://dlmf.nist.gov/10.40)

Project $g$ onto $D\le\beta$, calling the result $g_<$. By (3), $\|g-g_<\|^2=O(h)$ and $\|\nabla g_<\|^2=O(\beta h)=O(h^{-2})$. For precision identify all center-even Hilbert spaces with subspaces of the same Euclidean $L^2$ space. Take the positive-real-part representative and write $U_i=\exp(h x_i)$, $|hx_i|<\pi/2$; the cut has zero Haar measure. Multiply by the square root of the full rescaled Haar density and extend by zero off the chart. This is an isometry $J_h$. On each fixed $x$-ball the metric tends after rescaling to the Euclidean metric. The density is a constant times $h^{3k}\prod_i\operatorname{sinc}^2(h|x_i|)$, where $\operatorname{sinc}t=\sin t/t$. Thus $J_hg_<$ is locally bounded in $H^1$; the scaled gradient cost is $O(h^2\beta h)=O(1)$. Compactness on bounded balls and (2) imply that $J_hF$ has a strongly convergent $L^2$ subsequence as $h\downarrow0$. No global Sobolev bound on the zero extension at the chart boundary is required.

Any such limit belongs to the form domain of $H$. On fixed balls the scaled metric and the logarithmic derivatives of the density converge smoothly to their flat values. Weak lower semicontinuity on these balls followed by increasing radii bounds the full limiting gradient by the scaled kinetic cutoff estimate. Similarly $(e^V-1)/h\to 2\sum|x_i\times x_j|^2$ uniformly on compact sets and $J_hg$ has the same strong limit. Taking the increasing-ball limit of the nonnegative integrals bounds its potential energy. Invariance under simultaneous rotation passes through the isometry.

## 3. Testing the discrete transfer on compact functions

For each smooth compactly supported gauge-invariant $\psi$ in Euclidean coordinates lift it by the inverse density isometry, $\psi_h=J_h^*\psi$. For small $h$ this is a smooth center-even function away from all cuts, vanishing in their neighborhoods. Then
$$
J_h(I-T)\psi_h/h\longrightarrow H\psi\quad\text{in }L^2. \tag{4}
$$
Indeed $(I-T)=(1-e^{-V})+e^{-V/2}(I-K)e^{-V/2}$. On the compact support $V/h$ and its fixed-order derivatives converge to the quartic polynomial by $\mathbf u_i=\sin(h|x_i|)x_i/|x_i|$. The first term yields the potential. For the second, put $w_h=e^{-V/2}\psi_h$. Its invariant derivatives of orders $s\le3$ have global $L^2$ norm $O_\psi(h^{-s})$ by the chart formula. Their scaled coordinate expressions, including the density, converge locally to the corresponding flat derivatives.

For one Wilson increment let $\xi=\theta\hat n$ be its principal Lie algebra vector. The radial law is proportional to $\sin^2\theta\exp[-\beta(1-\cos\theta)]d\theta$. Scaling by $\sqrt\beta$ gives $\beta\mathbb E\xi_a\xi_b\to\delta_{ab}$ and $\mathbb E|\xi|^3=O(\beta^{-3/2})$ by Gaussian domination on $[0,\pi]$ and radial symmetry. Odd first moments vanish. The product walk uses independent increments. Taylor-expand right translations on the product group along the one-parameter path determined by those vectors. Haar invariance bounds the integrated third-order remainder in $L^2$ by $C\beta^{-3/2}h^{-3}=O(h^{3/2})$. The quadratic term in $I-K$ is $\mathbb E[\xi_1^2]D w_h/2$, where the subscript denotes one Cartesian component. Since $\beta h^3=1$, the scaled kinetic operator gives $-\Delta\psi/2$ in the common coordinates. The left half-weight tends to one on the support of the quadratic term and is a contraction on the global remainder. This proves (4) with its normalization.

## 4. Closing the spectral argument

The Euclidean form with nonnegative polynomial potential is closed on $H^1\cap L^2(V_{\rm flat}\,dx)$ (the latter condition means finite potential energy). Smooth compact functions are a form core by cutoff and mollification; averaging over the compact rotation group gives an invariant core. Its resolvent is compact: at fixed $x_i$ one pair term and the two transverse components of $-\Delta_j/2$ form a two-dimensional oscillator of frequency $2|x_i|$, bounded below by $2|x_i|$. All discarded terms are positive. This gives the same $L^2$ tail criterion as (2), while the Euclidean form directly bounds the gradients. The ground state is simple and strictly positive on the full space by positivity improvement of the Schrödinger semigroup (the Brownian bridge kernel has positive weight for a finite continuous nonnegative potential). It is rotation invariant by simplicity, so the invariant restriction still has $e_1>e_0$.

Min–max on arbitrarily accurate finite-dimensional smooth trial spaces using (4) gives $\limsup (1-\lambda_j)/h\le e_j$. For the reverse inequality choose the lowest $j+1$ orthonormal eigenvectors of $(1-T)/h$ on a subsequence realizing its $j$th liminf. Their energies are bounded by the upper estimate. Section 2 gives $j+1$ simultaneous strong limits, still orthonormal. Test their eigenvalue equations against (4), passing to a further subsequence on which each eigenvalue converges. Each limit is a form-domain weak eigenfunction of $H$ at the corresponding limiting eigenvalue: integration by parts on compact tests and the form core extend the identity to the full invariant form domain. The Euclidean min–max principle therefore gives $e_j\le\liminf(1-\lambda_j)/h$. Finally $-\log\lambda_j=(1-\lambda_j)+O(h^2)$ at each fixed index. Subtract the two convergent absolute energies to obtain the positive limiting gap coefficient.

The localization and kinetic compactness arguments do not supply constants uniform in the number of spatial sites. This spectral limit addresses the center-even one-site question only. [Native checks and generator quadrature](checks.md)
