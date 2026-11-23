# Audit checks

The [quaternion control](check.py) applies all eight combinations of link reflection to one full-rank, noncommuting background and two distinct transverse fluctuation fields. It independently reconstructs the target plane from site-gauge singular vectors and evaluates the induced volume from the 42-dimensional metric determinant. Maximum absolute errors were $3.56\times10^{-15}$ for plane isometry, $2.23\times10^{-16}$ for the two magnetic actions, $1.12\times10^{-16}$ for the temporal action, and $1.37\times10^{-15}$ for log volume. These probe exact identities at finite displacements. The differentiated operator estimate is a written proof.

The [charge-order audit](../../../one-site-vacuum/excitation/charge-order/README.md) includes a direct angular metric and fit sensitivity check. Three [native PCP OS workers](worker.c) generated the common [Lean lemmas](ReflectionAudit.lean) in a host-mediated parent, child, grandchild sequence. Generation and fresh replay matched all three ELF hashes and the Lean SHA-256 `441b9fd105fd4b770505880a0eb09f03f955491ed9ecaddc744a62131c26b99e`. The measured kernel was `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`, with 47 register events per boot.

| Guest | Control | ELF SHA-256 |
|---|---|---|
| Parent | Square-group action on the Gram anisotropy variables | `c0ee79139dc7404e2ac91afa3afbd4e9a408c6fd482fa47d33f4776acac23757` |
| Child | Strict ordering of squared angular indices | `3d78dabdac0152b87eeb1253fd0e429bcf0250518b82b0ba55d061ff3a74fa95` |
| Grandchild | Cancellation of every cubic monomial under axis reflections | `1121d1980948c0b60e6a50ee1bd7169ce33d2f595f1cf83c68cbf30174b26f8d` |

Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked six declarations using only the standard axioms. They cover the Gram determinant, reflection commutation, the continuous-rotation degeneracy constraint on a diagonal block, charge ordering arithmetic, odd cancellation and a scalar lower bound. Neither analytic spectral conclusion has an end-to-end Lean proof. Run the [replay driver](../../../transfer-increments/replay-guests.py) and controls from this directory.

```sh
python ../../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ReflectionAudit.lean
lake env lean ReflectionAudit.lean
python check.py
python ../../../one-site-vacuum/excitation/charge-order/check.py
```
