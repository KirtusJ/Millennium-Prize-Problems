# An exact counterexample to Step S6 on the periodic SU(2) lattice

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

In Z4’s Step S6, nonnegative trace on every plaquette is supposed to give horizontal Bakry–Émery curvature at least $1/2$ for all sufficiently large Wilson coupling $\beta$. There is an explicit counterexample on every periodic four-cube of side $L\ge2$, including every dyadic side in the manuscript. The plaquette traces can approach their maximum, and the total weighted Wilson action on a fixed box can tend to zero, while the horizontal curvature tends to minus infinity. This disposes of that pointwise hypothesis. A Poincaré inequality for the equilibrium measure or a spectral bound for its transfer matrix is a separate question. [Step S6 and the metric convention](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2d3e65698f41a398bee4264ccfe685999ecb0a9f/yang-mills/z4/attempt/paper/sec_negative.tex#L28-L98) · [Shen, Zhu and Zhu on strong-coupling functional inequalities](https://arxiv.org/abs/2204.12737)

## Constant links and a horizontal geodesic

Let $V=L^4$, and let $\sigma_1,\sigma_2$ be distinct Pauli matrices. Give every positive link in direction 1 the value $\exp(ia\sigma_1)$ and every positive link in direction 2 the value $\exp(ia\sigma_2)$, with identity on directions 3 and 4. For any angles $A,B$, the commutator of $\exp(iA\sigma_1)$ and $\exp(iB\sigma_2)$ has half-trace $1-2\sin^2 A\sin^2 B$. Indeed conjugation about the first axis rotates the second Pauli axis through angle $\pm2A$; the scalar part after multiplication by the inverse second link is $\cos^2B+\sin^2B\cos(2A)$. Hence, writing $u=\sin^2a$, the $V$ faces of type 12 have half-trace $1-2u^2$. All other faces have half-trace one.

Vary the two link angles to $A=a+t$, $B=a-t$ along the corresponding one-parameter subgroups. This is a product geodesic for the paper’s metric $\langle X,Y\rangle=-\operatorname{Tr}(XY)$. Its left-trivialized velocity is $v_1=i\sigma_1$, $v_2=-i\sigma_2$, and zero otherwise. Its squared norm is $4V$.

For arbitrary site generators $\omega_x$, the vertical tangent on $e=(x,x+\hat\mu)$ is $\omega_x-\mathrm{Ad}(U_\mu)\omega_{x+\hat\mu}$. Each nonzero $v_\mu$ commutes with its link and is constant in $x$. The inner product with this vertical tangent sums to zero by shifting $x$ one periodic step in the second term, separately in each direction. Thus $v$ is horizontal even with respect to the full site gauge group.

The potential along the geodesic, up to an additive constant, is
$$
2\beta V\sin^2(a+t)\sin^2(a-t)=2\beta V(u-\sin^2t)^2 .
$$
Its second derivative at zero is $-8\beta V u$. With the manuscript’s Ricci contribution $+1$, the horizontal Rayleigh quotient gives
$$
\kappa_H(U)\le\frac{(\mathrm{Ric}+\mathrm{Hess}\,V_{\rm Wilson})(v,v)}{|v|^2}=1-2\beta u.
$$
This is an upper bound on the smallest horizontal eigenvalue; the argument only needs one direction.

* **Fixed links:** $a=\pi/4$ gives minimum half-trace $1/2$ and quotient $1-\beta$.
* **Near identity:** $u=1/\beta$ for $\beta\ge2$ gives minimum half-trace $1-2/\beta^2$ and quotient $-1$.
* **Vanishing total action at fixed volume:** $u=\beta^{-3/4}$ gives weighted action deficit $2V/\sqrt\beta$, minimum half-trace $1-2\beta^{-3/2}$ and quotient $1-2\beta^{1/4}$. All quantifiers can hold on the same fixed dyadic box.

## Cross-check against the numerical record

The [independent checker](check.py) inserts these links and velocities into the original program’s plaquette, gauge matrix and full Hessian routines. On $L=2,3$, $\beta=3,12,48$ and all three choices of $u$ above, 18 checks passed for gauge orthogonality, speed, minimum trace and Rayleigh quotient. A three-generation PCP OS deployment counted face multiplicity and speed on a $4^4$ torus and emitted the polynomial identities for the action and tensor. Hosted Lean 4.19.0 accepted four supporting declarations and the verifier rejected four adverse controls. The geodesic and horizontality arguments are proved above. [Original Hessian implementation](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2d3e65698f41a398bee4264ccfe685999ecb0a9f/yang-mills/z4/attempt/reviews/a4-chalcurv/lat.py) · [Worker](worker.c) · [Lean declarations](HorizontalCurvature.lean) · [Verifier](verify.py)

For the paper’s curvature figure, the archived output supplies stronger descriptive evidence than the table. Program 2 recorded four periodic $3^4$ configurations per plotted coupling. Its per-sample maximum deficit is $1-\tfrac12\mathrm{ReTr}\,Q$ maximized over all faces. Across the four rows at each of $\beta=12,24,48$ that maximum never exceeded $0.3241,0.1776,0.0860$, respectively. Every face was therefore positive in those twelve records. The open $4^4$ panel also has all three raw ranges at high coupling: $[2.8798,3.2089]$, $[9.1849,10.0072]$, and $[23.1503,23.4645]$. Those ranges can replace the rounded singleton points. The periodic zero-momentum eigenvector weights at $\beta=12$ span $0.185$ to $0.912$; the quoted $0.96$–$0.99$ needs its coupling range specified. [Periodic output](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2d3e65698f41a398bee4264ccfe685999ecb0a9f/yang-mills/z4/attempt/reviews/a4-chalcurv/result_a2_L3p.txt) · [Open-box output](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2d3e65698f41a398bee4264ccfe685999ecb0a9f/yang-mills/z4/attempt/reviews/a4-chalcurv/result_a2_L4o.txt)

The separate flux figure also replays. Both archived SVG byte hashes match their `expected_svg_sha256` receipts. With the unchanged `zflux.py`, all 14 output lines, including the six estimates, their ten-bin jackknife errors and the failed U(1) tree-level predicate, reproduced at printed precision after stripping elapsed times. The six plotted intervals are the rounded table estimates plus or minus the rounded errors. The executable seeds are $1000+10L$ for SU(2) and $1001+10L$ for U(1). The curvature program likewise specifies $1000L+\mathbf1_{\rm open}+\operatorname{round}(\beta)$. The plotted flux estimator is $L\operatorname{arcosh}[(C(0)+C(2))/(2C(1))]$. At $L=6$ the SU(2) reading at the next lag is $6(0.8398)=5.0388$, versus $8.0194$ at the first lag. Label the figure with its measured effective mass. Replay establishes reproducibility of these outputs; the archived calculation does not establish a ground-state plateau or quantify autocorrelation bias in the stated errors. [Original flux program](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2d3e65698f41a398bee4264ccfe685999ecb0a9f/yang-mills/z4/attempt/reviews/a3-Afs/zflux.py) · [Measurement record](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/2d3e65698f41a398bee4264ccfe685999ecb0a9f/yang-mills/z4/attempt/reviews/a3-Afs/result_zflux_1.txt) · [Wolff on Monte Carlo error estimates](https://arxiv.org/abs/hep-lat/0306017)
