# Exact time-moment completion with an unknown vacuum

The data are Hermitian matrices $C_j=J^*T^jJ$, $j=0,\ldots,d$, for finitely many probes on one clock. A proposed positive energy gap $\Delta$ gives $q=e^{-\tau\Delta}<1$. A compatible transfer model is a positive contraction whose measured spectrum lies in $[0,q]\cup\{1\}$. Its Gram matrix at $1$ is $V$. This model reproduces the measured entries and imposes no field algebra or locality axiom. The interval alone is the classical truncated matricial Hausdorff moment problem. Below the isolated vacuum is kept as an unknown matrix. [Truncated matrix moment problem](https://intlpress.com/site/pub/files/_fulltext/journals/maa/2012/0019/0001/MAA-2012-0019-0001-a002.pdf) · [Block quadrature](https://www.math.kent.edu/~reichel/publications/blkagauss.pdf) · [Lattice variational correlators](https://arxiv.org/abs/0902.1265)

## The interval construction at odd order

For data $S_0,\ldots,S_{2r+1}$ and $0\le l<q$, form $H=(S_{i+j})$, $K=(S_{i+j+1})$ for $0\le i,j\le r$. A realization supported on $[l,q]$ exists exactly when $lH\preceq K\preceq qH$. Necessity follows by integrating each vector polynomial squared against the two linear endpoint factors.

For sufficiency, these inequalities imply $H\succeq0$, $K\succeq0$ and $\ker H\subseteq\ker K$. Give vector polynomials through degree $r$ the Gram form $H$ and divide by its null space. The form $K$ induces a selfadjoint operator $A$ on this finite Hilbert space with $lI\preceq A\preceq qI$. For monomials of degree below $r$, $A[u^iv]=[u^{i+1}v]$ by pairing with every monomial in $H$. Embed each initial probe as its constant polynomial using $B$. Splitting powers between the two arguments reproduces $S_k=B^*A^kB$ through degree $2r$. Pair the two degree-$r$ monomials using $K$ to obtain degree $2r+1$. The model has dimension $\operatorname{rank}H$, minimal for this $S$ since any representation contains the polynomial probe Gram. No inverse of a singular Gram matrix enters. [Checked Gram descent, selfadjoint representative and power identities](FiniteReadings.lean)

For the unknown vacuum put $S_j=C_j-V$ and require $V\succeq0$. Fixing $V=0$ is justified when the probes are known to be orthogonal to the entire vacuum sector. If an independent rank bound on that sector is imposed, add the corresponding rank constraint on $V$. A physically allowed test vector may excite only a proper part of the spectrum.

The maximum feasible vacuum Gram for this odd-order test can be found without optimizing over matrices. In the raw lower pencil $K_C-lH_C$, change the polynomial basis to $1,(1-u),u(1-u),\ldots,u^{r-1}(1-u)$. If this raw pencil fails positivity, no $V\succeq0$ works. Otherwise write it in this basis as $\left(\begin{smallmatrix}A&B\\B^*&D\end{smallmatrix}\right)$. Subtracting a vacuum changes only $A$, by $-(1-l)V$. Positivity implies $B$ kills $\ker D$. Completing the square on $\operatorname{ran}D$ gives $V\preceq V_{\max}=(A-BD^\dagger B^*)/(1-l)$. The upper pencil $qH_S-K_S$ increases by the positive vacuum contribution $(1-q)V$ in the same corner. Hence $V_{\max}$ passes both pencils whenever any vacuum does. At $r=0$ the trailing block is empty. The code computes the quadratic correction using independent principal pivot indices. [Exact implementation](moments.py)

A finite Hamiltonian has injective $e^{-\tau H}$. For fixed $V$ and $l=0$, exact finite-energy realization is equivalent to $\ker H=\ker K$ in addition to the two pencil tests. A larger shifted-form kernel forces a zero-transfer atom for the corresponding polynomial state. With an unspecified vacuum the largest $V$ at $l=0$ can create such an atom even when another completion has none. Equivalently, an injective realization of these finite readings exists if the two-pencil test succeeds for some $l>0$ with $l<q$. For example $C_0=1,C_1=1/2,q=1/2$ admits a finite energy with zero vacuum weight. Maximizing $V$ at $l=0$ instead gives equal masses at 0 and 1. The code accepts a positive lower cutoff when finite energies are required.

## Even order and the sharp transfer threshold

At $d=2r$, $r\ge1$, first require the raw Hankel matrix $H_r(C)=(C_{i+j})_{0\le i,j\le r}$ to be positive. Set $D_j=C_j-C_{j+1}$. Apply the odd interval construction to these $2r$ difference readings with $r$ block rows, using the same $[l,q]$. These conditions are necessary and sufficient.

Indeed $D$ measures $(1-u)\,d\mu$, so no vacuum enters it. Let $A,B$ realize $D$. Reweight the inner product by $(I-A)^{-1}$, which is positive and bounded since $q<1$. This gives excited moments $B^*A^j(I-A)^{-1}B$. Set $V=C_0-B^*(I-A)^{-1}B$. For each vector $c$ and every polynomial $p$ of degree at most $r-1$, the raw Gram applied to $c-(1-u)p(u)$ gives
$$
 c^*C_0 c\ \ge\ 2\operatorname{Re}\langle Bc,[p]\rangle-\langle[p],(I-A)[p]\rangle.
$$
Taking the supremum over this quotient space gives $V\succeq0$. Every actual vacuum is also bounded above by $V$, since the same raw square includes its contribution $c^*V_{\rm actual}c$. The constructed model agrees at zero time and on every difference, so it agrees at every measured time. For compatible nonconstant data with $l=0$, the greatest generalized eigenvalue of the shifted difference form relative to its Gram, restricted to its range, is the **smallest feasible $q$**. A sole vacuum permits every $q>0$. If the measured spectrum includes zero transfer, that point is allowed in the compact-transfer test.

An independent odd-order extremal construction uses $D_j=C_{j+1}-C_{j+2}$ through $j=2r-1$ after checking raw admissibility on $[0,1]$. These data measure $u(1-u)\,d\mu$. In the nonzero finite Gram quotient its compressed operator $A$ has $0<A<I$ because this weight vanishes at both endpoints. Require its top eigenvalue to be at most $q$. Reweight its spectral Gram by $[A(I-A)]^{-1}$. Add endpoint weights
$$
 V_1=C_1-B^*(I-A)^{-1}B,\qquad
 V_0=C_0-C_1-B^*A^{-1}B .
$$
Both are positive by completing squares in the original measure, using respectively $u|c-(1-u)p|^2$ and $(1-u)|c-up|^2$. Here the squared notation denotes the corresponding vector quadratic form under the matrix measure. The zeroth and first readings then agree, and the differences from index one recover all later readings. This supplies the sharp odd-order upper transfer endpoint under the compact-transfer convention. At degree one, masses $C_1$ and $C_0-C_1$ at 1 and 0 suffice. A positive lower transfer cutoff uses the preceding odd two-pencil test. [Independent exact endpoint constructions and controls](check_moments.py)

## What rejection and acceptance establish

For the even upper pencil and a polynomial polarization $p_i$, write $\psi=\sum_i T^i Jp_i$. Its excess over a candidate threshold is
$$
 D=\langle\psi,(T-q)(I-T)\psi\rangle,\qquad
 \mu_\psi((q,1))\ \ge\ \frac{4D}{(1-q)^2}
$$
when $D>0$, since the multiplier is nonpositive outside the open interval and at most $(1-q)^2/4$ inside. If the measured matrices have operator-norm errors $\epsilon_j$, the error in $D$ is at most
$$
 \sum_{i,j}\|p_i\|\|p_j\|
 [\epsilon_{i+j+2}+(1+q)\epsilon_{i+j+1}+q\epsilon_{i+j}].
$$
Use a positive lower confidence or deterministic bound on the excess before asserting a rejection in noisy data. The exact-rational implementation treats its input as exact.

For an actual limiting contraction and a fixed $q$, passing the tests at every order excludes all measured weight on $(q,1)$. For a scalar polarization and $q<a\le b<1$, a normalized monomial of high order isolates $[a,b]$. Its adverse contribution from $[0,q]$ is at most $q(q/a)^n$ times total mass. On $[a,b]$ the contribution is at least $(a-q)(1-b)$. The even-order tests supply the even exponents $n=2k$. Their geometric remainder tends to zero. Odd exponents can also be obtained from the odd weighted tests. A countable exhaustion covers $(q,1)$. Equivalently, every finite truncation admitting a compact-support realization gives an all-order supported subsequential limit by compactness and polynomial uniqueness. Interpreted across a dense family, the tests characterize a gap above the full vacuum sector. Finite success alone leaves other compatible spectra. [Formal interval exclusion and finite margin](FiniteReadings.lean)
