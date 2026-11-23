# Execution record

B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

## Free integrals and an adversarial rank check

Run the sibling Python checker with NumPy. It integrates the whole lattice Brillouin zone at each finite radius. The continuum integral uses cutoffs 36 and 48 as a numerical cross-check. Equal-time convergence over the full continuum domain follows from the integrable majorant in the proof. For $s=4$ the one-color continuum covariance at lags $0,1,2$ was $0.29257135$, $0.01742004$, $0.00153602$. The corresponding connected readings were $0.0470244431$, $0.0000701797594$, $0.000000544463591$.

| Packet radius | Maximum absolute discrepancy from the continuum over three offsets and three lags |
|---|---|
| 4 | 0.0409737 |
| 8 | 0.00916544 |
| 16 | 0.00222715 |
| 32 | 0.000552813 |

For the window $(2,4.2)$ in scaled energy, restrict each of the two momenta in the first term of the spectral expansion to the reflected boxes specified in the checker. Every such pair lies strictly inside the window. The four eigenvalues of this restricted free Gram matrix were approximately $9.05\times10^{-9}$, $1.49\times10^{-7}$, $3.91\times10^{-7}$ and $6.69\times10^{-7}$. Two quadrature orders agreed. Repeating the last displacement made the least eigenvalue zero to numerical precision. The estimates on the interacting state come from the analytic comparison; these numbers describe the free integrals. [Numerical implementation](check.py)

## Three native PCP OS worker boots

The existing host relay booted a parent, a requested child and a requested grandchild under QEMU, checked each measured image and exit, and matched the emitted lines byte for byte. Each role ran its own freestanding executable. The first guest checked eight exact convolutions, including the long-difference telescope. The second checked 6,125 signed paths for a purely magnetic primitive. The third tested 625 finite Gram forms, a repeated displacement and an empty energy window. These are finite tests of specific proof steps. The analytic estimates and full-rank theorem are written proofs. [Worker source](worker.c) · [Expected output](checks.txt) · [Host relay](../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Kernel register head, 47 events each |
|---|---|---|
| Parent | 5407a20e0751c304ca27dc6933d8256f84967e9519c4e0db43acdb305ef02aa4 | 050c3209d18527d06184a00f7417a2f6697e6e11cb21b7dfd6417a2aa1c84075 |
| Child | 21f04b4b7c37c7de512b0e58dc87ed3f7c932162f2e7a6c9e4a19447a00d439f | 519e84b520c8c4c1b9bbc996674616418aab149922113d5d972eba217dd80599 |
| Grandchild | c7d6ef98ecb2281d65bc4559f4a58ca8a4855aa640d740affb67667e392d123f | 405e3b689c3cf4bcfde650283cd1643f707ee7bff73409d8404fb1561068e00b |

Kernel file SHA-256 was d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f. The guest-generated check record SHA-256 was 68a84620ef6d2416243ffa6993882dfd9557329866aeabde3bf4c5d1fe82a7cd. From this directory, with the pinned kernel available and QEMU on the host path, run the two commands below. The relay also accepts explicit QEMU executable and firmware paths.

```sh
python check.py
python ../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```
