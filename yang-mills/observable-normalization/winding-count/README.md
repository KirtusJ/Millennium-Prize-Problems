# Counting the minimal witnesses for two electric charges

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For the charge $h=(1,1,0)$ in G4's occupied-slab comparison, independent Bernoulli bonds at probability $p$ on the fixed periodic cubic graph satisfy
$$
 \Pr_p(h\in W(B)) =
 \big[L^2\tbinom{2L}{L}+L^4-2L^3\big]p^{2L}+O_L(p^{2L+2}).
$$
On side four the leading coefficient is **1,248**. The corresponding minimal electric spin-network space has dimension **1,312**. The difference comes from the second invariant coupling at each of the 64 crossing supports. These are fixed-box statements for the spatial graph of the Wilson regulator, in G4's even-side range $L\ge4$. The probability gives an upper bound on the charged transfer norm. Its leading coefficient describes the independent-bond comparison. [G4's occupied-slab proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/25d2f03b2047c55992f72a6bd384deae14543684/yang-mills/g4/winding-flux/slab.md) · [Electric decomposition](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/25d2f03b2047c55992f72a6bd384deae14543684/yang-mills/g4/winding-flux/electric.md)

## Support and frequency of bends

A witness is an even-degree edge subset with winding parity $h$. It uses an odd number of edges on each of the $2L$ charged cuts. At minimal size it uses exactly one on each, with no links in the third direction. Decomposition into simple edge-disjoint cycles exhausts the length budget. Either there are two straight axial lines, or there is one simple cycle winding in both directions. In the latter case all steps in each coordinate have a common sign and the path lies in one plane. A cycle with zero winding cannot occur in either decomposition because it would spend edges needed by the charged cuts.

To resolve simple cycles by their shape, orient the path to move positively in $x$ and mark the start of one of its $k$ runs of consecutive $x$ edges. The ordered lengths of the $x$ runs form a composition of $L$ into $k$ positive integers, as do the $y$ runs. Choose a starting vertex and either vertical sign. For $k\ge2$ the resulting path is simple. A proper cyclic subpath returning to its starting vertex would have to spend all $L$ steps along one axis and zero along the other. No run has that length. Forgetting the distinguished start divides by $k$, even for repeating words, since the marked vertices are distinct. Thus the number with $2k$ bends is
$$
 S_k=\frac{2L^3}{k}\binom{L-1}{k-1}^2,\qquad 2\le k\le L .
$$
Equivalently, counting rooted words gives $2L^3[\binom{2L}{L}-2L]/(2L)$ simple cycles in total. At $L=4$ the four-, six- and eight-bend counts are 576, 384 and 32. Add $L^4$ pairs of axial lines for the support count. Of these pairs $L^3$ cross at a single vertex. The tensor product of four spin halves has a two-dimensional invariant space there; all two-valent vertices have a unique coupling. Counting that extra state gives G4's dimension.

For each minimum witness the event that it is occupied has probability $p^{2L}$, including arbitrary extra occupied bonds. Two different such witnesses have symmetric difference a nonempty even subgraph. The simple cubic torus has girth four, so the difference contains at least four edges and the union contains at least $2L+2$. Any nonminimum witness has at least $2L+2$ edges by cut parity. A finite union bound on those larger witnesses and the pairwise Bonferroni bound on the minimum witnesses give the expansion above. This also explains why its degree-$2L+1$ coefficient vanishes. The graph-dependent remainder does not provide a uniform small-coupling expansion as $L$ grows.

## Independent check on PCP OS

The [native workers](worker.c) count by a row sweep. Within a common plane, write $a,b$ for the columns of the incoming and outgoing vertical edge of a row. The horizontal edge mask must have binary boundary $\{a\}\mathbin{\triangle}\{b\}$. Track the already occupied horizontal cuts and reject a repeated cut. Close the last row against the first and require that every horizontal cut was used. A change $a\ne b$ contributes two bends. Translation restores the fixed initial column and plane. The zero-change case puts a horizontal ring across one vertical line. Pairs of rings in different planes are counted separately.

The root, child and grandchild ran the sweep on sides 4, 5 and 6 under separate PCP OS boots. Each checked every bend count and the total rank before emitting its proof fragment. The odd side is an extra finite counting control. The ranks were 1,312, 6,800 and 34,344. A second [three-guest replay](../transfer-increments/replay-guests.py) reproduced [WindingCount.lean](WindingCount.lean), SHA-256 `772e1289b004860e61fe4795c9f6d44185b810969b9ab8ff5924da4f308a42a4`. Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked the three finite rank values. The general counting and probability arguments are given above. A4 also recompiled G4's nine supporting declarations and reran G4's distinct cut-based enumeration and signed-kernel controls at the linked commit.
