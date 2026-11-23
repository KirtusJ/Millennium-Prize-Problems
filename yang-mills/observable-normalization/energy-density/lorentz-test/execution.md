# Replaying the boost and positive-time estimates

The root guest requested the spectrum worker. That worker requested the limit worker. The host supervisor launched each requested role in a fresh PCP OS guest, checked its measured image, ELF digest, completion and kernel self-tests, and assembled the emitted Lean source. The three workers executed authored templates. A second complete hierarchy reproduced the same bytes. The public kernel and QEMU 10.0.13 instruction-counted invocation are pinned in the [earlier replay record](../../smeared-plaquettes/action-curvature/execution.md).

From this directory run

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof LorentzTest.lean --qemu /path/to/qemu-wrapper
python check_shells.py
```

At the [first revision](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/ad7901cc3ed9db23f3f4c2d4a91a7c1083da9175/yang-mills/observable-normalization/energy-density/lorentz-test) the second run returned

```text
w0.elf c8332f9de0f9d1b4f0f0e49529a57af757c02af6c59a4137d9ecd48b0527a3b4 kernel register: 47 events, head 9881b99239bc13f14a4c53b77f33d1bef9195b675035a8b973b85fa5f43ffe65
w1.elf e6511bbb9cd90026017f654d4035810bdc0792e2f0130a7b61f7e608cbe82c44 kernel register: 47 events, head 8fb07a85476e80bace2046c7874a8ca3117d9f7393e2df921b9561161db26b84
w2.elf 43df8e7aac0ca82886e2caabe00a8b842d6b4e58fc20a48048e2688e626f8dd6 kernel register: 47 events, head 1f1bddaa6387717f7f577f59eef4872f5e4d5e94ebc6db869ecc6710d9798715
generated source SHA-256 c4e20c959c4fc209778dce497862de616a49cad65d162809b086520975f3bff6
```

Host Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked the emitted source with exit status zero. From that Mathlib checkout run `lake env lean /absolute/path/to/LorentzTest.lean`. Each of the fourteen printed declarations used only `propext`, `Classical.choice` and `Quot.sound`. The file checks the boost and projector arithmetic, the shell cancellation, the pointwise detector estimates, the integrated upper bound, monotone exhaustion, the finite-resolution inequalities and the contradiction for arbitrarily large dilations. The lattice Hamiltonian estimates, covariant disintegration, identification of the target component, spatial Fourier scaling and application to the successive limits are analytic steps in the accompanying notes.

Two altered files failed Lean. Replacing the null boost multiplier by the opposite rapidity already fails for cosh(y) = 5/4, sinh(y) = 3/4 and unit amplitude, where the two predictions are 4 and 1/4. Allowing the largest required test threshold to be min(1,R) removes the arbitrarily fine probes. The modified conclusion fails with c = A = L = 1 for every R.

The numerical control used two quadrature orders on the smooth radial test. Columns are dilation, massive improvement tensor, null improvement tensor and time component of the unit-mass conserved vector. The first line gives the largest residual for the boost and conservation calculations.

```text
maximum matrix residual 6e-15
1 0.7958578261 1.095531582 0.3001220987
4 1.072672258 1.095531582 0.02552215645
16 1.094083639 1.095531582 0.001628050898
64 1.09544101 1.095531582 0.0001018836476
```

## Polarization of the full symmetric tensor

The current source adds two declarations for the timelike contractions. Repeating the generation and the replay above returned

```text
w0.elf c8332f9de0f9d1b4f0f0e49529a57af757c02af6c59a4137d9ecd48b0527a3b4 kernel register: 47 events, head bda1e5ec53fd8bdacc63a8d4a77bbcbcab066a1f2e7faf94df2ab59883bec7e7
w1.elf 2cae35e5c3d2ffb56f3d3582a1a7e48e5839ec0930a15d6d27758f4b56d4ab13 kernel register: 47 events, head 26903259e7576240b76b460540d44a97baf79f95b35e61e796303e3fc7ed428b
w2.elf 721a5c08b423212032717d0b5a2a35d3aa45f5efbd3daeab4d9e0a7f0dede970 kernel register: 47 events, head 5d9ae3ccc003570c904b5ae32a7e2c965745c03a3ca0a808580f6aa6dc0d3003
generated source SHA-256 af4ae926fa38e297c8cd8e9fc26110b219cbba850403c27d8a92ccd876141532
```

All sixteen declarations checked with the same three standard axioms, without warnings. In a copy of the source, deleting the shear contribution from the diagonal measurement made `shearPolarization` fail. The tensor with unit 12 and 21 entries and all other entries zero satisfies the altered premises.

The control script uses NumPy and SymPy. It constructs the observation matrix in the four diagonal and six off-diagonal components over the rationals. Its absolute determinant is 1/64, its first seven rows have rank seven, and the maximum absolute row sum of its inverse is eight. The annular controls reproduced the values above. These checks verify polarization and numerical conditioning. Lorentz covariance of a candidate field and invariance of its vacuum remain hypotheses.
