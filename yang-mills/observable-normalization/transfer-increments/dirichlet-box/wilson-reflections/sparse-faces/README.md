# Uniform Wilson plaquette exponential moments below 9/5

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Let $Y_p=\beta(1-\operatorname{Re}\operatorname{Tr}U_p/N)$ for the isotropic Wilson measure in four dimensions. In any thermodynamic limit of periodic boxes of dyadic side, for fundamental SU(2) and $0\le\lambda<9/5$,

$$
\mathbb E_\mu e^{\lambda Y_p}
\le \left(\frac{6}{1-5\lambda/9}\right)^{1152}.
$$

The constant is large. The gain is the interval of exponents. For example, in the weak-coupling limit $\mathbb E e^{Y_p}\to 2^{3/2}$. The earlier estimate bounded that endpoint moment but did not imply its convergence. The statement is local and gives no lower bound for the mass gap. [Earlier one-face estimate and its obstruction](../moment.md) · [Rooted Wilson moment comparison](../../../local-action/README.md)

## What the surrounding cubes contribute

Write $s(U)=\|I-U\|_{\rm HS}^2/(2N)$. The chord $\sqrt{s}$ is invariant under conjugation and inversion, and $\sqrt{s(UV)}\le\sqrt{s(U)}+\sqrt{s(V)}$. In a three-dimensional elementary cube, the five faces complementary to $p$ form a disk spanning the boundary of $p$. Their oriented holonomies, transported to one base point and ordered along the boundary, multiply to the holonomy of $p$ or its inverse. One construction starts with the opposite square and attaches its four side squares in cyclic order. Each attachment replaces the common boundary path by the other path around that square. The two boundary words therefore differ by a conjugated face word. This works for noncommuting links. Telescoping the chord and applying Cauchy gives

$$s(U_p)\le5\sum_{q\in\partial c,\ q\ne p}s(U_q).$$

In four dimensions there are four such cubes, one on each side in each transverse direction. Their twenty complementary faces are distinct. The total action on the marked face and those twenty faces is at least $9s(U_p)/5$.

This coefficient is sharp **for the 21-face comparison**. In an abelian subgroup prescribe signed curl $\epsilon$ on the middle square and signed curl of magnitude $\epsilon/5$ on each complementary face so that its oriented cube sum vanishes. These values are attained by link angles. Each disk can be filled consistently with the same middle boundary links because the oriented face sum on its cube is zero, and the cubes share only that middle face and its subfaces. The exact incidence solve in the check below also constructs such links. The action ratio on the patch is $1+20\sin^2(\epsilon/10)/\sin^2(\epsilon/2)\to9/5$. The same example lies in diagonal SU(2). It gives no upper restriction on the actual moment at $9/5$.

## Reflection and pressure

Partition the dyadic torus of side $L\ge8$ into $M=(L/4)^4$ closed cells of side four. In the reference cell place the face along the first two axes at base $(1,1,2,2)$. Its four surrounding cubes are strictly interior, with vertex coordinates between one and three on each axis. Site reflections in the boundary planes of the cells replicate the marked face while keeping the 21-face patches disjoint. The dyadic doubling proof applies to a bounded nonnegative test in the cell. At scale four a reflection in plane $4r$ sends cell index $j$ to $2r-1-j$. Each doubling squares its expectation before extending the product to twice as many cells. After $4\log_2(L/4)$ doublings this gives $(\mathbb E e^{\lambda Y_p})^M\le\mathbb E e^{\lambda\beta P}$, where $P$ sums the marked deficits, one per cell. Reversing the face orientation preserves the real trace. [Z4’s dyadic proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/eafb765/yang-mills/z4/attempt/paper/sec_proof.tex#L135)

Bhattacharjee et al., Proposition 160, already use site reflection for coarse dyadic cells. Their displayed bound charges possible plaquette overlap and the absolute partition-function normalization. Here the twenty-one faces used in each cell are interior, and the normalized Wilson expectation is bounded by a pressure difference. [Coarse chessboard proposition, pp. 86–87](https://hexagonmath.org/pdf/2610.00341v6#page=86)

For the total deficit $S$ the disk argument gives $S\ge9P/5$ pointwise. Put $c=1-5\lambda/9>0$. Since $S-\lambda P\ge cS$, the last expectation is at most $Z_L(c\beta)/Z_L(\beta)$. Let $z(b)=\int e^{-bs(U)}dU$. Temporal-forest Haar integration bounds the numerator by $z(c\beta)^{3(1-1/L)L^4}$. The independent trial law on the free links bounds the denominator below by $z(6\beta)^{(3+1/L)L^4}$. Taking $M$th roots and sending $L\to\infty$ at fixed coupling gives

$$\mathbb E_\mu e^{\lambda Y_p}\le [z(c\beta)/z(6\beta)]^{768}.$$

The local observable is bounded and continuous at this first limit. For SU(2), $b^{3/2}z(b)$ increases with $b$ by the radial integral, giving the claimed exponent $768\cdot3/2=1152$. This argument uses dyadic periodic states throughout. [Forest and trial-pressure bounds](../moment.md)

## Consequences at weak coupling

* **Fundamental SU(2).** The earlier rooted moment comparison gives $Y_p\Rightarrow\chi_3^2/4$ in these states. For each $0<\lambda<9/5$, choose $\lambda'$ strictly between $\lambda$ and $9/5$. The moment at $\lambda'$ gives uniform integrability at $\lambda$, hence $\mathbb E e^{\lambda Y_p}\to(1-\lambda/2)^{-3/2}$. At $\lambda\ge2$ bounded truncations and the divergent Gaussian moment imply that the Wilson expectation tends to infinity. This leaves $[9/5,2)$ undecided.
* **U(1), defining character.** The same pressure ratio is bounded uniformly in $\beta$ for each fixed $c>0$. Indeed $z(b)=\pi^{-1}\int_0^\pi e^{-b(1-\cos u)}du$ satisfies $z(b)\asymp(1+b)^{-1/2}$ by the two quadratic bounds on $1-\cos u$ on this interval. A charged cube has at least one principal face angle of magnitude $\pi/3$ or greater, so $Y_p\ge\beta/2$ there. For any specified set of $K$ cubes the probability of any charge is at most $6K C_\lambda e^{-\lambda\beta/2}$. For a single cube the limsup of $\beta^{-1}\log\Pr(m_c\ne0)$ is at most $-9/10$, taking fixed $\lambda\uparrow9/5$ **after** the limsup. In particular all cubes are charge-free with probability tending to one in any predetermined family with $\limsup \beta^{-1}\log K<9/10$. Independence is unnecessary. This bounds local wrapping, without addressing long-distance mixing. [Z4’s winding argument](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/eafb765/yang-mills/z4/attempt/paper/sec_general.tex)

[Lean scope and reproducible controls](checks.md)
