# Execution record

Director B4 · 22 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The reviewed source is `TwoSector.lean`, 6,143 bytes, SHA-256 `34fd029c08d52376f97452fc27e93cb60d9e92738210401de4b2a6921f985b1b`. Two deterministic PCP OS guests generated the proof bodies for `comparison_iff` and `no_uniform_floor`. A third guest assembled those bodies with the supplied statements and supporting proofs. The supervisor checked the emitted file byte for byte and passed it to Linux-hosted Lean 4.19.0, revision `6caaee842e94`, using mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` and its upstream cache. The guests ran a small freestanding program using prescribed proof templates and finite witness searches. Lean kernel checking ran on the host.

## Boot and method

| Input or check | Observed result |
|---|---|
| Enterprise inspection binary | SHA-256 `dd68d895f11fa419f5508377106d18a2beeda0676c6441c017d987b5b8aaf93a`; 57 of 57 listed method files matched manifest `3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18`. |
| Core and Mathematics 1.0 | Core specification SHA-256 `39efd83b4122545455124f20420f212590a06064f391b259e93ea968449e6b7f`; Mathematics `8c5009a8b6a610fb03ae4fe1e25d4674e0d256c9593885fb03b8159e580463f1`. |
| Public ISO and kernel | ISO `93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15`; kernel file `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. The complete kernel bytes occurred once in the verified ISO. |
| Guest image measurement | `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3` agreed in the boot serial with the independently computed loader value. |
| Six fresh Core read-backs | Exact file matched. Changed final byte, missing final byte and appended byte produced DIFFERENT. Absent file produced MISSING and denied access produced DENIED. All six expected guest exits matched. |
| Runtime limits | QEMU 10.0.13, x86-64 TCG microvm, 32 MiB, networking disabled. The boot serial records that asynchronous keyboard tests were skipped because this configuration has no keyboard controller. No physical machine or language-model comprehension was assessed. |

## Three-level worker hierarchy

The Rust PCP recursion desk admitted a root supervisor, its generation worker and that worker’s two children. Each child started a fresh PCP OS kernel and emitted a proof body. After reading back the child outputs, the generation worker started the assembly guest. The root read back the assembled result after the generation worker exited. The four desk nodes reached `Finished`, at revision 8 with no live workers. The hierarchy used host-supervised guests. All three guests used the same ELF, SHA-256 `1cb649a9954be008a7f74ada3fb1494f1949d7947b85bf221875c655ea59afcd`. The byte identity and exit of each worker were checked.

| Guest | Output bytes | Raw serial SHA-256 from the recorded run |
|---|---:|---|
| Comparison proof | 607 | `0e14a011129c2a4514544f9eee1cde3cadb7c0433399fbb8e3e80aecd877726f` |
| Collapse proof | 319 | `cd8d760248dd249f50ddc404aebe51e3c5a230d9181863f4193a9c13d9b83e89` |
| Assembled Lean source | 6,143 | `159f908ac3ad4d1b0c3468643795b7cdcd3c4986016f1cfa7e4fa5bf37cd77f5` |

Lean exited 0. Each of the nine declarations in the file reported exactly `propext`, `Classical.choice` and `Quot.sound`. A copy changing the necessity witness from $c$ to $-c$ failed at the type check for the pivot identity. A copy replacing the strict scale $m/3$ with $m/2$ failed at the final contradiction. The first development attempt at the complex inner product used the wrong notation for this mathlib release and failed elaboration. The recorded source uses the release’s scoped notation.

## Reproduce

Use the public ISO at the pinned PCP revision, PCP OS source at `92623fa6759bbb4e4f27ce5aa381de213a55ae0c`, the stated mathlib checkout, and the matching Lean toolchain. Install the two Rust recursion-desk commands from the pinned PCP OS source. The runner uses Python 3, a C compiler, GNU ld, QEMU and Lake. This example assumes that `ISO`, `PCP` and `MATHLIB` point to your local files and checkouts.

```sh
xorriso -osirrox on -indev "$ISO" -extract /kernel.elf32 kernel.elf32
cargo install --locked --path "$PCP/store/apps/parrots-all-the-way-down/host"
(cd "$MATHLIB" && lake exe cache get Mathlib/Analysis/InnerProductSpace/Basic.lean Mathlib/Analysis/SpecialFunctions/Log/Basic.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean)
python3 pcp/replay.py --pcp "$PCP" --mathlib "$MATHLIB" --kernel kernel.elf32 --out replay-output
```

Use a fresh output directory. Optional `--qemu` and `--firmware` arguments select local installations. The runner retains each serial, regenerated proof, Lean output from the positive and adverse cases, and the closed desk record. The bare Lean file can also be checked from the pinned mathlib workspace with `lake env lean /absolute/path/to/TwoSector.lean`. [ISO and published checks](https://github.com/KirtusJ/pcp-os/blob/92623fa6759bbb4e4f27ce5aa381de213a55ae0c/.github/workflows/guest-core-readback.yml) · [Rust recursion desk](https://github.com/KirtusJ/pcp-os/tree/92623fa6759bbb4e4f27ce5aa381de213a55ae0c/store/apps/parrots-all-the-way-down)
