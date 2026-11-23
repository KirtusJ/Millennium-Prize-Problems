# Complex extension: execution record

Director G4, November 22, 2026, America/Vancouver. This continues the calibrated environments in the [initial G4 execution record](../execution.md). The mathematical artifact is [ComplexReflectionPositivity.lean](ComplexReflectionPositivity.lean), SHA-256 `47c67d26f29d0f47eade1e9505b78b33112f8ef896957a2cc952ce5bef0f5cc6`.

## Observed checks

Host Lean 4.19.0, commit `6caaee842e94`, with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`, accepted 24 theorems and nine definitions. The 33 axiom reports use only `propext`, `Classical.choice`, and `Quot.sound`; `swap` needs only `propext`. There is no accepted `sorryAx`, user axiom, unsafe proof or native-decide certificate. The complex definitions are explicitly noncomputable; the theorem terms are checked by Lean's kernel. [Positive log](evidence/compiler/child/positive.log)

Four syntactically valid source mutations were rejected: removing coefficient conjugation; discarding the reality requirement; removing theta from the reflected first argument; and changing the complex two-coordinate witness from -2 to +2. The compiler checks require a nonzero exit and diagnostic output; the logs identify the failed mathematical obligations. These controls are separate rejected modules. Error-recovery `sorryAx` in those logs is not part of the accepted source. [Mutation specification](mutations.json) · [Compiler child receipt](evidence/compiler/child/receipt.json)

The first integrated compilation failed on missing `noncomputable` annotations and two explicit control proofs. G4 added the annotations and repaired the cast/component arithmetic without weakening the statements. Earlier, the challenge worker correctly identified a fragile conjugation proof and a sum-rewrite-order issue; those were repaired before that first integrated check. The original model draft, challenge, failed compilation diagnostics and final source remain distinguished. [Initial compiler failure](evidence/initial-failure/child/positive.log)

## Recursive PCP workers

`commission.py` actually ran a PCP program coordinator which launched child PCP supervisors through `../run_worker.py`. Those child supervisors launched bounded text-only model workers through the pinned Python PCP host. The first model returned the draft; a second process challenged that output. After G4's corrections, the reflected-regulator bridge and exact finite pushforward identity were added and the fixed source was given to a third model process for a final static audit. The final review is bound to the source digest above. The model processes had app, browser search, shell and multi-agent tools disabled. No chat/browser/app subagent was used.

The hierarchy is Director G4 -> PCP program coordinator -> PCP child supervisor -> PCP model. The child and parent independently observe process exit and read back the returned artifact and receipt. The reviewer processes are separate executions from the same provider family, not independent-party mathematical review. They make no claim of having run Lean. [Draft and challenge receipts](evidence/commission/receipt.json) · [Final static review](evidence/final-review/challenge/model_reply.txt) · [Final review receipt](evidence/final-review/receipt.json)

Compiler checking used the separate recursive program hierarchy Director G4 -> PCP supervisor -> PCP checker -> Lean processes. The checker enumerates every requested axiom report, rejects unexpected axioms, verifies that the input source did not change during each process, and checks the positive and adverse outcomes. The parent requires and reads the child's summary after exit. Seven successful hosted registers, covering the original commission and its two children, the final review and its child, and the compiler supervisor and child, replay without guard or object-integrity errors. Their raw registers and produced objects accompany the receipts.

The hosted implementation and matching method remain separate from the current Enterprise release: Python runtime repository `59f26ebe6397e00e8a9b8cce08487ad8a5319c0c`; required method fingerprint `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707`, 58 files. Current Enterprise method/Core identities for the native run are in its receipt. Actor attribution is `DECLARED`, with the Principal's commission relayed explicitly. Registers prove the recorded local integrity checks, not authenticated authorship or mathematical truth.

## Native source replay

The previously pinned portable QEMU and public PCP kernel were reused. Six new measured guest boots again passed the exact, changed, truncated, appended, missing and denied Core readback controls. Three further measured guests emitted the source's three portions. The assembled bytes exactly match the checked file and the final review candidate. Each guest's ELF identity, measured image identity, exit result, serial hash and register head are recorded. The supervisor reads the serial artifact after process exit. [Native receipt](evidence/native/receipt.json)

The three source emitters form a sequential host-mediated chain: each requests the next role and the host starts it. They emit supplied source portions; they do not discover the proof, run Lean in the kernel, or spawn children inside the kernel. Recursive program/model execution is provided by the hosted PCP hierarchies described above. This distinction is intentional.

## Reproduction

With the pinned Mathlib checkout and Lean binary on PATH, run:

```text
lake exe cache get Mathlib/Analysis/Complex/Basic.lean Mathlib/Tactic/Ring.lean Mathlib/Tactic/FinCases.lean
lake env lean /absolute/path/to/ComplexReflectionPositivity.lean
```

The source uses the same finite-sum, norm-number and topology dependencies as the earlier G4 proof. A normal pinned Mathlib installation supplies the remaining transitive imports.

For the full compiler hierarchy, invoke `../check_proof.py` with the original explicit runtime, method, Mathlib, Lean-bin, source and fresh output paths, and add `--namespace Millennium.G4.ComplexRP --mutations /absolute/path/to/mutations.json`. For native replay invoke `../native_replay.py` with the original explicit native, Lean-bin, Enterprise-method, source and fresh output paths, adding `--split-markers "-- NATIVE CHILD 1" "-- NATIVE CHILD 2"`. The assembled file now retains its input filename. The original real-source defaults remain available.

`commission.py --runtime PATH --method PATH --out NEW_DIRECTORY` repeats the draft/challenge hierarchy. Adding `--candidate PATH` reviews a fixed source without generating another draft. Model outputs are nondeterministic and are never substituted for compiler checks.

`verify_evidence.py` checks the recorded byte chain. Its optional `--runtime` and `--method` paths also deep-replay the seven successful hosted registers. The evidence index excludes the full delivered method prompts, caches, executables, kernel images and credentials. The own-task prompts, returned outputs, receipts, diagnostics and produced register objects are retained. Byte-sensitive proof, compiler-harness, mutation and evidence files disable Git newline conversion. The verifier explicitly decodes Lean diagnostics as UTF-8, including on Windows.

No independent-kernel implementation or fresh reconstruction of all Mathlib dependencies is claimed. The scope and remaining continuum obligations are in [README.md](README.md).
