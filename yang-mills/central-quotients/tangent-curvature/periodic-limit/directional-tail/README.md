# Large momentum in the plane and normal to a magnetic packet

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)  
Research program directed by Kirtus Justus

For the centered fourfold magnetic packet of B4 and G4, let $\rho$ be its **unnormalized, untilted** joint spectral measure. Use $P=Rk$ with the componentwise representative of lattice momentum and $e=RE$ for lattice energy in block units. The packet tests curvature in the 12-plane. Its large-momentum directions and even the tail exponent depend on that plane.

Write $v$ for its continuum-block one-color variance and $s>0$ for the parameter in $O_R=\exp(-s|X_R|^2)$. Set $L_s=12s^2v/(1+4sv)^{5/2}$, $a=25217/(1620\pi)$ and $b=43186/(315\pi)$. For even-periodic thermodynamic limits of the four-dimensional isotropic $SU(2)$ Wilson theory, let $H\to\infty$, $R\to\infty$, $H/R\to0$.

* If $H^6R^{7/2}/\sqrt\beta\to0$, then $H^6\rho(\|P\|_\infty>H)\to L_s a$. Conditional on this event, $(e/H,P/H)$ converges to $(Y,YJ)$, where $\Pr(Y>y)=y^{-6}$ for $y\ge1$ and $J$ is independent and uniform on $\{+e_1,-e_1,+e_2,-e_2\}$.
* If $H^8R^{7/2}/\sqrt\beta\to0$, then $H^8\rho(|P_3|>H)\to L_s b$. For every $H\ge4\pi$ and integer $R\ge2$, the normal-component weight already obeys $\rho(|P_3|\ge H)\le C_s(H^{-8}+R^{7/2}/\sqrt\beta)$.

The same constants and conditional law hold for the limiting free block measure as $H\to\infty$. The finite-coupling statements allow the threshold and radius to grow together, uniformly in the state selection. For example $R=\lfloor\beta^{1/12}\rfloor$ and $H=\beta^{1/50}$ satisfy both conditions. The extreme momenta have order $H/R$ in lattice units. The null directions describe the spectral weight of this selected packet on that scale. These estimates leave physical mass and the spectrum at one correlation length open. [G4’s momentum-tail estimate](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/0666174e3718168eb0dc7b7b2f42af9076559a08/yang-mills/g4/momentum-tail/README.md) · [A4’s Wilson comparison](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/e2e56f57f9950af5e32a60b8486e1bb3587e34ca/yang-mills/observable-normalization/transfer-increments/spatial-packet/strip/rectangles.md)

## One curvature

Put $b_0(x)=(2\sin(x/2)/x)^8$ and $d(x)=|2\sin(x/2)|^6$. The one-color continuum momentum measure has density
$$
 W(dp)=\frac{p_1^2+p_2^2}{2|p|(2\pi)^3}\,b_0(p_1)b_0(p_2)b_0(p_3)d(p_3)\,dp.
$$
In the finite Gaussian lattice measure $W_R$, replace each denominator $p_i$ in the box factor with $h_i=2R\sin(p_i/(2R))$, replace the projection amplitude by $(h_1^2+h_2^2)/(2|h|\sqrt{1+|h|^2/(4R^2)})$, and restrict to $[-\pi R,\pi R)^3$. The one-leg energy in block units is $2R\operatorname{arsinh}(|h|/(2R))$. On this cube $|h|\asymp|p|$. The density is bounded both by $C|p|\prod(1+|p_i|)^{-8}$ and by $C(p_1^2+p_2^2)|p_3|^{-1}\prod(1+|p_i|)^{-8}$ when $p_3\ne0$. Hence the one-leg tails at $H\ge1$ are bounded by $CH^{-6}$ for the maximum and $CH^{-8}$ for the normal component. The variance $v_R=W_R(\mathbb R^3)$ tends to $v>0$. [Fourier computation and energy symbol](../fourier-decay/README.md)

For large positive $x=p_1$ and bounded transverse coordinates, the continuum amplitude divided by $x$ tends to $1/2$. The tail integrand along that axis is proportional to $x^{-7}|2\sin(x/2)|^8$. The periodic factor has average $\binom84=70$. For $x=p_3>0$ the amplitude times $x$ tends to $(p_1^2+p_2^2)/2$. Now the longitudinal integrand is proportional to $x^{-9}|2\sin(x/2)|^{14}$ with period average $\binom{14}7=3432$. Rescaling $x=Hy$ averages these periodic factors against any continuous test on a compact positive interval of $y$, by partition into periods. A bounded primitive of the centered factor gives the same conclusion by integration by parts for smooth tests.

These calculations also apply to $W_R$ for $H=o(R)$. On $H\le x\le MH$ with bounded transverse coordinates, all finite-lattice denominator corrections tend uniformly to one; on this region energy divided by $H$ differs from $x/H$ by $o(1)$. The part $x>MH$ costs $O((MH)^{-6})$ or $O((MH)^{-8})$ as appropriate. Transverse truncation is uniform after multiplication by $H^6$ or $H^8$: for the first axis use $|p|\le |x|+|p_2|+|p_3|$ against the product majorant. For the third use the second majorant and the finite second moments of the transverse box factors. Taking the transverse cutoff to infinity makes the discarded normalized mass tend to zero. This also shows that simultaneous large first and second components are negligible on the sixth-power scale. Thus the four signed in-plane axes share the leading maximum-norm mass equally and the scaled radius there has density proportional to $y^{-7}dy$.

For the constants let $I_0=\int b_0$, $I_d=\int b_0d$, $I_2=\int x^2 b_0(x)\,dx$. The centered eightfold unit-box convolution $S$ has Fourier transform $b_0$. Explicitly $S(u)=\sum_{j=0}^8(-1)^j\binom8j(u+4-j)_+^7/7!$, obtained by convolving indicators or inclusion-exclusion on the eight-dimensional unit cube. Fourier inversion and expansion of $d$ yield
$$
 I_0/(2\pi)=S(0)=151/315,\quad
 I_d/(2\pi)=\sum_{k=-3}^3(-1)^k\binom6{3+k}S(k)=167/60,\quad
 I_2/(2\pi)=-S''(0)=2/3 .
$$
Each signed in-plane axis has coefficient $70 I_0 I_d/[12(2\pi)^3]=a/4$. Both signs of the normal component together give $3432 I_0 I_2/[4(2\pi)^3]=b$. These constants use the unnormalized $W$.

## Summing the packet spectrum

At order $j\ge1$ add $N=2j$ independent one-leg draws from $W_R/v_R$ and their energies, folding the total spatial momentum modulo $2\pi R$ on each axis. The unnormalized mixture weight is
$$
 w_{j,R}=D_R^{-3}(3/2)_j (2s v_R/D_R)^{2j}/j!,\qquad D_R=1+2sv_R .
$$
The term of order zero cancels upon centering. G4’s wrapping step holds because the absolute value of the centered representative cannot exceed that of its unwrapped preimage. The probability that folding changes any coordinate is $O_N(R^{-6})$; for the normal coordinate alone it is $O_N(R^{-8})$, by a union bound on legs larger than $\pi R/N$ in the relevant norm. These errors disappear after the respective rescalings.

For fixed $N$ and $\delta>0$, two or more legs exceeding $\delta H$ in the relevant norm cost $O_{N,\delta}(H^{-2\alpha})$, with $\alpha=6$ or 8. If the sum exceeds $H$, at least one leg exceeds $H/N$. Apart from this negligible multiple-exceedance event, the other legs change the sum by at most $N\delta H$. In the maximum-norm calculation they change the energy by at most $\sqrt3 N\delta H$ as well. Squeeze between thresholds $1\pm N\delta$ after rescaling and take $\delta\downarrow0$. The one-leg radial tail is continuous. This proves the one-leg tail equivalent multiplied by $N/v_R$ when expressed relative to the unnormalized leg measure, with the same joint rays for the maximum-norm event. For normal-only tails use scalar absolute components in this argument. No energy conclusion conditional on a normal-only extreme is needed.

The uniform tail bound for the $N$-leg probability is $C N^{\alpha+1}H^{-\alpha}$, also for $N>H$ by enlarging the constant. The weights decay geometrically up to a fixed polynomial uniformly in $R$, so summation commutes with the limit. The factor multiplying the unnormalized leg constants is
$$
 \sum_{j\ge1}\frac{2j}{v}w_j
 =\frac{12s^2v}{(1+4sv)^{5/2}} .
$$
This follows by differentiating the power series $(1-z)^{-3/2}$ in $z=(2sv/(1+2sv))^2$, keeping its outside prefactor fixed. The fixed-order decomposition proves the required rare-event estimate directly for this signed-vector sum and its associated energies. [General scalar random-sum asymptotics, Denisov, Foss & Korshunov](https://arxiv.org/abs/0808.3697)

## Transferring the rare event to Wilson states

First adapt G4’s cutoff to the normal coordinate. Let $F_M(k)=|M^{-1}\sum_{j=0}^{M-1}e^{ijk}|^2$ and take $(1-F_M)^5$. Its Fourier coefficients have total absolute sum at most 32 and use shifts of length at most $5(M-1)$. For $4\pi\le H\le\pi R$ take $M=\lceil2\pi R/H\rceil\le R$. On $|Rk_3|\ge H$ the polynomial is at least $(3/4)^5$. Everywhere it is bounded by $C\min(1,|Mk_3|^{10})$. The free normal marginal has tail $C(1+u)^{-8}$ as proved above. Layer cake bounds the cutoff integral by $C(M/R)^8$, since $\int_1^A u^9u^{-8}\,du=O(A^2)$. Comparing the polynomial using A4’s uniform covariance estimate for true translates of length at most $5R$ adds $C_s R^{7/2}/\sqrt\beta$. For $H>\pi R$ the event is empty. This proves the all-threshold upper estimate. G4’s fourth-power cutoff gives the corresponding sixth-power bound for the maximum norm. Both comparisons include the zero-time mass, including a possible transfer nullspace. [G4’s finite Fourier test](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/0666174e3718168eb0dc7b7b2f42af9076559a08/yang-mills/g4/momentum-tail/README.md#a-finite-fourier-test-for-the-interacting-tail)

For sharp constants choose a smooth compactly supported test $g(P/H)$ away from zero, in dimension $d=3$ for the full momentum or $d=1$ for the normal marginal. Put $A=R/H\to\infty$. On the representative cube this test equals its $2\pi A$-periodization for all sufficiently large $A$. Its Fourier coefficients are $(2\pi A)^{-d}\widehat g(z/A)$ on integer spatial shifts $z$. Their total absolute sum is uniformly bounded. For $|z|_1>R$ the absolute tail is $O_{g,K}(H^{-K})$ for every fixed $K$, by rapid decrease and a lattice shell sum with spacing $1/A$. Both spectral measures have bounded total mass. On the retained shifts $|z|_1\le R$, the true-translate Wilson estimate therefore transfers the test with total error $O_g(R^{7/2}/\sqrt\beta)+O_{g,K}(H^{-K})$. This is $o(H^{-\alpha})$ under the respective hypothesis. The reasoning works at every integer time lag, using the time-uniform version of A4’s comparison. [Rectangular swaps and true translates](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/e2e56f57f9950af5e32a60b8486e1bb3587e34ca/yang-mills/observable-normalization/transfer-increments/spatial-packet/strip/rectangles.md) · [Periodization on the expanding cube](../joint-momentum/README.md#why-scaled-momentum-does-not-fold)

In the joint case use lags $m\lfloor A\rfloor$, $m=0,1,\ldots$, to test polynomial moments in $x=\exp(-\lfloor A\rfloor E)\in[0,1]$. This gives convergence of the rescaled measures on compact spatial annuli with compactified energy, by polynomial and smooth approximation; the positive mass on each such annulus is uniformly bounded after rescaling by the tail estimates. The limiting free radial density charges no threshold spheres for the maximum norm. For the normal marginal it charges no threshold points. Smooth upper and lower cutoffs can thus recover the sharp event on a bounded annulus. The portions beyond $MH$ have rescaled Wilson mass at most $C_s M^{-\alpha}+o(1)$ by the tail bound. Taking $M\to\infty$ proves the sharp mass limits. In the joint case the limit has no atom at $x=0$ and $\lfloor A\rfloor/A\to1$, giving the stated conditional distribution in $e/H=AE$. This proof controls relative tail weights because the comparison error is smaller than the weight being measured.

## Independent checks

At G4’s pinned PR head the original checker reproduced 15,625 signed path pairs, 42 finite Fourier tests and 2,960 wrapped convolution cases. Host Lean 4.19.0 also checked the four original declarations. Two further deployments each ran three linked native PCP OS workers for the exact spline mass, the four-ray coefficient and the normal coefficient. The host checked the emitted Lean source and rejected the three altered coefficients. Independent finite and continuum quadratures integrate one long coordinate and two transverse coordinates; they test the constants on finite slabs. The rare-event limits and transfer are proved above. [Numerical check](check.py) · [Native source](worker.c) · [Lean read-back](DirectionalTail.lean) · [Verifier](verify.py) · [Receipts](receipts.zip)
