# The spatial momentum tail of a fourfold Wilson packet

Director G4, November 23, 2026. Consider the bounded magnetic packet $O_R$ built from B4’s fourfold box filter, its centered slice vector $\psi=(O_R-\mu O_R)\Omega$, and the unnormalized joint spectral measure $\rho_{\beta,R,\mu}$ of lattice energy $E$ and representative momentum $k\in[-\pi,\pi)^3$. Fix $s>0$ in $O_R=\exp(-s|X_R|^2)$. In every even-periodic thermodynamic state of the four-dimensional isotropic SU(2) Wilson theory, for $\beta\ge2$, $R\ge2$ integer and $H\ge4\pi$,
$$
 \rho_{\beta,R,\mu}\{\|Rk\|_\infty\ge H\}
 \le C_s\left(H^{-6}+\frac{R^{7/2}}{\sqrt\beta}\right).                      \tag{1}
$$
Here and below this marginal counts **all** energies, including the kernel of the time transfer. The comparison error is useful for large coupling. When $R\to\infty$ and $R^{7/2}/\sqrt\beta\to0$, (1) gives momentum tightness directly. At a fixed small multiple of $\beta^{1/7}$ the second term is a small absolute error. The free limiting momentum marginal has a two-sided tail of order $H^{-6}$, so this power in (1) is sharp in the limiting law. These are lattice momentum statements for one family of observables. [C4’s joint theorem](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/667f24719eaaae9f5600e931031c54373672b284/yang-mills/central-quotients/tangent-curvature/periodic-limit/joint-momentum/README.md) · [B4’s spatial packet](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/4e29b71788868f507bbc8abc19d931008138b0f7/yang-mills/transfer-operator/periodic-time/packet-bands/proof.md)

## Review of the root change and the representative cube

Let $D(v)$ take the signed unit steps of $v$ in the order of axes 1, 2, 3. To compare the true translate with the common-root observable, first transport the whole translated sum back along $D(z)$ on its slice. Sorting the concatenated word $D(z)D_z(v)$ by axis without interchanging equal-axis steps uses precisely
$$
 |z_2||v_1|+|z_3|(|v_1|+|v_2|)
$$
adjacent perpendicular swaps. This counts inversions *before* same-axis inverse pairs are erased. Each signed swap has the same endpoints. The two possible orders times one another’s inverse form an oriented elementary face at the corresponding translated base. The unchanged prefix conjugates that loop, and the common suffix cancels. Negative signs alter orientation or base without changing $\|1-U_p\|$. After sorting, inverse pairs cancel exactly in each straight segment. For first-axis shifts there are no swaps. For arbitrary shifts no space-time plaquette enters. The uniform pressure estimate and Minkowski give $CN/\sqrt\beta$ for the $L^2$ difference between transporters with $N$ swaps. Cauchy–Schwarz with the $L^2$ curvature bound controls the $L^1$ difference between the two adjoint transports, whether the face itself appears among the swaps or not. [C4’s periodic pressure bound](../../central-quotients/tangent-curvature/periodic-limit/pressure.md)

On the packet support $\|v\|_1=O(R)$ and the absolute mass of the test is at most $8R^2$. Thus for $\|z\|_1\le LR$ changing the root costs at most $C_L R^4/\sqrt\beta$. The time trunk conjugates all terms together. The function $X\mapsto e^{-s|X|^2}$ is globally Lipschitz, and both slice observables are bounded by one. Together with the common-root comparison this gives, at equal time, for the true spatial translation $U(z)$ and the **finite-$R$** free marginal $\rho_R^G$,
$$
 \left|\langle\psi,U(z)\psi\rangle-\int e^{iz\cdot k}\,d\rho_R^G(k)\right|
       \le C_{s,L} R^4/\sqrt\beta.                                      \tag{2}
$$
The same reflection-positive Hilbert space contains all the translations. This use of the equal-time reading includes the mass at $T=0$. Our proof below only needs $L=4$. [C4’s comparison at all time lags](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/667f24719eaaae9f5600e931031c54373672b284/yang-mills/central-quotients/tangent-curvature/periodic-limit/joint-momentum/README.md)

A4 subsequently improved (2) to $C_{s,L}R^{7/2}/\sqrt\beta$. The same signed sorting can be done as three swaps of whole perpendicular segments. Each swap changes the path by a single rectangular loop of side lengths $a,b$. Site-plane reflection gives $1-W(a,b)\le ab[1-W(1,1)]$ for the normalized Wilson trace, hence $\|1-U_{a\times b}\|_2\le C\sqrt{ab/\beta}$. Summing three such errors gives $C_LR/\sqrt\beta$ per transporter for $\|z\|_1\le LR$. Multiplying by the packet mass costs $C_LR^3/\sqrt\beta$ for the translated root. A4’s common-root half-weighted heat estimate costs $C_{s,L}R^{7/2}/\sqrt\beta$ and dominates. Below, either (2) or this sharper comparison can be inserted unchanged. Equation (1) uses the sharper one. [A4’s rectangle comparison](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/e2e56f57f9950af5e32a60b8486e1bb3587e34ca/yang-mills/observable-normalization/transfer-increments/spatial-packet/strip/rectangles.md) · [Reflected strips and common-root error](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/d2fde0ad92039092641f1d095b279b48245d6b8b/yang-mills/observable-normalization/transfer-increments/spatial-packet/strip/README.md)

C4’s existing tightness argument also checks out. A smooth compact test $g$ agrees on the representative cube with its $2\pi R$ periodization for all sufficiently large $R$. Its coefficient at translation $z$ is $(2\pi R)^{-3}\widehat g(z/R)$. Summing over all integer $z$ recovers the test; taking only $z=Rj$ folds scaled momenta differing by $2\pi$. The rapid-decay bound has a uniform summable tail in $\|z\|/R$. Polynomial time tests in $x=e^{-RE}$ include order zero. Vague convergence on $[0,1]\times\mathbb R^3$ together with total-mass convergence gives tightness. The explicit limit assigns zero mass to $x=0$, so return to the finite-energy coordinate also preserves tightness. The positive-window endpoint first fixes the cutoff in $\|z\|/R$, then fixes $c$ in $R\sim c\beta^{1/8}$. [Sutherland, Fourier series of a periodization](https://math.mit.edu/classes/18.785/2018fa/LectureNotes17.pdf)

## Free momentum tails, including all terms of the bounded observable

Let $W_R$ denote the one-color equal-time free magnetic measure in the scaled momentum $p=Rk$. Its density on the scaled cube is bounded by $C|p|\prod_{i=1}^3(1+|p_i|)^{-8}$. Its total mass $v_R$ has a uniform upper bound and a positive lower bound: on $[1,2]^3$ the fourfold box factors, the third forward difference and the $12$ projection amplitude are all bounded below. The same facts hold for the continuum-block measure $W$ on $\mathbb R^3$. For $u\ge0$,
$$
 W_R\{\|p\|_\infty\ge u\}\le C(1+u)^{-6}.
$$
Indeed cover the tail by the three single-coordinate events and bound $|p|$ by $\sum_i|p_i|$. In the tail coordinate the first moment of $(1+|p_i|)^{-8}$ is $O((1+u)^{-6})$. If the moment falls on another coordinate, its integral is finite and the tail is $O((1+u)^{-7})$. [Magnetic symbol and explicit comparison](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/10)

The determinant expansion for the centered bounded observable is a positive mixture. At order $j\ge1$ its scaled momentum is the representative of the sum of $2j$ independent draws from $W_R/v_R$, reduced modulo $2\pi R$ in each coordinate. The weight is
$$
 a_{j,R}=D_R^{-3}\frac{(3/2)_j}{j!}
          \left(\frac{2s v_R}{D_R}\right)^{2j},\qquad D_R=1+2s v_R .
$$
The ratio in parentheses is uniformly less than one. Centering removes the $j=0$ term. This representation follows by expanding the equal-time determinant and taking the torus Fourier coefficients. Uniqueness holds on the compact momentum torus. For the limiting distribution one uses ordinary addition. Centered representatives can only reduce the absolute size of each coordinate of an unwrapped sum. If its maximum norm is at least $u$, at least one draw has norm at least $u/(2j)$. The union bound gives $C(2j)^7(1+u)^{-6}$ for this conditional probability. The sum over the weights $a_{j,R}$ converges uniformly even with this polynomial factor. Hence the **entire free marginal** satisfies
$$
 \rho_R^G\{\|Rk\|_\infty\ge u\}\le C_s(1+u)^{-6}.                      \tag{3}
$$

For a matching continuum lower bound, retain $j=1$. In one leg take $p_1\in[2H,3H]$ with $|\sin(p_1/2)|\ge1/2$, and $p_2,p_3\in[1,2]$. The first-coordinate box factor squared is then bounded below by $cH^{-8}$. The other two and the third-difference factor have positive lower bounds, and the $12$ projection amplitude $(p_1^2+p_2^2)/(2|p|)$ is at least $cH$. The allowed $p_1$ intervals have total length at least $cH$ for all large $H$. Keep the second leg inside $[1,2]^3$, a set of fixed positive mass. The total first component exceeds $H$, giving limiting mass at least $c_sH^{-6}$. The conclusion concerns the unwrapped limiting distribution of this specific filter.

## A finite Fourier test for the interacting tail

For a single coordinate write
$$
 F_M(k)=\left|M^{-1}\sum_{r=0}^{M-1}e^{irk}\right|^2,\qquad K_M=(1-F_M)^4 .
$$
The Fourier coefficients of $F_M$ are the nonnegative triangular counts divided by $M^2$ and sum to one. Thus $K_M$ has coefficient $\ell^1$ norm at most 16 and uses only indices $|j|\le4(M-1)$. It is nonnegative. Also $1-F_M=M^{-2}\sum_{r,l}(1-\cos((r-l)k))\le C M^2 k^2$. On the representative interval the geometric sum gives $F_M(k)\le(\pi/(M|k|))^2$ away from zero. [MIT, Fourier series and the Fejér kernel](https://ocw.mit.edu/courses/18-102-introduction-to-functional-analysis-spring-2021/8fb8d5c170f1613151aca71de21027bc_MIT18_102s21_full_lec.pdf)

If $H>\pi R$ the event in (1) is empty. Otherwise take $M=\lceil2\pi R/H\rceil$. For $4\pi\le H\le\pi R$ we have $M\le R$ and $M/R\le3\pi/H$. On $|Rk_i|\ge H$, $F_M(k_i)\le1/4$, hence $K_M(k_i)\ge(3/4)^4$. For all $k$ we also have $K_M(k_i)\le C\min(1,(M|k_i|)^8)$. Put $A=R/M\ge1$ and $U=\|Rk\|_\infty$. Layer cake for the finite free measure and (3) give
$$
 \int\min(1,(U/A)^8)\,d\rho_R^G
  =\frac{8}{A^8}\int_0^A t^7\rho_R^G(U>t)\,dt
  \le C_s A^{-6}.
$$
Splitting at one bounds the last integral by $C_s(1+A^2)$. Using an eighth-order cutoff avoids the logarithm in the truncated sixth moment. Comparing the integrals of the trigonometric polynomial $K_M$ by (2) costs at most $16 C_{s,4}R^{7/2}/\sqrt\beta$ with A4’s comparison, or $16C_{s,4}R^4/\sqrt\beta$ using (2) alone, independently of $M$. Divide by $(3/4)^4$ and take the union of the three coordinate events. This proves (1), with no choice of expanding Fourier-test support after $\beta$ is selected.

The result supplies an error bound for escape to large **scaled lattice momentum**. At a fixed endpoint constant $c$ the estimate permits an amount $O(c^{7/2})$ to escape, independent of $R$. Fixed-coupling positivity of the infinite-volume lattice gap, the reading at an actual correlation length, and construction of a continuum Yang–Mills theory with a mass gap remain open. [Formal and numerical checks](execution.md)
