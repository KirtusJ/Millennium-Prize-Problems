# Checks on the one-site spectral limit

The analytic proof is in the [research note](README.md). Three PCP OS guests executed in parent, child and grandchild order. The host followed the child requests emitted by the first two guests. The measured kernel hash was `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. A second run reproduced the three guest binaries and emitted source bytes, with 47 register events in each boot.

| Guest | Finite control | Replay ELF SHA-256 |
|---|---|---|
| Parent | Tested the radius-dependent block length and the number of eligible late times for rational radii through denominator 80. | `8a09dd5f65b8043a315e4cfc683e8d0c1e17fe40003ec6deb5db71fb59d6bf8e` |
| Child | Enumerated products of three representation dimensions and checked the maximal-Casimir bound used in the frequency cutoff. | `2f05680f096d20d8e4846741581bbeca78a25fbba41bc37ebf89f34ca3600f4f` |
| Grandchild | Checked the isotropic component covariance normalization against six signed axes. | `0601923a4280928a7ac5e35b68d7b32514c0d9121f50827e7ce3d23bd4ef7e5d` |

The [generated Lean source](ToronExcitation.lean) has SHA-256 `c4974a58245dffc73ad76cc9c326208ef4cde6a9aaa10cec16c9135be74e25ec`. Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked seven declarations, including the implication from convergence of both scaled energies to an eventual positive lower bound. Their reports list only standard Lean axioms. Changing the power in the fiber scale identity and dropping one of the two eigenvalue errors each failed compilation. The confinement, compactness, consistency on test functions, and spectral convergence are written proofs.

The [independent generator check](check.py) evaluates the symmetrized Wilson transfer against a smooth center-even Gaussian reading using a numerical Wilson radial CDF and 65,536 scrambled Sobol points with antithetic increments. For two directions its rescaled action at the test configuration was 1.4267003, 1.6376896 and 1.6605124 for couplings $10^3,10^6,10^9$, with limiting value 1.6631858. For three directions the values were 1.7200833, 2.1231812 and 2.1677686, with limiting value 2.1726461. This pointwise quadrature checks the kinetic and potential normalization. It does not compute the first excited eigenvalue.

From this directory, run the [host replay](../../transfer-increments/replay-guests.py) with the supported kernel and compiler. The Python control requires NumPy and SciPy. [Native source](worker.c)

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ToronExcitation.lean
lake env lean ToronExcitation.lean
python check.py
```
