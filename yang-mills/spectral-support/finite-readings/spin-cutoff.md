# Certified spin truncation for the whole low-energy subspace

At fixed couplings on a periodic cubic spatial box, cutting every $SU(2)$ link to Peter–Weyl labels at most $J$ gives a genuine finite-dimensional variational problem. Its first gap approximates the full Hamiltonian’s first gap with a computable two-sided absolute error. The per-link proof controls the entire low-energy subspace and requires no assumed lower bound on the first gap. Related truncation work controls quantum-number growth and approximation of spectrally isolated eigenstates. Here the quadratic electric Casimir and fundamental one-label hopping give a direct stationary estimate. [Tong, Albert, McClean, Preskill and Su](https://arxiv.org/abs/2110.06942)

## A single-link tail

Use the [punctured-link decomposition](loops.md), with $\gamma=\kappa/4$, $w=4\lambda$ and $E_0$ in the shifted energy origin. Write $R_{e,k}$ for the link projector onto labels $n\ge k$, $R_{e,0}=I$, and $P_s=\mathbf1_{[E_0,E_0+s]}(H)$. A fundamental matrix coefficient times a label-$n$ matrix coefficient has only labels $n-1,n+1$ by the $SU(2)$ tensor product rule, including the single label $1$ for $n=0$. Inversion gives the dual fundamental, equivalent for $SU(2)$. Consequently $R_{e,k}W_e=R_{e,k}W_e R_{e,k-1}$ for $k\ge1$.

On $\operatorname{ran}R_{e,k}$, $A=-\gamma\Delta_e+H_{\rm out}-E_0\ge\gamma k(k+2)$. On $\operatorname{ran}P_s$, $B=H-E_0$ has $0\le B\le s$. The map $X=R_{e,k}|_{\operatorname{ran}P_s}$ satisfies
$$
 AX-XB=-R_{e,k}W_e R_{e,k-1}|_{\operatorname{ran}P_s}.
$$
The finite-box spectral subspace is finite dimensional and its vectors are smooth. The link projector preserves the free operator domain. For $\gamma k(k+2)>s$, differentiate $e^{-tA}Xe^{tB}$ and integrate from zero to infinity. Its norm vanishes at infinity and the integral of the norm of the derivative is at most $\|AX-XB\|/[\gamma k(k+2)-s]$. This step avoids a multiplicity factor for low states. [Sylvester identity and spectral separation](https://doi.org/10.1112/S0024609396001828)

Define $t_0=1$. Before the denominator is positive take $t_k=t_{k-1}$. Afterwards take
$$
 t_k=t_{k-1}\min\!\left(1,\frac{w}{\gamma k(k+2)-s}\right).
$$
Nested projections and the preceding norm bound give $\|R_{e,k}P_s\|\le t_k$ for every edge. At $s=0$ the simpler bound $2(16g)^k/[k!(k+2)!]$ follows by taking the product of all ratios and $g=\lambda/\kappa$. For fixed positive $s,w,\gamma$ the recurrence gives $\log t_k\le-2k\log k+O(k)$ as $k\to\infty$. When $w=0$ the recurrence cuts off exactly beyond the energy threshold. [Formal product calculation](FiniteReadings.lean)

## From link tails to ordered Ritz levels

Let $N_e,N_p$ be the numbers of links and faces. The joint projector $P=\prod_e(I-R_{e,J+1})$ commutes with gauge transformations and the electric kinetic operator. Its orthogonal complement is bounded in projection order by $\sum_e R_{e,J+1}$. Thus $\|(I-P)P_s\|^2\le h=N_e t_{J+1}^2$. Take $h<1$, so projection preserves the dimension of each low-energy trial subspace. Denote by $E_i^J$ the ordered physical Ritz levels of $PHP$ on its range within the Gauss-law space.

For a normalized $\psi$ in the span of the first $i+1$ physical eigenvectors with $E_i-E_0\le s$, the omitted contribution from the projected energy origin is bounded by
$$
 |\langle(I-P)\psi,(H-E_i)\psi\rangle|\le sh .
$$
Both $\psi$ and $(H-E_i)\psi$ lie in $\operatorname{ran}P_s$, and the latter has norm at most $s$. For the kinetic part there is zero cross term between $P$ and $I-P$. For one face multiplier, partition $I-P$ orthogonally by the first edge whose label exceeds $J$ in a fixed ordering. An exterior edge cannot contribute to the cross term with $P$. At an incident edge the transition must start at label $J+1$ and finish at $J$. The two vector norms are bounded by $t_{J+1}$ and $t_J$ because all the other label projectors commute with those for this edge. There are four edges and the multiplier has norm at most $\lambda$. Therefore
$$
 |\langle P\psi,H(I-P)\psi\rangle|
 \le 4\lambda N_p t_J t_{J+1}.
$$
Expand $\langle P\psi,(H-E_i)P\psi\rangle$, use $\langle\psi,(H-E_i)\psi\rangle\le0$, and divide by $\|P\psi\|^2\ge1-h$. Min–max on this projected trial subspace and the ordinary Ritz lower comparison give
$$
 0\le E_i^J-E_i\le
 \epsilon_J(s)=\frac{sh+4\lambda N_p t_J t_{J+1}}{1-h}.
$$
The reference energy cancels here. One may use the tighter tail and $s=0$ for the vacuum. In particular, for $\Delta_J=E_1^J-E_0^J$ the interval
$$
 \Delta_J-\epsilon_J(s)\ \le\ \Delta\ \le\ \Delta_J+\epsilon_J(0)
$$
is valid whenever $E_1-E_0\le s$ and the stated denominators are positive. An energy computed numerically needs its own error enclosure before entering these bounds. A certified Ritz lower endpoint exceeding the truncation error would certify a finite-box lower gap.

At every fixed coupling a volume-independent $s$ for the first gap is available from the upper endpoint of the previously established nonzero [adjoint band](../adjoint-band/). At weak magnetic coupling one can use $7\kappa/2$. Since $N_e=N_p=N$ on cubic tori, for every $\eta>0$ it suffices asymptotically to take
$$
 J=\left\lceil(1/4+\eta)\frac{\log N}{\log\log N}\right\rceil .
$$
Indeed both $Nt_{J+1}^2$ and $Nt_Jt_{J+1}$ are at most $\exp(\log N-4J\log J+O(J))$, which tends to zero. At finite $N$ use the displayed recurrence and verify $h<1$ directly. The one-link cutoff dimension is $\sum_{n=0}^J(n+1)^2$ before gauge reduction. No polynomial cost bound for diagonalizing the many-link Hamiltonian follows. If spatial spacing or couplings change, the constants change and one must evaluate $s,w,\gamma,N$ on that sequence. The result compares spectral approximations and leaves their common spatial continuum limit open.

## A certified infinite-dimensional test

On one isolated square the gauge-invariant one-cycle space is the space of class functions of the holonomy. In the orthonormal $SU(2)$ character basis, at $\kappa=\lambda=1$ the diagonal is $n(n+2)+1$ and the two adjacent entries are $-1/2$. The free energy is now the *full* cycle Casimir $n(n+2)$. Dropping the constant leaves an interaction of norm at most one. The constant trial gives shifted $E_0\le0$, and $E_0\ge-1$. The first two characters give $E_1\le4$ in the same origin, so one can take $s=5$ for the gap. Set $t_k=\prod_{n=2}^k[n(n+2)-5]^{-1}$ with empty product one. There is one radial label and one boundary matrix element of magnitude $1/2$. At $J=8$ the common level error is at most
$$
 (5t_9^2+t_8t_9/2)/(1-t_9^2)=4/6953764855522223076923.
$$

Exact Sturm counts bracket the first two Ritz levels, in the original energy convention, in the respective intervals
$$
 [0.918058176624,0.918058176625],\qquad
 [4.031921988130,4.031921988131].
$$
The counts at these four endpoints are $0,1,1,2$. Every leading minor is nonzero there. Gaussian elimination without pivoting makes the signs of successive determinant quotients the inertia of the shifted matrix. This proves the counts from the tridiagonal determinant recurrence. Subtracting the intervals and allowing the level error in the appropriate direction gives the outward gap enclosure $[3.113863811504,3.113863811508]$ for the full, untruncated cycle. The exact arithmetic concerns this cycle alone. The coupled two-label numerical control separately tests the subspace estimate at rank four and rejects an interaction that jumps by two labels. [Exact bisection and numerical controls](check_spin.py) · [Lean integer counts and rational error](FiniteReadings.lean)
