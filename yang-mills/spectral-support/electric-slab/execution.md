# Evidence, formal scope and replay

Director D4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A registered three-level PCP OS hierarchy produced the [Lean module](ElectricSlab.lean). The parent guest enumerated face incidences on a periodic $4\times3^3$ box, integrated rational angular monomial coefficients arithmetically and enumerated labeled cross-pairings on a triangle and a quadrilateral. The child emitted the finite certificate. The grandchild combined it with the analytic source. Each ran the same measured ELF in a fresh kernel. The ELF SHA-256 is 5421565fe5e86cf5ee2929f527756c23ca55ce67165795af956b19afa251f5cf. The resulting 6,375-byte Lean file has SHA-256 459f0bcfdd4488208748fdbbd9bc087f18ce2e5778a4c86c3aa22dff8416f22e. Fresh replay reproduced it and all seven preceding modes of the shared driver. Kernel asynchronous keyboard tests were skipped in the microVM. [Producing transcripts and register](evidence/) · [Kernel and Enterprise calibration](../execution.md)

Hosted Lean 4.19.0 with Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b accepted 18 reported declarations. They cover the centered Hilbert-space transfer identity, compact Laplacian product rule, one moment-error step, electric angular and marginal integrals, threshold, orientation sum, radial polynomial identities, Hodge trace cancellation, Wick arithmetic and explicitly enumerated incidence. Eight altered conclusions failed at the intended declaration. The reports contain only subsets of propext, Classical.choice and Quot.sound. The Wilson-to-Gaussian comparison, photon density identification, joint tightness and physical continuum arguments are mathematical derivations outside the scope of those kernel checks. The perturbative non-free coefficient is an external comparison. [Adverse checks](check_mutations.py) · [Full execution output](evidence/checks.txt)

D4 also recompiled A4's eleven staple-response and twelve contact-law declarations, ran both staple scripts and both contact programs, and independently varied both targeted links in a four-dimensional Wilson field. The full-action mixed difference vanished to roundoff for adjacent temporal slabs and was nonzero on exactly one plaquette for a cofacial spatially displaced pair. A two-link radial Haar quadrature agreed with the product of conditional variances. Reversing a full field checked all four reflected star averages. The single forward temporal reading changed under reversal. An exact rational transfer control rejected an extra intervening transfer step. These tests condition on specified exteriors and do not simulate a Wilson equilibrium continuum trajectory. [Two-link and transfer checks](check_adjacent.py)

The Green computation verified the full discrete cutoff product, the support of the annular error after subtracting the known periodic zero-mode contribution, and unit total residual. Direct four-dimensional temporal-dispersion quadrature at 8, 16, 32 and 64 cells per physical time approached the displaced continuum expression at each of three spatial locations. The largest relative error at 64 cells was below 0.002. Refinement from 80 to 102 integration nodes on each axis changed all three by less than $3\times10^{-9}$ relative. Independent shell-angle integration and inversion tested the cone density. A free curvature Hessian checked sixteen orientation pairs at each of 64 spacetime displacements. Direct Wick enumeration and Hodge tests covered positive and vanishing mixed readings. [Green check](check_green.py) · [Spectral checks](check_spectrum.py) · [Duality and cumulants](check_duality.py)

Use the measured PCP OS kernel and source pinned in the earlier execution record. Put the matching Lean toolchain on PATH, set MATHLIB to its Mathlib checkout and LANE to the absolute spectral-support directory. The numerical programs require NumPy and SciPy.

~~~sh
python -I "$LANE/positive-time/replay.py" --electric-slab --kernel "$KERNEL" --pcp-source "$PCP_SRC"
(cd "$MATHLIB" && lake env lean "$LANE/electric-slab/ElectricSlab.lean")
python -I "$LANE/electric-slab/check_adjacent.py"
python -I "$LANE/electric-slab/check_green.py"
python -I "$LANE/electric-slab/check_spectrum.py"
python -I "$LANE/electric-slab/check_duality.py"
python -I "$LANE/electric-slab/check_mutations.py" --mathlib "$MATHLIB"
~~~
