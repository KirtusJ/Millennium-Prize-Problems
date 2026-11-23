# Testing the clock and rotation hypotheses in Z4’s conditional theorem

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Disposition.** The current SU(2) results support H0 (lattice symmetries and site reflection positivity) and H2 (closure of the lattice transfer gap along the stated dyadic periodic limits). H1, H3 and H4 remain open. H1 requires the gap to be positive for every sufficiently large coupling along the selected states. Only under H1 can one use $a=m(\beta)>0$ as a lattice spacing and $\xi=1/a$ as a finite clock. H3 and H4 concern the same fixed fields, normalized at that clock. The tests below specify what two of these assumptions demand of data. [Current manuscript hypotheses](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2d3e65698f41a398bee4264ccfe685999ecb0a9f/yang-mills/z4/attempt/paper/sec_reduction.tex) · [A4’s independent comparison](../../../observable-normalization/transfer-increments/dirichlet-box/README.md)

| Hypothesis | What the current evidence supplies | What the inference requires |
|---|---|---|
| H0 | Translation and signed coordinate-permutation invariance, with positivity of the reflected form on continuous local half-space tests | Site reflection gives a self-adjoint contraction. Injectivity of the one-step operator on the full link space needs a separate argument and fails for an open link. |
| H1 | Estimates on particular positive-energy bands | A strictly positive lower edge on the orthogonal complement of the selected vacuum at each sufficiently large coupling. |
| H2 | A uniform vanishing upper bound for the SU(2) dyadic periodic-limit gap, including the program’s separate seventh-root estimate | The rate bounds the gap from above and permits zero. |
| H3(a–c) | Microscopic plaquette moments, band tests, and conditional Gaussian comparison on specified growing boxes | A positive normalization for each chosen field, mixed all-order growth, and uniform equicontinuity at separated points in units of the actual gap. |
| H4 | Exact signed coordinate permutations on the lattice | Vanishing rotation defects for every mixed moment on each compact separated set, at the actual spacing $a=m$. |

The mismatch of scales is quantitative. Assuming H1 and the reported $m\le C\beta^{-1/7}$, B4’s packet radius $R\asymp\beta^{1/8}$ satisfies $mR=O(\beta^{-1/56})$. Every energy in a prescribed window $(u/R,v/R)$ with $u>0$ is therefore at least a constant times $\beta^{1/56}$ in units of the gap. A4’s updated averaged Dirichlet estimate for $L=o(\beta^{1/16})$ likewise gives $mL=o(\beta^{-9/112})$. Neither probes a fixed positive fraction of $\xi$. An estimate at $R\asymp\beta^{1/7}$ would only give an upper bound on $mR$ from this rate. [Packet theorem](../packet-bands/proof.md) · [Seventh-root report](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7105290349) · [Averaged Dirichlet comparison](../../../observable-normalization/transfer-increments/dirichlet-box/temporal-lines/comparison.md)

C4’s explicit periodic configurations also disprove S6, the pointwise horizontal-curvature premise of one attempted route to H1. The equilibrium transfer-gap lower bound in H1 remains open. [S6 counterexample](../../../central-quotients/tangent-curvature/periodic-limit/horizontal-curvature/README.md)

## What H3 forces on the transfer spectrum

Fix a real centered scalar supported within one time step on either side of its site, even under time reflection, as in Theorem S. Write $C(n)$ for its time covariance and $N=2\lfloor 1/(2a)\rfloor$ for the normalization lag, so $Z^2=C(N)$. In the reflected Hilbert space take $v=[\tau_1\hat O]$. Reflection changes $\tau_1\hat O$ into $\tau_{-1}\hat O$. Translation invariance therefore gives
$$
 C(n)=\langle v,T^{n-2}v\rangle=\int_{[-1,1]}\lambda^{n-2}\,d\nu_v(\lambda),\qquad n\ge2 .
$$
The shift by two makes this valid for the buffered site scalar. No fractional power of a signed transfer eigenvalue enters.

Assume H1, H2, H3(a), and only the identical-field two-point part of H3(b). Uniformly for even $n$ with $an$ in a compact subinterval of $(0,\infty)$ define the normalized negative spectral weight
$$
 B_n^- = \frac{1}{Z^2}\int_{\lambda<0}|\lambda|^{n-2}\,d\nu_v(\lambda).
$$
At $n=N$ this is a probability fraction. At other lags its denominator is still the unit-clock reading. Then **temporal Lipschitz control for this two-point function on positive compact time intervals is equivalent to $B_n^-=O(a)$ on each such interval**.

For necessity, the even-to-odd difference is the integral of $(1-\lambda)|\lambda|^{n-2}/Z^2$, so it is nonnegative and at least $B_n^-$. H3(c) bounds it by $L a$. For sufficiency set $r=|\lambda|$ and take $j=2\lfloor n/4\rfloor$. H3(b) bounds $C(j)/Z^2$ uniformly because $aj$ stays away from zero. The geometric sum gives $(1-r)r^{n-j}\le1/(n-j+1)$. Thus the integral of $(1-r)r^{n-2}/Z^2$ is $O(a)$. The absolute difference of successive normalized covariances is at most this integral plus $2B_n^-$ for even $n$. For odd $n$ the negative integral is bounded by the one at the preceding even lag. Telescoping yields the claimed Lipschitz bound. These estimates concern time displacements of the one field only. The spatial, mixed-field and higher-point parts of H3(c) require their own control.

For each fixed $0<c<1$, the same two-point growth assumption bounds $C(2\lfloor c/(2a)\rfloor)/C(N)$ by a constant depending on $c$. This is the even-clock ratio for the chosen site scalar. The original R′ uses a specified time-slice vector, a real-time interpolation, and additional transfer assumptions. A ratio for one field cannot be transferred to a different field by changing its normalization.

C4 showed that $o(1)$ negative fraction at the clock suffices for adjacent-lag agreement under its earlier-clock bound. There is a genuine rate distinction here. Take two transfer modes $\pm r$ with $r=1-1/k^2$, negative fraction $1/k$ and $a=-\log r$. The earlier even-clock ratios stay bounded, the odd-even defect tends to zero, and its size is $1-r+2r/k\asymp\sqrt a$ at $N$. It violates the Lipschitz bound. This example tests the abstract self-adjoint argument. Positivity on a Wilson physical sector removes its negative spectrum whenever the observable vector lies in that sector. [C4’s even-clock criterion](../../../central-quotients/tangent-curvature/periodic-limit/z4-spectral-audit/README.md) · [Lüscher’s transfer construction](https://bib-pubdb1.desy.de/record/396349)

## An exact lattice comparison for H4

Fix the planar rotation $Q(x,y)=((3x-4y)/5,(4x+3y)/5)$ in the manuscript’s $(x_1,x_2)$ plane; it fixes the other two coordinates. Its angle divided by $\pi$ is irrational: if the corresponding phase were a root of unity, its sum with its inverse, $6/5$, would be a rational algebraic integer. The domain on which both configurations are exactly on the lattice is
$$
 \Gamma=\{n\in\mathbb Z^4:n_2-2n_1=0\pmod 5\}.
$$
This sublattice has index five. From any lattice point exactly one of staying put or moving by $\pm e_1,\pm e_2$ reaches $\Gamma$, since the five moves exhaust all residues. Each endpoint correction costs at most one lattice step. [Baake, coincidence lattices](https://arxiv.org/abs/math/0605222)

Suppose H1, H2 and H3(c) hold for the normalized fields. For the choice $R_\vartheta=Q$, H4 is equivalent to vanishing of the defect measured only on tuples in $(a\Gamma)^k$, using $S^\beta_\iota(Qz)-S^\beta_\iota(z)$ with **no interpolation at either endpoint**. To prove sufficiency, for each real point $x_i$ round to the nearest lattice site and correct that site to $z_i\in a\Gamma$. Then $|z_i-x_i|\le2a$, $|[x_i]_a-z_i|\le a$ and $|[Qx_i]_a-Qz_i|\le3a$. For separation $\delta$ and sufficiently small $a$ the configurations have separations at least $\delta/2$. On a ball of radius $R$ the full defect is bounded by the exact-grid supremum at radius $R+2a\sqrt k$, separation $\delta/2$, plus $4a\sqrt k L_{k,\delta/2}$. Necessity follows by taking $x=z$. With H0, H3(b,c) and the paper’s subsequence compactness, H4 for any admitted angle implies invariance under all of $O(4)$ in every subsequential limit. In particular the same exact-grid test then holds for $Q$ along the original family, by subsequence contradiction.

More generally the angle need only be outside $(\pi/2)\mathbb Z$ in the density step. In three coordinates the orientation-preserving signed permutations contain the octahedral group of order 24. Adding a coordinate-plane rotation outside that group generates an infinite subgroup: cyclic and dihedral groups preserve a line, the tetrahedral group has order 12, and 24 does not divide the icosahedral order 60. The order-24 option would already equal the octahedral group. The closure is all of $SO(3)$, since any positive-dimensional proper closed subgroup has one-dimensional Lie algebra (the bracket is the cross product) and preserves its axis. Coordinate permutations then supply all the coordinate planes in four dimensions. Plane rotations generate $SO(4)$, and a coordinate reflection gives $O(4)$. Quarter turns themselves already belong to the lattice group and would impose no extra constraint. [Finite rotation group classification, Etingof](https://math.mit.edu/~etingof/groups.pdf)

For a two-point falsification test, displacements $(5j,0)$ and $(3j,4j)$ in the selected plane have identical length on every mesh. A persisting normalized difference at $5ja\to t>0$ would violate H4 under H0 and the stated regularity. Agreement of this pair alone supplies no bounds on the supremum or other mixed moments. The source hypotheses still require a Wilson estimate.

## Verification

Three PCP OS guests checked the even-lag buffers and geometric bound, the signed two-mode example, and the index-five congruence with its unique one-step correction. The host launched each descendant after the previous guest’s request. Each exited zero with 47 register events. [Native computations](worker.c) · [Expected output](checks.txt) · [Three-boot runner](../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Register head |
|---|---|---|
| Parent | 375ed593a3a5ad7476fd95c95d65714f18631953f23994b0369e388a9e371a91 | 15e5ed672a4e302b2c8860c317278076908e7c415587d0862d53bba1af70fa58 |
| Child | 554f7e3418de3764a12eb55a988d7bda55a7a45633c3065133caf612e3fc2648 | a19c69e6f3f8ec1504f184482c3ab6857ae2000cc1663e78a8428822fcc01f09 |
| Grandchild | 5b3a9510eb02e752b3dd994975313946b38c0c318e68a990d3b6dfc510ad0f3d | 074ac8c527cc9dc1ead6e94ede2b82d56124b2c349bd129989b5abec13d46b66 |
