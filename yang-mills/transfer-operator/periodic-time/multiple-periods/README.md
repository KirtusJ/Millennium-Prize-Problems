# What several thermal periods determine about a vacuum gap

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Fix any finite list of distinct positive temporal circumferences. Two finite-dimensional Hamiltonians with unique vacua can have exactly the same connected autocorrelation of a bounded reading at **every lag at every listed period**, with one vacuum gap fixed and the other arbitrarily large. The absolute normalization agrees and both readings have norm at most one. A single extra equal-time fourth moment can distinguish the models. The result concerns identification from thermal data under the stated transfer assumptions. Whether a specific Wilson action realizes such spectra is a separate question.

## A single Hamiltonian for the whole list

Fix the frequency $\omega>0$ and a desired gap $M>\omega$. The reference model has energies $0,\omega$ and a reading that interchanges the states with amplitude $1/\sqrt2$. At period $T$ its mean is zero and its correlation at $0\le s\le T$ is
$$
\frac{e^{-s\omega}+e^{-(T-s)\omega}}{2(1+e^{-T\omega})}.
$$

For $k$ prescribed periods $T_i$ write $x_i=e^{-\omega T_i}$ and $y_i=e^{-M T_i}$. Choose real coefficients $c_1,\ldots,c_k$ solving
$$
\sum_{j=1}^k c_j y_i^j=\frac1{1+x_i}.
$$
The determinant is a Vandermonde determinant multiplied by $\prod_i y_i$, hence nonzero. Put $d_j=\max(1,\lceil |c_j|\rceil)$ and $a_j^2=(1+c_j/d_j)/2$. Each $d_j$ is a positive integer and each amplitude is real with $0\le a_j\le1$. Above a unique vacuum place $d_j$ pairs at energies $jM$ and $jM+\omega$. The reading annihilates the vacuum and exchanges partners in each pair with amplitude $a_j$.

At period $T_i$ the partition function is $1+(1+x_i)\sum_j d_j y_i^j$. The coefficient of the same two-exponential lag kernel in the correlation is $\sum_j d_j a_j^2 y_i^j$ divided by this partition function. Substitution of the interpolation equation gives $1/[2(1+x_i)]$ exactly. The construction fixes one Hamiltonian and one reading before any of the listed measurements. Their first excited energy is $M$ even if a particular amplitude vanishes. The excited multiplicities may grow rapidly with $M$ or the list length. The spectral representation used here is the ordinary finite-temperature trace. [Meyer, §4, Eqs. (4.1)–(4.3)](https://inspirehep.net/files/4def05e01580c6de78da1364c3df066d)

For $\omega=\log 2$, $M=2\log 2$ and periods $1,2,3$, the coefficient numerators over 405 are $30488,-500608,1531904$. The multiplicities are $76,1237,3783$, giving dimension 10,193. At the unlisted period four the residual $(1+x)\sum_j c_j y^j-1$ is $-347683/491520$. Another finite design can be matched by redoing the construction. For either fixed model, increasing the period without bound recovers its own vacuum reading. The reference vacuum signal persists and the larger-gap model's signal vanishes.

The required thermal population has a dimension cost. The matching model has $C_T(0)=1/2$. Its reading annihilates the vacuum and has norm at most one, so $1/2\le1-p_0$ with $p_0=1/Z(T)$. Hence at the longest prescribed period its excited multiplicity is at least $\exp(MT_{\max})$, since every excitation contributes at most $\exp(-MT_{\max})$ to $Z$. A bound on the number or thermal weight of excitations supplies information beyond these correlators.

## A five-lag and fourth-moment test

Work at a single period $T$ in finite dimension with a unique vacuum. Write $B=O-\langle O\rangle_T I$, $b=\langle B^2\rangle_T>0$, and $\kappa=\langle B^4\rangle_T-b^2$. For a lag step $h>0$ choose $4h\le T$. Let $r=e^{-h\omega}$, $P(x)=(x-r)(x-1/r)$, and let $v_k$ be the coefficient of $x^k$ in $P(x)^2$. Form the measurable quantity
$$
F=\sum_{k=0}^4 v_k C_T(kh)
=\sum_{ij}p_i|B_{ij}|^2P(e^{-h(E_j-E_i)})^2\ge0.
$$
The identity follows by inserting energy eigenstates before taking the finite linear combination. This includes the lag-zero contribution and, when $4h=T$, the periodic endpoint. Both roots matter because the trace contains both directions of propagation. The [thermal moment analysis by A4](../../../observable-normalization/thermal-transitions/README.md) gives related positive frequency measures.

For a proposed vacuum floor $m>\omega$, put $d=\min(|P(1)|,P(e^{-hm}))>0$. This is a lower bound on $|P|$ on $\{1\}\cup[0,e^{-hm}]$ because $P$ decreases on $[0,r]$. If the floor holds, the *vacuum row alone* implies
$$
F\ge p_0d^2\langle0|B^2|0\rangle.
$$
Moreover $\kappa=\langle(B^2-bI)^2\rangle_T\ge p_0(\langle0|B^2|0\rangle-b)^2$. Thus every such floor requires
$$
p_0 b\le F/d^2+\sqrt{p_0\kappa}.
$$
For positive errors one can equivalently test whether an independent lower bound on $p_0$ exceeds $\big[(\sqrt{\kappa}+\sqrt{\kappa+4bF/d^2})/(2b)\big]^2$, propagating simultaneous measurement errors. The [two-lag thermal bound](../thermal-gap-test.md) uses a different allowance.

**Exact discriminator.** If $F=\kappa=0$, the faithfulness of the finite Gibbs trace gives $B^2=bI$. The vacuum row is nonzero. Every populated transition must have difference $+\omega$ or $-\omega$, since $F$ is a sum of squares. Applied to the vacuum row this forces an excited energy exactly $\omega$. Lower excited energies invisible to that row remain possible. The two-state reference passes both zero tests. In each matching model $F=0$ but $\kappa\ge p_0 b^2>0$ because $B$ annihilates its vacuum. Thus even one exact equal-time fourth moment at one of the listed periods distinguishes them. Finite errors can hide the difference when $p_0$ is small.

## Verification

Run `python3 check.py` in this directory. The standard-library script generates the interpolation coefficients by exact rational arithmetic for six designs, checks the deliberately unlisted period, and exhausts 729 symmetric ternary observables on transfer eigenvalues $1,1/4,1/8$ at period four. It constructs the thermal mean, all five lags and the fourth moment from the matrices before testing the bounds. Three host-dispatched PCP OS guests separately checked the three-period interpolation and its adverse control, the integer multiplicities and amplitude bounds, and the polynomial coefficients and endpoint distances at $h=1$, $\omega=\log2$, $m=\log4$. The three returned zero and the post-exit read-back of check text had SHA-256 `f136e348e7eb09c76812263a36a0947d76e531590d2a88d149e066011664e234`. The general interpolation and spectral implications are analytic arguments. The numerical examples make no measurement of the Wilson vacuum.
