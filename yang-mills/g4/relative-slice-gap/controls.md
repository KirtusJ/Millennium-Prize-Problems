# Two-dimensional Wilson refinement and a gapless physical clock

## An SU(2) cylinder at fixed area

Use a spatial circle with $J\ge3$ links, $a_s=a_t=1/J$, $n=J$, period $\tau=2$ and $g^2=8$. Take $\beta=4/(g^2a_sa_t)=J^2/2$. The full spatial gauge orbit is specified by the conjugacy angle $\theta\in[0,\pi]$ of the total holonomy. The pushforward of Haar is $2\sin^2\theta\,d\theta/\pi$. Its orthonormal characters are $\chi_d(\theta)=\sin(d\theta)/\sin\theta$ indexed by dimension $d\ge1$. Each of the $J$ temporal plaquette convolutions acts on the representing matrix of a link by the scalar $I_d(\beta)/I_1(\beta)$, from the Weyl integral and the Bessel recurrence. Tracing the product around the circle gives a full slice eigenfunction. Thus the vacuum-normalized half-period kernel on conjugacy angles is
$$
 K(\theta,\varphi)=\sum_{d\ge1} R_d\chi_d(\theta)\chi_d(\varphi),\qquad
 R_d=\bigl[I_d(\beta)/I_1(\beta)\bigr]^{J^2}.
$$
The joint opposite-angle density is $K^2/\sum R_d^2$. These are complete spatial configurations on this cylinder. The circle and area fix the normalization of energies. [Ashtekar et al., Wilson continuum theory on the cylinder](https://arxiv.org/abs/hep-th/9605128) · [Dang and Nohra, §§7–8, two-dimensional Wilson scaling](https://arxiv.org/html/2602.08591v2)

For fixed $d$, the large-argument expansion gives $\log(I_d/I_1)=-(d^2-1)/(2\beta)+O_d(\beta^{-2})$. Hence $R_d\to e^{-(d^2-1)}$. For the uniform tail, the consecutive ratio $b_j=I_{j+1}(\beta)/I_j(\beta)$ is the mean of $x$ with density proportional to $e^{\beta x}(1-x^2)^{j-1/2}$ on $[-1,1]$. Integration by parts gives $(2j+1)b_j=\beta\mathbb E(1-x^2)\le 2\beta(1-b_j)$. Since $j\ge1$, $\beta\ge4$, and $(1+c/\beta)^\beta$ increases in $\beta$, each $b_j^{J^2}\le q=(8/11)^8$. Thus $R_d\le q^{d-1}$. The same geometric bound holds in the limit. [DLMF 10.40.1](https://dlmf.nist.gov/10.40) · [B4’s ratio bound](../../transfer-operator/blocked-time/README.md)

The character is a sum of $d$ exponentials with frequencies at most $d-1$, so $|\chi_d|\le d$ and $|\chi_d'|\le d(d-1)$. The geometric sums give
$$
 K\ge m=2-\frac{1+q}{(1-q)^3}>0,\qquad
 |\partial_\theta K|\le A=\frac{q(4+2q)}{(1-q)^4}.
$$
The series and its first derivatives converge uniformly to their continuum counterparts by dominated convergence. With 32 equal angular bins, the one-end log oscillation satisfies $z\le\pi A/(32m)<0.072$ at **every** $J$ and in the continuum. Normalization of $K$ by its Hilbert–Schmidt norm does not change this estimate. The upper certificate for $\rho_2/\rho_1$ stays below $1/100$ throughout this refinement for exact histograms or relative error $\eta\le10^{-9}$ at exact arithmetic precision. To see this use $R_2\le q$, $d_0=z^2/2$, $r_{\rm raw}\le q+d_0$ and the same measured-ratio inequality as in the four-dimensional test. Finite precision only needs to resolve the strict margin. [Uniform rational check](controls.py)

| Spatial links | Gibbs ratio from 32 bins | Exact character ratio enclosed independently |
| --- | --- | --- |
| 4 | $[0.001486,0.004445]$ | $[0.001695,0.001696]$ |
| 8 | $[0.002011,0.005037]$ | $[0.002255,0.002256]$ |
| 16 | $[0.002168,0.005212]$ | $[0.002421,0.002422]$ |
| Continuum circle | $[0.002222,0.005272]$ | $[0.002478,0.002479]$ |

Entries are rounded outwards. The exact continuum ratio is $e^{-6}$, corresponding to energy $3$ above the vacuum at period two. At $J=4,8,16$, the reference value is $R_2^2$. To construct each table, integrate $\chi_d\chi_e$ against Haar on each angular bin using the endpoint sine formula. Keep $d,e\le16$. The omitted sum of coefficients is at most $S=q^{16}/(1-q)$ and each cell Gram entry has absolute value at most one. The numerator error per entry is bounded by $(2\sum_{d\le16}R_d+S)S$ and the normalization tail by $S^2$. Positive Bessel series, sine endpoints, division and square roots all use outward bounds. Normalize the matrix of midpoint roots to unit Frobenius norm and square its entries to get the nominal table. If the maximum root interval width is $w$, its pre-normalization error has Frobenius norm at most $32w$. Normalizing adds at most the same error. Dividing by the measured norm, at least $1/32$, gives $\eta\le2\cdot32^2w<10^{-9}$ in each listed calculation. The singular-value calculator uses only the resulting table, oscillation and uncertainty. The character formula supplies the table and reference levels through two different calculations. [Interval integration](cylinder.py) · [Rational spectrum](relative.py)

## A massless family at fixed and varying physical periods

For a free Maxwell field on a periodic spatial box of physical side $\ell$, restrict to transverse photon oscillators with the harmonic zero modes removed. With light speed one, the lowest oscillator energy is $\omega=2\pi/\ell$. The full first Gibbs ratio is $e^{-2\pi\tau/\ell}$, tending to one for fixed $\tau$. A single real lowest-mode amplitude provides a further statistic. The Euclidean oscillator covariance is proportional to $\sum_{k\in\mathbb Z}e^{-\omega|t+k\tau|}$ by periodization of its line Green function. At opposite times the correlation coefficient is $\operatorname{sech}(\tau\omega/2)$. Resolve two standardized Gaussian readings as projections of a rotationally symmetric normal pair along unit vectors of that inner product. The two wedges with opposite signs occupy angle $2\arccos(\operatorname{sech}(\tau\omega/2))$. Their probability is
$$
 \pi^{-1}\arccos(\operatorname{sech}(\tau\omega/2))
 =\pi^{-1}\arctan(\sinh(\pi\tau/\ell))\sim\tau/\ell .
$$
Taking $\tau=c\ell$ holds both statistics constant while the gap tends to zero. The energy test must divide by the physical period. This is an exact free transverse-sector control. Fröhlich and Spencer’s massless phase in four-dimensional compact Abelian lattice gauge theory gives an interacting literature comparison, without identifying its finite-box frequencies or sign law with the Gaussian calculation. [Fröhlich and Spencer, 1982](https://doi.org/10.1007/BF01213610)

A finite positive-transfer example also isolates the role of full slices. A two-state half-transfer with eigenvalues $1,1/2$ has Gibbs ratio $1/4$. Tensoring with an independent positive two-state half-transfer with eigenvalues $1,1-1/L$ and summing over both of its endpoint labels leaves precisely the original observed joint law. The full second ratio tends to one. Even exact measurements of the visible factor cannot bound the hidden sector without more information about it. Fully resolving one hundred identical $1,1/2$ factors instead gives vacuum probability $(4/5)^{100}<10^{-9}$ and first ratio $1/4$. [Finite matrix and photon controls](controls.py)
