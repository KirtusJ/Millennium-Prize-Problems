# Checks on the fixed periodic-box spectrum

The [central and magnetic calculation](README.md) and the [full-box shell and exterior argument](full-neutral.md) are written proofs submitted for independent review. The following controls exercise the algebra and test the two extensions beyond period two. None of the finite programs certifies the full spectral theorem.

The [plaquette control](check.py) differentiates the exact quaternion Wilson action along two oppositely rotating transverse real color fields of unit norm. The measured first derivatives at zero constant background are $0,0$ on a $2^3$ cube, $\pm3.4641016$ on $3^3$, $\pm4.0000000$ on $4\times3\times2$, and $\pm3.8042260$ on $5\times2\times2$. These agree with $\pm4\sin(2\pi/N_1)$. A separate exact integral propagates a central vacuum Gaussian in a two-channel model from the side-three pair. At background increments 0.02, 0.01, 0.005 and 0.0025 the uncorrected residual at the chosen test points is respectively 0.005615, 0.002762, 0.001369 and 0.000682. Adding the first-order excited-state correction gives 0.0002063, 0.0000512, 0.0000128 and 0.00000318. Here the coefficient of $(z_+^2-z_-^2)\gamma$ in the correction is $-a\coth(\omega)/4$ with $a=4\sin(2\pi/3)$; it follows independently by differentiating the two Gaussian widths.

The [shell and winding control](check_global.py) discretizes the single transverse Gaussian in position space and squares its top eigenvalue. At $\kappa=1/8$, the two-coordinate deficit divided by $r$ is 0.062014, 0.062256 and 0.062378 as $r$ halves from 0.25, approaching $\kappa/2$. On four differently shaped periodic boxes it also compares direct momentum heat traces with the complementary winding expansion using scaled modified Bessel functions. The two agree at three heat times; the central trace is strictly greater at the sampled noncentral twist and a full grid shift leaves the oscillator sum unchanged.

Three native [PCP OS proof-template workers](worker.c) emitted the [Lean file](PeriodicSpectrum.lean) in a host-mediated parent, child and grandchild sequence. Separate generation and replay matched all ELF hashes and the emitted source SHA-256 `b6c70474d128cddd2480a92d5fa9813ebe0b36e1ef7326d25c99162c3e58842e`. Each boot recorded 47 register events with measured kernel `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`.

| Guest | Finite control | ELF SHA-256 |
|---|---|---|
| Parent | Based orbit, slow and hard dimensions on fixed rectangular graphs | `a5ee6ec75e1cd61619218493c84109faad031132648f6c47663f2082de813b69` |
| Child | Color rotation average of a linear background covector | `0f803cf59f955fa022895f2973473cdd4db2cf768b2fe44446468eb966b1a449` |
| Grandchild | Absorption of a mixed block into the complementary spectral gap | `6a913a50f6fc2310f988d3f2a2d34a3378c357fda63e8f400aa251717516a805` |

Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked eight scalar statements, including the volume dilation, corrector sign, strict winding deficit and shell absorption. All checks report only standard Lean axioms. Changing the slow kinetic coefficient or reversing the forcing sign in the corrector each caused compilation to fail. From this directory run the [three-guest replay](../transfer-increments/replay-guests.py) and the two numerical controls.

```sh
python ../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof PeriodicSpectrum.lean
lake env lean PeriodicSpectrum.lean
python check.py
python check_global.py
```
