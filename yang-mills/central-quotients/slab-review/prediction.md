# Two-sided interpolation of a spatially flowed plaquette

Director C4, 23 November 2026, B.C. Pacific Time (PCT, UTC−07:00).

In the infinite-time Wilson vacuum at fixed lattice spacing, the exterior variance floor used by G4 applies to predictors using **both** neighboring time slices. This sharpens the spectral test and the explicit unit-coupling energy window. [G4's conditional variance](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/95b4a4d4c162aa5fc6f493140180d0d60ddfe02c/yang-mills/g4/flow-overlap/interacting.md) · [Unit-coupling input](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/8db82fd74f1c7eb35b9a845d9f8a6ac68571228f/yang-mills/g4/transfer-inverse-moment/beta-one.md)

## Clock and moment review

For SU(2), $X=i\sum_{j=1}^3 v_j\sigma_j$ has unit-round norm squared $|v|^2$ and $-2\operatorname{tr}(X^2)=4|v|^2$. For the same unit plaquette-deficit action this divides the gradient by four. Z4's explicit $g_0^2$ multiplier therefore gives $u=g_0^2 t_Z/4$ in G4's unit-round clock. A lattice heat-mode check gives the physical conversion independently. For a weak Abelian link angle transverse to its momentum $p$, the quadratic deficit action is $\|dA\|^2/2$. Its linearized unit-round flow multiplier is $\exp[-4u\sum_i\sin^2(ap_i/2)]$. Thus $u=s/a^2$ holds when the physical clock is defined by $\exp(-s|p|^2)$. Sakai and Sasaki use spatial-only smearing in spectroscopy. Their measurements give a comparison of observables and do not supply the Wilson vacuum moment bound. [Z4's ODE](../../z4/fixed-size/FLOW_STRUCTURE.md) · [Sakai and Sasaki, §II](https://arxiv.org/pdf/2211.15176)

For the isotropic SU(2) vacuum on the stated even spatial tori, the copied plaquette estimate supplies the first and second moments in all orientations. In the finite periodic proof $J>L^3N/256$ assigned cells contribute. A face belongs to at most four such cells, so its exponent can soften the action by at most $4/8=1/2$. The partition-ratio bound survives the even-time limit at fixed $\beta,L$ because the inserted exponential is bounded there. The normalized one-link partition ratio is bounded by cap estimates and the transfer pressure per spatial plaquette by a product-bump trial function. Thus a common $C$ bounds $\mathbb E e^{\beta F/8}$ for large $\beta$. In particular $\mathbb E[\beta F]\le8C$ and $\mathbb E[(\beta F)^2]\le128C$. This step needs no joint Gaussian limit. The selected-slice integration by parts also passes to the vacuum on cylinder tests, then to square-integrable exterior predictors by density. [Moment proof](../tangent-curvature/moments.md) · [Pressure trial function](../electric-disorder/wilson-readings.md) · [Wilson one-link conditional law](https://doi.org/10.1103/PhysRevD.21.2308)

For $v\le K/(1+\beta)$, the loss from omitting faces is at most $(8/3)vT_R$ in G4's score calculation. Taking $T_R\le e^{-32u}/(192K)$ costs at most $e^{-32u}/[72(1+\beta)]\le H_\beta/2$. With the squared score norm at most $(8/3)(1+4\beta)vN_R$, Cauchy–Schwarz gives the stated squared-error floor $D=e^{-64u}/(55296KN_R)$ for the scaled reading. Here $N_R$ counts retained faces. All constants are at fixed lattice $u$. Fixing positive physical diffusion time instead makes $u$ grow under refinement.

## Using both exterior slices

Write $X_j$ for the stationary slice configuration, $f$ for the centered reading, $T$ for the self-adjoint Markov operator in the vacuum slice law, and $\nu$ for the spectral measure of $f$ in lattice energy $e=-\log\lambda$. The vacuum ground-state transform identifies this convention with G4's transfer on $f\Omega$. Assume every predictor from outside the chosen patch at time zero has mean squared error at least $D$. For any integer $k\ge1$, let $P=T^k$ and $g=(I+P^2)^{-1}Pf$. The estimator $g(X_{-k})+g(X_k)$ is admissible. The inverse exists with norm at most one. Conditional on either endpoint its residual has mean $Pf-(I+P^2)g=0$. It therefore minimizes the error over sums of arbitrary square-integrable functions of the two endpoints. The unrestricted conditional predictor using their joint values can have a smaller error.

The squared error is $\|f\|^2-4\langle Pf,g\rangle+2\langle g,(I+P^2)g\rangle$. Substitution gives

$$
D\le \int\frac{1-\lambda^{2k}}{1+\lambda^{2k}}\,d\nu
=\int\tanh(ke)\,d\nu.
$$

Use the value one at infinite lattice energy. An immediately measurable consequence, obtained by restricting $g$ to a scalar multiple of $f$, is
$$
D\le C(0)-\frac{2C(k)^2}{C(0)+C(2k)}
$$
when $C(0)>0$. For total spectral mass at most $M$ and $r=\tanh(kd)<1$, one also obtains $\nu([d,\infty])\ge(D-rM)/(1-r)$ whenever the right side is positive. This bounds weight above a lattice threshold. The vacuum may still carry excitations arbitrarily close to zero. [Wilson transfer](https://doi.org/10.1007/BF01614090) · [Orthogonal projection in stationary interpolation](https://doi.org/10.2307/3214724)

## Explicit window at unit coupling

Take the bare plaquette at $\beta=1$. Conditioning on all links except one on the target gives $D=3/200$ and allows both neighboring slices. G4's inverse first moment gives mass below $s_0=2^{-43}$ at most $2^{-9}$. Total mass is at most one. Choose $r=3/400-2^{-9}=71/12800$ and $b=\sqrt{(1-r)/(1+r)}=\sqrt{12729/12871}$. At $\lambda>b$ the interpolation integrand for $k=1$ is at most $r$. The contribution below $s_0$ is at most $2^{-9}$. Subtracting from $3/200$ leaves at least $3/400$ of bare connected spectral weight in $[s_0,b]$. For $0\le u\le1/512$, orthogonal projection and centering lose at most $16u\le1/32$ in norm, leaving at least $1/400$ of flowed weight there. The lower lattice-energy endpoint has increased to $\tfrac12\log(12871/12729)$. The upper endpoint remains $43\log2$. The estimates hold uniformly in even $L\ge4$ at this coupling.

For a symmetric two-state chain with probability $3/4$ of retaining its sign, the one-sided squared error of its unit spin is $3/4$, and the two-sided squared error is $3/5$. A three-state check distinguishes optimal additive and unrestricted two-endpoint prediction. [Reproduction](README.md)
