# Reflection after fixing spatial momentum

Use $d$ independent free Maxwell colors and the centered magnetic energy $H=\frac12\sum_{i,a}(B_i^a)^2$. The ordinary unflowed spatial-momentum kernel at positive time has a nonnegative transfer spectrum. Full flow smooths both readings for a physical time $s>0$. At temporal separation $t>0$ the scalar magnetic propagator factor at $p=|\mathbf p|>0$ is
$$
 D_s(t,p)=\int_{2s}^{\infty}\frac{e^{-\alpha p^2-t^2/(4\alpha)}}{\sqrt{4\pi\alpha}}\,d\alpha,\qquad
 D_0(t,p)=e^{-pt}/(2p).
$$
The magnetic tensor is $(p^2 I-\mathbf p\mathbf p^\top)D_s(t,p)$. This expression follows from the Schwinger parameter of the heat-smoothed four-dimensional propagator before magnetic differentiation. Spatial-only flow instead has factor $e^{-2sp^2}D_0(t,p)$. [Eller and Moore, §§2–3](https://arxiv.org/pdf/1802.04562) · [Previous point covariance](../spatial-flow/spectrum.md)

### All spatial sectors have a signed full-flow test

Fix $\mathbf k\in\mathbb R^3$, including zero. Put $\mathbf q=\mathbf k-\mathbf p$, $q=|\mathbf q|$, and let $c$ be the angle cosine between $\mathbf p,\mathbf q$ off their null sets. Wick contraction gives the connected full-flow reading per unit spatial Fourier measure,
$$
 G_s(t,\mathbf k)=\frac d2\int\frac{d^3p}{(2\pi)^3}\,
 p^2q^2(1+c^2)D_s(t,p)D_s(t,q).
$$
The factor $1+c^2$ is the trace of the two transverse projectors. Every displayed factor is positive almost everywhere. Integrating against $|\widehat f(\mathbf k)|^2d^3k/(2\pi)^3$ gives the reflected kernel for any fixed nonzero spatial Schwartz test $f$, including compactly supported probes. Negative tests below use the *same* $f$ at every reading.

Splitting the Schwinger integral at $2s$ gives, for $t>0$,
$$
 0<D_0(t,p)-D_s(t,p)\le e^{-t^2/(16s)}D_0(t/\sqrt2,p).
$$
For $0<\alpha\le2s$, split $e^{-t^2/(4\alpha)}$ into equal factors and bound one by $e^{-t^2/(16s)}$. Extending the remaining integration to infinity proves the estimate. In the product kernel subtract the two factors one at a time and use $D_s(t,q)\le D_0(t,q)\le D_0(t/\sqrt2,q)$. This gives the strict difference and bound
$$
 0<G_0(t,\mathbf k)-G_s(t,\mathbf k)
 \le 2e^{-t^2/(16s)}G_0(t/\sqrt2,\mathbf k).
$$
The same inequalities hold after any of the above spatial tests. At positive separation all unflowed integrals are finite; this follows directly from $e^{-t(p+q)}$. That factor also represents $G_0$ as a positive energy measure at $E=p+q$.

At $T+nh$ for any $T,h>0$, the unflowed sequence is a bounded moment sequence on $[0,1]$, obtained with $x=e^{-hE}$ and time tilt $e^{-TE}$. The flowed sequence differs by a strictly negative term $b_n$ decaying faster than every geometric sequence. If all flowed Hankel matrices were positive semidefinite, Hamburger's theorem and bounded even moments would give a positive representing measure on $[-1,1]$. The moment difference would be a finite signed measure. Its exterior Cauchy series extends holomorphically across every real point away from zero. Poisson inversion would confine that measure to zero and force $b_n=0$ for $n\ge1$. This contradicts the strict propagator deficit. **For every prescribed spatial momentum (also zero), spatial test as above, positive buffer, and mesh, there is a finite negative time test in that sector.** Strict signs survive narrow common temporal mollification. [Complete moment argument](../flow-reflection/grids.md) · [Schmüdgen, Thm. 1.12](https://arxiv.org/pdf/2008.12698)

### Finite temporal differences cannot restore positivity

On a chosen time mesh replace each reading by $\sum_{\ell}a_\ell H(t+\ell h)$ for any real nonzero finite vector with nonnegative lags. The comparison measure acquires weight $P(x)^2$, $P(x)=\sum_\ell a_\ell x^\ell$. The difference sequence is the finite combination $\sum_j [x^j]P(x)^2\, b_{n+j}$. It still decays faster than every geometric sequence. Suppose it vanished from some index on. After dropping leading zeros its first nonzero coefficient would give a constant-coefficient forward recurrence for a tail of $b$. This is impossible.

Indeed a recurrence $c b_n+\sum_{j\in S}a_j b_{n+j}=0$ with $c\ne0$ and finite $S\subset\mathbb N_{>0}$ gives $|b_n|\le A\max_{j\in S}|b_{n+j}|$, $A=\sum|a_j|/|c|$. If $S$ is empty it already forces a zero tail. Otherwise choose $B> \max(1,2A)$. The bounded sequence $v_n=B^n|b_n|$ would admit a later value at least $2v_n$ at every index. Iterating forces $v_n=0$ at every index of the tail, contradicting $b_n<0$. The defining geometric bounds persist under reindexing. Lean checks this recurrence argument for arbitrary finite sets and real coefficients. Thus the signed-measure contradiction still applies after **each nonzero finite time filter**, including subtraction of neighboring readings. Adding local contact terms at time separation zero also leaves every test here unchanged. [Formal proof](FlowMomentum.lean)

For a nonzero finite **nonnegative** measure of temporal offsets in a fixed compact subset of $[0,\infty)$, integrating the two readings gives the same conclusion directly. The deficit stays strictly negative at every index. The comparison measure is weighted by the squared Laplace transform of the offsets and the preceding uniform Gaussian bound applies. No conclusion for an arbitrary signed continuous temporal filter is needed.

These are exact obstructions to positive spectral reconstruction of the specified fully flowed magnetic observable. The free unflowed gauge theory and its underlying transfer remain positive. Large-time numerical fits can resolve the ordinary spectral scale while missing the much smaller signed tests. [Sakai and Sasaki, full and spatial flow in glueball spectroscopy](https://doi.org/10.1103/PhysRevD.107.034510)

Thermal heavy-quark transport calculations also distinguish finite-flow spectral models from the zero-flow extrapolation. The chromomagnetic Wilson-line observable, temperature and inverse problem in that work differ from the vacuum magnetic energy considered here. [Heavy quark diffusion coefficient with gradient flow, discussion of spectral reconstruction](https://doi.org/10.1103/PhysRevD.107.054508)
