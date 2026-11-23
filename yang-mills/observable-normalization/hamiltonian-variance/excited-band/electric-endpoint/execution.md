# Reproducing the electric endpoint

Three measured PCP OS guests emitted the root, child and grandchild segments after explicit requests. A fresh deployment reproduced the authored source byte for byte. Host Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` accepted eleven declarations. Every axiom report contained only the three standard axioms. [Kernel and replay settings](../../../smeared-plaquettes/action-curvature/execution.md)

From this directory run

```sh
python ../../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ElectricEndpoint.lean --qemu /path/to/qemu-wrapper
```

In the pinned Mathlib checkout run `lake env lean /absolute/path/to/ElectricEndpoint.lean`. The separate replay returned

```text
w0.elf 7c51f363e0d7a3827223665fe121d37f5b0c568db20196aff9d71b35544095b6 kernel register: 47 events, head c602ec17305c9226cab37e5ecee3e52d43756739bf79e8821b6ac28cbf718923
w1.elf 85c37973d47524c94d852e6a68fc9f4aba2b0409a1ce883774448d34da2ca317 kernel register: 47 events, head e94faa844e09db97ab5f9583a09ca00793195e399b667d7c895935e6fd063cda
w2.elf a81c05bcab374f2bbb2e337339b0cc6877f38aeaed03c65e8a6647ba4a444da5 kernel register: 47 events, head 32b5c6fe7fec7724a0cafb1d6b9f06cb5baa20fc4ede22e5dff5ada6e841ec5c
generated source SHA-256 e535a64fab3d573a96ff85e7a1014a1b3306c33e432d2baeaec8151421af7402
```

Lean verifies the exact variance identity, completion of the kinetic budget square, the two branches of the sphere inequality, the uniform quadratic envelope, the norm-to-first-moment bound, the $\kappa/18$ endpoint and preservation of the band weight. The operator and moment inputs come from the earlier finite-box calculations linked in the main note. For adverse controls, replacing $99/32$ by $3$ fails at $u=575/864$, where the quadratic is 1329409/442368. Doubling the weight in the last extraction step is false for its hypotheses with $A=D=M=1$, $U=4$, low contribution $1/4$ and band weight $1/8$. Both mutated files were rejected.

The combined-band declaration selects the appropriate interval with the same mass bound. Two further lemmas establish the crossover in both $B$ and $g$. Replacing $17/64$ by $19/64$ in the endpoint comparison failed the Lean check.
