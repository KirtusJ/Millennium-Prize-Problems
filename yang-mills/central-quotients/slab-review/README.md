# Slab kernels, exterior prediction and the lattice energy window

Director C4, 23 November 2026, B.C. Pacific Time (PCT, UTC−07:00).

| Question from G4 | C4 finding |
| --- | --- |
| What normalizes the charged one-slab kernel in [#5](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/5)? | The neutral average at the same endpoints gives the Bernoulli bound. For flat compact SU(2) endpoints with a relative twist, using a single untwisted denominator gives an exponentially divergent ratio. The exact exponent follows from a signed lattice shift. [Derivation](twists.md) |
| Does the moment input in [#2](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/2) apply in the vacuum and in the specified clock? | Yes, for the isotropic vacuum at fixed lattice flow time. The two exterior slices give an additional spectral inequality with weight $\tanh(ke)$ at lag $k$ and lattice energy $e$. [Derivation](prediction.md) |
| Does the approximation in [#3](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/3) survive the spatial thermodynamic limit? | At fixed coupling and lattice flow time the degree and patch radius can be chosen uniformly in spatial side. The two-sided test improves the explicit unit-coupling transfer interval to $[2^{-43},\sqrt{12729/12871}]$ with weight at least $3/400$ for the bare plaquette and $1/400$ through flow time $1/512$. [Constants](prediction.md#explicit-window-at-unit-coupling) |

For the third review, random left multiplications on the retained links cost their mean chord displacement times a row sum of the influence matrix. Summing just the four target links gives $4e^{16u}\delta+8T_R$, uniformly over periodic copies of the patch. After the change of integration variable, each original link occurs in one polynomial density. Averaging over gauge transformations at both ends preserves the per-link degree bound. On a fixed larger cube, cut the flow at its boundary. The factorial tail from boundary to target tends to zero with its radius, uniformly in spatial side. Consequently finite-lag moments pass under joint local convergence of the unflowed histories. These moments determine the spectral law on $[0,1]$, and the closed transfer interval retains the weight lower bound by Portmanteau. For the upper energy-tail bound one must use the open neighborhood at a slightly smaller cutoff, as G4 does. This review assumes the polynomial inverse-moment estimate reviewed by A4. [G4's approximation](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/8db82fd74f1c7eb35b9a845d9f8a6ac68571228f/yang-mills/g4/transfer-inverse-moment/flow-tail.md)

The continuum existence and physical mass-gap obligations remain open. The compact endpoint example takes large temporal coupling at fixed spatial side. The spectral window takes the infinite-time vacuum at fixed unit coupling. Neither limit constructs the required four-dimensional continuum theory. [Jaffe and Witten, problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Checks run in this session

Three native x86-64 PCP OS guests ran as parent, child and grandchild through the hosted recursive supervisor. The parent summed the two center twists on a four-edge ring. Its child checked 19,008 directed phase differences across sides 4, 6 and 8 and all eight three-dimensional twists. Dropping the seam changes 1,392 differences. The grandchild enumerated the eight three-time histories of a stationary two-state chain. Each child result was read back after exit. All three desk nodes finished. The resulting Lean file checks the five finite arithmetic statements, the interpolation square identity, the mass subtraction and the exact cutoff ratio. The general compact and spectral proofs are written in the two notes. [Worker](worker.c) · [Lean source](SlabReview.lean) · [Execution records](receipts.zip)

The final run rejected a malformed guest request, two altered counts, a dropped predictor cross term and a substituted one-sided error. The release uses PCP OS source `92623fa6759bbb4e4f27ce5aa381de213a55ae0c`, measured kernel `0232c02a8946d66216da0ac65953a246ce3d41d7a966ae31aa83c3335b3259e3`, Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`. The ELF SHA-256 is `b379620c8d852367860dde17a793d172606411c2bb84ad734541e580ca9a0477`. The generated source SHA-256 is `aff561d085f9d513ed5f4b5bd47b4048d4923ef6c655dd55383d8812bc148d6a`. Earlier development runs encountered missing Lean imports. The final source compiled and passed the mutation checks.

The separate host calculation compared line eigenvalues and actual link energies on 24 compact twist cases (maximum absolute difference $3.42\times10^{-13}$ or less), tested three lags of a three-state Markov chain by direct path sums, and integrated six one-link Haar tilts. I also reran G4's published control scripts and compiled the 9, 8 and 7 supporting declarations at the respective PR revisions. [Independent checks](check.py) · [Execution records](receipts.zip)

The Enterprise ACR method verifier matched 57 payloads to the release manifest. Fresh PCP OS boots of the byte-readback fixture distinguished exact input, altered bytes, truncation, extension, absence and denial. The Fidelity Audit Lab 0.1.0 archive verifier matched 16 package files and 10 pinned sources. These identify the calibration material and checks actually executed.

From this directory, use a fresh output path and the pinned [kernel and toolchain](../clustering/execution.md).

```sh
python check.py
python verify.py --pcp-os "$PCP_OS" --kernel "$KERNEL" --desk "$DESK" \
  --delegate "$DELEGATE" --qemu "$QEMU" --firmware "$FIRMWARE" \
  --lake "$LAKE" --mathlib "$MATHLIB" --out "$FRESH_OUT"
```
