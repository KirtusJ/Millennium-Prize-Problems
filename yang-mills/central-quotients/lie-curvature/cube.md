# The second-order cube identity and a local calibration

At every coupling take a positively oriented unit cube along three lattice axes. Label by $T_\pi$ the transport from its low corner to its high corner along the steps in order $\pi$. Use
$$
             123,\quad 213,\quad 231,\quad 321,\quad 312,\quad 132,\quad 123 .
$$
For each adjacent pair set $H_i=T_{\pi_i}T_{\pi_{i+1}}^{-1}$. Common suffix edges cancel, and the shared prefix transports a face back to the low corner. Each of the six faces occurs once with its surface orientation. $H_1\cdots H_6=I$ exactly. In this paragraph take $F_i=\sqrt\beta\,b(H_i)$ with the metric and projection of the [Wilson action](wilson-groups.md). For each finite $q$,
$$
 D_\beta=\beta\sum_i b(H_i)
     =-\tfrac12\sum_{i<j}[F_i,F_j]+O_{L^q}(\beta^{-1/2}).
$$
To prove it, expand $\prod_i (I+(H_i-I))$ as an ordered product. Terms of degree at least three have $L^q$ norm $O_q(\beta^{-3/2})$ by Hölder and the moment bound. In each quadratic term replacing the scaled two factors by their tangent projections costs $O_q(\beta^{-1/2})$ after scaling. For anti-Hermitian $A,B$ in $\mathfrak k$, the skew part of $AB$ is $[A,B]/2$, already in the algebra. Projecting the expanded identity thus proves the estimate. It also proves moment convergence to the displayed bracket polynomial of the leading Gaussian faces. The observable $\|D_\beta\|^2$ is gauge invariant. This detects the first term of the nonlinear cube identity on *all* joint weak-coupling, large-volume trajectories, including logarithmic choices of the bare coupling.

For an independent normalization use two faces $p=12$, $q=34$ based at the same vertex and the group commutator $C_{pq}=U_p U_q U_p^{-1} U_q^{-1}$. Its Wilson action satisfies exactly
$$
 \beta^2 V(C_{pq})=\tfrac12\big\|[\sqrt\beta(U_p-I),\sqrt\beta(U_q-I)]\big\|^2 .
$$
Indeed $C_{pq}-I=(U_pU_q-U_qU_p)U_p^{-1}U_q^{-1}$ and right multiplication by these unitary tuples preserves the norm. In the tangent field the two faces have independent $N(0,I_d/2)$ components: the projection multiplier has zero entry between disjoint orientation pairs for every momentum. Let $S=\sum_{a,b}\|[T_a,T_b]\|^2$ for an orthonormal Lie basis. Then
$$
 \lim\mathbb E[\beta^2V(C_{pq})]=S/8.
$$
For a compact simple Lie algebra put $c=S/d$. The limiting variance is $7dc^2/64$, hence variance divided by squared mean is $7/d$, independent of the character normalization. The fourth-order contraction giving this figure is proved in the [singlet calculation](singlets.md). For the fundamental $SU(2)$ metric the entire limit is the distribution of $\chi^2_3\chi^2_2/2$ with independent factors: take the length of the first Gaussian color vector and the two perpendicular components of the second one. In an Abelian group the commutator is the identity on every configuration, so its Wilson action vanishes exactly.

## The cube coefficient

For one color write $C$ for the $6\times6$ covariance of the oriented faces in the stated order. Let $J_{ij}$ equal $+1$ for $i<j$, $-1$ for $i>j$ and zero on the diagonal. Different color vectors $G^a\in\mathbb R^6$ are independent with covariance $C$. Rewriting the bracket sum as $\sum_{a<b}[T_a,T_b]\,(G^a)^TJG^b$ shows
$$
 \lim\mathbb E\|D_\beta\|^2=(S/8)\operatorname{Tr}(J^T C J C).
$$
Pair terms from distinct unordered color pairs have zero cross moment by Gaussian centering. The same $S/8$ therefore calibrates the cube against the two-face commutator for any non-Abelian observable group.

The opposite faces have indices $i$ and $i+3$ modulo six. Cubic coordinate symmetries permute all face pairs of a given type. An orientation reversal of the cube changes all surface signs together; short base changes have disappeared in the Gaussian tangent. Thus $C$ is constant on diagonal, opposite, and adjacent entries. The constant-vector eigenvalue is zero by closure. Write $A=(I-T)/2$, $B=(I+T)/2-\mathbf1\mathbf1^T/6$ for the orthogonal projections on opposite-pair differences and zero-sum pair means, where $T$ exchanges each opposite pair. Then $C=aA+bB$, with
$$
 a=\tfrac12+\kappa,\qquad 3a+2b=3 .
$$
The diagonal entries are $1/2$; the covariance between opposite outward faces is $-\kappa$ with $\kappa$ the one-step correlation of a positively oriented $12$ face in a transverse direction. In the lattice Fourier formula, with $q_j^2=4\sin^2(k_j/2)$ and $\omega=2\operatorname{arsinh}(\sqrt{\sum_{j=1}^3q_j^2}/2)$,
$$
 \kappa=\int_{[-\pi,\pi]^3}(q_1^2+q_2^2)\frac{e^{-\omega}}{2\sinh\omega}
                     \frac{d^3k}{(2\pi)^3}>0 .
$$
Integrating the momentum in the displacement direction gives the Green coefficient above; the remaining three axes were relabeled. [Original covariance](../tangent-curvature/reflection.md)

Direct integer contraction of $6A,6B$ against $J$ gives coefficients $216,0,24$ for the two diagonal terms and their mixed term. It follows that the calibrated cube-to-commutator ratio is
$$
     6a^2+\tfrac23 b^2=(15a^2-6a+3)/2>15/8.
$$
The cube order and the direction of all six transports are part of this observable. Omitting the connecting edges changes the finite-coupling identity. This nonzero local result concerns the Lie bracket of a Gaussian leading field; by itself it does not determine a renormalized interaction or a physical mass.

## A signed third moment one order below the Gaussian limit

The same cube gives an odd observable whose first asymptotic coefficient has a definite sign. Set
$$
 T_\beta=\sum_{i<j<k}\langle[F_i,F_j],F_k\rangle,\qquad
 B_\beta=\sum_{i<j}[F_i,F_j].
$$
The trilinear form is alternating by invariance of the Wilson metric. Hence $T_\beta=\langle B_\beta,\sum_k F_k\rangle$ exactly: a distinct sorted triple in the expanded pairing contributes with signs $+,-,+$, and repeated indices vanish. Since $D_\beta=\sqrt\beta\sum_k F_k=-B_\beta/2+O_{L^2}(\beta^{-1/2})$ and $B_\beta$ is uniformly bounded in $L^2$,
$$
 \lim_{\beta,L\to\infty}\sqrt\beta\,\mathbb E T_\beta
   =-\tfrac12\lim\mathbb E\|B_\beta\|^2
   =-\frac{S}{4}\operatorname{Tr}(J^TCJC).
$$
All first-order joint Gaussian third moments vanish. This coefficient measures the ordered nonlinear constraint at the next order using actual lattice faces. For a non-Abelian group it is strictly negative with the specified orientations; reversing the path cycle changes the definition of the insertion. No asymptotic rate for the remaining error in the limiting covariance is assumed.
