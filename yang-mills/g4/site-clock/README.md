# The Wilson site scalar at the correlation length

For the sum of the 24 plaquette half-traces around a site, the covariance at every even time separation of at least two lattice steps is strictly positive at all sufficiently large Wilson couplings. This holds uniformly over the choice of isotropic even-periodic thermodynamic limit in four-dimensional pure $SU(2)$. In particular the normalization $Z$ in Z4's H3(a) exists for this observable whenever the positive lattice gap defines the correlation length. The argument also gives a way to test the midpoint ratio using covariances at a sublinear number of earlier time steps. The required precision of those inputs matters. [Z4’s Theorem S, §§1–2](../../z4/attempt/reviews/c1-OS/THEOREM_S.md) · [Moment enclosures and precision](certificate.md)

A4 derived a quantitative floor for the same normalization on the actual clock. Combining it with the moment approximation below gives a relative-error test from Wilson covariances through time $O(N\beta^{-1/128})$. This is a bound on time extent. The test also requires independently certified moment values and a specified clock. [A4’s clover result](../../observable-normalization/transfer-increments/local-action/site-scalar/README.md) · [Quantitative degree and input precision](certificate.md#a-quantitative-bound-for-the-actual-wilson-clock)

## The one-slice buffer

Let $\mathcal P(x)$ be the 24 distinct unoriented elementary plaquettes with corner $x$. Put $O(x)=\sum_{p\in\mathcal P(x)}(1-\tfrac12\operatorname{Tr}U_p)$ and $Y(x)=\beta(O(x)-\langle O\rangle)$. Z4’s stated field is $S(x)=\sum_{p\in\mathcal P(x)}\tfrac12\operatorname{Tr}U_p=24-O(x)$, so $S(x)-\langle S\rangle=-Y(x)/\beta$. Time reflection in the site plane sends $Y(x)$ to $Y(\theta x)$, including its temporal plaquettes. Thus $Y(e_0)$ belongs to the closed positive-time link algebra, with support in times $0,1,2$. Write $v=[Y(e_0)]$ in the reflected Hilbert space and $T$ for a one-step translation. Translation invariance and the definition of its inner product give, for every integer $j\ge0$,

$$
 M_j=\operatorname{Cov}(\beta O(0),\beta O((2+2j)e_0))
     =\langle v,T^{2j}v\rangle
     =\int_{[0,1]} u^j\,d\nu(u).
$$

Here $\nu$ is the finite positive spectral measure of the positive contraction $T^2$ at $v$, and $u^0=1$ also at zero. Reflection first places the left insertion at $-e_0$ and the right at $(1+2j)e_0$. The two-step representation only needs a self-adjoint contractive $T$. Strict positivity of its spectrum in an infinite-volume state is unnecessary. The uniform one-face action moment and Cauchy–Schwarz bound $M_0\le B$ independently of state and large $\beta$. [Lüscher, Wilson transfer matrix](https://doi.org/10.1007/BF01614090) · [Osterwalder and Seiler, Wilson reflection positivity](https://doi.org/10.1016/0003-4916(78)90039-8) · [Periodic-state moment bound](../../central-quotients/tangent-curvature/periodic-limit/pressure.md)

## Two fixed-time inputs

At each fixed $j$, the joint rooted curvature theorem and uniform integrability of fourth moments give $M_j\to M_j^*$ uniformly in the periodic-state choice. Wick contraction gives

$$
 M_j^*=\frac32\sum_{p\in\mathcal P(0),\,q\in\mathcal P((2+2j)e_0)} P_{p q}^{\,2},
$$

where $P$ projects onto exact lattice two-forms in one color. Indeed a scaled single-face action tends to half the squared norm of a three-color centered Gaussian with component cross-covariance $P_{pq}I_3$. The calculation uses the joint fixed-list theorem for mixed orientations. A same-orientation comparison alone would leave cross terms undetermined. Every entry of $P$ is a Fourier coefficient of a bounded multiplier on the four-torus and hence tends to zero along the time axis. There are 576 terms, so $M_j^*\to0$. [C4’s original-link tangent theorem and constant-mode argument](../../central-quotients/tangent-curvature/periodic-limit/spectral.md)

Choose the spatial $12$ face based at each insertion point. Its covariance $G(n)$ is strictly positive for $n>0$ and $n^4G(n)\to1/\pi^2$. The Fourier integral has positive integrand $e^{-n\omega}(h_1^2+h_2^2)/(2\sinh\omega)$ on a set of positive measure. Rescaling $q=p/n$ gives the constant by spherical integration. The corresponding squared term in the sum gives $M_1^*>0$ and $M_k^*\ge c(1+k)^{-8}$ for all $k\ge1$. Only fixed-time Wilson convergence is used before $k$ is chosen. [A4’s spatial-face Fourier integral and limit](../../observable-normalization/transfer-increments/local-action/spectrum.md)

## A mass window that survives at weak coupling

Uniform convergence at $j=1$ yields $M_1>0$ at sufficiently large $\beta$. Thus $\nu((0,1])>0$, and every $M_j$ is positive, however far out the chosen integer $j$ lies. For $0<s<1$ choose a fixed $k$ so large that $Bs^k<M_k^*/4$. For all sufficiently large $\beta$,

$$
 \nu([s,1])\ \ge\ M_k-Bs^k\ \ge\ M_k^*/4=:b_s>0,
 \qquad M_j\ge b_s s^j\quad(j\ge0).
$$

This follows by splitting the integral at $s$ and using $u^k\le1$ on the upper window. All thresholds may depend on $s$. The limiting estimate does not require ergodicity of the chosen states. For every sequence $\beta\to\infty$, every choice of state and every $j=j(\beta)\to\infty$,

$$
 M_j\longrightarrow0,\qquad
 \frac{\log M_j}{j}\longrightarrow0,\qquad
 \frac{M_{j+1}}{M_j}\longrightarrow1.
$$

For the first limit use $M_j\le M_k$ at fixed $k$ and then $M_k^*\to0$. For the second use the window lower bound and let $s\uparrow1$. For the last, Cauchy–Schwarz gives $M_i^2\le M_{i-1}M_{i+1}$. The ratios increase, so $1\ge M_{j+1}/M_j\ge (M_j/M_0)^{1/j}$. For any fixed state the mass at $u=1$ may enter these integrals. Centering gives orthogonality to the distinguished vacuum and the proof makes no further assertion about invariant vectors.

Now assume the chosen state has $0<m<\infty$, with $m=-\log\|T|_{\Omega^\perp}\|$ and $N=2\lfloor1/(2m)\rfloor$. Along a weak-coupling sequence H2 gives $N\to\infty$. With $J=N/2-1$ the exact normalization is $\beta^2 Z^2=M_J>0$. This proves H3(a) for this single site scalar in the stated regime. Its scaled normalization tends to zero with $-\log(\beta^2Z^2)=o(N)$. The local effective rate $-\frac12\log(M_{j+1}/M_j)$ tends to zero along any diverging lattice time, including the gap clock. Both rates here use lattice units. A finite bound on $M_{\lfloor(J-1)/2\rfloor}/M_J$ would require control in units of $m$. [Z4’s midpoint condition and corrections](../../z4/attempt/A1_REDUCTION.md) · [Periodic-state H2 argument](../../central-quotients/tangent-curvature/periodic-limit/README.md)

The finite-moment test below gives a rigorous interval for that ratio once the gap clock and original Wilson moments have certified inputs. A state-uniform bound on the ratio, positivity of the infinite-volume Wilson gap, H3(b,c), rotations at the physical scale and the continuum construction remain open. The Clay problem requires a nontrivial continuum theory for every compact simple gauge group. [Finite-moment test](certificate.md) · [Lean and PCP verification](execution.md) · [Jaffe and Witten, official problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

Two positive transfer measures with the same gap and opposite midpoint behavior agree with every free clover time moment within the current comparison error. This locates the missing information in the weight near the gap. [Spectral counterexample at the available precision](precision-limit.md)
