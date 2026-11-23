# D4 execution and replay

Director D4 · 22 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The PCP OS guest emitted 6,518 bytes of Lean source. The final Linux-hosted Lean process exited 0. The five analytic and endpoint declarations list `propext`, `Classical.choice` and `Quot.sound`. The finite certificate lists only `propext`. D4 supplied the analytic proof text. The freestanding guest read it through the PCP OS file API, computed the seven integer weight corrections, constructed the finite certificate and emitted the assembled file over serial. This gives the provenance of each part. [Lean declarations](SpectralLimit.lean) · [Axiom output](evidence/lean.txt) · [Guest source](emit_e1.c)

| Item | Observed identity |
|---|---|
| Published ISO | Git blob `83d782f0b786d604c72a9d86c860e2f7c892d2a5` |
| Kernel from ISO member `/KERNEL.ELF32;1` | SHA-256 `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Kernel text and read-only data measured at boot | `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3` |
| Admitted guest ELF | SHA-256 `2f920f7d9dd19e99b2807e614b4565dbefb3a74096786857ad490179288359bd` |
| Assembled Lean source | SHA-256 `bc65f44f95de9855558b34c2a523a0768df41139a7297e887cfddecba52e3cb4` |
| Proof-generation serial transcript | SHA-256 `195a225628d86a70ed531f264db795efa2767e39442327bd4538f84290db82ee` |
| QEMU, compiler and linker | QEMU 10.0.13 TCG, GCC 14.2.0 and GNU ld 2.44 |
| Lean and Mathlib | Lean 4.24.0 `797c613eb9b6d4ec95db23e3e00af9ac6657f24b`, Mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7` with upstream compiled dependencies |

The boot used one emulated x86-64 CPU, 32 MiB of RAM, a measured multiboot kernel and no network interface. The guest exited 0 and QEMU returned 33 through the configured debug-exit device. The microVM lacks a keyboard controller, and the kernel reported that it skipped asynchronous self-tests. A fresh replay regenerated the committed bytes. [Boot transcript](evidence/native-boot.txt) · [Published ISO](https://github.com/KirtusJ/pcp/blob/983fc4a45dbbada52b507dd0e413b9f7d3ca0c9d/PCP-OS.iso)

## Worker and method checks

A Linux PCP OS 1.0.22 register admitted real processes to depth two before execution. The final read-back found 85 events and zero replayed guard problems. All 39 admissions were released. The final head is `b305389838afb7bc0aeaf0a949d747769a3d57fa5c1561efc4fcc6e30118aaf3`. The root launched its child, which launched the grandchild. The register-mode launcher used the published admission, wait and release routine with a register-only entry point. The ELF ran inside a fresh PCP kernel. Lean and the exact rational checker ran under Linux. These workers contributed executions of D4’s construction. Independent scientific assessment requires a separate reviewer. The register initializer tags the local coordinator as a declared human principal. D4 is an assistant and relayed Kirtus Justus’s commission. The tag supplies no evidence of a human terminal action. [Register](evidence/register.jsonl) · [Published worker routine](https://github.com/KirtusJ/pcp-os/blob/59f26ebe6397e00e8a9b8cce08487ad8a5319c0c/store/apps/parrots-all-the-way-down/host/src/bin/pcp-delegate.rs)

The packaged Enterprise inspector matched its pinned binary SHA-256 `dd68d895f11fa419f5508377106d18a2beeda0676c6441c017d987b5b8aaf93a`. Both Enterprise method copies use manifest `3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18`. The separate Build 22 host package used manifest `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707`. Its 58-file check and the Enterprise 57-file checks each found all listed files present and equal. The Fidelity Audit Lab’s older Core R13 and Mathematics R5 were inspected as distinct reference identities. The Build 22 register selected Core and Mathematics.

Fresh Enterprise guest read-backs accepted the exact Core, detected a last-byte change, truncation and appended content, and distinguished absence from denied access. In a separate fresh 22-question Build 22 retrieval check, D4 used programmatic clause and defined-term lookups. The scorer credited ten exact provisions, four defined terms and eight absent provisions or terms. It recorded zero inventions and zero unscored answers. This measures tool-assisted retrieval. Behavioral application has no independent assessment here.

## Adverse checks and corrections

| Change to the final Lean source | Observed result |
|---|---|
| Reverse the physical-time inequality | Lean rejects the final exponential comparison. Mathematically, zero steps cannot certify decay at positive time for a positive rate. |
| Include the endpoint in the excluded spectral tail | Lean rejects the countable-cover argument. The checked point-mass theorem supplies the counterexample. |
| Increase the energy-1 alternative weight from 90 to 91 | Lean rejects the finite certificate. Even the total numerator changes from 600 to 601. |

Earlier attempts exposed a missing firmware path, a missing C termination annotation, and an unsupported use of the Lean positivity tactic for the cutoff cover. The successful run used the firmware files, a nonreturning exit declaration and explicit addition of a positive quantity. The first mutation harness also expected different wording for the arithmetic diagnostic. The corrected harness matched the actual rejection for each mutation. The final proof has no admitted results. D4 did not replay either large RH or Navier–Stokes development. Their external verification records and claim scopes are recorded in the project rendezvous. [Opening dispositions](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/pull/293#issuecomment-7090676766)

## Replay

Use the kernel from the ISO above and the pinned PCP OS source checkout. The script rebuilds the guest, verifies its admitted hash and exit, decodes the serial frames and compares all emitted bytes with the committed Lean file. Set `LANE`, `KERNEL`, `PCP_SRC`, and `MATHLIB` to the corresponding absolute paths. On distributions with split firmware, pass `--firmware` and a directory containing the microVM BIOS and multiboot ROM. Use Lean 4.24.0 on the executable search path for the last commands. [Replay script](replay_native.py) · [PCP OS source](https://github.com/KirtusJ/pcp-os/tree/92623fa6759bbb4e4f27ce5aa381de213a55ae0c) · [Mathlib revision](https://github.com/leanprover-community/mathlib4/tree/f897ebcf72cd16f89ab4577d0c826cd14afaafc7)

```sh
python3 -I "$LANE/replay_native.py" --kernel "$KERNEL" --pcp-source "$PCP_SRC"
python3 -I "$LANE/check_family.py"
cd "$MATHLIB"
lake exe cache get Mathlib/MeasureTheory/Integral/Bochner/Set.lean Mathlib/Analysis/SpecificLimits/Basic.lean Mathlib/Analysis/SpecialFunctions/Exp.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Positivity.lean
lake env lean "$LANE/SpectralLimit.lean"
```
