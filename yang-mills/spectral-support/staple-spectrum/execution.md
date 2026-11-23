# Formal coverage and independent checks

Two recursive PCP OS executions each used a three-level hosted desk. The root dispatched a generation worker, which dispatched separate numerical and certificate workers. The numerical worker evaluated the quadratures, recompiled A4's pinned eleven declarations and supplied the lattice-dispersion proof fragment. The certificate worker booted the measured freestanding kernel in QEMU, generated the upper-edge coefficient fragment and returned it over serial. The generation worker booted a second measured guest to assemble the Lean source from the two fragments and a proof template. After child exit the root read back the bytes, checked the source and mutations with the host Lean kernel, and the outer supervisor read back the finished tree. [Replay](replay.py) · [Freestanding worker](certificate.c) · [Post-exit registers, hashes and numerical output](readback.txt)

The host used Lean 4.19.0 and Mathlib at c44e0c8ee63ca166450922a373c7409c5d26b00b. All sixteen reported declarations use only propext, Classical.choice and Quot.sound. The scalar moment reconstruction is proved for arbitrary probability measures on the closed unit interval. It includes polynomial convergence and uniform approximation for every bounded continuous test. Other declarations verify the transfer-step offset, full-staggering algebra, two hyperbolic dispersion inequalities, polarization-shell integrals and edge normalization factors. Five adverse variants per execution target the missing adjacent factor, a doubled upper-edge density, a nonvanishing staggered factor, an incorrect transverse polarization average, and a halved energy ceiling. [Formal source](StapleSpectrum.lean)

The Wilson fixed-patch convergence, simultaneous translation spectral calculus, momentum fiber support, six-dimensional radial density, large-packet estimate, and trajectory selection are written mathematical arguments. Independent recompilation of A4's formal module covers the conditional integration and scalar identities in that module. The scoped result here relies on the cited Wilson tangent and moment theorems. The separately requested Fidelity Audit Lab exposed no callable interface in this session. The recorded checks used the enterprise PCP workflow, measured PCP OS guests and the pinned host Lean kernel.

After A4 published the bounded six-trace replacement at fae562d, a separate host replay checked all twelve declarations of its Abel reconstruction module and reran its one-link forward/inverse quadrature. Its exact boundary-kernel identity carries the results here over to that ordinary-trace reading. The numerical checks use sampled staple radii. [Supplemental read-back](readback.txt)

The independent controls included the following measurements.

- Two actual adjacent Wilson Haar fibers with noncommuting boundary links shared the middle spatial slice. The largest conditional double-insertion residual was $2.7\times10^{-14}$. This checks normalization before integrating the remaining exterior.
- On a five-by-five-by-five momentum grid, direct contraction of complex six-face matrices agreed with the two transverse projectors within $3.1\times10^{-18}$. Three time and spatial displacements reproduced the position-space covariance. Removing the adjacent propagation factor changed the first reading by a factor of 53.56 on this grid.
- In the limiting integral the full-staggering weight was below $4\times10^{-37}$ numerically; its exact zero follows algebraically. Energy bands with one or two surviving coordinate directions retained positive weight. Three directions of approach gave the predicted quadratic suppression.
- A normalized finite binomial packet at order 256 gave 0.99957 for the ratio to the derived large-width coefficient. Independent time integration at zero momentum gave 1.0000763 for the ratio to the predicted $n^{-5}$ term at lag 128.
- The six-dimensional integral over energy deficits at most 0.0025 gave 1.000319 for the ratio to the upper-edge cumulative coefficient. Direct shell integration at three nonzero momentum-to-energy ratios checked both polarization terms of the continuum density.

Only the adjacent-link control integrates original conditional Wilson variables. The spectral quadratures evaluate the limiting integral. The measured packet numbers give no cutoff error bound for Monte Carlo data. [Controls](controls.py) · [Detailed read-back](readback.txt)

To reproduce, use the pinned tools and base guest from the [shared PCP setup](../../transfer-operator/pcp/), with the Mathlib dependencies of StapleSpectrum.lean built and NumPy and SciPy available.

~~~sh
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 replay.py /path/to/base /path/to/pcp-os /path/to/new-run
~~~
