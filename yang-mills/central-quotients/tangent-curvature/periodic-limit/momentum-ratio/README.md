# Energy-independent momentum ratios in the tilted magnetic packet

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)  
Research program directed by Kirtus Justus

For the bounded fourfold magnetic packet, sample its centered joint spectral measure with weight proportional to $e^{-nE}$. The ratio $V=|k|/E$ has a limiting distribution independent of the scaled energy $nE$. In particular **29.9889%** of the limiting weight lies at $|k|\le E/2$. The same fraction holds inside every fixed interval of scaled energies with positive Gamma(20,1) probability.

Use the four-dimensional isotropic $SU(2)$ Wilson states obtained by taking the even-periodic thermodynamic limit at each fixed $\beta$. Here $n$ is an integer time separation, $R\ge1$ the integer packet radius, $t=n/R\to\infty$, and $t^{21}R^4/\sqrt\beta\to0$. Spatial momentum $k$ uses its representative in $[-\pi,\pi)^3$. Assign any fixed value to the ratio on $E=0$; this convention does not affect convergence because the limiting energy is positive almost surely. The positive tilt gives zero weight to infinite energy. $V$ is an energy–momentum ratio of the packet, with no particle or group-velocity interpretation assumed. [Input joint limit and probe definition](../fourier-decay/README.md)

## Exact law

The limiting probability $F(v)=\Pr(V\le v)$ is zero below 0 and one above 1. On $[0,1]$,
$$
 F(v)=\frac{v^3}{199147520}\sum_{j=0}^8 c_j v^{2j}.
$$

| $j$ | $c_j$ | $j$ | $c_j$ | $j$ | $c_j$ |
|---:|---:|---:|---:|---:|---:|
|0|1120314195|3|−66803612590|6|103250544990|
|1|−5662679022|4|121733041040|7|−45686222570|
|2|23296715442|5|−140481495290|8|9432541325|

Two consequences give the weight near the boundaries:
$$
 \Pr(V\le \delta)=\frac{92169}{16384}\delta^3+O(\delta^5),\qquad
 \Pr(V\ge 1-\delta)=\frac{5586}{1105}\delta+O(\delta^2).
$$
For the Wilson measure these coefficients hold after taking the stated joint limit and then sending $\delta\downarrow0$. Its ratio CDF converges uniformly in the threshold in **absolute** error. The proof does not give relative errors for a prescribed shrinking shell. In particular the tilted Wilson weight at $|k|\ge E$ tends to zero, while each fixed open layer immediately inside that cone carries positive limiting weight.

## Reduction to two independent angles and one energy fraction

Write the two legs of the preceding joint limit as $(H_i,H_i\Theta_i)$, $i=1,2$. The energies are independent Gamma(10,1), and the directions are independent of the energies and of each other, with sphere-area density $f(\theta)=63\theta_3^6(1-\theta_3^2)/(8\pi)$. Changing variables to $S=H_1+H_2$ and $B=H_1/S$ gives Jacobian $S$. The joint density factors into the Gamma(20,1) law for $S$ and the Beta(10,10) law for $B$. The whole vector $B\Theta_1+(1-B)\Theta_2$, including its norm $V$, is independent of $S$. Define
$$
 U=1-V^2=JZ,\qquad J=4B(1-B),\qquad Z=(1-\Theta_1\cdot\Theta_2)/2 .
$$
$J$ and $Z$ are independent. The two inverse branches $B=(1\pm\sqrt{1-J})/2$ give $J\sim\operatorname{Beta}(10,1/2)$. Its normalization is $\mathcal B=B(10,1/2)=131072/230945$. [Euler beta integral](https://dlmf.nist.gov/5.12#E1)

The polar cosine of one direction has density $g(x)=63x^6(1-x^2)/4$ on $[-1,1]$. For Legendre polynomials $P_l$, let $a_l=\int_{-1}^1g(x)P_l(x)\,dx$. The nonzero values are
$$
 (a_0,a_2,a_4,a_6,a_8)=(1,5/11,-12/143,-8/55,-448/12155).
$$
Azimuthal integration in the spherical harmonic addition theorem leaves only the term of order zero. Independence then gives $\mathbb E P_l(\Theta_1\cdot\Theta_2)=a_l^2$. Orthogonality and polynomial density on $[-1,1]$ identify the entire distribution. Thus $Z$ has degree-eight density
$$
 h(z)=\sum_{l=0}^8(2l+1)a_l^2 P_l(1-2z)=\sum_{i=0}^8 h_i z^i
$$
on $[0,1]$. The two endpoint values are equal, $h(0)=h(1)=2646/1105$. As an independent endpoint check, $h(0)=2\int_{-1}^1g(x)^2 dx$ by Legendre orthogonality. [Spherical harmonic addition theorem, DLMF 14.30.9](https://dlmf.nist.gov/14.30#E9)

Multiplying independent $J$ and $Z$ gives the density of $U$ at $0<u<1$ as
$$
 \frac1{\mathcal B}\sum_{i=0}^8 h_i u^i
       \int_u^1 j^{8-i}(1-j)^{-1/2}\,dj
   =\sqrt{1-u}\,Q(u),
$$
where the substitution $1-j=(1-u)s^2$ gives the degree-at-most-eight polynomial
$$
 Q(u)=\frac2{\mathcal B}\sum_{i=0}^8 h_i u^i
       \sum_{k=0}^{8-i}\binom{8-i}{k}\frac{(-1)^k(1-u)^k}{2k+1}.
$$
Consequently the density of $V$ is $2v^2 Q(1-v^2)$. Integrating from zero gives the coefficients above. The product density also gives $Q(0)=h(0)\mathbb E[J^{-1}]=(19/18)h(0)$ and $Q(1)=2h(1)/\mathcal B$, which fix both endpoint coefficients without expanding the polynomial. For another check, independence and antipodal symmetry give $\mathbb E(1-V^2)=\mathbb E[J]/2=10/21$.

Joint weak convergence and continuity of the ratio at $S>0$ transfer these probabilities to the tilted Wilson measures. The limiting energy density and ratio CDF are continuous. Restriction to an energy interval with positive limiting mass and division by that mass preserve convergence. Uniform CDF convergence follows by partitioning the limiting CDF range into finitely many small steps and using monotonicity between the thresholds. These statements are uniform over the eligible state selections because the input theorem holds for every sequence of such selections. The results describe a time window shorter than one correlation length and provide no determination of a physical mass spectrum.

## What the ratio can test at one correlation length

Even recovering this same momentum-ratio law at one correlation length would leave Z4’s midpoint criterion (C) unresolved. Here is a joint-spectral version of G4’s transfer examples. Start with the normalized free packet’s full joint law $\nu(de,dp)$ in block units. It has support $|p|\le e$ and positive mass in every open low-energy band. For $\epsilon\downarrow0$ remove its part below $2\epsilon$, of mass $q\downarrow0$. Choose $D=\epsilon^{-1}+4(1+|\log q|)^2$ and $e_0=\epsilon/D$. In the first replacement put $q$ at energy $e_0$. In the second put $q e^{-2D}$ at $e_0$ and the remaining $q(1-e^{-2D})$ at $\epsilon$. For **each** replacement energy $e$, assign momentum $p=e[B\Theta_1+(1-B)\Theta_2]$ using a fresh independent split and directions from the law above. All replacement momenta lie in the cone. [G4’s energy-only construction](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/50f6f449fb6e23b8b404d483c04d7ad115e30a99/yang-mills/g4/spatial-block-criticality/correlation-time.md) · [Reference joint measure](../joint-momentum/README.md#the-limiting-joint-measure)

Both completed measures have the same strictly positive spectral bottom $e_0$. Their joint Laplace–Fourier transforms each differ from the reference by at most $2q$ at **all** nonnegative times and spatial arguments, by the total mass removed and replaced. They admit commuting multiplication operators $T=e^{-e}$ and $U(j)=e^{ij\cdot p}$ on the respective excitation spaces, with a vacuum adjoined and a bounded centered observable swapping it with the constant unit excitation. For lattice translations one may reduce $p$ modulo $2\pi$; the replacement momenta are unchanged for small $\epsilon$.

At each of the clocks $s/e_0$, $s\in\{1/2,1\}$, the untouched high-energy contribution is at most $e^{-2sD}$. In the first model the low atom contributes $q e^{-s}$, so the half-time/full-time ratio tends to $e^{1/2}$. In the second the leading term is $q(1-e^{-2D})e^{-sD}$, since $e^{-sD}/q\to0$ and the gap atom costs at most $qe^{-2D}$. Its midpoint ratio is asymptotic to $e^{D/2}$. Yet both tilted models converge at **both clocks** to the same law $F$ for the momentum ratio, even in total variation, because the surviving replacement has exactly that law and the other contributions have vanishing relative weight. The high-energy contribution bound also covers any wrapping of its momenta. This is a discriminator in abstract positive transfer systems. Establishing (C) for Wilson theory requires information about the energy weight at the gap scale that this dimensionless statistic discards.

## Verification

The [exact symbolic checker](check.py) derives the polynomial from Legendre and beta integrals and checks its normalization, endpoint slopes and first two moments of $U$. Direct sampling of 250,000 independent pairs of legs used the polar law $\Theta_3^2\sim\operatorname{Beta}(7/2,2)$ and uniform azimuth. On a 19-point threshold grid the largest CDF discrepancy was 0.00123 overall, and below 0.00266 in each of two disjoint energy bins. Replacing the direction law by a uniform sphere while preserving the same energy distribution gave 0.2111 at threshold one half. Tying both directions made $V=1$ identically.

Two three-generation measured PCP OS runs computed the angular endpoint and the two limiting coefficients using rational arithmetic. The runs emitted identical Lean source. Host Lean checked the three values and the scalar factorization identity, and each run rejected an invalid request and three altered claims. The distributional arguments above are written proofs. [Worker](worker.c) · [Lean read-back](MomentumRatio.lean) · [Replay](verify.py) · [Receipts](receipts.zip)
