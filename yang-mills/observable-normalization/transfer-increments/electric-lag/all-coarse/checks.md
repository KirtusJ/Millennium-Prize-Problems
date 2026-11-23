# Checking the coarse-space derivative estimate

Three PCP OS guests executed in parent, child and grandchild order. The host followed the requests emitted by the first two guests. Kernel SHA-256 was `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. A fresh run reproduced all three binaries and the [Lean file](CoarseResponse.lean) byte for byte. Each boot recorded 47 events.

| Guest | Finite check | ELF SHA-256 |
|---|---|---|
| Parent | Enumerated every fine face on tori of side 8, 12 and 16 at mesh 2, 3 and 4. Tested the two-direction mesh incidence and uniquely recovered the face from its outside edges, including at the seams. | `28b72903b934c90d5e7024e11303adab90243189b1074aea844015768d60fbc1` |
| Child | Recovered segment labels from unchanged links on meshes 2 through 8, varying the insertion position and representation change. | `8244a0841457bbbf37e76eab819d63bb7cf6d904009fc39b68685548b20cefda` |
| Grandchild | Enumerated the possible numbers of newly occupied and erased edges and checked the lower bound on remaining support. | `0c07140a8054474e8162281f16c80aa175947aeddc2bd2cd15c7c8af6fa060ee` |

Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` accepted five declarations covering support arithmetic, the finite spectral sum, its absolute endpoint estimate and squared normalization. The source SHA-256 is `6016192eb71d6d624a299270e9db7418d2e8eebf7ad54c9842b205f37fa6f2e8`. Axiom reports list only standard Lean axioms. Relaxing the mesh-edge count from two to three and halving the endpoint allowance each broke the corresponding declaration. The transfer, vacuum, uniform operator estimate and restricting a history to the mesh are written arguments in the [proof](README.md).

The independent [Python control](check.py) builds a binary electric regulator directly in its edge-character basis. It tests all 63 nonconstant products of six coarse squares, acts with every fine plaquette and forms the defect-normalized matrix at $q=0.95,n=3$. Its Gram matrix has vanishing off-diagonal entries. The columns produce 3,536, 5,584 and 7,632 distinct output characters at mesh 2, 3 and 4. The respective norms on this test space are 3.497996, 1.866868 and 1.049472, all below the analytic upper bounds. The code checks sign reversal on every spatial face, including seams, and preservation of every even coarse link. Keeping just one outside edge per face gives collisions and fails the uniqueness test. Binary characters test support and orthogonality; the spin multipliers in the SU(2) proof use its electric spectrum.

From this directory run the checks with a supported kernel, QEMU and the pinned Mathlib environment. The Python control requires NumPy and SciPy. [Guest source](worker.c) · [Replay driver](../../replay-guests.py)

```sh
python ../../replay-guests.py /path/to/kernel.elf32 --proof CoarseResponse.lean
lake env lean CoarseResponse.lean
python check.py
```
