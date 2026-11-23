# Computational record and formal scope

Two measured three-level native PCP OS deployments generated the same [Lean source](SpatialFlow.lean). The parent counted the four leading visible torus modes and the eight first mixed temporal modes. The child computed the signed integer bound from the rounded Fourier enclosures. The third level computed the two different low-energy powers. The hosted supervisor checked each returned child digest, desk ancestry and successful close state. The hosted Lean 4.19.0 kernel accepted 19 declarations in each run against Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b. The listed axioms are within propext, Classical.choice and Quot.sound. Source SHA-256 ae36bfb4ed021576fed203226b0925162ecb0793671dd3b0cd3e6b0fd0ccae5d; ELF SHA-256 fbfca2d8bb78c185221067adf80ac38cc54590e59d7ae459dc994f8bb645bbd9. [Worker source](worker.c) · [Archive](execution-logs.tar.gz) · [Pinned environment](../../clustering/execution.md)

The formal scope includes the measure-theoretic positive-time second-difference inequality, the numerical *implication* from three rational enclosures, the sign of the curvature of a Gaussian heat factor in the indicated interval, mode counts, transverse-projector arithmetic, and the two elementary counterexamples to steps used in the trajectory-identification argument. The high-precision intervals are separately computed, outside Lean. The passage from a compact Wilson measure to a flowed weak-coupling limit, complex analytic uniqueness, and the simple-group two-limit extension are written proofs. The latter is with the other directors for independent review.

Per release the incorrect native callback and five altered conclusions failed: a missing temporal sign, reversed reflection sign, exchanged threshold powers, inverted flow normalization, and an omitted cross term. Draft diagnostics and the early run rejected by the warning/axiom audit are included. The method manifest and all its listed payloads were verified again. [Replay driver](verify.py)

| Independent computation | Inputs, result and scope |
| --- | --- |
| [Finite torus interval sum](check_torus.py) | Uses 35-decimal interval arithmetic with radical cosine values and the exact multiplicities of all $16^4$ modes. At full flow time six the normalized form is below $-0.009862$. Integrating out temporal momentum analytically for spatial flow gives a positive interval above $0.0573332$. No stochastic samples or large-volume limit enter these enclosures. |
| [Momentum and heat-kernel checks](check_spectrum.py) | Four-dimensional Gaussian-weighted angular quadrature agrees with the closed covariance. The infinite-lattice Bessel calculation at radii 4, 8, 16 gives forms $-0.01511610$, $-0.01507400$, $-0.01506353$, against the continuum $-0.01506005$. An independent radial integral matches the zero-momentum density and the method distinguishes the spatial and full magnetic means by $8/3$. |
| [Compact nonlinear link test](check_links.py) | On a periodic $3^3\times6$ quaternion lattice, two configurations agree on every positive-time link and differ only on slice $-1$. With amplitude 0.1 the full flow changes the previously trivial spatial face deficit on slice $+1$ by $2.01165\times10^{-6}$. Spatial flow keeps it trivial. Halving the amplitude reduces the scaled nonlinear-to-linear curvature error from 0.0043780 to 0.0021841. A separate noncommuting link fixture checks gauge equivariance for both flows. This is a deterministic support and linearization test, not a sample from the Wilson vacuum. |

Use a fresh output directory per native run. The numerical checks use Python, NumPy, SciPy and mpmath.
```sh
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
python check_torus.py
python check_spectrum.py
python check_links.py
```
