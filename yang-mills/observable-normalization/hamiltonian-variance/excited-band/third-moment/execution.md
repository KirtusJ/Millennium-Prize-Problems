# Proof coverage and replay

The three roles ran in separate measured PCP OS guests. The root requested the spectrum role, which requested the limit role. The host supervisor launched the requested workers and reproduced the concatenated Lean source byte for byte. From this directory run

```sh
python ../../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof CubicMoment.lean
python check_sum_rule.py
```

The kernel is pinned by the [Hamiltonian execution record](../../execution.md). A second guest run produced

```text
w0.elf 0befb895adc836f822954a78c0f957b0fba7b412f0e045f304228c35f8f56af1 kernel register: 47 events, head 8f50a8cf53b0659fe49be1731ab991660f84402db458e070207aada128f1664c
w1.elf aa75d30367e964800464734f6419829281dbdcb8fb80fbf7096681cd13d1ac60 kernel register: 47 events, head 72a8ab827aee2a49c27fc59180b940d44ed6d108c6a2f8afd700036d5decbe52
w2.elf f084e879b33c869dc9bcd82f1f71ac5e115f622bd52f74f21cb09d64a9e64c91 kernel register: 47 events, head 4dbf35428abf20e08a1eabd9f2918294ccad8865670b2f9755bb4bee91faacea
generated source SHA-256 7e94ce615564b1045074a10e495a89ffdea0f9b33311fbde027d57567f49afdb
```

Host Lean 4.19.0 checked this file with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b`. From the Mathlib checkout run `lake env lean /absolute/path/to/CubicMoment.lean`. Lean exited successfully.

```text
'YangMills.CubicMoment.kineticDouble' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.CubicMoment.localThird' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.CubicMoment.momentInterpolation' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.CubicMoment.smallLoss' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.CubicMoment.largeLoss' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.CubicMoment.uniformSecond' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.CubicMoment.numericCeiling' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The checked declarations cover the scalar kinetic and magnetic estimates after the local operator bounds, interpolation of actual positive spectral measures, the two coupling regimes and the final numerical ceiling. The commutator identity, product-group coefficient counts, plaquette geometry, and sphere-gradient estimates are analytic in the [proof](README.md). Removing the spectral support condition from the interpolation and replacing it with the tautology that E equals itself made Lean reject the proof. The probability measure giving equal weight to −1 and 2 then has first three moments 1/2, 5/2 and 7/2. Its second moment squared exceeds the product of its first and third.

The rotor control independently evaluates the spectral third moment and both nested commutators using the character Jacobi matrix for one isolated SU(2) face. Columns are magnetic coupling, first moment, second moment, third moment, kinetic contribution and magnetic contribution, in units κ = 1. The commutator uses the kinetic matrix to compute [H,F]. The outer commutator is evaluated separately on the kinetic and magnetic matrices.

```text
0 3 9 27 27 0
1 2.95385292 9.35980118 30.4584762 29.1766457 1.28183048
16 1.67638225 17.0780627 178.019628 111.979673 66.0399554
256 0.501405445 22.0782287 973.409386 514.824847 458.584539
4096 0.130757283 23.5070377 4226.33057 2142.68736 2083.64322
```

The 64- and 128-character results agreed to the tolerances in the script, including the interacting cases. Dropping the magnetic contribution gives a large discrepancy. The calculation tests normalization and the double-commutator signs. Spatially adjacent plaquettes and the uniform-volume constants are handled by the local analytic estimates.
