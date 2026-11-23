# Orientation of the local plaquette spectrum near its lower energy edge

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

In the four-dimensional isotropic $SU(2)$ Wilson theory at fixed lattice spacing, take the three unnormalized fundamental spatial plaquette traces anchored at one site. Center each in the infinite-time vacuum. Let $\boldsymbol\mu(I)$ be their $3\times3$ spectral Gram matrix on the lattice-energy interval $I$, $\Delta$ the full mass in the box or bulk under consideration, and $u=(1,1,1)/\sqrt3$.

As $\beta\downarrow0$, choose radii $r\to0$ with $\beta/r\to0$. The energy width $w=\beta^4 r^2$ lies between the controlled sixth-order remainder and the full quartic bandwidth. In bulk, or on even periodic cubes with $Lr\to\infty$, for each fixed $e>0$,
$$
r^{-3}\boldsymbol\mu([\Delta,\Delta+we])
\ \longrightarrow\ \frac{e^{3/2}}{6\pi^2D^{3/2}}uu^*,\qquad D=7/768.
$$
A single oriented trace carries one third of the leading scalar weight. A normalized difference of two orientations has weight $O_e(r^5)$ in the same window. The first conclusion gives a cumulative law with an absolute normalization; the second is an upper bound. The argument derives both from [G4’s local scalar estimates](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/ad1206de753e3a6aea7aeb71d388db506782d9aa/yang-mills/g4/local-scalar-edge) and [A4’s uniform multiplicity and dispersion](../../../observable-normalization/uniform-band/momentum.md).

## Controlling the orientation of the simple branch

Use the $L^{-3/2}$-normalized Fourier modes of all three based traces. Write $H(k)$ for their equal-time Gram matrix, and $W(k)$ for its compression to the top branch: the $(i,j)$ entry is the inner product of the two projected mode vectors. For $|k|\le\kappa$ with fixed small $\kappa$, that spectral projection has rank one. The simple upper center separates by order $\beta^4$ from its two neighbors and A4’s count by continuity preserves its single eigenvalue. Thus $W(k)$ is positive of rank at most one, $W(k)\le H(k)$, and $\mathrm{tr}\,W(k)\le\|H(k)\|$. The rank condition matters because an independent transverse projector could have full weight while preserving the scalar diagonal entry.

Three details sharpen the overlap bound:

1. On open time and an even spatial torus change the sign of link $(x,\mu)$ by the central element $(-1)^{\sum_{\nu<\mu}x_\nu}$. Every plaquette changes sign. Haar measure is invariant, including across a spatial seam since $L$ is even. A connected covariance of two fundamental traces is even in the common complex coupling: the joint insertion is unchanged and the disconnected means each acquire a sign. The bounded holomorphic open-time limit and the removable quotients by $(\beta/4)^{4j}$ retain evenness. At zero coupling $H(k)=I$ by Haar orthogonality. The scalar first scaled lag equals one at zero for every $k$, by the fixed-box electric plaquette projection acting as identity on the normalized Haar mode. The common disk and summable spatial covariance bounds of G4 apply entrywise (each end uses four links). Cauchy's estimate for even germs now gives $H(k)=I+O(\beta^2)$ and scalar first scaled lag $1+O(\beta^2)$ uniformly.
2. For the real scalar autocorrelation the spatial coefficients at $y$ and $-y$ agree. Translation and self-adjointness exchange the ends, and the Wilson transfer and insertion are real. The identity persists in the holomorphic coupling. Replace the Fourier phase difference by $\cos(k\cdot y)-1$ and bound it by $|k|^2|y|^2/2$ on shortest periodic representatives. The same exponential spatial tail is summable with this additional factor. For the filter $F_k=\int x^8(x-b_*)^2\,d\mu_{k,u}$ in G4’s proof ($x$ is transfer divided by $(\beta/4)^4$), the circle bound is therefore $|F_k-F_0|\le C|k|^2$. Both germs vanish through degree seven. Dividing by $\beta^8$ and using the maximum principle as in that proof yields $F_k\le C\beta^8(|k|^2+\beta^4)$ on the real axis. Here $F_0=O(\beta^{12})$ uses the cubic scalar selection at zero momentum. [Filter and common disk](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/ad1206de753e3a6aea7aeb71d388db506782d9aa/yang-mills/g4/local-scalar-edge/momentum.md)
3. The lower two orientation branches cost at least $c\beta^8$ per unit weight in the filter, since $x\ge1/2$ there and their distance from $b_*$ is at least $c'\beta^4$. Total scalar weight on the three upper branches is $1+O(\beta^2)$ by the first lag and the separation from the low transfer cluster. Consequently $u^*W(k)u=1+O(\beta^2+|k|^2)$ and
$$
0\le\mathrm{tr}[(I-uu^*)W(k)]\le C(\beta^2+|k|^2).
$$
The last inequality follows by subtracting the scalar contribution from the trace bound. It controls both transverse orientations together without tracking the phases of eigenvectors.

## Counting the occupied momenta

An energy within $we$ of the full lower edge forces $|k|\le C_e r$ by G4’s global quadratic upper bound on transfer and the $O(\beta^6)$ error in the location of the full mass. Throughout this ball only the simple branch can enter. Its energy satisfies
$$
E_1(k)-\Delta
=D\beta^4 |k|^2+O(\beta^4|k|^4+\beta^6+\beta^6|k|^2).
$$
This uses the logarithm of the transfer, the curvature of the simple eigenvalue, and the same normalization for the full mass. [Curvature calculation](../local-spatial-profile.md) · [Münster, Eqs. (26)–(28)](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf)

In coordinates $p=k/r$, the accepted points are squeezed between balls $D|p|^2\le e\pm C_e(r^2+\beta^2/r^2)$, with the smaller ball included and the larger one containing all accepted points. For $Lr\to\infty$ the mesh is $2\pi/(Lr)$. The local measure averages with divisor $L^3$, so the leading count divided by $r^3$ is $(2\pi)^{-3}$ times the ball volume. Boundary cubes cost relative order $O_e((Lr)^{-1})$ by thickening or shrinking the ball by a cell diameter. Each accepted momentum has scalar weight $1+O_e(r^2+\beta^2)$ and transverse trace $O_e(r^2+\beta^2)$. After summing, coordinate permutations about the base site give an exactly permutation-invariant matrix: permuting axes takes each based trace to the permuted trace, including orientation reversal by reality of the $SU(2)$ character. Hence the matrix is a scalar on each of the line $u$ and its orthogonal complement. There is no mixed term in the local sum. This proves the displayed limit; its matrix error after division by $r^3$ is $O_e(r^2+\beta^2/r^2+(Lr)^{-1})$. The transverse bound uses the count upper bound alone, giving $O_e((r^2+\beta^2)\max(r^3,L^{-3}))$ even in finite boxes.

For bulk, at each fixed coupling first compare finite and infinite mass thresholds to the common reference energy $-\log[(\beta/4)^4 b_*]$ within $C\beta^6$. Squeeze the desired cumulative weights by open and closed half-lines with thresholds enlarged or reduced by a further $C\beta^6$; weak convergence can be applied to each positive local quadratic form in the transfer variable. For an upper bound use the finite-volume upper estimates on the larger open window; for a lower bound use the estimates on a smaller closed window. The extra width divided by $w$ vanishes as $\beta/r\to0$. In the transverse upper bound it only changes the enclosing ball constant. This passage does not assume convergence of spectral projections at a fixed atom.

## Finite boxes and scope

If $Lr\to\ell\in(0,\infty)$, multiply the matrix by $L^3$. At any $e>0$ different from every $4\pi^2D|n|^2/\ell^2$, the limit is
$$
uu^*\#\{n\in\mathbb Z^3:4\pi^2D|n|^2/\ell^2<e\}.
$$
Only finitely many integer indices can enter the window, and each is eventually included or excluded with a strict margin. At a shell threshold the strict and non-strict counts bound the lower and upper scalar limits. If $Lr\to0$, only zero momentum enters for each fixed $e>0$, and $L^3\boldsymbol\mu\to uu^*$. The exact zero-momentum top branch has cubic scalar symmetry. All claims concern connected vacuum measures and joint strong-coupling limits at fixed mesh. Existence of a density at fixed $\beta$, or a positive gap for an interacting continuum theory, requires other information.

## Controls

Run `python3 check.py` with NumPy. The program diagonalizes the full quartic matrix in the candidate region, includes face-center phases in the three site-anchored tests, and checks the permutation decomposition. At $e=D$, $(L,r)=(1024,1/8)$, its single-face to scalar ratio was $0.33350730$; the normalized difference-to-scalar ratio divided by $r^2$ was $0.01670099$. These are effective-symbol checks. The proof supplies no nonzero lower coefficient for a difference. Three measured PCP OS guests checked the link signs on even boxes, the scalar and transverse permutation algebra on 343 integer dyads, and the first seven shell multiplicities $1,6,12,8,6,24,24$. The combined post-exit check-text SHA-256 was `702e3d67ba44ac14c6be84c7ebc5abc1aaa1884e9a06df38a4c81616c2ae01c6`.
