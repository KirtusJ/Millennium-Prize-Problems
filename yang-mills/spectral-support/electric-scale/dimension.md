# How many link states must an interacting vacuum occupy?

Let $G$ be a compact connected simple Lie group of dimension $d$, with a fixed bi-invariant metric and a finite-dimensional unitary representation $\rho$ with injective differential. Use normalized Haar and $v(h)=1-\operatorname{Re}\operatorname{Tr}\rho(h)/\dim\rho$. Consider the spatial Hamiltonian on a finite periodic cubic lattice of side at least three,
$$H=a\sum_e(-\Delta_e)+\lambda\sum_p v(U_p),\qquad g_G=\lambda/a.$$
The positive vacuum defines a reduced density operator $\sigma_e$ by tracing out the other factors in the product of link Hilbert spaces $L^2(G)$. For a fixed $0<q<1$ let $r_q$ be the least rank of a one-link orthogonal projector $P$ with $\operatorname{Tr}(\sigma_eP)\ge q$. With natural logarithms, as $g_G\to\infty$,
$$r_q\asymp_{G,\rho,q}g_G^{d/4},\qquad
S(\sigma_e)=\tfrac d4\log g_G+O_{G,\rho}(1).$$
Constants may also depend on the fixed metric. They are independent of the box. For the round $SU(2)$ link, $a=\kappa/4$, $g_G=4g=2\beta^2$ at bare matching. This gives $r_q\asymp_q\beta^{3/2}$ and $S=(3/2)\log\beta+O(1)$.

## Earlier SU(2) truncation and entropy bounds

Mihajlovic proved a necessary retained dimension of order $g_{\rm YM}^{-3}$ for nonvanishing vacuum fidelity under the standard spin cutoff on one or more selected links, uniformly in the spectator system. With his spatial spacing $a_s$, the coefficients of the spin Casimir and of the plaquette deficit are $\kappa=g_{\rm YM}^2/(2a_s)$ and $\lambda=4/(a_s g_{\rm YM}^2)$. For our round metric $g_G=4\lambda/\kappa=32/g_{\rm YM}^4$. Thus his necessary power in (41.18) agrees exactly with the lower power above when $d=3$. The result here supplies a matching upper bound, allows arbitrary link subspaces and extends to compact connected simple groups and the stated joint forests. His Theorem 40.1 bounds the **classical relative entropy** of the full configuration law against product Haar from below, per selected edge-disjoint plaquette. The entropy above is the **von Neumann entropy** of a reduced link density operator and has upper and lower bounds. The matching leading powers concern these specified settings. [Mihajlovic, §§40.1–40.2, 41.1 and 41.4, Theorem 40.1 and equations (41.16)–(41.19)](https://arxiv.org/pdf/2611.11534v1#page=234)

## Variational inputs

On the compact link product the heat kernel of the kinetic operator is strictly positive at positive time. The bounded real potential preserves positivity improvement by Feynman–Kac. The full-space ground state is therefore unique up to phase and can be chosen strictly positive. Pairwise gauge transformations and lattice symmetries preserve that choice and the Hamiltonian. Thus its energy is the physical vacuum energy. A smooth normalized one-link bump supported inside an identity ball of radius $s$ has kinetic form $O(s^{-2})$, by rescaling a fixed test function in an exponential chart. In the product trial, every plaquette holonomy is at distance at most $4s$ from identity. The action there is $O(s^2)$. The product trial bounds the full-space minimum; uniqueness and gauge invariance identify it with the physical minimum. Take $s=g_G^{-1/4}$ for sufficiently large $g_G$. Cubic symmetry and the equality of link and face counts then give
$$K_e=\langle-\Delta_e\rangle\le C\sqrt{g_G},\qquad
u_p=\langle v(U_p)\rangle\le C/\sqrt{g_G}.$$
One needs only these bounds and gauge invariance in the rest of the argument.

## A bound for every local subspace

The zeros of $v$ are the finite kernel of $\rho$. At each zero the quadratic part in $X$ is $\|d\rho(X)\|_{\mathrm{HS}}^2/(2\dim\rho)$. Compactness then gives $\operatorname{Haar}\{v<s\}\le C s^{d/2}$ for all $s>0$, upon enlarging $C$. At any incident plaquette the multiplier $v_y$ in the marked link, conditional on fixed *coordinates* $y$ of the other links, is a translate of $v$ composed possibly with inversion. This preserves its Haar distribution. The conditional vacuum density itself need not be Haar.

An endpoint gauge transformation acts on the marked link by arbitrary left translation and on the spectators by a unitary. The reduced vacuum commutes with left translations. Twirl $P$ under them to obtain $T$, with $0\le T\le I$, $\operatorname{Tr}T=r$, and $\operatorname{Tr}(\sigma_eT)=\operatorname{Tr}(\sigma_eP)$. For any bounded nonnegative multiplier $w$,
$$\operatorname{Tr}(T^{1/2}M_wT^{1/2})=r\int_G w\,dh.$$
Indeed, expand the original projector in an orthonormal basis of its range, average the squared modulus of each translated basis function, and use Fubini. Truncation and monotone convergence extend the positive trace identity to unbounded $w$ whenever the integral is finite.

Set $w=(v_y+\delta)^{-1}$ with $\delta>0$. Splitting this bounded multiplier at $M\ge1$ and using operator norm at most trace for the high positive part gives
$$\begin{aligned}
\|T^{1/2}M_{\sqrt w}\|^2
&=\|T^{1/2}M_wT^{1/2}\|\\
&\le M+r\int (v^{-1}-M)_+\,dh
\le M+\frac{Cr}{d/2-1}M^{1-d/2}.
\end{aligned}$$
The last integral is bounded by integrating the Haar small-ball estimate from $M$ to infinity; $d>2$ is essential here. For rank $r\ge1$, choose $M=r^{2/d}$. Apply the operator to $M_{\sqrt{v_y+\delta}}\Omega(\cdot,y)$, integrate in $y$, and let $\delta\downarrow0$. This proves
$$\operatorname{Tr}(\sigma_eP)\le C' r^{2/d}u_p.$$
In particular every retained fraction $q$ imposes the lower rank estimate. For the upper estimate use the spectral subspace of $-\Delta_e$ below $C_q\sqrt{g_G}$ and Markov's inequality with $K_e$. The elliptic eigenvalue counting estimate on compact $G$ bounds its dimension by $C(1+C_q\sqrt{g_G})^{d/2}$. The same counting bound, integrated against the exponential, gives $\operatorname{Tr}\exp(t\Delta_e)\le C' t^{-d/2}$ for $0<t\le1$. [Hörmander, The spectral function of an elliptic operator](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6063-11511_2006_Article_BF02391913.pdf)

For defining $SU(2)$ the Haar density of $v$ is $2\sqrt{v(2-v)}/\pi$ on $[0,2]$. Thus the small-ball constant can be taken to be $C_0=4\sqrt2/(3\pi)$. The splitting estimate holds for every $M>0$ with this global bound. Optimizing $M+2C_0rM^{-1/2}$ gives the explicit inequality $\operatorname{Tr}(\sigma_eP)\le 3(C_0 r)^{2/3}u_p$. The one-cycle controls sort all reduced-state eigenvalues including magnetic degeneracy before testing this bound. [Numerical controls](check_shells.py)

## Entropy with a bounded remainder

Let $s_i$ be the decreasing eigenvalues of $\sigma_e$, starting with $i=1$, and put $F(r)=\sum_{i\le r}s_i$. Apply the projector estimate to the leading $r$ eigenvectors. Write $R=(C'u_p)^{-d/2}$. For the random positive integer $I$ with probabilities $s_i$, one has $s_i\le1/i$ and $S\ge\mathbb E\log I$. Integration of the lower tail gives
$$\mathbb E(\log(R/I))_+\le\int_0^\infty F(\lfloor Re^{-t}\rfloor)\,dt\le\int_0^\infty e^{-2t/d}\,dt=d/2.$$
Thus $S\ge\log R-d/2\ge(d/4)\log g_G-O(1)$. The Gibbs entropy inequality gives $S\le tK_e+\log\operatorname{Tr}\exp(t\Delta_e)$, with finite right side; it also follows by dephasing in a kinetic eigenbasis and applying the classical Gibbs bound. Take $t=g_G^{-1/2}$.

## Joint link factors

Fix $m$ marked edges forming a forest. Assume each has an incident plaquette containing none of the other marked edges. Site gauge transformations act transitively on $G^m$ on a forest: set a gauge value at a root and solve successively at the other vertices. The Haar twirl over the vertex group therefore averages each squared basis function to its $G^m$-Haar mean. With the spectators fixed, the chosen $m$ face coordinates are independent Haar isometric changes of the corresponding link coordinates under the **reference** product measure. Consequently $v_\Sigma=\sum_i v_{p_i}$ has $\operatorname{Haar}\{v_\Sigma<s\}\le C^m s^{md/2}$ and vacuum mean at most $mC/\sqrt{g_G}$. Repeat the rank proof with $d$ replaced by $md$. The kinetic heat trace for the sum of the $m$ marked Laplacians factors, and its mean is bounded by $mC\sqrt{g_G}$. One obtains
$$r_{q,\mathrm{joint}}\asymp_{G,\rho,q,m}g_G^{md/4},\qquad S_{\mathrm{joint}}=(md/4)\log g_G+O_{G,\rho,m}(1).$$
Subadditivity bounds $\sum_e S_e-S_{\mathrm{joint}}$ between zero and a constant for such fixed sets. This allows finite nonzero mutual information; it supplies no physical-distance decay estimate. The proofs concern fidelity inside the original extended link factors. Gauge fixing on a maximal tree changes those factors, and approximating selected energy levels is a different criterion. [D’Andrea et al., maximal-tree Hamiltonian truncation](https://doi.org/10.1103/PhysRevD.109.074501) · [Tong et al., dynamical truncation estimates](https://arxiv.org/abs/2110.06942)
