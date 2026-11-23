# A four-dimensional Wilson box with exponentially small vacuum probability

Take B4’s periodic three-dimensional spatial SU(2) lattice, fixed spatial spacing, even side $L\ge4$ and $V=L^3$. Use $\kappa>0$, $0\le\kappa\lambda\le1/384$, $n\ge4$, time spacing $a=\kappa/(4n)$, temporal coupling $\beta_t=4n$ and spatial coupling $a\lambda$. The full period of $2n$ fine steps has physical duration $\tau=\kappa/2$. Positive $\lambda$ includes the spatial magnetic interaction. The spatial volume and time resolution may increase together. [B4’s regulator, normalization and uniform physical gap](../../transfer-operator/blocked-time/README.md)

## Bounding the thermal vacuum weight

On the gauge-invariant Hilbert space let $K$ be the independent product of normalized electric link convolutions. The full transfer is $T=MKM$ with $M=\exp(-aW/2)$ and $W=\lambda\sum_p(1-\operatorname{ReTr}(U_p)/2)$. There are $3V$ spatial faces and every deficit belongs to $[0,2]$. Hence $e^{-3a\lambda V}\le M\le1$, $\lambda_1(T)\le1$, and
$$
 \lambda_i(T)=\sigma_i(K^{1/2}M)^2\ \ge\ e^{-6a\lambda V}\lambda_i(K).
$$
Indeed, $K^{1/2}=(K^{1/2}M)M^{-1}$ and right multiplication increases each singular value by at most $\|M^{-1}\|$. This argument works with the noncommuting magnetic and electric factors.

In each $xy$ layer take the elementary faces with both lower coordinates even. These $V/4$ faces have disjoint link sets. For any subset $S$ their product of unnormalized fundamental characters is gauge invariant. Different subsets are orthogonal in product Haar measure, since each selected face holonomy is independent Haar, the character has mean zero and its squared norm is one. Convolution on any participating link multiplies each fundamental matrix element, including an inverse-link element, by $r=I_2(4n)/I_1(4n)$. The resulting eigenvalues of $K$ are $r^{4|S|}$. The binomial sum in the physical trace and the singular-value comparison give
$$
 \rho_1(T)=\frac{\lambda_1(T)^{2n}}{\operatorname{Tr}_{\rm phys}T^{2n}}
 \le\frac{\exp(6\tau\lambda V)}{(1+r^{8n})^{V/4}}.
$$

For the single-link tilted Haar law, $r$ is the mean of $x=\operatorname{ReTr}(U)/2$. The density of $y=1-x$ is proportional to $e^{-4ny}y^{1/2}(2-y)^{1/2}$ on $[0,2]$. This is a Gamma law of shape $3/2$ and rate $4n$ tilted by the nonincreasing function $\sqrt{(2-y)_+}$. Oppositely monotone functions have nonpositive covariance, so $\mathbb Ey\le3/(8n)$. Thus $r^{8n}\ge(1-3/(8n))^{8n}\ge(29/32)^{32}>1/24$. The middle bound uses monotonicity of $(1-c/x)^x$ for $x>c$, from $u-\log(1+u)\ge0$ with $u=c/(x-c)$. Finally $\log(25/24)\ge1/25$, $6\tau\lambda\le1/128$, and $1/100-1/128=7/3200$. This proves $\rho_1(T)\le e^{-7V/3200}$ without assuming a lower bound on the gap.

## What a complete slice measurement would certify

B4 proves $E_1-E_0\ge4\log(3)/(13\kappa)$ on these same finite regulators. Therefore the exact **half-period** ratio is $s_2/s_1\le3^{-1/13}<23/25$. For an orbit partition with $\beta_t\delta\le1/10$, use $h_0=199/200$, $d_0=1/200$ and $a_0=1/20$ in the uniform bound. Let $\eta=1/1000$ bound the root-table operator error relative to the measured norm. The exact raw singular ratio satisfies $\sigma_2(B)/b\le s_2/s_1+d_0$ by the lower compression inequality. Hence the measured ratio is at most $(1+\eta)(23/25+d_0)+\eta$. Propagating the measurement uncertainty back through the upper bound gives
$$
 \frac{\bigl(((1+\eta)(23/25+d_0)+2\eta)/(1-\eta)+d_0\bigr)^2+2a_0^2}{h_0^2}
 =\frac{35013189256}{39521837601}<\frac9{10}.
$$
This bounds the worst certificate from the ideal measured singular ratio at these tolerances. Rational computation can approach the displayed bound to arbitrarily small rounding error. There is strict slack below $9/10$. The certified physical floor is $2\log(10/9)/\kappa$, even along sequences with $\rho_1\to0$. B4’s stronger physical floor is the independent calibration input here. A new trajectory with no prior gap bound would be tested using its own measured table and error allowance. [B4’s full-spectrum proof](../../transfer-operator/blocked-time/README.md) · [Rational checks](controls.py)

One explicit finite protocol fixes a spanning tree. Representatives have $k=2V+1$ remaining SU(2) links modulo simultaneous conjugation. Partition $[-1,1]^4$ into $m$ intervals per coordinate, restricting the cubes to the unit quaternions. Pick one point from each nonempty cell. The fundamental operator chord equals Euclidean distance of the unit quaternions, so the product net has covering radius at most $4k/m$ in total chord and at most $m^{4k}$ points. Passing the centers to the gauge quotient cannot increase this radius. Assign each orbit to a closest center with a fixed rule for ties. Its cell then has diameter at most $8k/m$. Taking $m\ge80k\beta_t$ ensures the required geometry. Independently sample full periodic histories until a deterministic sample size $S$ obeys
$$
 D[D^2\log(S+1)+\log(1/\alpha)]/S\le10^{-6}.
$$
Here $D$ is the number of cells or a known upper bound. Then the relative error is at most $10^{-3}$ with probability at least $1-\alpha$. A sufficiently accurate numerical singular-value enclosure must also leave room below the threshold. The number of cells in this construction grows rapidly. No four-dimensional histogram was acquired in this study. The sampling protocol assumes independent equilibrium draws and supplies no mixing estimate for a simulation. [Sampling bound](compression.md)

The spatial mesh stays fixed in this proof. B4’s fixed-mesh physical gap, the thermal trace estimate, and the threshold margin do not provide a trajectory with uniform physical estimates as the spatial mesh vanishes. Z4’s frozen rows contain scalar measurements and cannot be retrofitted to this full-orbit protocol. [B4’s spatial-refinement analysis](../../transfer-operator/blocked-time/local-limit.md) · [B4’s corrected measurement disposition](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7100771694)
