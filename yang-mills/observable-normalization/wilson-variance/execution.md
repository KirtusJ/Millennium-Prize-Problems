# Verification record

The attached Lean source checks six algebraic steps: one axis average, its second iterate, the trace-square floor, the fair-sign identity, the weighted-color inequality, and the scalar drift-cost estimate. The lattice independence, compact-group integration by parts, shift comparison, and variance theorem are proved analytically in the note. They are outside the six formal declarations.

Three measured PCP OS guests emitted A4’s source templates. A fresh three-guest replay with the supervisor from the transfer-increments directory matched the source bytes. Run from this directory with the pinned kernel in that supervisor’s receipt.

```sh
python ../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof WilsonVariance.lean
```

```text
w0.elf 47d5c387612052820ad1defe315fe57fa16f09ae0bcb55a4dc3889cf9edeaf5d kernel register: 47 events, head 0a49f416a8a65ee960496e758536e4ffbdd6e9c99a879599ad719a3f606af333
w1.elf 268c9bda729e630be2372d9c807160b82871feb4dafa6e2626d8960c1536d81b kernel register: 47 events, head 900b40c2e32b0d143d420168ca09283530ea86b353c4c7b3bde865d4184a9532
w2.elf 2d6cadaa023da9da7bda0c255897d60c7b2437351855e64f8282facb46cbe56d kernel register: 47 events, head 72b9401648f8ba09ef17eb8332ed0cbc2597bc81977c53aca791251cb70f94a7
generated source SHA-256 98c8dcce2a5b980db720d3d3bf5cddb7e6845f24e65ed683fa5c259388c9bd96
```

Host Lean 4.19.0 with Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b and cached dependencies exited zero.

```text
'YangMills.BlockVariance.oneAxisAverage' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.BlockVariance.twoAxes' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.BlockVariance.traceSquareFloor' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.BlockVariance.splitSign' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.BlockVariance.assemble' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.BlockVariance.localCost' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The exact-arithmetic script `python -I check_blocks.py` enumerates both signs for each of nine axis pairs on rational unit quaternions. It includes an inverse rotation, two one-link nuisance terms and a constant. Both the enumerated and predicted squared mixed coefficient are 1944/15625. Independent enumeration on periodic sizes 3, 4, 5 and 8 gives closed neighborhood sizes 9, 10, 11 and 11. These examples supplement the all-size combinatorial argument.
