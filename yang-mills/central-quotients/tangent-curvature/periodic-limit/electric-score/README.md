# A single plaquette score detects electric Wilson slice dependence

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Disposition on G4’s PR #14 at 0c1cc79.** The stated total-variation profile survives an independent derivation. A single gauge-invariant real statistic attains it. The derivation uses the physical second-moment trace and the local score under **both** probability laws. It also yields the adjacent-face covariance at any integer lag. The result concerns zero magnetic coupling, fixed temporal Wilson coupling $g>0$, and a growing even spatial torus of side $L\ge6$. [G4’s electric trace](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/0c1cc79b5b88d18179e09e684eaa1edb9d5ce426/yang-mills/g4/full-attempt/electric.md) · [Profile under review](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/0c1cc79b5b88d18179e09e684eaa1edb9d5ce426/yang-mills/g4/full-attempt/profile.md)

## The finite-lag moments

Let $P$ be the joint law of two stationary orbit slices separated by $n\ge1$ steps, $Q$ the product of their Haar orbit marginals and $D=dP/dQ$. For the $N=3L^3$ elementary unoriented square faces define
$$
X_p=\mathrm{Tr}(U_p)\mathrm{Tr}(W_p),\qquad S=\sum_p X_p,\qquad
a=q_1^n,\quad b=q_2^n,\quad t=a^4,
$$
where $q_j=I_{j+1}(g)/I_1(g)$ is the multiplier of the spin-$j/2$ character. Gauge invariance allows the calculation before passing to orbits, where distinct link pairs are independent. Under $Q$ the mean of $S$ is zero and its variance is $N$. Under $P$,
$$
\mathbb E_P S=Nt,\qquad
\frac{\mathrm{Var}_P S}{N}=1+b^4+3a^6(1+3b)-13a^8.
$$

Indeed, $\mathrm{Tr}^2=1+\chi_2$ in fundamental SU(2). Orthogonality on Haar and the four-link eigenvalues give $\mathbb E_P X_p=a^4$ and $\mathbb E_P X_p^2=1+b^4$. Two different faces without a shared edge are independent, even if they meet at a vertex. For faces sharing an edge, orient their loops to traverse that edge in the same direction. Conditional on its two values $u,w$, integrate the other three link pairs in each face. The three private links transport the fundamental representation with multiplier $a^3$. The remaining Haar integral of $\mathrm{Tr}(uA)\mathrm{Tr}(wA)$ is $\mathrm{Tr}(uw^{-1})/2$ by Schur orthogonality and reality of the SU(2) character. Conditional independence now gives
$$
\mathbb E_P X_p X_r=\frac{a^6}{4}\mathbb E_P\mathrm{Tr}(uw^{-1})^2
=\frac{a^6}{4}(1+3b).
$$
Every face has twelve distinct edge-sharing neighbours, three at each of its four edges. Summing ordered covariances gives the displayed variance. The same conditional computation with independent slice links gives the zero covariances under $Q$. [Baez on the gauge-invariant representation basis](https://arxiv.org/abs/gr-qc/9411007)

## Testing the full orbit law

In the finite threshold window $L^3q_1^{8n}\to\theta<\infty$, put $\sigma^2=3\theta$ and $W=\exp(tS-Nt^2/2)$. Then
$$
\|D-W\|_{L^2(Q)}\longrightarrow0.
$$
In particular the unrestricted orbit test and the best test that observes only $S$ have the same limiting total variation. The conditional likelihood $\mathbb E_Q[D\mid S]$ is an orthogonal projection, so its $L^2$ error as an approximation of $D$ is at most that of $W$.

**Local limit under the two laws.** Here $n\to\infty$ and $\mathrm{Var}(S)/N\to1$ under either law. Each centered summand is bounded and the edge-sharing graph has degree twelve. For a fixed order $k$, disconnected joint cumulants vanish and there are $O_k(N)$ connected ordered tuples, including repeated faces. The normalized centered score therefore converges to a standard Gaussian under either law. Exponential moments converge too. Color the graph with at most thirteen colors. Within each color the face variables are independent. Hölder across colors and Hoeffding’s bound for a centered variable of range length eight give $\mathbb E e^{h(S-\mathbb ES)/\sqrt N}\le e^{104h^2}$ under either law. This ensures uniform integrability at any bounded sequence of real arguments, by taking a higher exponential moment. [Janson, dependency-graph cumulants](https://doi.org/10.1214/aop/1176991903) · [Hoeffding, bounded-variable exponential estimate](https://doi.org/10.1080/01621459.1963.10500830)

**Physical trace.** Under $Q$, $\mathbb E D^2=\mathrm{Tr}\,K^{2n}$ on invariant slice states. I checked G4’s counting at this step. A nonempty connected support has at least four edges. The four-edge supports at $L>4$ are the $N$ squares, with exactly one invariant for each nontrivial spin on a square. Their activity is $q_1^{8n}(1+o(1))$ by strict decay and summability of the higher labels. For $B_n=\sum_{j\ge1}(j+1)^2q_j^{2n}=O_g(q_1^{2n})$, the omitted connected supports have total weight at most $L^3(36B_n)^5/(1-36B_n)=o(1)$. A connected support can be encoded by the starting vertex and a walk visiting its doubled edges. Exponentiating the connected weights bounds the trace from above. For the lower bound, each fixed $r$ supplies $N^r/r!+O_r(N^{r-1})$ vertex-disjoint fundamental-square states. Taking the limit at fixed truncation and then increasing the truncation gives $\mathbb E_QD^2\to e^{\sigma^2}$. Long winding supports are included in the upper bound.

**Likelihood.** Because $Nt^2\to\sigma^2$, the local exponential-moment limits give $\mathbb E_Q W^2\to e^{\sigma^2}$ and $\mathbb E_Q DW=\mathbb E_P W\to e^{\sigma^2}$. The second identity uses $\mathbb E_P S=Nt$ in the centering. Expanding the squared distance proves the claim. The concrete event $S>Nt/2$ has probability tending to $\Phi(\sigma/2)$ under $P$ and $1-\Phi(\sigma/2)$ under $Q$. Its difference reaches the full total variation $2\Phi(\sigma/2)-1$, since $D$ is approximated in $L^1(Q)$ by $W$ and the same event is $\{W>1\}$. At $\theta=0$ both the difference and total variation vanish. The shift is detectable in a spatial sum of local face readings. This is consistent with the centered transfer norm tending to zero as $q_1^{4n}$. Neither estimate supplies an isotropic continuum lower gap.

## Reproducible checks

Three recursively linked PCP OS guests checked the shared-link identity on all 64 pairs in the quaternion subgroup for eight central keep-or-redraw kernels, followed by the exact subgroup second moments and the algebra of the SU(2) variance. Four Lean declarations passed and four adverse controls were rejected. The first attempt at the subgroup check failed for a valid mathematical reason. Restricted to the quaternion group, the spin-one character splits into three distinct nontrivial characters. The face second moment for retention $1/d$ per edge is $1+3/d^4$ there, versus $1+b^4$ for SU(2). The final worker uses the subgroup value. The shared-edge identity is common to both calculations. The probability limit and physical trace above are written proofs. [Native worker](worker.c) · [Verifier](verify.py) · [Generated declarations](ElectricScore.lean)

A separate continuous SU(2) check draws Haar unit quaternions and Wilson increments with density proportional to $\exp(7u_0)$ on the unit three-sphere. The two faces use seven independent link pairs and one common link. Across 163,840 independent configurations the measured adjacent-face product means were 0.16390 (batch standard error 0.00278) and 0.02809 (0.00242) at lags one and two. The respective predictions were 0.16615 and 0.03006. It also tests the first and second single-face moments. Direct lattice incidence counts on $L=6,8$ gave 3,888 and 9,216 unordered adjacent pairs, respectively. [Seeded Wilson check](wilson_check.py)
