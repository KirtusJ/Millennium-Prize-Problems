# Reproduction and proof coverage

The [worker source](worker.c) builds three freestanding guest executables. Each runs under its own PCP OS kernel in QEMU. The first guest requests the spectrum worker, which requests the limit worker. The host dispatches each request and concatenates the guest-emitted source lines. A fresh three-guest replay reproduced the [Lean file](UniformBand.lean) byte for byte. Each of the six boots reached the kernel self-test pass and each guest returned exit zero.

Use the [guest replay script](../transfer-increments/replay-guests.py) with the measured kernel, then check the emitted file under Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b`.

```sh
python ../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof UniformBand.lean
lake env lean UniformBand.lean
OPENBLAS_NUM_THREADS=1 python check.py
```

The replay runs from this directory. Run the Lean command in the pinned Mathlib environment with the path to the emitted source. The kernel SHA-256 is `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`.

The [numerical and symbolic controls](check.py) passed. Real-space periodic incidence operators on cubes of sides eight and ten reproduced the Fourier symbol at all tested modes. Both zero-momentum spectra gave the orientation coefficients 26/3, 26/3 and 98/3 to numerical precision. The exact controls tested the scaled quartic coefficients, polynomial zero orders including repeated roots, and matched moments. A four-state binary transfer on two faces provided a separate high-precision control on the two spectral scales. Its gauge group and coefficients differ from those of the Wilson theory studied here.

The Wilson transfer construction, holomorphy and density hypotheses, representation decomposition, eigenvalue counts and thermodynamic-limit argument are mathematical arguments in the accompanying text. The Lean declarations cover individual implications used there.

The emitted source SHA-256 was `1c88251feaa0b232c0d5700de9fe1c64d52bbdd23f84b205acb147be794cfe8b`. Lean returned zero. All ten printed axiom lists contained only `propext`, `Classical.choice` and `Quot.sound`. The checks include the maximum-modulus bound for a supplied holomorphic quotient, positive-measure tail exclusion, root separation, the second-lag bounds, coefficient arithmetic and exact moment matching. In a separate negative-control file, Lean rejected each altered declaration when the tail inequality was reversed, the simple-root denominator was doubled, or the mass of the wider pair was changed.
