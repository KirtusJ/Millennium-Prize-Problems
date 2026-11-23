# A summable bound at every scale in the quadratic Wilson comparison

For the zero-coupling Gaussian curvature comparison in the finite spatial torus vacuum, the block method admits an explicit rate:
$$0\le\chi_{\rm G}-B_{\rm G}(L)\le{9\pi\over2L},\qquad 1\le L\le N.$$
The bound is uniform in side and includes the last, truncated doubling. On dyadic scales each positive increment is at most $9\pi/(2L)$. The result illustrates the kind of estimate that is missing for the interacting Wilson measure.

Use the [three-color Gaussian convention](../isotropic-variance/quadratic.md), a quadratic approximation to the Wilson theory. For an $xy$ plaquette the scalar curvature covariance $g$ on one time slice has symbol $h(q)=(s_x+s_y)/\sqrt{s(s+4)}$, $s_i=4\sin^2(q_i/2)$, $s=\sum s_i$, $h(0)=0$. Wick's formula gives the centered energy covariance $C_{\rm G}(r)=3|g(r)|^2/2$. It is this identity for the energy, together with the Fourier regularity of the curvature, that gives the scale estimate.

The continuous periodic symbol is coordinatewise 2-Lipschitz. Off zero use $|\partial_j s|\le2\sqrt s$, $0\le s_x+s_y\le s$ and $|\partial_j(s_x+s_y)|\le2\sqrt s$. Differentiating the quotient gives a first term at most $2/\sqrt{s+4}\le1$ and a second term at most $2(s+2)/(s+4)^{3/2}\le1$. The value at zero follows by continuity and splitting the integration interval if it crosses that point. For $d_j(r)=\min(r_j,N-r_j)$, Parseval and $\sin(\pi d/N)\ge2d/N$ then give
$$
 {16\over N^2}\sum_r d_j(r)^2|g(r)|^2
 \le \sum_r4\sin^2(\pi r_j/N)|g(r)|^2
 ={1\over V}\sum_q|h(q+2\pi e_j/N)-h(q)|^2\le {16\pi^2\over N^2}.
$$
Also $\sum_r|g(r)|^2\le1$ since $0\le h\le1$. Cauchy–Schwarz bounds $\sum_r d_j(r)|g(r)|^2$ by $\pi$ in each coordinate. The periodic fraction of a side-$L$ cube overlapping a translate by $r$ is at least $1-\sum_j d_j(r)/L$ by the union bound, counting only the sites that can leave at each face. Multiply the missing overlap by $C_{\rm G}(r)$ and sum. Positivity gives the other inequality and proves the estimate. Coordinatewise monotone overlap can also be verified directly from the periodic interval overlap formula.

For the interacting measure, an upper bound independent of $N,\beta$ on $\sum_r\sum_j d_j(r)|C(r)|$ would give the same $O(1/L)$ tail. With the local second moment it would also bound $\chi$. The interacting energy four-point terms have no Wick reduction supplied here. [Exact all-size controls for the comparison](quadratic-tail.py) · [Interaction and block observations](blocks.md)
