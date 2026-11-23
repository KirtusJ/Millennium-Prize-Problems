# Time decay for the interacting SU(2) Wilson regulator

Director B4 · November 22, 2026 · From Prephysical Hypotheses to Physical Models, Millennium Prize Problems subproject

On a spatial three-torus of side $L\ge2$, consider the four-dimensional Wilson measure with spatial and temporal plaquette couplings $\beta_s,\beta_t\ge0$. If both $\tanh\beta_s$ and $\tanh\beta_t$ are at most $1/20$, the vacuum-normalized transfer operator on centered gauge-invariant states has norm at most $1/3$, uniformly in $L$. This gives a lattice energy gap of at least $\log 3$ per step. At a fixed positive physical time, the same estimate forces every connected matrix element between uniformly norm-bounded states to vanish as the time spacing tends to zero. A nontrivial Yang–Mills scaling limit with finite-energy excitations therefore requires a different trajectory. Strong-coupling exponential clustering is classical. This calculation gives explicit constants and tests a boundary of the single-link method. [Osterwalder and Seiler](https://doi.org/10.1016/0003-4916(78)90039-8) · [Program transfer normalization](../README.md) · [Clay problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## From the Wilson density to time decay

Use open time slabs, periodic space, and product Haar reference measure on positively oriented links. Each face contributes $\exp(\beta_p\operatorname{ReTr}(U_p)/2)$, with the appropriate one of the two couplings. For a bounded real observable $F$, let $\delta_e F$ be its maximal oscillation when only link $e$ changes. Let $C_{ef}$ be the supremum total variation distance between conditional laws at $e$ when only $f$ changes. Use the convention $\mathrm{TV}=\sup_A|\mu(A)-\nu(A)|$.

If a normalized likelihood ratio $X$ lies in $[a,b]$ with $0<a< b$, then $a\le1\le b$. Applying the chord bound to $(X-1)_+$ and taking expectations gives $\mathrm{TV}\le (b-1)(1-a)/(b-a)$. Writing $b=ak^2$, this is at most $(k-1)/(k+1)$, or $\tanh(\log(b/a)/4)$. Clearing the positive denominators leaves $(k+1)(ak-1)^2\ge0$. If the ratio is constant the laws coincide. For a shared Wilson face the change in its log weight is in $[-2\beta_p,2\beta_p]$ as a function of $U_e$. The normalization adds a constant. Its contribution to conditional variation is therefore at most $\tanh\beta_p$. Replacing the affected face factors successively and applying the triangle inequality handles shared faces with multiplicity. Write $s=\tanh\beta_s$ and $t=\tanh\beta_t$. Every unweighted row sum is at most $18\max(s,t)\le9/10$. [Cohen and Fausti, Corollary 5.2.1](https://arxiv.org/pdf/2309.02413)

Tilt the finite-volume measure by $\exp(\epsilon G)$ for a bounded real $G$. Each conditional law changes by at most $\tanh(|\epsilon|\delta_fG/4)\le |\epsilon|\delta_fG/4$. The Dobrushin comparison theorem for the discrete metric on each link applies to the two finite Gibbs measures. In its summability hypothesis $C^k\mathbf1\to0$ by the unweighted row bound. Dividing the expectation difference by $|\epsilon|$ and differentiating at zero yields

$$
|\operatorname{Cov}(F,G)|\le \tfrac14\sum_{e,f}\delta_e F\, D_{ef}\,\delta_f G,
\qquad D=\sum_{k\ge0}C^k .
$$

Boundedness justifies differentiation within the finite probability integral. The comparison uses the influence matrix of the original measure. [Rebeschini and van Handel, Corollary 2.6 and p. 9](https://web.math.princeton.edu/~rvan/dobrushin130819.pdf)

Anchor each positive link at its starting time $u_e$. For $R>1$ use $w_e=R^{u_e-n}h_e$, taking $h_S=1$ on spatial links and $h_T=h$ on temporal links. The following matrix acting on $(1,h)^T$ bounds the rows of $Cw$ after removing the factor $R^{u_e-n}$.

$$
A(R)=\begin{pmatrix}12s+t(R+R^{-1}) & 2t(1+R^{-1})\\
6t(1+R)& 6t\end{pmatrix}.
$$

A spatial link belongs to four spatial faces, each with three remaining spatial links. Its two time faces contain a parallel spatial link at offsets $+1$ and $-1$, respectively, and two temporal links in each face anchored at offsets $0$ and $-1$, respectively. A temporal link belongs to six time faces. Each contains one other temporal link at the same time and two spatial links at offsets $0$ and $+1$. At an open time end some faces disappear. For $L=2$ different incidences can refer to the same neighbor, for which the successive-factor upper bound still applies. A periodic time seam would invalidate this choice of linear time coordinate; the argument takes the long-slab limit with open ends.

At $R=3$, $h=26/15$ and $s=t=1/20$, the two normalized row bounds are $449/450$ and $129/130$. Each decreases if either coupling decreases. Consequently $Cw\le (449/450)w$, and every partial sum $\sum_{k=0}^N C^kw$ is at most $450w$. For $F$ on spatial links at time zero and $G$ on spatial links at time $n\ge0$, one has $\delta_fG\le \|\delta G\|_\infty w_f$ throughout the slab. This proves

$$
|\operatorname{Cov}(F,G)|\le
\frac{450}{4}\,3^{-n}\left(\sum_e\delta_e F\right)\max_f\delta_f G .
$$

The times can be translated together anywhere in the slab. Tilting by $R=4$ at the same coupling endpoint gives incompatible inequalities for $h$ in this matrix. The optimal physical decay rate remains undetermined by that test.

## From bounded time-slice observables to all physical vectors

At fixed finite $L$ the gauge-invariant transfer kernel integrates over a compact product of link groups. The kernel is continuous, pointwise strictly positive, symmetric and compact as an integral operator. In temporal gauge its kinetic part convolves each spatial link by the class function $\exp(\beta_t\operatorname{Tr}(U)/2)$. This function is positive definite: its exponential series is a nonnegative sum of characters of tensor powers of the fundamental representation, including the constant term. Multiplying on both sides by the positive half spatial Wilson density and projecting to the invariant subspace gives a nonnegative self-adjoint transfer. This also covers $\beta_t=0$, for which zero transfer eigenvalues can occur. For the physical kernel the temporal link integrations implement the gauge projection. [Lüscher, transfer construction and Proposition 1](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf)

Strict kernel positivity gives a simple leading eigenvalue and a strictly positive ground function $\Omega$ by the compact positive-kernel theorem. The positive open-end boundary weights overlap with $\Omega$. Taking each endpoint to infinity at fixed insertion times therefore gives the vacuum correlations of $T$, normalized by the leading eigenvalue. For a centered real continuous gauge-invariant multiplication observable $F$, the bound above now gives $\langle F\Omega,T^nF\Omega\rangle\le K_F 3^{-n}$ at all $n$. The positive spectral measure of this vector has no mass on $(1/3,1]$, since its mass above any $r>1/3$ is at most $K_F(3r)^{-n}$. The continuous gauge-invariant multipliers are dense for the vacuum-weighted measure on the compact spatial configuration space modulo gauge. Multiplication by $\Omega$ identifies that space with the physical Hilbert space, and centering projects onto the vacuum complement. Taking complex spans and using closedness of the kernel of the spectral projection yields $\|T|_{\Omega^\perp}\|\le1/3$. [D4’s checked spectral-support implication](../../spectral-support/README.md)

For arbitrary centered $v_a,w_a$ of uniformly bounded norm at each spacing and volume, $|\langle v_a,T_a^{N_a}w_a\rangle|\le \|v_a\|\|w_a\|3^{-N_a}$. Thus even growing-support or cutoff-dependent observables of bounded Hilbert norm have zero connected limit if $N_a=\lceil\tau/a\rceil$ with fixed $\tau>0$ and $a\downarrow0$. The finite-volume energy bound in that clock is $(\log3)/a$. This result treats SU(2) in a specified strong bare-coupling rectangle. The required nonzero continuum correlations, ultraviolet construction, physical normalization and quantifier over compact simple groups remain open. [A4’s nontriviality criterion](../../observable-normalization/README.md) · [Jaffe and Witten, §4](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## A lower bound on the actual influence matrix

Consider isotropic $\beta$. At a bulk link on a torus with each period at least three, the other edges in its six incident plaquettes form six disjoint triples. In each oriented loop use trace invariance under cyclic permutations and inversion to write the trace as $\operatorname{ReTr}(U_e S_p)$ with $S_p$ the three-link staple. Let $f$ be any of the 18 neighbors. Set the other two links in its triple to the identity. Independently prescribe the five remaining staples to be

$$I,\ -I,\ I,\ \operatorname{diag}(\omega,\bar\omega),\
\operatorname{diag}(\bar\omega,\omega),\qquad \omega=e^{2\pi i/3}.$$

Their matrices sum to zero. Each assignment is realized by varying one link of its triple, taking its inverse when the orientation requires it. Switching $f$ from $I$ to $-I$ therefore gives conditional densities proportional to $e^{\pm\beta x}$ relative to Haar, with $x=\operatorname{Tr}(U_e)/2$. Normalizers agree by Haar symmetry. These configurations are in the support of the Wilson measure; continuity also gives the same lower bound for essential suprema. The maximizing environments in $C_{ef}$ are allowed to depend on $f$.

Under normalized Haar measure $x$ is one coordinate on the unit three-sphere. Its density is $2\sqrt{1-x^2}/\pi$ on $[-1,1]$, hence $\mathbb E|x|=4/(3\pi)$. Testing on $x>0$ attains the total variation of the two conditional densities and gives

$$C_{ef}\ge d(\beta)=
\frac{\mathbb E\sinh(\beta |x|)}{\mathbb E\cosh(\beta x)}.$$

This is the mean of $\operatorname{sign}(x)$ under the positive tilt. Its derivative is the covariance of $\operatorname{sign}(x)$ and $x$ under that tilt, nonnegative by taking half the mean of the product of their differences on two independent samples. For $0\le\beta<\sqrt 2$, use $\sinh y\ge y$ at $y\ge0$ and $\cosh\beta\le1/(1-\beta^2/2)$ term by term, since $(2k)!\ge2^k$. Thus $d(\beta)\ge [4\beta/(3\pi)](1-\beta^2/2)$. At $\beta=2/15$, $\pi<22/7$ yields $18d(\beta)>12488/12375>1$. Monotonicity extends the strict row lower bound to every $\beta\ge 2/15$.

All rows on the four-torus meet this lower bound. Given any positive diagonal weight, choose a link where the weight is smallest. The ratio $(Cw)_e/w_e$ there exceeds one. Hence the actual one-link total-variation influences cannot satisfy a strict weighted row contraction in that regime. The conclusion concerns this criterion; it supplies no thermodynamic transition or upper bound on the mass gap. For open time slabs the same construction proves failure of the unweighted row test at interior links. The interval between the sufficient and obstructed regimes is unresolved by these estimates.

## Verification

Lean checks the likelihood-ratio algebra, a partial Green-series estimate on arbitrary finite sets, the two time-tilt tests, the arithmetic of the influence lower bound, the minimum-weight obstruction, and the scalar vanishing limit. The Wilson conditional laws, the comparison theorem, Haar integrals, compact-kernel argument and density of time-slice vectors are analytic parts of the proof. [Lean source](WilsonInfluence.lean) · [Replay and observed controls](execution.md)
