# Director G4 execution and calibration

November 22, 2026, America/Vancouver. UTC timestamps in the raw records fall on November 23. This record distinguishes method integrity, actual process execution, native kernel checks, and mathematical verification.

## Verified mathematical artifact

`ReflectionPositivity.lean` has SHA-256 `46715ecc5c64e73a9cfc72845cf99bfc62ceddbe22411f8c9946745860537e7a`. Host Lean 4.19.0 (commit `6caaee842e94`) with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` accepted all eight theorems and three definitions. The eleven printed dependency reports contain only `propext`, `Classical.choice`, and `Quot.sound`. No `sorryAx` is accepted. The final check consumed the source assembled from native guest serial output, whose bytes equal the repository file.

The adverse control changes the first conclusion from nonnegative to strictly negative while retaining its hypotheses and proof. Lean rejects it at the intended type mismatch. Its rejected diagnostic output contains `sorryAx` from error recovery; this is not the accepted artifact. [Compiler evidence](evidence/compiler/child/receipt.json) · [Accepted axiom log](evidence/compiler/child/positive.log) · [Rejected mutation log](evidence/compiler/child/negative.log)

The original hosted model draft failed elaboration of the finite-kernel limit proof at the default heartbeat limit. G4 introduced the fixed test and coefficient map before forming its finite-sum limit and replaced that proof body. Imports were narrowed. The theorem statement was retained. [Initial failure](evidence/draft-failure/child/positive.log)

A later evidence-parser check incorrectly rejected a successful compilation because its declaration regex did not accept Windows CRLF endings. That failure is retained separately; the parser was repaired, exact source-byte mutation was used, and the full positive/adverse run was repeated. [Parser failure receipt](evidence/parser-failure/child/receipt.json)

## Actual hosted PCP workers

The local Python implementation is `PCP_OS_Python` from `KirtusJ/pcp-os` commit `59f26ebe6397e00e8a9b8cce08487ad8a5319c0c`. Its required method has fingerprint `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707`, Core descriptor `9f5998dd75e921afe490687783787847916428f7ee7bcea410a88dad04646fb0`, and 58 files. Its verification reported `matches_required: true`. It is distinct from the installed Enterprise method and historical Fidelity Lab sources.

`run_worker.py` actually launched the PCP command provider with a bounded, text-only Codex model commission. The process had shell, apps, browser search and multi-agent tools disabled. G4's supervisor waited for host exit, read the output artifact, and recorded completion and deep register verification. The result is a draft from a worker of the same provider family, not an independent reviewer. Actor attribution and the relayed Principal instruction are `DECLARED`, not authenticated signatures. [Model receipt](evidence/model/receipt.json) · [Model process](evidence/model/model_process.json) · [Draft output](evidence/model/model_reply.txt)

The provider's logical UTF-8/LF response digest is `f09a6be377b0e0475170ea8b19ee21350edcddb8eecf703e2f49f165f4702647`; Windows text persistence gives the separate CRLF artifact digest `87f370292665a34a84b3e7d134cb6f591bba52ca58281de8f7c227cc5ce1192b`. Both artifacts are retained in the model register. These are distinct byte objects, not an unexplained hash substitution. The full delivered method prompt is omitted; its digest is retained.

`calibrate.py` rejected completion without a result and completion with a wrong readback digest, leaving the register unchanged in each adverse case. The valid completion passed. Deep replay found no guard problems or changed objects. [Host calibration](evidence/host-calibration/calibration.json)

`check_proof.py` used a separate recursive program hierarchy: Director G4 -> PCP program supervisor -> PCP program checker -> Lean compiler. Parent and child maintain separate PCP registers, wait for their subprocesses to exit, read artifacts back, and deep-verify. The parent fails if the child summary is absent. The child requires the complete requested axiom-report list with only the allowed axioms. These are actual hosted processes, not independent model opinions or freestanding-kernel Lean execution. [Supervisor receipt](evidence/compiler/receipt.json)

## Native PCP OS calibration

Using B4's pinned public inputs, G4 extracted a portable QEMU distribution without installing a system service. The Windows QEMU build reports 11.1.0 (`v11.1.0-12130-ge470268ff4`). Its published SHA-512 was checked. [Input receipt](evidence/native/inputs.json)

| Input | Identity |
|---|---|
| Public ISO commit | `KirtusJ/pcp` `e23784155622311cfff697468beb0ba8bbe83194` |
| ISO SHA-256 | `93ed3b599ad7be0e1e88a64813b1f2b5299d51507df2edca691aaf6189d10d15` |
| Kernel file SHA-256 | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Measured kernel code/data identity | `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3` |
| Upstream readback source | `KirtusJ/pcp-os` `92623fa6759bbb4e4f27ce5aa381de213a55ae0c` |
| Installed Enterprise method manifest | `3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18` |
| Enterprise Core specification | `39efd83b4122545455124f20420f212590a06064f391b259e93ea968449e6b7f` |

All 57 installed method payloads were compared against their manifest byte lengths and hashes. This verifies local integrity, not semantic compliance. [Manifest verification](evidence/enterprise-method.json)

The unchanged upstream readback program ran inside six fresh measured PCP kernels. Exact bytes gave `MATCH`/guest exit 0; changed-last-byte, truncated and appended sources gave `DIFFERENT`/1; a missing source gave `MISSING`/2; denied access gave `DENIED`/3. The host checks the admitted ELF identity, measured kernel identity, guest outcome, and QEMU debug-exit status 33, then reads the serial file after process exit. Each serial contains the kernel's successful register/self-test report. Raw serials and their hashes are retained. [Native receipt](evidence/native/receipt.json)

Three further measured guests emitted pre-authored portions of the corrected Lean source. A guest requests the next role, the host launches it, and the host assembles the read-back bytes only after matching each portion. This is a sequential host-mediated emission chain with three roles, not in-kernel child spawning or independent proof discovery. Mathematical generation used the actual hosted model above; the native emitters verify method exposure and source transport. The recursive PCP program hierarchy performs the compiler check separately.

Initial native build attempts failed before boot because the bundled Windows compiler lacked freestanding standard headers and the linker defaulted to PE. The successful harness supplies the two required intrinsic typedefs and explicitly selects ELF linking. It compiles with LLVM/LLD 15.0.1 targeting `x86_64-unknown-linux-gnu`; no operating-system installation was needed.

## Reproduction and limits

For the mathematical result, use the pinned Lean/Mathlib checkout and run `lake env lean /absolute/path/to/ReflectionPositivity.lean`. `#print axioms` gives the dependency receipts. This is a Lean kernel run with the stated library inputs, not an independent kernel implementation or a complete Mathlib rebuild.

For the native run, `prepare_native.py OUTPUT_DIRECTORY` downloads and checks the pinned ISO and portable Windows QEMU. Then call `native_replay.py --native DIRECTORY --leanbin LEAN_BIN_DIRECTORY --method ENTERPRISE_METHOD_DIRECTORY --source PROOF_FILE --out NEW_RUN_DIRECTORY`. It needs the existing 7-Zip executable named in the preparation script. Short output paths avoid Windows argument/path issues. The download requires network access; it does not change machine installations.

For hosted model generation or checks, explicitly provide the older Python runtime and its matching method to `run_worker.py`, `calibrate.py`, or `check_proof.py`. Do not substitute the newer Enterprise method silently. `formalizer_task.txt` records the model commission. Each script's `--help` specifies its paths. Existing output directories are refused. Registers and produced objects are included with the relevant receipts, so their original deep-verification result can be replayed with that runtime. They contain declared local actors and are not externally anchored.

`evidence/manifest.json` indexes the evidence bytes. Run `python verify_evidence.py` to check that index, the three emitted source portions, final compiler logs and receipt links. Supplying `--runtime` and `--method` additionally replays the four successful hosted registers with the pinned implementation. This check verifies recorded evidence; it does not substitute for a fresh native boot or Lean compilation. Source and evidence files opt out of Git newline conversion so that checked and published byte identities agree. Large toolchains, kernel images, caches, credentials and the full delivered method prompt are not committed.

The Enterprise and OS skills were read and used for bounded claim assessment and process readback. The Fidelity Audit Lab's historical Mathematics text was consulted as a separate source; no complete fidelity certification is asserted. Successful byte, guard and compiler checks do not establish a Yang–Mills construction. The precise mathematical scope and still-open complex test-algebra and continuum obligations are in [README.md](README.md).
