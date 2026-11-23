# Execution and scope of the checks

Three recursively dispatched PCP OS workers ran at depths zero, one and two. The first native guest derived the twelve incident-face masks from the three axes of a six-link star. Its child used those bytes to enumerate the flat twists, allowed electric outcomes and magnetic-clock rates. The third guest combined the generated certificate with D4's analytic Lean text and emitted the complete module. Each worker booted a separate measured instance of the pinned kernel. The Linux host ran the proof checker. These workers share D4's authorship; their separate processes establish reproducibility. [Parent serial](evidence/factor.serial.txt) · [Child serial](evidence/flux.serial.txt) · [Assembly serial](evidence/assemble.serial.txt) · [Native guest](guest.h)

The final ELF has SHA-256 `9a0c055625830f7377cbd54bbc3e4e2fa0e86d23df35bb5a471160673c69381c`. A separate rebuild reproduced the complete 9,001-byte Lean source, SHA-256 `d8b44086b7234ac94b9d4acb4d71c868b8a888ddb3645d4ac0e3962295bcd792`. The four older generator modes reproduced their published modules. The host used Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`. All 17 Lean reports used only the standard axioms shown in the evidence. The cumulative register continues the preceding 387 events byte for byte. [Checks and hashes](evidence/checks.txt) · [Register](evidence/register.jsonl) · [Earlier register](../finite-readings/evidence/register.jsonl) · [Kernel identity and ISO](../execution.md)

## What Lean and the independent controls checked

Lean proves the adjacent-shell ground-state transform and a full prefix variational bound from a positive vector satisfying the row equations. It checks the endpoint algebra, shell probability variation, energy scaling, center anticommutation implication for expectation values, integrated low-energy spectral tail estimate and its relative-error constant, and the lower bound on a Laplace reading from its mass and first moment. The kernel checks the emitted star kernel, 32 allowed outcomes, four rates, and their multiplicities by finite computation. The identification of the spherical harmonics, compactness and entropy arguments, link-gauge twirl, gauge-theory residual, class-probe covariance and continuum-limit qualifications are mathematical proofs in the accompanying notes. [Lean module](ElectricScale.lean)

A separate cubic enumerator built oriented faces on tori of side 3, 4 and 7. Diagonalizing the 32-state Markov generator recovered the same spectrum. Two-interval correlation words and all 64 twist characters agreed with the spectral prediction. A group-matrix control checked the potential error for three groups. Numerical Gegenbauer quadrature checked seven angular sectors, including nonradial harmonics; five matrix sizes distinguished free and hard endpoints. A four-edge one-cycle model tested the spin tails, degeneracies of the reduced density, and the normalized center and class-probe correlations across four couplings. It has one affected face, while a link in the cubic theorem has four. These computations test the formulas and limits; the volume-uniform estimates use the analytic arguments. Four false modifications failed at the intended Lean declarations. [Shell and class-probe checks](check_shells.py) · [Center checks](check_center.py) · [Proof mutations](check_mutations.py)

## Reproduction

Use the kernel ELF and PCP source pinned in the [original execution record](../execution.md). Set LANE to the absolute spectral-support directory, and MATHLIB to the pinned checkout with its dependencies compiled. Put its Lean toolchain on PATH. Numeric controls require NumPy and SciPy.

```sh
python -I "$LANE/positive-time/replay.py" --electric-scale --kernel "$KERNEL" --pcp-source "$PCP_SRC"
(cd "$MATHLIB" && lake env lean "$LANE/electric-scale/ElectricScale.lean")
python -I "$LANE/electric-scale/check_shells.py"
python -I "$LANE/electric-scale/check_center.py"
python -I "$LANE/electric-scale/check_mutations.py" --mathlib "$MATHLIB"
```

The driver also accepts a QEMU executable and firmware directory. Supplying the dispatcher and an adopted register records admissions for the child hierarchy. Replaying the generator compares its mathematical output byte for byte. Wall-clock fields in serial receipts can differ between boots. [Shared driver](../positive-time/replay.py)
