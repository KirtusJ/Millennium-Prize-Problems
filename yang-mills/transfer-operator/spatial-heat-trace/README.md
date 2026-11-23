# A spatial heat trace on the four-dimensional Wilson measure

Director B4 · November 22, 2026 research session · November 23 continuation, B.C. Pacific Time (PCT, UTC−07:00)

A charged particle diffusing over a fixed physical distance defines a gauge-invariant sum of spatial loops. On the **original isotropic SU(2) Wilson law**, its unrenormalized heat trace per physical volume tends to zero as the mesh $b$ goes to zero whenever $b^2(1+\beta)\to0$. On trajectories with $\beta$ at most polylogarithmic in $1/b$, it tends to zero faster than any power of $b$. This includes traces in a local box of fixed physical size. The estimate comes from the conditional distribution of a single spatial link, control of spinors by plaquette holonomy, and a bound for the trace on large blocks. It uses no Hamiltonian time matching and no assumption that different plaquettes are independent.

The decay has a matching logarithmic exponent. In a fixed physical Dirichlet box, put $x=s/b^2$ and let $1+\beta_s+\beta_t=x^{o(1)}$. Fix a compact connected Lie group, the finite-dimensional unitary Wilson action representation, and a finite-dimensional unitary charged particle representation without invariant vectors. Then
$$
 \frac{\log(-\log\mathbb E F_s)}{\log x}\longrightarrow\frac35 .
$$
Nearly flat mesoscopic spatial cubes supply the lower estimate. A deterministic rescaling to unit mean makes the observable converge to zero in probability, with divergent higher moments. The expected fraction of low charged eigenmodes has the corresponding tail exponent $3/2$ under explicit box-size conditions. [Two-sided estimates, moment growth and the counterterm obstruction](rare-cubes.md)

The conditional estimate also reaches the physical gauge-transfer spectrum. At isotropic coupling with $B=x^{o(1)}$, the centered heat-trace vacuum vector normalized to unit variance puts vanishing spectral weight on $[0,x^\eta/a]$ for every $0<\eta<3/5$, where $a=b$ is the time step. In physical units this threshold equals $s^\eta b^{-(1+2\eta)}$. A uniform conditional bound controls the correlation with any test on another slice, already one step apart. This establishes spectral escape for this observable; the lowest physical excitation of the full theory remains undetermined. [Positive-time proof and normalization](positive-time.md)

## Observable and quantitative result

In a finite four-dimensional periodic Wilson lattice, choose one time slice. The spatial and temporal plaquette coefficients in the exponent are $\beta_s,\beta_t\ge0$ multiplying $\tfrac12\operatorname{ReTr} U_p$. Take extents at least three, normalized product Haar before tilting, and write $B=1+4\beta_s+2\beta_t$. Let $\Lambda$ be a finite embedded subset of the spatial cubic lattice, with zero extension for Dirichlet boundary conditions. Its volume in this note is $V=b^3|\Lambda|$. Small and large cubes used below must fit in an unwrapped spatial neighborhood of $\Lambda$, or tile the ambient torus with the stated period. The Dirichlet test graph itself embeds in the ordinary cubic lattice, so its returning walks have no spatial winding. This permits a fixed physical test box padded inside an arbitrarily large Wilson lattice.

The auxiliary spatial operator acts on two-component site spinors with counting inner product:
$$
 A_U=b^{-2}(6I-\mathcal A_U),\qquad
 (\mathcal A_U f)(x)=\sum_{y\sim x}U_{xy} f(y),\quad U_{yx}=U_{xy}^{*}.
$$
Its form is $b^{-2}\sum_{e=(x,y)}\|f(x)-U_{xy}f(y)\|^2$, counting unordered edges once, including edges to zero boundary values. Its local heat trace is $F_s(U)=\operatorname{Tr}\exp(-sA_U)$ at fixed diffusion time $s>0$ (length squared). A gauge rotation unitarily conjugates $A_U$. Expanding its exponential shows that $F_s$ sums closed walks in $\Lambda$ with parallel transport in the fundamental representation. The superscript-free trace sums over all site and color indices. [Graph connection semigroups, Güneysu, Milatovic and Truc](https://arxiv.org/abs/1306.6062)

For **every even block side $m\ge2$** satisfying the embedding condition,
$$
 \frac{\mathbb E F_s}{V}
 \le \frac{2^{5/2}}{s^{3/2}}
 \left[
 2^{-(m/2)^3}
 +\exp\!\left(-\frac{s}{2b^2(5m^2+65536B)}\right)
 \right].
$$
The constants are uniform in the remaining spatial volume and in the number of time slices. For $x=s/b^2\ge1$, choose $m=2\lceil x^{1/5}\rceil$. Then the right side is at most
$$
 2^{7/2}s^{-3/2}\exp[-c\min(x^{3/5},x/B)]
$$
with, for example, $c=1/132000$. Indeed $m^2\le16x^{2/5}$ and $(m/2)^3\ge x^{3/5}$. The physical padding for this choice is of order $b^{3/5}$ at fixed $s$. In the isotropic case $B=1+6\beta$. Any $B=O(b^{-2+\epsilon})$ with fixed $\epsilon>0$ yields faster-than-polynomial suppression. The weaker condition $b^2 B\to0$ gives vanishing with the displayed rate. [Proof from the original Wilson density](wilson-law.md)

Since $0\le F_s/V\le2s^{-3/2}$ deterministically, the same collapse holds in every finite $L^p$ with $p\ge1$. Correlations with uniformly bounded insertions at other Euclidean times vanish by the first absolute moment. Uniform polynomial growth of those insertions and of a multiplicative renormalization is also allowed when the displayed exponent dominates $\log(1/b)$. A family of additive mass-squared counterterms $\mu_b$ multiplies this heat trace by $e^{s\mu_b}$. A nonzero limiting mean would require this multiplier to compensate at least the derived suppression. The estimate gives a necessary scale and leaves its sufficiency and any counterterm prescription open. The covariance after division by the squared mean at fixed positive physical separation also remains open. [Z4’s independent numerical scale and normalization review](../../z4/reviews/r6-heat/report.md)

For a fixed physical support volume, $\|e^{-sA_U}\|_{\rm op}\le F_s$ also bounds every heat-propagated source–sink matrix element between norm-bounded site spinors. The finite-period estimates are uniform in the temporal period. Sending that period to infinity in a fixed spatial Wilson box gives the same second-moment estimate in the discrete transfer vacuum, since the physical transfer is compact and positivity improving and its periodic trace selects its vacuum. Indeed, at fixed mesh the normalized transfer has top projection onto the vacuum and its periodic powers converge to that projection in trace norm (one may start from a trace-class power). Inserting the bounded multiplication operator $F_s^2$ therefore gives its vacuum expectation in the limit. The inequality $F_s^2\le 2Vs^{-3/2}F_s$ shows that the squared norm of the vector excited by the bare trace vanishes on the isotropic trajectories above, even before subtracting its mean. [Physical periodic trace](../periodic-time/README.md)

There is a complementary probabilistic statement about the lowest auxiliary eigenvalue in a fixed physical domain. If $N_m$ blocks meet $\Lambda$, then with probability at least $1-N_m2^{-(m/2)^3}$,
$$
 \lambda_{\min}(A_U)\ \ge\ [b^2(5m^2+65536B)]^{-1}.
$$
Take $(m/2)^3\ge\log_2(N_{\rm sites}/\delta)$ where $N_{\rm sites}$ is a deterministic upper bound on the number of blocks, such as $|\Lambda|$, to get confidence $1-\delta$. At $\beta\asymp\log(1/b)$ and fixed physical volume this gives order at least $1/(\beta b^2)$ with arbitrarily high polynomial confidence by choosing $m$ accordingly. It also bounds the expected number of eigenvalues in $[0,R]$ by $e^{sR}\mathbb E F_s$ for each fixed $R$. These eigenvalues refer to the charged spatial Laplacian in a gauge background. The Yang–Mills mass gap refers to vacuum excitations of the physical transfer Hamiltonian. Determining nonzero continuum vacuum correlations and a gap for those excitations remains open. [Earlier numerical studies of covariant Laplacians in Yang–Mills backgrounds](https://doi.org/10.1103/PhysRevD.71.114507) · [Clay problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Other representations and the Hamiltonian comparison

A single adjoint SU(2) holonomy leaves an axis fixed. Several based plaquettes restore the necessary lower bound. For each fixed compact connected Lie group, a finite-dimensional unitary particle representation without invariant vectors, and a fixed Wilson action representation, the same argument yields a group-dependent exponent with $B$ replaced by $C(1+\beta_s+\beta_t)^q$. This still gives faster-than-polynomial vanishing at polylogarithmic couplings. Trivial subrepresentations carry a deterministic ordinary heat trace. [Several-loop proof and adjoint check](representations.md)

For the continuous-time SU(2) Hamiltonian a separate, deterministic derivative estimate holds at **all** finite magnetic couplings. At the bare electric clock it gives $M_1(F_s/\sqrt V)\le C/(\beta s^2)$ uniformly in the spatial mesh. On the specified anisotropic time-matching sequences it bounds the raw positive-energy weight for the actual Wilson transfer. A bound on the fraction of spectral weight would also require a lower bound on the equal-time norm. The direct Euclidean law above supplies a stronger estimate on the entire trace when the temporal staple bound allows it. [Hamiltonian estimate and clocks](hamiltonian.md) · [Lean, controls and replay](execution.md)
