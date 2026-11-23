# Reproduction and scope

Two three-generation PCP OS runs produced the same [Lean source](InteriorLeakage.lean). A host supervisor read each parent request and booted the named child in a separate guest. Each of the six boots recorded 47 kernel events. The host checked the resulting source with Lean 4.19.0, Mathlib revision `c44e0c8ee63ca166450922a373c7409c5d26b00b`. All four declarations depend only on `propext`, `Classical.choice` and `Quot.sound`. [Guest payload](worker.c) · [Kernel and replay setup](../../../smeared-plaquettes/action-curvature/execution.md)

| Item | SHA-256 |
|---|---|
| Kernel ELF | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent payload | `f595adb951614c3b22fc01fc9218bac3286b577f934b9af73234800241ff7b4d` |
| Child payload | `79adb3fb1c8959f2620cbf8ed0a04f4633bd14fdd93e89bbdeaa5868e2f5d64f` |
| Grandchild payload | `eb321fb4d27d56079cbe24b90eee72aa3239c69e25db6d4a3a9d91c57d0176a2` |
| Generated Lean source | `80d0d17c6cec3c11697ec1afbb5893b20ce590fb38fc36c362b407a9fd811570` |

The formal statements give the lower energy bound with one leg near its peak, the attainable boundary energy, the criterion for an intermediate branch in the minimum of three affine costs, and its momentum range. Two negative controls changed the error allowance from $2\delta$ to $\delta$ and the upper range endpoint from $3k$ to $4k$. Both broke their respective proofs. For the first, take $k=1,r=2,p=1.9,q=0.9,\delta=0.1$ on the closed triangle. For the second take $k=1,e=3.5$. The oscillatory integral bounds, secant limit and sign at the intermediate crossing are proved in the [analytical argument](README.md).

From this directory, with the kernel, QEMU wrapper and firmware paths set for the local installation, run

```sh
python ../../../transfer-increments/replay-guests.py "$KERNEL" --proof InteriorLeakage.lean --qemu "$QEMU_WRAPPER" --firmware "$FIRMWARE"
lake env lean InteriorLeakage.lean
OPENBLAS_NUM_THREADS=1 python check_leakage.py
```

The Lean command assumes the pinned Mathlib environment is active. The [quadrature](check_leakage.py) integrates the exact finite filter on $1<E<12$, $0<z<1$, exploiting reflection symmetry. It splits the energy interval at the threshold band edge $1.1$. Composite Gauss rules of orders 12 and 18 agree within the script's relative tolerance of $2\times10^{-8}$ at orders 256, 1024 and 4096. The $E>12$ tail is omitted in both numerical rules. For these clocks its unnormalized integrand is bounded by $256[(E^2-1)^2+1]e^{-E^2}$. The analytical proof treats the full energy range.

At $m=4096$ the normalized threshold probabilities multiplied by the predicted power $m^d$ or $m^{2d}$ were 4.402194, 0.6394035 and 0.01874593 for $e=1.5,2.5,4$ respectively. The two-sided power bounds permit oscillating prefactors. The free estimates do not assume that multiplying by this power produces a unique limiting constant.
