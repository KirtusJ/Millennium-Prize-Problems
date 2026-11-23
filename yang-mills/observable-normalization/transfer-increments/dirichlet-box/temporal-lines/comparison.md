# A linear total variation bound from an exchange of two densities

For the SU(2) forest and a Wilson-distributed breadth-first shell of side $L=2N$, let $\psi$ denote the scaled shell links, $X$ the full vector of scaled links, $D$ the curl of a free vector with zero exterior and $dX$ the curl including the shell. Let $a_\psi$ minimize the squared linear curl for that exterior. With the notation of the [previous comparison](../mean-shell.md), we obtain

$$\sup_{\mu\in\mathcal L_\beta}\mathbb E_\mu d_{\rm TV}(K_\psi,\Gamma_\psi)\le C\frac{L^8}{\sqrt\beta},\qquad L^8\le\sqrt\beta.$$

## Fourth moments under both joint laws

For every free horizontal link in a zero-shell variation $u$, a temporal strip to the top gives $|u_e|^2\le L\|Du\|_2^2$ by Cauchy–Schwarz. For a bottom time link at vertex $s$, the variational characterization of the inverse Hessian gives $|u_e|^2\le L(A^{-1})_{ss}\|Du\|_2^2$, by the [exact temporal marginal](README.md). This bound applies componentwise and sums correctly for a vector. In the three-dimensional Dirichlet sine basis, $|e_k(s)|^2\le 8/L^3$ and $\lambda_k\ge4|k|^2/L^2$ by the sine chord inequality. Group the frequencies by $q=\max_j k_j$. There are $q^3-(q-1)^3\le3q^2$ on shell $q$, so $(A^{-1})_{ss}\le 6$ uniformly. Combine the resulting point-evaluation bound with $\sum_e|u_e|^2\le32L^3\|Du\|_2^2$ from the [global strip estimate](../coercivity.md). Then

$$\sum_e|u_e|^4\le C L^4\|Du\|_2^4. \tag{1}$$

Under Wilson sampling the existing rooted-loop bound gives $\||X_e|\|_p\le C_pL^2$ for each fixed finite $p$. In particular $\mathbb E\sum_e |X_e|^4\le C L^{12}$, including the shell, as there are $O(L^4)$ links. Write $s_p=\sum_{e\in p}|X_e|$ on a face. Its ordered quaternion word $U_p(t)$, with scaled logarithms in the four factors divided by $\sqrt\beta$ and multiplied by $t$, satisfies $U_p(0)=1$ and $\sqrt\beta U'_p(0)=(dX)_p$. Unitarity bounds the norm of $U''_p(t)$ by $s_p^2/\beta$. Thus

$$\left|\sqrt\beta(U_p(1)-1)-(dX)_p\right|\le s_p^2/(2\sqrt\beta). \tag{2}$$

The uniform Wilson plaquette tail bounds the fourth norm of $\sqrt\beta |U_p(1)-1|$. The eighth moment of each link gives $\|s_p^2\|_4\le C L^4$. By (2), $\|(dX)_p\|_4\le C$ in the stated range. Summing squared face norms in $L^2$ and then squaring gives $\mathbb E\|dX\|_2^4\le C L^8$.

For the other joint law keep the same Wilson shell, then use $a_\psi+\zeta$ on the free links, where the centered Gaussian fluctuation $\zeta$ has precision $D^*D$ per color. Couple it to a Wilson draw $X$ with that shell. The projection identity $\|D(X_{\rm free}-a_\psi)\|_2\le\|dX\|_2$ and (1) bound the expected sum of fourth powers of $X_{\rm free}-a_\psi$ by $C L^{12}$. The covariance of each centered Gaussian link is at most $6L I_3$ by the point-evaluation bound. Therefore $\mathbb E\sum_e|\zeta_e|^4\le C L^6$. Writing $a_\psi+\zeta=X_{\rm free}-(X_{\rm free}-a_\psi)+\zeta$ gives the same $C L^{12}$ bound for the sum of fourth powers of all links under Gaussian sampling. Its total expected squared curl is at most $C L^4$: the minimizing curl has norm at most the actual Wilson curl, and $D\zeta$ has covariance a projection of rank $O(L^4)$. This also holds for the Wilson sample by its fourth-curl bound. All these estimates refer to expectations with the original Wilson shell marginal.

## Ordered action and normalization

The compact face action is $\beta |U_p(1)-1|^2/2$ exactly. Squaring (2) about its linear approximation bounds the absolute action error on that face by

$$C\left(|(dX)_p|s_p^2/\sqrt\beta+s_p^4/\beta\right).$$

This inequality uses no small-coordinate expansion. Since $\sum_p s_p^4\le C\sum_e|X_e|^4$ by bounded incidence, Cauchy–Schwarz over faces and probability gives an expected total error at most $C(L^8/\sqrt\beta+L^{12}/\beta)$ under either joint law. On the set $B=\{\max_{e\ {\rm free}}|X_e|\le\sqrt\beta\}$, the absolute log Haar factor is at most $C\sum_e |X_e|^2/\beta$. Its expected contribution is at most $C L^8/\beta$. Markov's inequality bounds the mean probability of $B^c$ by $C L^{12}/\beta^2$ under either law. In the Gaussian comparison the compact density vanishes beyond the principal chart. Its logarithm is needed only on $B$.

Fix a shell. Denote the normalized laws by $P,Q$ and set $h=\log f_\beta-\log f_\infty$ for their unnormalized chart densities on $B$. Projection to the first sample gives $d_{\rm TV}(P,Q)\le d_{\rm TV}(P\otimes Q,Q\otimes P)$. At $(x,y)\in B^2$ the reversed-to-forward density ratio equals $\exp(h(y)-h(x))$ because both normalizers cancel. The positive difference of forward and reversed density, integrated there, is at most $\mathbb E_{P\otimes Q}[(|h(x)|+|h(y)|)\mathbf1_{B^2}]$ by $(1-e^{-u})_+\le |u|$. On its complement the positive difference is bounded by forward mass, at most $P(B^c)+Q(B^c)$. Averaging over the shell and inserting the preceding estimates proves the stated bound, since $L^4\le\sqrt\beta$ in the claimed range. This argument leaves the exterior marginal intact and works even when one of the two original densities vanishes on a set of positive mass for the other.
