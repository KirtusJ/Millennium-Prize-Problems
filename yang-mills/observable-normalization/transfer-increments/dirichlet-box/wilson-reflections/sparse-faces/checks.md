# Reproducing the sparse-face checks

Three PCP OS guests ran under kernel SHA-256 `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`. The host followed the parent’s request for a child and the child’s request for a grandchild. Each guest emitted its Lean segment after its finite check and recorded 47 register events. A separate replay reproduced the three executable hashes and all source bytes.

| Guest | Check | Executable SHA-256 |
|---|---|---|
| Parent | All sixteen reflected positions of the middle face keep their four cubes inside the cell | `fbd421a15ccf0a191c84eaeeb46137bf4c0e4e29aa8368307126ccaafc819932` |
| Child | Enumerating the four cube boundaries gives twenty distinct complementary plaquettes | `8af9ac02ae974bd8ef4144a3799093f0bce8f14d59c86b42cec9f1f135e1af16` |
| Grandchild | Enumerated dyadic sides 8 through 128 have exactly one marked cell per 256 sites | `cbca5bfc47e2d4985f710be85b776fd01d575af235e513b9341c062315293380` |

The [generated Lean source](SparseFaces.lean) has SHA-256 `74618141ca3392172224170fcb6f2fb4a863b5e6d4588282962987d14c3672ac`. Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked six declarations. The axiom reports contained only standard Lean axioms. The disk holonomy, dissemination, pressure bounds and probability limits are proved in the [mathematical note](README.md). Three stronger, false scalar variants failed compilation. Replacing five by four in the chord inequality exhausted the tactic heartbeat budget; the explicit tuple $(1,1,1,1,1)$ gives $25>20$. The other controls changed nine to ten in the cube budget and five to four in the pressure cost. Setting $s=5$ and all four disk sums to one disproves the first. Taking $S=9,P=5,\lambda=1$ disproves the second.

The [independent link calculation](check.py) realizes the sharp abelian curl data by exact rational linear algebra and checks 1,024 disk inequalities using seeded, noncommuting Haar SU(2) link matrices. The action ratio of the abelian example was 1.800006400 at angle 0.01. This tests local sharpness separately from the thermodynamic-limit argument.

From this directory with the supported kernel, QEMU and compiler available, run the native replay. Run Lean in the pinned Mathlib environment. The Python check requires NumPy and SymPy.

```sh
python ../../../replay-guests.py /path/to/kernel.elf32 --proof SparseFaces.lean
lake env lean SparseFaces.lean
python check.py
```

[Native guest source](worker.c) · [Host replay driver](../../../replay-guests.py)
