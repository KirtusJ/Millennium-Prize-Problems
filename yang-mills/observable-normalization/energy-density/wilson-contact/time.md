# Contact variance across time and its transfer-spectrum consequence

## All spatial slices on one Wilson history

For arbitrary real weights $w_{p,t}$, the spatial-link conditional argument can be applied simultaneously in every time slice. Properly color the cycle of time layers with at most three colors. Randomly permute the three spatial orientations and assign each time layer the orientation of its color. Adjacent layers then select different orientations, and each layer has a uniform orientation marginal. Use the transverse spatial checkerboard mask within each layer. A temporal face has parallel spatial links in consecutive layers, hence contains at most one selected link. Spatial faces already have that property. This construction works for odd as well as even periods.

The variance of the sum over all the slices is bounded below by the sum of the single-slice $D_b(w_t)$. In particular for the same spatial test and any real temporal coefficients $c_t$ the connected time covariance matrix dominates $D_b I$ as a quadratic form. If $S_b=b\sum_t O_b(t)$ with smooth spacetime-dependent spatial-face profiles, then
$$
 \liminf b^4\operatorname{Var}(S_b)
 \ge\frac1{36}\int dt\,d^3x\sum_i\left(\sum_{j\ne i} f_{ij}(t,x)\right)^2 .
$$
The temporal extent is taken to a fixed positive physical period with smooth periodic tests, or the tests fit with padding in a growing physical box. The result concerns an ordinary variance in the original history measure, including coincident supports.

## All six plaquette orientations

For $S_b=\beta\sum_p f_{ij}(x_p^{\rm center})(1-x_p)$ including time-oriented faces, choose one link orientation uniformly among four throughout the whole box. Mask one parity on the other three coordinates, deleting one randomized seam in each odd transverse period before coloring. Every link has inclusion probability tending to $1/8$ as all site counts grow. At finite cutoff use its actual orientation-dependent inclusion probability. No face contains two selected links. The same conditional argument uses $\mathbb E(U_e\cdot a_e)=\sum_{p\ni e}w_p m_{ij}$, and all six orientation means tend uniformly to one. Thus
$$
 \liminf b^4\operatorname{Var}(S_b)\ge
 \frac1{48}\int d^4x\,\sum_{i=1}^4
      \left(\sum_{j\ne i} f_{\min(i,j),\max(i,j)}\right)^2 .
$$
For three equal spatial weights $m(x)$ and three equal temporal weights $d(x)$, the integrand before division by 48 equals $3(2m+d)^2+9d^2=6(m^2+d^2)+6(m+d)^2$. Mixing the two types with opposite signs still leaves a divergence for every nonzero pair. For unrestricted six-tuples the incidence map has a kernel. For instance $f_{12}=f_{34}=g$, $f_{13}=f_{24}=-g$, and the remaining weights zero make this lower bound vanish. A separate [two-link integration-by-parts estimate](dual.md) also controls these two missing directions.

The lower bound gives a necessary $O(b^2)$ overall suppression to keep these unmodified, spacetime-smeared history variables bounded in $L^2$ along the trajectory, when the right side is positive. A reflection-positive norm with support separated from its reflected copy uses a different covariance. Likewise the electric plaquette on a Wilson history and an equal-time Hamiltonian kinetic operator have different contact conventions. This divergence cannot decide the existence of the physical stress field.

## Alternating readout on the original transfer

At fixed finite spatial box take the infinite-period vacuum transfer limit. The standard positive Wilson transfer yields $C_b(n)=\int_{[0,\infty)}e^{-|n|bE}\,d\nu_b(E)$ for the centered spatial insertion, with a finite positive spectral measure. Equivalently one can work with transfer eigenvalue $r\in[0,1]$ throughout, with $r=0$ interpreted at infinite energy if needed. The finite-period covariance inequality passes to each fixed finite time vector; the spatial mean in $D_b$ also has its vacuum limit. [Wilson transfer and vacuum limit](../../../transfer-operator/periodic-time/)

Use the alternating coefficients $(-1)^j$ on $N$ consecutive times, for even $N$. The result divided by $N$ has spectral kernel
$$
 \frac1N\sum_{j,k=0}^{N-1}(-1)^{j+k}r^{|j-k|}
 =\frac{1-r}{1+r}+\frac{2r(1-r^N)}{N(1+r)^2}.
$$
The remainder lies in $[0,1/N]$ uniformly, including $r=1$. Passing to the limit at this fixed spatial cutoff gives
$$
 \int\tanh(bE/2)\,d\nu_b(E)\ \ge D_b(w).
$$
This identifies which spectral reading the temporally local noise forces. A lower bound for this integral alone does not bound the proportion of spectral weight at the mesh energy.

If a fixed physical time $t>0$ has an upper bound $C_b(t)\le V$ uniform in the cutoffs (with the transfer interpolated by its spectral calculus), then for any $M>0$,
$$
 \nu_b((M,\infty))\ge D_b(w)-\tfrac12 bM e^{tM} V .
$$
On $[0,M]$ use $\tanh(bE/2)\le bM/2$ and the positive-time bound; on the upper interval the kernel is at most one. Thus even the growing threshold $M_b=(6-\epsilon)\log(b_*/b)/t$, $0<\epsilon<6$, leaves $\liminf b^5\nu_b((M_b,\infty))$ at least the coefficient in the main note ($b_*>0$ fixes the reference length). The uniform positive-time input here is a hypothesis. The lower bound on the alternating readout and the equal-time loss require no such input.
