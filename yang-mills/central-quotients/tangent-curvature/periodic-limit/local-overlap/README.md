# Light-mode overlap at one correlation length in a local Gaussian lattice model

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)  
Research program directed by Kirtus Justus

A fixed bounded observable can have positive spectral weight arbitrarily close to its own threshold and still violate the midpoint bound in condition (C). This example uses a translation-invariant nearest-neighbor Gaussian action on the four-dimensional lattice. The observable is supported at three sites on one time slice. Its underlying magnetic covariance approaches the same free $12,12$ lattice Maxwell kernel used in the Wilson calculations, uniformly over **all space-time separations**.

For two closing lattice masses $0<m<M\to0$ with $D=M/m\to\infty$, let $w\in(0,1)$ be the squared overlap of one fixed field coordinate with the light mode. The full transfer gap is $m$. For a fixed fraction $0<s<1$, the connected reading $C$ obeys
$$
 \limsup \frac{C(s/m)}{C(1/m)}<\infty
 \quad\Longleftrightarrow\quad
 \liminf \frac{w}{D^{3/2} e^{-sD}}>0.
$$
Thus (C) uses $s=1/2$, whereas (C⁺) for this reading holds precisely when $\log(1/w)=o(D)$. The example isolates a missing overlap estimate for a **specified** local probe. The theory also admits other local readings that couple strongly to the light field. No conclusion about (C) for all Wilson observables follows from this example. [Z4’s reduction and the quantifier over observables](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/34f97d20a9e854b58a1c30d89e6b574ad29792f4/yang-mills/z4/attempt/A1_REDUCTION.md) · [G4’s abstract transfer examples](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/50f6f449fb6e23b8b404d483c04d7ad115e30a99/yang-mills/g4/spatial-block-criticality/correlation-time.md)

## A fixed local action form and a fixed probe

Take real scalar doublets $\phi_{i,c}(x)\in\mathbb R^2$ for $i=1,2$, $c=1,2,3$, on $\mathbb Z^4$. Use six independent copies of the quadratic form
$$
 \frac12\sum_x\left(\sum_{a=0}^3|\phi(x+e_a)-\phi(x)|^2+\phi(x)^T A\phi(x)\right).
$$
The positive on-site matrix $A$ has eigenvalues $\mu_m^2,\mu_M^2$, where $\mu_a=2\sinh(a/2)$. Its light eigenvector is $(\sqrt w,\sqrt{1-w})$. Only this on-site matrix changes with the parameter. In the original coordinates set
$$
 F_c=\nabla_1\phi^{(1)}_{2,c}-\nabla_2\phi^{(1)}_{1,c},\qquad
 O=\exp(-\lambda\sum_{c=1}^3 F_c^2),\quad \lambda>0
$$
using forward differences. Both the formula and its support are fixed, and $O$ is even under time reflection and invariant under a common color rotation. The model is a Gaussian scalar theory with a curl reading. The comparison with Wilson theory concerns the covariance of this observable.

Fourier inversion of each diagonal mode gives the one-particle energy
$$
 \omega_a(p)=2\operatorname{arsinh}\big(\sqrt{\mu_a^2+|\widehat p|^2}/2\big),\qquad
 \widehat p_i=2\sin(p_i/2),\qquad p\in[-\pi,\pi]^3 .
$$
The time Fourier coefficient of the scalar covariance is $e^{-n\omega_a}/(2\sinh\omega_a)$ at integer $n\ge0$. This gives reflection positivity directly: the reflected covariance for positive-time tests is an integral of squared Laplace sums against a positive measure. Wick products give positive Gram forms by symmetric tensor powers, and Gaussian polynomials are dense. Time translation acts on the resulting Gaussian chaoses by products of $e^{-\omega_a}$, so the vacuum is unique and the full gap is exactly $m$; one-particle wave packets near $p=0$ approach the infimum. Orthogonal rotation of the two species preserves this construction. For real times use the positive spectral calculus. [Free lattice propagator, Maas, chapter 2](https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/maas_axel/lattice2020.pdf)

Let $G_a(n,z)$ be the same integral with multiplier $e^{ip\cdot z}(\widehat p_1^2+\widehat p_2^2)$ and measure $d^3p/(2\pi)^3$. The one-color covariance of $F$ is $X=wG_m+(1-w)G_M$. Its zero-mass limit $G_0$ is exactly the lattice Maxwell $12,12$ covariance. In four-momentum let $L=\sum_{a=0}^3\widehat k_a^2$ and $N=\widehat k_1^2+\widehat k_2^2$. The difference of massive and massless symbols has magnitude $N\mu_a^2/[L(L+\mu_a^2)]\le\mu_a^2/L$, integrable in four dimensions. Thus $\sup_{n,z}|X-G_0|=O(M^2)$ on integer displacements, uniformly over every choice of $w$. The same bound holds for the connected bounded reading by the determinant formula below. For $1\ll n\ll M^{-1}$ both modes have $n^4G_a(n,0)\to1/\pi^2$, by scaling $p=u/n$ in the positive integral; the dominating radial density is $C|u|e^{-c|u|}$ in three dimensions. Every example therefore has the same pre-correlation-length eighth-power decay for $O$. [Maxwell kernel for A4’s Wilson plaquette comparison](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/1fd502bc5efee86f0f56f8919b51e79a117fcbc9/yang-mills/observable-normalization/transfer-increments/local-action/README.md)

With $V=X(0,0)$, $d_0=1+2\lambda V$, Gaussian integration gives the exact connected reading
$$
 C(n)= [d_0^2-4\lambda^2 X(n,0)^2]^{-3/2}-d_0^{-3}.
$$
At large separation it is $6\lambda^2d_0^{-5}X(n,0)^2[1+O(X(n,0)^2)]$ uniformly here. Every coefficient in the expansion in positive even powers of $X$ is positive. The two-light term has strictly positive mass in $(2m,2m+\delta)$ for every $\delta>0$: the derivative numerator vanishes at the exact minimum, but is positive almost everywhere in each small momentum ball. All terms start at energy at least $2m$. Thus the probe’s own spectral bottom is exactly $2m$ at every parameter, including arbitrarily small positive $w$. In the even field sector the transfer gap is also $2m$.

## The two clock asymptotics

For fixed $s>0$, as $m\to0$, $D\to\infty$, $M=mD\to0$,
$$
 \begin{aligned}
 G_m(s/m,0)&=m^4[g(s)+o(1)],&
 g(s)&=\int_{\mathbb R^3}\frac{u_1^2+u_2^2}{2\sqrt{1+|u|^2}}e^{-s\sqrt{1+|u|^2}}\frac{d^3u}{(2\pi)^3},\\
 G_M(s/m,0)&=m^4 D^{3/2}e^{-sD}[h(s)+o(1)],&
 h(s)&=(2\pi)^{-3/2}s^{-5/2}.
 \end{aligned}
$$
Both errors are relative to the individual mode’s scale, so mixing them with even exponentially small $w$ is legitimate. In the first integral put $p=mu$. The amplitude divided by $m$ is bounded by $C|u|$ and the exponent by $e^{-c_s|u|}$. In the second put $p=m\sqrt D\,u$. The amplitude divided by $m$ tends to $(u_1^2+u_2^2)/2$ and is bounded by $C|u|^2$. The energy difference $(\omega_M-M)/m$ tends to $|u|^2/2$. Indeed $\cosh\omega_M-\cosh M=|\widehat p|^2/2$ exactly; $\sinh r\asymp r$ over the bounded energy range gives $\omega_M-M\asymp |p|^2/(M+|p|)$. After rescaling this bounds the exponential by $\exp[-c_s |u|^2/(1+|u|)]$ once $D\ge1$. Dominated convergence on the expanding cube gives the Gaussian integral $h(s)$. Using the exact lattice threshold $M$ avoids an error in the exponential on very long clocks. Integer times rounded by at most one have the same equivalents since $m,M\to0$ and $\omega$ is bounded. As a cross-check, the continuum one-color integral with mass ratio $d$ is $d^2 K_2(sd)/(2\pi^2s^2)$ by the radial substitution $E=\sqrt{d^2+|u|^2}$. [NIST DLMF 10.32.8](https://dlmf.nist.gov/10.32#E8) · [Large-argument expansion](https://dlmf.nist.gov/10.40#i)

Write $A_s=D^{3/2}e^{-sD}$. At fixed $s$ and 1 the determinant prefactor cancels and the midpoint ratio is asymptotic to
$$
 \left[\frac{w g(s)+(1-w)h(s)A_s}{w g(1)+(1-w)h(1)A_1}\right]^2.
$$
If $w\ge cA_s$ eventually, this ratio is bounded. Conversely $A_1=o(A_s)$, so along any subsequence with $w/A_s\to0$ the denominator is $o(A_s)$ while the numerator is bounded below by a positive multiple of $A_s$. This proves the stated equivalence. For the dyadic assertion apply it to each $s=2^{-j}$. Taking successively smaller $s$ proves necessity of $\log(1/w)=o(D)$, and this condition implies sufficiency separately for every fixed $j$. On a compact parameter prefix one may choose the action coefficients continuous and $w>0$ as in the examples. For a clock defined by the even-sector or probe gap $2m$, substitute $s/2$ and $1/2$ in the ratio; its corresponding overlap threshold is $D^{3/2}e^{-sD/2}$. In particular an arbitrarily small positive coupling to the lowest *accessible* sector still does not ensure (C).

| Light weight $w$ | (C) at the full gap | (C⁺) at the full gap |
|---|---|---|
| $e^{-\sqrt D}$ | Holds | Holds |
| $e^{-D/3}$ | Holds | Fails at the quarter clock |
| $e^{-2D}$ | Fails | Fails |
| $e^{-D/2}$ | Fails by the polynomial prefactor | Fails |
| $D^{3/2}e^{-D/2}$ for large $D$ | Holds at the borderline | Fails |

For $M=\sqrt m$ the first and third rows have the **same masses at every parameter**. Their one-color magnetic covariances differ at most by $C|w_1-w_3|=O(e^{-m^{-1/4}})$ uniformly over lattice displacements, since both component variances are bounded. The determinant, including the possible variance change, has bounded first derivatives on this range, so their bounded local connected readings also agree to every algebraic order in $m$ in absolute error. Their midpoint ratios nevertheless have opposite behavior. This directly tests attempts to infer (C) from locality, threshold support and an algebraically accurate weak-coupling profile alone.

## (C⁺) versus polynomial regularity in gap units

The distinction extends to H3(b) in Z4’s second attempt. For the curl reading and any fixed $K\ge0$ the following two conditions are equivalent, with constants independent of the parameter:
$$
 \frac{C(n)}{C(1/m)}\le C_K(mn)^{-(8+2K)}
 \quad(1\le n\le 1/m,\ n\text{ integer})
 \qquad\Longleftrightarrow\qquad
 w\ge c_K D^{-K}\quad\text{eventually}.
$$
For the forward implication take $n$ nearest $1/M$. Both $G_m(n,0)$ and $G_M(n,0)$ are bounded above and below by positive constants times $M^4$. This follows from the light integral on scale $M$ with mass ratios $1/D$ and 1. Thus $C(n)\asymp M^8$ uniformly in the mix. The unit-clock denominator is at most $C m^8(w+A_1)^2$. The assumed bound forces $w+A_1\ge cD^{-K}$ and $A_1=o(D^{-K})$.

Conversely $G_0(n,0)\le C n^{-4}$ from the positive Fourier integral. For $a=m,M$, splitting the exponential at half time gives $0\le G_a(n,0)\le e^{-na/2}G_0(n/2,0)$. The connected determinant is comparable to $X^2$ over the full bounded covariance range, since its derivative in $X^2$ has positive upper and lower bounds there. The unit-clock denominator is at least $c m^8 w^2$. Put $u=mn$. The normalized ratio is bounded by $C u^{-8}(1+e^{-uD/2}/w)^2$. The condition on $w$ and the bound on $y^Ke^{-y/2}$ yield the claimed $u^{-(8+2K)}$. In particular a weight comparable to $D^{-K}$ gives this optimal time-axis exponent, as the time $n\sim1/M$ attains it.

There is an on-site, hypercubic-scalar control for H3 as well. In the same action take $O_0(x)=\exp[-\lambda\sum_{c=1}^3 (\phi^{(1)}_{1,c}(x))^2]$ and center it. In all scalar covariance integrals the derivative numerator is now 1. The two clock prefactors become $m^2$ and $m^2D^{1/2}e^{-sD}$; the heavy integral after rescaling has limiting constant $s^{-3/2}/[2(2\pi)^{3/2}]$. For the light integral with mass ratio 1 the kernel is bounded by $C e^{-c_s|u|}$ after removal of $m^2$. At mass ratio tending to zero one uses $C|u|^{-1}e^{-c_s|u|}$, also integrable. Consequently (C⁺) again holds for $w=e^{-\sqrt D}$. At $n\sim1/M$ the unnormalized connected covariance is comparable to $M^4$, while at $1/m$ it is comparable to $m^4w^2$. Their ratio grows as $D^4e^{2\sqrt D}$ up to fixed multiplicative constants. At physical separation $mn\sim1/D$ this violates **every polynomial two-point bound**. Rounding the unit normalization clock to the nearest even separation does not affect this conclusion. The same upper/lower argument as above gives threshold $w\gtrsim D^{-K}$ for the temporal envelope of exponent $4+2K$ in this on-site case.

Thus even for a bounded hypercubic site scalar in an exactly local, reflection-positive Gaussian action, controlling each fixed dyadic clock does not supply H3(b). The counterexample concerns the specified normalized field. It leaves open how to select a Wilson family satisfying all hypotheses of Theorem S. [Z4’s H3(b) and its implication for (C⁺)](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/5b58bcd4035aa94d639404e78dbe47276d211040/yang-mills/z4/attempt/reviews/c1-OS/THEOREM_S.md)

## Reproduction

The [numerical check](check.py) integrates the time-exact lattice kernel at both mass scales, avoiding subtraction of nearly equal energies. At $D=256$, $m=D^{-2}$, the scaled log half-clock ratio of the squared covariance is 1.0136 for $w=e^{-2D}$, consistent with the limiting slope 1. For $w=e^{-D/3}$ the corresponding half- and quarter-clock readings are 0.0228 and 0.2569 in scaled log units, with limiting slopes 0 and $1/6$. The large-$D$ polynomial correction is retained in the proof and the quadrature. The numerical controls also compare two quadrature orders and the continuum Bessel formula. An independent on-site calculation at $D=1024$ recovered the predicted log short-time ratio within $0.000003$. Two three-generation PCP OS deployments returned identical supporting Lean source. An initial run exposed a missing real-number import before the two verified replays. [Worker](worker.c) · [Lean source](LocalOverlap.lean) · [Verifier](verify.py) · [Receipts](receipts.zip)
