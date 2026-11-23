# Free-field controls for the proposed interaction tests

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)  
Research program directed by Kirtus Justus

Two calculations bear on Z4’s hypothesis (E). The proposed finite-volume test (E-c*) gives a false interaction signal if the comparison to $2m$ is allowed in an arbitrary symmetry channel. The proposed integrated four-point test (E-a) can give a nonzero continuum-limit number even in an exactly free theory. For a Wick square, its result depends on the definition of correlation length. Both calculations below use free fields with an isolated one-particle mass shell. [Formulations reviewed, §§0–1](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/5b58bcd4035aa94d639404e78dbe47276d211040/yang-mills/z4/attempt/reviews/c1-E/HYPOTHESIS_E.md)

## A strictly positive shift with identity scattering

Take a single free nearest-neighbor real scalar on a periodic spatial cube of integer side $L$, with infinite Euclidean time. Its one-particle energy and action mass parameter satisfy
$$
 \omega_m(p)=2\operatorname{arsinh}\left(\tfrac12\sqrt{\mu^2+\sum_i4\sin^2(p_i/2)}\right),\qquad
 \mu=2\sinh(m/2),\qquad p=2\pi j/L.
$$
Energies in the two-boson sector with total momentum zero are $2\omega_m(p)$. The zero-relative-momentum state transforms in the spatial cubic trivial representation $A_1^+$. On the first nonzero shell the three unordered pairs of momenta $\{\pm 2\pi e_i/L\}$ transform by permutation of the coordinate axes. The all-ones line is $A_1^+$; the two-dimensional plane of coefficients summing to zero is $E^+$. There is no $E^+$ at relative momentum zero. Thus the lowest two-boson energy in $E^+$ is **exactly** $2\omega_m(2\pi e_1/L)$. This is a symmetry assignment of actual states. A zero-total-momentum source obtained by summing $:(\nabla_1\phi)^2-(\nabla_2\phi)^2:$ has the nonzero shell weight $\widehat p_1^2-\widehat p_2^2$ and creates such states. Normal ordering is with respect to the free vacuum. [Lüscher 1991, §5.1, especially eqs. (5.2a,c) and Table 1](https://www-library.desy.de/preparch/desy/postpr/1990/desy90-131.pdf) · [Free lattice dispersion](../local-overlap/README.md)

Now send $m\downarrow0$ with $mL\to z>0$. The purported interaction shift for this channel tends to
$$
 \frac{E_{2,E^+}(L)-2m}{m}\longrightarrow 2\left(\sqrt{1+(2\pi/z)^2}-1\right)>0 .
$$
At $z=8$ the shift is 0.54310855 in mass units, with the pair energy below $3m$. The free scattering operator is the identity. Subtracting **the free level with the same relative-momentum shell and cubic representation** gives zero already at every regulator. In the $A_1^+$ channel the genuine two-particle ground energy is $2m$. Nevertheless the zero-momentum sum of the spatial gradient square $:\sum_i(\nabla_i\phi)^2:$ has a pair matrix element proportional to $\sum_i\widehat p_i^2$, which vanishes at rest. Its connected correlator starts at the first nonzero shell even in $A_1^+$. An observable’s first visible level need not be the channel ground level.

**Correction for the reduction.** Specify the stable particle species, boundary conditions, total momentum, cubic representation, and which elastic level the observable resolves. Form the additive free baseline from the identified one-particle dispersion and allowed relative momenta, resolving shell multiplicities where necessary. In the scalar trivial channel with the lowest rest pair identified, this baseline is twice the one-particle rest energy. Account for one-particle finite-volume shifts when comparing to an infinite-volume mass. To infer a nonzero infinite-volume on-shell scattering amplitude, one also needs an applicable finite-volume quantization relation and control of its finite-size and cutoff errors. A fixed value of $mL$ by itself gives no large-volume error estimate. The counterexample addresses the “some symmetry channel” quantifier. It leaves a matched elastic-level test and a direct nonidentity scattering test available.

Lüscher’s 1986 paper explicitly singles out the lowest $p=0$ level in eq. (1.3); eq. (1.6) sets the scattering-length sign convention. In that convention the leading energy correction is $-4\pi a_0/(mL^3)$ at large $L$. The 1991 treatment resolves cubic representations and relates the spectrum below inelastic threshold to the elastic phases, with finite-range or exponentially small finite-volume qualifications as appropriate. The formulas concern different momentum levels and approximation regimes. [Lüscher 1986, eqs. (1.3)–(1.6)](https://doi.org/10.1007/BF01211097) · [Lüscher 1991, introduction and §§5,7](https://www-library.desy.de/preparch/desy/postpr/1990/desy90-131.pdf)

A sufficient threshold witness under these scattering hypotheses can be written in gap units. Let $\delta_0(z)$ be the continuum limit of the mass-normalized shift of the **identified rest-pair ground state** at $mL=z$, with the one-body reference consistently matched. If the continuum large-box expansion applies and one-body or other residual errors are $o(z^{-3})$ in these units, then
$$
 -\frac{1}{4\pi}\lim_{z\to\infty} z^3\delta_0(z)=m_{\rm phys}a_0 .
$$
A finite nonzero value is sufficient to exclude free elastic scattering in that channel. Zero scattering length does not settle the amplitude at other energies or in other channels. Here the continuum limit at fixed $z$ precedes the large-box limit; an interchange would need uniform errors. For comparison the free $E^+$ example has an uncorrected $4\pi^2/z^2+O(z^{-4})$ shift simply from motion on the first shell. No Wilson scattering limit or phase extraction is supplied by the example.

## What the integrated four-point coupling measures for a Wick square

On infinite $\mathbb Z^4$, take $k$ independent real Gaussian fields with scalar covariance $G_\mu$, whose Fourier transform is $D_\mu(p)^{-1}=(\mu^2+\sum_{a=1}^4 4\sin^2(p_a/2))^{-1}$. Set $O_x=\tfrac12\sum_{c=1}^k :\!\phi_c(x)^2\!:$ and use the connected correlations of $O$. Let $\chi$ be the sum of the two-point function, $u_4$ the sum over three independent locations of the connected four-point function with the fourth fixed, and $\xi_2^2=\sum_x |x|^2\langle O_0 O_x\rangle/(8\chi)$. Define $I_j=\int D_\mu^{-j}d^4p/(2\pi)^4$ over the Brillouin zone and $J=\int |\nabla_p D_\mu^{-1}|^2d^4p/(2\pi)^4$.

Wick contractions give $\langle O_0O_x\rangle=kG_\mu(x)^2/2$. At fourth order there are six directed cycles, each with coefficient $k/2$. Each integrated cycle gives $I_4$ by convolution. For instance these coefficients also follow by expanding $-k\log\det(I-GT)/2$ for a diagonal matrix of local sources $T$. Parseval applied to $x_jG_\mu(x)$ gives the exact identities
$$
 \chi=kI_2/2,\qquad u_4=3k I_4,\qquad \xi_2^2=J/(8I_2).
$$
The lattice regulator includes coincident positions throughout these sums. At fixed $\mu>0$ absolute convergence follows from exponential decay of the massive propagator. The cumulant calculation at a single point alone cannot give these susceptibility or length asymptotics.

For $\mu\downarrow0$,
$$
 I_2=\frac{\log(1/\mu)}{8\pi^2}+O(1),\qquad
 I_3\sim\frac{1}{32\pi^2\mu^2},\qquad I_4\sim\frac{1}{96\pi^2\mu^4}.
$$
On a fixed small ball the substitution of $|p|^2$ for the lattice symbol in $I_2$ has integrable error bounded by $C|p|^4/(\mu^2+c|p|^2)^3$. The continuum radial integral gives the log coefficient. For $I_3,I_4$, rescale $p=\mu q$ and dominate by $(1+c|q|^2)^{-j}$ using the chord bound throughout the cube. The limiting integrals are $\Gamma(j-2)/(16\pi^2\Gamma(j))$. Finally, integrating $\partial_{p_i}(\sin p_i D_\mu^{-3})$ over the torus and summing gives the exact identity
$$
 J=\tfrac13\big[(8+\mu^2)I_3-I_2\big]\sim\frac{1}{12\pi^2\mu^2}.
$$

It follows that the *specific normalization proposed in (E-a)* has a finite nonzero limit:
$$
 g_R=-\frac{u_4}{\chi^2\xi_2^4}
     =-\frac{768 I_4}{kJ^2}\longrightarrow-\frac{1152\pi^2}{k}.
$$
The sign follows the minus sign in the definition in Z4’s note. This is a Gaussian lattice action, an exactly known local composite and identity scattering. The result supports the warning in (E-a) and supplies the missing integrated derivation. Meanwhile $\xi_2^2\sim[12\mu^2\log(1/\mu)]^{-1}$. The exponential correlation length of the **same composite** is $\xi_{\rm exp}=1/(2m)$ because the two-particle support starts at $2m$. With that length in the denominator the result is instead
$$
 -\frac{u_4}{\chi^2\xi_{\rm exp}^4}
   \sim -\frac{128\pi^2}{k\log^2(1/\mu)}\longrightarrow0 .
$$
Thus the two sampling conventions can give opposite answers to a nonvanishing test in the very same free model. These are infinite-volume sums followed by a weak-mass limit. A finite-size Binder measurement at prescribed box-to-length ratio needs its own analysis.

## Verification

The numerical checker enumerates the first nonzero cubic shell and integrates the full infinite-lattice propagator by the heat-kernel formula. Specifically $D^{-j}=\int_0^\infty t^{j-1}e^{-tD}dt/\Gamma(j)$, and each coordinate integral contributes $e^{-2t}I_0(2t)$ (modified Bessel function). Inserting a cosine uses $e^{-2t}I_1(2t)$. The two numerical evaluations of $J$ agree within $2\times10^{-10}$ relative error. At $\mu=2^{-12}$ the measured $kg_R/\pi^2$ was $-1152.0000613$. For $L=1024$, $mL=8$, the free $E^+$ shift was 0.54310057. Two three-generation PCP OS deployments emitted the same four Lean-checked declarations covering the shell weight, cycle count and arithmetic. The analytic limits and matching correction are written arguments. [Numerical checker](check.py) · [Native worker](worker.c) · [Lean read-back](InteractionControls.lean) · [Verifier](verify.py) · [Receipts](receipts.zip)
