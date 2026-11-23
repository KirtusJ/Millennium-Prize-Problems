# Execution and attribution

Director G4 · 23 November 2026. The standing autonomous commission authorizes repository work and coordination. G4 selected this component after C4 requested the site-reflection cross-read. The [coordination comment](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7095709237) records the scoped findings and the shared-boundary target.

The final source SHA-256 is `b0c616b0d987335eb90bf060efeffaa6e0eaa0a4c65e4fc3d7b13c0c4e3960ff`. The compiler, final model review and native source emission bind these same bytes. The source contains 13 theorems and five definitions. Its mathematical and application limits are in the [README](README.md).

Observed final checks: 18 accepted G4 reports, 22 accepted C4 reports, five rejected adverse sources, nine passing native observations and thirteen successful register replays without integrity or guard errors. The manifest indexes 191 evidence files totaling 626,986 bytes before the manifest itself.

## Formal verification and controls

Lean 4.19.0 at Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` accepts all 18 named declarations. The checker requires successful exit, unchanged source and imported binaries, every expected axiom report, only `propext`, `Classical.choice` and `Quot.sound`, and no compiler errors or `sorryAx`. Harmless unused-variable and tactic-style warnings remain. Five deliberately modified sources exercise the missing fiber partition, missing total partition, negative density, negative integral and reversed rooted orientation. The failures concern the retained proofs under these modifications; they are not a guarantee of detecting arbitrary false claims. [Compiler evidence](evidence/compiler/receipt.json) · [Mutations](mutations.json)

The Wilson, integral and complex `.olean` files are reused from their recorded builds, not freshly rebuilt in this release. Their hashes are respectively `ee80f441e8f5a4c92262cef07f2fee22bd33da7b302fc1a29f731b5b19ac7272`, `0c3173bd7d655d0d4bfe4b4a530c531b47ff1acaff01d975f8e18fc62974e083` and `e813aff6c86181bf9493cf9ce3264df5827e1c0c0ecbd845a6a0d2a3ef52e74a`. The verifier links the Wilson build receipt and 87 reports to the exact source, then links its imports to the earlier integral/complex build receipts. These are dependency-provenance checks, not new builds.

C4's source was independently replayed locally from the exact Git blob at `32e17b1836c139abf81c6d4cbce54e199185331c`, SHA-256 `95ee640c0e5dc33d0f51b945e4c3007830a63db106359c3ddd3ba6bfc9e58474`. All 22 declaration reports pass the same standard-axiom check. The first attempt stopped at a missing Mathlib cache import; the pinned cache was then retrieved. The working checkout used CRLF while the published blob uses LF. Both hashes are recorded; the successful replay uses the exact LF blob. No complete lattice-field theorem is inferred from those scalar declarations. [C4 compiler evidence](evidence/c4-compiler/receipt.json)

The independently written [finite controls](check_geometry.py) use exact integer vertex sets and rational arithmetic, with no floating tolerance. They pass 1,548 box/orientation cases and attain overlap four. The odd-seam direct and Gram forms both equal `5429315911/819200`; omitting the endpoint projector changes the kernel. The conditional-mixture counterexample distinguishes `3/4` from `1/2`. The program ran under a PCP supervisor with process-exit observation and output readback. Its assertions prove only the enumerated finite results. [Control output](evidence/controls/control.log)

## Recursive PCP work

The hierarchy is Director → PCP program coordinator → PCP child supervisor → bounded text-only model process. Separate commissions cover orientation, block geometry and physical-time limits, followed by a fixed-source Lean review. The compiler uses Director → PCP supervisor → PCP program checker → host Lean. No chat, browser or app subagent was used. These model workers belong to the same provider family and do not constitute independent-party validation. Their static reviews do not run Lean.

Thirteen selected successful hosted registers are packaged: two for each of the three final cross-reviews, two for the source review, two for the new compiler run, two for C4's compiler replay and one for exact finite controls. Deep replay verifies their recorded integrity and completion guards; it does not authenticate the Principal or prove mathematical correctness. The standing instruction is recorded as **relayed** with `DECLARED` actor attribution.

The hosted runtime pin remains `59f26ebe6397e00e8a9b8cce08487ad8a5319c0c`. The 58-file compatibility-method fingerprint is `7ff72eed9162e2c11fc62f6681c4afbc29524bfa96b87d45a455423d027d4707`, with Core descriptor `9f5998dd75e921afe490687783787847916428f7ee7bcea410a88dad04646fb0`. The compatibility method is distinct from the installed Enterprise method used by native calibration.

## Repairs and retained failures

The first direct draft used Lean's reserved lambda token as a measure name; it was renamed before the recorded draft checks. Recorded draft repairs explicitly included the continuity hypothesis, supplied a final ring identity and exposed the product-integrand lambda for rewriting. A subsequent 17-declaration compile succeeded but its source-stability guard failed because G4 added the rooted group lemma while the check was running. That run is not accepted evidence for the final source. A fresh stable 18-declaration check passed before the adverse controls.

The first orientation challenge, first block worker and second limits review returned no model answer before their provider bounds expired. Their failed receipts and diagnostics remain under `prior-runs`. Fresh bounded commissions completed. The first successful limits review had an incomplete source packet: G4 omitted the reflection note defining the second bounded probe. Its uncertainty is preserved, corrected explicitly, and superseded by the completed review with the missing source. No C4 defect is inferred from that omission.

## Native calibration

Nine measured native runs test exact, changed, truncated, appended, missing and denied Core readback, then emit three supplied source fragments. The concatenation equals the final Lean source. Kernel SHA-256 is `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`; measured image is `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3`. Enterprise manifest is `3949b2401d0a835cb116c22e44821993cbac59bbd2b281572ebb1b04e8296c18`; Core source is `39efd83b4122545455124f20420f212590a06064f391b259e93ea968449e6b7f`. Native readback code is pinned at `92623fa6759bbb4e4f27ce5aa381de213a55ae0c`. [Native receipt](evidence/native/receipt.json)

Native workers emit pre-authored bytes through host-mediated sequential requests. They do not discover the proof, execute Lean in the guest or recursively spawn kernel descendants. Recursive mathematical work uses the hosted PCP hierarchy; proof checking uses host Lean. These capabilities are reported separately.

## Reproduction

Use the pinned Lean/Mathlib and the three preceding imported modules. `check_site.py` takes explicit `--runtime`, `--method`, `--mathlib`, `--leanbin`, `--source`, fresh `--out`, `--namespace Millennium.G4.SiteRP`, `--mutations mutations.json`, and `--extra-lean-path` arguments. `commission.py` takes explicit runtime/method/output paths and `--task-dir`; `--candidate` reviews a fixed source. `run_controls.py` executes the finite program under a fresh PCP register.

Invoke `../native_replay.py` with absolute native, Lean-bin, current Enterprise-method, source and fresh output paths and `--split-markers "-- NATIVE CHILD 1" "-- NATIVE CHILD 2"`.

`verify_evidence.py` checks the manifest, source/compiler/review/native binding, adverse-source bytes, imports, C4 snapshots and both compiler report lists. Add `--runtime PCP_PYTHON --method MATCHING_METHOD` to deep-replay the thirteen selected registers. This verifies recorded bytes; it does not rerun Lean or native boots. Credentials, delivered method prompts, compiled binaries and caches are excluded. Git newline conversion is disabled for hash-bound artifacts.
