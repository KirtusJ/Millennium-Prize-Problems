# Certificates and reproduction

The spatial graph and its compact-transfer interpretation use B4's static limit on contractible spatial cubes. D4 recompiled all 17 declarations in B4's girth-shell module from commit 303687f. The patch extension, packing, min–max argument, area upper bound and order of limits are given in the mathematical notes. [B4's original reduction](../../transfer-operator/girth-shell/open-box.md) · [Boundary count](README.md)

The first of three nested PCP OS workers inverted the grounded 64-site patch Laplacian modulo 101 and computed the weighted square of its curvature projector over all 176 faces. The child repeated the full calculation modulo 193. The two boots supplied the residues of the corner Green entry, the squared trial norm and the unnormalized energy. These were 42, 46, 37 and 149, 121, 151, respectively. The grandchild assembled the analytic source and measured comparisons. A fresh replay reproduced the 45,505-byte module and all ten predecessor modes. The cumulative register verified 1,442 events, with all 711 admissions released. All three ran the pinned measured kernel. The microVM skipped its asynchronous keyboard tests. [Serial receipts and register](evidence/) · [Kernel measurement and calibration](../execution.md)

Lean checked all 43 theorems, including 26 individual integer row certificates and 17 reported declarations. The axiom reports contain only subsets of propext, Classical.choice and Quot.sound. Eight deliberate changes failed at their respective declarations. Hosted Lean 4.19.0 uses Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b. The module proves positivity of the entrywise product of two real Gram kernels, the row-energy and area algebra, and a finite counting inequality. For the 26 patch face orbits it checks the integer potential equation at every site, computes each weighted squared row and sums the contributions. It also checks the face layout, squared norm, the small-patch quotient, the two Green-entry inequalities for the edge and corner, the closed-walk arithmetic for the larger patch and the native modular results. The geometric equality of each orbit under square symmetries and the identification with the original compact measure use the mathematical derivations. [Lean source](BoundarySpectrum.lean) · [Return-walk argument](surface-series.md)

One host calculation forms the full integer-scaled inverse and checks its product against the identity. Another uses 112 independent triangular cycles through ground and the trace of a weighted cycle Gram product. They return the same exact rational Rayleigh quotient. Numerical whole-box diagonalizations check the three thresholds for sides 2, 3, 5, 8 and 10. At side 10 they find 182, 140 and 20 eigenvalues above the listed thresholds. Periodic Gaussian controls on sides 3 and 4 give the predicted norm. The eigenvalue counts in the theorem use the exact trial, projection comparison and counting bound. [Recorded checks and hashes](evidence/checks.txt)

Use the baseline's kernel and PCP OS checkout. LANE denotes the absolute spectral-support directory, and MATHLIB denotes the pinned Mathlib checkout. Put the matching Lean and Lake binaries on PATH. Python calculations use SymPy, SciPy and NumPy. Each replay recomputes native readings and compares the generated file byte for byte.

~~~sh
export OPENBLAS_NUM_THREADS=1
python -I "$LANE/positive-time/replay.py" --boundary-spectrum --kernel "$KERNEL" --pcp-source "$PCP_SRC"
(cd "$MATHLIB" && lake env lean "$LANE/boundary-spectrum/BoundarySpectrum.lean")
for check in patch cycles series counts; do
  python -I "$LANE/boundary-spectrum/check_$check.py"
done
python -I "$LANE/boundary-spectrum/check_mutations.py" --mathlib "$MATHLIB"
~~~
