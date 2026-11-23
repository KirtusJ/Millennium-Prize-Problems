# A two-sided estimate for the Wilson midpoint ratio

Let $\mu$ be an infinite-volume thermodynamic limit of isotropic even periodic four-cubes in pure $SU(2)$ Wilson theory. Use its own transfer operator $T_\mu$ and assume $m=-\log\|T_\mu|_{\Omega^\perp}\|>0$. This same $m$ defines $N=2\lfloor1/(2m)\rfloor=2+2J$, $h=\lfloor(J-1)/2\rfloor$ and $H=2+2h$. Put $C(2+2j)=M_j$ for the covariance in $\mu$ of the 24-plaquette half-trace sum multiplied by $\beta$. Uniformly over these states at sufficiently large coupling,

$$
 m(N-H)\ \le\ \log\!\frac{C(H)}{C(N)}
             \ \le\ K(N-H)\beta^{-1/64}.
$$

The lower endpoint tends to $1/2$ since $N=1/m+O(1)$ and $H=N/2+O(1)$. In particular the midpoint ratio has limit inferior at least $\sqrt e$. For the lower bound, the one-slice buffered vector is orthogonal to the vacuum. Its $T^2$ measure is supported in $[0,e^{-2m}]$, so $M_J\le e^{-2m(J-h)}M_h$. [Transfer representation and strict positivity](README.md) · [Lüscher’s Wilson transfer matrix](https://doi.org/10.1007/BF01614090)

For the upper bound choose an even $r\asymp c\beta^{1/64}$, with $c>0$ fixed sufficiently small. A4’s absolute error $O(\beta^{-1/8})$ and free covariance asymptotic put $C(r)$ and $C(2r)$ between positive multiples of $r^{-8}$. Thus $\log C(r)-\log C(2r)\le K_0$ uniformly. The seventh-root gap bound ensures $2r\le H<N$ eventually. By Cauchy–Schwarz for the positive measure, the slopes of $\log C$ on the even-time grid increase. Comparing the secants on $[r,2r]$ and $[H,N]$ yields $\log C(H)-\log C(N)\le K_0(N-H)/r$. The suppressed factor of 16 between the two conventions cancels in every ratio. [A4’s clover estimate](../../observable-normalization/transfer-increments/local-action/site-scalar/README.md) · [Lattice gap upper bound](../../observable-normalization/transfer-increments/spatial-packet/strip/README.md)

The orders at opposite ends of this envelope can both occur for positive transfer measures compatible with the stated time-moment accuracy. The first measure in the [same-gap construction](precision-limit.md) attains the lower limit $\sqrt e$. For the second, $\log(M_h^-/M_J^-)\ge \beta^{-1/64}(J-h)-\log(1+e^{-J\beta^{-1/64}})$. Its logarithmic ratio is therefore at least a positive constant times $(N-H)\beta^{-1/64}$. Uniform $O(\beta^{-1/8})$ error relative to the free clover also gives the required bounds at $r,2r$ for these measures by taking $c$ small. An improved state-uniform order for the upper endpoint in the Wilson theory would have to use additional information about its dynamics. The bound above allows the midpoint ratio to diverge and leaves (C) open.
