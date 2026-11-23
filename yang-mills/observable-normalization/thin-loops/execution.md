# Verification

Three measured PCP OS guests emitted A4’s theorem templates. A fresh replay from this directory with the pinned kernel and the following command reproduced the Lean bytes.

```sh
python ../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ThinLoop.lean
```

```text
w0.elf 259d268b79d8774c5615f345621e9c10902d1f9ca296663de830dbe971078ac6 kernel register: 47 events, head 8a20267a4db3b604d8b91b461c8ba1ed60067fbaeca6b59952b1a84fd7cf8112
w1.elf a1bff707982cb2085f3fcde1584bf4ec6079cdb2203aebea14ae3e5fa6591852 kernel register: 47 events, head cbbcfb253f187ac4392e366f61099cdf63aff1640f14db478a973ee737677f21
w2.elf 5d25ca7f7e19839b1b91a552de947c254910e638e44287c7e961166835c1e595 kernel register: 47 events, head 34fa0362c5429cecca4960fdc79dffc78c6e3a88e6ff31de38dc38c4771bb276
generated source SHA-256 14a25d72a7f612df837976c2e0e7228da739838c42f6b23cb85fab74daf81e81
```

Host Lean 4.19.0 and cached Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b checked those bytes, exiting zero.

```text
'YangMills.ThinLoop.conditionalContraction' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ThinLoop.loopEnvelope' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ThinLoop.varianceFloor' depends on axioms: [propext, Classical.choice, Quot.sound]
'YangMills.ThinLoop.singlePlaquetteLoss' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The Lean results cover the scalar contraction from the score inequality, the exponent from the edge count, the variance floor and the normalized one-step loss inequality. The conditional-measure argument, representation identities, graph selection, continuum-limit interpretation and the spectral consequence are analytic.

The accompanying `check_link.py` compares angular quadrature with the two scaled Bessel ratios at seven concentrations from 0 through 256. On this run the largest absolute discrepancy, including the two integration-by-parts residuals, was 1.304×10⁻¹². The same script checks why a repeated inverse traversal lies outside the theorem.
