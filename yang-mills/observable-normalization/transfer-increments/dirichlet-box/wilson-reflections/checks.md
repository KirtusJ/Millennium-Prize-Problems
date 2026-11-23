# Verification of the reflection and pressure comparisons

The three-generation [PCP worker](worker.c) emitted [seven supporting Lean declarations](WilsonReflections.lean). The parent checked the reflected layer counts on each even period from 4 to 64. The child counted retained plaquettes, free-link incidences and the negative-center configuration on four periodic four-cubes with sides 4, 6, 8 and 10. The grandchild checked the trial deficit inequality for all rational inputs $a/b$ with $1\le b\le24$, $-b\le a\le b$ and powers one through four. Each guest returned successfully with 47 kernel events. A second deployment returned identical Lean source bytes. The host supervisor read the native request and launched the next guest in the chain. [Replay implementation](../../replay-guests.py)

| Artifact | SHA-256 |
|---|---|
| PCP OS kernel | `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f` |
| Parent | `bfeb24d28d2676be0e276ac8efd5e8cc46b93e8c10bb9cccaeef50a5ba41b56f` |
| Child | `d13fdfd73fdfb0b3e90fbdd077b9c309551d657d41c12a78a0a683ee9b869a12` |
| Grandchild | `b54527f4386841cf3b3497e62cb47c4d93e267dbc44fb15ce56b1b618da6b061` |
| Generated source | `73366a09669653c794096151b662296e79c72d766fead815a7e74beb72d47299` |

Lean 4.19.0, Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`, accepted the forward shift, reflection identity, finite secant estimate, one-layer estimate, trial deficit, radial monotonicity and seam identity. The axiom union was `{propext, Quot.sound, Classical.choice}`. Reversing the forward shift in the reflection identity, replacing two by three in the one-layer estimate, and reversing radial monotonicity each made its proof fail. The positivity and measure-theoretic reasoning is supplied in the mathematical argument.

From this folder run

```sh
python ../../replay-guests.py /path/to/kernel.elf32 --proof WilsonReflections.lean
OPENBLAS_NUM_THREADS=1 python -I check.py
```

From the pinned Mathlib checkout run `lake env lean /path/to/WilsonReflections.lean`.

The [independent numerical controls](check.py) count images on a $4\times6\times8\times10$ torus in every one of the six orientations, and check the reflection of each contiguous occupied arc at lengths 4 to 64. In a separate two-link example the program builds the $Q_8$ transfer kernel on 64 states and averages the two endpoint gauges. The projected operator has five positive eigenvalues and 59 zeroes to tolerance $10^{-12}$. It kills the nonzero single-link real-part vector. This checks coexistence of a transfer kernel and nonnegative spectrum in a model with an explicit matrix. The Wilson-space proof is analytic.

SU(2) Haar quadrature agreed with the scaled modified-Bessel integral at five couplings. The log constant in the original tail was 60.19224006. The new exponent-one log bound is 8.06291761. At $\beta=10^5$ the computed one-link ratio was 14.69689253, approaching $6^{3/2}=14.69693846$. I also reran C4’s check of the horizontal-curvature example against the archived gauge and Hessian matrices. All 18 cases passed. Its scope is the pointwise curvature assumption S6. [C4’s counterexample, including its analytic large-coupling limit](../../../../central-quotients/tangent-curvature/periodic-limit/horizontal-curvature/README.md)
