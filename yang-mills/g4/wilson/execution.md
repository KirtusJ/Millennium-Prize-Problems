# Wilson formalization: execution and reproduction

Director G4. Mathematical scope and hypotheses are in [README.md](README.md). This lane follows the [program rendezvous](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/pull/293) and the [Millennium director coordination](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1). G4's working coordination comments are [initial scope](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7093783692) and [boundary-gauge interface](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7094125992).

The accepted source SHA-256 is `465d565057c6b5a1b0b196cf24a1bb3285eaf63c41f75141d2959ef9bf906f3f`. The final source review, compiler and native source assembly bind these exact bytes.

Observed final validation: all 87 declaration reports passed, all five altered sources were rejected, all nine native observations passed, and all nineteen selected hosted registers deep-replayed without integrity or guard errors. The evidence manifest indexes 203 files totaling 1,122,334 bytes before the manifest itself. Two of those registers retain the original unsuccessful Gram review, followed by its separately recorded successful retry.

## Compiler contract

Lean 4.19.0 with Mathlib commit `c44e0c8ee63ca166450922a373c7409c5d26b00b` accepts all 87 named declarations: 62 theorems and 25 definitions. Every declaration has a corresponding axiom report. The checker accepts only `propext`, `Classical.choice` and `Quot.sound`, and requires exit zero, unchanged source and imported module bytes, and no errors or error-recovery `sorryAx`. Harmless unused-section-variable, unused-hypothesis and tactic-style warnings remain. [Compiler receipt](evidence/compiler/receipt.json) · [Complete positive log](evidence/compiler/child/positive.log)

The imported integral module is freshly compiled from source SHA-256 `6c035f89d1f29c8f1e0b712dad6b8982a7d30bcccda7a557b8403df3853b9f0f`; the resulting `.olean` is `0c3173bd7d655d0d4bfe4b4a530c531b47ff1acaff01d975f8e18fc62974e083`. The complex module is reused from the previously recorded build, SHA-256 `e813aff6c86181bf9493cf9ce3264df5827e1c0c0ecbd845a6a0d2a3ef52e74a`, and bound to its [earlier source/build receipt](../integral/evidence/dependency/receipt.json). Its source remains `47c67d26f29d0f47eade1e9505b78b33112f8ef896957a2cc952ce5bef0f5cc6`. No fresh complex compilation is claimed here. [Integral dependency build](evidence/dependency/receipt.json)

Five [adverse source mutations](mutations.json) exercise a false negative exponential limit, missing test conjugation, omitted partition normalization, reversed coupling signs, and a missing boundary inverse. They are rejected modules, not admitted facts. The expected failures test the retained proof against these alterations; they are not a completeness guarantee for proof-attack detection.

Concrete falsifying cases explain the controls. At z=0 the Taylor limit is +1. A constant-i test needs conjugation to give +1 rather than −1. A singleton probability with exponent log 2 requires its partition denominator. With w=−1 and a constant real unit feature, sqrt(w)² is zero rather than w. With all other group factors equal to one and a boundary value of order three, h differs from h⁻¹. The compiler diagnostics record the actual failed proof obligations; no separate machine-checked counterexample is claimed for this explanatory list.

## Recursive PCP work and corrections

Four draft/challenge commissions addressed convergence, ordered-word Gram expansion, Haar temporal transport and explicit slab geometry. The actual hierarchy is Director → PCP program coordinator → PCP child supervisor → bounded text-only model. The parent reads the child's output only after observing its exit and records the digest and task end. The compiler has a separate Director → PCP program supervisor → PCP checker → Lean hierarchy. No chat, browser or app subagent was used.

The original Gram draft completed, but its challenge provider failed. Its failed receipt is preserved under `evidence/gram`; a successful separate review of the original draft is under `evidence/gram-review`. The final full-source review first exceeded the Windows command-line length limit. The new local `run_worker.py` passes the documented PCP `@file` task argument, leaving the previously published worker unchanged. The retry reviewed the complete accepted source. The failed launch is retained under `prior-runs/wilson-audit1`.

Earlier compiler runs are retained under `prior-runs`. Corrections addressed finite-sum casts, the real/complex exponential distinction, product-measure notation, complete codomains for generic Bochner integrals, exact matrix API names and beta reduction. The final integration derives the actual partition and numerator transport and supplies the concrete weighted plaquette invariance/continuity lemmas requested by the geometry reviewer.

The [final audit](evidence/final-review/challenge/model_reply.txt) found no circular integral premise and described the finite-graph scope. It was a static source review: the worker did not run Lean or inspect the imported module source. Compiler acceptance and transitive axiom reports supply separate evidence. All model workers are from the same provider family; no independent-party validation or certification of unseen method clauses is claimed. Actor attribution is `DECLARED`, with the Principal's instruction relayed explicitly.

Nineteen selected hosted registers are included for deep integrity replay: three each for convergence, Gram, slab and geometry; two each for Gram retry and final review; two compiler registers and one dependency register. The original Gram parent and failed challenge are valid integrity records of unsuccessful work. The other seventeen correspond to completed successful work. Failed task status is not converted into success merely because the register verifies.

The hosted runtime is pinned at `59f26ebe6397e00e8a9b8cce08487ad8a5319c0c`. Its required compatibility-method fingerprint is `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707` over 58 files; Core descriptor is `9f5998dd75e921afe490687783787847916428f7ee7bcea410a88dad04646fb0`. This is distinct from the current Enterprise method used for native calibration.

## Native calibration

Nine measured native guest runs passed: exact, changed, truncated, appended, missing and denied Core readback, followed by three source emitters. Their emitted portions concatenate byte-for-byte to the accepted Lean source. [Native receipt and serial evidence](evidence/native/receipt.json)

The Enterprise method manifest is `3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18`, and Core is `39efd83b4122545455124f20420f212590a06064f391b259e93ea968449e6b7f`. The kernel file is `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`, with measured image identity `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3`. The readback emitter source pin is `92623fa6759bbb4e4f27ce5aa381de213a55ae0c`.

The native emitters read supplied proof fragments. They do not discover proofs, run Lean, or recursively spawn descendants inside the kernel. The host mediates their sequential child requests. Recursive execution belongs to the hosted PCP workers; formal proof checking belongs to host Lean. This distinction is part of the execution claim.

## Reproduction

Use the pinned Mathlib checkout and Lean binary. In addition to the prior integral module caches, fetch the imports of the new source, including `Mathlib.LinearAlgebra.UnitaryGroup`, `Mathlib.LinearAlgebra.Matrix.Trace`, `Mathlib.MeasureTheory.Group.Measure`, `Mathlib.Tactic.Group`, `Mathlib.Analysis.SpecialFunctions.Exponential` and `Mathlib.MeasureTheory.Integral.DominatedConvergence`.

Rebuild the complex dependency with the previous `../integral/build_dependency.py`. Then `build_dependency.py` in this folder takes `--runtime`, `--method`, `--mathlib`, `--leanbin`, `--source` (the integral source), `--complex-module` (the pinned complex `.olean`) and `--out` (a fresh directory). Binary bytes may depend on paths/toolchain; the recorded binary pins reproduce this environment, while portable verification should rebuild from the pinned sources.

```text
python -B check_wilson.py --runtime PCP_PYTHON --method MATCHING_METHOD --mathlib PINNED_MATHLIB --leanbin LEAN_BIN --source WilsonReflectionPositivity.lean --out NEW_CHECK_DIRECTORY --namespace Millennium.G4.WilsonRP --mutations mutations.json --extra-lean-path DEPENDENCY_DIRECTORY
```

`commission.py` accepts explicit runtime, method and fresh output paths. Select `--task-dir convergence`, `gram`, `slab` or `geometry` for the corresponding draft/challenge. For a fixed-source audit use `--candidate ABSOLUTE_SOURCE`, which selects this folder's `reviewer_task.txt`. The prior commissions used the previous worker; the current runner uses PCP's `@file` task input for large candidates.

For native replay invoke `../native_replay.py` with absolute `--native`, `--leanbin`, current Enterprise `--method`, `--source` and fresh `--out` paths, and `--split-markers "-- NATIVE CHILD 1" "-- NATIVE CHILD 2"`.

`python -B verify_evidence.py` verifies the manifest, source/report chain, negative sources, imported-module provenance, fixed-source review and native assembly. Add `--runtime PCP_PYTHON --method MATCHING_METHOD` to deep-replay all nineteen selected registers. This is recorded-byte verification, not a fresh compiler run, native boot or independent audit. Evidence omits credentials, delivered method prompts, caches and binaries. Hash-bound source and evidence have Git newline conversion disabled.
