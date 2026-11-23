# The weighted Gaussian retraction

Use the retraction, curvature projection $\Pi$ and spacetime update exteriors of [the original proof](../full-complement/gaussian.md). Let $S_{pe}$ be the oriented coefficient of spatial face $p$ in the retraction of fine edge $e$, $R_p=\sum_e|S_{pe}|$, and $w_e=\sum_p R_p|S_{pe}|$. If $m_e$ is the number of the 24 colours that cover $e=(x,i)$, then
$$m_e=2\#\{j\ne i:x_j\text{ odd}\}.$$
For each odd transverse coordinate $j$, both incident $ij$ faces select $e$ at their odd-odd corner. Their base parities differ and give two distinct colours. An even transverse coordinate contributes none.

For each base parity the following pairs are $(m_e,w_e)$ in direction order. Starting from the positive word of the deposited retraction, each adjacent interchange inserts its oriented face. Summing absolute coefficients at each face gives $R_p$. Feeding these row counts back through the incidences gives the second member of each pair. The calculation checks the signed boundary of each column separately. [Integral enumeration](weighted.py) · [Swap rule](../full-complement/retraction.py)

| Parity | $x$ edge | $y$ edge | $z$ edge |
|---|---|---|---|
|000|(0,0)|(0,0)|(0,0)|
|001|(2,3)|(2,2)|(0,0)|
|010|(2,4)|(0,0)|(2,0)|
|011|(4,5)|(2,1)|(2,3)|
|100|(0,0)|(2,0)|(2,0)|
|101|(2,1)|(4,2)|(2,5)|
|110|(2,2)|(2,6)|(4,0)|
|111|(4,3)|(4,7)|(4,8)|

Translation by two repeats the signed stencil. Each word lies in the three-dimensional box of coordinate widths at most two starting at the even root. On side six no two faces of one column become identified at a seam. Each target face receives one copy of every contribution with its parity on the infinite cover, since the corresponding source translates by the same even displacement. This applies to every even side of at least six. The side-two table used for the parity calculation agrees with the side-six table. The explicit checks on sides 6, 8, 10 and 12 cover 10,368 edges, including seams. Equality at parity 110 in direction $y$ is equality of the counting bound $w_e\le3m_e$.

Cauchy–Schwarz in each row, followed by the table, gives
$$\|Sc\|^2\le\sum_e w_e|c_e|^2\le3\sum_e m_e|c_e|^2.$$
For a closed contractible current $c$, the orthogonal residual variance is at most $\|\Pi Sc\|^2$. A colour uses disjoint pairs of curvature variations with Gram blocks of diagonal 6 and off-diagonal $\pm1$, so the inverse is at least $I/7$. Summing the lost variances over all colours with their actual multiplicities gives $J_{\rm avg}\ge\sum_e m_e|c_e|^2/168$. Consequently $J_{\rm avg}\ge\|Qf\|^2/504$ on first chaos.

Each compressed exterior prediction is a positive contraction fixing the coarse first chaos. Its tensor powers preserve the sectors of coarse and orthogonal factors. In a sector containing a residual factor, retain one such factor, bound the others by the identity, then average the colours. This proves the same constant in every chaos. The estimate includes three independent Gaussian colours, spatial contractible circulation observables and the fixed-volume time vacuum. Harmonic windings and the interacting Wilson measure remain separate. The stronger Gaussian transfer lower bound for the actual two-step physical defect in the earlier rendezvous uses a different quadratic form. [Gaussian transfer discussion](../full-complement/rendezvous.md)
