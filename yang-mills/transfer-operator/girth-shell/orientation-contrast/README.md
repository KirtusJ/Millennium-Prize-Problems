# Moving a plaquette contrast from a vertex to a cube center

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Two differences of spatial Wilson plaquette traces distinguish the location of the measurement in the scalar band. In an even periodic cube or its spatial thermodynamic vacuum, write $f_{y,i}$ for the centered, unnormalized fundamental trace of the face based at $y$ with normal $i$. For a real unit vector $h$ with $\sum_i h_i=0$, use either
$$
A_y=\sum_i h_i f_{y,i},\qquad
C_y=\sum_i h_i(f_{y,i}+f_{y+\hat e_i,i})/2 .
$$
Thus the first test uses three faces meeting at one vertex. The second averages the opposite faces in each direction before taking the contrast. There is no further normalization of the second reading.

Use the infinite-time vacuum of isotropic four-dimensional $SU(2)$ Wilson theory at fixed mesh. Let $I=[\Delta,\Delta+e\beta^4r^2]$ with $\Delta$ the full lattice mass on the same geometry, $e>0$ fixed, $r\to0$, $\beta/r\to0$, and $\beta>0$. For bulk or $Lr\to\infty$, let $D=7/768$ and $R=\sqrt{e/D}$. The connected local spectral weights obey
$$
\mu_A(I)\sim\frac{R^5 r^5}{360\pi^2},\qquad
\mu_C(I)\sim\frac{R^7 r^7}{11340\pi^2}.
$$
Both coefficients are positive. Opposite-face averaging cancels the first-order displacement between the three face centers. The second coefficient retains both the remaining geometric displacement and the change of the scalar eigenvector with momentum. The results refine the [orientation upper bound](../oriented-edge/README.md); all energies and momenta use lattice units.

## A matrix estimate for the original transfer

Fix momenta $|k|\le\kappa$ in a sufficiently small neighborhood of zero. The three scaled centers $b_i(z,k)$ from A4's band argument have gaps $|b_1-b_i|\ge c|z|^4$ for $i=2,3$. The center differences are exactly proportional to $z^4$. Define
$$
Q_{z,k}(x)=x^5\frac{(x-b_2)(x-b_3)}{(b_1-b_2)(b_1-b_3)} .
$$
At small real coupling $z=\beta$, let $X$ be the centered transfer in this sector divided by $(\beta/4)^4$, and $P_1$ the exact top-branch spectral projection. Then $\|Q_{\beta,k}(X)-P_1\|\le C\beta^2$ uniformly in box and momentum. On the simple branch $x=b_1+O(\beta^6)$; both linear factors relative to their denominators equal $1+O(\beta^2)$, and $x^5=1+O(\beta^2)$. On the lower cluster $|x|\le C\beta^2$ the fifth power pays for the denominator of order $\beta^8$. On the other two upper branches use A4’s product estimate $|x^7\prod_i(x-b_i)|\le C\beta^{14}$. There $x\ge1/2$ and $|x-b_1|\ge c\beta^4$, so $|(x-b_2)(x-b_3)|\le C\beta^{10}$. This works also when the two lower centers coincide. [Uniform band, product estimate and three-branch multiplicity](../../../observable-normalization/uniform-band/momentum.md)

Let $J_\beta(k)$ have as columns the normalized centered Fourier trace vectors acting on the vacuum. Write $W_\beta=J_\beta^*P_1J_\beta$ in matching Fourier coordinates. The equal-time Gram bound gives $\|J_\beta\|=O(1)$. The matrix of $Q$ on these columns approximates $W_\beta$ to $O(\beta^2)$. It also has an even holomorphic continuation through $z=0$ with a uniform circle bound. To see this, expand it in lag moments of orders five through seven. Each scaled matrix moment has the common disk and uniform boundary bound from the connected spatial covariance estimates; apply those estimates entrywise, or polarize the two endpoint tests. The only remaining possible pole is of order eight from the displayed denominator. Boundedness along small positive real couplings removes it. On a fixed inner circle the two center gaps are uniformly bounded below. Evenness follows from the all-plaquette sign flip on even tori and the two local trace insertions. Cauchy's estimate now bounds the change from the value at zero by $C\beta^2$ uniformly. Analytic continuation here applies to the moment combination. [Common-disk estimates](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/ad1206de753e3a6aea7aeb71d388db506782d9aa/yang-mills/g4/local-scalar-edge/momentum.md) · [Evenness and endpoint bounds](../oriented-edge/README.md)

At each fixed box, the shell identification tends to its Haar inclusion and the vacuum endpoints tend to the Haar Fourier traces. After scalar subtraction and division by the quartic scale, the logarithm on the shell tends to Münster’s real symmetric matrix $B(k)$. Its simple top has a positive gap from the other orientations throughout this neighborhood. Consequently the value at zero just identified is the projector onto its normalized top vector $v(k)$, in face-centered coordinates. The fixed-box expansion is used only to identify this value; its volume-dependent remainder is absent from the circle estimate. Thus
$$
\|W_\beta-v(k)v(k)^*\|\le C\beta^2
$$
in face-centered coordinates. The same estimate holds in based coordinates after the corresponding diagonal phases. Since $W_\beta$ is positive of rank one, write it $w w^*$. Its nonzero eigenvalue is $1+O(\beta^2)$. Applying $I-vv^*$ to its normalized eigenvector equation bounds the perpendicular component by $O(\beta^2)$, so the phase can be chosen to give $\|w-v\|\le C'\beta^2$. **This amplitude estimate matters for the seventh power**: an additive error of order $\beta^2$ in the squared weight alone would be too large on some admissible trajectories. [Fixed-box shell identification](../joint.md) · [Münster, Eqs. (26)–(28)](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf)

## First surviving amplitudes

Put $s=\sum_i k_i^2$ and $u=(1,1,1)/\sqrt3$. At zero the top of $B$ is separated from the transverse pair by 24. The quadratic perturbation has diagonal $-s$ and off-diagonal $-(k_i^2+k_j^2)$. Acting on $u$, then removing the scalar component and dividing by 24, gives
$$
v_i(k)=\frac1{\sqrt3}\left[1-\frac{k_i^2-s/3}{24}\right]+O(|k|^4).
$$
Indeed $B(k)-B(0)=O(|k|^2)$ and the first-order eigenvector remainder is quadratic in that perturbation. Use the real top vector with positive scalar component.

Apart from a phase common to all three faces, the vertex coordinates supply factors $e^{\pm ik_i/2}$, with the sign depending on the Fourier convention. Averaging the opposite faces supplies instead $\cos(k_i/2)$ in coordinates centered on the cube. For the vertex contrast the leading amplitude is therefore $\pm i\sum_i h_i k_i/(2\sqrt3)$ with error $O(|k|^2+\beta^2)$. For the cube-centered contrast it is $-\sum_i h_i k_i^2/(6\sqrt3)$ with error $O(|k|^4+\beta^2)$: the coefficient combines $1/24$ from the moving eigenvector and $1/8$ from the cosine.

On the selected branch, set $p=k/r$. The near-edge estimates squeeze the accepted momenta between $D|p|^2\le e\pm o(1)$ and bound $|p|$ uniformly. The two squared amplitudes divided respectively by $r^2$ and $r^4$ tend uniformly on such bounded $p$ to
$$
\frac{|h\cdot p|^2}{12},\qquad
\frac{|\sum_i h_i p_i^2|^2}{108}.
$$
In the second expression the amplitude error $\beta^2/r^2$ vanishes under the stipulated hierarchy. Each local reading averages these weights over the momentum grid with divisor $L^3$. The normalized uniform ball of radius $R$ has $\mathbb E p_i^2=R^2/5$, $\mathbb E p_i^4=3R^4/35$ and $\mathbb E p_i^2p_j^2=R^4/35$ for $i\ne j$. The resulting ball averages are $R^2/60$ and $R^4/1890$. Multiplication by $r^3R^3/(6\pi^2)$ gives the stated weights. The open/closed window squeeze for bulk works with the same weighted balls because the integrands are uniformly bounded after rescaling and the limiting sphere has zero volume. [Momentum window and passage to bulk](../oriented-edge/README.md)

If $Lr\to\ell\in(0,\infty)$ away from a shell threshold, $L^3\mu_A(I)/r^2$ and $L^3\mu_C(I)/r^4$ converge to the respective sums of the displayed squared amplitudes over $p=2\pi n/\ell$ inside the ball. Either sum can vanish. For $Lr\to0$ only the cubic scalar at zero momentum can enter, and both contrasts have exactly zero weight there by symmetry. These joint asymptotics do not give a fixed-coupling threshold exponent or a physical continuum gap.

## Reproduction and adverse control

Run `python3 check.py` with NumPy. The program integrates the exact quartic matrix symbol and its eigenvectors over a window whose radial boundary is computed separately in each angular direction. With $e=D$ and $r=0.05$, the vertex and cube estimates, divided by $(4\pi/3)r^5$ and $(4\pi/3)r^7$ before the common Fourier factor, were $0.01666973$ and $0.00052926$. Freezing the cube eigenvector at its zero-momentum value gives $0.00029771$ and tends to $1/3360$, exposing the missing orientation correction.

The [guest runner](../../../observable-normalization/transfer-increments/replay-guests.py) accepts the measured PCP kernel followed by `--proof checks.txt` from this directory. It compiles the included `worker.c`, follows two child requests and compares the emitted check text after the three exits. The checks cover the product bound with coincident lower roots, 125 directional quadratic corrections, and the three ball constants. The aggregate text reproduced SHA-256 `b60ff403f70dde297c0065bc78ec6a17b8f5ca217c7960ce5a89b78858a9d937`. The runner's historical source-generation wire labels are reused for plain arithmetic receipts. The compact-transfer conclusion relies on the analytic argument above.
