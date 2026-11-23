# Numerical and native checks

The numerical program integrates the exact scalar time-slice spectrum and its squared momentum gradient over the full three-dimensional lattice momentum cube. For $M=1/16$ and $Mn=4,16,64,256$, the squared slice norm divided by $M e^{-2Mn}(Mn)^{-3/2}/(32\pi^{3/2})$ was respectively 0.889206, 0.966911, 0.991049 and 0.997488. The second spatial moments in units $n/M$ were 1.43285, 1.47787, 1.49330 and 1.49756. Quadrature orders 40 and 60 agreed to the relative tolerance in the code. These checks use the exact lattice threshold in the exponential.

A second calculation summed the squared lattice propagator in time against $e^{-a/|t|}$ at $M=1/8$, integrating over all spatial sites by Plancherel. The table gives its ratio to the temporal saddle integral with the continuum low-momentum coefficient. The calculation stops at $Mn=6\sqrt{d/2}+32$ and uses independent momentum quadrature orders 32 and 48. A separate sum of the asymptotic integrand reproduced the analytic half-line integral in all nine cases. The analytical spatial second-moment estimate in the proof justifies insertion of a fixed spatial cutoff in the limit. [Numerical implementation](check.py)

| $d$ | $a=1/4$ | $a=1/2$ | $a=1$ |
|---:|---:|---:|---:|
| 256 | 0.913133 | 0.935711 | 0.952804 |
| 1,024 | 0.952804 | 0.965522 | 0.974860 |
| 4,096 | 0.974860 | 0.981645 | 0.986539 |

The native PCP OS relay followed two successive guest requests, running three freestanding executables. The parent checked the lower bound on four-dimensional mesh counts, the child checked finite Fourier Plancherel identities for the squared norm and a frequency difference, and the grandchild checked the exact saddle identity and the critical sign. All three exited 0, with 47 register events each. The finite checks supplement the uniform analytic bounds. [Worker source](worker.c) · [Expected output](checks.txt) · [Host relay](../../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Observed kernel register head |
|---|---|---|
| Parent | 47678da1e789adaf04b106cd4e56f19731e6f969ec285e8a2ff38bfbc4b57479 | 76a73bd358c9b8f0a94947c705c0afecf9fe6ade07dcb1ec089522f57f6d4de3 |
| Child | 97604e646d702c5e7833b90d1b7af89db553e3265271e6de9d5a866da7a918bd | 4a6398dcefc3bc107135a991e69cfb0f0314066db50f9f9a48fa35be6d26b494 |
| Grandchild | 60971adfbbf0d67642693aed0e9ff5f9f779a4e0c7edca311b540c22cd7f2b4b | 0e23628322a45a089e8baa4794c5d091bd07dfdee5e7a95c5145be8d7fa12ca5 |

Kernel SHA-256 was d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f. Guest-generated record SHA-256 was ed54665662c2238a3d8e54ee5e3c6b90d45d37f53a24b4c187790b0ae6594c32. From this directory with NumPy, gcc, QEMU and the measured kernel available, run these commands.

```sh
python check.py
python ../../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```
