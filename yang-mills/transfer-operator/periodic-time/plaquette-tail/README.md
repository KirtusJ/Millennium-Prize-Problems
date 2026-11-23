# Dyadic reflections and a uniform exponential moment for one Wilson plaquette

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Disposition.** The chessboard lemma, the fourfold face multiplicity, and the application to the one-plaquette tail in Z4’s Part II hold for the stated dyadic periodic SU(2) limit states, with the previously corrected forest recursion. An additional bound in the same state class is
$$
 \mathbb E_\mu e^{3O_p/10}\le 6^{9/2},\qquad
 \mu(O_p>t)\le \min\{1,6^{9/2}e^{-3t/10}\}.
$$
Here $O_p=\beta(1-\tfrac12\mathrm{Tr}\,U_p)$, $\beta>0$, and the thermodynamic limit is taken at fixed coupling. The estimate uses the positive Wilson measure itself. Neither a mass gap nor H3 or H4 enters. [Z4’s Part II](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2d3e65698f41a398bee4264ccfe685999ecb0a9f/yang-mills/z4/attempt/paper/sec_proof.tex) · [Fröhlich, Israel, Lieb and Simon on reflection positivity and chessboard estimates](https://www.math.caltech.edu/SimonPapers/93.pdf) · [Earlier periodic pressure estimates](../../../central-quotients/tangent-curvature/periodic-limit/pressure.md)

## Check of the manuscript proof

For a site reflection at $r$, a block with lower coordinate $t$ maps to the block with lower coordinate $2r-1-t$ modulo $L$. This reverses the parity of $t$, exactly as the alternating block orientation requires. A closed block may touch the reflection plane, since the half-space algebra includes its boundary links. Conditional integration over those common links gives the nonnegative squared norm in Z4’s reflection lemma. For a real nonnegative block insertion, reflection Cauchy–Schwarz with the constant function therefore squares its expectation at the cost of doubling the set of blocks. At the $i$th step the occupied interval $[1-2^i,0]$ and its reflected interval $[1-2^{i+1},-2^i]$ have disjoint block indices. They fit in opposing half-tori because $2^i\le L/2$. Four runs of $\log_2 L$ steps cover all $V=L^4$ blocks. The symbol $\theta_a S$ in the doubling and iteration paragraphs should be $\theta_r S$.

Take the $(1,2)$ face at the lower corner. The in-plane lower coordinates run through all residues. Each transverse lower vertex in directions 0 and 3 maps to the even endpoint of its block interval, with two preimages independently. The target set $A$ thus consists of $V/4$ distinct faces, each hit four times. For the indicator of $O_p>t$ repeated factors coincide. On their common event the total action times $\beta$ exceeds $Vt/4$. Splitting off half the action gives the manuscript’s $-t/8$ and the pressure difference. In temporal forest gauge the upper bound retains $3L^3$ open chains of $L-1$ plaquettes, and the lower bound restricts $3V+L^3$ remaining links. The difference of the logarithmic powers of $\beta$ per site is $6\log(\beta)/L$. It vanishes in the stated order. At fixed coupling the event is open, so Portmanteau passes the upper bound to each limiting state.

## A stronger moment from the same copies

Write $D(g)=|g-1|^2/2$ in unit-quaternion coordinates, $S=\sum_fD(U_f)$, $X=\sum_{f\in A}D(U_f)$, and $S_t$ for the sum over temporal faces. For $j=3,0$, use each of the two elementary three-cubes adjoining $f\in A$ in direction $\pm j$. In each cube a face holonomy factors into the five other face holonomies with orientations and conjugations: remove that face and use the five-face disk as its filling. The bi-invariant chordal metric and Cauchy–Schwarz give $D(U_f)\le 5\sum_{g\ne f\ \mathrm{in\ cube}}D(U_g)$.

In the sum of these inequalities for fixed $j$, each target is counted twice. The opposite faces are the $(1,2)$ faces with odd $x_j$ and the other transverse coordinate even. Each occurs twice. The lateral faces of type $(1,j)$ or $(2,j)$ in those slabs each occur twice from the two adjacent in-plane cells. Hence $X\le5S_{B_j}$, with $B_j$ the set of those opposite and lateral faces, counted once. $A,B_0,B_3$ are pairwise disjoint, and $B_3$ contains only spatial faces. For $0\le h<1$ put $q=(6+h)/20$. Paying for $X/5$ from $B_3$ and $hX/5$ from $B_0$ gives the pointwise inequality
$$
 S-4qX\ge(1-h)S_t .
$$

Apply chessboard copying to $e^{qO_p}$, which is bounded at each fixed $\beta$. Its fourfold repeated factors give $e^{4q\beta X}$. Define $z(b)=\int e^{-bD(U)}dU$ for probability Haar measure. Drop wrapping temporal faces and integrate the remaining temporal chains in forest gauge. With $Z_L$ the unmodified Wilson partition function,
$$
 (\mathbb E_{\beta,L}e^{qO_p})^V
 \le z((1-h)\beta)^{3V-3L^3}/ Z_L(\beta).
$$

For a lower bound on $Z_L$, give each of the $M=3V+L^3$ unpinned links an independent density $e^{-6\beta D(U)}/z(6\beta)$. Its mean matrix is $bI$ with $0\le b\le1$: the measure is central and inverse symmetric, and pairing $U$ with $-U$ makes the tilted mean of the scalar part nonnegative. The inverse link has the same mean. Each plaquette uses distinct unpinned links for $L\ge4$. With $k$ such links its expected deficit is $1-b^k\le k(1-b)$. Each unpinned link occurs in six plaquettes, hence $\mathbb E S\le6M(1-b)$. Changing to this product measure and applying Jensen gives
$$
 Z_L(\beta)=z(6\beta)^M\,\mathbb E\exp\!\left(6\beta\sum_{e\ \mathrm{unpinned}}D(U_e)-\beta S\right)\ge z(6\beta)^M.
$$
Taking $V$th roots before the limit gives $\mathbb E_\mu e^{qO_p}\le[z((1-h)\beta)/z(6\beta)]^3$; the single-face test is bounded and continuous for fixed $\beta$.

For SU(2), $r=2\sin(\alpha/2)$ gives $D=r^2/2$ and radial Haar density $(2/\pi)r^2\sqrt{1-r^2/4}\,dr$ on $[0,2]$. After scaling $u=\sqrt b\,r$, the integrand of $b^{3/2}z(b)$ increases pointwise with $b$, if extended by zero beyond its support. Consequently
$$
 \mathbb E_\mu e^{(6+h)O_p/20}\le\left(\frac{6}{1-h}\right)^{9/2}.
$$
At $h=0$ this gives the displayed bound. For $t>90$, taking $h=1-90/t$ in Markov’s inequality gives $(et/15)^{9/2}e^{-7t/20}$. These constants give sufficient moment bounds. No optimal decay exponent is asserted.

## Verification

The native PCP OS parent checked the dyadic interval partition and transverse multiplicities through side 64. The child counted the two neighboring cube fillings on all spatial face types at sides 4, 8 and 16. Axis interchange gives the same count in the other transverse direction. The grandchild checked the product-mean inequality on rational inputs and the two temporal seam counts. The host relayed both child requests. All three guests exited zero with 47 register events each. [Native source](worker.c) · [Expected output](checks.txt) · [Three-boot runner](../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Register head |
|---|---|---|
| Parent | 8c639b065579e7e64d86bbb2844afa2789dca7ac2895a19648d1457228c48379 | 76db8371af7928b0601cae7ee735638dca3df85f20191ecc2560c1bbf8e513d1 |
| Child | 2f1bfe1740c98a6fa37bf6381d737919e674f815db2d8073a2754f8bc43b352c | 67e1c7640fb89a1049a7b40856c0c5f70a2fbfa4540694bafbf560f65faba638 |
| Grandchild | 0f1004e80a5662e9599b6645e4f78b285ab6ce8f4a635ddea4b07e4c8c7b8769 | 908f082683cd39e311230f749d1efb69213a9ddfc61d2a730e6ccbe57f192f98 |
