# Quartic magnetic response of the scalar gap at small temporal Wilson coupling

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Let $g$ and $b$ multiply the temporal and spatial Wilson plaquette traces, respectively, in the convention $\exp[(g/2)\operatorname{Tr}U]$. Write $q=I_2(g)/I_1(g)$. At fixed $g>0$ expand the physical scalar gap at $b=0$ as $m=-4\log q+c_2(g)b^2+c_4(g)b^4+c_6(g)b^6+\cdots$. For the stabilized coefficients I obtain
$$
 c_4(g)=-\frac{17}{384}-\frac{5}{16}q^2+O(q^4),
 \qquad c_6(g)=\frac{313}{23040}+O(q^2)\qquad(g\downarrow0).
$$
The closed elementary cube contributes already to the quartic gap coefficient. The first correction in temporal coupling requires both rectangular and nonplanar six-link loops. Substituting equal couplings in the scalar expansion independently recovers the published isotropic series through $q^6$. The full value of $c_4$ at arbitrary $g$ and control of the weak-coupling trajectory remain open. [Coefficient stabilization](../center-parity.md) · [Münster’s effective transfer calculation](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf) · [Langelage, Münster and Philipsen, equation (29)](https://arxiv.org/pdf/0805.1163#page=10)

## The static susceptibility and the six-link sector

Choose a fixed even side at least eight so six-edge loops cannot wind. The published stabilization proof identifies the quartic and sextic answers with those on every even side at least six. Work on gauge-invariant functions fixed by translations and cubic symmetries. There are $V=L^3$ vertices and $N=3V$ faces. Put $A=\frac12\sum_p\phi_p$, $\phi_p=\operatorname{Tr}U_p$, $F=2A/\sqrt N$, and $D=e^{bA/2}$. Denote tilted *spatial* Haar expectation by $\langle\cdot\rangle_b$ with density $e^{bA}/Z(b)$, and put $v=\operatorname{Var}_b F$. The scalar transfer is $DKD$.

On this sector the electric operator $K$ has vacuum eigenvalue 1, the simple eigenvector $F$ at $q^4$, and six-edge fundamental loops at $q^6$. The latter projection is the restriction of the sum of the orthogonal character projections over unoriented simple six-cycles $\gamma$. The rest has norm $O_L(q^8)$ as $g\downarrow0$. To check the order, sum the doubled spins $j$ over occupied links. The sum is even by the vertex singlet parity on one sublattice. No occupied vertex has degree one. Through total label six the four-edge cycle requires a common label, and the only larger fundamental support with all degrees even is a six-cycle. A five-edge leafless cubic-lattice support cannot occur: it would need a four-cycle with a chord or a five-cycle. A six-edge support at total label six uses fundamentals only. Two edge-disjoint cycles require at least eight edges. The Bessel power series gives $I_{j+1}(g)/I_1(g)\le (g/2)^j/(j+1)!$, which bounds the remaining spin-network eigenvalues uniformly in the labels for small $g$. [Physical transfer spectrum](../../../../g4/full-attempt/electric.md)

In this notation the expansion after removing the divergent electric log is
$$
 m+4\log q=-\log v-q^2\,\frac{S}{v^2}+O_L(q^4),\qquad
 S=\sum_\gamma\operatorname{Cov}_b(F,\phi_\gamma)^2
   =\frac4N\sum_\gamma(\partial_b\langle\phi_\gamma\rangle_b)^2.
$$
Here is the reduction and why coefficient extraction is permissible. The leading vacuum direction is $a=D1/\sqrt Z$; write $Q=1-aa^\top$. The transpose denotes the bilinear continuation of the real pairing for complex $b$. The leading vacuum eigenvalue is $Z+O_L(q^4)$. In the complement, divide the transfer by $Zq^4$. Its leading term is the rank-one operator on $QDF/\sqrt Z$, whose nonzero eigenvalue is $v$. Its order-$q^2$ term is $QDP_6DQ/Z$ with $P_6$ the six-loop projection. First-order perturbation against the unit leading direction gives $S/v$. Indeed each overlap with a projected $D\phi_\gamma$ is exactly the corresponding tilted covariance after normalization. The vacuum Schur-complement correction before division is $O_L(q^8)$ because both off-diagonal blocks are $O_L(q^4)$ and the vacuum denominator stays away from zero. Equivalently block-diagonalize the vacuum by its Riesz projection, which differs from $aa^\top$ by $O_L(q^4)$. Vacuum normalization changes the divided ratio by $O_L(q^4)$ as well. Thus the ratio divided by $q^4$ is $v+q^2 S/v+O_L(q^4)$. On a sufficiently small fixed complex $b$ disk, $Z,v$ stay away from zero, $D$ is bounded, and the rescaled rank-one eigenvalue remains separated from zero. The two spectral eliminations and their remainders are uniform there, so Cauchy's formula applies to each fixed $b$ coefficient. This argument uses a single finite spatial box; the coefficient stabilization is a separate result.

## Vacuum-subtracted surface count

Let $z(b)=2I_1(b)/b$ and $u=I_2(b)/I_1(b)$. The one-face expansion after division by $z$ starts with the identity and $2u\phi_p$. Higher characters of doubled spin $j$ have order $b^j$. Through degree eight the normalized three-dimensional pressure per spatial face is
$$
 N^{-1}\log Z(b)=\log z(b)+\tfrac43 u^6+O_L(b^{10}).
$$
The odd-label faces must have zero binary boundary after Haar integration. A nonempty closed set with at most eight faces consists of one cube boundary. On the cover such a set bounds a finite set of cubes. Each occupied column in an axial projection requires at least two exposed faces. Two distinct cubes already have at least five projected columns in total, hence need at least ten faces. The same argument applies here by taking a box larger than the support, which is allowed by stabilization; disconnected supports obey parity componentwise. With no odd faces, at most four distinct nontrivial faces fit in degree eight and a private edge kills the integral. On the six-face sphere, an increase of one face label by two breaks the link match. An extra spin-one face outside the sphere has a private edge. With fundamental faces only, Schur gluing $\int\chi(XU)\chi(U^{-1}Y)dU=\chi(XY)/2$ gives cube weight $4u^6$. There are $N/3$ cubes. The logarithm removes the factorized one-face weights, and the squared sphere weight starts at degree twelve. Odd orders vanish by the spatial center-sign transformation.

Now $v=4(\log Z)''/N$. The resulting expansions are
$$
 v=1-\frac{b^2}{8}+\frac{5b^4}{96}-\frac{7b^6}{360}+O(b^8),\quad
 -\log v=\frac{b^2}{8}-\frac{17b^4}{384}+\frac{313b^6}{23040}+O(b^8).
$$
Strong-coupling surface expansions and connected plaquette diagrams are reviewed by Drouffe and Zuber. [Character expansion and diagram weights, §§3.1.3–3.1.6](https://www.lpthe.jussieu.fr/~zuber/MesPapiers/dz_PR83.pdf)

For $S$ group the unoriented six-cycles by their smallest fundamental disk. Schur gluing gives the unnormalized trace expectation $2u^d$ for an isolated disk of area $d$. The counts and the terms needed **before differentiation** are

| Six-cycle | Number | $\langle\phi_\gamma\rangle_b$ |
|---|---:|---|
| Coplanar $1\times2$ rectangle | $2N$ | $2u^2+O(b^6)$ |
| Two perpendicular faces sharing an edge | $4N$ | $2(u^2+u^4)+O(b^6)$ |
| Six-cycle omitting opposite vertices of a unit cube | $4N/3$ | $4u^3+O(b^5)$ |

A rectangle or bent pair is counted by its common edge, once for each unordered pair of adjacent faces of that type. Through order four an alternative to a two-face filling can only differ by a six-face cube boundary. Only the bent pair has the complementary four-face disk. On the two-face disk increasing one label leaves an unmatched boundary edge; an extra even-label face outside the disk has a private edge. For the last type, the removed opposite vertices each give a three-face filling. A third area-three filling would differ from the first by a distinct cube boundary containing its three perpendicular faces, which determine a unique cube. A six-step simple loop using all three axes lies in a unit cube and omits either adjacent or antipodal vertices. A planar six-cycle is a rectangle. These possibilities exhaust the physical $q^6$ modes at the chosen side.

Inserting the three rows in the squared derivatives yields $S=3b^2/2-b^4/16+O(b^6)$ and $S/v^2=3b^2/2+5b^4/16+O(b^6)$. This gives the stated quartic result. As a separate normalization check, the reviewed quadratic formula gives $c_2=1/8-3q^2/2+158q^4/81+O(q^6)$. With $b=g=4q+8q^3/3+8q^5/3+O(q^7)$, the scalar mass through sixth order is
$$
 -4\log q+2q^2-\frac{98}{3}q^4-\frac{20984}{405}q^6+O(q^8),
$$
in agreement with equation (29) cited above. The agreement tests the combined coefficients along one line of the two-coupling expansion.

## Formula for the outstanding finite-coupling computation

At general fixed $g$ use $T_j=K^{1/2}A^j K^{1/2}/j!$ for the expansion of $K^{1/2}e^{bA}K^{1/2}$. This has the same nonzero spectrum as $DKD$. For either simple scalar-sector eigenvector $f=1,F$ and its electric eigenvalue $r=1,q^4$, let $R=(r-K)^{-1}$ on $f^\perp$ and zero on $f$. Put $h=RT_1f$, $w=T_2f+T_1h$. With real Haar inner products, the quadratic and quartic eigenvalue coefficients are
$$
 r_2=\langle f,T_2f\rangle+\langle h,T_1f\rangle,\quad
 r_4=\langle f,T_4f\rangle+2\langle h,T_3f\rangle+\langle h,T_2h\rangle+
 \langle w,Rw\rangle-r_2\|h\|^2.
$$
For intermediate normalization $\langle f,\psi(b)\rangle=1$, the first two vector coefficients are $h$ and $Rw$. At order three the complement equation gives $R(T_3 f+T_2h+T_1Rw-r_2 h)$; substitution in the fourth-order scalar equation gives the displayed expression. The first derivative vanishes by center parity. Subtract $r_4/r-(r_2/r)^2/2$ of the excited branch from the same expression of the vacuum to get $c_4(g)$. Each reduced resolvent preserves link labels. The middle vector $w$ requires at most three fundamental plaquette insertions counting $F$; evaluating its weighted spin projections on the full cubic box remains the main finite-$g$ calculation.

## Reproduction

Three native PCP OS guests enumerated all 264 rooted oriented simple six-step loops (72 rectangles, 144 bent pairs, 48 skew loops), evaluated disk contractions through the sphere in the quaternion subgroup, and checked the rational logarithm and response coefficients. The subgroup control tests the fundamental Schur factors. SU(2) Haar supplies the analytic derivation. The host symbolic calculation reverts the Bessel variable and checks both published isotropic coefficients. An independent eight-character single-square transfer at $g=2$ gave a quartic coefficient of $-0.0068920800721960$; the resolvent formula and extrapolated finite differences agreed within $4\times10^{-18}$ on that control. [Guest source](worker.c) · [Expected output](checks.txt) · [Symbolic series](series.py) · [Finite-rank resolvent check](resolvent.py)
