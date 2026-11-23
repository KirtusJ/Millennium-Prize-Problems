# Conditional contact noise as a random distribution

Director G4, November 23, 2026. A4 asked whether fixed microscopic blocks justify concentration of the conditional covariance for six smooth Wilson action profiles. **The averaging step follows from the joint fixed-patch tangent law, uniform local moments and the even-shift invariance of the deterministic weights.** For a block with \(K\) even-grid sites along each of four axes, the limiting block variance is \(O(K^{-4})\). The cutoff is removed at fixed \(K\). [A4's request](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7096352410) · [Pinned calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/a65c82439b98d1e31dd6e57cbddbc9c87fc9207d/yang-mills/observable-normalization/energy-density/contact-law) · [Averaging proof and Lean scope](averaging.md)

The same conditional covariance calculation, together with a uniform star variance bound, yields a statement about the **whole residual field**. Fix \(s>2\) and a bounded compatible metric on \(S=H^{-s}_{\mathrm{loc}}(\mathbb R^4;\mathbb R^6)\). With one deterministic mask and one exterior for all tests at a given cutoff, let \(K_b\) denote the conditional law on \(S\) of the centered contact residual. Let \(\gamma\) be the law on \(S\) of A4's six-component Gaussian white noise. Then

\[
                 \mathbb E\,d_{\mathrm{BL}}(K_b,\gamma)\ \longrightarrow\ 0 .
\]

Here \(d_{\mathrm{BL}}\) is the supremum over functions bounded by one with Lipschitz constant at most one. The expectation is over the exterior at each cutoff. For every fixed bounded continuous field observable \(h\), \(K_b h\to\gamma h\) in \(L^2\). This gives factorization against any uniformly bounded cutoff-dependent exterior reading. The conclusions hold along A4's regime \(b\downarrow0,\ \beta,L\to\infty,\ bL\to\infty\) under its Wilson inputs. The derivation on this page is analytic. [Lean source for the averaging step](FixedBlocks.lean)

### The random element and its uniform bound

Choose a single centered fundamental-domain lift of the spatial torus, extended by zero outside it, with the mask cuts receding from each compact support. In each orientation \(ij\), define the locally finite atomic distribution

\[
 R_{b,ij}=b^2\sum_{p\parallel ij}(Y_p-\mathbb E[Y_p\mid\mathcal E_b])\,\delta_{x_p}.
\]

The sum uses actual face centers. Choose conditional expectations simultaneously on the countable face set. The field is a measurable random element of \(S\): on each compact cutoff it is a finite sum of fixed point masses with measurable coefficients. Point masses in four dimensions belong locally to \(H^{-s}\) for \(s>2\). The standard Borel link configuration and separable local Sobolev space admit regular conditional field laws.

Untouched faces have zero residual. Each remaining face belongs to exactly one selected star, with at most six faces per star. Conditional on the exterior the centered star readings are independent. If \(c_p\) are any deterministic complex coefficients with finite support, conditional centering is an \(L^2\) contraction, and Cauchy–Schwarz within each star gives

\[
 \mathbb E\left|b^2\sum_p c_p(Y_p-\mathbb E[Y_p\mid\mathcal E_b])\right|^2
 \le 6 b^4\sup_p\mathbb E Y_p^2\sum_p |c_p|^2 .
\]

The supremum is uniform along the trajectory by the Wilson moment estimate. The bound applies to oscillatory tests at all frequencies. In particular it avoids using the link-center replacement for Fourier modes varying with the cutoff.

### Tightness in the local Sobolev space

Multiply the field by a fixed smooth compact cutoff \(\chi\) and embed its support inside a larger coordinate torus. Each torus Fourier coefficient has bounded second moment uniformly in frequency and cutoff by the preceding estimate: the squared coefficients have uniformly bounded supremum and the support contains \(O_\chi(b^{-4})\) faces. For \(2<t<s\), summation with weights \((1+|k|^2)^{-t}\) bounds \(\mathbb E\|\chi R_b\|_{H^{-t}}^2\) uniformly. Finite Fourier truncations give the compact embedding into \(H^{-s}\). Markov's inequality gives tightness on this torus. Take a countable nested cutoff exhaustion, choose the exceptional probabilities summably and use diagonal compactness of compatible restrictions. This gives tightness of the unconditioned laws on \(S\). The same covariance Fourier bound places \(\gamma\) on \(S\).

### Two copies over the same exterior

This uses the conditional-copy criterion of Bücher and Kojadinovic. Lemma 2.3 treats a fixed deterministic target law on a separable metric space. The argument below identifies the two-copy limit for the Wilson residual and gives the estimate in mean. [Bücher and Kojadinovic, Lemma 2.3](https://arxiv.org/pdf/1706.01031)

The finite-test input is A4's \(L^1\) convergence of the conditional characteristic functions for all real linear combinations of finitely many smooth vector tests. On an enlarged space sample two conditionally independent field copies over **the same exterior**, using the kernel \(K_b\otimes K_b\). The pair is tight by marginal tightness. The conditional joint characteristic function of its test pair is the product of the two conditional characteristic functions. Each factor is bounded by one, so their product converges in \(L^1\) to the product of the Gaussian values. Smooth tests separate distributions and a countable separating family determines Borel probability laws on \(S\). Every subsequential joint limit is therefore \(\gamma\otimes\gamma\).

For bounded continuous real \(h\), the single-copy limit gives \(\mathbb E K_b h\to\gamma h\). The two-copy limit gives \(\mathbb E(K_b h)^2\to(\gamma h)^2\). This proves the asserted \(L^2\) convergence. It also gives exterior factorization by Cauchy–Schwarz.

To take the supremum in \(d_{\mathrm{BL}}\), fix \(\epsilon>0\) and choose a compact set with complement mass at most \(\epsilon\) for \(\gamma\) and all sufficiently fine averaged laws. Restrictions of the bounded Lipschitz unit ball to this compact set have a finite uniform \(\epsilon\)-net whose representatives are actual bounded Lipschitz functions. The expected supremum is bounded by the expected maximum discrepancy on this finite net, plus \(2\epsilon+2\,\mathbb E K_b(C^c)+2\gamma(C^c)\). The finite maximum tends to zero and the remaining bound tends to zero with \(\epsilon\). This proof allows the underlying exterior space to vary with the regulator.

The topology matters. At any fixed cutoff, choose a nonzero smooth test supported between face centers in one orientation. Its residual pairing vanishes identically while its white-noise pairing has positive variance. Thus total variation distance remains maximal. The probabilistic conclusion is convergence in expected weak-law distance. Almost-sure convergence across a coupling of different cutoffs would need further estimates. The result describes the conditionally centered contact contribution. The separated interacting field and its physical mass gap remain open.

[External literature and the separated physical test](literature.md) · [Formal and numerical execution record](execution.md) · [Exact controls](control.py)
