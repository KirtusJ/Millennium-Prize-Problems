# From single-link probabilities to the heat trace

## The conditional Wilson law

A spatial link occurs once in each of four spatial plaquettes and two temporal plaquettes. Fixing every other link makes its log density a constant plus $h\cdot u$ on the round quaternion sphere $S^3$, with $|h|=R\le B-1$. This follows from multiplication by unit quaternions and inversion being real-linear isometries on the quaternion coordinates. It holds when the observed link is in an arbitrarily chosen time slice of the four-dimensional lattice.

The conditional density relative to normalized Haar is bounded by $20(1+R)^{3/2}$. Indeed, in the cap of angular radius $(1+R)^{-1/2}$ about the maximizer, the unnormalized density is at least $e^{R-1/2}$. Angular Haar has density $2\sin^2\vartheta/\pi$ and $\sin\vartheta\ge2\vartheta/\pi$ on that cap. Integrating gives a Haar mass at least $8(1+R)^{-3/2}/(3\pi^3)$. The claimed constant follows using $3\pi^3 e^{1/2}/8<20$. A chordal ball of radius $r\le2$ has Haar mass at most $r^3$. Integrate $\sin^2\vartheta\le\vartheta^2$ up to $2\arcsin(r/2)\le\pi r/2$.

In each elementary cube containing $2^3$ vertices, choose one specified spatial plaquette and one of its links. Call the cube bad when the quaternion chord $r_p=|1-U_p|$ is smaller than $r_0=1/(8\sqrt B)$. Conditional on all other links, the permissible values of the chosen link form a translated or inverted chordal ball. Hence the conditional bad probability is at most $20/8^3<1/16$, uniformly in the exterior. For disjoint small cubes, any other specified bad events are measurable with respect to the complement of this chosen link. Integrating it out and iterating shows that the probability that all of any $k$ specified cubes are bad is at most $16^{-k}$. This step also works with fixed external links. A union bound over all subsets in a block of $n$ small cubes shows that the probability of at least half being bad is at most $2^n16^{-\lceil n/2\rceil}\le2^{-n}$. [Lean dependence and majority bounds](HeatTrace.lean)

## Magnetic energy on a small and a large cube

Use dimensionless edge energy $E_C=\sum_{(x,y)\subset C}\|f(x)-U_{xy} f(y)\|^2$ with free boundary. The defining SU(2) representation obeys
$$
 (I-U_p)^*(I-U_p)=(2-\operatorname{Tr}U_p)I=r_p^2 I .
$$
Transport each of the four face differences to their common basepoint $o$ and telescope. Cauchy–Schwarz gives $r_p^2\|f(o)\|^2\le4E_C$. A path of at most three edges from $o$ to any site of the small cube gives $\|f(x)\|\le\|f(o)\|+\sqrt{3E_C}$. Squaring, summing the eight sites and using $r_p^2\le4$ yields
$$
 r_p^2\sum_{x\in C}\|f(x)\|^2
 \le (64+48r_p^2)E_C\le256E_C .
$$
In particular the total squared norm on all good small cubes in a large block is at most $16384B$ times its internal energy. The graph paths retain their orientations even when links do not commute. [Lean isometric path and cube checks](HeatTrace.lean)

Now take a block of $m^3$ sites, $m$ even, containing $n=(m/2)^3$ small cubes. Put $g(x)=\|f(x)\|$. The triangle inequality gives $|g(x)-g(y)|^2\le\|f(x)-U_{xy}f(y)\|^2$. The scalar free-boundary cube has Poincaré inequality $\sum|g-\bar g|^2\le m^2 E_{\rm block}$. For instance the one-dimensional free-boundary path has eigenvectors $\cos(\pi k(j+1/2)/m)$, $0\le j,k<m$, with eigenvalues $2-2\cos(\pi k/m)$. The product cube has the sums of those eigenvalues and its first positive value is at least $4/m^2$.

If good small cubes contain at least half the sites, sum $|\bar g|^2\le2g(x)^2+2|g(x)-\bar g|^2$ over their sites. Adding back the variance gives
$$
 \sum_{x\in{\rm block}}\|f(x)\|^2
 \le (5m^2+65536B) E_{\rm block}.
$$
Define $v(x)=1/[b^2(5m^2+65536B)]$ throughout such a block, and zero in the others. Dropping edges between blocks in the nonnegative form proves $A_U\ge v$ as forms. For a partially occupied block extend $f$ by zero into the block before applying the estimate. Edges to zero sites are included in the Dirichlet form, and links in the surrounding buffer are sampled from the same Wilson law. If every block touching the domain is good, the variational characterization already gives the claimed lower bound on its least eigenvalue.

## Paying for rare blocks without a site-count divergence

For any fixed link configuration the diagonal block of $K_t=e^{-tA_U}$ at a site is positive semidefinite and has operator norm at most the return probability $p_t(0)$ of the free continuous-time walk on $b\mathbb Z^3$. To see this, expand $e^{-6t/b^2}\exp(t\mathcal A_U/b^2)$. Every admissible return walk contributes a unitary matrix times a positive scalar. Taking its norm and allowing all walks on $\mathbb Z^3$ proves the bound. Fourier inversion and $1-\cos k\ge2k^2/\pi^2$ for $|k|\le\pi$ give
$$
 p_t(0)=\left[\frac1{2\pi}\int_{-\pi}^{\pi}
       e^{-2t(1-\cos k)/b^2}\,dk\right]^3
 \le\left(\frac{\sqrt\pi\, b}{4\sqrt t}\right)^3
 \le b^3 t^{-3/2}.
$$
This is why the comparison to a physical volume works uniformly in $b$. [Discrete vector-bundle semigroups](https://arxiv.org/abs/1306.6062)

Since $A_U\ge(A_U+v)/2$, the finite-dimensional min–max principle bounds the trace of $e^{-sA_U}$ by that of $e^{-s(A_U+v)/2}$. Golden–Thompson bounds the latter by $\operatorname{Tr}(e^{-sA_U/2}e^{-sv/2})$. The last expression sums the positive diagonal blocks of the heat kernel with scalar weights. Use the diagonal bound at $t=s/2$ **before** taking the expected bad-site fraction. A site lies in a bad large block with probability at most $2^{-n}$ independently of the size of the test domain. Its expected weight is therefore at most $2^{-n}+\exp[-s/(2b^2(5m^2+65536B))]$. Summation gives the finite-volume estimate in the main note. Operator monotonicity of the matrix exponential is not needed. [Golden's trace inequality](https://doi.org/10.1103/PhysRev.137.B1127) · [Rates and eigenvalue conclusions](README.md)

### If the particle also has periodic spatial boundary conditions

The original gauge ensemble above is periodic while the particle has an embedded Dirichlet domain. For a particle moving on the entire spatial torus with block side dividing the torus sides, the same form and trace comparison instead uses the scalar torus return probability. With $L_i$ sites in direction $i$ it is at most
$$
 \prod_{i=1}^3 \left( L_i^{-1}+\frac{\sqrt\pi b}{4\sqrt t}\right).
$$
For each coordinate, use the discrete Fourier series and bound the positive frequency tail by the integral of $\exp[-16t u^2/(bL_i)^2]$ over $u\ge0$, counting both signs. For fixed physical sides bounded below and fixed $s$, this still gives an $O_s(b^3)$ diagonal bound at $t=s/2$. The $L_i^{-1}$ terms account for winding and the constant free mode.
