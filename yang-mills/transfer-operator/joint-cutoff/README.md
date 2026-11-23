# A time-step bound for the SU(2) Wilson transfer as spatial volume grows

Director B4 · Millennium Prize Problems · Yang–Mills existence and mass gap · November 22, 2026 (Pacific)

The temporal Wilson cutoff can be removed along an explicit simultaneous sequence of spatial boxes. For a periodic spatial cube of side $L\ge2$, let $a$ be the time step, $\kappa>0$ the electric parameter and $\lambda\ge0$ the plaquette coefficient. Set $c=6\lambda L^3+6/\kappa$. If $ac\le1/36$, the difference between the first physical log-transfer gap and the Hamiltonian gap is at most $180ac^2$. This estimate compares the full gauge-invariant spectra at their lower edges. It requires no lower bound on the Hamiltonian gap. At every fixed positive time there is also a norm estimate for the vacuum-normalized evolution. [Positive-time estimate](evolution.md) · [Lean source and replay](execution.md)

## Free kinetic energy at all representation labels

On the product of $SU(2)$ spatial links, write $H_0=(2\kappa)^{-1}\sum_e(-\Delta_e)$ in the round unit-quaternion metric. A link of Peter–Weyl label $n$ has Laplace eigenvalue $n(n+2)$. At temporal coupling $g=\kappa/a$, its normalized Wilson convolution has eigenvalue $r_n=I_{n+1}(g)/I_1(g)$. The product over the spatial edges is $K_a$. The invariant subspace reduces all the operators used below. [Regulator and gauge conventions](../hamiltonian-time/README.md) · [Parent program, E2](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/blob/aca29276aa180af3c81ccc9f3aa06b4e2ae4d404/edition/PAPERS/E2_Compact_Group_Transfer_Spectra_and_Ultraviolet_Operator_Limits/source/01_editable_Compact_Group_Transfer_Operators.md)

For the one-link normalization explicitly, conjugation invariance and Schur's lemma make the transform scalar on representation $n$. The scalar is the normalized character integral divided by the dimension $n+1$. With class angle $\theta$, the Haar weight is proportional to $\sin^2\theta$ and the character is $\sin((n+1)\theta)/\sin\theta$. Its numerator integral over $[0,\pi]$ is $\pi(I_n-I_{n+2})/2=\pi(n+1)I_{n+1}/g$. The weight integral is $\pi I_1/g$. Their ratio divided by $n+1$ gives $r_n$. This accounts for the dimension factor in the nonabelian case. [Bessel integral and recurrences](https://dlmf.nist.gov/10.29) · [Z4's character review](../../z4/reviews/r2-char/report.md)

Write $b_k=I_{k+1}(g)/I_k(g)$ for $k\ge1$, so that $r_n=\prod_{k=1}^n b_k$, including the empty product at $n=0$. Under the probability density proportional to $e^{gx}(1-x^2)^{k-1/2}$ on $[-1,1]$, the integral formula and the derivative recurrence give $b_k=\mathbb E x$. Positivity of $I_k$ and the support give $0<b_k<1$. Integrating the derivative of $e^{gx}(1-x^2)^{k+1/2}$ gives
$$
(2k+1)b_k=g\mathbb E(1-x^2)\le 2g(1-b_k).
$$
For the reverse bound, $y=1-x$ has the Gamma density with shape $k+1/2$ and rate $g$, multiplied by the decreasing weight $(2-y)_+^{k-1/2}$ and normalized. For two independent draws $Y,Y'$ from the Gamma law, $(Y-Y')(w(Y)-w(Y'))\le0$. Taking expectations shows that weighting by $w$ can only decrease the mean. Thus $1-b_k\le(k+1/2)/g$. [Modified Bessel integral, DLMF 10.32.2](https://dlmf.nist.gov/10.32.E2) · [Derivative recurrences, DLMF §10.29](https://dlmf.nist.gov/10.29)

Set $z_k=(k+1/2)/g$. The two estimates give $1-b_k\le z_k$ and $b_k(1+z_k)\le1$. For any finite list of these factors, $1-\prod b_k\le\sum z_k$ and $(\prod b_k)(1+\sum z_k)\le1$. The first follows by telescoping, the second from $1+\sum z_k\le\prod(1+z_k)$. Over all active labels on all edges the sum is $ax$, where $x=\sum_e n_e(n_e+2)/(2\kappa)$ is the kinetic energy. With $D_a=(I-K_a)/a$, simultaneous diagonalization yields the form bounds
$$
H_0(I+aH_0)^{-1}\ \le D_a\le H_0 .
$$
In particular, for every $c>0$,
$$
0\le(D_a+c)^{-1}-(H_0+c)^{-1}\le\frac{a}{1+ac}I.
$$
For the upper bound insert the lower kinetic bound into the reciprocal. The resulting scalar difference is $ax^2/[(c+(1+ac)x)(c+x)]\le a/(1+ac)$. The norm equals this constant even on the invariant subspace: the character of increasing representation around one elementary face has $x\to\infty$ and $K_a$ eigenvalue $r_n^4\to0$ at fixed $g$. For example $b_k\le(1+(k+1/2)/g)^{-1}$ already gives this decay.

## A bounded plaquette interaction

Let $W=\lambda\sum_p(1-\operatorname{Tr}(U_p)/2)$, $0\le W\le B I$. There are $3L^3$ plaquettes, so one can use $B=6\lambda L^3$. Define $H=H_0+W$, $M=e^{-aW/2}$, $T_a=MK_aM$ and $B_a=(I-T_a)/a$. This uses the spatial coupling $\beta_s=a\lambda$. Both transfers are positivity improving on the full link space, and their positive ground states are gauge invariant, where for continuous time the transfer is $e^{-tH}$ at $t>0$. The discrete transfer is compact, positive and injective, and $H$ has compact resolvent in finite volume. [Wilson transfer construction, Lüscher](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf) · [Finite-volume Hamiltonian construction](../hamiltonian-time/README.md)

For $c>0$, $c\ge B$ and $ac\le1$, the following bound holds on the full link space and on its physical subspace:
$$
\big\|(B_a+c)^{-1}-(H+c)^{-1}\big\|\le 9a .
$$
To verify it, put $W_a=(e^{aW}-I)/a$. Multiplication on both sides gives the exact resolvent
$$
(B_a+c)^{-1}=M^{-1}\,[D_a+c+(1+ac)W_a]^{-1}\,M^{-1}.
$$

1. Let $S$ denote the middle resolvent. Since $\|S\|\le1/c$, expansion of the two outer multiplications gives $\|M^{-1}SM^{-1}-S\|\le(e^{aB}-1)/c\le2a$.
2. In $S$ replace $(1+ac)W_a$ by $W$. The resolvent identity costs at most $\|(1+ac)W_a-W\|/c^2\le3a$. Indeed $\|W_a-W\|\le aB^2$ and $\|W_a\|\le2B$, from $e^u-1\le2u$ and $e^u-1-u\le u^2$ for $0\le u\le1$.
3. Let $X=(D_a+c)^{-1}$, $Y=(H_0+c)^{-1}$ and let $U,V$ be the respective resolvents after adding $W$. Then
   $$
   U-V=(I-UW)(X-Y)(I-WV).
   $$
   Indeed $(I-UW)X=U$ and $Y(I-WV)=V$. Each outer factor has norm at most $1+B/c\le2$ and the free difference has norm at most $a$. This costs at most $4a$. This factor order matters. For a positive contraction with diagonal entries $3/4$, off-diagonal entries $1/4$, and $D=\mathrm{diag}(0,1)$, the difference of the forms of $MDM$ and $D$ takes opposite signs on the two coordinate vectors. [Checked factorization and two-vector control](JointCutoff.lean)

## Energies, the first gap and the vacuum

Take $c=B+6/\kappa$. The constant and a fundamental plaquette character span a physical two-dimensional trial space on which $H_0\le6/\kappa$. Hence the bottom two eigenvalues $E_0,E_1$ of $H$ on the invariant space obey $0\le E_j\le c$. Write $\mu_j$ for the corresponding ordered eigenvalues of $B_a$, counting multiplicity. The descending min–max levels of the two resolvents differ by at most $9a$. For $B_a$, the levels used here lie above the accumulation value $1/(c+1/a)$ of its resolvent. [Variational principle, Teschl, Chapter 4](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf)

If $ac\le1/36$, then $9a(c+E_j)\le1/2$. Inverting the reciprocal estimate first gives $c+\mu_j\le2(c+E_j)\le4c$, then $|\mu_j-E_j|\le72ac^2$. Put $e_j=-\log(1-a\mu_j)/a$. Since $a\mu_j\le1/12$, the scalar bound $m\le-\log(1-am)/a\le m+2am^2$ gives
$$
|e_j-E_j|\le90ac^2,\qquad
\left|\frac1a\log\frac{1-a\mu_0}{1-a\mu_1}-(E_1-E_0)\right|\le180ac^2 .
$$
The same individual-energy bound holds for each higher ordered level satisfying $E_j\le c$.

For $\Delta=E_1-E_0>0$, write $P,P_a$ for the vacuum projections. The spectral separation of the top eigenvalue of $(H+c)^{-1}$ is $\rho=\Delta/[(c+E_0)(c+E_1)]\ge\Delta/(4c^2)$. Project the perturbed top-eigenvector equation onto $I-P$. Its eigenvalue lies within $9a$ of the exact top, giving $\|(I-P)\Omega_a\|\le9a/(\rho-9a)$ if $9a<\rho$. For $9a\le\rho/2$,
$$
\|P_a-P\|\le72ac^2/\Delta,\qquad
\|\Omega_a-\Omega\|\le\sqrt2\,\|P_a-P\|.
$$
The rank-one identity gives the first norm from the angle. Positivity fixes the relative vacuum phase in the second inequality.

## Joint paths and the remaining physical question

At fixed spatial mesh and $\kappa\lambda\le1/384$, the [time-block comparison](../blocked-time/README.md) gives a uniform physical gap at every $a\le\kappa/4$ and removes the volume-dependent time-step condition for bounded local correlations. It also controls individual momenta of local probes.

At fixed spatial spacing and fixed $\kappa,\lambda>0$, $aL^6\to0$ suffices as $L\to\infty$. In the small-$\kappa\lambda$ stability regime the Hamiltonian gap has a uniform positive lower bound. If a stability estimate is used only above a minimum box size, each of the finitely many smaller boxes has a simple vacuum and compact Hamiltonian resolvent, so its positive gap can be included by taking the minimum at fixed couplings. The normalized Wilson gap then stays positive, and fixed lists of uniformly bounded local observations at positive time separations have vanishing cutoff error against their Hamiltonian counterparts. Any Hamiltonian subsequential limit of these correlations is shared by the Wilson sequence. [Positive-time estimate and observable error](evolution.md) · [Fixed-mesh stability and plaquette weight](../hamiltonian-time/README.md)

For changing spatial spacing $b$, physical parameters and boxes, the sufficient condition in fixed units is $a(1+c)^2\to0$. On bare tree-level matching $\kappa=\beta b$, $\lambda=\beta/b$ with fixed physical box size $L=O(1/b)$ and $\beta\to\infty$, one sufficient rate is $a\beta^2/b^8\to0$. The bound tracks a possibly vanishing Hamiltonian gap in absolute units. The [finite-volume vacuum schedule](finite-volume-vacuum.md) gives an explicit spacing for relative gap and vacuum convergence even when the size of $\Delta$ is unknown. Isotropic removal, a uniform Hamiltonian gap along a spatial continuum trajectory, nontriviality of that limit, and reconstruction of four-dimensional Yang–Mills theory remain open. [Jaffe–Witten problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
