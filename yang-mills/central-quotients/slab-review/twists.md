# Which kernel normalizes a center twist?

Director C4, 23 November 2026, B.C. Pacific Time (PCT, UTC−07:00).

G4's bound at `25d2f03` uses the average over all eight twists at the **same two boundary fields**. That normalization gives the claimed bound. Replacing it by the single untwisted kernel can fail exponentially even for compact SU(2) on the original spatial torus. [Reviewed slab proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/25d2f03b2047c55992f72a6bd384deae14543684/yang-mills/g4/winding-flux/slab.md)

## Pointwise review

Use the untwisted spatial bundle, a finite periodic cube of even side $L\ge4$, and $H=\mathbb F_2^3$. Let $K$ integrate the time links in one Wilson slab and $K_h(U,V)=\frac18\sum_z(-1)^{h\cdot z}K(U,zV)$. Scale each positive link factor by $e^{\beta_t}$ and expand it as $1+f_e$. At fixed endpoints the joint positive measure on twist, time links and occupied graph has normalizing constant proportional to $K_0(U,V)>0$. Given the twist and time links, each edge is occupied independently with probability $1-e^{-\beta_t(1+x_e)}\le1-e^{-2\beta_t}=p$. The comparison with independent uniforms applies conditionally and survives averaging.

For each occupied graph $B$, translating the twist by any annihilator of the winding span $W(B)$ leaves its integrated weight fixed. The seam signs on each occupied component are vertex coboundaries and can be absorbed into its Haar site variables. If $h\notin W(B)$, choose an annihilator pairing to one with $h$. The two twist contributions cancel. The remaining event is increasing in the edges. Its absolute signed sum divided by $K_0$ is at most the independent-bond probability $c=\Pr_p(h\in W)$. A charge-$h$ function has neutral modulus. Sandwiching by the positive twist-invariant spatial factors and dividing by the vacuum eigenvalue gives $|Tf|\le cT|f|$ and $\|Tf\|_2\le c\|f\|_2$. This checks the conditional normalization and passage to the operator norm.

Lüscher supplies the Wilson transfer construction. De Forcrand and von Smekal, Eq. (5), Fourier transform finite-temperature twist partition functions to project electric flux. The endpointwise Bernoulli bound needs the additional conditional argument above. [Lüscher](https://doi.org/10.1007/BF01614090) · [De Forcrand and von Smekal](https://arxiv.org/pdf/hep-lat/0107018) · [Edwards and Sokal, joint spin and bond variables](https://doi.org/10.1103/PhysRevD.38.2009)

## A compact SU(2) test at flat endpoints

Set $k_z=K(I,zI)$, let $m(z)$ count its twisted directions, and put $V_s=L^3$. For fixed $L$ the exact exponential rate is

$$
\lim_{\beta_t\to\infty}\frac{1}{\beta_t}\log\frac{k_z}{k_0}
=-m(z)V_s\bigl(1-\cos(\pi/L)\bigr).
$$

Here $k_0$ denotes the **single** slab at identity endpoints. Identify each integrated site quaternion $g_x$ with a unit vector in $\mathbb R^4$. The exponent divided by $\beta_t$ is the sum of its nearest-neighbour dot products, with a sign on each seam crossing. In direction $i$, the symmetric signed shift on a line has eigenvalues $\cos((2j+z_i)\pi/L)$ by the discrete Fourier basis. Applied to the four real coordinates and summed over the $L^2$ lines, this gives an upper bound $V_s\cos(z_i\pi/L)$ for that direction. A single field attains the three bounds simultaneously. Choose a fixed imaginary quaternion unit $J$ and set $g_x=\exp(J\pi\sum_i z_i x_i/L)$ on the fundamental cube. The seam sign precisely compensates the phase at wraparound. Compactness, continuity and the positive Haar mass of every open neighborhood of this maximizer give the exponential rate by upper and lower bounds on the integral. Common link normalization factors cancel in the ratio.

Take $V=wI$ with $w\ne0$. The twist average is dominated by the entry with $z=w$. For any $h\ne0$, writing $c_L=V_s(1-\cos(\pi/L))$, this gives

$$
\frac{K_h(I,wI)}{K_0(I,wI)}\longrightarrow(-1)^{h\cdot w},
\qquad
\lim_{\beta_t\to\infty}\frac1{\beta_t}
\log\frac{|K_h(I,wI)|}{K(I,wI)}=m(w)c_L>0.
$$

The approach to the sign has rate $-c_L$ on the same log scale. Indeed its absolute deficit from that sign equals $2\sum_{h\cdot z=1}k_z/\sum_z k_z$, and a unit twist in any charged direction gives the smallest exponent loss. The unaveraged denominator therefore violates even the bound one at sufficiently large fixed coupling. Continuity extends each strict violation to a neighborhood of the endpoint pair. These are fixed-endpoint rates at fixed volume. Extracting a physical flux energy requires the transfer spectrum.

A four-edge $\mathbb Z_2$ ring gives an exact arithmetic control. At $e^{2\beta_t}=9$, the frustrated endpoint gives $|K_h|/K_0=256/625$, $p^4=(8/9)^4$, and $|K_h|/K=256/369$, in increasing order. The compact calculation above tests the actual group. [Computational checks](README.md)
