# Checks for the reflected-strip estimate

Two PCP OS runs each booted three deterministic native programs in succession. The parent requested the child, the child requested the grandchild, and the host relayed each request. Each guest ran a finite arithmetic control and reported a 47-event kernel register. Both runs emitted the same Lean source. The host checked the five declarations with Lean 4.19.0 and Mathlib commit `c44e0c8ee63ca166450922a373c7409c5d26b00b`. Every axiom report lists only `propext`, `Classical.choice` and `Quot.sound`. [Guest source](worker.c) · [Generated Lean source](ReflectedStrip.lean) · [Execution convention](../../execution.md)

| Item | SHA-256 |
|---|---|
| Kernel ELF | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent ELF | `dfa91cba9fefd81911f6b374c5f60e7a7c9085384a7f7b498bdef0db428bf0f4` |
| Child ELF | `0dbcda6d3f13bfa04e83f38564a6a340d671dc931e8a8b8a92d1a51673269791` |
| Grandchild ELF | `b88c525754909e09c7273bbfc87eebccb045cac5198e8af8b8a48671aa403411` |
| Generated source | `101276928ff07ff3f85961ae0405dc8af4038353c23c248beacfcf3e0a93e314` |

Lean proves the initial step of a bounded convex sequence is nonincreasing, the scalar strip deficit bound on $[-1,1]$, the finite square-root weight inequality, the combination of the cubic and quartic bounds, and the seventh-power scale substitution. The construction of the Gram space, Wilson path estimates, Haar variation and transfer applications have [written mathematical proofs](README.md).

Two altered Lean files were rejected. Replacing $n(1-x)$ by $n(1-x)/2$ already fails at $n=1,x=0$. Strengthening the scale conclusion from $c^7$ to $c^8$ fails at $R=1$, $s=2$, $c=1/2$.

The [finite controls](check_strip.py) perform three different checks.

* Free reduction and cyclic base-point changes recover the trace of the rectangle for 588 reflected staple pairs. Direct comparison, before taking any trace, identifies the conjugating prefix and oriented rectangular boundary for every block swap in 648 signed ordered-path insertions. These include negative time coordinates and backwards spatial steps.
* For an open two-dimensional strip with gauge group $Q_8\subset SU(2)$, independent axial-gauge plaquettes have weights $k^2,1,k,\dots,k$ on $1,-1$ and the six imaginary units at $\beta=\log k$. Exact convolution on all eight elements yields $W(n)=r^n$ with $r=(k^2-1)/(k^2+6k+1)$ for all 96 tested pairs of coupling and length. At $k=4096,n=24$ the ratio $(1-W(n))/(n(1-r))$ is $0.983356651$. At fixed $n$ the ratio tends to one as $k$ increases. This checks sharpness from the strip moment hypotheses alone.
* A coherent rotation has $W(n)=\cos(n\theta)$. At $\cos\theta=3/5$ its first two-by-two staple Gram determinant is $-16/25$. At $\theta=\pi/64$ the claimed linear deficit bound fails at length 64. Translation symmetry and a small plaquette deficit alone do not imply the strip bound.

Run these commands from this directory with the kernel and QEMU environment in the [replay instructions](../../execution.md). Run the last command from the pinned Mathlib checkout using the full path to the generated source.

```sh
python check_strip.py
python ../../replay-guests.py "$KERNEL" --proof ReflectedStrip.lean --qemu "$QEMU_WRAPPER" --firmware "$FIRMWARE"
lake env lean /path/to/ReflectedStrip.lean
```
