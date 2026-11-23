# Reproduce the checks

[The manuscript](README.md) proves the fixed-regulator conditional and transfer estimates. [The covariance calculation](covariance.md) proves the upper bound and spatial support for the part removed. The physical four-dimensional measure, gauge-invariant projection and conditional disintegration are manuscript arguments. Lean checks nine declarations including the full finite-sum monotonicity implication, the quaternion lower bound, the numerical cost of changing density, adjoint and duality constants, colour averaging and the two-endpoint inequality. The finite-sum theorem takes nonnegative longitudinal correlations as a hypothesis; its Wilson justification is the spatial-transfer proof. [Lean source](Floor.lean)

The native PCP OS supervisor and children emitted pre-authored Lean sections. The hosted supervisor and compiler checked the assembled source against Lean 4.19 and mathlib. Both deliberately false mutations fail. The initial compiler attempt failed on an unavailable tactic and its diagnostic is retained. The archived model replies are research drafts and challenges, including their original objections. A successful worker receipt verifies process and readback. The proof as adopted is in the manuscripts. The review of the reduced model is limited to the Harnack and path-ball interfaces plus the stated normalization check. [Archive](evidence.zip) · [Register and source verifier](verify.py)

Run the following from this directory with Python and NumPy. The upstream signed comparison also uses SciPy. The verifier accepts the same PCP runtime and method as the earlier joint-refinement release.

~~~text
python controls.py
python blocks.py
python source.py
python quadratic-tail.py
python ../plaquette-covariance/signed.py
python verify.py
python verify.py --runtime /path/to/PCP_OS_Python --method /path/to/Method
~~~

The [opposite-source test](source.md) gives Z4 a finite source strength at which a uniform partition-function estimate would suffice. It also specifies the two-copy test for residuals conditioned on the same coarse data.

The incidence control includes periodic coarse paths in four dimensions. At temporal period six it permits lags two and four and detects actual action faces coupling the endpoint sets at lags one and five. The quaternion control uses noncommuting samples, tests the mixed sign sum against its formula, and checks cancellation of duplicate oppositely oriented traces. The half-band test includes a failed closed-band boundary example. The block program checks the zero-mode normalization against per-configuration signed sums and reproduces every block by independent Fourier and spatial overlap counts. The quadratic program evaluates all block sizes on each of six spatial sides. None of these finite computations supplies the open interacting variance ceiling.
