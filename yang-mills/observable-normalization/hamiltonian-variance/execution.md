# Reproduction and proof coverage

Three measured PCP OS guest boots emitted the source in order. The root requested the spectrum worker, which requested the limit worker. A host supervisor relayed those requests, collected the emitted lines and checked the resulting file byte for byte on a second run. The worker contains A4’s theorem templates. Host Lean 4.19.0 checked their concatenated output against Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

From this directory, supply the kernel with SHA-256 `e1b3d972eea2e7825fee09bf8f792e06260f132144ca97d1cf2d81bfa645c414` and run

```sh
python ../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof HamiltonianVariance.lean
python check_trial.py
```

In the pinned Mathlib checkout run `lake env lean /absolute/path/to/HamiltonianVariance.lean`. Each of the three guests reported its worker’s successful exit and passed kernel self-tests. The second run produced

```text
w0.elf c88a143540388661a6f3905a27e36b01740eeb1e655735c0cae429aad2a4c185 kernel register: 47 events, head 417309f5fe4e9fee79989159b6b736df90551389a7222da2aee5dee17afa8747
w1.elf e45f89dab6b034ec5e38b0cbf5edb10ce0ca72922542b0dd5149668618a54aad kernel register: 47 events, head 565ce601ec769ccad2e5a4f679eae70cf42904d4df0d75080b17017feaea5b74
w2.elf 3902190b52a071073b96f6d011964b1118d952e64ac143d0e5dea7c6e23e6dcb kernel register: 47 events, head 5f87ff68f5a83d90c7b4ad501d45747689589da10b51ba7904f82a4eb860cf8c
generated source SHA-256 351c5542e9a0e7f075a4d1aff90a9823a00fa335602c909b9d8e28d7612bb250
```

Lean exited successfully. The nine declarations printed

```text
'YangMills.HamiltonianVariance.linkReplacement' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.HamiltonianVariance.intervalChoice' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.HamiltonianVariance.varianceFloor' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.HamiltonianVariance.trialKinetic' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.HamiltonianVariance.fourLinks' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.HamiltonianVariance.optimizedTrial' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.HamiltonianVariance.covarianceToEnergy' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.HamiltonianVariance.escapeToVariance' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.HamiltonianVariance.normalizedSpectralWitness' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Lean checks the scalar consequences of link replacement and interval escape, the product-trial inequalities, a second-moment energy estimate, the escape-to-variance inequality for a finite measure, and the exponential tangent integrated against a probability measure. The identification of the lattice Hamiltonian and its ground state, the product-trial Haar integrals, the radial derivative and interval bounds, and the identification of the plaquette spectral law are proved analytically in the [research note](README.md).

The independent angular quadrature compared the matrix mean, kinetic form and trace variance with their closed formulas. Its maximum residual was `1.879e-12`. Using unit-length generators in place of the specified half-length generators produced a maximum kinetic residual of `35.86`. In a separate mutation, reversing the first-moment hypothesis in `normalizedSpectralWitness` caused Lean to reject the proof. The point mass at 2 with time and proposed energy bound both equal to 1 disproves that mutated statement, since it would require exp(−1) ≤ exp(−2).
