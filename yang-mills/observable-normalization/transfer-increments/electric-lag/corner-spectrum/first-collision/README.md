# The first non-Gaussian moment of a finite square

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Let $\nu_\ell$ be A4’s distribution of first-order energy slopes weighted by a fundamental square of side $\ell\ge2$. Use the finite even periodic SU(2) lattice with $L\ge4\ell$, fixed temporal coupling $g>0$, and take the spatial magnetic derivative at zero. The first moment differing from that of $N(0,1/4)$ is exactly order $2\ell$. Its value is

$$
\int s^{2\ell}\,d\nu_\ell(s)
=\frac{(2\ell-1)!!}{4^\ell}-\frac{4}{16^\ell}\binom{2\ell}{\ell}
=\frac{(2\ell-1)!!}{4^\ell}\left(1-\frac{4}{2^\ell\ell!}\right).
$$

For example the side-two fourth moment is $3/32$, half the Gaussian value. At side three the sixth moment is $55/256$, compared with $15/64$. The correction comes from attempts to remove the last occupied cell on one original side. It gives the first non-Gaussian cumulant as well, since all lower moments agree. The observable is an excited perimeter-cluster response at fixed regulator. [Definition and normalization](../README.md) · [Lower moments and sign symmetry](../b4-review/README.md)

## Which contacts change the last step?

Let $B=-PAP$, with $P$ the whole electric spectral projection at $r=q^{4\ell}$ and $A$ half the sum of fundamental plaquette traces. Then the moment is $\|B^\ell f\|^2$ for the initial square trace $f$. Through $\ell-1$ steps the existing result identifies the states with four corner Young diagrams. Their total size is at most $\ell-1$. Consider a test cell before the last step. Its edges on the boundary are exactly the interfaces with opposite occupancy. Faces outside the square or normal to its plane still meet at most one edge.

Suppose a retained cell has removed neighbors belonging to two different diagrams of sizes $m,n$. A path from one original corner to the other through these two neighbors and the test cell has length at most $(m-1)+2+(n-1)=m+n\le\ell-1$. Opposite corners are farther apart. Adjacent corners attain this bound only by going straight along their common side. Equality uses the entire removal budget. All cells on that side except the test cell have been removed. The same equality occurs if a removed neighbor from one corner influences a test cell on one of that corner’s two far sides. Reaching the far side takes at least $\ell-1$ steps from the corner and at most $m$ via the removed neighbor. The test cell is then the last occupied cell of the side, at its far end. This includes a diagram of size zero at the second corner.

A removed test cell cannot have an edge-neighbor in another diagram, since that would join the corners in at most $m+n-1$ steps. It cannot reach a far side either. Away from the last-cell case, the previous one-corner occupancy argument therefore applies: two boundary edges are adjacent and toggle exactly one addable or removable diagram cell. In the exceptional case the remaining cell has three consecutive boundary edges, including the exterior edge of the original side. Either neighboring diagram would formally allow its addition.

## The full electric projection kills the three-edge contact

Orient the common path consistently and write $X$ for the product of its three links. The two traces contain $X$ and $X^{-1}$, so the shared dependence decomposes into one singlet and one spin-one representation of the path product. In particular the triplet carries spin one on **each** shared link. If $a=I_3(g)/I_1(g)$ and $q=I_2(g)/I_1(g)$, the electric multipliers relative to $r$ are $q^{-2}$ for the singlet and $q^{-2}a^3$ for the triplet. Three old fundamental factors disappear and one new fundamental factor appears. The first ratio exceeds one and the second is strictly less than one because $0<a<q<1$. Hence the entire $r$-projection vanishes for this contact at every allowed coupling. The ordinary two-edge case still has amplitude $-1/4$ in $B$. [Shared-path calculation](../../bends/README.md) · [Soni’s modified Bessel inequality](https://doi.org/10.1002/sapm1965441406)

## Counting the missing amplitude

In the formal four-diagram walk, all paths ending at a deleted full side use exactly $\ell$ additions. The end state records how many cells were removed from each end. For the split $h,\ell-h$, the number of paths is $\binom{\ell}{h}$ because growth from either corner has a fixed linear order. Every such path is legal until its last move, which has just been projected out. Conversely every projected-out formal move finishes one of these states. There are four choices of side. The sum of their squared unnormalized amplitudes is $4\sum_{h=0}^\ell\binom{\ell}{h}^2=4\binom{2\ell}{\ell}$.

For $\ell\ge3$, all other final diagrams give distinct simple loop boundaries. To see why their boundaries cannot pinch, let a corner cell have inward coordinates $(i,j)$ starting from zero. Its diagram needs at least $i+j+1$ cells. For two adjacent corners, contact even at a vertex requires the two inward coordinates along their common side to sum to at least $\ell-2$. The total size bound $\ell$ then forces both transverse coordinates to be zero, equality in the count, and deletion of the full side. For opposite corners contact requires the same $\ell-2$ lower bound in each coordinate, costing at least $2\ell-2>\ell$. A single diagram reaching the opposite side also uses the entire budget on a straight row. In all remaining cases the four simple staircase detours stay apart. The filled region recovers the corner components and the boundary recovers the region using the prescribed exterior. Different boundaries have a private edge and are Haar-orthogonal. Each trace has unit norm.

At $\ell=2$, each of the four possible first detours has one return move to the original square. Removing opposite corners in either order leaves two unit loops meeting at one vertex. Following the oriented detours in either order gives the same single trace $\operatorname{Tr}(U_1U_2)$ up to cyclic permutation, with both lobes carrying the inherited orientation. The lobe holonomies are independent Haar variables, so this trace has unit norm. The two choices of diagonal and the original square are orthogonal by private edges. The squared count is $4^2+2^2+2^2=24$.

Dividing the missing squared count by $4^{2\ell}$ gives the claimed correction to the Gaussian moment. The formal norm comes from the four Young lattices and their raising/lowering commutator. The physical deficit depends on the SU(2) projection above. [Stanley, *Differential Posets*](https://math.mit.edu/~rstan/pubs/pubfiles/77.pdf)

## Checks

An independent enumeration carries **ordered vertex words**, keeping the detour pairing at a self-intersection. At sides 2 through 9 it found exactly $4\ell$ three-edge contacts at the last step, weighted by $4\,2^{\ell-1}$ incoming walks. It reproduced every squared norm and found exactly the two predicted pinched words at side two. Three native PCP OS guests separately checked occupancy walks at sides two and three, the singlet trace contraction on the quaternion subgroup, and the binomial squared count through side twelve. [Ordered-word enumeration](check.py) · [Native checks](worker.c) · [Expected output](checks.txt)
