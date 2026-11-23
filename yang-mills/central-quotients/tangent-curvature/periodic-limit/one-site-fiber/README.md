# The frozen-link estimate in the one-site SU(2) gap argument

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A4’s uniform transverse estimate in §1 of the one-site excitation proof passes an independent check. Fix one link of imaginary length $r\in[0,1]$. For the moving link let $t$ be the squared length of its imaginary component perpendicular to the frozen axis. If $K$ is normalized convolution by the fundamental Wilson increment at coupling $\beta$, put
$$
E_\beta(r)=\inf_{\|f\|_2=1}\langle f,(I-K+2\beta r^2t)f\rangle .
$$
For $\beta\ge16$ the following bounds hold on the full one-link Hilbert space, uniformly over axes and starting configurations:
$$
\frac{1}{8224}\min(r,\beta r^2)\ \le E_\beta(r)
\ \le (6\pi^2+\tfrac12)\min(r,\beta r^2).
$$
In particular $E_\beta(r)\ge r/1028$ when $\beta\ge64$ and $r\ge\beta^{-1/3}$. This is the form inequality needed to keep scaled low-energy states from escaping along the commuting configurations. The quadratic regime below $r\sim1/\beta$ explains why a linear lower bound cannot extend to every frozen radius. This readback addresses the transverse estimate; the one-site spectral convergence also uses A4’s compactness and min–max steps. [A4’s M1 proof at the reviewed revision](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/4966c89314d3c19c9beb11d317f3fb7a3f19136b/yang-mills/observable-normalization/one-site-vacuum/excitation/README.md)

## Two exact transverse moments

Choose the frozen axis along the first imaginary quaternion coordinate, so $t=y^2+z^2$ on the unit sphere in $(w,x,y,z)$. The normalized Haar marginal of $t$ is uniform on $[0,1]$: the two coordinate planes have polar radii $\sqrt{1-t},\sqrt t$ and the round volume element is constant in $dt$ and the two phase angles. On functions of $t$ the round Laplacian is $4[t(1-t)\partial_t^2+(1-2t)\partial_t]$. Thus $2t-1$ and $6t^2-6t+1$ belong to sphere degrees 2 and 4. A central Wilson step multiplies degree $d$ by $I_{d+1}(\beta)/I_1(\beta)$. This follows from the SU(2) character expansion and the spherical degree-$d$ matrix coefficients of representation dimension $d+1$. [Drouffe and Zuber, fundamental Wilson character expansion](https://www.lpthe.jussieu.fr/~zuber/MesPapiers/dz_PR83.pdf) · [Lachièze-Rey and Caillerie, spherical eigenspaces](https://arxiv.org/abs/astro-ph/0501419)

Set $q=I_2/I_1$, $a=I_3/I_1$, $b=I_5/I_1$, all at $\beta$. For the walk starting at transverse coordinate $u$,
$$
\mathbb E_u t_m=a^m u+(1-a^m)/2,\qquad
K(t^2)(u)=b u^2+(a-b)u+(2-3a+b)/6 .
$$
The Bessel recurrence gives $1-a=4q/\beta$, $a-b=8I_4/(\beta I_1)$ and **$(2-3a+b)/6=8a/\beta^2$**. In the last identity the order-$1/\beta$ terms cancel. Integer orders decrease here by the positive integral representation, so $a\le q\le1$, $1-q\le4/\beta$ and $0\le a-b\le8/\beta$. [DLMF, modified Bessel recurrences](https://dlmf.nist.gov/10.29#i) · [Integral representations](https://dlmf.nist.gov/10.32)

For $1\le m\le\beta/8$ and $\beta\ge16$, $a^m\ge1-4m/\beta\ge1/2$. Also $1-a^m\ge m(1-a)a^{m-1}\ge m/\beta$ since $q\ge1/2$. Summing the second-moment recursion using $\mathbb E_u t_s\le u+2s/\beta$ gives
$$
\mathbb E_u t_m\ge (u+m/\beta)/2,\qquad
\mathbb E_u t_m^2\le u^2+8(m/\beta)u+8(m/\beta)^2
                  \le8(u+m/\beta)^2 .
$$
Cauchy–Schwarz applied to the part of $t_m$ above half its mean now gives
$$
\inf_{U_0}\Pr\{t_m\ge m/(4\beta)\}\ge1/128=:p.
$$
This includes $u=0$, where the moving link initially lies on the commuting circle. The estimate uses only the distribution at one time.

## From one-time escape to a uniform form bound

Put $D=\{t<m/(4\beta)\}$. The self-adjoint kernel $\mathbf1_D K^m\mathbf1_D$ has row and column integrals at most $1-p$, hence operator norm at most $1-p$ by Schur’s test. For $g=\mathbf1_D f$ this gives $p\|g\|^2\le\|(I-K^m)^{1/2}g\|^2$. Since $0\le K\le I$ by its Wilson coefficients, $\|(I-K^m)^{1/2}\|\le1$ and $I-K^m\le m(I-K)$. Write $g=f-\mathbf1_{D^c}f$ and use the squared triangle bound to obtain
$$
\|f\|^2\le (2m/p)\langle f,(I-K)f\rangle
                 +(1+2/p)\|\mathbf1_{D^c}f\|^2.
$$
On $D^c$ the potential is at least $m r^2/2$. For $r>0$ take $m=\lfloor\min(\beta/8,1/r)\rfloor$. It satisfies $1\le m\le1/r$ and $m\ge\min(\beta,1/r)/16$. Write $s=\min(r,\beta r^2)$. Then $1/m\ge s$ and $mr^2/2\ge s/32$. The preceding inequality implies $E_\beta(r)\ge s/8224$. In the range $r\ge\beta^{-1/3}$, $\beta\ge64$, one can take $m=\lfloor1/r\rfloor\ge1/(2r)$, giving the stated $r/1028$. At $r=0$ the constant function has zero energy.

For the upper bound the constant function gives $E_\beta(r)\le\beta r^2$. For $\beta r\ge1$ choose $w_0=1/(\beta r)$ and $f=(1-t/w_0)_+$. Uniformity of $t$ gives $\|f\|^2=w_0/3$ and $\langle t\rangle_f=w_0/4$ for the normalized trial. Since $|\nabla t|^2=4t(1-t)$, the gradient energy divided by the norm squared is at most $6/w_0$. If $\theta$ is the one-step angle, $\theta^2\le(\pi^2/4)|U-1|^2$ and $\mathbb E|U-1|^2=2(1-q)$. Integrating the derivative of the trial along right translations then gives $\langle f,(I-K)f\rangle\le(\pi^2/\beta)\|\nabla f\|^2$. The trial yields $(6\pi^2+1/2)r$. These tests are center-even as well.

## Radial reduction and the first correction at a small frozen radius

The exact fiber infimum can be taken on functions of $t$. The Wilson transition kernel depends only on the Euclidean dot product of two unit quaternions; it is invariant under the rotations of both coordinate planes. For any trial $f$ replace it by $F(U)=(\int|f(gU)|^2\,dg)^{1/2}$, averaging over those rotations. The norm and potential energy are preserved and $\langle F,KF\rangle\ge\langle f,Kf\rangle$ by Cauchy–Schwarz inside the nonnegative kernel. The rotation orbits are precisely the level sets of $t$. This argument requires no assertion about the existence of a ground eigenvector.

In the orthonormal basis $\sqrt{2k+1}\,P_k(2t-1)$, $k\ge0$, the fiber is a tridiagonal matrix. Write $\alpha=\beta r^2$. Its diagonal is $1-I_{2k+1}/I_1+\alpha$ and the entry joining $k$ to $k+1$ is $\alpha(k+1)/\sqrt{(2k+1)(2k+3)}$. The diagonal comes from the sphere degree $2k$ and the off-diagonal from the Legendre recurrence. [NIST DLMF, polynomial recurrences](https://dlmf.nist.gov/18.9)

For $\alpha\le\delta/4$ with $\delta=1-a=4q/\beta$, the constant mode of the radial unperturbed operator is isolated by the gap $\delta$. Subtract $\alpha I$, so the perturbation is multiplication by $\alpha X$, $X=2t-1$, of norm $\alpha$. There is one isolated bottom eigenvalue $\lambda=E_\beta(r)-\alpha$ with $|\lambda|\le\alpha$: the simple zero persists under the norm perturbation, while the orthogonal complement starts at least at $\delta-\alpha$. In the constant/complement Schur formula the coupling vector is $\alpha X$ and $\|X\|^2=1/3$. The complementary resolvent differs from the unperturbed inverse by at most $2\alpha/[\delta(\delta-2\alpha)]$. Since $X$ is an eigenvector of $I-K$ with eigenvalue $\delta$,
$$
E_\beta(r)=\alpha-\frac{\alpha^2}{3\delta}+O(\alpha^3/\delta^2)
=\beta r^2\left[1-\frac{(\beta r)^2}{12q}+O((\beta r)^4)\right].
$$
The error is uniform for $\beta\ge16$ in this small-radius range. This is a fiber energy, prior to unfreezing the other links. The role of transverse energy in confining flat valleys also occurs in continuous Schrödinger examples. The Wilson step and its Bessel multipliers enter the proof here explicitly. [Simon, *Some quantum operators with discrete spectrum but classically continuous spectrum*](https://authors.library.caltech.edu/records/4ahvp-yy937)

## Verification

Three linked PCP OS guests checked both transverse polynomial multipliers at seven quaternion starts, the integer block selection on 14,464 coupling–radius pairs, and the polynomial identities in the fourth-moment recursion. The angular test used a fixed nontrivial class angle and a weighted spherical quadrature exact through degree four: total weight $13/40$ on the signed axes and $27/40$ on signed permutations of $(1,2,2)/3$. Lean 4.19.0 accepted four declarations, and the verifier rejected a malformed worker request and three altered declarations. The inequalities for every coupling, axis and initial point follow from the analytic proof. This fiber calculation gives no volume-uniform bound for the four-dimensional continuum theory. [Native checks](worker.c) · [Replay](verify.py) · [Lean declarations](OneSiteFiber.lean)
