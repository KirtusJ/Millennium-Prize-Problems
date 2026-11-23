# Wilson character actions and their local curvature

Fix a compact connected Lie group $G$, finitely many finite-dimensional unitary representations $\rho_j$ of dimensions $n_j$, and fixed weights $w_j>0$. Use normalized Haar on every link, and the isotropic action $\beta\sum_p V(U_p)$, where
$$
 V(u)=\sum_j w_j[1-\operatorname{Re}\operatorname{Tr}(\rho_j(u))/n_j].
$$
Pass first to $K=G/\bigcap_j\ker\rho_j$, identified with its image in the product of unitary groups. Edgewise Haar pushforward is exactly normalized Haar on $K$; the action is the pullback of the indicated function of quotient links. Thus every expectation involving only those links is the same at all couplings and volumes. In a finite periodic history the conditional lifts of separate edges are independent Haar on the corresponding kernel cosets. At one transfer step the kernel averages independently over these invisible link directions; nonzero transfer eigenvectors are in the lifted quotient space. This statement uses an action already constant on those fibers. For the fundamental $SU(2)$ action the center changes the action and its pushforward to $SO(3)$ has the coupled face signs described in the [original quotient calculation](../README.md).

Write $d=\dim K$ and assume $d>0$. Regard its Lie algebra $\mathfrak k$ as a real subspace of the product of matrix spaces. Give the product the real Hilbert norm from
$$
 \langle A,B\rangle=\sum_j (w_j/n_j)\operatorname{Re}\operatorname{Tr}(A_j^* B_j).
$$
Use this restricted inner product on $\mathfrak k$ and its associated bi-invariant geodesic distance on $K$. Write $u$ for the matrix tuple representing a group element. With $\Pi$ the real orthogonal projection onto $\mathfrak k$, define $b(u)=\Pi(u-I)$. Then
$$
 V(u)=\tfrac12\|u-I\|^2,\quad b(u^{-1})=-b(u),\quad
 D_X V(u)=\langle X,b(u)\rangle,\quad b(e^X)=X+O(\|X\|^3).
$$
The derivative is for multiplication by $e^{sX}$ on either side, using cyclic trace and skew adjointness of $X$. Projection kills Hermitian matrices, including $X^2$. Conjugation acts isometrically and preserves $\mathfrak k$, so the projection is equivariant. Near identity $V(e^X)=\|X\|^2/2+O(\|X\|^4)$. Away from that neighborhood faithfulness on $K$ and compactness give $c\,\mathrm{dist}(1,u)^2\le V(u)\le C\,\mathrm{dist}(1,u)^2$. Constants throughout can depend on this fixed group and its representations.

## Vacuum bound and original site reflection

On a spatial side-$L$ torus ($L\ge3$) first take the time period to infinity at fixed $\beta,L$. The transfer is the product convolution sandwiched by $M=\exp[-\beta\sum_{p\,{\rm spatial}} V(U_p)/2]$ and restricted to gauge invariants. Its one-link kernel before normalization is
$$
 e^{-\beta V(uv^{-1})}=e^{-\beta\sum_j w_j}\exp[\beta\langle u,v\rangle].
$$
Each tensor power of the real matrix feature is positive definite, so the exponential power series gives a positive operator. The normalized convolution has norm one. The unrestricted sandwiched kernel is strictly positive as a function and compact on a finite box; its largest eigenvalue is simple with a positive gauge-invariant eigenfunction. Gauge projection commutes with the transfer. A finite positive power is trace class by bounded kernel and compactness of the configuration space (the transfer is Hilbert–Schmidt). Fixed-box vacuum cylinder limits follow from the top projection, Haar-averaging a whole cylinder over its finitely many site gauges when needed.

In normal coordinates $z(\gamma)=\int e^{-\gamma V}du$ is between positive constants times $\gamma^{-d/2}$ at $\gamma\ge1$. The same cap estimate gives $\int \mathrm{dist}(1,u)^2 e^{-\gamma V}du/z(\gamma)\le C/\gamma$ by Gaussian integration in the identity chart and exponential suppression outside it. A nonnegative normalized one-link bump $f_\delta$ in a ball of radius $\delta$ has squared gradient norm at most $C/\delta^2$. Integrating squared translation differences along shortest paths gives $\langle f_\delta,K_\beta f_\delta\rangle\ge1-C/(\beta\delta^2)$. On the support of the product bump every spatial face has $V\le C\delta^2$. With $P=3L^3$ links and the same number of spatial faces, positivity of the kernel gives the lower Rayleigh bound
$$
 \|T_\beta\|\ge e^{-C\beta P\delta^2}(1-C/(\beta\delta^2))^P.
$$
Take $\delta=A/\sqrt\beta$ with a sufficiently large fixed $A$. This proves $-P^{-1}\log\|T_\beta\|\le C_0$ uniformly in the side. The vacuum lies in the physical sector even though the trial bump need not be invariant.

Site reflection in an even extent conditions on the shared boundary slices. For an odd spatial extent the far crossing has the form $M K_\beta\Pi_{\rm gauge} M$, up to positive constants, with product convolution $K_\beta$ commuting with the orthogonal gauge projection. This is a positive quadratic form on arbitrary endpoint functions. The geometric even/odd argument and gauge average of the whole reflected product therefore hold also on $K$. The copied positive face factors in the reflected-block estimate use only $V(u^{-1})=V(u)$ and invariance under conjugation. Every face has at most four assigned copies. Consequently the finite-volume moment of $\exp(\beta V_p/8)$ to the power of the copied block volume $J>L^3N/256$ is bounded by the partition ratio at $\beta/2$ and $\beta$. Its log divided by $NP$ tends at fixed box to $\log[z(\beta/2)/z(\beta)]+P^{-1}\log[\|T_{\beta/2}\|/\|T_\beta\|]$, uniformly bounded above. In particular
$$
               \sup_{\beta\ge\beta_0,L,p}\mathbb E e^{\beta V(U_p)/8}<\infty .
$$
[Even and odd site reflection](../tangent-curvature/reflection.md) · [Copied-block geometry](../tangent-curvature/moments.md) · [Osterwalder and Seiler, Gauge field theories on a lattice](https://doi.org/10.1016/0003-4916(78)90039-8)

## Fixed cells on every weak-coupling trajectory

Transport each face into a common root frame along fixed tree paths. For **every** $\beta,L\to\infty$, $F_p=\sqrt\beta\,b(U_p^{\rm rooted})$ converges on finite sets, with all polynomial moments, to the centered Gaussian lattice curvature with covariance the projection $P_{\rm ex}$ onto the closure of exact cubical two-forms, independently in $d$ orthonormal colors. Here are the group-dependent steps in this deduction.

* Fixed contractible chord loops fill by finitely many conjugated plaquettes, so each local tree-gauged link has $L^q$ distance $O_q(\beta^{-1/2})$ from identity for all finite $q$. A change of finite root paths has the same control up to a common rotation. Expanding a four-factor matrix word and projecting shows $F=dA+O_{L^q}(\beta^{-1/2})$ where $A_e=\sqrt\beta\,b(U'_e)$; projection of an inverse changes sign. Thus all limits are closed.
* For the variation at a selected edge use a tree avoiding it. Left Haar variation by a rooted generator inserts $X$ with its incidence sign in the face word. The score is the corresponding component of the face field up to conjugation by at most four local gauged links. The error tends to zero in $L^q$ since the adjoint action is smooth on the compact group. The derivative of each scaled face under a $1/\sqrt\beta$ link variation tends to its incidence times $X$. These facts give $\mathbb E[\partial_{dh} f(F)]=\mathbb E[F(dh)f(F)]$ for compact tests. The uniform moments justify passage to the limit. The argument applies to each orthonormal color.
* The scalar characteristic ODE on exact tests and the cubical Hodge identity give $F=Z+H$ where $Z$ has covariance $P_{\rm ex}$ and $H$ is an independent spatially and temporally constant random two-form. The coordinate second moments are uniformly bounded. In the proof the difference field is closed and coclosed; bounded scalar harmonic functions obtained by testing its coordinates against $L^2$ random variables are constant. Its characteristic function factors from the projected Gaussian. This lattice step is unchanged for any finite number of colors. The single-face variance per color is $1/2$ by permutation symmetry of the four coordinates.
* Reflect a bounded sine of a single rooted color component in a plane through its base-path root perpendicular to one of its axes. With straight axis transports the reflected face is exactly the inverse of the positively oriented opposite face in its root frame. The coordinate $b$ is inverse-odd. At large separation the Gaussian cross covariance tends to zero, so positivity gives $0\ge e^{-t^2/2}\mathbb E\sin^2(t H_{ij,c})$. Taking $t=1/m$ proves $H=0$. This proves uniqueness of the finite marginals on every sequence. Exponential single-face moments give convergence of all moments. [Characteristic and harmonic argument](../tangent-curvature/gaussian.md)

On each fixed face $\sqrt\beta(u-I)-F\to0$ in every finite $L^q$: near one the normal component is quadratically small, and away from one the exponential bound absorbs all powers of $\beta$. The exact norm identity for $V$ now gives $\beta V(U_p)\Rightarrow\chi^2_d/4$, with limiting mean $d/4$ and variance $d/8$. This concerns the observable group $K$ and its Wilson metric. A fixed nontrivial representation of a compact connected simple group has a finite central kernel; a faithful finite-dimensional unitary representation can also be used for each compact Lie group. The constants are for a fixed choice and need not be uniform as the rank grows.
