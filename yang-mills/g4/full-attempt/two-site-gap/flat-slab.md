# Fixed blocks fail even at flat central endpoints

The high magnetic energy configuration in the one-step test leaves open the possibility that several Wilson steps, or endpoints confined to a central patch, could repair the estimate. Here the endpoints have zero magnetic action and can both approach the identity at the predicted slow scale. We keep the intermediate spatial Wilson weights and allow arbitrary intermediate link fields. This extends the one-step flat endpoint question C4 took on the directors’ board. [C4's stated scope](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7108543566)

Let $n\ge1$ and use the same periodic spatial box and projected transfer as in the [one-step calculation](kernel.md). Set $x$ equal to the identity links. In $y$ put $\exp(i\theta\sigma_3/L)$ on every positive link along direction one and identity on the other links, with $0\le\theta\le\pi/2$. Denote the continuous kernel of $T^n$ on the gauge and center quotient by $K_n$. For the geometric ratio
$$
 R_n=\frac{\sqrt{K_n(x,x)K_n(y,y)}}{K_n(x,y)}
$$
one has
$$
 \log R_n=\beta nL^3[1-\cos(\theta/(nL))]
             +O(nL^3(1+\log\beta)),\qquad \beta\ge2 .
$$
The error constant is independent of $n,L,\theta$. $R_n^2$ is the projective cross-ratio.

**Exact minimum action.** Write each plaquette loss as $1-\cos t$, where $t\in[0,\pi]$ is its $SU(2)$ geodesic angle. Use temporal gauge with one endpoint gauge average. Since the center and gauge projections commute with the transfer and are idempotent, all endpoint symmetry averages can be consolidated there. In each of the $L^2$ spatial winding rows in direction one, telescope the $n$ successive loop holonomies. Replacing the $L$ factors of one loop by those of the next one changes its holonomy by at most the sum of the $L$ geodesic distances of the corresponding links, by bi-invariance and the triangle inequality. Those distances are the angles of the temporal faces in temporal gauge. The final holonomy is conjugate to $e^{i\theta\sigma_3}$ or to its negative, so its distance from the identity is at least $\theta$. Consequently the $nL$ face angles on each disjoint row sum to at least $\theta$.

Decrease these angles until their sum equals $\theta$. They now belong to $[0,\pi/2]$. The Wilson loss is increasing on $[0,\pi]$ and convex on $[0,\pi/2]$. Jensen bounds the original row loss below by $nL[1-\cos(\theta/(nL))]$. Other losses are nonnegative. Set the direction-one links on slice $t$ equal to $\exp(it\theta\sigma_3/(nL))$ for $t=0,\ldots,n$, use trivial seam and identity endpoint gauge. All spatial plaquettes stay flat and every direction-one temporal face attains the row average. This gives the mixed minimum exactly. Both diagonal minima are zero by the constant paths. [Lean Jensen inequality](TwoSite.lean)

**From the minimum to the kernel.** Strip the common link normalization from all four entries. Haar measure is a probability and the center average has eight terms. The upper integral bound is the exponential of minus $\beta$ times the minimum loss. For a lower bound, retain the trivial cut and restrict each independent interior link and each site variable at the endpoint to a chordal cap of radius $1/\beta$ about its optimizing value. There are at most $3(n-1)L^3+L^3$ such variables. The half-trace is Lipschitz in the sum of the link distances of a plaquette, also after the endpoint gauge rotation. There are $O(nL^3)$ plaquettes, so the loss increases by at most $C nL^3/\beta$. Cap mass is at least $c\beta^{-3}$. These bounds prove the displayed estimate with the same scalar normalization for all three entries.

For fixed $n,L$ and $\theta=k\beta^{-1/3}$, $k>0$,
$$
 \lim_{\beta\to\infty}\beta^{-1/3}\log R_n=\frac{Lk^2}{2n}.
$$
The corresponding per-step lower bound on the gap, $-n^{-1}\log\tanh(\Delta_n/4)$, is at most $n^{-1}\log[(R_n+1)/(R_n-1)]$. It is exponentially small in $\beta^{1/3}$ even when both endpoints belong to a central ball of radius $O(\beta^{-1/3})$ at fixed volume. This also places an obstruction on the diameter computed from just those endpoint rows and columns of the full slab kernel. Compression of intermediate integrations changes the operator and requires its own analysis. For fixed positive $\theta$, the action term is of order $\beta L\theta^2/n$ when $\theta/(nL)$ is small. The explicit entropy error shows precisely where this calculation ceases to resolve the exponent for growing block lengths. It does not exclude averages with respect to the vacuum, momentum-dependent estimates, or a block length increasing on the slow time scale.
