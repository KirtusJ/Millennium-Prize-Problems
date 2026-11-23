# Reproducibility

Run the Python checker with NumPy and SciPy. It directly builds the signed face-edge incidence matrix on cubes of radii 1, 2 and 3, projects the central face by least squares, and checks the normal-equation residual. An independent calculation uses a cosine transform along the edge direction and sine transforms transversely. These are the Neumann and tangential Dirichlet boundary conditions for the relative one-form Laplacian. Applied to $d^*\delta_p$, its quadratic inverse gives the diagonal curl projection. The two computations agreed to absolute tolerance $2\times10^{-12}$. The first radius also agrees with the exact $7/24$ arithmetic below. [Checker](check.py)

| Radius | Conditional one-color variance | $R^4 v_R$ | $R^8\operatorname{Var}(\mathbb E[X_p\mid\mathcal G_R])$ |
|---|---|---|---|
| 1 | 0.2916666667 | 0.2083333 | 0.0651042 |
| 2 | 0.4926748048 | 0.1172031 | 0.0206049 |
| 3 | 0.4991559926 | 0.0683646 | 0.0070106 |
| 4 | 0.4997835882 | 0.0554014 | 0.0046040 |
| 8 | 0.4999886021 | 0.0466858 | 0.0032693 |
| 16 | 0.4999993151 | 0.0448882 | 0.0030224 |

The three native PCP OS programs used the shared host relay. The parent enumerated 216 choices of a bridge and two lasso values in the noncommutative group $S_3$. For each, it counted the full joint orbits under two independent endpoint gauges and checked independence of the transformed bridge. The child solved all 48 oriented radius-one projection tests in integer arithmetic. The grandchild checked the conditional fourth-moment identity for 49 parameter pairs by a three-point rule exact to fourth order. They are finite controls for the identified steps. [Native source](worker.c) · [Expected lines](checks.txt) · [Three-boot relay](../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Kernel register head (47 events each) |
|---|---|---|
| Parent | da40ca31fa9eb2ca41ff00a4e86c6a9df9cce4e5b68499c0b7bc336d76490e9e | 6674763b49b0ef353c0715e85c47a0a8578faa91c49ff3238f795c4a197b7259 |
| Child | 88fb159aa1a71c136525b7499e31a05d3332e9af0f5dff540894d21d27e15087 | bdadda928d7977abf134f27d8dafa35a14465a7073abdb483530012ed81e29a4 |
| Grandchild | 34a2c10187326a74a07d48f2e5b9e7804d0ce1ffc1f12986216a7085fe453cc2 | 2afefb636ed0160f8246af9531e233c2cf3ff9a9d5f0fe3c1231d842459d4dfc |

The checker output by the guests had SHA-256 6eda228f476cdea12efecfefb7b8565473f8b25a0ab6e8a0befe9756b15ee9a6. Kernel file SHA-256 was d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f. An earlier boot failed the keyboard-wakeup self-test and entered SAFE before the first worker started. A complete retry with identical kernel and QEMU settings passed. The register heads identify the successful run.

From this directory run the following, with the pinned kernel and QEMU available locally.
```sh
python check.py
python ../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```
