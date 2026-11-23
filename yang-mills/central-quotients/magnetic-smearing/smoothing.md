# Smoothing with a stopped lattice walk

All cochains here live on the lifted four-dimensional cubical lattice. Let $\Delta=dd^*+d^*d$ and $T=I-\Delta/16$ on each coordinate component. This is the lazy walk holding with probability $1/2$ and moving to each of eight neighbors with probability $1/16$. For an integer $s\ge2$, take $D=\lceil\sqrt{24s\log(s+2)}\rceil$ and stop the walk from zero on first reaching sup distance $D$, at time $\tau$. Set
$$
 \Gamma(x)=\tfrac1{16}\sum_{j=0}^{s-1}\mathbb P(S_j=x,\tau>j),
 \qquad \eta=\operatorname{Law}(S_{s\wedge\tau}).
$$
The exact identity $\Delta\Gamma=\delta_0-\eta$ follows by telescoping the surviving distributions and adding back each step's exit mass at its exit site. In particular $\eta$ is a probability and the primal and dual Hodge pieces below have finite support. The maximal exponential martingale bound for a martingale with increments bounded by one gives
$\mathbb P(\tau\le s)\le 8e^{-D^2/(2s)}\le8(s+2)^{-12}$. For example, in each signed coordinate use $\mathbb E e^{\lambda(S_{j+1}-S_j)_i}\le e^{\lambda^2/2}$, stop at the first crossing, and optimize $\lambda=D/s$.

For the unrestricted kernel $p_j$ and one coordinate difference $\nabla_i$, $\|\nabla_i p_j\|_1\le C/\sqrt{j+1}$. To verify this, generate a step by choosing an axis uniformly, then an increment with probabilities $1/4,1/2,1/4$. Start two walks at neighboring vertices, synchronize other axes, and on updates of the differing axis use increment pairs $(-1,0),(0,-1),(1,0),(0,1)$ equally until the walks meet. The difference at these updates is a simple symmetric one-dimensional walk from one. Its survival through $k$ updates is $2^{-k}\binom{k}{\lfloor k/2\rfloor}$ by reflection, bounded by $C/\sqrt{k+1}$. The binomial number of relevant updates is at least $j/8$ except with probability $O(1/(j+1))$ by Chebyshev. The coupling inequality for total variation now gives the asserted $\ell^1$ estimate. Applying a first difference to the subprobability of survivors changes the unrestricted difference by at most twice the exit probability. Consequently $\|\nabla_i\Gamma\|_1\le C\sqrt s$. For $m=1,2$, split $p_s$ into $m$ convolution factors of comparable times and apply one difference to each to get $\|\nabla_i^m p_s\|_1\le C_m s^{-m/2}$.

Choose $r=1/b\to\infty$ and a real $\psi\in C_c^\infty(\mathbb R^3)$. Let $\nabla_3 a(x)=a(x)-a(x-e_3)$ on lattice sites. Set $\psi_r(x)=\psi(x/r)$. On one time slice give the spatial $12$ faces the weights
$$
                 g_{m,r}(x)=r^{m-1}(\nabla_3^m\psi_r)(x),\qquad m=1,2 .
$$
A fixed finite linear combination of such slices at bounded physical times with a common $m$, profiles and color coefficients satisfies $\|g\|_1\le C r^2$ and $\|g\|_\infty\le C/r$. The mean-value formula for a finite difference bounds it by $r^{-m}\|\partial_3^m\psi\|_\infty$. Before differencing, the $\ell^1$ mass of the weighted profile is at most $C r^{m+2}$. Take
$$
 h=d^*(\Gamma*g),\quad k=d(\Gamma*g),\quad w=\eta*g .
$$
Then $g=dh+d^*k+w$ exactly. Convolution inequalities and coupling stopped and unrestricted endpoints on the same walk give
$$
 \|h\|_1+\|k\|_1\le C\sqrt s\,r^2,\qquad
 \|w\|_1\le C(r^{m+2}s^{-m/2}+r^2(s+2)^{-12}).
$$
All supports and the required rooted paths lie inside a patch of radius $R=C_\psi(r+D+1)$; the constant may depend on the finite list of times. The magnetic Fourier integral bounds $\|Pg\|_2$ uniformly, including finite linear combinations by the triangle inequality. [Fourier calculation](spectrum.md)

For clarity the following sufficient joint conditions include all logarithms. Write $\ell=\log(2+r)$.

| Difference order | Spatial side in cells | Inverse bare coupling |
| --- | --- | --- |
| $m=1$ | $L/(r^3\sqrt\ell)\to\infty$ | $\beta/(r^{16}\ell)\to\infty$ |
| $m=2$ | $L/(r^2\sqrt\ell)\to\infty$ | $\beta/(r^{12}\ell)\to\infty$ |

To check the rates, set $\nu=1+2/m$ so $\nu=3$ or $2$. Put $s=\lceil A r^{2\nu}\rceil$, where $A\to\infty$ slowly with $A\le r$. Then $D=O(\sqrt A\,r^\nu\sqrt\ell)$ and $\|w\|_1=O(A^{-m/2}+r^2s^{-12})$. The [Ward error](ward.md), including the variance correction, is bounded by
$$
 C\left[A^{-m/2}+r^2s^{-12}
             +A\,r^{2\nu+2}\sqrt\ell/\sqrt\beta\right].
$$
Indeed $R+r^2=O(\sqrt A\,r^\nu\sqrt\ell)$ for both rows. One explicit choice is the minimum of $r$, $L/(r^\nu\sqrt\ell)$, and $(\sqrt\beta/(r^{2\nu+2}\sqrt\ell))^{1/2}$. Each tends to infinity, $R/L\to0$, and the last error tends to zero. This proves convergence of the characteristic functions on every joint sequence satisfying the indicated row. Neither a time-diagonal subsequence nor a volume-dependent Gaussian approximation is assumed.
