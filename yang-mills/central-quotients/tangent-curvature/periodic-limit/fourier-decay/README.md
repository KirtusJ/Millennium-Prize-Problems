# The magnetic packet at a growing tilt time

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)  
Research program directed by Kirtus Justus

G4’s uniform Fourier estimate at `50f6f44` passes independent review. Keeping the zero of the magnetic filter in that estimate yields two further conclusions for the same fourfold spatial packet in four-dimensional SU(2) Wilson theory. At each fixed β take any thermodynamic limit of even periodic cubes. Write R ≥ 1 for the integer packet radius, n for an integer lag and t=n/R. Exponentially tilt the **centered** packet’s joint spectral measure by exp(−nE) and divide by its total after tilting. Along sequences with β and t tending to infinity, uniformly in the eligible states:

* If $t^{20}R^4/\sqrt\beta\to0$, the marginal law of $nE$ tends to Gamma(shape 20, rate 1). This includes fixed R.
* If $t^{21}R^4/\sqrt\beta\to0$, the joint law of $(nE,nk)$ tends to the sum of two independent vectors $(H,H\Theta)$, with $H$ of Gamma(shape 10, rate 1), independent of the direction $\Theta$. Relative to sphere area, the direction has density $63\theta_3^6(1-\theta_3^2)/(8\pi)$. Here k uses the representative in $[-\pi,\pi)^3$.

These scales satisfy $nm\to0$ by the eighth-root lattice gap upper bound. The result describes the selected magnetic reading before one correlation length. A positive fixed-coupling gap and the continuum mass-gap problem remain open. [G4’s requested comparison](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/50f6f449fb6e23b8b404d483c04d7ad115e30a99/yang-mills/g4/spatial-block-criticality/spectrum.md) · [B4’s packet](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/4e29b71788868f507bbc8abc19d931008138b0f7/yang-mills/transfer-operator/periodic-time/packet-bands/proof.md)

## Discrete Fourier comparison

Use G4's scaled momentum variable p and abbreviate $r=|p|$, $a_R=R\omega(p/R)$. Write $C_R(n,j)$ for the one-color free lattice covariance at spatial displacement $j\in\mathbb Z^3$ and $C(t,y)$ for the continuum reference, with $y=j/R$. Both integrals include the phase $e^{iy\cdot p}$. On the cube $[-\pi R,\pi R]^3$, $c r\le a_R\le r$ with an absolute $c>0$ by the chord bound for sine and the positive minimum of $\operatorname{arsinh}(u)/u$ on $[0,\sqrt{3}]$. Taylor remainders on these compact rescaled arguments give
$$
 |a_R-r|+|A_R-A|\le C r^3/R^2,\qquad
 |e^{-t a_R}-e^{-tr}|\le C R^{-2} t r^3 e^{-ctr}.
$$
Here $A=(p_1^2+p_2^2)/(2r)$ and $A_R$ is its lattice counterpart from G4. For the amplitude bound, set $h_i=2R\sin(p_i/(2R))$. Then $|h-p|\le Cr^3/R^2$, $|h|\asymp r$, and $A_R=(h_1^2+h_2^2)/(2|h|\sqrt{1+|h|^2/(4R^2)})$. Both amplitudes are at most $r/2$. Define $W=\prod_i\min(1,\pi/|p_i|)^8$. The squared filters are bounded by $64W$ on the cube. Their difference is at most $CW r^2/R^2$, since each bounded ratio $(u/\sin u)^8$ differs from one by at most $Cu^2$ there. Outside the cube the limiting filter still obeys $64W$ and $1\le r^2/(\pi R)^2$. Finally $\sup_{t\ge0} tr\exp(-ctr)<\infty$ and $\int r^3W\,dp<\infty$ by the one-coordinate moments. This verifies the all-time $O(R^{-2})$ comparison, including the discarded tail at zero lag.

For $t\ge1$ retain the factor $|e^{ip_3}-1|^6\le r^6$. Both squared filters are now bounded by $Cr^6$ and their difference on the cube by $Cr^8/R^2$. After including the amplitudes, the error integrand is dominated by
$$
 C R^{-2}(r^9+t r^{10})e^{-ctr}.
$$
The discarded continuum integrand is bounded by $C R^{-2}r^9 e^{-tr}$ using the same exterior inequality. Spherical integration yields the stronger uniform estimate
$$
 \sup_j |C_R(n,j)-C(t,j/R)|\le C R^{-2}(1+t)^{-12}.
$$
The phase has modulus one even when the displacement grows with the lag. In the continuum integral the squared filter differs from $p_3^6$ by at most $Cr^8$, by Taylor expansion at the origin and polynomial domination for $r\ge1$. At $y=0$ it follows that $C(t,0)=A_3 t^{-10}+O(t^{-12})$, $A_3=2880/\pi^2$. Indeed the radial integral is $9!$ and the angular integral is $8\pi/63$, with prefactor $1/[2(2\pi)^3]$. The Laplace endpoint expansion here has an explicit integrable remainder. [NIST DLMF §2.3(ii)](https://dlmf.nist.gov/2.3#ii)

## Tilted energy

Keep the exact equal-time factor $D_R=1+2sC_R(0,0)$ for the fixed reading parameter $s>0$. It lies in a compact subset of $[1,\infty)$ independently of R. By expansion of the Gaussian determinant around zero covariance, the centered free reading at zero displacement has the asymptotic
$$
 B_R^G(n,0)=6s^2D_R^{-5} A_3^2 t^{-20}\,[1+O_s(t^{-2})].
$$
The leading coefficient is bounded above and bounded away from zero. The error is uniform over integer $R\ge1$. G4’s interacting comparison contributes an absolute $O_s(R^4/\sqrt\beta)$. Under the first stated condition this is $o(t^{-20})$. At each integer $l\ge0$, the ratio of readings at lags $(l+1)n$ and $n$ tends to $(l+1)^{-20}$. The factor $D_R^{-5}$ cancels for every R. These are all the moments of $x=e^{-nE}$ under the tilted measure. Polynomials are dense on $[0,1]$ and the specified gamma law pushes forward to those moments with no mass at zero. This proves the marginal limit, including when R stays fixed. For example $R=2$ and $t$ of order $\beta^{1/50}$ satisfy the new condition although $t^{20}/R^2$ diverges. [G4’s Wilson comparison](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/50f6f449fb6e23b8b404d483c04d7ad115e30a99/yang-mills/g4/spatial-block-criticality/heat.md)

## Tilted momentum

For actual translates of the packet the interacting comparison in absolute covariance is at most $C_s(1+|j|_1/R)R^4/\sqrt\beta$, independent of lag. The linear dependence used here follows directly from the original-link estimates. In B4’s weighted heat sum each translate adds $|j|_1$ times the **unweighted** primitive norm, at most $CR^3Y$ (sum the short bound $R^2N^{-1/2}$ to $N=R^2$ and long bound $R^5N^{-2}$ thereafter, for Fourier amplitude $Y$). The primitive sup norm is at most $CY$. Thus each spatial path adds at most $|j|_1$ to its length, with total face coefficient norm at most $CR^2Y$. The incident derivative uses the same weighted heat sum times the unshifted test sup bound. The time trunk costs zero. Changing the root of the translated reading costs at most $C|j|_1R^3/\sqrt\beta$ by signed spatial face swaps. Integration over the two Gaussian Fourier variables absorbs the powers of $Y$. Together these bounds give the claimed linear dependence. [Original-link estimates](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/4e29b71788868f507bbc8abc19d931008138b0f7/yang-mills/transfer-operator/periodic-time/packet-bands/proof.md) · [Change of spatial root](../joint-momentum/README.md)

Fix $l\ge0$ integral and $|j|_1\le Ln$. In the continuum covariance substitute $p=q/t$. Uniformly on this range the scalar covariance at $((l+1)t,j/R)$ multiplied by $t^{10}$ differs by $O(t^{-2})$ from
$$
 J_l(j/n)=\int e^{-(l+1)|q|+i(j/n)\cdot q}\,q_3^6\,
       \frac{q_1^2+q_2^2}{2|q|}\,\frac{d^3q}{(2\pi)^3}.
$$
The bound follows from the $Cr^8$ remainder regardless of the phase. The free lattice comparison above preserves this error. The determinant expansion holds uniformly for signed scalar covariances as well. Its normalized leading term is $J_l(j/n)^2/A_3^2$ after division by the zero-displacement reading at lag n. Under the second stated condition the Wilson error on this bounded range of $j/n$ is $o(t^{-20})$. The normalized mixed transforms therefore differ from $J_l(j/n)^2/A_3^2$ by $o(1)$ uniformly there.

The measure with transform $J_l(y)/A_3$ in the variables $e^{-lH+i y\cdot H\Theta}$ is the one-leg probability stated above, by spherical integration. Squaring the transform gives the sum of two independent legs. To identify the actual momentum on the expanding representative cube, periodize any smooth compactly supported $g$ on $[-\pi n,\pi n)^3$. Its exact Fourier coefficients are $(2\pi n)^{-3}\widehat g(j/n)$. Pair this series with $x^l$ under the tilted measure. Every normalized mixed transform has absolute value at most one by the joint spectral representation and the positive tilt. Rapid decay makes the tail $|j|_1>Ln$ uniformly negligible when L grows. On the compact range the established bound and the Riemann sums give convergence to the stated law for $x^l g$. Such tests determine vague convergence on $[0,1]\times\mathbb R^3$. All measures, including the limit, have total mass one, giving tightness and weak convergence. The limit assigns zero mass to $x=0$. Transforming back gives the assertion for $nE$ and the unfolded three-dimensional momentum $nk$. [Fourier periodization and the momentum representative](../joint-momentum/README.md#why-scaled-momentum-does-not-fold)

## Computational checks

The radial coefficient, the ratio $11!/9!$, and a family of exponent comparisons were checked in a three-generation PCP OS deployment and read back in Lean. A separate quadrature uses the variables $tp$ and tests the predicted error order at zero and off-axis displacement. These are finite supporting checks. The estimates above supply the proof. [Native source](worker.c) · [Lean read-back](FourierDecay.lean) · [Replay](verify.py) · [Quadrature](check.py) · [Receipts](receipts.zip)
