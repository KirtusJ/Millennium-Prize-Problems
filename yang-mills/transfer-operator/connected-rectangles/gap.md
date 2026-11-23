# The gauge-invariant spectral gap and the shortest spatial cycle

Use open time, periodic space $L^3$, $L\ge2$, a positive Wilson transfer divided by its top eigenvalue, and its normalized invariant vacuum. Positive oriented links are distinct variables, including opposite directed links between the same two sites on a side-two torus. In the spatial multigraph the girth is $g=\min(4,L)$. For $L\ge4$ a simple shorter cycle cannot lift to a closed circuit of the cubic lattice and cannot wind around the torus. For $L=2,3$ a winding line realizes length $L$. There are no self-loops. The four sides of an ordinary plaquette realize length four.

Hold $0\le\beta_s\le\rho$ fixed and vary the common temporal coupling $\zeta$. For bounded observables $F,G$ on single spatial slices $k$ steps apart, expand in the temporal face variables at zero, retaining all spatial couplings. The forest factorization at each intervening slab forces degree at least $gk$. It holds with arbitrary spatial face factors. The analytic bound is uniform in open time extent, box size and separation. Its prefactor may depend on the support of $F,G$. Schwarz's lemma for $|\zeta|\le\rho$ gives
$$
        |\operatorname{Cov}(F_0,G_k)|\le
        2\|F\|_\infty\|G\|_\infty e^{m_F+m_G}
                  (\beta_t/\rho)^{gk}.
$$
Pass to the infinite-time vacuum at fixed $L$. For a centered slice vector $v=(F-\langle F\rangle)\Omega$, the left side with $G=F$ (conjugating the first reading when complex) is $\langle v,S^k v\rangle$. For any $s>(\beta_t/\rho)^g$ the spectral mass on $[s,1]$ is bounded by the prefactor times $[(\beta_t/\rho)^g/s]^k$. Sending $k$ to infinity removes it. Bounded gauge-invariant multipliers of the strictly positive ground state are dense in the gauge-invariant slice Hilbert space. Taking the closed spectral projection over that dense set proves
$$
                  \|S_{\mathrm{vac}^\perp}\|\le(\beta_t/\rho)^g
                  \quad (0<\beta_t<\rho).
$$
This refers to the physical gauge-invariant space. In the infinite-volume vacuum the same estimate holds with $g=4$. For local half-history tests in the reflected Hilbert space, their supports are separated by $k-O_F(1)$ empty slabs after translating one of them. The same forest and local analytic bounds apply on the real axis after the volume limit. The fixed loss in the number of slabs is absorbed into the test-dependent prefactor. Such tests generate the vacuum Hilbert space. The positive time transfer and the same projection argument give the norm bound. [Periodic transfer](../periodic-time/) · [General spectral-projection argument](../../spectral-support/)

## A matching lower test on the isotropic trajectory

Take $F=\chi$ around a shortest winding polygon at $L=2,3$, and around one elementary plaquette at $L\ge4$ or in infinite volume. Write $C_1$ for its adjacent connected moment and $C_0$ for its variance. Then uniformly in these volumes,
$$
               C_0=1+O(\beta),\qquad C_1=(\beta/4)^g(1+O(\beta)).
$$
Under independent Haar the product of distinct links is Haar, with $\mathbb E\chi=0$ and $\mathbb E\chi^2=1$. For the adjacent moment the intervening slab must contain a cycle. At the minimal degree $g$ there are only temporal faces, once each. The center parity on the lower spatial links forces exactly the chosen $g$ edges. They form a cylinder to the same upper contour, including for the two different parallel edges at $L=2$. The cylinder contraction gives $4^{-g}$. Its subsets cannot fill just one of the two contours or form a closed surface. The disk estimate with support bounded by eight links and $g\le4$ gives a volume-independent Taylor remainder. This reasoning for one elementary plaquette and one step does not use the growing-rectangle theorem's assumptions $n,m,k\ge2$.

Apply the Rayleigh quotient to the centered $F\Omega$. It gives $\|S_{\mathrm{vac}^\perp}\|\ge C_1/C_0$. Together the bounds give a lattice mass between $g\log(\rho/\beta)$ and $g\log(4/\beta)+O(\beta)$, uniformly in $L$, on the isotropic trajectory $\beta\downarrow0$. In infinite volume the bottom of positive spectral support need not be an isolated eigenvalue for this argument.

Münster's strong-coupling expansion treats the glueball mass in Euclidean lattice gauge theory. His later calculation resolves glueball dispersion and higher-order terms. Langelage, Münster and Philipsen explicitly derive the elementary-plaquette tube and its leading $u^{4k}$ correlator in Eqs. (40)–(42), where $u=I_2(\beta)/I_1(\beta)$ for $SU(2)$. Our volume-uniform bound proves the leading logarithmic slope and distinguishes winding in a small spatial torus. It does not determine the higher-order glueball series. The surface competition for two large rectangles uses their extra cap area and multiplicity. [Münster (1981)](https://doi.org/10.1016/0550-3213(81)90570-8) · [Münster (1985), Eq. (28)](https://www-library.desy.de/preparch/desy/postpr/1985/desy85-007.pdf) · [Langelage, Münster and Philipsen (2008), Eqs. (40)–(42)](https://arxiv.org/pdf/0805.1163) · [Osterwalder and Seiler, strong-coupling lattice theory](https://doi.org/10.1016/0003-4916(78)90039-8)

## Comparing the mass with the string tension

There is a scale test which does not require taking infinite rectangle sides first. For any nonempty ordinary rectangle define $\sigma_Q=-A^{-1}\log(\langle W_Q\rangle/2)$ in lattice units. The [uniform single-loop bounds](../wilson-surfaces/) squeeze it between $\log(1/u)-\log(84)/A$ and $\log(1/q)$, where $u\sim1536\beta$ and $q\sim\beta/4$. Hence $\sigma_Q=|\log\beta|+O(1)$ uniformly over the rectangle. The same bounds apply to any area-law tension extracted from large rectangles. For the infinite-volume gauge-invariant mass $m$ just proved,
$$
          \frac{m^2}{\sigma_Q}=16|\log\beta|+O(1).
$$
Indeed, with $L_0=|\log\beta|$, write $m=4L_0+e$ and $\sigma_Q=L_0+d$ with uniformly bounded $d,e$. Subtracting $16L_0$ leaves $[(8e-16d)L_0+e^2]/(L_0+d)$, which stays bounded. Restoring one common isotropic spacing gives $(m/b)^2/(\sigma_Q/b^2)=m^2/\sigma_Q$. No common choice of physical units can give both a finite nonzero mass and a finite nonzero tension along $\beta\downarrow0$. This obstacle applies at the strong end. The usual asymptotically free continuum trajectory approaches the opposite end of the bare coupling.

At fixed spatial coupling the leading eigenvalues and multiplicities of the entire first cluster can now be computed from the single-slice covariance of the shortest Wilson loops. In particular on a fixed isotropic torus the additive error after $g\log(4/\beta)$ tends to zero. [Finite-box transfer reduction](../girth-shell/transfer.md)
