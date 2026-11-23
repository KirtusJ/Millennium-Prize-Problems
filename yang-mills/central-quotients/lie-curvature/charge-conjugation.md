# A charge-conjugation-odd Wilson measurement for SU(N)

Use the normalized fundamental trace $\tau=\operatorname{Tr}/N$ and the pure Wilson potential $1-\operatorname{Re}\tau(U_p)$ on $SU(N)$. Complex conjugation of every link is an exact symmetry of Haar and of the finite-regulator action. It commutes with the transfer, and its unique positive vacuum is even. On a time slice an invariant magnetic bracket contraction is even, whereas the imaginary part of a fundamental trace is odd. Their mixed expectations vanish already at finite coupling. This selection rule also distinguishes two different cubic probes of the same smoothed magnetic vectors.

With orthonormal anti-Hermitian generators $T_a$ define the real completely symmetric tensor
$$
     s_{abc}=\operatorname{Im}\tau[(T_aT_b+T_bT_a)T_c],\qquad
     S_-=\sum_{abc}s_{abc}^2=2(N^2-1)(N^2-4).
$$
To verify the normalization put $H_a=-iT_a$. Then $\tau(H_aH_b)=\delta_{ab}$ and $s_{abc}=-\tau(\{H_a,H_b\}H_c)$. For fixed $a$ sum the squared projection of $\{H_a,H_b\}$ onto the traceless basis over $b$. The projection onto $I$ subtracts $\sum_b(2\delta_{ab})^2=4$. Completeness gives $\sum_bH_b H_a H_b=-H_a$ and $\sum_bH_b^2=(N^2-1)I$. The sum of the full squared norms is $-2+2(N^2-1)$, giving $2(N^2-4)$ after removing the scalar. Also $\sum_as_{aac}=0$ since $\sum_a H_a^2$ is scalar. Complex conjugation negates $s(X,Y,Z)$, whereas it preserves $\langle[X,Y],Z\rangle$. For $SU(2)$ this symmetric tensor and the imaginary part of the fundamental character vanish identically.

## The imaginary trace of one actual plaquette

On any weak-coupling, large-box sequence, at a fixed plaquette define $I_p=\beta^{3/2}\operatorname{Im}\tau(U_p)$. Its expectation is exactly zero. Near identity write $U_p=e^A$ with traceless anti-Hermitian $A$. In the imaginary trace expansion the linear term vanishes by tracelessness, even powers have real trace and the cubic term is $\operatorname{Im}\tau(A^3)/6$. Since $b(e^A)=A+O(|A|^3)$, the [uniform Wilson moments](wilson-groups.md) imply, for every finite $q$,
$$
              I_p=\tfrac1{12}s(F_p,F_p,F_p)+O_{L^q}(\beta^{-1}) .
$$
The fifth-order remainder gives the indicated rate before taking the tangent law. Leaving a fixed logarithm chart costs exponentially small probability. The limiting single-face variance is $S_-/192$: all internal Gaussian pairs vanish by $\sum_a s_{aac}=0$, while the $3!$ cross-pairings contribute $(6/12^2)S_-(1/2)^3$. In particular the $SU(3)$ limiting variance is $5/12$.

For the same spatial face at a fixed time separation $n$ in lattice steps the limiting covariance is $(S_-/24) C_1(n)^3$, where $C_1$ is the single-face one-color covariance. Its limiting energy measure in lattice units is $(S_-/24)\mu_1^{*3}$; here $\mu_1$ is the radial lattice-dispersion measure in the [single-face proof](../tangent-curvature/reflection.md). Its mass below $\epsilon$ is asymptotic to $S_-\,\epsilon^{12}/(24\pi^6\,12!)$. Moment convergence includes zero time, so the conclusion about the finite-regulator odd spectral measures follows from convergence of all integer Laplace moments. For $N\ge3$ the odd sector thus has arbitrarily low **lattice-unit** energies on every stated weak trajectory. This fixed-cell conclusion gives no rate at a shrinking physical-energy window.

## A physical odd channel

Using the three cyclic spatial smearings from the [singlet calculation](singlets.md), put $T_-=s(X_1,X_2,X_3)$ and $T_+=\langle[X_1,X_2],X_3\rangle$. These scalars use only one slice. At finite regulator $X_i$ changes to its entrywise complex conjugate when all links are conjugated. Thus $\mathbb E T_-=0$ and all even–odd cross readings vanish at any separation. The expressions can be evaluated using link matrices directly. For the defining representation $b(U)=(U-U^\dagger)/2-\tau((U-U^\dagger)/2)I$, so the invariant polynomials also expand into traces and products of traces of the rooted loop words.

On the explicit rapidly weakening trajectories, the connected physical measures for $T_-$ and $T_+$ are $S_-\mu^{*3}$ and $2N^2(N^2-1)\mu^{*3}$ respectively. For $N\ge3$ their two positive-time readings have the ratio
$$
 \lim\frac{\langle T_-(0)T_-(\lfloor rt\rfloor)\rangle}
            {\operatorname{Cov}(T_+(0),T_+(\lfloor rt\rfloor))}
       =1-\frac4{N^2}\qquad(t>0).
$$
The two operators have the same nonzero Gaussian time dependence, are orthogonal by an exact lattice symmetry, and have positive mass in every sufficiently small fixed physical energy interval. In particular the lowest **charge-conjugation-odd** physical energy tends to zero on these free trajectories. In $SU(3)$ the ratio is $5/9$. For a single smoothed orientation the cubic $s(X_1,X_1,X_1)$ also has a pure third-order Wick law because the tensor has zero trace. The physical-time result uses spatial smearing; the preceding result for the ordinary imaginary trace uses a single unsmeared face.
