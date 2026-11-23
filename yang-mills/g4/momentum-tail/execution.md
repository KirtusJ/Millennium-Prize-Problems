# Checks on momentum tightness

G4 checked C4’s signed path reordering, periodized spatial tests and the return from compactified energy to finite energy at revision 667f247. The fourth power of the normalized Fejér test then gives an explicit tail for the whole fourfold-packet momentum marginal. A4’s reflected rectangles and common-root estimate at e2e56f5 supply the sharper finite-coupling input. These analytical results depend on the stated Wilson pressure and covariance estimates. [Proof and hypotheses](README.md) · [C4’s original review request](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7102737200)

Four named Lean declarations compiled under Lean 4.19.0 and Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b. They prove bounded-error transfer for a finite real Fourier coefficient sum, the fourth-power test floor, the eighth-moment cutoff estimate for a Pareto-six comparison, and integration of a measurable-set test floor against an arbitrary finite measure. The test coefficients in the paper are real and symmetric, so the finite-sum statement applies to the real parts of the spatial readings. Four distinct altered statements failed elaboration. The original link integration, Fourier kernel estimate, layer-cake application and interacting tail theorem are written proofs. [Lean source](MomentumTail.lean) · [Altered statements](mutations.json)

Five PCP OS research reviews covered signed paths, the free mixture, the Fourier cutoff, the first manuscript and the manuscript with A4’s stronger input. A distinct drafting commission produced the finite-sum Lean statement and proof, followed by a separate challenge. The compiler had its own parent and child. The hosted parent registers bind each child’s receipt and post-exit readback. These Codex workers share the director’s provider family. Six native method cases and three native source emitters ran on fresh PCP OS kernel boots. The emitted bytes assemble to the same source that ran in host Lean, SHA-256 a6efe1affa5087a1ba2beaa6e89e28e580494566a385c3c1487be50cee433b4c. [Evidence and logs](evidence.zip) · [Verifier](verify.py)

The free-tail review pointed out that a one-sided density estimate cannot establish sharpness. The lower bound uses the exact fourfold magnetic density on positive-measure strips in the first coordinate. The Fourier review identified the maximum-norm convention at the edge of the Brillouin cube and the need for the zero-shift reading. The endpoint error can permit residual escaping mass at fixed $c$. Full comparison at the original eighth-root scale and the updated seventh-root scale each received a separate review.

The independent exact controls checked 15,625 signed path pairs, 67,500 swaps in all 12 ordered-axis/sign cases, 42 rational Fourier evaluations at each of degrees four and five and 2,960 wrapped three-leg sums. A stride-only test folded scaled momenta $0$ and $2\pi e_1$. The full filter distinguished them exactly. Six rational layer-cake examples gave $4/A^6-3/A^8$ and $5/A^8-4/A^{10}$ respectively for $A\ge1$. G4 also reproduced C4’s 160 signed quaternion tests and 375 periodization checks and recompiled the six declarations from the pinned upstream file. The first run of C4’s script encountered a Windows console encoding error while printing the final $\pi$; the UTF-8 rerun completed both groups. [Exact controls](check.py)

From this directory use Python 3.11 or later. The verifier checks all expected archive objects, source digests, compiler and mutation logs and the native serial payload. With the optional runtime and method arguments it replays all 19 hosted registers. The verifier reuses the repository’s existing compiler and native verification helpers.

~~~text
python -B check.py
python -B verify.py
python -B verify.py --runtime <PCP_OS_Python> --method <Enterprise-method-directory>
~~~

## Direction-resolved follow-up

C4 independently cleared the centered wrapping and transfer of the Fourier cutoff at the original branch revision, reproduced the 2,960 wrapped cases and 42 degree-four Fourier tests, and independently identified the eighth power for the normal component. [C4’s director review](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/11#issuecomment-7103114184)

B4 checked the common Fourier coefficient budget, the summable $(2j)^7$ mixture factor and the far-angle floor at the representative seam $H=\pi R$. B4 also reproduced the 20 floor checks and concurred with the sharp sixth power under the stated equal-time Wilson comparison. [B4’s director review](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/11#issuecomment-7103139183)

For the specified fourfold box, the squared normal box factor is exactly $[\sin(p_3/2)/(p_3/2)]^8$. On the lower-bound set $2H\le p_3\le3H$ with $|\sin(p_3/2)|\ge1/2$, it is at least $(3H)^{-8}$. This checks the additional factor required by the last reader.

For momentum normal to the $12$ face, the projection amplitude gains an extra inverse power of $|p_3|$ while both in-plane momentum factors have finite second moments. The limiting normal tail is of order $H^{-8}$, and a fifth-power Fejér test transfers the upper bound to Wilson with the same additive error. Two additional PCP reviews tested the change of power. The first identified the need to pin the stride in the lower bound. The squared stride-$R$ difference is exactly $(2|\sin(p_3/2)|)^6$ in scaled coordinates, so the same set of phases controls both the difference and the box denominator. [Directional estimate and proof](directions.md)
