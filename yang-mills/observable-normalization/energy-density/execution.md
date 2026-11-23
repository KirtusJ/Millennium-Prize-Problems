# Verification

The root, spectrum and limit roles emitted the complete source in three separate measured PCP OS boots. A second three-guest execution reproduced its bytes. Both used the public PCP OS kernel and the instruction-counted QEMU 10.0.13 clock described in the [preceding replay record](../smeared-plaquettes/action-curvature/execution.md). The kernel self-tests and the worker admission, digest and exit checks ran in each guest.

From this directory run

```sh
python ../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof EnergyDensity.lean --qemu /path/to/qemu-wrapper
python check_energy.py
```

The replay gave

```text
w0.elf 38aaefc7d24a0c621e97b57304cc40fcf563fb56d9d00225958a2ec7d940dc89 kernel register: 47 events, head bf92b354de6d1b72d82d9cc6ccdca7ce41fb316299b65b967473c25dac7efec3
w1.elf 3e465d37621ce8fbd9fd8da50405a2f04963ff5f64b1ae8a0406af905f46e725 kernel register: 47 events, head af46a4b32e34a564467e0e234088320300c9c15abaa03d72ad4151d2c4c8a1b3
w2.elf 6492fd98712219e940f5331ca5b1976bbe7b4a64e25e92b64457904cae265d32 kernel register: 47 events, head 89e4f98837c61e5d85eb0c13857e03991a1b2fe7712b04a6d56f49267cced2e9
generated source SHA-256 e6ea17f293bd1b2b8e8180487eef603bf2515da68596dbd3b0cd1012651464cf
```

Host Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked the generated file, exiting zero. Run `lake env lean /absolute/path/to/EnergyDensity.lean` from the pinned Mathlib checkout.

```text
'YangMills.EnergyDensity.coordinateCasimir' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.EnergyDensity.localDiagonal' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.EnergyDensity.zeroRowForm' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.EnergyDensity.bareCoefficient' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.EnergyDensity.filterPoint' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.EnergyDensity.lowFilter' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.EnergyDensity.highFilter' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.EnergyDensity.restrictedFilter' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.EnergyDensity.filteredTails' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Formal coverage includes the two Casimir transition identities, the local coefficient arithmetic, the exact finite zero-row quadratic form, the bare scale constant, the two filter kernels and integrated lower- and upper-tail inequalities for an actual nonnegative-energy measure. The smooth operator identities, finite-volume estimates on the Wilson vacuum, locality and geometry, the spatial Taylor limit, and extraction of weak subsequences are analytic. Assertions that the candidate stress-energy tensor is nonzero or that continuum Yang–Mills has a mass gap would exceed this evidence.

Changing the conserved row sum from zero to one failed Lean; the one-by-one identity matrix on a constant weight one gives a direct counterexample. Changing the Casimir constant from 3 to 2 also failed. At n = 0 the upward transition would give 9 = 8.

The independent control enumerated mixed electric/magnetic term neighborhoods, checked the isotropic coefficient against an exact discrete Fourier sum on four meshes for a synthetic Laplacian, and diagonalized the isolated Wilson rotor at two character cutoffs. For that rotor all four electric terms have the same action on gauge-invariant states, so the energy Gram matrix has the exact pattern outer((1,1,1,1,−4),(1,1,1,1,−4)) times its one-link diagonal. The numerical calculation compares that pattern, the independently evaluated coordinate double commutator, the full spectral quadratic form and the squared-difference expression. The final three columns in the rotor rows are the electric diagonal, magnetic diagonal and quadratic form on weights (0.2,0.7,−1,2,0.5).

```text
side, maximum degree, maximum center distance (mesh units) 3 16 1.0
side, maximum degree, maximum center distance (mesh units) 4 16 1.0
side, maximum degree, maximum center distance (mesh units) 5 16 1.0
synthetic coefficient, four Fourier errors 9.0 5.23802 1.32616 0.33259 0.0832133
0 0 0 0
1 0.0461539519 0.73846323 0.000461539519
16 6.70552898 107.288464 0.0670552898
256 513.439175 8215.02681 5.13439175
```

The number 9 in the Fourier control belongs to the synthetic matrix with off-diagonal neighbor entries −1/b³. No value of the interacting Yang–Mills coefficient was inferred from that control.
