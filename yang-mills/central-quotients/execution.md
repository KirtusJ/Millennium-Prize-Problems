# Reproducing the central-quotient calculations

Director C4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Three PCP OS user processes generated the nine Lean theorem declarations from C4-authored templates and computed coefficients. The root searched the Hamilton multiplication table for an obstructed pair. Its child tested all four signs of the returned lifts. The grandchild enumerated the 256 ordered tuples and all 4,096 cube edge-sign assignments. Lean checked the generated file on the Linux host, using only its standard library. For the cube it recomputed face multiplicities by a different method, adding one edge at a time. [Guest code](worker.c) · [Reproduction script](reproduce.py) · [Serial transcripts, desk and Lean output](execution-logs.tar.gz)

## Observed checks

| Item | Result |
|---|---|
| PCP host release executable | SHA-256 `dd68d895f11fa419f5508377106d18a2beeda0676c6441c017d987b5b8aaf93a` |
| Enterprise method manifest | `3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18`. All 57 listed files matched. |
| Selected review texts | ACR 1.0 Core `39efd83b4122545455124f20420f212590a06064f391b259e93ea968449e6b7f` and Mathematics `8c5009a8b6a610fb03ae4fe1e25d4674e0d256c9593885fb03b8159e580463f1`. The Fidelity Audit Lab’s separately identified comparison texts were Core R13 and Mathematics R5. |
| Guest calibration | Core byte-for-byte match exited 0. Last-byte change, truncation and append exited 1. Missing file exited 2. Denied read exited 3. QEMU returned the expected diagnostic code 33 in each case. |
| Kernel ELF | 733,284 bytes, SHA-256 `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. Its bytes occur exactly once in the pinned ISO, at offset 806,912. |
| Kernel text and read-only data | Every proof guest measured `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3`. QEMU 10.0.13 ran a networkless microVM. The asynchronous keyboard checks were skipped in this machine profile. |
| Guest program | The same 8,992-byte ELF ran in each role and the negative control. SHA-256 `47b9e0da11a69ee5f74e4712ea7485c8ef1643e16aebcc2a6142f247137da2bf`. Each guest read a separate three-byte task module. |
| Recursion | PCP’s hosted Rust desk admitted nodes 1, 2 and 3 at depths 0, 1 and 2. Each host worker waited for its child and reread the returned bytes and digest. The desk reported all three finished at revision 6. Each node ran a separate PCP kernel. The host conveyed guest requests and launched QEMU. |
| Lean | 4.19.0, commit `6caaee842e94`. Both source files compiled. Six declarations use no axioms. Three cube declarations report only `propext`. |
| Source read-back | Model SHA-256 `c897922c33e0f8c93692babe379f0128015360063ea063279bf866f2ae847ae5`. Generated proof SHA-256 `6e70d8cc8c4c859a30fa6b19df2cbb8f96cf67b408157b83c3bb4fbb4888f766`. A fresh second hierarchy reproduced the proof byte for byte. The archive records this second run. |
| Adverse controls | A request to prove the two lifts of the same axis obstruct one another exited 5 before emitting proof or a child request. Changing the zero-flux count from 46 to 47 caused Lean to prove the mutated proposition false during elaboration and exit nonzero. |

The first compile attempt exposed a missing nonreturning annotation. An early guest ELF with an empty writable segment failed admission. The final worker uses a static buffer for the incoming task. An early host model also failed to elaborate its list enumeration; the published version uses explicit list operations. These attempts supplied no accepted theorem.

A separate host calculation indexed cube vertices by their three binary coordinates and exhaustively averaged the weights as rational numbers. It found 32 patterns of multiplicity 128, an exact weight of 8177/2048, and an excess of 729/4096 over the independent-face product. The analytic one-link bound was also checked numerically at six couplings from 0.01 to 1000. Its proof is the recurrence argument in the research note.

## Replay

Use Python 3, GCC/binutils, QEMU x86-64 with its firmware, and Lean 4.19.0 on Linux. From the PCP OS checkout at `92623fa6759bbb4e4f27ce5aa381de213a55ae0c`, build the hosted recursion desk. The linked public ISO has SHA-256 `93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15`. Extract its `/kernel.elf32` and check the digest above. [PCP OS checkout](https://github.com/KirtusJ/pcp-os/tree/92623fa6759bbb4e4f27ce5aa381de213a55ae0c) · [Public ISO](https://github.com/KirtusJ/pcp/blob/983fc4a45dbbada52b507dd0e413b9f7d3ca0c9d/PCP-OS.iso) · [Upstream calibration harness](https://github.com/KirtusJ/pcp-os/blob/92623fa6759bbb4e4f27ce5aa381de213a55ae0c/examples/method-readback/check.py)

```sh
cargo build --locked --release \
  --manifest-path "$pcp_os/store/apps/parrots-all-the-way-down/host/Cargo.toml"
desk_bin="$pcp_os/store/apps/parrots-all-the-way-down/host/target/release"
python3 reproduce.py --pcp-os "$pcp_os" --kernel "$kernel" \
  --desk "$desk_bin/parrots-all-the-way-down" --delegate "$desk_bin/pcp-delegate" \
  --qemu "$(command -v qemu-system-x86_64)" --lean "$(command -v lean)" \
  --out "$new_output_directory"
```

The output directory must be new because the script creates a fresh desk and preserves evidence from each attempt. With a separate QEMU firmware location, add `--firmware /path/to/firmware`. To check only the published Lean sources, run the following in this directory with a temporary output directory for the compiled modules.

```sh
compiled=$(mktemp -d)
lean -o "$compiled/Model.olean" Model.lean
LEAN_PATH="$compiled" lean -o "$compiled/CentralQuotient.olean" CentralQuotient.lean
```
