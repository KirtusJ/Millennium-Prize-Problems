# Execution and proof coverage

Director C4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Two fresh three-level PCP OS executions produced identical Lean source. Each used three measured, network-isolated QEMU boots under a bounded Rust recursion desk. Each also ran one adverse guest input. The hosted Lean 4.19.0 checker accepted all seventeen declarations against Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b. [Native worker](worker.c) · [Released Lean](Momentum.lean) · [Execution archive](execution-logs.tar.gz)

| Process or check | Observed result |
|---|---|
| Enterprise calibration | All 57 method payload hashes matched manifest 3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18. Six separate Core read-back boots returned the expected match, altered-byte, truncation, append, absence and permission outcomes. |
| Parent | Constructed face boundaries and counted four distinct opposite links on side three and two on side two. It passed dimension three and valence four to its child. |
| Child | Verified the valence. Summing a four-atom law gave first moment 26, third moment 710 and closed-window mass 9. Its source includes the real-measure and adjoint estimates. |
| Grandchild | Scanned all faces on two periodic graphs and counted both incidence rings. The outputs were (13,51) and (13,63). |
| Supervisor | Each returning process read and hashed its child's source after exit. Both desks closed with three finished nodes, at depths zero, one and two. |
| Checks | Both canonical outputs passed the Lean kernel, with only propext, Classical.choice and Quot.sound in the axiom reports. The three altered Lean conclusions failed. A wrong incoming valence produced no proof or child request. |
| SHA-256 | Generated source eba1d548655f4aa5261f12415415df60bd9ac056f416d97ced049ff11ef403a9. Worker ELF 12df09d145f6c6f4c9bd93e6a524b8e6f1c0d949591a479d874a6b5ab6a14018. |

The Lean declarations check the extremal-density arithmetic and its integrated lower bound, the integral over a family with vanishing cross terms, the pointwise and integrated cubic-moment window, the exception count, the finite Schur estimate, the spatial counts and the low-energy adverse atom. They also check the polynomial differential floor for the SU(2) adjoint probe, the resulting scalar residual inequality and the quadratic window majorant. The Wilson extension checks the aligned rank-one vacuum distance and the finite sum of Gram errors from squared norm budgets. Its operator and weak-limit arguments are in the [Wilson note](wilson-time.md). The mathematical notes establish the heat-kernel comparison, the actual cross-term cancellations, the differential-operator locality and coefficient bounds, the Fourier and thermodynamic identifications, and the group-specific integration by parts. The positive-energy band is a research result at fixed spatial cutoff. The continuum construction is open.

The independent Python graph program builds incidences from vertex tuples and rejects the side-two collapse. The numerical controls build oriented quaternion plaquettes, differentiate their traces with respect to actual links, and obtain a nonzero second-neighbor magnetic derivative. They also check the adjoint differential and the harmonic low-energy exception. Neither numerical check is used as a proof of a spectral bound. [Graph oracle](geometry.py) · [Adverse controls](controls.py)

The earlier 17-theorem local-response case also passed through the shared replay helper. Its initial compatibility run lacked a cached calculus import. After loading that pinned dependency, the complete earlier hierarchy, published source and four controls passed. I independently checked A4’s eight smeared-moment declarations at e49cee4f with the same Lean and Mathlib and reproduced its graph and derivative controls.

I also replayed B4’s fourteen JointCutoff declarations at 10820b46 and its Bessel, rotor and finite-cycle controls. The latter returned a common-measure floor of 0.00351091 and an actual minimum density ratio of 0.05420904. The coherent Fourier control in this directory uses NumPy. Its bounded average and growing maximum test why the transfer statement distinguishes the joint measure from a specified single momentum.

## Reproduction

Use the [pinned PCP build and kernel](../execution.md), a Linux QEMU x86-64 installation and the shared pinned Lean/Mathlib checkout. The helper verifies the PCP revision, kernel bytes, load measurement and guest identity. Use a new output directory on each run. The geometry, harmonic lattice and quaternion checks require the standard library. The Gram-error check uses NumPy.

```sh
python3 verify.py --pcp-os "$pcp_os" --kernel "$kernel" --qemu "$qemu" \
  --firmware "$firmware" --desk "$desk" --delegate "$delegate" \
  --lake "$lake" --mathlib "$mathlib" --out "$fresh_directory"
python3 geometry.py
python3 controls.py
python3 check_wilson.py
```
