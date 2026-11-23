# Spectrum of the bounded magnetic observable

On each slice transport every positively oriented $12$ plaquette to the slice origin along the same ordered spatial path used in the Haar calculation. Write the vector sum of their scaled imaginary parts with coefficients $g_R$ as $X_R(t)$. For fixed $s>0$ use $O_R(t)=\exp(-s|X_R(t)|^2)$. Appending the time trunk from the spacetime origin conjugates the whole slice sum by the same quaternion. Its norm is unchanged, so $O_R$ is a gauge-invariant cylinder on a single time slice. Its spatial diameter is $O(R)$. Denote its connected covariance at lag $n$ in the periodic-limit state by $B_{\beta,R}(n)$.

For one reading use a Fourier variable of law $N(0,2s I_3)$. For two readings use independent such variables, including at coincident times. Their characteristic functions represent $O_R$ and its product, and the amplitude $Y$ in the [Wilson estimate](heat.md) has finite first and second moments. Apply it to the joint test and each marginal. Since their moduli are at most one, subtraction of the product of means gives
$$
 \sup_{n\ge0}|B_{\beta,R}(n)-B_R^G(n)|\le C_s R^4/\sqrt\beta.                 \tag{1}
$$
The superscript denotes three independent centered lattice Gaussian curvatures with one-color covariance the cubical exact-form projection $P$.

## Reference covariance at every time lag

Put $z=Rk\in[-\pi R,\pi R]^3$, $h_i=2\sin(z_i/(2R))$, $S=\sum h_i^2$, $\omega=2\operatorname{arsinh}(\sqrt S/2)$, and define
$$
 \Phi_R(z)=|e^{iz_3}-1|^3\prod_{i=1}^3
       \left|\frac{\sin(z_i/2)}{R\sin(z_i/(2R))}\right|^4,\qquad
 A_R(z)=\frac{R(h_1^2+h_2^2)}{2\sinh\omega}.
$$
Use continuous values at removable singularities. The modulus of the spatial Fourier transform of $g_R$ is $R^2\Phi_R$. The $12,12$ entry of the projection is $(h_1^2+h_2^2)/(S+4\sin^2(k_0/2))$. Taking its time Fourier coefficient gives
$$
 C_R(n)=\int_{[-\pi R,\pi R]^3} |\Phi_R(z)|^2 A_R(z)e^{-n\omega}\frac{d^3z}{(2\pi)^3}.
$$
The time integral follows from the Fourier series of $(\cosh\omega-\cos k_0)^{-1}$. Set $D_R=1+2s C_R(0)$. Gaussian integration for each of three colors gives
$$
 B_R^G(n)=[D_R^2-4s^2 C_R(n)^2]^{-3/2}-D_R^{-3}.
$$
This includes the common-slice variance at $n=0$.

Define $\Phi$ by replacing $R\sin(z_i/(2R))$ with $z_i/2$, and $A=(z_1^2+z_2^2)/(2|z|)$. Let $C(t)$ be the integral on $\mathbb R^3$ with $\Phi,A$ and $e^{-t|z|}$. Define $D=1+2sC(0)$ and $B(t)$ by the same determinant formula. Uniformly for **all** integer lags,
$$
 |B_R^G(n)-B(n/R)|\le C_s R^{-2}.                                           \tag{2}
$$
To see this, put $W(z)=\prod_i\min(1,\pi/|z_i|)^8$. Both squared filters are bounded by $64W$ on the scaled cube. Multiplication of the limiting filter by the bounded factors $[(z_i/(2R))/\sin(z_i/(2R))]^8$ changes its square by at most $C W |z|^2/R^2$. On this cube $R\omega$ is comparable to $|z|$. The sine and inverse-hyperbolic-sine remainders give $|R\omega-|z||\le C|z|^3/R^2$. Likewise $|A_R-A|\le C|z|^3/R^2$ by the numerator error $O(|z|^4/R^2)$ in scaled coordinates and $\sinh\omega=\sqrt S\sqrt{1+S/4}$. Both amplitudes are bounded by $|z|/2$. The supremum over $t\ge0$ of $|e^{-tR\omega}-e^{-t|z|}|$ is at most $C|z|^2/R^2$ by the mean-value theorem. Hence the integrated error is bounded by $CR^{-2}\int |z|^3W(z)\,dz$, including the tail outside the cube where $|z|\ge\pi R$. The determinant map has bounded first partial derivatives for bounded variances $v$ and covariances $0\le x\le v$, since $(1+2sv)^2-4s^2x^2\ge1$. This proves (2) also at zero lag. [B4’s Fourier conventions for the same fourfold filter](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/4e29b71788868f507bbc8abc19d931008138b0f7/yang-mills/transfer-operator/periodic-time/packet-bands/proof.md)

For $s=1$, a separate outward rational integration encloses the continuum difference $B(1)-B(2)$ between **0.000016469 and 0.001335849**. A midpoint evaluation gives about 0.00018063. These numbers concern the Gaussian block profile. The uniform finite-$R$ Wilson argument below uses its own analytic bound. [Outward integration](enclosure.py) · [Mesh comparison](profile_checks.py)

## A positive band at the eighth-root scale

The cube $[1,2]^3$ lies inside the scaled integration domain at every $R\ge1$. There $|\Phi_R|^2\ge(2/\pi)^{30}$, $A_R\ge4/(7\pi^2)$ and $\sqrt3/\pi\le R\omega\le\sqrt{12}$. These follow from $2x/\pi\le\sin x\le x$ on $[0,\pi/2]$, $\sinh\omega=\sqrt S\sqrt{1+S/4}$, and $S\le12$. Thus, with
$$
 g_*=(2/\pi)^{30}\frac{4 e^{-\sqrt{12}}}{7\pi^2(2\pi)^3},
$$
we have $C_R(R)\ge g_*$ and $C_R(R)-C_R(2R)\ge g_*(1-e^{-\sqrt3/\pi})$. For example $C_{\max}=32\int |z|W(z)\,dz/(2\pi)^3$ bounds every variance. Write $D_{\max}=1+2s C_{\max}$. The derivative of the determinant expression in $x^2$ is at least $6s^2D_{\max}^{-5}$. Consequently
$$
 B_R^G(R)-B_R^G(2R)\ge d_*=
 6s^2D_{\max}^{-5}g_*^2(1-e^{-\sqrt3/\pi})>0 .
$$
Choose a fixed $c>0$ with $C_s c^4\le d_*/4$ in (1). Let $R$ be the largest even integer at most $c\beta^{1/8}$ and take $\beta$ large enough for $R\ge2$. Then $B_{\beta,R}(R)-B_{\beta,R}(2R)\ge d_*/2$ uniformly over the periodic-limit states.

The state and transfer operator here are those of the same infinite-time limit at fixed coupling. Site reflection gives the slice vector $\psi=(O_R-\mu O_R)\Omega$ with $\|\psi\|^2=B_{\beta,R}(0)\le1$. The site and adjacent link reflections of the Wilson action give a nonnegative one-step transfer contraction, with $\langle\psi,T^n\psi\rangle=B_{\beta,R}(n)$. In the site reflection inner product the one-step form is the link reflection form on observables translated to lie on one side of that link plane. Finite-cylinder positivity passes to the chosen limit. The lower bound on the operator norm also follows using the even moments alone. Thus $d_*/2\le B_{\beta,R}(R)\le e^{-Rm(\beta,\mu)}$ yields
$$
 \sup_\mu m(\beta,\mu)\le C\beta^{-1/8}
$$
in lattice time steps. [Lüscher, construction of a positive transfer matrix](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf) · [G4’s site reflection on even periodic lattices](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/9)

For the spectral measure of $\psi$ put $E=-\log\lambda$, including $E=+\infty$ when $\lambda=0$. The two-lag difference integrates $e^{-x}(1-e^{-x})$ at $x=RE$. This kernel is at most $1/4$ and at most $\delta=d_*/4$ off $(a,b)=(\delta,-\log\delta)$. It vanishes at both zero and infinity. Therefore the unnormalized mass on $(a/R,b/R)$ is at least $4(d_*/2-\delta)=d_*$, even with multiple fixed vectors.

## Limiting law and the range of its time asymptotic

For $R\to\infty$, $R=o(\beta^{1/8})$, divide by the variance at time zero, which tends to $B(0)>0$. Equations (1) and (2) imply that the normalized laws of $RE$ converge weakly to the probability law with Laplace transform $B(t)/B(0)$. For example push forward by $x=e^{-RE}$ onto $[0,1]$ and take all integer moments, including order zero, at lags $jR$. The moments determine a unique measure by polynomial approximation. The limiting energy law has no mass at infinity, as its Laplace transform is continuous at zero. Define $\sigma$ as the pushforward of $|\Phi|^2 A\,d^3z/(2\pi)^3$ by $z\mapsto |z|$. The unnormalized law equals
$$
 D^{-3}\sum_{j\ge1}\frac{(3/2)_j}{j!}
       (4s^2/D^2)^j\,\sigma^{*2j}.
$$
Here $(3/2)_j$ is the rising factorial. The series converges in mass since $2sC(0)<D$. The first convolution already assigns positive mass arbitrarily close to zero, and all terms have a continuous energy distribution.

At large $t$, $C(t)\sim A_3t^{-10}$ with $A_3=2880/\pi^2$. Substitute $z=y/t$. The squared third-difference filter has leading term $z_3^6$, and the angular integral for $u_3^6(1-u_3^2)$ on the unit sphere is $8\pi/63$. The radial integral is $9!$, and the denominator is $2(2\pi)^3$. The domination follows from $|e^{iz_3}-1|\le |z_3|$ and the unit bound for the limiting sinc factors. Thus $B(t)\sim 6s^2 D^{-5} A_3^2 t^{-20}$. If $t=t_\beta\to\infty$ with
$$
 t^{20}\big(R^4/\sqrt\beta+R^{-2}\big)\longrightarrow0 ,
$$
then exponential tilting of the centered Wilson law at lag $\lfloor tR\rfloor$ yields a limiting Gamma law of shape 20 and rate 1 in energy units $tRE$. Indeed the Laplace transform at $v\ge0$ is the covariance ratio at lags asymptotic to $(1+v)tR$ and $tR$. Monotonicity brackets fractional powers between adjacent integer lags. Both covariances have relative error tending to zero, so the ratio tends to $(1+v)^{-20}$. The bound on $m$ gives $tRm\to0$ in this window. [What the estimates imply at one correlation length](correlation-time.md)
