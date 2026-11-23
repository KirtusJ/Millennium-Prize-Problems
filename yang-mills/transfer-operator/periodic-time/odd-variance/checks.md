# Checks of the reflection and window comparison

The Python checker evaluates all 16 corner monomials using complex SU(2) matrices on a random five-site-per-side torus. All 64 signed reflections agreed to absolute tolerance $2\times10^{-15}$. Omitting the corner toggle gave a discrepancy above 0.01 in every direction. Four box sizes supplied 230,528 checks of invariance of the site-to-cell coefficients in interior directions. Separately, A4’s quaternion torus calculation reproduced total charge 2.8911380360 with agreement between the site and cell sums. [Independent checker](check.py) · [A4’s torus and Gaussian checks](../../../observable-normalization/transfer-increments/local-action/odd-clover/check_odd.py)

The checker also compares discrete sine autocorrelations through width 64 with those of a sufficiently large normalized box. As a numerical example, take the positive spectrum $1+2\sum_i(1-\cos p_i)$, whose bulk variance density is 1. The excess above 1 at width $h$ illustrates the rate of the window error. This example tests the window calculation; the Wilson bound uses the analytic local comparison.

| Width | Box excess | Sine excess | Sine excess times width squared |
|---:|---:|---:|---:|
| 8 | 1 | 0.4824590 | 30.8774 |
| 16 | 0.5 | 0.1362152 | 34.8711 |
| 32 | 0.25 | 0.0362246 | 37.0940 |
| 64 | 0.125 | 0.0093422 | 38.2656 |

The PCP OS relay followed guest requests through three generations. The parent checked all ternary boundary patterns and detected changes in some singleton directions. The child checked side-two slab reflections at separations 1 through 128, and the grandchild used integer tent windows to check translation costs and box domination by exact arithmetic. Each guest exited 0 with 47 register events. One earlier grandchild boot stopped at the kernel keyboard-wakeup self-test before starting the worker. [Worker](worker.c) · [Expected output](checks.txt) · [Relay](../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Register head in the complete run |
|---|---|---|
| Parent | 3e03016c6893ee9ba22f5fb9463deabdf7be81a05c5441778a5068542501734f | 1bcb5d5e3bb4577c42a316f1ef4314bb3e6f202f4b56f9254a5b381d6a6357a4 |
| Child | f70f10edd1d47677515bacd682af738e8a7f697448780cc5d6efcefd9741c1f2 | 53a6b28da136091702a5acc27d86756ce994ef1a27778fee48c74e471c0bbb85 |
| Grandchild | 2b7b00115315b6d8a75a2640668765f5609d7ac19de08f23434dc792a5cebce6 | af7eb54b04277c58d46d322b1142d9c5d2e9a1b4ee429d2149dae0f72df114dc |

The pinned kernel SHA-256 is d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f and the generated record SHA-256 is 7884e2fec7424fc76f37c962bb8d3239a1336ad89bc8acdd35c99b80e361c233. To reproduce with NumPy, gcc, QEMU and the pinned kernel available, run the following commands from this directory.

```sh
python check.py
python ../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```
