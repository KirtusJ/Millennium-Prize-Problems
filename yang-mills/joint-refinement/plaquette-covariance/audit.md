# Disposition of the two spectator assessments

G4 checked the spectator pre-audit and the independent assessment supplied on 23 November 2026 against their stated baseline e4d699c and the subsequent covariance argument. Both identify a real failure of the sliding spatial-difference inference. The Wilson result below uses a smaller, explicitly embedded coefficient space. The distinction can be tested on the auditors’ own model.

### The periodic Ising control

Take three independent centered periodic ferromagnetic Ising chains with $r=e^{-1/N}$, multiply their spins coordinatewise to form a three-dimensional field, and add independent unit-variance signs at its sites. Between endpoints retain the hidden configuration with probability $\rho=1-1/N$, otherwise resample it, and always refresh the noise. The stationary temporal transition on the latent variables is positive and reversible. The hidden spatial covariance is a tensor product of the three chain covariances. The one-dimensional sequence $(r^j+r^{N-j})/(1+r^N)$ has Fourier transform $c(q)=\tanh(1/2)(1-r^2)/(1-2r\cos q+r^2)$. This follows by summing the two finite geometric series. Writing $C(p)=\prod_j c(p_j)$, the observed equal-time and transmitted spectra are $1+C(p)$ and $\rho C(p)$.

For *all translates* of the unscaled three-direction unit difference, the covariance eigenvalues acquire $w(p)=\prod_j|1-e^{ip_j}|^2$. Wherever $w(p)>0$ the transmission quotient stays $\rho C(p)/(1+C(p))$. In particular $C(2\pi(1,1,1)/N)$ grows as $N^3$ and the quotient tends to one. The filtered equal-time covariance remains bounded: $|1-e^{iq}|^2 c(q)\le\tanh(1/2)(1-r^2)/r$, and the filtered unit-noise term is at most 64. Bounded absolute weight does not establish normalized contraction.

| $N$ | Sliding-filter variance at the specified mode | Its transmission | Largest transmission of the disjoint Wilson-style packet span **in this spin model** |
|---:|---:|---:|---:|
| 16 | 0.00370752 | 0.0452589 | 0.00135726 |
| 64 | $3.68731\,10^{-6}$ | 0.745921 | $2.36239\,10^{-5}$ |
| 256 | $4.38738\,10^{-8}$ | 0.991132 | $3.74896\,10^{-7}$ |
| 1024 | $6.82164\,10^{-10}$ | 0.998945 | $5.87632\,10^{-9}$ |

For the last column, take the normalized differences $(e_{8i}-e_{8i+4})/\sqrt2$ in each direction. At a coarse Fourier index, average $|1-e^{4iq}|^2c(q)/2$ over its eight fine aliases in each axis. The hidden-field eigenvalues on this span are products of these three averages. The same calculation with $c=1$ gives exactly one for the noise. Thus the innovation from fresh noise is at least the identity in these packet coordinates. A single slow fine plane wave cannot be isolated by tuning the coefficients of this family. The full observed space still contains it. [Reproducible spin calculation](audit_controls.py)

### Where the two Wilson inequalities meet

Let $D$ synthesize the disjoint normalized eight-corner packets from their coefficients. Then $D^*D=I$ exactly. For their coarse residuals let $G_D$ and $H_D$ denote the vacuum Gram and transmitted matrices. Independent private link pairs at every occupied corner give $G_D-H_D\succeq\delta D^*D=\delta I$. Spatial covariance control on the same coefficients gives $G_D\preceq8KI$. Hence $G_D-H_D\succeq[\delta/(8K)]G_D$. Moreover the exterior fixes every coarse reading, so the defect inequality holds after adding any coarse vector to the packet. This proves the stronger joint-block statement used for coupling. It leaves out both the uniform sum and slow modes outside this packet span. It does not transfer the conclusion to all translates of a sliding filter. [Matrix and coupling proof](README.md)

The second assessment’s projected-reflection objection also stands. For independent signs $X,Y$ and $\mathcal C=\sigma(X+Y)$, the residual $(X-Y)/2$ has reflected pairing $-1/2$ when reflection exchanges the sites. We reproduced this by enumeration. Spatial transfer positivity is applied **before** coarse conditioning. The only step from raw covariance to residual covariance is $\|(I-\mathbb E[\cdot\mid\mathcal A])O(c)\|_2\le\|O(c)\|_2$. Conditional independence at the two physical-time endpoints is proved separately. No monotonicity or maximum-at-zero property is claimed for the residual spectrum.

### Checks on the earlier result, physical time and scope

A vectorized incidence test reproduced all 6,690,600 spatial plaquette incidences for even sides 6 through 64. None contained two selected links and the global minimum selection count was $\lfloor N/6\rfloor$. The pressure comparison constant is 60.19224006167791, $K=14{,}905{,}840.64$, $\delta=2^{-22}/169$, and $\delta/K=9.46448346764\,10^{-17}$. The older erased-path vanishing bound requires $(1+\beta_N)\log N=o(N)$. The isotropic packet result requires no such coupling envelope. [Previous Wilson proof](../low-spin/README.md) · [Arithmetic and complete incidence check](audit_controls.py)

The physical-clock objection is correct for a box-side clock sent to infinity. For the present packings the two-end proof only uses **at least two** fine time steps between insertions, so no plaquette meets both private sets. At spacing $a_t$ one may choose $m=\max(2,\lceil t_0/a_t\rceil)$ for a fixed physical $t_0>0$ independently of the spatial side. At fixed spatial regulator use a vacuum cylinder with an extra exterior layer beyond each endpoint. The constants in the packet defect and covariance remain the same for $S=(T/\lambda)^m$. The coarse compression $a$ in the joint bound must be evaluated at this same lag. A compression on these non-invariant observable spans alone cannot be converted into a lower spectral gap for the whole theory.

The isotropic unfiltered covariance, unrestricted coarse-coefficient products, uniform coarse contraction, coverage of the physical observable algebra, continuum and volume limits, and the other compact simple groups remain separate obligations. The cited November 10 assessment reports an existence construction and leaves the mass gap and infinite-volume uniqueness open. The Clay problem asks for a nontrivial theory with a positive gap for every compact simple gauge group. Issue #1 stays open. [November 10 assessment](https://alexisdpc.github.io/yang-mills/references/assessment-1-2026-11-10.pdf) · [Clay’s problem statement](https://www.claymath.org/wp-content/uploads/2022/02/MPPc.pdf)
