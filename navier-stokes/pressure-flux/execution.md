# Source and execution record

At the external revision `f9e8bc5b38b6e212696e8a30e3e91517af887bbd`, the `R3/PressureFlux.lean` and `R3/WholeSpaceUniqueness.lean` blobs are respectively `542377decf40306a50ce2170783de99a384b8d41` and `ad83465eedc6b723fb01d10603453234cf7f84b4`. Its toolchain is Lean 4.34.0-rc2. The [research note](README.md) follows calls in proof bodies. The external development was read as source. The Lean and PCP runs below reproduce A4’s own checks.

The four local declarations check the unit values of the two real-power envelopes, the failure of uniform scalar domination, and the final linear absorption implication. A three-level sequence of measured PCP OS guests emitted the authored Lean templates. A second run reproduced the source bytes. The host supervisor launches each child after reading its parent’s request, checks the ELF measurement, exit status and guest self-tests, and joins the three outputs. The kernel image and QEMU instruction-counted wrapper are specified in the [guest setup](../../yang-mills/observable-normalization/smeared-plaquettes/action-curvature/execution.md).

From this folder run

```sh
python ../../yang-mills/observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof PressureFlux.lean --qemu /path/to/qemu-wrapper
```

The replay returned

```text
w0.elf 0a8e13b6671ef9f107387d2670de08988a3252ccfc4d00cd55b790dec9c3d4d1 kernel register: 47 events, head 3a196e83fc30168988b3abd0ecad0a41169eb333f904ca13f8e50a8148db1f73
w1.elf 9fd5292bce09625e10b86a08554b5deab71fbe1cebbfc5d2dedc7477356a186a kernel register: 47 events, head 5cd34bba757f9e916eb62860d73e0235384dba9cf50ab4337e79f1b0388b8ff6
w2.elf fc9a023fd4617402d7913881dbc4edc44166f2fd942ecded555e9d37a015099b kernel register: 47 events, head 0e5586159b3a826c71af0d1367913076db889c1da24a7e8d874bddc8aad0d302
generated source SHA-256 a81eb0a70f164d33d067593f3a9cc3f92950a6dff156e031a02c8923112ed447
```

Host Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked the emitted file with no warnings. From that checkout run `lake env lean /absolute/path/to/PressureFlux.lean`.

```text
'NavierStokes.PressureAudit.printedUnit' depends on axioms: [propext, Classical.choice, Quot.sound]
'NavierStokes.PressureAudit.formalUnit' depends on axioms: [propext, Classical.choice, Quot.sound]
'NavierStokes.PressureAudit.noUniformComparison' depends on axioms: [propext, Classical.choice, Quot.sound]
'NavierStokes.PressureAudit.absorb' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Requiring the dissipation to satisfy A ≤ 1 in the separating control failed. At comparison constant 2, all such A give a formal unit envelope at most 5, while twice the printed envelope is 6.
