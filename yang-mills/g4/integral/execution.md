# Integral extension: execution and reproduction

Director G4, continuation of the 22 November 2026 session, America/Vancouver. Mathematical scope is in [README.md](README.md). The formal artifact is [IntegralReflectionPositivity.lean](IntegralReflectionPositivity.lean); the matrix-feature application is the separately audited [analytic Wilson-kernel proof](wilson-kernel.md).

The accepted source SHA-256 is `6c035f89d1f29c8f1e0b712dad6b8982a7d30bcccda7a557b8403df3853b9f0f`. The fixed-source review and final native source emission bind these same bytes. The separate analytic candidate hashes are in their review receipts. This lane continues the [program rendezvous](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/pull/293) through the [Millennium director coordination issue](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1).

## Verification contract

Observed final result: all 31 declaration reports passed, all five altered sources were rejected with the expected diagnostics, all nine selected native observations passed, and all fifteen packaged hosted registers deep-replayed without integrity or guard errors. The evidence manifest indexes 208 files (740,193 bytes before the manifest itself). The previous complex component's byte verifier also remains passing. These results are distinct from the static mathematical reviews and the analytic slab application.

The compiler run uses Lean 4.19.0 and Mathlib commit `c44e0c8ee63ca166450922a373c7409c5d26b00b`. The source has 28 theorems and three definitions. Each named declaration has a corresponding axiom report. The checker accepts only `propext`, `Classical.choice` and `Quot.sound`, requires a successful process exit and unchanged source bytes, and rejects error-recovery `sorryAx`. The final digest and all observed results are recorded in the [compiler receipt](evidence/compiler/receipt.json) and [positive log](evidence/compiler/child/positive.log).

The imported complex module is compiled from the previously published source, SHA-256 `47c67d26f29d0f47eade1e9505b78b33112f8ef896957a2cc952ce5bef0f5cc6`, before checking this extension. Its generated `.olean` hash is bound in both compiler receipts and the [dependency receipt](evidence/dependency/receipt.json). The module binary is not committed; its source, compilation command, output and post-exit digest are available. A different path or toolchain may change binary bytes; reproduce from the pinned source and compiler rather than trusting a downloaded binary.

Five adverse source mutations target missing conjugation, a false zero normalization for the constant-one test, an omitted partition denominator, reversed Gram-weight signs, and a false nonintegrable-tilt identity. They are separate rejected modules, not admitted facts. The [mutation specification](mutations.json) and compiler diagnostics identify exactly what was altered. Expected failures test the retained proofs against these false changes; they are not a completeness claim about arbitrary proof attacks.

The intended adverse failures are concrete: constant i changes a conjugated square from +1 to −1; a probability’s constant-one expectation cannot be zero; on a one-point probability with S=log 2, dropping Z changes expectation 1 to 2; the one-mode weight a=−1 gives a negative Gram integral; and a nonintegrable exponential produces a zero tilt rather than preserving a nonzero base measure.

## Corrections and limits of formal coverage

The first model draft used an invalid namespace alias. G4 replaced it with qualified names and fixed a finite-sum index order error. Integrating the factorization required a common named universe for both finite-test quantifiers. The normalized Wilson bridge needed explicit complex casts and beta reduction before applying the tested-density identity. Earlier compiler diagnostics are retained under `evidence/prior-runs`; they do not count as successful verification. A relative-path launch was also corrected by resolving all compiler arguments before starting child processes. The imported module's first output build needed Lean's explicit `--root` flag. Missing Mathlib caches were fetched at the existing pin.

Two harmless unused-premise warnings remain: a continuity premise used to establish a probability tilt is stronger than needed for one integrability sublemma, and the rank-one integral identity itself holds under totalized integration even without its mode-integrability premise. The finite-sum theorem uses the integrability premises to justify its interchanges. The final conditional Wilson theorem explicitly concludes both actual test integrability and complex nonnegativity, and supplies a finite strictly positive partition.

The matrix-entry feature identity, uniform exponential-tail bound and identification with specified lattice crossing plaquettes are not Lean formalized. The analytic review required explicit product measurability, a finite positive full partition for boundary conditioning, and the reweighted boundary law after fiber normalization. These corrections are in the fixed reviewed text. A positive density or positive Gram truncation is not asserted to establish all Wilson lattice geometry or the continuum theory.

The director rendezvous then supplied the [open temporal slab identification](open-slab.md). Its recursive PCP audit found that extra reflected end weights must also be gauge invariant. A concrete ±1 partition counterexample exposed the missing assumption; the statement was corrected and reviewed again. The density sign convention is explicit. The free-end case needs no extra boundary factor. This application remains analytic; the Lean module is unchanged.

## Actual PCP worker hierarchy

The first complete positive-and-five-negative run rejected every altered source, but its missing-partition diagnostic matcher expected the phrase `type mismatch`. Lean instead reported a failed definitional equality in the normalized bridge (and an earlier stuck typeclass in the altered density proof). That run remains marked failed. The matcher was narrowed to the observed failed equality, and the complete compiler hierarchy was rerun with the unchanged accepted Lean source. The earlier specification, receipts and diagnostics are retained under `prior-runs/integral-check10`.

`commission.py` launches a PCP program coordinator, then child PCP supervisors through `../run_worker.py`, then bounded text-only model processes. One draft/challenge commission developed the integral interface; a second developed the finite Gram identity and its product-measure version. A final reviewer sees the exact Lean source. A separate reviewer challenges the analytic Wilson-kernel proof, with an additional run after corrections. The subsequent slab identification receives its own original and corrected-source review. No chat, browser or app subagent was used.

These are actual processes, with task-start events, process-exit observations, artifact readback and task-end receipts. The parent verifies each child receipt after exit. The compiler has its own Director → PCP program supervisor → PCP checker → Lean hierarchy. Fifteen selected successful hosted registers are included for deep replay: three integral-commission registers, three factorization registers, two final-source-review registers, two final-analytic-review registers, two open-slab-review registers, two compiler registers and one dependency-build register. Earlier static reviews are retained separately with their different candidate digests.

Review workers come from the same provider family and have no shell, browser, app or multi-agent tools. Their static assessments are not independent-party validation, compiler execution or certification of uninspected method clauses. G4 is a director moniker, not a clause identifier. The Principal's instruction is explicitly relayed; actor attribution is `DECLARED`, not an authenticated signature.

Hosted runtime and required method identities remain those in the [prior execution record](../complex/execution.md): runtime commit `59f26ebe6397e00e8a9b8cce08487ad8a5319c0c`, required method fingerprint `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707` (58 files). This compatibility method is not conflated with the current Enterprise release used by the native calibration.

## Native calibration and source emission

The selected final native run uses the previously pinned portable QEMU and PCP kernel. Six measured guest boots exercise exact, changed, truncated, appended, missing and denied Core readback. Three further measured guests emit the final source portions, which the host assembles and compares byte-for-byte with the compiled candidate. [Native receipt](evidence/native/receipt.json)

The current Enterprise manifest is `3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18`; Core is `39efd83b4122545455124f20420f212590a06064f391b259e93ea968449e6b7f`. The kernel file identity is `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`, with measured image identity `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3`. No new system-wide runtime is installed.

Native source emission is a sequential host-mediated chain of supplied proof fragments. It does not discover the proof, run Lean in the kernel or spawn descendants inside the kernel. The hosted PCP program/model hierarchy supplies recursive task execution; host Lean supplies formal checking. An earlier native replay matched an intermediate source; only the selected final run is bound to the accepted source.

## Reproduction

Use the pinned Mathlib checkout with the Lean binary on PATH. Install its import caches, including:

```text
lake exe cache get Mathlib/MeasureTheory/Integral/Prod.lean Mathlib/MeasureTheory/Measure/Tilted.lean Mathlib/MeasureTheory/Function/LocallyIntegrable.lean Mathlib/MeasureTheory/Constructions/Pi.lean
```

`build_dependency.py` takes explicit `--runtime`, `--method`, `--mathlib`, `--leanbin`, `--source` (the complex source) and `--out` (fresh directory). It compiles `ComplexReflectionPositivity.olean` into that directory and checks all its axiom reports. Then run:

```text
python -B check_integral.py --runtime PCP_PYTHON --method MATCHING_METHOD --mathlib PINNED_MATHLIB --leanbin LEAN_BIN --source IntegralReflectionPositivity.lean --out NEW_CHECK_DIRECTORY --namespace Millennium.G4.IntegralRP --mutations mutations.json --extra-lean-path DEPENDENCY_DIRECTORY
```

For a direct replay, add the dependency directory to `LEAN_PATH` and invoke `lake env lean ABSOLUTE_SOURCE` from Mathlib. `commission.py --runtime PATH --method PATH --out NEW_DIRECTORY` launches the draft/challenge hierarchy. `--task-dir factorization` selects the second commission; `--candidate ABSOLUTE_SOURCE --task-dir final-review` selects the source audit. The analytic review uses `wilson-kernel.md` and `--task-dir analytic-review`. Use absolute paths for these commission arguments.

For native replay use `../native_replay.py` with explicit native, Lean-bin, current Enterprise-method, source and fresh output paths, and `--split-markers "-- NATIVE CHILD 1" "-- NATIVE CHILD 2"`.

`python -B verify_evidence.py` checks the exact recorded-byte chain, every named declaration's report, the mutations, imported-module binding, fixed-source and fixed-document review digests, and all nine selected native observations. Adding `--runtime PCP_PYTHON --method MATCHING_METHOD` deep-replays the fifteen hosted registers. Recorded-byte verification is not a fresh Lean build or native boot. Evidence excludes credentials, full delivered method prompts, caches, binaries and kernel images. Git newline conversion is disabled for hash-bound source, harness, mutation, analytic candidate and evidence files.
