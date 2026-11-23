# The elementary cube in the quartic magnetic gap

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For fixed temporal SU(2) Wilson coupling $g>0$, put $q=I_2(g)/I_1(g)$ and $x=q^2$. The part of the scalar quartic log-gap coefficient coming from **six distinct spatial faces** is exactly
$$
c_{4,\mathrm{cube}}(g)=-
\frac{5+44x+143x^2+200x^3+143x^4+44x^5+5x^6}
     {128(1-x^2)^3}.
$$
This contribution is negative throughout the electric family. At $q=1/2$ it is $-117413/432000$; as $q\uparrow1$, $(1-q)^3c_{4,\mathrm{cube}}\to-73/1024$. With $g=\kappa/a_t$ and $b=a_t\ell$, its contribution to the coefficient of $\ell^4$ in the gap divided by $a_t$ therefore tends to $-73\kappa^3/3456$, using $1-q\sim3/(2g)$. The remaining fourth-order terms involve repeated faces and the logarithmic subtraction. Their sign and size at general $g$ remain open. [Full coefficient at small temporal coupling](../README.md) · [Effective transfer treatment of the low-lying glueballs, Münster](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf)

## Extracting the cube

Use the connected two-time function of $F=\sum_p\operatorname{Tr}U_p/\sqrt N$, with $N=3L^3$, at lags $0,M$. The order-four spatial perturbation inserts four traces, each weighted by $1/2$. At zero magnetic coupling its two-time function is $q^{4M}$. In the coefficient of the logarithm, isolate the six-distinct-face contribution of the order-four connected cumulant divided by $q^{4M}$. The other term is a product of order-two coefficients; it is kept with the repeated-face remainder. Equivalently, attach a sign $\epsilon_p=\pm1$ to each spatial trace in both the test and the perturbation, and select the product of the six cube signs in the finite-lag Taylor coefficient. All order-two terms are independent of these signs, since a set of at most four distinct squares cannot close. This gives an unambiguous separation before taking the time-slope limit. No spectral assertion for a sign-modified transfer is needed.

Electric link chains can be center-flipped independently. A nonzero contribution from six distinct faces thus requires a closed binary surface. Work first in a sufficiently large periodic box so the rooted support lifts. In the cubic cover a finite closed binary surface bounds a finite set of elementary cubes (the cubical complex is contractible). Each occupied column in any axial projection requires at least two exposed faces. Two or more cubes give at least five projected columns in total, hence at least ten exposed faces. Six distinct faces must therefore bound a single cube. Every nonempty proper subset has an unmatched edge, so all proper submoments vanish and the six-point cumulant equals its moment. The preceding [lifting and time-limit proof](../../coefficient-stability.md) applies to the full coefficient, and the particular cube term lifts at side six as well.

Label the six faces by opposite pairs $(0,1),(2,3),(4,5)$. Their adjacency graph is the octahedron. Assign each face an integer time $t_i$. At each spatial edge exactly two fundamental matrix entries occur, one from either incident face. Conditional expectation on the earlier link gives a multiplier $q^{|t_i-t_j|}$ on the later entry. Independence of complete link chains reduces the remaining integral to six simultaneous Haar traces. Consistently orient the sphere; reversing a face leaves its SU(2) character unchanged. Successively merging neighboring faces by Schur orthogonality, or fixing a tree and using five independent Haar face variables and their inverse ordered product, gives $2^{-4}$. The moment is consequently $2^{-4}q^{\sum_{i\sim j}|t_i-t_j|}$ for unordered adjacent pairs.

## Time summation

Pin face 0 at zero and a second face at $M$. Sum over the four other time labels on the entire integer line after taking the boundary limit at fixed $M$. The sums converge for $0<q<1$. Sort the occupied time levels, allowing ties. Across a gap of length $d$ between successive levels, the exponent receives $d\,|\partial S|$ where $S$ is the set of earlier faces. Normalizing by $q^{4M}$ subtracts four from the cut size on gaps between the two marks. Cuts of size four occur only at a singleton or its complement. All other proper cuts have size six or eight.

Only orderings with the two marks alone at the two ends contribute a term linear in $M$. Indeed the coefficient of $M$ requires two gaps with zero residual exponent inside $[0,M]$. With at most one such gap its length is determined by $M$ and the other gap lengths, whose positive-exponent sums are bounded geometric series. Outside the marks the full cut exponent is positive. This also bounds every ordering having a tie with either mark. When both end gaps have zero residual exponent, the interior widths have summable geometric weights. At fixed interior widths the number of positive end-gap pairs whose lengths complete $M$ is $M+O(1+\text{sum of interior widths})$ up to truncation at zero. Dividing by $M$ and using the summable bound gives a factor one. This directly evaluates the time slope without a finite-window extrapolation.

For each of the 75 ordered partitions of the four labeled insertions into nonempty levels, start from face 0 and add whole levels in order. For every intermediate prefix (after at least one level and before the last), multiply by $q^{|\partial S|-4}/(1-q^{|\partial S|-4})$. Summing these products gives the weights for an opposite or an adjacent sink:
$$
W_o=\frac{(1+x)(1+8x+x^2)}{(1-x)^3},\qquad
W_a=\frac{1+8x+26x^2+36x^3+26x^4+8x^5+x^6}{(1-x^2)^3}.
$$
Each fixed source belongs to two cubes. Together they offer two opposite and eight adjacent sinks. The $4!$ assignments of distinct inserted faces cancel the Taylor factorial. The four factors $1/2$ and the Haar moment supply $1/256$. Finally the gap is the negative slope of the log correlation. Hence $c_{4,\mathrm{cube}}=-(2W_o+8W_a)/256$. Its expansion begins $-5/128-11q^2/32$. Subtracting it from the earlier full coefficient gives the independent target $-1/192+q^2/32+O(q^4)$ for the repeated-face and logarithmic terms.

## A second channel checks the scalar calculation

At zero spatial momentum give the three plaquette orientations real weights $w_i$, with $\sum_iw_i^2=3$. The scalar choice is $(1,1,1)$. The two-dimensional cubic representation $E^{++}$ is the plane $\sum_iw_i=0$. The electric plaquette cluster contains one copy of this representation at zero momentum. Cubic symmetry makes the effective eigenvalue scalar on that copy, so the earlier susceptibility reduction applies to either unit polarization. Equivalently one can select the subspace odd under exchange of two axes, at zero momentum and even under all axis sign flips: inside the plaquette cluster this isolates the difference of those two orientations. The corresponding vacuum-normalized energy is the plaquette branch of this symmetry type.

Introduce three spatial sources $b_i$ and the derivative $\partial_w=\sum_iw_i\partial_{b_i}$, setting all $b_i=b$ after differentiating. Through the required orders, the pressure per face is $\sum_i\log z(b_i)/3+(4/3)\prod_i u_i^2$, where $u_i=I_2(b_i)/I_1(b_i)$. The susceptibility is four times its second directional derivative. In the six-loop correction use the first directional derivatives of $2u_i^2$ for a rectangle, $2u_i u_j(1+u_h^2)$ for a bent pair ($h$ the remaining orientation), and $4u_1u_2u_3$ for a skew loop. These are the two-source versions of the disks counted in the scalar calculation; the omitted terms cannot enter at the displayed orders. In the $E$ plane the skew derivative vanishes at equal sources. The normalized susceptibility and correction give
$$
 c_4^{E}=\frac1{384}+\frac{3}{32}q^2+O(q^4),
 \qquad c_6^{E}=-\frac1{11520}+O(q^2).
$$
For this polarization the cube part at arbitrary $q$ is $-(2W_o-4W_a)/256$: each of the two other orientations has four adjacent sinks, and their weights sum to the negative of the source weight. At $q=0$ the repeated-face remainder is again $-1/192$. Using the previously calculated quadratic adjacency eigenvalue zero in the $E$ plane and setting $b=g$ recovers the published isotropic $E^{++}$ coefficients $-26/3$ and $13036/405$ at fourth and sixth order in $q$. The scalar calculation gives $-98/3$ and $-20984/405$ in the same convention. [Langelage, Münster and Philipsen, equation (29)](https://arxiv.org/pdf/0805.1163#page=10)

## Independent checks

A finite-window calculation visits faces by advancing a 64-state subset distribution, including insertions exterior to both marks. At lags 160 and 161, with 160 additional time layers on either side, the normalized first differences reproduced the analytic slopes at $q=1/4,1/2,3/4,7/8$ to relative error below $2\times10^{-10}$. Three native PCP OS guests checked the cut spectrum, summed the rational weights at $q=1/2$ by subset recursion, and recovered the scaled $q\uparrow1$ limit using the strictly ordered layers. All three passed on replay. The first run stopped on a kernel keyboard self-test before admitting the second guest. [Ordered partitions](sheets.py) · [Finite-window calculation](height_check.py) · [Polarization check](polarization.py) · [Guest source](worker.c) · [Expected output](checks.txt)
