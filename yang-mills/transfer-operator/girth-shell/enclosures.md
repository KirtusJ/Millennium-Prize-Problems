# Finite-coupling enclosures for the actual Wilson spectrum

One can bound the whole finite-volume spectrum at a specified pair of couplings using only one spatial Gibbs measure. Take $0<\beta_t<\infty$, define $u=I_2(\beta_t)/I_1(\beta_t)<1$, and retain every orthonormal gauge-invariant spin network $\psi_a$ up to total electric degree $m$, including the constant. Write $k_a=\prod_e I_{d_e}(\beta_t)/I_1(\beta_t)$ and form the finite Hermitian matrix
$$
 B_{ab}=\sqrt{k_ak_b}\,\mu(\overline{\psi_a}\psi_b).
$$
Let $b_0\ge b_1\ge\dots$ be its eigenvalues, padded with zeros. If all omitted degrees are at least $m+h$, put $e_m=D u^{m+h}$, with $D$ as in the transfer estimate. For every index $j$ the actual positive transfer satisfies
$$
 \frac{b_j}{b_0+e_m}\le\frac{\lambda_j}{\lambda_0}\le
 \frac{b_j+e_m}{b_0}.
$$
Indeed $I_d^2>I_{d-1}I_{d+1}$ for positive argument, so successive ratios decrease and $I_d/I_1\le u^{d-1}$. Strict $u<1$ also follows from the positive one-link measure for which $u$ is the mean of the half-trace. The omitted electric operator is positive and bounded by $u^{m+h}I$. After inserting $M$ on both sides and dividing by $Z$ it costs at most $e_m$. The retained operator is the synthesis map with columns $\sqrt{k_a}w\psi_a$ times its adjoint, whose nonzero eigenvalues equal those of $B$. Ordered min–max bounds and $b_0\ge1$ prove the ratio bounds. At each fixed regulator $h=1$ suffices for convergence as $m\to\infty$. This yields arbitrarily tight enclosures in principle when the finite spatial moments are themselves enclosed. The number of required moments and $D$ can grow with volume. [Baricz and Ponnusamy, §1, Turán inequality](https://arxiv.org/pdf/1010.3346) · [Transfer conventions](transfer.md)

## A certified original SU(2) example

On one spatial cube at $\beta_s=1$ and $\beta_t=1/100$, the following disjoint intervals hold for $x_j=\lambda_j/(\lambda_0u^4)$. All inequalities are strict.

| Excitation indices | Lower bound | Upper bound |
|---|---:|---:|
| 1 | 0.8993 | 0.9040 |
| 2–6 | 0.8836 | 0.8883 |
| 7 and higher | 0 | 0.00456 |

The bounds include every color representation and every higher spin network of the full gauge-invariant transfer. The unscaled values are these numbers times $u^4$. The five indices share an enclosure; the calculation does not require their exact degeneracy at positive temporal coupling.

For the proof retain the constant and the six elementary loops. The cube is bipartite and has no electric degree five. The remainder is bounded by $D u^6$ with $D\le729$ and $u\le1/400$. By permutation symmetry of the **static** one-cube measure on the six characters, the retained Gram matrix on the five transverse directions is $u^4c_T I$, where $c_T$ is the transverse covariance eigenvalue. On the scalar and constant it is
$$
 \begin{pmatrix}1&\sqrt6 u^2 m_1\\ \sqrt6 u^2 m_1&u^4(c_S+6m_1^2)\end{pmatrix},
 \qquad m_1=\mu\chi_p .
$$
Its determinant is $u^4 c_S$; its top eigenvalue $b_0$ lies in $[1,1+24u^4]$ by the trace bound $\mu|\sum\chi_f/\sqrt6|^2\le24$. Its smaller eigenvalue is therefore $u^4c_S/b_0$. The character integral orders this above the transverse levels at these couplings. The bounds in the table follow by padding the rest of the Gram spectrum with zero and applying the general inequalities.

The [rational verifier](cube_bounds.py) encloses $Z$, $Z_p$, $Z_{pp}$ and $Z_{pq}$ for distinct $p,q$ by summing $d\le7$ and power-series index $k\le8$. With $a_d=2I_d(b)/b$, the coefficient of $b^{d+2k-1}$ is $1/[2^{d+2k-1}k!(d+k)!]$. At $b=1$ the tail of any of its first two derivatives, including order zero, is at most $4/[(k_0+1)!(d+k_0+1)!]$ after index $k_0$. Indeed the falling power from differentiating is at most $2\cdot2^{d+2k-1}$ and the tail decreases at least geometrically. Also $a_d^{(j)}(1)\le j!a_d(2)<j!3/d!$ for $j\le2$ by positivity. After dimension cutoff $d_0$, each of the four partition derivatives has remaining sum at most $4\cdot3^6(d_0+1)^2/[(d_0+1)!]^6$ by the same geometric tail comparison. Finally
$$
 c_T=4(Z_{pp}-Z_{pq})/Z,\qquad
 c_S=4[(Z_{pp}+5Z_{pq})/Z-6(Z_p/Z)^2].
$$
All arithmetic from the truncated sums to the stated endpoints is rational. The only numerical diagonalizations elsewhere in this directory serve as controls. [Exact character gluing](cube.md)
