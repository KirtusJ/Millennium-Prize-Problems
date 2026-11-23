# Replay and scope of the checked proof

Director D4 · November 22, 2026

Three nested PCP OS workers produced the 9,637-byte Lean module. The parent selected the two polynomial coefficients from the sphere dimension. Its child calculated the divergence polynomial, and its grandchild combined that certificate with D4’s analytic Lean template. Each registered supervisor booted a fresh measured kernel with the same freestanding guest. The host passed verified output bytes to the next guest and finally ran Lean 4.19.0 against Mathlib at c44e0c8ee63ca166450922a373c7409c5d26b00b. The 13 declarations passed with only propext, Classical.choice and Quot.sound among their dependencies. [Lean source](AdjointBand.lean) · [Actual outputs](evidence/checks.txt)

| Registered stage | Input and output |
|---|---|
| T113, parent | Dimension 3 produced coefficient bytes 03 03 04. [Boot transcript](evidence/factor.serial.txt) |
| T114, child | Integer polynomial arithmetic produced the divergence identity with coefficient 8. [Boot transcript](evidence/divergence.serial.txt) |
| T115, grandchild | The analytic template and generated certificate arrived as distinct boot inputs. The guest appended the declarations for inspection. [Boot transcript](evidence/assemble.serial.txt) |

The guest ELF SHA-256 is 215b28f7d03d4f722a75bc86123ecdb6966b1d9f9a49865ad1ff6b1e13d32128. The source SHA-256 is e03ee1d3bef8f6fca3b41b74e08c2f70bdbc524a63161a68633c0bdd1ecef508. The 266-event record extends the previous 193 events byte for byte. All 127 task admissions have matching releases, and the PCP OS 1.0.22 verifier reported zero guard problems. The recorded actor relays the Principal’s standing commission. Its declared role is described in the original execution record. [Register](evidence/register.jsonl) · [Kernel image, source pin and role receipt](../execution.md)

Lean checks the scalar implications of the one-link divergence, the two-character identity, the square commutator in an arbitrary ring, the graph-norm implication, the local magnetic count, the measure inequalities for finite measures on the line, the selection theorem for countable real readings, and its prescribed-diagonal counterexample. The Haar integrations, Hamiltonian domains, geometric derivative identities, transfer identification and application of weak convergence are proved in the accompanying mathematical notes. The signed-error tests altered the divergence coefficient, overclaimed a band weight, reversed temporal refinement and tripled the first-moment floor. Lean rejected all four. For the overclaimed weight, a unit atom at energy one with both moments equal to one is an explicit counterexample. [Band proof](README.md) · [Wilson limit](wilson-limit.md)

The quaternion control samples twelve configurations on each of periods three and four. The character rotor uses independent truncations for six couplings from zero to 65,536. At the largest coupling the 72-character truncation missed the product-rule tolerance. With 120 and 160 characters the two moment calculations agreed at the original tolerances and the 160-character product-rule residual was below $6\times10^{-10}$. These controls check the local differential identities and a solvable one-plaquette model. The spectral theorem for the interacting cubic boxes is the analytic calculation. [Local checker](check_local.py) · [Independent magnetic-order control](check_resolvents.py)

## Reproduction

Use the [pinned kernel, ISO and PCP OS checkout](../execution.md), a C compiler, GNU ld and QEMU with microVM support. Each stage runs with one emulated processor, 32 MiB and the network disabled. Point LANE at the spectral-support directory, KERNEL at the kernel ELF extracted from the ISO, PCP_SRC at the pinned source checkout, and MATHLIB at the pinned Mathlib checkout with Lean 4.19.0. For installations with split QEMU firmware pass the firmware directory to the native replay. The optional dispatcher and register arguments associate each supervisor with its native admission and release. [Shared replay driver](../positive-time/replay.py) · [Guest implementation](guest.h) · [Mathlib revision](https://github.com/leanprover-community/mathlib4/tree/c44e0c8ee63ca166450922a373c7409c5d26b00b)

~~~sh
python3 -I "$LANE/positive-time/replay.py" --adjoint --kernel "$KERNEL" --pcp-source "$PCP_SRC"
cd "$MATHLIB"
lake exe cache get Mathlib/MeasureTheory/Integral/Bochner/Set.lean Mathlib/Analysis/SpecialFunctions/Exp.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/FieldSimp.lean Mathlib/Tactic/NoncommRing.lean Mathlib/Tactic/Ring.lean
lake env lean "$LANE/adjoint-band/AdjointBand.lean"
OPENBLAS_NUM_THREADS=1 python3 -I "$LANE/adjoint-band/check_local.py"
OPENBLAS_NUM_THREADS=1 python3 -I "$LANE/adjoint-band/check_resolvents.py"
~~~

Both previous positive-time modes also regenerated their original guest ELF and Lean files byte for byte. Serial transcripts from distinct boots may differ. The committed transcripts are from the recorded T113–T115 run.
