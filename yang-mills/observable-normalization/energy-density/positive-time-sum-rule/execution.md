# Execution and coverage

The root, spectrum and limit workers ran in three fresh measured PCP OS guests. Each child launch followed its parent’s explicit request. The supervisor checked the guest image, admitted ELF, completion and self-tests before accepting its lines of authored Lean source. A second hierarchy reproduced the file exactly. Host Lean 4.19.0 checked the emitted source against Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`. Twelve printed axiom reports contained only the three standard axioms. [Kernel and QEMU wrapper](../../smeared-plaquettes/action-curvature/execution.md)

From this directory run

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof PositiveTimeSum.lean --qemu /path/to/qemu-wrapper
python check_readings.py
```

From the pinned Mathlib checkout run `lake env lean /absolute/path/to/PositiveTimeSum.lean`.

```text
w0.elf fbccd750c485baffc01fe4c16f285c2279ea6acf58d8def49665d901c216dea8 kernel register: 47 events, head d692d02fab43db999d20c8a768b01786981f65e017691b369afd59615c418bbb
w1.elf 6e2246ef7f9d777578eee2aec09bfdc957fcc77a798ced8da87740aa92aa617d kernel register: 47 events, head 92089942f45b0cb418ca5d36b77d3a84cf42026e9fcbe1e23a5c050c80729f6e
w2.elf b6ded86db14599ef320d044fafbdc8a6bc9fc0c7bac016cd625ebd912289be95 kernel register: 47 events, head d723959a48569d51165faa8e4ea7e88f22aff7d9ace900e53685ad9784025eda
generated source SHA-256 ab670589a7f1eca551aa082dcee0695eaf2b24c8fc6c459e542d05dc3f018112
```

Lean proves the nonnegative sum rule over an actual spectral measure, including the exponential square mixture, two applications of integration in the opposite order, the evaluation and positivity of the logarithmic constant, and the energy-zero case. It also checks the real-coordinate rigidity of the two unit phases and the arithmetic of a finite error interval. The Mellin transform, Fourier uniqueness, endpoint convergence, quadrature variation and instability argument are analytic in the notes.

Changing the coefficient of log 2 from four to two failed the integration over the square. Changing the relative sign of the phase with coefficient three failed rigidity. With the altered sign, the phases corresponding to 2 and 3 can respectively be +1 and −1 and satisfy the altered relation.

The independent SciPy control returned

```text
constant 0.523248143765, maximum characteristic errors 1.4e-13, 2.7e-13
grid 32: retained 0.883297541, estimate 0.892778023, margin 0.183939721
grid 128: retained 0.883297541, estimate 0.885747332, margin 0.045984930
grid 512: retained 0.883297541, estimate 0.883914963, margin 0.011496233
escape 32: early 0.345521, middle 0.439842, late 0.214637
escape 1024: early 0.228966, middle 0.488403, late 0.282631
escape 32768: early 0.205250, middle 0.497900, late 0.296850
frequency 4: sampled max 0.002045604, bound 0.01531805
frequency 16: sampled max 9.455553e-05, bound 0.003829511
frequency 64: sampled max 5.839566e-06, bound 0.0009573778
```
