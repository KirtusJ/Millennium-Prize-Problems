# Source and execution record

The original endpoint blob is `dbd5db70bc11b35f18fa5751216ab335321e7bfc` and the original `ChTop.lean` blob is `ce06a34a9e0b1b332e10d3b7efb04a06e9ab77f5`. Source links in the note pin the original Lean 4.33.1 branch. The [research note](README.md) follows calls in proof bodies. The external development was read as source. The Lean and PCP runs below reproduce A4’s own checks.

The three local declarations check the exact normalization, the four upper costs, and passage from a pointwise bound to a finite mean. A three-level sequence of measured PCP OS guests emitted the authored Lean templates. A second run reproduced the source bytes. The host supervisor launches each child after reading its parent’s request, checks the ELF measurement, exit status and guest self-tests, and joins the three outputs. The kernel image and QEMU instruction-counted wrapper are specified in the [guest setup](../../yang-mills/observable-normalization/smeared-plaquettes/action-curvature/execution.md).

From this folder run

```sh
python ../../yang-mills/observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof PrimeInequality.lean --qemu /path/to/qemu-wrapper
```

The replay returned

```text
w0.elf 1a010361a7b6a79ecde0bd1c77e8045d13c3c864027b8863171583940cd7dfb8 kernel register: 47 events, head 27c5e3b5b32c8a10469e0ede74a0814ae007e7fc01d31a92420afc5dc8ca7260
w1.elf 0a47f56f04ae72f5642a640ed9eef32f580e6ee936d2bd4c5458c1948f81a9b5 kernel register: 47 events, head ca68082933e138f27578486cb8df0d8bd2d371192873ce0a0b2520eb36668445
w2.elf f52d9bb965f9209ce3c06e26ea847f6a03e638b1317d2113dcca2f718f8c633e kernel register: 47 events, head 63565845c6df6c91f68e72bd607abe113297e3cc3af3a703a3e74658b07bcbe7
generated source SHA-256 60909d6b308d4bb82d85d10a515fe9db52d02fa9c6debacb5ce4218b4e119216
```

Host Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked the emitted file with no warnings. From that checkout run `lake env lean /absolute/path/to/PrimeInequality.lean`.

```text
'Riemann.PrimeInequality.normalizeBracket' depends on axioms: [propext, Classical.choice, Quot.sound]
'Riemann.PrimeInequality.fourCosts' depends on axioms: [propext, Classical.choice, Quot.sound]
'Riemann.PrimeInequality.translateMean' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Removing the divisor two in the table normalization failed the identity. Setting all variables to one gives raw bracket 5, normalized bracket 10 and altered quotient 5.
