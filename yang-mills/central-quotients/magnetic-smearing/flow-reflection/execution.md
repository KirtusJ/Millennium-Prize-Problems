# Formal and numerical verification

Two fresh three-generation PCP OS deployments each closed a parent, child and grandchild on the measured native kernel. The parent collected the coefficients of the three-reading Hankel form. The child computed outward endpoints for the exponential base. The grandchild computed the signed integer endpoint from the five rational moment bounds. Each parent verified the returned digest. Hosted Lean 4.19.0 with Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b accepted all 14 declarations on both runs; the reported axioms are within propext, Classical.choice and Quot.sound. The source SHA-256 is 2023cbf3fbf0dbdee3dc38e43c4a1ed5f6fe9f9164dcd52d390a8db4440f3252. The native worker ELF SHA-256 is fa8eb6ec75b99a6a6f80d920341fd3abf1a8580f3fab9b64f953f2a062ac745c. [Generated Lean](FlowReflection.lean) · [Native worker](worker.c) · [Execution archive](execution-logs.tar.gz) · [Environment pins](../../clustering/execution.md)

The kernel proof includes the actual negative exponential covariance at $s=1/8$, the rank-one shifted form, a discrete convexity bound, and the constancy implication for quadratic temporal increments (an ordinary stationary covariance also satisfies $C(t)\le C(0)$). The proof of the specific negative form uses the kernel-checked exponential bounds inside Mathlib, without numerical input hypotheses. Both runs refused an invalid child task and rejected four proof mutations involving the reflection distance, the middle polynomial coefficient, the exponential enclosure, and the magnitude of the negative form. The archive includes the development warning removed before the release, the kernel reports, and the numerical outputs. The written all-buffer moment argument, continuum consistency estimates for the compact flow, and Wilson spectral limits have separate mathematical proofs outside Lean. The method manifest check covers all 57 pinned payloads.

The exact integer [grid checker](check_grids.py) encloses eight signed forms from the deposited [integer vectors](grids.json). Its last normalized interval is $[-4406,-4405]\times 10^{-54}$. Its other computations include a direct rational comparison against the unflowed kernel. The [classical compact Wilson check](check_classical.py) gives the following bounded positive-side readings before clipping, using the smooth negative-half bump specified in the code. Its mesh and time-integration checks are numerical.

| Cells per period | Wilson deficit divided by $a^4$ | Absolute error against continuum | Change on halving integrator step |
| ---: | ---: | ---: | ---: |
| 16 | 0.0000767721242 | $6.42\,10^{-6}$ | $1.02\,10^{-9}$ |
| 32 | 0.0000820354155 | $1.15\,10^{-6}$ | $3.96\,10^{-12}$ |
| 64 | 0.0000828626370 | $3.27\,10^{-7}$ | $1.48\,10^{-14}$ |
| 96 | 0.0000830439363 | $1.46\,10^{-7}$ | $5.72\,10^{-16}$ |

The continuum Fourier calculation gives 0.0000831896130. The configuration that starts at identity stays at zero at every resolution. Replay using a fresh output directory, Python with NumPy for the nonlinear test, and the pinned PCP and Lean tools. If using a partial Mathlib build, first run `lake build Mathlib.Data.Complex.ExponentialBounds` in that checkout.

```sh
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
python check_grids.py
python check_classical.py
```
