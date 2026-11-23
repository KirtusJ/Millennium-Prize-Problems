# A relative bound on ordered Gibbs probabilities

Consider the positive physical Wilson transfer $T$ in a finite periodic spatial box. Use the periodic time law with $2n$ steps, physical step $a_t>0$ and period $\tau=2na_t$. Integrating the two slabs gives the joint full-slice density $U(x,y)^2$ against spatial Haar probability on gauge orbits, with $U=T^n/\sqrt{\operatorname{Tr}T^{2n}}$. The continuous kernel is real, symmetric and pointwise positive. The operator is positive, compact and has Hilbert–Schmidt norm one. Write $s_i=\sigma_i(U)$ in decreasing order, so $\rho_i=s_i^2$. A common positive rescaling of $T$ cancels from $\rho_i$. [Finite Wilson transfer, Lüscher](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf) · [Half-period normalization](../paired-slice-spectrum/spectrum.md)

## Projecting one endpoint at a time

Use a measurable partition into $D$ positive-measure orbit cells, positive spatial half-weight $M$, normalized vectors $\phi_i=M1_{C_i}/\|M1_{C_i}\|_2$, their span projection $P$ and $Q=I-P$. In this basis put $C=PUP$ and $B_{ij}=(\int_{C_i\times C_j}U^2)^{1/2}$. Suppose that for fixed opposite endpoint the log of $F(x,y)=U(x,y)/(M(x)M(y))$ has essential oscillation at most $z_i$ as the varying endpoint runs over $C_i$. For the Wilson action $z_i=\beta_t\delta_i$ suffices when $\delta_i$ bounds the cell’s gauge-orbit sum-of-link-chords diameter. A stronger half-kernel estimate can be inserted directly. Write
$$
 h_{ij}=\operatorname{sech}((z_i+z_j)/2),\quad a_i=\tanh(z_i/2),\quad
 b=\|B\|,\quad \ell=\|h\circ B\|,\quad e=\|(1-h)\circ B\|,\quad
 t=\|\operatorname{diag}(a_i)B\|.
$$
Matrix norms here are operator norms. Nonnegative masks $h_{ij}$ may be lowered and the $a_i$ raised within $[0,1]$. The cell-pair mean and root-mean-square inequality gives $h\circ B\le C\le B$ entrywise. Thus $\|B-C\|\le e$ and $\ell\le s_1\le b$. For the upper bound on $s_1$, bound each block bilinear form of $U$ by its Hilbert–Schmidt norm $B_{ij}$ times the two local vector norms, then apply the matrix norm to their vectors. The other comparisons use monotonicity of the operator norm for entrywise nonnegative matrices. These steps do not assume $B$ positive semidefinite. [Cell means and endpoint oscillations](../paired-slice-spectrum/spectrum.md)

For fixed $y$, the vector $u(x)=U(x,y)$ on $C_i$ satisfies
$$
 \langle\phi_i,u\rangle\ \ge\ \operatorname{sech}(z_i/2)\|u\|_{L^2(C_i)}.
$$
Indeed, the mean of a positive variable in $[m,M_0]$ divided by its root mean square is at least $2\sqrt{mM_0}/(m+M_0)$. Apply this to $F(\cdot,y)$ with the normalized $M^2$-weighted cell measure. Pythagoras gives $\|(Qu)|_{C_i}\|\le a_i\|u\|_{L^2(C_i)}$. Integrating its square for $y\in C_j$ bounds each block Hilbert–Schmidt norm of $QU$ by $a_iB_{ij}$. The same block comparison proves $\|QU\|\le t$. By self-adjointness $\|PUQ\|\le t$.

Put $c_i=\sigma_i(PUP)$, padding by zeros. The two positive differences
$$
 U^*U-U^*PU=(QU)^*(QU),\qquad
 PUU^*P-(PUP)(PUP)^*=(PUQ)(PUQ)^*
$$
each have norm at most $t^2$. The intermediate operators $(PU)^*(PU)$ and $(PU)(PU)^*$ have identical ordered nonzero eigenvalues with multiplicity. Compact min–max, with zeros appended if necessary, gives $0\le s_i^2-c_i^2\le 2t^2$. Because $PU$ has rank at most $D$, $s_{D+1}\le\|U-PU\|\le t$. Singular-value perturbation gives $|c_i-\sigma_i(B)|\le e$. Thus, whenever $\ell>0$,
$$
 \left((\sigma_i(B)-e)_+/b\right)^2\le\frac{\rho_i}{\rho_1}
 \le\min\left\{1,\frac{(\sigma_i(B)+e)^2+2t^2}{\ell^2}\right\}.
$$
For each $i>D$ the upper bound improves to $\min(1,t^2/\ell^2)$. The sum over all unresolved levels is a different observable. If a conservative mask makes $\ell=0$, use the trivial upper bound one. At uniform $z$, $\ell/b\ge\operatorname{sech}z\ge1-z^2/2$, $e/b\le1-\operatorname{sech}z$, and $t/b\le\tanh(z/2)\le z/2$. Both squared endpoints are within $O(z^2)$ of $(\sigma_i(B)/b)^2$ uniformly in $b$ and $i$ for small $z$. A square-root transfer ratio itself can have first-order uncertainty near zero. [Mirsky, singular-value perturbation](https://doi.org/10.1093/qmath/11.1.50) · [A4’s resolved-level estimate](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/ec15bb2/yang-mills/observable-normalization/replica-gap/paired-ritz/README.md)

## Errors in the observed table

Suppose a symmetric normalized table has root matrix $\widehat B$ and $\|B-\widehat B\|\le\eta\widehat b$ with $\widehat b=\|\widehat B\|$. If $\eta<1$ and $\widehat r_i=\sigma_i(\widehat B)/\widehat b$, then the true raw ratio $\sigma_i(B)/b$ belongs to
$$
 [(\widehat r_i-\eta)_+/(1+\eta),\ \min\{1,(\widehat r_i+\eta)/(1-\eta)\}].
$$
This follows by perturbing each singular value separately. Insert the left and right endpoints in the corresponding uniform bounds. A signed operator error allows this uniform calculation for any supplied geometry. For different masks a sufficient stronger input is $\|\,|B-\widehat B|\,\|\le\eta\widehat b$, with entrywise absolute value. Then the norm of every masked difference with weights in $[0,1]$ is at most $\eta\widehat b$, by entrywise domination. Replace $\ell$ by its measured lower value minus that allowance, and raise $b,e,t$ by the allowance when used as upper bounds. Enlarge the singular-value intervals as well. The calculator intersects the masked bounds with the uniform ones. Its signed-error guarantee must apply to the chosen estimator, including any symmetrization. [Rational calculator](relative.py)

For $S$ independent equilibrium histories and a fixed $D$-cell partition, take one opposite pair per history. With probability at least $1-\alpha$, the Frobenius root error of the symmetrized frequency table is at most $\sqrt{[D^2\log(S+1)+\log(1/\alpha)]/S}$. The multinomial type bound controls relative entropy and hence the squared root error. Symmetrization by averaging the counts and their transpose contracts the root distance to the symmetric target. Frobenius error dominates the operator norm of the entrywise absolute error. Divide the displayed bound by the observed $\widehat b$ to obtain a simultaneous relative allowance. Since $\|\widehat B\|_F=1$, $\widehat b\ge D^{-1/2}$. For finite $D$ this gives a finite, potentially very large, sufficient sample size. Correlated histories need their own error analysis. [Multinomial argument](../paired-slice-spectrum/spectrum.md)

## Passing a certified gap to a vacuum theory

A ratio bound $R_k\le e^{-m\tau_k}$ gives $\|(T_k/\lambda_{1,k})^{2n_k}|_{\Omega_k^\perp}\|\le e^{-m\tau_k}$ at each regulator. The period is physical. To pass to a proposed reconstructed theory, for example assume $\tau_k\to\tau>0$, separating vacuum and excited states at each cutoff, and dense centered limit test vectors with convergent squared norms and vacuum two-time quadratic forms at that same physical lag. Their limiting forms satisfy $\langle v,e^{-\tau H}v\rangle\le e^{-m\tau}\|v\|^2$. Density in the entire vacuum complement and the spectral theorem exclude spectrum below $m$ there. Density in a smaller observable sector gives only that sector’s bound. Thermal histogram convergence alone supplies neither a reconstructed vacuum theory nor these vacuum limits. [D4’s spectral-support lane](../../spectral-support/README.md) · [Jaffe and Witten’s existence and gap requirements](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)
