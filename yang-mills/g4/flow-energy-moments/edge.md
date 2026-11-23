# Recovering the lowest energy seen by the observable

For the centered spatial plaquette let $m_k=\int E^k\,d\nu(E)$, with $m_0=\nu([0,\infty))$. These are energy moments. Integer-lag transfer correlations instead give moments of $\lambda=e^{-E}$. Here $t$ is the continuously interpolated Euclidean **lag** in $C(t)=\int e^{-tE}\,d\nu$, using the spectral interpolation of the one-step transfer. The spatial flow time stays fixed throughout.

## Determinacy and thermodynamic limits

Write $y=E/\log(e+E)$. It increases from zero to infinity. The tail established above implies $\int e^{b y}\,d\nu\le1+Ab/(c-b)$ for $0<b<c$ by layer-cake integration. For $E\ge1$, $E\le C y\log(e+y)$ since the ratio tends to one at infinity and is continuous. At $y\le k$ this gives $E\le Ck\log(e+k)$ for integers $k\ge1$, increasing $C$ for $E<1$. At $y=kz$ with $z\ge1$, concavity gives $\log(e+kz)\le z\log(e+k)$, hence
$$
E^k e^{-by}\le[Ck\log(e+k)]^k(z^2e^{-bz})^k .
$$
The final factor has a bounded $k$th root. Integration yields $m_k^{1/k}\le C'k\log(e+k)$ uniformly in the stated volumes and parameters. The Carleman sum $\sum_{n\ge1} m_{2n}^{-1/(2n)}$ diverges by comparison with $\sum 1/[n\log(e+n)]$. If a positive even moment vanishes, the measure is already supported at zero. Thus the energy measure is Hamburger determinate. In particular the right derivatives $C^{(k)}(0+)=(-1)^k m_k$ determine it uniquely. Differentiation follows from the moment bounds by dominated convergence. This determination uses the entire derivative sequence. [Schmüdgen, Theorem 2.2](https://arxiv.org/pdf/2008.12698) · [Tail estimate](time-jets.md)

Along a weak transfer-measure limit the same bounds hold and there is no atom at $\lambda=0$. Truncate $(-\log\lambda)^k$ by a continuous cutoff on $[0,1]$ and use uniform integrability, for example from the next higher moment. This proves convergence of every fixed energy moment, also for the limiting spatially flowed reading when the finite-lag correlations converge. The lowest support point need not converge with these moments. For example $(1-1/j)\delta_1+j^{-1}\delta_{1/j}$ tends to $\delta_1$ while its spectral bottom tends to zero.

## Shifted moment matrices

For nonzero $\nu$ and $n\ge0$ form two matrices with $0\le i,j\le n$,
$$
G_n=(m_{i+j}),\qquad H_n=(m_{i+j+1}).
$$
Over vectors with $v^\mathsf{T}G_n v>0$, put $r_n=\inf (v^\mathsf{T}H_n v)/(v^\mathsf{T}G_n v)$. These are the Rayleigh quotients of the polynomials $p(E)=\sum_{i=0}^n v_iE^i$ in $L^2(\nu)$. This definition works with singular Gram matrices. The sequence decreases to $E_*=\inf\operatorname{supp}\nu$, and for any $\Delta$
$$
E_*\ge\Delta\quad\Longleftrightarrow\quad H_n-\Delta G_n\succeq0 \quad\text{for every }n\ge0.
$$

To see density of the tests, let a real $g\in L^2((1+E)d\nu)$ be orthogonal to all polynomials. The signed measure $g(1+E)d\nu$ is finite and its positive and negative parts have identical moments. By Cauchy–Schwarz their moments of order $2n$ are bounded by $\|g\|\sqrt{m_{4n}+m_{4n+1}}$. Their $2n$th roots are $O_g(n\log(e+n))$ using the growth bound above and boundedness of $(n\log(e+n))^{1/(4n)}$. Carleman's criterion gives equality of the parts, so $g=0$. Thus polynomials are dense in the weighted space. For each $\epsilon>0$, approximate the positive-mass indicator of $[E_*,E_*+\epsilon]$ in this weighted norm. The approximation converges in both the ordinary norm and the quadratic energy form by Cauchy–Schwarz. Its Rayleigh quotient tends to a value at most $E_*+\epsilon$. Every nonzero quotient is at least $E_*$. This proves both conclusions. The finite matrices give upper bounds on the lowest visible energy. [Lean sign and indicator estimates](EnergyMoments.lean) · [Finite-order ambiguity](finite-moments.md)

For the **bare** channel there is a quantitative first bound requiring no measured moments. The inverse-transfer budget gives $\int e^E\,d\nu\le B_\beta=4 k_{\min}^{-4}A_1^8$. Conditioning on one link gives $m_0\ge\rho_\beta=3/[2(4+6\beta)^2]$. Jensen applied to $\nu/m_0$ yields
$$
E_*\le r_0=m_1/m_0\le\log(B_\beta/\rho_\beta).
$$
At $\beta=1$, $B_\beta<2^{34}$ and $\rho_\beta=3/200$, giving $E_*<28$ in lattice units in every stated volume and thermodynamic limit. The rational control bounds $e^{28}$ from below by its first 49 positive terms. [One-link and inverse bounds](../transfer-inverse-moment/beta-one.md) · [Exact check](control.py)

A lower bound for this single channel permits other channels to carry lower energies. For a self-adjoint Hamiltonian one can pass a lower quadratic-form bound to the full excitation space if it holds on a form core there. Equivalently one may exclude the unwanted spectral projection on a total set of excitation vectors. The needed uniform physical inequality and nontrivial limiting state have yet to be established. [Clay problem and physical Hamiltonian](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
