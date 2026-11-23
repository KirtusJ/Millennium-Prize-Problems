# How much of the first scalar state does the ordinary plaquette measure?

For the original symmetric $SU(2)$ Wilson transfer, sum the fundamental plaquette over the spatial slice, subtract its exact vacuum expectation, and normalize the resulting vector. On a periodic cubic torus of side $L\ge5$, its first loss of spectral weight away from the **true lowest excitation** is computable. At second order in the spatial coupling only three types of intermediate states contribute. Widely separated two-plaquette excitations cancel exactly at this order. The coefficients below are independent of $L$. Error bounds are at fixed $L$, and for an effective-mass reading also at fixed time separation.

## Wilson time step

Keep the [first-band notation](../band.md), including $r=u^4$, $c=(1+r)/(1-r)$, $f(k)=(r+k)/(r-k)$, and $D=12$. Put $W=\frac12\sum_p\chi_p$ and use the physical transfer $T_\sigma=e^{\sigma W/2}Ke^{\sigma W/2}$, dropping its scalar action constant. Let $\Omega_\sigma$ be its normalized vacuum, and set

$$
 v_\sigma=\frac{(W-\langle W\rangle_\sigma)\Omega_\sigma}
                  {\|(W-\langle W\rangle_\sigma)\Omega_\sigma\|}.
$$

Writing $P_{\rm first}(\sigma)$ for the projection on the lowest excitation at small positive $\sigma$, the result is

$$
 1-\|P_{\rm first}(\sigma)v_\sigma\|^2
    =\sigma^2\sum_{j=1}^3 w_j+O_{L,\gamma}(|\sigma|^3),\qquad
 w_j=m_j\left(\frac{c-f(k_j)}2\right)^2 .
$$

| State created by the second plaquette | Electric eigenvalue $k_j$ | Squared norm factor $m_j$ |
|---|---:|---:|
| Adjoint on the same square | $v^4$ | $1/4$ |
| Two squares sharing one edge, spin zero there | $u^6$ | $D/8$ |
| Two squares sharing one edge, spin one there | $u^6v$ | $3D/8$ |

Here $v=I_3(\gamma)/I_1(\gamma)$ in the table. To derive it, take $\Phi=d^{-1/2}\sum_p\chi_p$, where $d=3L^3$ and $W1=\sqrt d\,\Phi/2$. The plaquette adjacency graph is connected. One can move from one square to its translate using parallel adjacent squares or a perpendicular square across a common edge, and rotate between orientations by an edge. The uniform eigenvector of the largest adjacency eigenvalue is therefore simple. The positive hopping coefficient in the [band calculation](../band.md) selects its continuation as the actual first excitation for all sufficiently small positive $\sigma$ at fixed box. Under spatial translations and cubic rotations the first electric band contains only one invariant direction. Restricting to this symmetry space makes its eigenvalue simple already at zero, so the branch and the total-plaquette vector are analytic there.

For a normalized isolated eigenvector of $K$ with eigenvalue $s$, the component of its derivative at a different eigenvalue $k$ is its $W$ matrix element times $(s+k)/(2(s-k))$. This follows by differentiating the eigenvalue equation with $T'_0=(WK+KW)/2$. The vacuum therefore moves by $(c/2)W1$. At a higher electric eigenvalue $k$, the normalized centered probe derivative is $(c/2)P_k W\Phi$, whereas the first eigenvector derivative is $(f(k)/2)P_k W\Phi$. Vacuum centering removes the ground component from the spectral leakage; normalization only changes the component parallel to $\Phi$ to this order. More precisely, the probe and first eigenvector derivatives have the same vacuum component by differentiation of their separate orthogonality to $\Omega_\sigma$. Their complementary difference is precisely the term in the squared-norm formula.

In $W\Phi$ the squared-face terms have coefficient $1/(2\sqrt d)$ and the unordered distinct pairs have coefficient $1/\sqrt d$. Distinct unordered pairs are orthogonal by edge-center parity. For the squared faces their adjoint parts are mutually orthogonal. The $dD/2$ neighboring pairs each split in weights $1/4,3/4$ by shared-link Haar integration. This gives the table. Every distinct pair with no common edge has eigenvalue $r^2$, and $f(r^2)=c$. Its potentially volume-growing contribution is exactly zero. These orthogonal decompositions also cover degeneracies with higher spin networks.

The bias in a directly measured effective mass follows. Let $C_\sigma(n)=\langle v_\sigma,(T_\sigma/\lambda_0)^n v_\sigma\rangle$ and $x_j=k_j/r$. At each fixed integer lag $n\ge0$,

$$
 \log\frac{C_\sigma(n)}{C_\sigma(n+1)}-\Delta_{\sigma,L}
   =\sigma^2\sum_j w_j(1-x_j)x_j^n+O_{L,\gamma,n}(|\sigma|^3).
$$

Indeed, after dividing $C_\sigma(n)$ by the first transfer ratio to power $n$, the residual vector contributes $\sigma^2\sum_j w_j x_j^n$, and normalization subtracts $\sigma^2\sum_j w_j$. Perturbing an $n$-step bounded transfer on an $O(\sigma)$ residual changes its quadratic form only at third order for fixed $n$. Subtract the two logarithms. Each leading bias is nonnegative and its three rates are explicit. The argument uses an ordinary spatial-slice insertion, so no temporal flow crosses a reflection plane.

## Direct continuous-time calculation

Keep spatial spacing fixed and use the program's Hamiltonian with $\gamma=\kappa/a$, $\sigma=a\lambda$, and $z=\kappa\lambda$. After dropping the action constant, in units $1/\kappa$ the generator is $\kappa H=H_0-zW$. A link of twice-spin $m$ contributes $m(m+2)/2$ to $H_0$. At finite box the bounded perturbation permits a direct spectral calculation. It avoids any exchange of the limits in $a$ and $\lambda$. [Hamiltonian normalization and time-cutoff result](../../../transfer-operator/hamiltonian-time/)

The vacuum, first band, doubled disjoint pair, same-face adjoint, and two shared-edge channels now have dimensionless electric energies $0,6,12,16,9,13$, respectively. For the first band, second-order perturbation of $H_0-zW$ uses the diagonal intermediate factors $2/(6-E_j)$. The vacuum factor on its only intermediate band is $-2/6$. Equivalently, for minus the excitation's energy curvature, the factors corresponding to $c,h,g$ in the Wilson computation are $1/3,1/5,8/21$, since $2/(9-6)$ and $2/(13-6)$ occur with weights $1/4,3/4$. The same adjacency and vacuum subtraction give

$$
 \kappa\Delta_H=6-\frac{71}{840}z^2+O_L(|z|^3).
$$

For the lowest spatial momentum branch the coefficient of $z^2$ in $\kappa[E(k)-E(0)]$ is $|k|^2/126+O(|k|^4)$ with lattice momentum $k$. This is a fixed-spatial-regulator dispersion. An independent physical length scale is still needed to compare spatial and temporal units.

For the centered total plaquette the vacuum derivative is $W1/6$. The first eigenvector derivative at energy $E_j>6$ is $P_j W\Phi/(E_j-6)$. A disjoint pair again has exactly zero difference. The full first-state loss for small positive $z$ is

$$
 z^2\left[\tfrac14(1/6-1/10)^2+
           \tfrac{12}{8}(1/6-1/3)^2+
           \tfrac{36}{8}(1/6-1/7)^2\right]+O_L(|z|^3)
 =\frac{1999}{44100}z^2+O_L(|z|^3).
$$

The Wilson leakage coefficient divided by $\gamma^2$ tends to the same number as $\gamma\to\infty$. At fixed time step both the Wilson leakage and the effective-mass bias can be checked independently by inserting the magnetic operator into the full two-square transfer eigensystem. [Replay and direct measurements](execution.md)
