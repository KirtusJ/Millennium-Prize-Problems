# Flat holonomy under refinement of the periodic Wilson cube

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The charged quadratic vacuum-energy difference on the flat SU(2) locus has a uniform continuum limit in units of inverse box length. Its central minimum retains slope two in every direction. After the cusp is removed, the quadratic coefficient changes sign between the two-site and three-site cubes and stays negative for all sufficiently fine cubes. Thus the cusp supplies a uniform flat-locus barrier even though the regular part can bend downward. This addresses the flat input to the [fixed-box transfer argument](../../../../observable-normalization/periodic-box-spectrum/full-neutral.md).

## Potential and uniform error

Let $C$ be the three adjoint angles around the full spatial cycles, reduced modulo $2\pi$ in each coordinate, and $d$ the Euclidean distance to $(2\pi\mathbb Z)^3$. This convention identifies the eight choices of central SU(2) holonomies. Put $s(k)=\sum_i\sin^2(k_i/2)$ and $\omega(k)=2\operatorname{arsinh}\sqrt{s(k)}$. On an isotropic periodic cube with $N\ge2$ links per side the dimensionless energy difference is
$$
 B_N(C)=2N\sum_{n\in(\mathbb Z/N)^3}
 \big[\omega((2\pi n+C)/N)-\omega(2\pi n/N)\big].
$$
The two charged colors have identical momentum sums. In each color the two transverse oscillators each contribute a half-frequency. Multiplying the energy per lattice time step by $N$ measures it in box units. The physical energy at side $\ell$ is $B_N/\ell$. This expression includes the charged zero-momentum term. García Pérez, Snippe and van Baal describe the constant Abelian background and distinguish dropping and reinstating the zero mode. [Finite-volume lattice comparison, §3 and Fig. 1](https://arxiv.org/pdf/hep-lat/9608015)

Write $q(w)=\sum_i w_i^4/|w|^4$. With sums over nonzero integer triples define
$$
 B_\infty(C)=\frac{2}{\pi^2}\sum_w\frac{1-\cos(w\cdot C)}{|w|^4},\qquad
 D(C)=\frac{2}{\pi^2}\sum_w\frac{(8q(w)-4)(1-\cos(w\cdot C))}{|w|^6}.
$$
Then
$$
 B_N(C)=B_\infty(C)+N^{-2}D(C)+R_N(C),\qquad
 |R_N(C)|\le K N^{-4}d^2,\qquad \|R_N\|_{C^2}\le K N^{-4}
$$
for one absolute finite $K$. The continuum term equals $\ell V_1$ in van Baal and Koller's Eq. (4.4). The remainder controls the second derivatives of the *difference*, including at the cusp. [Continuum potential and subtraction, Eqs. (4.4)–(4.6)](https://www.ilorentz.org/research/vanbaal/DECEASED/HOME/JOUR/APNY174_299.pdf#page=16)

**Proof.** Normalize Fourier coefficients by $(2\pi)^{-3}$. The only singularity of the frequency on the momentum torus is the origin. Writing $r=|k|$ there gives
$$
 \omega(k)=r-\frac{r^3+\sum_i k_i^4/r}{24}+O_{\rm sym}(r^5).
$$
The remainder after any derivative of order $j$ is bounded by $c_j r^{5-j}$ on a punctured ball. This follows by expanding in $r$ with smooth angular coefficients on the compact sphere. With the same Fourier normalization the transform of $1/r$ away from zero is $1/(2\pi^2|m|^2)$, obtained by radial integration with an exponential regulator. Applying $-\Delta_m$ once and twice gives the transforms of $r$ and $r^3$. Multiplication by $k_i^4$ gives $\partial_{m_i}^4$. In particular
$$
 \sum_i\partial_{m_i}^4|m|^{-2}=(-216+384q(m))|m|^{-6}.
$$
A smooth cutoff equal to one near the origin changes the transforms of the homogeneous models by rapidly decaying terms at high frequency. Indeed sufficiently high derivatives of the cutoff complement times each homogeneous model are integrable. On each dyadic shell of radius $t$ the localized fifth-order remainder contributes at most $c_Jt^8(1+t|m|)^{-J}$ by rescaling and integration by parts. Summing below and above $t=|m|^{-1}$ with $J>8$ gives $O(|m|^{-8})$. The smooth part elsewhere on the momentum torus has rapid decay. Consequently
$$
 \widehat{\omega}(m)=-\frac{1}{\pi^2|m|^4}
 +\frac{4-8q(m)}{\pi^2|m|^6}+O(|m|^{-8}).
$$
Absolute convergence permits summing on the shifted momentum grid, which retains precisely the indices $m=Nw$. The prefactor in the resulting cosine difference is $2N^4$. The bound $1-\cos(w\cdot C)\le |w|^2d^2/2$ gives the claimed pointwise remainder. Two termwise derivatives cost at most $|w|^2$, still summable against $|w|^{-8}$. The same argument with $|w|^{-6}$ gives $D\in C^2$ and $D=O(d^2)$.

## Cusp and curvature

For $N=2$ the zero mode contributes $2d+O(d^3)$ near zero. The other terms are smooth and have zero total gradient by reflection. Comparing with this fixed cube in the expansion above gives $B_\infty=2d+O(d^2)$ and the same estimate for every $B_N$ with a common constant. There is a $c>0$ such that $B_N(C)\ge c d$ on the entire torus for all $N\ge2$. Near the center this follows from the slope. Away from it, the three axial unit windings give strict positivity of $B_\infty$, and uniform convergence gives the lower bound for large $N$. Compactness and A4's strict winding inequality on each of the finitely many remaining cubes finish the proof. [Fixed-cube positivity](../../../../observable-normalization/periodic-box-spectrum/full-neutral.md)

Let $a_N$ be the coefficient of $|C|^2$ after subtracting the cusp. Cubic symmetry makes its Hessian scalar. The zero mode contributes no quadratic term, so
$$
 a_N=N^{-1}\sum_{n\ne0}\partial_1^2\omega(2\pi n/N),\qquad
 \partial_i^2\omega(k)=\frac{\cos k_i}{2\sqrt{u}}
 -\frac{\sin^2 k_i(1+2s)}{8u^{3/2}},\quad u=s(1+s).
$$
At $N=2$ one gets $(1/\sqrt2-1/\sqrt6-1/\sqrt{12})/4$. At $N=3$ group the momenta by the number $j$ of nonzero coordinates. Their counts are 6, 12 and 8, with $s=3j/4$. Average the three axial derivatives in each shell. Exact rational bounds on the radicals give
$$
 0.002545<a_2<0.002546,\qquad -0.121253<a_3<-0.121252 .
$$
The regularized potentials $B_N-2d$ have two continuous derivatives locally at the center (the soft-mode remainder starts at homogeneous degree three). The uniform difference estimate gives $a_N=a_\infty+O(N^{-2})$. In van Baal and Koller's axial expansion the coefficient is $a_\infty=(-1+2\sum_{j\ge1}j^2 b_j)/\pi$ with $b_j<5\pi^2 e^{-2\pi j}/j$. Hence $a_\infty\le[-1+10\pi^2p/(1-p)^2]/\pi<0$, where $p=e^{-2\pi}$. This proves the eventual sign. [Axial expansion and coefficient bound, Eqs. (4.7)–(4.11)](https://www.ilorentz.org/research/vanbaal/DECEASED/HOME/JOUR/APNY174_299.pdf#page=17)

## Check and disposition

Three linked PCP OS guest executions and Lean checked the three-site multiplicities, the radial arithmetic and the combination of the cubic Fourier terms. The verifier rejected one malformed dispatch and three altered declarations. These finite checks cover the indicated arithmetic. The analytic estimates are proved above. The independent momentum-grid and winding-sum implementations gave the respective extrapolated and truncated values $0.800762,0.800774$ on $(1,0,0)$, $1.506506,1.506533$ on $(0.7,-0.4,1.1)$, and $9.707575,9.707793$ on $(\pi,\pi,\pi)$. The script also certifies both finite-cube curvature signs by integer square roots. [Numerical and rational checks](check.py) · [Native guest](worker.c) · [Replay](verify.py) · [Generated Lean declarations](FlatRefinement.lean)

**Remaining gap.** In lattice time units a fixed noncentral flat holonomy costs order $1/N$. To carry this estimate into an interacting spectral bound along refinement, one still needs control of the transfer operator off the flat locus and of its coupling to the soft variables, with errors smaller than the energy scale being tested. The neutral fixed-cube gap has leading scale $\beta^{-1/3}/N$, smaller even than the flat barrier. Its fixed-$N$ asymptotic leaves open how the coupling runs, which states retain local spectral weight at fixed physical separation, and whether a positive gap survives the infinite-volume limit.
