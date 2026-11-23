# Measured generation and independent checks

Director D4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The three registered PCP OS stages were actual nested supervisor processes. Each booted a fresh kernel with a measured freestanding guest, 32 MiB, one emulated x86-64 CPU and no network. D4 supplied the analytic template and the guest program. The parent took the four-link plaquette length and calculated the two electric exponents. The child computed the four scaled diagonal and off-diagonal entries in integer arithmetic from those exponents. The grandchild read the analytic source and certificate through separate guest inputs and assembled the module. The supervisor verified each loader measurement, guest digest and exit before consuming the output. [Guest code](guest.h) · [Recorded register](evidence/register.jsonl)

| Worker | Output |
|---|---|
| T170, parent | Fundamental and adjoint electric exponents 3 and 8. [Boot record](evidence/factor.serial.txt) |
| T171, child | Signed diagonal and cross-channel numerators at four consecutive times. [Boot record](evidence/moments.serial.txt) |
| T172, grandchild | The complete 19,442-byte Lean source. [Boot record](evidence/assemble.serial.txt) |

The admitted guest ELF has SHA-256 974b4663a8f26a4b11868e967c4e0a3bda96b766e9b9d1a022113a180b71450d. The resulting Lean source has SHA-256 029ce009e020212b7f7dbd45bcb574b80a7e831c2de8bf137eda55c9857aee68. A separate replay regenerated the same ELF and Lean bytes. All three previous positive-time runner modes also reproduced their recorded ELF and source bytes. Serial hashes can differ across boots. The register extends the preceding 266-event record byte for byte. All 187 admissions in its 387 events have matching releases, and native guard replay found zero problems. The coordinator relayed the Principal’s standing commission, as documented in the original actor receipt. The Linux host ran Lean 4.19.0 against Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b. Its 31 axiom reports used only propext, Classical.choice and Quot.sound. [Lean source](FiniteReadings.lean) · [Verified kernel and ISO](../execution.md) · [Outputs and hashes](evidence/checks.txt)

## Scope of verification

Lean proves the existence of a Gram-selfadjoint representative for a pair of complex matrix forms with the stated positivity bounds, including singular Gram matrices. It checks the shift-power identities and moment recovery, the open-interval mass detector, propagation of three errors, all-even-order interval exclusion, the local kinetic inequality from its two premises, the spectral residual tail inequality, and the scalar weak-coupling and positive-time margins. It also verifies the factorial product, Rayleigh normalization, gap-error directions, four exact Sturm counts, nonvanishing of the associated leading minors, and the exact rational truncation allowance for the isolated square. The Hilbert-space and gauge-theory identifications, endpoint completion and compactness arguments, Sylvester comparison, hopping support, and many-link min–max proof are given in the mathematical notes. The three guest processes implement D4’s calculation and supply reproducible execution evidence.

The matrix implementation accepts exact rational real and imaginary parts. For each accepted trial the checker compares every time entry of the returned realization, with genuinely singular probe spaces among the controls. The Schur and endpoint constructions agreed on all 36 additional complex rational trials. Replays of an isolated cycle at two character truncations check the commutator and spectral windows. A coupled two-label calculation tests a four-dimensional low-energy subspace. A direct jump by two labels breaks the nearest-label induction, as expected. The numerical models and the rational one-cycle enclosure have different evidentiary scopes. [Matrix controls](check_moments.py) · [Cycle controls](check_loops.py) · [Ritz controls](check_spin.py)

Seven altered Lean modules exercise the null-space condition, sharp quadratic coefficient, local kinetic constant, polarization sign, inertia, truncation allowance and positive-time margin. An early complex-matrix replay exposed an unevaluated Gaussian-rational pivot. Expanding exactly before sign comparison fixed the implementation and the entire suite passed. An early proof of the rational truncation allowance did not reduce in Lean. The final proof computes the integer denominators first and checks the resulting rational identity. Fresh processes also checked B4’s fourteen blocked-time declarations and reproduced the spatial incidence rows $(16,24,16)$ on periods two through five. These are independent checks of the indicated formal and computational steps. [False mutations](check_mutations.py) · [B4’s reviewed revision](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/5d25ad9cb284bb001325eaa4bea2f16b82736c6c/yang-mills/transfer-operator/blocked-time)

## Reproduction

Set LANE to the absolute spectral-support directory, KERNEL to the kernel ELF from the pinned ISO, PCP_SRC to the pinned PCP OS source, and MATHLIB to the stated Mathlib checkout. Put the pinned Lean toolchain on PATH. The native replay accepts a QEMU executable and a firmware directory if needed. The dispatcher and register options enable process-level admissions on an authorized register. The exact matrix checker uses SymPy and the numerical controls use NumPy and SciPy. [Shared native driver](../positive-time/replay.py) · [Toolchain and image pins](../execution.md)

~~~sh
python3 -I "$LANE/positive-time/replay.py" --finite-readings --kernel "$KERNEL" --pcp-source "$PCP_SRC"
cd "$MATHLIB"
lake exe cache get Mathlib/LinearAlgebra/Matrix/PosDef.lean Mathlib/LinearAlgebra/Basis/VectorSpace.lean Mathlib/MeasureTheory/Integral/Bochner/Set.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean Mathlib/Tactic/NormNum.lean
lake env lean "$LANE/finite-readings/FiniteReadings.lean"
python3 -I "$LANE/finite-readings/check_mutations.py" --mathlib "$MATHLIB"
python3 -I "$LANE/finite-readings/check_moments.py"
OPENBLAS_NUM_THREADS=1 python3 -I "$LANE/finite-readings/check_loops.py"
OPENBLAS_NUM_THREADS=1 python3 -I "$LANE/finite-readings/check_spin.py"
~~~
