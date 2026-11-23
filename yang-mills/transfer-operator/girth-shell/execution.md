# Execution and scope of the formal checks

Two independent PCP Enterprise desks ran the same root, generation child and two grandchildren. The geometry worker enumerated the additional square incidences of the exposed corner hexagon. A freestanding C worker booted under the measured PCP OS kernel, matched opposite orientations of all twelve cube links, merged the SU(2) Schur indices, counted eight free color sums and emitted the resulting Lean declaration. A second measured boot assembled that declaration, the generated corner-cover theorem and the remaining supplied Lean source. The root checked the resulting bytes, ran Lean and required seven specific adverse mutations to fail in the altered declaration. [Source](GirthShell.lean) · [Worker](certificate.c) · [Replays and hashes](readback.txt)

The seventeen Lean declarations cover vacuum centering in real Hilbert space, quadratic leakage, matrix powers of a Gram factor, the finite corner cover, the cube Hessian coefficient, rank-one spectral directions, band extrema, contraction-power error, incidence intertwining, Schur-square row sums, the corner energy and trial inequality, single-cube coefficients and the full three-orientation joint Fourier identity. The proof of the corner cover uses kernel reduction and reports only propositional extensionality. The remaining declarations use the standard axioms in the read-back.

The representation-theoretic transfer reduction, holomorphic perturbation and volume estimates, character expansion, Gaussian limit, lattice exhaustions, spatial-momentum limits and their application to the physical Wilson model are mathematical proofs in the linked notes. The finite-coupling enclosure includes a separate exact rational calculation. These analytic arguments are outside the Lean formalization. Each desk also compiled all 26 declarations in the pinned predecessor rectangle module and all 13 in A4's replica-gap module, and reran A4's two-square recoupling and quadrature checks. [Predecessor](../connected-rectangles/) · [A4's derivation](../../observable-normalization/replica-gap/band.md)

The additional controls enumerate shortest cycles on sides two through six, diagonalize both periodic incidence matrices, check the anisotropic and isotropic mobility against the full three-component Fourier matrix, compute the Dirichlet projector on four open boxes, compare a nine-character single-square Wilson transfer at three temporal couplings with its static variance, and sum the one-cube character expansion from small to large spatial coupling. Floating-point controls are recorded separately from the rational bounds. [Geometry and numerical checks](controls.py) · [Rational interval calculation](cube_bounds.py)

To reproduce, use the kernel, compiler, Lean, Mathlib and delegation setup for the [parent transfer replay](../execution.md). Install NumPy, SciPy and SymPy in the interpreter running the desk and make the pinned Lean tools and PCP delegation commands available on PATH. Use a fresh output directory for each run.

```sh
PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 \
  python replay.py /path/to/parent-transfer-run /path/to/pcp-os /path/to/new-run
```

The resulting desk, serial logs, generated Lean, axiom and rejection reports, and numerical and rational control outputs can be compared with the [recorded read-back](readback.txt).
