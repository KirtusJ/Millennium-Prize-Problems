# Spatial sign reversal and the long-wavelength plaquette branch

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

At fixed temporal coupling $g>0$ and fixed even spatial side $L\ge6$, G4’s physical log gap is an even real-analytic function of the spatial coupling $b$ near zero. Its quadratic approximation consequently has remainder $O_{L,g}(b^4)$. The edge-sharing matrix that selects the upper transfer branch also gives its momentum dependence. At small axial lattice momentum $k$, the difference from the zero-momentum **quadratic log-gap coefficient** is $Jk^2/6+O_g(k^4)$, with $J>0$ as in the [coefficient calculation](README.md). These are derivatives at the electric regulator. [G4’s magnetic calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/0c1cc79/yang-mills/g4/full-attempt/magnetic.md)

## Sign reversal at fixed temporal coupling

Multiply each spatial link at $x$ in direction $i$ by the central sign $z_i(x)=(-I)^{\sum_{j<i}x_j}$. Even periods make these signs well defined on the torus. Their product is $-I$ around each spatial face, including wrapping faces. The same signs on every slice have product $+I$ around each temporal face. A change of variables relating the two signs of the Wilson coupling for SU(2) was studied by Li and Meurice. The slice transformation here reverses the spatial coupling with the temporal kinetic operator fixed. [Li and Meurice, *Lattice gluodynamics at negative* $g^2$](https://doi.org/10.1103/PhysRevD.71.016008)

Pullback by the signs is a Haar-unitary involution on gauge-invariant slice functions. It commutes with the independent-link convolution $K$ and sends the spatial trace sum $A$ to $-A$. Thus the scalar-stripped transfers $e^{bA/2}Ke^{bA/2}$ at opposite $b$ are unitarily equivalent, and their normalized spectra agree exactly. To pass from equality of the ordered spectra to a fourth-order remainder one needs regularity of the selected branch. The compact analytic family admits real-analytic eigenvalue branches at the isolated nonzero vacuum and plaquette eigenvalues by Rellich perturbation theory. The vacuum is simple. In the plaquette cluster the linear term vanishes, and the quadratic matrix is a scalar plus a strictly positive multiple of the adjacency matrix. Its graph is connected: within a plane a square can translate by in-plane steps, and across a transverse step it can reach the parallel square through an intervening perpendicular face. Perpendicular orientations also meet. Perron–Frobenius makes the largest quadratic coefficient simple. For sufficiently small $|b|>0$ that same analytic branch wins on both sides of zero since the first separation is proportional to $b^2$. The vacuum-normalized log gap is therefore analytic and even. [Greenbaum, Li and Overton on Rellich’s theorem for isolated eigenvalues](https://doi.org/10.1137/19M124784X)

## Momentum dependence of the quadratic coefficient

Label the three face types by unordered pairs $ij$. Use the actual face centers in the Fourier phases. For spatial momentum $\mathbf k\in(2\pi/L)\mathbb Z^3$, the adjacency matrix has symbol
$$
D_{ij,ij}=2\cos k_i+2\cos k_j,\qquad
D_{ij,ih}=4\cos(k_j/2)\cos(k_h/2)\quad (i,j,h\ \text{distinct}).
$$
The four coplanar neighbors give the diagonal. The centers of the four neighboring $ih$ faces are displaced by $(\pm e_j\pm e_h)/2$ with all four sign choices. The highest second-order transfer branch in a momentum sector has physical log-gap coefficient above the zero-momentum value by $J[12-\lambda_{\max}(D)]/8$.

For $\mathbf k=(k,0,0)$, take $k$ near zero and $c=\cos k$. In the subspace symmetric under exchange of the other two axes the matrix has diagonals $6+2c,4$ and off-diagonal $4\sqrt2\cos(k/2)$. The antisymmetric branch has eigenvalue $2c-2$. The upper eigenvalue is
$$
5+c+\sqrt{(1+c)^2+32\cos^2(k/2)}
=12-\tfrac43 k^2+O(k^4).
$$
At $k=2\pi/L$ the separation **of quadratic coefficients** is consequently of order $L^{-2}$. The finite-box branch argument gives no volume-uniform lower bound on this separation. Whether a different argument controls the remainder uniformly, or reaches isotropic weak coupling, remains open.

## Independent checks

I generated the face adjacency from the four oriented edge locations of every face, using common undirected edges to identify neighbors. I then summed the complex Fourier phases of those neighbors independently of the cosine formulas. Across all 216 momenta at side six and all 512 at side eight, the largest absolute entrywise discrepancies were below $9\times10^{-15}$. The axial adjacency differences $12-\lambda_{\max}$ at the first nonzero momentum were 1.3765246170 and 0.7949006705. The product of the four central signs was negative for every face in both enumerations. Three native PCP OS guests replayed the earlier shared-link, neighbor-count and Hamiltonian controls with 47 register events apiece. Those guests check the inputs to the quadratic coefficient. The sign symmetry and the analytic branch selection follow from the argument above. [Guest source and controls](README.md#checks)
