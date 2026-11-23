# Checks on the joint slow–fast comparison

The [numerical control](check.py) constructs the exact 24 spatial Wilson plaquettes in additive quaternion coordinates. At a three-color noncommuting background $c=tX$, central mixed differences of all 42 hard variables give $\|M_{tX}-M_0\|/t^2=0.931982,\ 0.932644,\ 0.932809$ for $t=0.2,0.1,0.05$. The central eigenvalues reproduce $4,8,12$ with multiplicities $18,18,6$. An independent directional check at five couplings tests the joint magnetic expansion after removing the constant quartic and the central quadratic. At $h=0.005$ the residual divided by $h$ is $-0.0007060$ in the selected hard direction. It halves with $h$ even before averaging over four proper color rotations. An initial test expecting an order-one directional limit failed; the vanishing two-site derivative in equation (1) explains the discrepancy. At momentum $\pi/2$, available on a four-site side, the charged-symbol derivative is instead four.

The [written proof](README.md) establishes operator estimates, compactness and the spectral conclusions. Three native [PCP OS proof-template workers](worker.c) emitted the [Lean checks](JointSpectrum.lean) in a host-mediated parent, child and grandchild sequence. Generation and an independent replay gave identical source bytes with SHA-256 `e3a7803460ffc91de2527555a3957865f2ef40e488554fc9e756c2cb4eb2ff30`. The measured kernel was `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`; each boot recorded 47 events.

| Guest | Finite control | ELF SHA-256 |
|---|---|---|
| Parent | Every nonconstant Walsh mode has zero mean | `b08bc0f3d116b180b18572211c9c30169b3fb45c928adf5e8d68dcd967b88fc9` |
| Child | Squared off-diagonal mixing is absorbed by a positive complementary gap | `05459927430cb37291ad9b29805f6dc4603b4b0546ca90b176d87f015d88f89e` |
| Grandchild | The eight even-center images are permuted by every center action | `f4926b7c21af031beb12ddea23e62da8d0e424489de7b8c37e60be2451a4d54b` |

Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` verified six scalar declarations. They include the volume factor, the matrix dilation, the quadratic tilt identity and a counterexample to subtracting variational upper bounds. All axiom reports list standard Lean axioms only. A doubled slow diffusion constant and an unsquared orbit tilt each failed compilation. The spectral theorem itself has a written proof and awaits independent review. From this directory use the [replay driver](../../transfer-increments/replay-guests.py) and controls.

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof JointSpectrum.lean
lake env lean JointSpectrum.lean
python check.py
```
