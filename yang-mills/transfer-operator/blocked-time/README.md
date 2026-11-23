# A volume-independent gap in physical time units at fixed spatial spacing

Director B4 · Millennium Prize Problems · Yang–Mills existence and mass gap · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

On the periodic SU(2) spatial lattice of side $L\ge2$, let the time spacing be $a$, the temporal Wilson coupling $g=\kappa/a$ and the spatial coupling $a\lambda$, with $\kappa>0$, $\lambda\ge0$. Write $z=\kappa\lambda$. In the range
$$
a\le\kappa/4,\qquad z\le 1/384,
$$
the full gauge-invariant, vacuum-normalized Wilson transfer has a first log gap of at least **$4\log(3)/(13\kappa)$** in physical time units, independently of $L$ and $a$. The same floor holds for the continuous-time Hamiltonian. Blocking several time steps makes the free endpoint density close to Haar while preserving the local support of the magnetic interaction. At fixed spatial spacing and couplings, local vacuum correlations converge along **every** simultaneous sequence $a\downarrow0$, $L\to\infty$. [Joint local limit, error rate and spatial-refinement obstruction](local-limit.md) · [Individual momentum laws](momentum.md) · [Faithful characters on compact connected groups](compact-groups.md) · [Execution and formal scope](execution.md)

## The free endpoint density

Use the product link space and Haar probability, the round unit-quaternion metric, and $W=\lambda\sum_p(1-\operatorname{Tr}U_p/2)$. Let $K_a$ be the product of single-link normalized central convolutions with positive density proportional to $\exp(g\operatorname{Tr}U/2)$. Then $T_a=e^{-aW/2}K_ae^{-aW/2}$ is the transfer on gauge-invariant functions. Its gauge-equivariant extension to the full space is positive, compact and positivity improving. The invariant vacuum is unique. Its continuous-time counterpart is $H=(2\kappa)^{-1}\sum_e(-\Delta_{S^3,e})+W$. [Regulator and transfer conventions](../hamiltonian-time/README.md) · [Lüscher, transfer construction](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf)

Use $m=\lceil3g\rceil$ fine steps per block and $s=ma$, so $3\kappa\le s\le13\kappa/4$ for $g\ge4$. The one-link eigenvalue at label $n$ is $r_n=I_{n+1}(g)/I_1(g)$. Its factors $b_j=I_{j+1}(g)/I_j(g)$ for $1\le j\le n$ satisfy $b_j[1+(j+1/2)/g]\le1$. This follows by integrating the derivative of $e^{gx}(1-x^2)^{j+1/2}$ and using $1-x^2\le2(1-x)$. Bernoulli's inequality with exponent $g/4\ge1$ gives
$$
(1+3/(2g))^{m}\ge(1+3/(2g))^{3g}\ge(11/8)^{12}>44 .
$$
Consequently $r_n^m\le44^{-n}$. The endpoint density on one link is $h_m=1+\sum_{n\ge1}(n+1)r_n^m\chi_n$. Since $|\chi_n|\le n+1$ and $(n+1)^2\le4^n$, the series converges uniformly and
$$
\sup_u |h_m(u)-1|\le\sum_{n\ge1}(4/44)^n=1/10 .
$$
Peter–Weyl coefficients identify the sum with the actual convolution density. The estimate is independent of the number of links. [Consecutive-ratio proof and normalization](../joint-cutoff/README.md) · [Lean denominator bound](BlockedTime.lean)

## Exact representation of the magnetic factors

Take a finite **open** slab with endpoints at block times and free boundary vectors $1$ on both ends. At each site $(e,j)$ use one spatial edge endpoint $x_{e,j}$ at block time $j$ and an independent random seed for its outgoing segment. Use product Haar for endpoints and product reference probability for seeds. Each temporal factor is $h_m(x_{e,j}^{-1}x_{e,j+1})$. Given its two endpoints, generate the $m-1$ intermediate link values from the *free* conditional bridge on that edge. Its density with respect to product Haar is the product of the $m$ one-step kernels divided by the endpoint kernel. Different edge segments have independent seeds before inserting the plaquette weights.

One measurable realization uses independent proposals of $m-1$ Haar elements and independent uniforms. Accept a path with probability equal to its unnormalized kernel product divided by the $m$th power of the one-step sup norm. The one-step density has a positive minimum on SU(2), so for every pair of endpoints the first acceptance occurs almost surely. On exceptional seeds use any fixed intermediate values. This construction needs no continuity of the bridge map in its endpoints. The terminal site's unused seed can be integrated out.

For each spatial face in each slab include *one* factor given by its Wilson potential on that four-edge bridge, summed over fine times with weight $a$ inside and $a/2$ at the two endpoints. Its log weight belongs to $[-2\lambda s,0]$. Multiplying with the endpoint densities and integrating the seeds gives exactly the original $T_a^m$ kernel, because conditional normalization cancels and adjacent half potentials combine at each fine interior slice. The same identity holds with bounded insertions at interior fine times. Retaining the random bridges is essential: averaging each magnetic factor separately would discard the dependence of adjacent faces sharing an internal link. [Finite-circuit test and endpoint-only control](execution.md)

## Conditional influence and decay

Change one neighboring site while conditioning a site. For a factor with log weight in an interval of width $D$, the change in its log weight as a function of the conditioned variable has oscillation at most $2D$. The sharp total-variation bound for this change is $\tanh(D/2)$. Sequentially changing shared factors adds their bounds. An endpoint factor in $[1-\delta,1+\delta]$ thus contributes at most $\delta$ with $\delta=1/10$. A magnetic factor contributes at most $\tanh(\lambda s)\le p=\lambda s$. Both bounds hold for all endpoints and seeds. [Likelihood-ratio proof](../strong-coupling/README.md) · [Cohen and Fausti, Corollary 5.2.1](https://arxiv.org/abs/2309.02413)

Each edge belongs to four spatial faces. A magnetic factor on one slab depends on eight endpoint-and-seed sites, four at each end. A given interior site lies in four factors in each of its two adjacent slabs. In each of the eight factors there are three other sites at its own time and four at the other end. The magnetic incidence counts at offsets $-1,0,1$ are therefore $16,24,16$. Two endpoint factors contribute one temporal neighbor on either side. Count repeated neighbors with multiplicity. At an open time boundary some factors are absent. [Enumerated directed faces at sides 2 through 5](block_checks.py)

Write $C$ for the conditional influence matrix in total variation. Its maximum row sum is at most $q_0=2\delta+56p\le647/960$ on the stated range. For an open slab, the row sum weighted by $w_{e,j}=R^j$ and divided by the site's own weight is bounded by
$$
q_R=24p+(\delta+16p)(R+R^{-1}).
$$
At $R=3$, $p\le13/1536$ gives $q_3\le569/576<1$. The finite-volume Dobrushin comparison theorem applies to this lifted probability measure. With the discrete site metric its single-site distance is total variation, including on the seed space. Tilting by $\exp(\epsilon G)$ and differentiating at zero bounds the covariance by $\frac14\sum_{i,j}\delta_i F\,[(I-C)^{-1}]_{ij}\,\delta_j G$, where $\delta_i F$ is the single-site oscillation. The unweighted row bound establishes summability. Positive matrix iteration gives $\sum_{k\ge0}C^kw\le w/(1-q_3)$. [Rebeschini and van Handel, Corollary 2.6 and p. 9](https://web.math.princeton.edu/~rvan/dobrushin130819.pdf) · [Checked row iteration](BlockedTime.lean)

For bounded real functions $F,G$ of endpoints on time slices zero and $n$ this yields
$$
|\operatorname{Cov}(F_0,G_n)|\le\frac{144}{7}\,3^{-n}
\left(\sum_i\delta_i F\right)\max_j\delta_j G .
$$
The estimate is independent of the open ends. Sending both ends to infinity at fixed $L,a$ gives vacuum correlations, since the boundary vector overlaps the unique positive vacuum. For $G=F$ this bounds the positive spectral moment of the centered vector $F\Omega_a$ for $(T_a/\|T_a\|)^m$. Any part of its spectral measure on $[r,1]$ with $r>1/3$ vanishes by taking $n\to\infty$. Centered gauge-invariant multipliers span a dense subspace of the physical vacuum complement. Thus the entire excited transfer norm per block is at most $1/3$. Taking $-\log$ per unit block time gives $\Delta_{a,L}\ge\log 3/s\ge4\log 3/(13\kappa)$. Fixed-$L$ convergence of the two lowest log energies then transfers the bound to $H$. [Spectral-support argument](../strong-coupling/README.md) · [Finite-box log-energy convergence](../joint-cutoff/README.md)

More generally $z<2/455$ gives $q_0<1$ and, by continuity, some $R>1$ with $q_R<1$. This yields a positive uniform floor $4\log R/(13\kappa)$ throughout this larger open interval. The explicit $R=3$ conclusion above uses $z\le1/384$. The independent Hamiltonian stability argument also applies at sufficiently small coupling. [Fixed-mesh Hamiltonian stability](../hamiltonian-time/README.md)

G4’s magnetic curvature at the electric endpoint agrees with an independent Hamiltonian calculation. The comparison with Z4 identifies the missing bound in independently set slab units. [Derivation and track dispositions](magnetic-curvature/README.md)
