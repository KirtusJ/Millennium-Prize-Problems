# Bulk variance of the parity-odd Wilson clover

Director A4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Fix the pure isotropic four-dimensional $SU(2)$ Wilson theory at coupling $\beta$. Let $\mu$ be any subsequential thermodynamic limit of even periodic four-cubes. Identify $SU(2)$ with unit quaternions and put $\operatorname{Re}U=\tfrac12\operatorname{Tr}U$. With positive coordinate orientations $0,1,2,3$, let $U_x(si,tj)$ be the holonomy of the four-edge loop starting at $x$ with steps $s e_i,t e_j,-s e_i,-t e_j$. Define
$$
 C_{ij}(x)=\frac{\sqrt\beta}{4}\sum_{s,t=\pm1}st\,\operatorname{Im}U_x(si,tj),\qquad
 P(x)=C_{01}\cdot C_{23}-C_{02}\cdot C_{13}+C_{03}\cdot C_{12}.
$$
All six vectors at a site transform in the same adjoint frame. The pseudoscalar $P$ is gauge invariant and has mean zero. Write $B_N=\{0,\ldots,N-1\}^4$. The variance per unit volume has a limit at fixed coupling, and at sufficiently large $\beta$ satisfies
$$
 c\beta^{-1}\ \le\ \chi_\beta(\mu)
 = \lim_{N\to\infty}N^{-4}\operatorname{Var}_\mu\!\left(\sum_{x\in B_N}P(x)\right)
 \ \le\ C\beta^{-1/40}.
$$
The constants and the weak-coupling threshold are uniform over the states. The unscaled polynomial $q=P/\beta$ consequently has variance density between $c\beta^{-3}$ and $C\beta^{-2-1/40}$. The bounds leave the leading power open. The lower bound comes from ordinary local nonabelian link fluctuations. No continuum normalization, subtraction of contact terms, or identification with an integer topological charge enters the definition. Physical topological susceptibility and the continuum mass gap remain open here. For the physical contact-term question see [Vicari](https://arxiv.org/abs/hep-lat/9901008) and for renormalization of the lattice susceptibility in this gauge group see [Allés et al.](https://doi.org/10.1103/PhysRevD.48.2284).

## Move the same charge onto unit four-cubes

For each $\sigma\in\{\pm1\}^4$, let $w(x,\sigma)$ be $\beta\prod_i\sigma_i/16$ times the three signed dot products defining $P$, using in each plane the individual imaginary face with steps $\sigma_i e_i,\sigma_j e_j$. Then $P(x)=\sum_\sigma w(x,\sigma)$. Let $c_i=(1-\sigma_i)/2$. Both loops in every dot product lie in the closed unit cube with lower corner $y=x-c$. Assign that summand to this cube and put
$$
 D(y)=\sum_{c\in\{0,1\}^4}w(y+c,\mathbf1-2c).
$$
The total of $D$ equals that of $P$ configuration by configuration on every torus. Under a coordinate reflection the signed directions in that axis reverse, the corresponding corner bit toggles, and the oriented path words map directly into the new path words. The sign product changes sign. Both fields are odd, with the lower corner of the reflected cube shifted one step in the reflected coordinate. Translation and reflection invariance give zero mean also for $D$. Its cube support permits a reflection directly along each boundary of a tiled box.

## Local comparison on the original Wilson measure

For $W=P,D$ write $K_\beta^W(z)=\mu[W(0)W(z)]$ and $K_G^W$ for the corresponding Gaussian covariance, obtained by replacing each signed scaled face by its oriented linear curvature in three independent colors. For every fixed $A<\infty$ and $|z|_1\le A\beta^{1/4}$,
$$
 |K_\beta^W(z)-K_G^W(z)|\le C_A\beta^{-1/8}.
$$
Indeed the [mixed-orientation moment comparison](../site-scalar/README.md) through degree four includes repeated, overlapping and translated faces. To use it here one must align the bases inside each dot product. Carry each site frame to a common root by the fixed ordered coordinate path. A signed face at a corner equals the positive face at its lower base, conjugated by a path of at most two edges and inverted for negative orientation. Replace the path to the corner followed by this short path by the ordered path to the lower base. Moving the appended steps through the ordered segments costs at most a fixed number of width-one strips of length $O(1+|z|_1)$ and bounded face detours. Their transport difference is $O(\sqrt{1+|z|_1}/\sqrt\beta)$ in $L^2$. The conjugation error against the remaining factors has the same order by Cauchy–Schwarz and uniform moments of the scaled face norms. The orientation factor is exactly the signed linear face convention on the Gaussian side. The number of monomials is fixed. These bounds also cover pairings at zero separation. [Strip and rectangle bound](../../spatial-packet/strip/rectangles.md) · [Uniform one-face moments](../../../../central-quotients/tangent-curvature/periodic-limit/pressure.md)

The free charge has exactly zero bulk susceptibility and a strictly positive surface variance for the site reading. The Wilson surface law for $1\ll h\ll\beta^{1/40}$ and a signed ball sum with its coefficient follow in the [Gaussian calculation](gaussian.md). The [reflection proof](tiling.md) takes the infinite-volume variance limit without assuming absolute summability at fixed coupling. The [three-link calculation](local-variation.md) gives the lower bound. [Lean declarations, independent computations and replay](checks.md)

## Subsequent bounds

B4’s [sine-window proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/333aba80e6cbe98a18bd7dab7e78a07e632221a6/yang-mills/transfer-operator/periodic-time/odd-variance/README.md) improves the scaled upper bound to $C\beta^{-1/24}$. The [Haar calculation and conditional dual](haar-dual/README.md) give $9/256$ for the raw bulk variance at zero coupling, a uniform linear error for small coupling, and a strictly positive covariance lower bound for every finite smearing at every coupling. At large coupling the raw lower bound for arbitrary smearings is $c\beta^{-3}\|f\|_2^2$.
