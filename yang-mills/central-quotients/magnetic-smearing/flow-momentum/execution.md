# Verification and independent comparisons

Two fresh three-generation native PCP deployments generated the same Lean source. The parent convolved a time-difference polynomial, the child computed the two-channel threshold denominator, and the grandchild computed the signed rational upper endpoint for the zero-momentum torus fixture. The hosted recursion desk verified parent-child returns and closure. Each release used Lean 4.19.0 with Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b. Lean accepted 17 declarations with only propext, Classical.choice and Quot.sound in the reports. The source SHA-256 is 006462ac3df2fccde91e980ab454e0d422d5f35b3a412f258e5ff0d5196b8250. The native ELF SHA-256 is 7b090677e79f697410091ca56c4dad798b3cfc084b12556e383e937a1a32ac0b. [Worker](worker.c) · [Generated proof](FlowMomentum.lean) · [Logs](execution-logs.tar.gz)

The formal proof of the finite-recurrence obstruction treats arbitrary finite lag sets and real coefficients. Its hypotheses express boundedness after every geometric reweighting. Other formal results concern the heat-tail exponent, two-particle phase algebra, positive angular weight, and the rational implication from the zero-momentum lattice readings. The integral representations and their Wilson limits are derived separately. Each replay refused an incorrect callback and four mutations to the time filter, threshold coefficient, propagator deficit and torus sign estimate. The method manifest and its 57 listed payloads were checked.

The [continuum calculator](check_momentum.py) compares integration over total energy and energy difference with an independent radial/angular integral of the transverse projector. It checks both flow prescriptions and the unflowed limit at four external momenta. At $s=1$ the reflected second difference at separations $0.125,0.1875,0.25$, divided by the variance, is shown below. These numbers are numerical quadratures. The fixed-momentum theorem uses strict inequalities in the Schwinger representation.

| Momentum magnitude | Full flow | Spatial flow | Spatial right threshold density, one color |
| ---: | ---: | ---: | ---: |
| 0 | −0.001132447237 | +0.006998042567 | 0 |
| 0.5 | −0.001176868944 | +0.007638098504 | 0.000009922391 |
| 1 | −0.001225679445 | +0.008452345072 | 0.00006816308 |
| 2 | −0.001448480893 | +0.01305955441 | 0.00004092944 |

At $k=0.75$ the integrated ratios $t e^{kt}G_s^{\rm sp}(t,k)/\rho_{s,k}(k+)$ are 0.9775120, 0.9915772 and 0.9977159 at times 40, 160 and 640. The [finite torus calculator](check_zero_mode.py) instead sums a finite list of outward-rounded intervals. Its spatial projection uses the trace of the squared magnetic covariance and absolute spatial multiplicities. [Three-direction derivation](torus.md)

Run the offline verification with a fresh output directory and the [pinned kernel, desk and Mathlib settings](../../clustering/execution.md). The numerical scripts use NumPy, SciPy and mpmath.

```sh
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
python check_zero_mode.py
python check_momentum.py
```
