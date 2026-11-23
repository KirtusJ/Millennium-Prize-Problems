# Reproducing the electric endpoint

Three measured PCP OS guests emitted the root, child and grandchild segments after explicit requests. A fresh deployment reproduced the authored source byte for byte. Host Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` accepted eight declarations. Every axiom report contained only the three standard axioms. [Kernel and replay settings](../../../smeared-plaquettes/action-curvature/execution.md)

From this directory run

```sh
python ../../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ElectricEndpoint.lean --qemu /path/to/qemu-wrapper
```

In the pinned Mathlib checkout run `lake env lean /absolute/path/to/ElectricEndpoint.lean`. The separate replay returned

```text
w0.elf 7c51f363e0d7a3827223665fe121d37f5b0c568db20196aff9d71b35544095b6 kernel register: 47 events, head f55fd5e0c6a70836bd941cf759aef28b96cad17b60c30bf2285d27fcdbd4c6fa
w1.elf 85c37973d47524c94d852e6a68fc9f4aba2b0409a1ce883774448d34da2ca317 kernel register: 47 events, head 8654f589912f43fb8b9c7ae7ed1d033ee844d3c7e48163a9b1559e6ae24e6e1f
w2.elf 48aa1c2e9f2506da8a8db25f9b49679987ed7ccef1a707a57be7c036a1dd90c3 kernel register: 47 events, head 20b57fbe42bba1b3658fb83baab0a1170d6e3c22a57bc2ce42ef1837139bdc09
generated source SHA-256 7d70a91f4d3a859698184915667043f71c4c0f8104c0aaa3be9f2a8e4c6eb963
```

Lean verifies the exact variance identity, completion of the kinetic budget square, the two branches of the sphere inequality, the uniform quadratic envelope, the norm-to-first-moment bound, the $\kappa/18$ endpoint and preservation of the band weight. The operator and moment inputs come from the earlier finite-box calculations linked in the main note. For adverse controls, replacing $99/32$ by $3$ fails at $u=575/864$, where the quadratic is 1329409/442368. Doubling the weight in the last extraction step is false for its hypotheses with $A=D=M=1$, $U=4$, low contribution $1/4$ and band weight $1/8$. Both mutated files were rejected.
