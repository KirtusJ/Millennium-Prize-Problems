# A complete colour sweep on a clear coarse field

Fix the isotropic four-dimensional SU(2) Wilson regulator at finite spatial size, a straight spatial skeleton $s$ on one slice and its conditional vacuum law. The same construction applies to the finite periodic time preparation. Let $x$ denote the free links on that slice and $y$ the off-slice environment on a slab containing its neighbours. Write $\mu_s(dx,dy)$ for their joint law and $\nu_s$ for the $x$ marginal. There are $k=24$ colours from the [Wilson heat baths](../full-complement/wilson.md). On the joint Hilbert space let $E_i$ be conditional expectation on the raw exterior of colour $i$, and let $U$ be isometric pullback from the slice. For a centered unit slice test write
$$J_s(f)=k^{-1}\sum_i\|(I-E_i)Uf\|^2,\quad
W_s=U^* E_k\cdots E_1 U,\quad H_s=W_s^*W_s.$$
One sweep first draws $y$ conditional on the incoming $x$, holds $y$ fixed while updating the full sequence of colours, and discards it on exit. The indicated product orders updates in the corresponding operator order. Its adjoint uses the reverse sequence. Every new sweep draws its environment conditional on its own incoming slice. Independent marginal environments would change the stationary law.

The sweep preserves $\nu_s$ and commutes with the stabilizer of $s$. It acts on functions invariant under that stabilizer, equivalently on the orbit space of the free links on this fibre. Haar averaging at skeleton-preserving vertices gives this quotient. Use that space for both the norm and the traces below. A bound for all its tests suffices for the gauge and center-neutral theory. If one uses all raw slice coordinates, the resulting upper bound on the norm remains conservative. The $y$ variables are auxiliary and never enter the test function.

Write $q_s$ for the singular norm of $W_s$ on centered tests in this space, and $\gamma_s=\inf J_s(f)$. At every fixed regulator,
$$
\frac{1-q_s}{k(1+q_s)}\ \le\ \gamma_s\
\le\ \frac{k+1}{2}(1-q_s^2).
$$
For the lower estimate, put $v_0=Uf$ and $v_i=E_i v_{i-1}$. Their squared step lengths sum to $1-\|v_k\|^2$. Put $u=\Re\langle v_0,v_k\rangle\le q_s$. The identity $v_{i-1}-v_i=(I-E_i)v_{i-1}$ and orthogonality give
$$(1-u)^2\le\Big(\sum_i\|(I-E_i)v_0\|^2\Big)(1-\|v_k\|^2)
\le kJ_s(f)(1-u^2).$$
When $q_s<1$ divide by $1-u$ and use monotonicity. For $q_s=1$ the lower bound follows from positivity. For the other direction $\|(I-E_i)v_0\|\le\sum_{j\le i}\|v_{j-1}-v_j\|$. Cauchy–Schwarz and summation bound $kJ_s(f)$ by $k(k+1)(1-\|v_k\|^2)/2$. Since $\|v_k\|\ge\|W_sf\|$, take a sequence approaching the singular norm. Both implications compare the same 24 local variances with a sweep on the entire slice. For general comparisons between random and systematic scans see [Gaitonde and Mossel](https://arxiv.org/abs/2410.11136).

**A bounded-kernel test.** Each block conditional has a bounded density relative to product Haar on its updated links, uniformly in all boundary values at this fixed finite regulator and finite $\beta$. This follows directly by bounding all incident Wilson face weights above and below. The product of these finitely many upper bounds dominates the law of a sweep by that of independent Haar redraws at each update, conditional on its starting point and environment. Every free spatial link is covered. Reading its last redraw gives a product-Haar final configuration in the reference process, including when colours overlap. The stationary slice density is bounded below relative to product Haar by the finite-regulator bound in the Wilson proof. Thus $W_s$ has bounded density relative to $\nu_s$. Passing to the invariant orbit quotient averages this kernel. The same reasoning works in the vacuum because the ground-state factors on the outer boundaries of the slab are unchanged during the scan. The constants from this argument alone deteriorate with volume.

For any integer $p\ge 2$, compute the cyclic integral of the stationary endpoint kernel of $H_s$ using [the marginal normalization](cycles.md), and let $M_s(p)=\operatorname{Tr}(H_s^p)-1$. Then
$$
q_s\le Q_s(p)=\min(1,M_s(p)^{1/(2p)}),\qquad
\gamma_s\ge\frac{1-Q_s(p)}{24[1+Q_s(p)]}.
$$
Indeed $H_s$ is positive, trace class and preserves constants. Each centered eigenvalue contributes its $p$th power. The bound decreases to $q_s$ on the norm side as $p$ grows. The environment is refreshed at the join between the forward and reverse sweeps. A raw return to a bin, a physical temporal correlator, or a trace with one frozen environment through every sweep would evaluate a different kernel.

For comparison with Z4's test, use a fixed continuous global gauge-invariant test with nonzero fibre variance at a strictly clear background. Its conditional Rayleigh quotient is continuous there by the compact slab formula. Every sufficiently small open neighbourhood lies inside the clear sector and has positive skeleton marginal mass by positivity of the Wilson density. Multiplying the centered test by the corresponding coarse-orbit gate gives the essential upper bound. [Fibre extension and full support](../sparse-coarse-fields/comparison.md) The cycle estimate supplies the opposite bound only when controlled uniformly over clear backgrounds. Establishing that uniform bound with a rate compatible with $\sum a_n/\gamma_n<\infty$ remains open. The [finite-state calculation](checks.py) exercises both inequalities for every test in a small model with a hidden, correlated environment.
