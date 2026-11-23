# A volume-independent disk for local Wilson expectations

Take $\rho=1/1024$. Work on finite open boxes, or on spatial tori of side $L\ge2$ with open time. With independently complex plaquette couplings $|a_f|\le\rho$, the normalized Haar expectation of any bounded function $F$ depending on $m$ links is holomorphic in the interior and obeys
$$
                 |\langle F\rangle_a|\le \|F\|_\infty e^m .
$$
This estimate also applies to complex observables. Only the dependence on the support, with no separation or box-volume cost, matters here. The following deletion proof supplies the bound and the zero-free disk used in the Taylor and spectral arguments. Abstract polymer convergence is classical. [Kotecký and Preiss, main theorem](https://doi.org/10.1007/BF01211762)

Expand each Wilson factor as $1+f_p$, where $\|f_p\|_\infty\le\epsilon=e^\rho-1$. Connect plaquettes sharing a link. The expectation of the product for any chosen set factors over its connected components. Each nonempty connected plaquette set $H$ is a polymer of weight $w_H$ bounded by $\epsilon^{|H|}$. Distinct polymers can occur together if their union is disconnected across the two sets. Intersecting polymers are also incompatible. The result is exactly a hard-core polymer partition sum.

Each face has at most 20 neighbors (four edges, five other incident faces), including on the short periodic tori. The number of connected $j$-face sets containing a specified face is at most $80^{j-1}$. Record a deterministic rooted spanning tree, its ordered tree shape (fewer than or equal to $4^{j-1}$ choices), and one of at most 20 labeled neighbors at each step. The record recovers the set. Put $u_H=(e\epsilon)^{|H|}$ and $v=e\epsilon<1/256$, since $e<3$ and $e^\rho\le(1-\rho)^{-1}$. Then
$$
 \sum_{K\text{ incompatible with }H}u_K
      \le 21 |H|\frac{v}{1-80v}<|H|/2 .
$$

For any subfamily of polymers let $Z$ be its compatible-set sum, including the empty term. Add $H$ to a smaller family. Relative to its former partition sum the factor has the form $1+q$, where $q$ is $w_H$ times the ratio obtained by deleting every former polymer incompatible with $H$. Inductively suppose the modulus of the inverse factor for deleting $K$ in any smaller family is at most $e^{2u_K}$. Then $|q|\le |w_H|\exp(2\sum_{K\nsim H}u_K)\le u_H<1/2$. This proves nonvanishing, $|1+q|\le e^{u_H}$, and $|(1+q)^{-1}|\le(1-u_H)^{-1}\le1+2u_H\le e^{2u_H}$. It closes the induction, starting with $Z=1$.

Pin the $m$ links on which $F$ depends at arbitrary group elements. The polymer construction still works with the other links integrated, using the same incompatibility graph and bounds. Only polymers containing a face incident to a pinned link can change weight. Delete these polymers in both systems to get identical partition sums. Their total $u_H$ is at most $6m v/(1-80v)$. Add them back in the pinned partition sum and use the inverse factors for the original sum. The quotient has modulus at most $\exp(18m v/(1-80v))\le e^m$. Integrating $F$ times this quotient in normalized Haar over its support gives the claim. For two observables the covariance is bounded by $2\|F\|_\infty\|G\|_\infty e^{m_F+m_G}$.

## Coefficients and error

For our rectangles this bound is $M=8e^{2P}$. Under a common coupling the finite-box holomorphic function has its first term $B_k(\beta/4)^{D_k}$ exactly, once both loops are inside an open box. For real $0<\beta<\rho$, Cauchy's inequalities on the disk give
$$
 \left| C_k-B_k(\beta/4)^{D_k}\right|
 \le M\frac{(\beta/\rho)^{D_k+1}}{1-\beta/\rho}.
$$
The estimate passes to the strong-coupling infinite-volume state at each fixed contour and lag by uniqueness. For fixed supports, normal-family compactness and agreement on the real interval also give the same analytic germ there. No convergence at a complex physical coupling is needed. Without taking the leading term, Schwarz's lemma with multiplicity gives $|C_k|\le M(\beta/\rho)^{D_k}$. For the one-loop mean use $M=2e^P$, degree $A$, and coefficient $2/4^A$ from the planar disk. Both bounds involve the perimeter in the prefactor rather than the survey volume. [Single-disk coefficient](../wilson-surfaces/prefactors.md) · [Uniqueness and transfer vacuum](../strong-coupling/)

In particular the relative remainder after the connected leading term is at most
$$
 \frac{8 e^{2P}}{B_k}\left(\frac4\rho\right)^{D_k}
       \frac{\beta/\rho}{1-\beta/\rho}.
$$
When the physical side lengths and time tend to positive finite limits, $P=O(b^{-1})$, $D_k=O(b^{-2})$. Therefore $|\log\beta|b^2\to\infty$ suffices. For finitely many fixed integer offsets from $k$ the relative errors are $O(\exp(-|\log\beta|/2))$ eventually. The argument removes the previous extra factor $\log(1/b)$ in the sufficient growth of $|\log\beta|$. Above the crossover it also controls the connected term, which is much smaller than the product of the means. At fixed small bare coupling and macroscopic loops the resulting error need not be small relative to the first term.
