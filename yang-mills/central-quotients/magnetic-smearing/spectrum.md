# A positive-time magnetic signal and its physical-energy law

At spacing $b=1/r$, use the weights $g_{m,r}$ and the joint condition for $m=1$ or $2$ from the [smoothing estimate](smoothing.md). On a spatial slice $n$ put
$$
 X_r(n)=\sqrt\beta\sum_x g_{m,r}(x)\operatorname{Im}
   [P_x U_{12}(x,n)P_x^{-1}],\qquad O_r(n)=\exp(-\sigma|X_r(n)|^2),\quad\sigma>0 .
$$
Here $P_x$ uses spatial coordinate paths from the slice's origin. $O_r$ is bounded, gauge invariant, depends only on this slice, and has support of bounded physical diameter. The scale factor is consistent with integrating a curvature of dimension two against a three-dimensional spatial profile: the cell volume times $b^{-2}$ is $b$, and $g_{m,r}$ approximates $b\,\partial_3^m\psi$. The norm is taken **after** summing the transported curvatures. For computations at several slices one may transport each $X_r$ along the time axis to a common origin. This leaves each $O_r$ exactly unchanged. The Ward theorem for vector components below refers to this common frame.

## Fourier limit

Define $\widehat\psi(p)=\int_{\mathbb R^3} e^{-ip\cdot x}\psi(x)\,d^3x$. The Gaussian covariance of the finite set of linear tests used in the [Ward proof](ward.md) is that of the cubical projection onto exact two-forms. Write $q_j^2=4\sin^2(k_j/2)$ and $\omega(k)=2\operatorname{arsinh}(\sqrt{\sum_{j=1}^3q_j^2}/2)$. For one color and equal profiles at time difference $n$, the discrete covariance is
$$
 \int_{[-\pi,\pi]^3}\!\!\!
 |\widehat g_{m,r}(k)|^2\frac{q_1^2+q_2^2}{2\sinh\omega(k)}
                e^{-|n|\omega(k)}\,\frac{d^3k}{(2\pi)^3}.
$$
This is the Fourier calculation for two spatial faces with a spatial weight on each. Integrating the temporal multiplier $(\sum_{i=1}^3q_i^2+2-2\cos k_4)^{-1}$ gives the indicated one-dimensional Green coefficient. [Lattice projection and normalization](../tangent-curvature/dipole.md)

Poisson summation gives $\widehat g_{m,r}(k)=r^{m+2}(1-e^{-ik_3})^m\sum_{\ell\in\mathbb Z^3}\widehat\psi(r(k+2\pi\ell))$. Substitute $k=p/r$. On the expanding cube the profile sum is bounded by $C_N(1+|p|)^{-N}$ for any fixed $N$: the nonzero translates have norm at least a constant times $r|\ell|_\infty$ and $\widehat\psi$ is rapidly decreasing. Also $r^m|1-e^{-ip_3/r}|^m\le |p_3|^m$ and $(q_1^2+q_2^2)/(2\sinh\omega)\le C|p|/r$. These bounds dominate the integrand after cancellation of the powers of $r$, including equal time. For $n/r\to t$ the covariance tends to
$$
 C_m(t)=\int_{\mathbb R^3}|\widehat\psi(p)|^2 p_3^{2m}
       \frac{p_1^2+p_2^2}{2|p|}e^{-|t||p|}\frac{d^3p}{(2\pi)^3}.
$$
Mixed profiles have the corresponding polarized integral. This also proves the uniform variance bound used in the Ward error. Combining that estimate with Cramér–Wold gives the joint Gaussian limit of all the chosen commonly transported linear tests. The colors are independent. Distinct bounded physical times and time zero are allowed. All calculations here take joint regulator limits on the actual Wilson vacuum.

## Transfer measurements

Choose any nonzero real profile. Then $C_m(0)>0$ and $C_m(t)>0$ at every finite $t$. In the three colors a Gaussian determinant gives, with $D=1+2\sigma C_m(0)$,
$$
 \mathbb E O_r\to D^{-3/2},\qquad
 B_r(\lfloor rt\rfloor)=\operatorname{Cov}(O_r(0),O_r(\lfloor rt\rfloor))
 \longrightarrow B(t)=[D^2-4\sigma^2 C_m(t)^2]^{-3/2}-D^{-3}>0 .
$$
At zero the same formula uses a single Gaussian vector. Bounded continuity gives all these convergences. In particular the mean-normalized and variance-normalized connected readings at any fixed physical $t>0$ both converge to strictly positive, finite numbers. So does $B_r(\lfloor rt\rfloor)/B_r(\lfloor rt_0\rfloor)$ for fixed positive $t,t_0$. These are positive-time limits along the specified weak-coupling trajectory for the same time-slice operator at both insertions.

Let $\mu$ be the pushforward of the positive weight in $C_m(0)$ under $p\mapsto |p|$. The connected spectral measure for the limiting **physical** energy is
$$
  \rho=D^{-3}\sum_{j\ge1}\frac{(3/2)_j}{j!}
                    (4\sigma^2/D^2)^j\,\mu^{*2j}.
$$
The series converges in total mass since $2\sigma C_m(0)<D$. It reproduces $B(t)$ including its value at zero. For the original normalized transfer $\widehat T$, test its spectral measure in the vector $(O_r-\langle O_r\rangle)\Omega$ at energies $E=-r\log\widehat T$. The moments of the measures pushed forward under $E\mapsto e^{-E}$ on $[0,1]$ converge to those of $\rho$. For integer $j\ge1$, replacing $e^{-jE}$ by $e^{-\lfloor rj\rfloor E/r}$ costs $O(1/(rj))$ uniformly in $E\ge0$ by the mean-value bound, and the norms of the vectors are bounded. The zeroth moment also converges. Polynomial density proves weak convergence on the compactified energy axis. The stated limit has no atoms at zero or infinity, and the continuous radial pushforward gives no finite atoms. All finite intervals with positive limiting weight therefore converge with their raw spectral weight.

If $J=\int\psi\ne0$, let $d=2m+4$. The density of $\mu$ at small energy has the expansion
$$
  \mu(dE)=\left[\frac{|J|^2}{2\pi^2(2m+1)(2m+3)}\,E^{d-1}
     +O(E^{d+1})\right]dE .
$$
Indeed $|\widehat\psi(p)|^2=|J|^2+O(|p|^2)$ for a real smooth compact profile, and the angular integral of $\theta_3^{2m}(\theta_1^2+\theta_2^2)$ is $8\pi/[(2m+1)(2m+3)]$. Define $a=(d-1)!|J|^2/[2\pi^2(2m+1)(2m+3)]$. Then $C_m(t)\sim a\,t^{-d}$, and integrating the first convolution over a simplex gives
$$
 B(t)\sim 6\sigma^2D^{-5}a^2 t^{-2d},\qquad
 \rho([0,\epsilon])\sim \frac{6\sigma^2D^{-5}a^2}{(2d)!}\epsilon^{2d}.
$$
Higher convolutions have total mass $O(\epsilon^{4d})$ on this interval; bound each by $\mu([0,\epsilon])^{2j}$ in the series. This gives exponents twelve and sixteen for the two orders. Every sufficiently small fixed window $(\epsilon/2,\epsilon)$ has positive limiting mass. Consequently $r\,\Delta_{\rm lattice}\to0$ along each admissible trajectory for the finite-box full gauge-invariant transfer gap.

There is a rate consequence even when no physical spacing has been chosen. For arbitrary $\beta,L\to\infty$ set $r=\min(\beta^{1/13},L^{1/3})$. Both second-order conditions then hold because $\beta\ge r^{13}$ and $L\ge r^3$. Thus $\min(\beta^{1/13},L^{1/3})\Delta_{\rm lattice}\to0$. For a prescribed logarithmic bare trajectory with a separately fixed physical spacing, this last estimate concerns only the lattice-unit gap. The continuum correlations derived above are those of free magnetic curvature in the exhibited sector. An interacting continuum construction at a fixed nonzero renormalized scale requires other control.
