# Numerical and native checks

The Python check integrates the finite-lattice one-leg density in the slab $H<|p_3|<2H$ with transverse integration truncated to $|p_i|\le16\pi$. It tests the transverse characteristic function of the exceptional leg. At dual momentum $(1,1/2)$ the limiting value from the spline is $597627/9895936$. The slab readings at $H/(2\pi)=4,12,24$ were respectively 0.06102470, 0.06046699 and 0.06041027. At $(4.5,0)$ the exact limiting value is zero and the absolute last-slab reading was below $10^{-7}$. Fifteen periodization checks include both edges of the representative momentum interval. The conditional Wilson limit and tightness use the analytic estimates in the [proof](proof.md).

Three freestanding executables ran in separate PCP OS boots. The host relay followed the parent and child requests and matched the three emitted records. The parent checked exact spline evaluations, the child enumerated finite transverse convolutions with a signed exceptional leg, and the grandchild tested the size-biased order recurrence for ten successive orders. Each guest exited 0 and its serial register showed 47 events.

| Guest | Executable SHA-256 | Observed kernel register head |
|---|---|---|
| Parent | 9f32ae621a91f2e5b65130a8011121f56ca3f934a3fec4a5aeb9d5a604a91308 | 945e1d438539436ac86bad122df46a344147c822759b18fd21d819b97335a6ba |
| Child | a30778321db82786746e9b9179fbfa7119afb9c7a51ae01b542df9336bb9a044 | 8a2ed2fb38017574cd1fcdfb0400ea2a976c97fe7b2abfe6ab9917a68f052451 |
| Grandchild | d9827c6bc40fdb9e61db019231e6bfe29fda8d93777439df7de7194508f93f41 | cc9bf1846d9013ffa1eff8f7a42f3ad522840f56b292055e38a819c87596ac1e |

Kernel file SHA-256 was d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f. The three-line record SHA-256 was e06bd40abd15bc26917a232d9c8fc26da86704ecd5f5d2c2933e0c006ab2a99f. To reproduce from this directory with NumPy, QEMU and the kernel available, run the following commands. [Host relay](../../../../observable-normalization/transfer-increments/replay-guests.py) · [Guest source](worker.c)

```sh
python check.py
python ../../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```
