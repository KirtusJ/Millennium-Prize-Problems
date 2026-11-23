# Reproduction and proof scope

Run the following from this directory with the [parent note’s pinned kernel](../execution.md).

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ExcitedBand.lean
python check_rotor.py
```

The supervisor dispatched the root, spectrum and limit workers as three separate PCP OS boots. A second run reproduced all emitted source bytes.

```text
w0.elf fcb0846943dba09a73168ef71942370bd91ed427358351d30028735680bd0d94 kernel register: 47 events, head 28699d71d98e58269148fcf799a1602e3fb0bedf04885f2d0ba8b68f6c626d37
w1.elf dc5a29df80cff317875eb00c06ccf5ebdbe7cef01bb1b6e812649c1817b713ba kernel register: 47 events, head cea90b80d74db13b05b2dcd1985f2a8e4d3bc95302c25698ed49342461f13257
w2.elf 1047db84b5ce2ae4a0df78d973daab137893ab79f707b5436bbaaa1c51e2bdc0 kernel register: 47 events, head 3e55c118cbbf6a7e1f3270bd9958eb4c726be5d9ce7519c53a0dc6834c54e5d9
generated source SHA-256 75d6c4a41e83bfff7bcb792310a15c4f7cea5a0ecf55dd188e5ac52105e5d883
```

Host Lean 4.19.0 checked the emitted file against Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`. Run `lake env lean /absolute/path/to/ExcitedBand.lean` from that Mathlib checkout. Lean exited successfully with the following output.

```text
'YangMills.ExcitedBand.scoreFloor' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ExcitedBand.pointBand' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ExcitedBand.momentWindow' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ExcitedBand.windowWeight' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ExcitedBand.differenceKernel' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ExcitedBand.integratedDifference' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The six declarations check the scalar score bound, the pointwise indicator inequality, its integral against an actual finite measure, the extraction of interval mass, and the pointwise and integrated time-difference lower bounds. Identifying the sphere divergence, Hamiltonian domain and commutator, spectral moments, and any limiting theory requires the [analytic argument](README.md). Deleting the second-moment contribution in the conclusion of `momentWindow` caused Lean to reject the modified proof. A unit atom at an energy above the proposed window, with lower endpoint zero, disproves that modification.

The numerical control uses a single isolated SU(2) plaquette. In the class-character basis, multiplication by the trace connects adjacent characters with unit coefficient and the four-link kinetic operator has diagonal entries n(n+2) in units of κ. The script diagonalized the resulting interacting tridiagonal Hamiltonian at truncations 48 and 96, checked the energy-form and commutator identities independently of the spectral moment sums, and tested the inequalities using the rotor’s own per-link kinetic form. Truncating the trace at the last basis vector introduces a boundary effect; repeating the truncation check bounds its observed impact on the listed numbers. The free one-atom comparison is exact analytically. The columns give coupling ratio, first moment, second moment, interval mass and time difference at t = 0.1, s = 0.2.

```text
0 3 9 1 0.150809061
1 2.95385292 9.35980118 0.942197855 0.148799466
16 1.67638225 17.0780627 0.166632846 0.0456209191
256 0.501405445 22.0782287 0.0113945112 0.00014010977
```

Both truncations agreed to relative tolerance 1e−9 and absolute tolerance 1e−10. These values test the generator and moment conventions on the isolated plaquette. The uniform cubic-volume estimates follow from the proof.
