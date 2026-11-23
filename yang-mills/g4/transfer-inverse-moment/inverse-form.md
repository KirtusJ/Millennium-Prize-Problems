# A uniform inverse transfer moment for local polynomials

Let $P$ be a set of $r$ spatial links and let $f$ be a real, gauge-invariant polynomial supported on $P$, with Peter–Weyl label at most $d_i$ in link $i$. Subtraction of its vacuum mean only changes the constant coefficient. Write $K_1$ for one-link convolution with the probability-Haar density $k(x,y)=e^{\beta\operatorname{Re}(xy^{-1})}/Z_\beta$. Set $k_{\min}=e^{-\beta}/Z_\beta$. The following estimate holds for every exterior volume.

$$
\int_{[0,1]}\lambda^{-1}\,d\nu_{f\Omega}(\lambda)
\le k_{\min}^{-r}\|f\|_\infty^2
\prod_{i=1}^r\left(\sum_{n=0}^\infty
\frac{(n+1)h_n}{\sqrt{h_{n+d_i}}}\right)^2,
\qquad h_n=\frac{I_{n+1}(\beta)}{I_1(\beta)} .
$$

The inverse at zero in this formula is the extended spectral inverse. The argument below proves membership in its form domain. A uniform bound also passes to a weak limit of these measures by lower semicontinuity.

## Removing the magnetic multiplication factors

On the gauge-invariant spatial Hilbert space with product probability Haar measure use $M=e^{-\beta S_{\mathrm{sp}}/2}$, $K=\bigotimes K_1$ and $T=MKM/a_0$, where $a_0$ is the largest eigenvalue of $MKM$. Any scalar plaquette or time-link normalization cancels upon vacuum normalization. The temporal gauge projection is the identity on this space. $K$ and $M$ commute with simultaneous site gauge transformations. The full strictly positive continuous kernel of $MKM$ on the finite product has a normalized positive top vector $\Omega$, invariant by simplicity. Put $b=M\Omega$. Then $Kb=a_0 M^{-1}\Omega$ and $\langle b,Kb\rangle=a_0$. This is Lüscher's electric convolution and spatial potential decomposition. The locality used below is the product in the temporal kinetic factor. Lüscher and Weisz also exploit Wilson locality to factor expectations across time slabs. [Lüscher, §§II–III](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf) · [Lüscher and Weisz, §3](https://arxiv.org/pdf/hep-lat/0108014)

For a positive injective operator $D$, the squared inverse-form norm of $v$ equals $\sup_{g\ne0}|\langle v,g\rangle|^2/\langle g,Dg\rangle$, with infinity allowed. This follows from spectral truncation and Cauchy–Schwarz. Since $M$ is invertible in each finite box, the substitution $h=Mg$ and the equation for $Kb$ yield
$$
\|T^{-1/2}f\Omega\|^2=
\frac{\|K^{-1/2}(f\,Kb)\|^2}{\langle b,Kb\rangle}.
$$
The test vectors can be taken gauge invariant. Equivalently the spectral inverse in the full space preserves the invariant subspace. The proof below bounds the numerator before forming any unbounded inverse.

## Exterior integration

Write $K=K_P\otimes K_O$ for patch and exterior. For each patch input $y$, set $b_y(z)=b(y,z)$ and $\bar b=\int b_y\,dy$. Suppose the patch kernel columns admit
$$
h_y=K_P^{-1/2}\big[f(\cdot)k_P(\cdot,y)\big],\qquad \sup_y\|h_y\|_2\le H .
$$
Construct $W=\int h_y\otimes K_O^{1/2}b_y\,dy$ as a Bochner integral. Strong measurability of $h_y$ follows from the uniform representation expansion below. Integrability follows from $\int\|b_y\|_2\,dy\le\|b\|_2$ and boundedness of $K_O^{1/2}$. Applying $K^{1/2}$ gives $f\,Kb$. Injectivity identifies $W$ with its inverse image. Expanding its squared norm gives
$$
\|W\|^2=\iint\langle h_y,h_{y'}\rangle\langle b_y,K_O b_{y'}\rangle\,dy\,dy'
\le H^2\langle\bar b,K_O\bar b\rangle .
$$
Indeed $b\ge0$ and the integral kernel of $K_O$ is pointwise nonnegative. The Gram factor has absolute value at most $H^2$. In the denominator the same double integral with $k_P(y,y')$ in place of the Gram factor is at least $k_{\min}^r\langle\bar b,K_O\bar b\rangle$. The common factor is strictly positive. This cancellation avoids every exterior-volume factor. The supplied finite-state control tests this step with a nonproduct vacuum amplitude and shows why a signed exterior kernel can invalidate the inequality. [Exact control](control.py)

## Domain of the patch inverse

Label SU(2) irreducibles by $n=2j$ with dimension $n+1$. In the class angle $\theta$, Haar has density $(2/\pi)\sin^2\theta$ and $\chi_n=\sin((n+1)\theta)/\sin\theta$. Character integration gives coefficient $I_n-I_{n+2}=2(n+1)I_{n+1}/\beta$ for the unnormalized one-link Wilson factor. Thus $Z_\beta=2I_1(\beta)/\beta$ and the convolution eigenvalues are $h_n$. They are positive and decrease with $n$. For example $h_1<1$ from the mean normalized fundamental character, and the positive-order Turán inequality makes successive Bessel ratios decrease. No positive uniform lower bound on all $h_n$ is needed. [DLMF, Bessel series](https://dlmf.nist.gov/10.25.E2) · [Baricz and Ponnusamy, inequality (2)](https://arxiv.org/pdf/1010.3346)

At any center $y$, the label-$n$ part of the one-link kernel column has $L^2$ norm $(n+1)h_n$ by character orthogonality and translation. Multiplication by $f$ has norm at most $\|f\|_\infty$ and takes a patch block of labels $(n_i)$ into blocks with labels at most $n_i+d_i$ in coordinate $i$, by the SU(2) tensor product rule. On those finitely many output blocks $K_P^{-1/2}$ has norm at most $\prod_i h_{n_i+d_i}^{-1/2}$. Summing the input-block bounds yields $H\le\|f\|_\infty\prod_i A_{d_i}$, where $A_d$ is the sum in the theorem. [Woit, Theorem 9.1](https://www.math.columbia.edu/~woit/QMbook/qmbook-latest.pdf)

For $x=\beta/2$, the positive series gives $x^j/j!\le I_j(2x)\le e^{x^2}x^j/j!$. Inserting these bounds gives the convenient summand majorant
$$
e^{3x^2/2} x^{-d/2}\,\frac{x^{n/2}\sqrt{(n+d+1)!}}{n!}.
$$
Its successive ratio is $\sqrt{x(n+d+2)}/(n+1)\to0$. Uniform summability in the column centers gives graph-norm convergence by closedness of the inverse square root. For growth in $d$, use $(n+d+1)!\le2^{n+d+1}n!(d+1)!$ and $\sum_n(2x)^{n/2}/\sqrt{n!}\le\sqrt2\,e^{2x}$ by Cauchy–Schwarz. Thus $\log^+ A_d=O_\beta((d+1)\log(d+2))$, locally uniformly for $\beta>0$. At zero coupling the one-link convolution projects onto constants and this argument ceases to apply.
