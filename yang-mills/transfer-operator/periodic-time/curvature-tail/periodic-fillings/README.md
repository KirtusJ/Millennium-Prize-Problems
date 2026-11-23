# Based-loop fillings on G4’s periodic four-cube

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Disposition for PR #13.** Equation (1) of G4’s compact-integral proof holds for every fixed integer side $L\ge1$, including the one-site model and the parallel links at side two. The review below reconstructs the noncommutative fillings of every residual link and all six anchor commutators. It gives explicit constants for the global comparison and examples showing why those constants must depend on box size. The reviewed proof is identical at the requested commit and its determinant follow-up. [G4’s proof at e850219](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/e8502191d7a169ed0e81f7998baffaa8d648419f/yang-mills/g4/periodic-zero-modes/proof.md) · [PR #13](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/13)

Asano and Nishimura study Wilson loops and toron zero modes in periodic four-dimensional lattice gauge theory. Gubarev treats a lattice non-Abelian Stokes theorem for SU(2). The comparison here uses only elementary square exchanges and the bi-invariant chordal metric. It does not use a perturbation expansion. [Asano and Nishimura](https://arxiv.org/abs/2303.01008) · [Gubarev](https://doi.org/10.1103/PhysRevD.69.114502)

## Constructive bounds

Put $V=L^4$, $D(g)=|g-1|^2/2$ in unit-quaternion coordinates, $S=\sum_p D(U_p)$ and $T=S_1+\sum_eD(h_e)$ with G4’s tree, anchors and ordering $h_e=U'_e B_e^{-1}$. Then
$$
 T\le [6V(L-1)+6L^2]S,\qquad S\le (L^2+24)T.
$$

**First direction.** Write $P_x$ for the positive axis-ordered tree path to $x\in\{0,\ldots,L-1\}^4$. For a positive $i$-edge from $x$ to $y=x+e_i\bmod L$, start with word $A=P_x i$. Use target $B=P_y$ for an ordinary edge and $B=i^L P_y$ for a wrap. The two words have identical displacements in the covering lattice. Their ratio $U(A)U(B)^{-1}$ equals $h_e$ in the common root frame. In particular the inverse anchor occurs on the right after forming the tree loop.

For a path segment with prefix $P$, the exchange $PabQ\mapsto PbaQ$ costs one factor $U(P)H_{ab}U(P)^{-1}$ on the left, where $H_{ab}$ is the oriented square based at the end of $P$. This follows by cancelling the common suffix. Multiplying these factors in exchange order gives the original transport times the inverse final transport, with no commutativity assumption.

Commute the appended step back across the suffix of coordinates $j>i$. This costs $\sum_{j>i}x_j$ exchanges. On a wrap, an $i^L$ block now precedes that suffix. Move it to the front across all earlier coordinates at cost $L\sum_{j<i}x_j$. For a fixed $j$ the crossed faces are a strip of width one or $L$ and length $x_j<L$. Its lower corners in the two moving coordinates are distinct modulo $L$, including the strip of full width. Strips of different $j$ have different orientations. Thus **each individual filling uses distinct periodic faces**. Tree links and anchors have zero cost in this construction. Summing the suffix terms over all positive edges yields $3V(L-1)$, since there are six ordered pairs $i<j$ and the mean of $x_j$ is $(L-1)/2$. Summing the prefix terms over wraps gives another $3V(L-1)$.

For $[g_i,g_j]$ transform $i^Lj^L$ to $j^Li^L$ using the full $L$ by $L$ rectangle in the cover. All $L^2$ faces are distinct on the torus. At $L=1$ the projected square is the word of the two one-site generators. At $L=2$ the positive link is indexed by its starting site and direction, so two positive parallel links remain distinct. Each word of $m$ conjugated face factors satisfies $D(\mathrm{word})\le m\sum_{p\text{ used}}D(U_p)\le m S$ by the triangle inequality, conjugation invariance and Cauchy–Schwarz. Adding the costs proves the first inequality.

**Reverse direction.** Replace the four links on each face by their backgrounds one at a time. The distance error of either orientation is $|h_e-1|$. The background contributes a commutator only at a double wrap. Each coordinate pair has $L^2$ such faces, so the sum of squared background distances, divided by two, is $L^2S_1$. Each positive link occurs six times among all face boundaries, counting repetitions at side one. By Cauchy–Schwarz on each four-term sum, followed by the triangle inequality in the space of square-summable face distances,
$$
 \sqrt S\le L\sqrt{S_1}+\sqrt{24\sum_eD(h_e)}
 \le \sqrt{(L^2+24)T}.
$$
Together the inequalities identify the same zero set and provide G4's fixed-box coercivity input. The partition-function prefactor and the plaquette coefficient require the other steps of G4's proof.

## Forced size dependence

* For a pure background $h_e=1$, choose two noncommuting anchors. Then $S/T=L^2$ exactly. The optimal constant bounding $S/T$ is therefore between $L^2$ and $L^2+24$.
* For the other direction let $L\ge2$. Along the root axis of the **last** tree direction give each positive edge holonomy $\exp(i\theta\sigma_3/L)$; all other edges carry identity. Exactly $6L$ plaquettes have defect $1-\cos(\theta/L)$. The anchor in the last direction is $\exp(i\theta\sigma_3)$. At the $L^3-1$ off-axis wraps in that direction both tree paths avoid the root-axis links, and the residual equals the inverse anchor. Hence, as $\theta\to0$, the optimal constant bounding $T/S$ is at least $L(L^3-1)/6$. The constructive upper bound above is of order $L^5$; the sharp exponent for this direction remains open in this review.

## Reproducibility

The Python checker builds periodic links in the permutation group on three letters. For every positive edge and anchor pair it independently uses stable adjacent exchanges to reach the target. It checks ordered products with conjugators, absence of repeated faces within each filling, and the complete area count. [Checker](check.py)

| Side | Positive edges | Anchor pairs | Unit-square exchanges |
|---:|---:|---:|---:|
| 1 | 4 | 6 | 6 |
| 2 | 64 | 6 | 120 |
| 3 | 324 | 6 | 1,026 |
| 4 | 1,024 | 6 | 4,704 |
| 5 | 2,500 | 6 | 15,150 |

The PCP OS parent independently sums chord areas, its child checks conjugation on 1,296 permutation assignments, and the grandchild counts the double-wrap sheets and isolated-axis action faces through side 16. The host relay starts each descendant after the preceding guest’s request. [Native source](worker.c) · [Expected output](checks.txt) · [Three-boot relay](../../../../observable-normalization/transfer-increments/replay-guests.py)

```sh
python check.py
python ../../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```

All three guests exited zero on the completed chain, with 47 kernel-register events per guest. Two earlier boots entered SAFE during keyboard self-tests before admitting the requested guest. The successful retry used the same kernel, payloads and launch settings.

| Guest | Executable SHA-256 | Register head |
|---|---|---|
| Parent | 29859bc49b11c692c48b0dd558d32b92675cd17ebd3aa855b6753281a3aa8ea4 | 2ec6fbb7954cbfc1efa9034bad1c166ee634419500c345c2c7057de8105c0122 |
| Child | b8c9434f5caa0c9de82a5aaa909d805031f1e4913db3ffa87aea5da9f15cf1a0 | 25138e8a1fc246d976013568cad8601f8096375aaee6456bced63c0b07e1188a |
| Grandchild | ab8924be110194549cf6cab4b25f0bfd2e23c898d23bdae8790de049f0ec6260 | bd4f528370bee8ec309c658965f3c746bc51511c7b0fa580f8442d7d73f36eb6 |
