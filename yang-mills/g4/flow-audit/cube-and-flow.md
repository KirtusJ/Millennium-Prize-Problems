# Periodic partition ratio and convergence of the Lie–Euler flow

## Checking C4's original powers

Let \(\ell\ge 4\) be even, \(P=3\ell^3\), \(z(\gamma)=\int \exp(-\gamma V(U))\,dU\), and normalize Haar on each link. For the defining SU(2) action \(V=1-\operatorname{ReTr}(U)/2\), its quadratic minimum and the three-dimensional Haar density give \(z(\beta)\asymp\beta^{-3/2}\). The one-step transfer extracts \(z(\beta)^P\). In the periodic trace the residual temporal holonomies implement the slice gauge projection. The strictly positive normalized top eigenfunction is simple and gauge invariant and its eigenvalue is at least \(e^{-CP}\) by the local product trial function. The even power in the trace permits keeping its top contribution. Thus \(Z_\ell(\beta)\ge z(\beta)^{P\ell}e^{-CP\ell}\).

For the upper bound drop the spatial action and the seam layer of \(P\) temporal plaquettes. With the temporal links fixed, each spatial link in the last slice appears in exactly one retained factor. Right or left Haar translation and inversion give \(z(\gamma)\) per integral. Peeling backwards over the \(\ell-1\) layers gives \(Z_\ell(\gamma)\le z(\gamma)^{P(\ell-1)}\). Per \(P\ell\), the log ratio at \(\gamma=\beta/2\) is at most \(C+\log(z(\beta/2)/z(\beta))-\ell^{-1}\log z(\beta/2)\). The last term costs \(O((1+\log\beta)/\ell)\). The copied-face inequality uses \(J\ge c\ell^4\) and bounded face multiplicity, giving the uniform local exponential moment on \(\beta=\ell\). This audit uses the program's original even-site reflection and finite-patch Haar identities. The sine half-test takes its displacement to infinity **after** identifying the tangent law. [C4's periodic proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/04370b2e92106cd77f45e1c5e020bc12c36e6356/yang-mills/central-quotients/magnetic-smearing/spatial-flow/wilson.md) · [Transfer input](../../central-quotients/lie-curvature/wilson-groups.md) · [Copying estimate](../../central-quotients/tangent-curvature/moments.md)

## A periodic seam bound with only four unmatched factors

There is also a direct partition check without a transfer eigenfunction, with a smaller cost in the ratio. In dimension \(d\) on the periodic side-\(\ell\) hypercube one can retain
\[
                         N_d=(d-1)(\ell^d-1)
\]
plaquettes and integrate exactly \(z(\gamma)^{N_d}\). Dropping all other nonnegative deficits bounds the full partition from above. The count is the same for every side \(\ell\ge3\).

1. In each column gauge the first \(\ell-1\) vertical links to identity. The change of variables consists of successive products by fixed group elements conditional on the vertical links. Product Haar leaves independent spatial Haar links and one Haar seam holonomy \(H_x\) per base vertex. The open column-tree variables integrate to one.
2. Keep every nonseam vertical plaquette, one seam plaquette for each edge of a spanning tree on the \((d-1)\)-dimensional spatial torus, and the recursively retained spatial plaquettes of the base slice. Integrate seam holonomies **first**, stripping leaves of the spatial tree. Each leaf variable then appears just once in a single remaining seam plaquette, inside \(A H_x^{\pm1}B\). Its integral is \(z(\gamma)\) whatever the two spatial slice configurations. The root holonomy integrates to one.
3. Next strip the spatial links at times \(\ell-1,\ldots,1\). Each appears just once when integrated, in its nonseam vertical plaquette. The base slice retains an ordinary \((d-1)\)-dimensional periodic Haar integral. The counts obey \(N_1=0\) and \(N_d=(d-1)\ell^{d-1}(\ell-1)+(\ell^{d-1}-1)+N_{d-1}\), yielding the formula above. Keeping a closed seam cycle instead of a tree would leave a loop constraint.

For a lower bound, gauge fix a spanning tree of the full \(d\)-torus graph. Of its \(d\ell^d\) links, \(\ell^d-1\) become identities. Restrict each of the \((d-1)\ell^d+1\) remaining independent Haar links to a ball of radius \(1/\sqrt\beta\) about identity. In the defining SU(2) model this ball has mass at least \(c z(\beta)\) for large \(\beta\). Every elementary holonomy lies within four such radii of identity, and the total action costs at most \(C_d\ell^d\) in the exponent. Absorbing all constants per link yields
\[
 e^{-C_d\ell^d} z(\beta)^{(d-1)\ell^d+1}
 \ \le Z_\ell(\beta)\ \le z(\beta)^{(d-1)\ell^d-(d-1)} .
\]

There are \(d\) unmatched one-link factors. Since \(z(\beta/2)/z(\beta)=O(1)\), this implies \(\ell^{-d}\log(Z_\ell(\beta/2)/Z_\ell(\beta))\le C'_d+O_d((1+\log\beta)/\ell^d)\). In particular the **four-dimensional even-cube** copying estimate now gives a uniform single-plaquette exponential moment all along \(\log\beta=O(\ell^4)\). The partition inequalities themselves do not rely on evenness. The statement about moments uses the even-cube reflection input. The finite check constructs the actual edge incidences and tests that each integrated link has exactly one surviving plaquette, in dimensions 2–4 on sides 3–5. [Incidence check](control.py)

Faria da Veiga and O’Carroll's published Theorem 1, Eqs. (71)–(72), uses positivity of the omitted plaquette actions and one-link factors for periodic and free boundaries. Their periodic factors use counts of retained and extra bonds. Chatterjee's §9 explains axial gauge fixing by a tree and the product-Haar change of variables. The count here uses a tree of *seam plaquettes* after fixing the vertical forest; the recursive choice is stated explicitly so it can be compared on the same periodic graph. These partition results concern the real action. The different source observable in Faria da Veiga and O’Carroll's Theorem 4 was addressed separately. [Faria da Veiga and O’Carroll, Theorem 1](https://repositorio.usp.br/directbitstream/ef6d3c36-bb3e-4609-acf3-305a632492f3/3265110.pdf) · [Chatterjee, §9](https://arxiv.org/pdf/1602.01222) · [Observable comparison](../contact-blocks/literature.md)

## Checking the integrator at the required normalization

Fix a finite time \(\tau\) in lattice units and a moment exponent \(q\ge1\). In the bi-invariant metric set \(\|D(U,W)\|_{q,*}=\sup_e\|\operatorname{dist}(U_e,W_e)\|_{L^q}\). There is no maximum over random links inside the expectation. The trivialized Wilson velocity \(v_e\) is smooth in a bounded list of neighboring links. Each one-link derivative is uniformly bounded on the compact group, independently of volume. The moment estimate gives initial velocity of order \(\beta^{-1/2}\) in this norm. Comparing velocity at time \(s\) to time zero, telescoping over its neighbors and integrating the link speeds gives \(B(s)\le B(0)+C\int_0^s B(r)\,dr\), where \(B(s)=\sup_e\|v_e(U(s))\|_q\). Thus \(B(s)\le C_{q,\tau}/\sqrt\beta\) for \(s\le\tau\).

For \(h=\tau/M\), compare the exact flow over one step to the trajectory driven by the frozen velocity at its start. In a bi-invariant metric the distance between solutions with left-trivialized velocities \(v,w\) and equal initial data is bounded by \(\int|v-w|\) (differentiate their relative group element and use invariance under conjugation). The local \(L^q\) error is at most \(C_{q,\tau} h^2/\sqrt\beta\). Also \(\operatorname{dist}(\exp X,\exp Y)\le|X-Y|\), by the same comparison along the two exponentials. Hence a frozen step has Lipschitz constant \(1+Ch\) in the link norm. Summing propagated errors bounds the final link error by \(C_{q,\tau}/(M\sqrt\beta)\). Four-link telescoping gives the same order for a plaquette. Its exact and numerical holonomies both stay \(O_{L^{2q}}(\beta^{-1/2})\) from identity.

For exact and numerical plaquettes \(U,V\), use the defining quaternion norm identity and Hölder:
\[
 \|\beta(V_{\rm act}(U)-V_{\rm act}(V))\|_q
 \le \tfrac{\beta}{2}\|U-V\|_{2q}
                 \big(\|U-1\|_{2q}+\|V-1\|_{2q}\big)
 \le C_{q,\tau}/M.
\]
An unscaled uniform error bound of order \(1/M\) on arbitrary compact configurations would lose a factor of \(\beta\) at this step.

For each fixed \(M\), the numerical update for finitely many marked faces depends on a finite contractible patch when \(\ell\) is large enough. Gauge the initial patch in one tree frame. The off-tree links are products of conjugated fixed-patch plaquettes and differ from identity by \(O_{L^{2q}}(\beta^{-1/2})\). Linearizing the finite update costs \(O_{L^q}(\beta^{-1/2})\) after curvature scaling. Taylor's formula on the identity chart and higher moments on its complement suffice; constants may depend on \(M\). At the identity the linear curvature update is \((I-hdd^*)^M\) on curls. The bounded lattice operator gives its heat multiplier when \(M\to\infty\). Thus the finite-patch cube limit is taken first, at fixed \(M,\tau\); the uniform scaled error then permits \(M\to\infty\). Uniform higher moments justify the same limiting passage for action products. No uniform integrator estimate at growing \(\tau\) enters the time-20 sign test.

Lüscher's Appendix C treats numerical integration of Wilson flow as an ODE on a product of compact groups. His higher-order algorithm and fixed-lattice error estimates explain the Lie-group update. The \(L^q\) link estimate with its \(\beta^{-1/2}\) factor is needed here to pass rescaled observables through a growing sequence of cubes. [Lüscher, Appendix C](https://arxiv.org/pdf/1006.4518) · [Fixed-time sign test](README.md)
