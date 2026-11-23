# Verification

Three sequential measured PCP OS guests produced the Lean source from A4’s templates. A fresh supervisor run checked each admitted image, child request, success receipt and the final assembled bytes. From this directory run the following with the pinned kernel from the transfer-increments receipt.

```sh
python ../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof SmearedPlaquette.lean
```

```text
w0.elf b6deddc28d8c53152ae12a7c7e5da6881b05775ff68fb8f6722eaeb2aa7e1c19 kernel register: 47 events, head 2637997b04249b3078fb3b9eba4d3a9d125d0145d8e1d58686d4e57ecf993226
w1.elf 33553b6261de6ff0a7dff04479820cac7b827687ed676cef634ea5648a3f808a kernel register: 47 events, head 086b6544f2b29bc4421ab4fc4035c561aa1f22273fd614e7ef2e0e332b64a59b
w2.elf 9a4c396c9fcd271f04e27ac3b8b2795959f020fa6ef234dac65f1795cf4dc62e kernel register: 47 events, head d931dad97570611f6aea1ea902fc43f082911f14461202f825170f36e4b3161c
generated source SHA-256 58450f982172ac0f49eaf4b737787a0002e0e53faa8336a924b685a86a0e6284
```

Lean 4.19.0 on the Linux host with Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b checked the generated source, using upstream compiled dependencies. The process exited zero.

```text
'YangMills.Plaquette.joinedTrace' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.Plaquette.mismatch' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.Plaquette.edgeDecomposition' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.Plaquette.edgeUpper' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.Plaquette.commonSmearing' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The formal statements check scalar trace and norm identities after choosing quaternion coordinates, the local quadratic energy decomposition and inequality, and the final division by a positive variance. The mapping of link gradients to those coordinates, the lattice sums and the probability calculation are analytic arguments in the note.

The independent matrix implementation in `check_shared_edge.py` used 64 configurations, central differences in three Pauli directions, and oppositely traversed shared links. The largest absolute discrepancy was 3.297×10⁻⁹. Replacing the required inverse product by the other trace word increased the largest error to 1.98. This is a numerical orientation control, with no sampling of the physical Yang–Mills vacuum.
