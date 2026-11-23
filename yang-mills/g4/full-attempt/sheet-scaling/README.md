# Taking time and area limits in the first Wilson sheet

Director G4, November 23, 2026. For a planar rectangle $R$ of $m$ tiles in the four-dimensional anisotropic $SU(2)$ Wilson regulator, the first nonzero magnetic coefficient of the normalized vacuum loop is $4^{-m}Z_R(q)$. Here $q=I_2(g)/I_1(g)$ is the fundamental electric eigenvalue at temporal coupling $g$. The spatial torus is even and can be chosen at least four times the longer side of $R$, so the minimal sheet is unique. At each finite size the coefficient is extracted at $b=0$. The preceding proof applies to the rectangle by the same planar projection and Haar disk contraction. The estimates below show that **the large-square and continuous-time limits commute for the logarithm of this coefficient per tile**, in Hamiltonian magnetic units. A one-tile-wide strip gives an exact growth constant and a lower bound for squares. [Vacuum-sheet proof](../all-readings/area.md) · [Wilson’s surface expansion](https://doi.org/10.1103/PhysRevD.10.2445)

### An error bound uniform in the shape per tile

Write $\epsilon=-\log q$. For real tile heights $x$, let $E_R(x)$ sum $|x_i-x_j|$ over all internal nearest-neighbor edges and $|x_i|$ over every edge to the fixed exterior height zero. Put
$$
 Z_R(e^{-\epsilon})=\sum_{t\in\mathbb Z^m}e^{-\epsilon E_R(t)},\qquad
 C_R=\int_{\mathbb R^m}e^{-E_R(x)}\,dx .
$$
For every nonempty finite planar tile set,
$$
 \left|\frac{1}{m}\log\frac{\epsilon^m Z_R(e^{-\epsilon})}{C_R}\right|
 \le 2\epsilon . \tag{1}
$$
Indeed partition $\mathbb R^m$ into half-open cubes of side $\epsilon$ centered at the heights $\epsilon t$. Each coordinate rounding error has magnitude at most $\epsilon/2$. The error on an internal edge is at most the sum of the two endpoint errors. On a boundary edge only the interior endpoint contributes. Each tile appears four times in this count. Thus $|E_R(x)-E_R(\epsilon t)|\le 2m\epsilon$, including on tiles next to corners and holes. Integrate the two exponential bounds cell by cell. Finiteness follows by retaining a forest connected to the fixed exterior and integrating or summing its successive height increments. Equation (1) compares normalized coefficients even for areas growing arbitrarily fast with time refinement. [Zero-boundary height Hamiltonian, eq. (1.1)](https://arxiv.org/pdf/2301.09197#page=1)

For square sides $N$, write $p_c=\lim_N N^{-2}\log C_{N\times N}$ and $p_d(\epsilon)=\lim_N N^{-2}\log Z_{N\times N}(e^{-\epsilon})$. Both exist. Joining two patches removes two boundary terms $|x|+|y|$ and introduces $|x-y|$, increasing both partition functions relative to their product. Tile a large square by fixed squares and singletons in the leftover rows and columns. Their fraction tends to zero and each singleton has real integral $1/2$ or integer sum $(1+q^4)/(1-q^4)$. This proves that the limiting inferior dominates the supremum over fixed squares, with a finite upper bound from a rooted forest. It also avoids fixing leftover continuous heights on a null set. Consequently
$$
 \big|p_d(\epsilon)+\log\epsilon-p_c\big|\le 2\epsilon .
$$
Along any $N\to\infty$, $a_t\downarrow0$, put $g=\kappa/a_t$, $b=a_t j$ and $\epsilon=-\log[I_2(g)/I_1(g)]$. The leading coefficient in $j$ is $(a_t/4)^m Z_R(e^{-\epsilon})$. Since $a_t/\epsilon\to2\kappa/3$, its normalized logarithm on the square tends to $\log(\kappa/6)+p_c$ in either order and along every joint sequence. At each size the coefficient is computed before either limit. The magnetic Taylor remainder in the underlying vacuum expectation can still depend on area, box and coupling. [Bessel asymptotics](https://dlmf.nist.gov/10.40) · [Hamiltonian convention](https://doi.org/10.1103/PhysRevD.11.395)

The Hamiltonian coefficient can also be obtained directly at fixed box, without a discretization limit. On the gauge-invariant product-link space the electric Hamiltonian is $(2/\kappa)\sum_e C_2(e)$ with constant vacuum, compact resolvent and a positive gap. Its magnetic perturbation is the bounded multiplication operator $-j\sum_p\mathrm{Tr}(U_p)/2$. The unit-time semigroup is compact and analytic near $j=0$ by its norm-convergent Duhamel series. Its simple leading projection gives locally uniform convergence of the constant-endpoint window ratios, as in the discrete proof. The time-ordered integrals for a loop at zero obey the same link-history center selection. At order $m$ the unique spatial sheet gives each tile once, and summing the orders gives one copy of the whole time cube. A fundamental on one link propagates by $\exp[-3|t|/(2\kappa)]$. The gauge-invariant insertions, the constant endpoints and the commuting electric projection therefore give the same disk factor $4^{-m}$ times the integral of $\exp[-3E_R(t)/(2\kappa)]$. Rescaling all $m$ times recovers $(\kappa/6)^m C_R$ for the actual stationary Hamiltonian vacuum. [Fixed-volume disk contractions and vacuum argument](../all-readings/area.md) · [Hamiltonian normalization](https://doi.org/10.1103/PhysRevD.11.395)

### Quantitative bounds for squares

Split $E_R=E_{\rm h}+E_{\rm v}$ into horizontal and vertical edges, including the corresponding exterior edges. Cauchy–Schwarz bounds $C_R$ by the geometric mean of the integrals with energies $2E_{\rm h}$ and $2E_{\rm v}$. The first factors over all horizontal runs. A run of $k$ tiles has integral $f^{*(k+1)}(0)$ for $f(x)=e^{-2|x|}$. Since $\|f\|_1=\|f\|_\infty=1$, that integral is at most one. The same reasoning applies in the other direction. Hence $C_R\le1$ for every tile set. For integer heights the same proof gives $Z_R(q)\le[(1+q^2)/(1-q^2)]^m$. Both bounds include the outer edges at the two ends of every run.

The [unit-width strip](strip.md) has continuous growth rate $\lambda_*=2/(j'_{1,1})^2=0.58997\ldots$, where $j'_{1,1}$ is the first positive zero of $J_1'$. Joining $N$ strips of length $N$ into a square gives $C_{N\times N}\ge C_{1\times N}^N$. Thus
$$
 \log\lambda_*\le p_c\le0,\qquad
 \frac{\kappa}{3(j'_{1,1})^2}\ \le\
 \lim_{N\to\infty}\big([j^{N^2}]\pi_j^H W_{N\times N}\big)^{1/N^2}
 \ \le\ \frac{\kappa}{6}.
$$
Here $[j^m]\pi_j^H W$ denotes the coefficient in the finite-box Hamiltonian vacuum expectation. The strip and square results concern the indicated derivatives. A finite-$j$ area law or a positive relativistic mass gap would also require control of higher contributions and the spatial continuum construction. [Controls and formal scope](checks.md) · [Jaffe–Witten problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
