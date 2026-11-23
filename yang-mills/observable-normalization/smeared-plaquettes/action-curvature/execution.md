# Verification of the curvature and window estimates

Three measured PCP OS guests emitted the Lean source through the root, spectrum and limit roles. A second complete run reproduced the file byte for byte. The host supervisor collected each requested worker’s source after verifying admission, successful exit and the kernel’s self-tests. The public ISO, extracted kernel, measured digest and supported replay script are pinned in the [spatial moments receipt](../moment-bounds/execution.md).

One earlier boot failed the kernel’s asynchronous keyboard wake-up self-test, before contributing any accepted source. Some ordinary-clock replay attempts also stopped early. The successful final generation and replay used single-threaded TCG with an instruction-counted virtual clock. Kernel self-tests remained enabled. To reproduce with QEMU 10.0.13, supply a shell wrapper executable containing the following, then pass its absolute path via `--qemu`.

```sh
#!/bin/sh
exec qemu-system-x86_64 -accel tcg,thread=single -icount shift=3,align=off,sleep=off "$@"
```

From this directory run

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ActionCurvature.lean --qemu /path/to/qemu-wrapper
python check_response.py
```

The second guest hierarchy produced

```text
w0.elf a3a7d47fc380c431a83c1de265dde52af36e75d8149c88b122a7a943b4e1f5e6 kernel register: 47 events, head 07587766f10b086117ec70b67645caac7a7c69ca74252be432c2701f02c6bae3
w1.elf 330fe466f7d82c5d95edae15b27b56103ac3a5317c27988bb6bc16954b0667b1 kernel register: 47 events, head 48398750f8853a58d16d5747334044adedda084addc54b3e7593a070b701442f
w2.elf 3e628097c3da3db07c946673b48bbee5df8a8cc2f8488ba44dc43294c2b8975f kernel register: 47 events, head 300e314146b6a146a748a84a19ef97affa347834ec92ed388433da84743dd2bd
generated source SHA-256 837b0e5f899558c5412663ba4340bee8ddc877533015847f58c602b4a6e74d25
```

Host Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked the emitted file. From that Mathlib checkout run `lake env lean /absolute/path/to/ActionCurvature.lean`. Lean exited zero.

```text
'YangMills.ActionCurvature.curvatureBudget' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ActionCurvature.budgetCeiling' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ActionCurvature.inverseInterpolation' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ActionCurvature.lowMass' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ActionCurvature.windowAverage' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ActionCurvature.rmsBound' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ActionCurvature.scaledTail' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ActionCurvature.dyadicRawLow' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The checked declarations include the fundamental theorem of calculus for the curvature identity given the derivative, inverse/first-moment interpolation for an actual measure, its low-energy mass inequality, the RMS arithmetic, and the averaged raw low-energy tail for an actual family of finite measures on a real coupling interval. The last theorem explicitly assumes the inverse-moment budget, variance floor, positive-energy support, and required integrability. The Hamiltonian perturbation calculation that supplies these assumptions, the physical clock identification, and the interpretation of the limits are analytic in the [research note](README.md).

Reversing the endpoint drop in the curvature budget failed Lean. The derivative of u(g) = −g on [1,2] supplies a counterexample. Changing the cubic power of r to a square in the pointwise tail estimate also failed. Set r = 2, v = ε = J = 1, V = 1/4 and m = 2; the altered conclusion reads 8 ≤ 4.

The independent character-basis calculation returned the following numbers. Columns are G, the integrated inverse moment multiplied by √G, the root mean square of G V, the averaged normalized first and inverse moments in √G energy units, and the slow fraction at the selected avoided crossing.

```text
16 0.624024073 1.91814484 3.13454072 0.324306901 0.448275862
64 0.621896466 2.02003257 3.2913131 0.3074115 0.448275862
256 0.621454492 2.07074804 3.36955353 0.299896406 0.448275862
1024 0.62135277 2.09605155 3.4086437 0.296335014 0.448275862
```

The two rotor character cutoffs were 64 and 128. Each scan used 24 Gauss–Legendre points, checked the integral of transition strengths against the endpoint drop to absolute tolerance 2e−11, and differentiated the independent mean-action expression at the midpoint. These are isolated-rotor checks. The three-dimensional box estimate rests on the analytic argument and the published spatial smearing bounds. [Avoided-crossing construction](controls.md)
