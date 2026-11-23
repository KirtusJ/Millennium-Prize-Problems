# Verification of the spatial-packet estimate

Two complete PCP OS runs booted a parent, child and grandchild, with the host dispatching the next guest after the preceding request. All six guests finished successfully and each reported a 47-event kernel register. Both runs emitted the identical [Lean source](SpatialPacket.lean). The host checked its six declarations with Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`. Every axiom report contains only `propext`, `Classical.choice` and `Quot.sound`. [Guest payload](worker.c) · [Replay convention](../execution.md)

| Item | SHA-256 |
|---|---|
| Kernel ELF | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent ELF | `91574a967e93835b39a57089bfe4a545f2c7c32d8fb949edb9ca85d0de6059d3` |
| Child ELF | `e54ef792477e351b8e822a3375a957e1ab80849fcf310e49cb5937e081aaa4f6` |
| Grandchild ELF | `fe3a4277c1fd4a5743b61378ba3ec653c63ed2d64488e1e52949b138c494f1c1` |
| Generated source | `905549c9ce41981f630fe4a305e78223ddb7a5e852f896e5553921867afd4dd9` |

Lean checks the arbitrary-stride telescope, the finite path-charge inequality, the algebra combining the four heat sums given their scalar bounds, the eighth-power scale substitution, the single-reading implication for the gap and the lower bound on positive-band mass. Shifting the telescoping endpoint by one extra cell and improving $c^4$ to $c^5$ both broke the altered proofs. In the second case $R=1$, $s=2$, $c=1/2$ disproves the alteration. The [Haar comparison and heat estimates](comparison.md), the Fourier limit and the application to the Wilson state have written mathematical proofs.

The [numerical control](check_packet.py) checks the long-difference Fourier multiplier against a direct transform of the signed real-space tent. It integrates the free finite-lattice kernel by panel Gauss quadrature and a separate midpoint grid at $R=2,4,8,16,32$. Both rules agree to the script's relative tolerance $5\times10^{-8}$ and absolute tolerance $10^{-12}$. At $R=32$ the free one-color covariances in the infinite-volume lattice integral were $2.59914913,0.07869739,0.00452003$ at lags $0,R,2R$. With this packet normalization the corresponding connected readings at the last two lags were $4.06499\times10^{-6}$ and $1.33990\times10^{-8}$. Direct integration of the continuum integrand at times 1 and 2 gave $0.07849743$ and $0.00450702$ for the one-color covariances. The checks integrate free kernels. The unknown Wilson constants and the onset in $\beta$ were not estimated.

The following commands use the pinned local paths.

```sh
OPENBLAS_NUM_THREADS=1 python check_packet.py
python ../replay-guests.py "$KERNEL" --proof SpatialPacket.lean --qemu "$QEMU_WRAPPER" --firmware "$FIRMWARE"
```

From the pinned Mathlib checkout run `lake env lean /path/to/SpatialPacket.lean`.
