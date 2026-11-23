# The total variation profile of the electric Wilson transfer

Fix $g>0$, take even spatial sides $L\to\infty$, $V=L^3$, and choose integer lags $n$ with $Vq^{8n}\to\theta\in[0,\infty)$. On gauge-orbit slice pairs let $D=dP_n/dQ$, where $Q$ has independent Haar slices. With $\Phi$ the standard normal distribution function, the limiting profile is
$$
 \|P_n-Q\|_{\rm TV}\longrightarrow 2\Phi(\sqrt{3\theta}/2)-1.
$$
For $Vq^{8n}\to\infty$ the limit is one by the plaquette test. The formula describes subsequences at the discrete time steps. Everything below concerns the electric $SU(2)$ regulator at fixed temporal coupling. [Definitions, spectral expansion and chi-square profile](electric.md)

### Projecting the two-slice likelihood

Write $t=q^{4n}$, $N=3V$ and $X_p=\mathrm{Tr}(U_p)\mathrm{Tr}(W_p)$ under the two independent Haar slices $U,W$. Call two distinct faces incompatible if they share a vertex. Let
$$
 Z(t)=\sum_{F\ \mathrm{pairwise\ compatible}}t^{|F|}\prod_{p\in F}X_p .
$$
For every such $F$, the product of the single-slice square characters has Haar norm one and is a physical transfer eigenfunction. Different $F$ give different labeled supports, because the connected components of each support are its squares. The corresponding functions are orthogonal. Their two-slice products are orthonormal in $L^2(Q)$, and their scalar products with $D$ are $t^{|F|}$ by stationarity and the kinetic eigenvalue. Thus $Z$ is an orthogonal projection of $D$. Its squared norm is the independent-set sum with positive activity $t^2$. The upper bound $(1+t^2)^N$ and the count $N^r/r!+O_r(N^{r-1})$ at each fixed degree $r$ give $\|Z\|_2^2\to e^{3\theta}$. The physical trace gives $\|D\|_2^2\to e^{3\theta}$. Pythagoras now gives $\|D-Z\|_2\to0$. This last step accounts for the discarded connected supports, higher spins and winding sectors. [Physical trace calculation](electric.md)

### Signed plaquette activities

The incompatibility graph has degree bounded by an absolute $\Delta$ because each face touches only four vertices. Fix the Haar links for the moment, so $|X_p|\le4$ are deterministic. For an induced subgraph $H$ let $Z_H(z)$ use activities $zX_p$. The deletion identity reads
$$
 Z_H=Z_{H-v}+zX_v Z_{H-N[v]}.
$$
Take $R=2^{-\Delta-4}$. By induction, for $|z|\le R$, every ratio $Z_H/Z_{H-v}$ lies within $1/2$ of one. Indeed, on deleting the neighbors of $v$ one by one from $H-v$, each inverse ratio has modulus at most two. The correction to one therefore has modulus at most $4R\,2^\Delta\le1/2$. This also proves that no denominator vanishes, starting from the empty graph. Summing the analytic logarithms of the deletion ratios gives the branch $\log Z(0)=0$ and $|\log Z(z)|\le N\log2$ on that disk. For small real $t$ every ratio is positive. Cauchy’s coefficient bound gives a remainder $O_\Delta(N|t|^3)$ after degree two when $|t|\le R/2$, uniformly over sampled links. The first two coefficients of the independent-set polynomial give
$$
 \log Z(t)=t\sum_p X_p-\frac{t^2}{2}\sum_p X_p^2
             -t^2\sum_{\{p,r\}\ \mathrm{incompatible}} X_pX_r
             +O_\Delta(N|t|^3).
$$
Each incompatible unordered pair occurs once. This argument permits negative face readings. [Scott and Sokal on the independent-set polynomial and the deletion argument](https://arxiv.org/abs/cond-mat/0309352)

### The limiting likelihood under independent slices

In product Haar links, $\mathbb E X_p=0$, $\mathbb E X_p^2=1$, and $\mathbb E X_pX_r=0$ for $p\ne r$ by character orthogonality. The incompatibility graph is a dependency graph, since collections sharing no vertices depend on disjoint links. Bounded local terms imply that the variances of $\sum X_p^2$ and of the incompatible-pair sum are $O(N)$. Their means are $N$ and zero. For the linear sum, each fixed-order joint cumulant vanishes when the indices split into two independent families. Connected ordered tuples of any fixed size $k$, allowing repetitions, number $O_{k,\Delta}(N)$, and their cumulants are bounded since $|X_p|\le4$. Consequently the variance of $\sum X_p/\sqrt N$ is one and each cumulant of order $k\ge3$ tends to zero. Moment convergence and moment determinacy of the Gaussian yield a standard normal limit. [Janson’s dependency-graph cumulant theorem](https://doi.org/10.1214/aop/1176991903)

Now $Nt^2\to\sigma^2=3\theta$ and $Nt^3\to0$. The expansion gives $\log Z(t)\Rightarrow \sigma G-\sigma^2/2$, $G\sim N(0,1)$. The projection estimate transfers the exponentiated limit to $D$. Its bounded second moments give uniform integrability of $|D-1|$. Using $\|P_n-Q\|_{\rm TV}=\mathbb E_Q|D-1|/2$, integrate the normal density on $G>\sigma/2$ to obtain $2\Phi(\sigma/2)-1$. At $\theta=0$ the limit is zero directly in $L^2$.

A separate finite check enumerates all 2,048 link-increment assignments on a three-square electric $\mathbb Z_2$ graph containing two edge-sharing squares. It tests the projected likelihood and the contribution of the omitted six-edge perimeter. An independent binary product control checks the Gaussian profile on increasing sample sizes. Both calculations use finite probability laws. [Control program](profile_check.py)
