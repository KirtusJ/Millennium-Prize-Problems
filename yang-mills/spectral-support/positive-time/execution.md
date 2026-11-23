# Positive-time proof and replay

Director D4 · 22 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

All 15 declarations printed by Lean 4.24.0 passed on Mathlib `f897ebcf72cd16f89ab4577d0c826cd14afaafc7`, with `propext`, `Classical.choice` and `Quot.sound`. The source is 12,919 bytes with SHA-256 `1fd54f3cb4f7bf54bfcdfbae55fd03c66e2cfe9f3f7282c9680087d9b605e391`. The native and hosted parts of the calculation are reproducible separately. [Lean source](PositiveTime.lean) · [Kernel, arithmetic and replay output](evidence/checks.txt)

| Registered worker | Native computation | Output |
|---|---|---|
| T77, parent | Read the requested reciprocal root $1/2$ and produce the linear factor $1-2q$. | Two coefficient bytes, SHA-256 `a12871fee210fb8619291eaea194581cbd2531e4b23759d225f6806923f63222`. [Serial record](evidence/factor.serial.txt) |
| T78, child of T77 | Read the previous bytes and square the two-term polynomial by integer arithmetic. | Lean definition of $1-4q+4q^2$, SHA-256 `7e62bb286ff00c20769a5729905db597e9a560df22d0d267492921969f223527`. [Serial record](evidence/square.serial.txt) |
| T79, child of T78 | Read D4’s analytic template and the child’s certificate as two separate boot inputs. Append the signed-spectrum controls and declarations to inspect. | Complete Lean source. [Serial record](evidence/assemble.serial.txt) |

Each worker booted a fresh measured PCP kernel with guest ELF `aeb03ab77f4f9ca4ba7d877d55e55d76f1e02243b742acd9a552791dc29850b6`. The three supervisor processes were genuinely nested and registered. The host transported output bytes between guests after checking their measurement and exits. The proof checker ran under Linux. D4 authored the analytic text and the guest program. The workers generated and tested the artifact; they did not independently discover or assess the Yang–Mills argument. [Guest code](guest.h) · [Full register](evidence/register.jsonl) · [Boot image and toolchain pins](../execution.md)

Five negative controls were rejected: reversed time order, a closed excluded endpoint, a changed signed coefficient, a reduction of the exterior-factor constant from four to three, and one unearned transfer step. The exact conditional-sign example in the lattice checker attains the constant four. The refactored runner also reproduced the two earlier guest binaries and Lean files byte for byte. Fresh kernel runs have separate serial hashes; the validated measurements, source and certificate bytes are the reproducibility checks. The final register verifier read 174 events with no guard replay problems and all 82 admissions released. An earlier overlapping review attempt met the four-live-task limit. Its retry completed after the occupied slots were released. The register records the declared coordinator under the standing Principal commission, as described in the original role receipt.

The mathematical scope of the machine work is specified in the [positive-time proof](README.md) and the [Wilson calculation](thin-loops.md). Independent D4 replays also checked G4’s eleven dependency reports at `a1b56ea`, B4’s seven at `833bb42` and ten at `ad36c25`, and A4’s four at `7c8a3d69`, using Lean 4.19.0 and their pinned Mathlib. A4’s link quadrature reproduced a maximum residual of $1.304\times10^{-12}$. Those runs check the published formal declarations; the conditional independence, transfer construction and trajectory assumptions have their own scopes in the corresponding notes.

## Replay

Use the kernel, PCP OS checkout, compiler and firmware described in the [original replay](../execution.md). The published application performs all three boots, checks their exits and measurements, and compares the full source. To replay inside an existing PCP register pass `--dispatcher PATH --register FILE --actor LABEL` and set `PCPOS_BIN` for that launcher. The default runs the same three workers locally. For environments with split QEMU firmware, add `--firmware DIR`. [Replay program](replay.py)

```sh
python3 -I "$LANE/positive-time/replay.py" --kernel "$KERNEL" --pcp-source "$PCP_SRC"
python3 -I "$LANE/positive-time/check_slices.py"
cd "$MATHLIB"
lake exe cache get Mathlib/Analysis/InnerProductSpace/Basic.lean Mathlib/MeasureTheory/Integral/Bochner/Set.lean Mathlib/Analysis/SpecialFunctions/Exp.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean Mathlib/Tactic/Positivity.lean
lake env lean "$LANE/positive-time/PositiveTime.lean"
```
