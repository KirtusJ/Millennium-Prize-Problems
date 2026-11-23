# A magnetic reading with weight at finite lattice energy

This argument uses only the bare first moment and the transfer norm. The [two-moment proof](concentration.md) below the same coupling threshold gives a much larger interval of permitted flow times and a narrower energy band. The inverse-flow construction in this note serves both proofs.

This uses two volume-uniform inputs from B4 for the **same** isotropic SU(2) Wilson vacuum. For sufficiently small $0<\beta<r=1/1024$ the normalized positive transfer on the centered gauge-invariant subspace has norm at most $B=(\beta/r)^4$ on tori of spatial side at least four. The unnormalized elementary plaquette trace has connected one-step correlation $(\beta/4)^4(1+O(\beta))$, with uniform remainder. B4 also gives the transfer bound and the local leading term in the infinite-volume strong-coupling vacuum. We use these estimates as inputs. The elementary tube giving the fourth power is consistent with the primary strong-coupling calculation of Langelage, Münster and Philipsen. [B4's proof and its volume assumptions](../../transfer-operator/connected-rectangles/gap.md) · [Analytic disk](../../transfer-operator/connected-rectangles/analyticity.md) · [Primary calculation, Eqs. (40)–(42)](https://arxiv.org/pdf/0805.1163)

Let $F=1-\operatorname{Re} U_p$ be one bare elementary spatial plaquette deficit and let $G\in[0,2]$ be another gauge-invariant reading of one slice. Put $c=r^4/4096=2^{-52}$. Uniformly for sufficiently small positive $\beta$, centering and dividing the trace by two give

$$C_1(F)\ge\frac{1}{8}(\beta/4)^4=2cB.$$

If $\|F-G\|_\infty\le\delta$, their centered vectors differ in vacuum norm by at most $\delta$ because centering is orthogonal projection. Each centered norm is at most one by the range bound. Inserting the difference in each of the two slots gives

$$|C_1(G)-C_1(F)|\le 2\delta B.$$

Using the norm on the centered subspace matters. It supplies the same factor $\beta^4$ as the signal and lets us fix the allowed error **independently of the coupling**. Thus $\delta\le c/2$ gives $C_1(G)\ge cB$.

For the transfer spectral measure of $G$, the total mass is at most one and the centered support is in $[0,B]$. If $w$ is the mass in $[cB/2,B]$, its first moment is at most $(cB/2)(1-w)+Bw$. We obtain

$$
w\ge\frac{c}{2-c},\qquad
C_k(G)\ge\frac{c}{2-c}(cB/2)^k\quad (k\ge1).
$$

In lattice energy $aE$ the interval is $[4\log(r/\beta),\,4\log(r/\beta)+\log(2/c)]$. The width and certified absolute weight are independent of volume and of sufficiently small $\beta$. The interval moves to high energy as $\beta\downarrow0$. The constants are conservative. [Lean implications](MagneticVariance.lean)

## Which flowed measurements give the bound

**Ordinary flowed plaquette.** Every spatial link has speed at most four in the round metric. Telescoping its four link factors gives $\|F\circ\Phi_u-F\|_\infty\le16u$. The spectral result holds for $0\le u\le c/32=2^{-57}$, a small but strictly positive interval in the specified lattice clock.

**A local measurement at any prescribed finite $u$.** Given flowed links $V$, keep those within cofacial distance $R$ of the target plaquette's links. Complete the other links by identity, evolve the completed slice backwards for $u$ and read the bare plaquette there. Call the result $K_R(V)$. The reversed flow obeys the same distance comparison proved for forward flow. The initialized links inside the patch agree exactly and the exterior chord diameter is two. Thus

$$|K_R(V)-F(\Phi_{-u}V)|\le 8T_R(u).$$

Average $K_R$ over the vertex gauge group at the endpoints of the kept links. The resulting reading $H_R$ is gauge-invariant, remains in $[0,2]$ and depends only on those links. Each term has the same error bound since the exact inverse reading is gauge-invariant. Take $G=H_R\circ\Phi_u$ and $8T_R(u)\le c/2$. One sufficient choice is $R\ge56$ and $R+1\ge32eu$. Indeed $n!\ge(n/e)^n$ and the remaining series is at most $\sum_{n>R}2^{-n}=2^{-R}$. This gives the stated band and separated correlation bounds. The reading uses a locally approximated inverse. For a general $u$ the overlap of the ordinary flowed plaquette is a different question.

The same local recipe can be used across large boxes. Lift the patch to the cubic lattice and pad by identity there. The bounded finite-range vector field is Lipschitz in the sup norm on bounded quaternion arrays on a neighborhood of the unit configurations. Picard iteration gives solutions, link norms are conserved, and the bounded force extends them in either time direction. Periodic solutions lift by uniqueness. Alternatively, periodic padded approximants on increasing auxiliary tori agree on successively larger neighborhoods, and the comparison-series tail makes their readings uniformly Cauchy. The patch reading therefore defines a single continuous cylinder function of the flowed links. Composing it with forward flow gives a uniform limit of cylinder functions at fixed $u$. This justifies the use of local weak limits for its two-time correlations. On small periodic boxes one can directly use the finite torus inverse and average the gauge transformations on its distinct patch vertices.

The result certifies a separated interacting signal in the strong-coupling lattice regime. In the physical refinement of interest $u=s/a^2$ grows, and the radius supplied by the reconstruction bound grows with it. The exact alternating solution shows why a time-uniform deterministic inverse estimate cannot supply the missing fixed-physical-size witness. [Inverse-flow example and clock](README.md) · [G4's physical-window criterion](../exterior/spectral-test.md) · [Jaffe and Witten, §4](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
