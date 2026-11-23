# Recovering shell links from rooted plaquette matrices

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Disposition for L4.** On the cubical shell of side $L=2N$, there is an explicit spanning tree for which every gauge-fixed link is a word of at most $16(L+1)^2$ rooted plaquette matrices and their inverses. The exponent two is sharp for this tree in the maximum class-angle norm. This proves exact reconstruction in one common root frame for arbitrary field strength. Revision one's limiting conditional-law argument in L4 already uses the weaker, linear inversion at fixed $N$. The construction below also justifies the exact group statement after Step 7 when the shell tree is chosen as specified here. [Z4, shell lemma and L4](../../../../z4/attempt/paper/sec_proof.tex)

Maximal-tree gauge and its residual common colour rotation are standard in lattice Yang–Mills theory. Ligterink, Walet and Bishop give a Hamiltonian construction of independent variables in that gauge. Here the inputs are the redundant elementary shell plaquette matrices with specified connectors. The explicit inverse and its bounds follow from the square equations below. [Ligterink, Walet and Bishop, Annals of Physics 284 (2000), 215–262](https://arxiv.org/abs/hep-lat/0001028)

## Data and tree

Use integer coordinates $(t,x_1,x_2,x_3)$ in $[0,L]^4$, $L\ge2$. Take the links and squares in its boundary faces. Orient links in increasing coordinate directions. Root the tree at the origin. For each positively oriented square, transport its holonomy to the root along the tree path to its lower corner. Its full matrix $H_{ij}(x)$ in the root frame enters as data. Independent plaquette traces discard the relative colour directions. A change of colour basis at the root simultaneously conjugates all inputs and all outputs.

1. On the bottom cap $t=0$, take all direction-3 links, direction-2 links with $x_3=0$, and direction-1 links with $x_2=x_3=0$.
2. From each vertex of the spatial boundary on the bottom cap, run its vertical column to the top cap.
3. On the top cap, for each strictly interior pair $(x_2,x_3)$ take the direction-1 path from $x_1=0$ through $x_1=L-1$. Omit its final link to $x_1=L$.

The bottom tree spans its cap. Each subsequent path adds fresh vertices to one vertex already reached. These paths include every shell vertex. In this gauge all tree links are the identity, so each input $H$ equals the untransported matrix at its lower corner in the fixed gauge.

## Ordered reconstruction

For distinct axes write $H_{ji}=H_{ij}^{-1}$ at the same lower corner. The square equation $H_{ij}(x)=U_i(x)U_j(x+e_i)U_i(x+e_j)^{-1}U_j(x)^{-1}$ gives the propagation rule

$$
U_j(x+e_i)=U_i(x)^{-1}H_{ij}(x)U_j(x)U_i(x+e_j).
$$

Use the following order. Length means the number of signed input matrices in an expanded word, with identity of length zero.

1. **Bottom cap.** For a direction-$j$ link outside the tree choose the largest $k>j$ with $x_k>0$. Apply the rule from $x-e_k$ with $i=k$. Both direction-$k$ links are tree links. Decreasing the selected coordinate to zero and repeating consumes at most $2L$ squares before reaching a tree link.
2. **Sides.** Propagate each spatial edge lying in a spatial boundary face from $t=0$ upwards. Both time links are in the tree. All side links are therefore known, with length at most $3L$.
3. **Top transverse links.** For each direction $j=2,3$, start with the known edge on the $x_1=0$ plane. Propagate in direction 1 as far as $x_1=L-1$. Each required longitudinal link is either a short top tree link or a known side link. The $x_1=L$ plane is already known. Hence all transverse edges are known, each with length at most $3L+(L-1)(1+6L)$. If both endpoint columns have interior transverse coordinates, both longitudinal links are identities at every step, giving the smaller bound $4L$.
4. **Top seam.** Only direction-1 links at $x_1=L-1$ with interior $(x_2,x_3)$ remain. Fix interior $x_3$. Start at $x_2=0$ with a known side link and propagate the seam in direction 2. At $x=(L,L-1,j,x_3)$ this is
   $$
   U_1(x+e_2)=U_2(x)^{-1}H_{12}(x)^{-1}U_1(x)U_2(x+e_1).
   $$
   The far-plane edge costs at most $3L$. The near-plane edge costs at most $4L$ whenever $1\le j\le L-2$. At the single entrance step $j=0$ one column is on a side, allowing at most another $3L(L-1)$ factors for that step. No exit step is needed. The seam word has length at most $3L+(L-1)(1+7L)+3L(L-1)$.

All bounds are at most $K=16(L+1)^2$. Every substitution uses already known links, so on data arising from any group connection this procedure is a left inverse of the rooted face map. No choice of unknown conjugators enters. Simple connectivity and normal generation by the face words give the flatness and angle statements of Z4's shell lemma, but alone do not specify those conjugators for an exact inverse on nonflat data.

For a bi-invariant metric, multiplication and inversion give $d(U_e(H),U_e(H'))\le K\max_q d(H_q,H'_q)$ by telescoping. With the SU(2) class angle $\alpha$ and a uniform one-face estimate $\mathbb E[\beta\alpha(H_q)^2]\le B$, Minkowski's inequality applied to each *fixed word* yields $\mathbb E[\beta\alpha(U_e)^2]\le BK^2$. Counting at most $24L(L+1)^2$ shell edges gives $(\mathbb E\|\psi\|_2^2)^{1/2}\le\sqrt{24BL}(L+1)K$ for the scaled principal logarithms. Any choice of logarithm of norm $\pi$ at the cut point gives the same norm estimate.

## Sharp exponent for this tree

In a common Cartan subgroup set $U_1(t,x)=\exp(i t\theta\sigma_3)$ on all direction-1 links and use identity elsewhere. The $(0,1)$ faces have class angle $\theta$ and all others vanish. Along the path to the initial vertex of an interior seam link the top tree transport is $\exp(i(L-1)L\theta\sigma_3)$. The endpoint on $x_1=L$ is reached up a side column with identity transport. The tree-gauge seam link is therefore $\exp(i L^2\theta\sigma_3)$. For $0<\theta<\pi/L^2$, its class angle is exactly $L^2$ times the largest face angle. The lower bound applies to the chosen tree and the stated norm.

## Consequence for the conditional law

Tree paths on the shell are exterior-measurable. At fixed $L$, the moment bound makes $\psi$ tight; moreover differentiating the word map at the identity gives a linear left inverse of the shell curl on tree-gauge fields. On bounded sets of scaled shell data, the quadratic Taylor remainder in the scaled logarithm is $O_L(\beta^{-1/2})$. This recovers the shell step in L4 with its common colour frame. The passage to the conditional law still uses the interior L3 kernel estimate and finite-dimensional weak convergence with exterior test functions. The polynomial shell estimate by itself gives neither a growing-volume L3 estimate nor a continuum mass gap. [Independent numerical and native controls](checks.md)
