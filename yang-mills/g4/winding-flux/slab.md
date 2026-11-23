# A single-slab bound by occupied winding cycles

Take product probability Haar measure on the spatial links of $(\mathbb Z/L)^3$ and gauge-invariant slice functions. For each coordinate direction $i$ choose one dual transverse plane. Multiplying by $-I$ on its forward crossing links preserves the spatial Wilson action. Moving this plane across a layer changes the transformation by site gauge signs on the intervening vertices. On physical functions these transformations define $H=\mathbb F_2^3$. Write $\chi_h(z)=(-1)^{h\cdot z}$. The spatial flow is equivariant because the twists are isometries preserving the spatial action. A contractible loop has even intersection parity with every plane and is invariant under these twists, at every flow time.

For boundaries $U,V$, let $g_x$ be the integrated temporal links. Up to a positive scalar, the projected kinetic kernel is
$$
K(U,V)=\int\prod_{e=(x,y)} \exp\{\beta_t x_e(U,V,g)\}\,\prod_x dg_x,\qquad
x_e=\tfrac12\operatorname{Tr}(U_e^{-1}g_x V_e g_y^{-1}).
$$
Multiplying a boundary link by its central sign multiplies $x_e$ by that sign. Sending $g_x$ to a site sign times $g_x$ similarly gives the coboundary sign on each edge. With $M(U)=e^{-\beta_s S_{\rm sp}(U)/2}$ and vacuum eigenvalue $a_0$ of $MKM$, the transfer is $T=MKM/a_0$. It is positive self-adjoint on the physical Hilbert space. The kernel is strictly positive in every finite box, and the normalized positive vacuum is unique and center invariant. $M$ commutes with every flat twist. [Lüscher's transfer construction](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf) · [Program's finite-volume normalization](../transfer-inverse-moment/inverse-form.md)

Let $K_h(U,V)=|H|^{-1}\sum_z\chi_h(z)K(U,zV)$ and denote the neutral projection by $K_0$. For a subgraph $B$ of the spatial bonds let $W(B)\subset\mathbb F_2^3$ be the winding image of its binary cycle space. Our pointwise bound is
$$
|K_h(U,V)|\le K_0(U,V)\,\mathbb P_p\{h\in W(B)\},
\qquad p=1-e^{-2\beta_t},
$$
where the last probability uses independent bonds of the spatial torus.

1. For each twist expand $e^{\beta_t x}=e^{-\beta_t}(1+f)$ with $f=e^{\beta_t(1+x)}-1\ge0$. Sum products $\prod_{e\in B}f_e$ over all bond subsets and integrate the site variables. Normalize the joint positive weight on $(z,g,B)$ using **the neutral kernel at these same endpoints**. Given $z,g$, the bonds are independent with conditional probabilities $f_e/(1+f_e)=1-e^{-\beta_t(1+x_e)}\le p$. Coupling to independent uniforms gives domination by Bernoulli $p$ for every increasing graph event. Occupations after averaging over $z,g$ can be correlated. This expansion uses the joint spin/bond idea also studied by Edwards and Sokal. [Edwards and Sokal](https://doi.org/10.1103/PhysRevD.38.2009)
2. For fixed $B$, integrate out $g$ in its contribution. If $w$ annihilates $W(B)$, its flat seam sign has product one around every occupied cycle. On each component, start at a root and accumulate the sign along any occupied path to each vertex. The cycle property makes the value independent of the choice of path, including on isolated vertices. These vertex signs absorb $w$ on every occupied edge by a Haar change of $g$. Hence the integrated weight is unchanged by $z\mapsto z+w$. If $h\notin W(B)$, finite-dimensional binary linear algebra gives such a $w$ with $h\cdot w=1$. Translation by $w$ reverses the Fourier sign and cancels the whole subgraph contribution. [Lean path-potential and cancellation lemmas](WindingFlux.lean)
3. On the surviving increasing event $h\in W(B)$, the absolute Fourier contribution is bounded by the sum of the positive weights. Dividing by $K_0$ now gives the event probability in the above mixture, bounded by its independent-bond probability. Sandwich by $M$ and normalize by $a_0$. For charge-$h$ functions, $|Tf|\le c\,T|f|$ pointwise with $c=\mathbb P_p(h\in W(B))$, because $|f|$ is neutral and the neutral projected kernel acts on it. Taking $L^2$ norms uses the vacuum-normalized contraction $T$. This proves $\|T|_h\|\le c$ for the entire physical sector.

The empty graph has independent probability $(1-p)^{3L^3}>0$ and cannot carry a nonzero $h$. Thus the bound is strictly below one in each finite box at any finite temporal coupling. To control large boxes one needs the winding estimates. [Finite-volume and asymptotic bounds](bounds.md) · [Compact Haar and signed finite-group controls](control.py)
