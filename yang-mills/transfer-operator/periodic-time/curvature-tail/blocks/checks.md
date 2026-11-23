# Two incident square loops and three native controls

Take the positive $01$ and $02$ faces at the origin. They share one edge, giving two independent cycles. For the one-color infinite Gaussian covariance, both diagonal entries equal $1/2$. The off-diagonal entry is $0.1077813135$ by integration of the four-dimensional lattice heat kernel. Only the common edge direction contributes; the two transverse differences give the integrand $e^{-8t}(I_0(2t)-I_1(2t))^2 I_0(2t)^2$. In the cube the relative one-form Laplacian separates into one Neumann and three Dirichlet directions. Inserting the two distinct transverse currents yields the finite cross covariance. The sum and difference of face readings diagonalize both matrices, so both exterior fractions can be computed without a matrix fit. [Numerical checker](check.py)

| Enclosing radius | Sum-mode fraction | Difference-mode fraction | $R^4 t_*$ |
|---|---|---|---|
| 2 | 0.01070184 | 0.02076906 | 0.3323050 |
| 4 | 0.00034664 | 0.00056637 | 0.1449915 |
| 8 | 0.00001864 | 0.00002924 | 0.1197685 |
| 12 | 0.000003588 | 0.000005591 | 0.1159252 |

For these radii the best invariant Gaussian reading is the centered squared norm of the standardized difference mode. A separate radius-one arithmetic check gives $7/24$ and $7/48$ for the diagonal and cross conditional curvature entries. At radius one some vertices of these squares lie on the shell. That check tests the curvature matrix only; the compact block theorem requires the graph strictly inside.

Three measured PCP OS guests reproduced the finite controls. The parent enumerated 7,776 endpoint gauge transformations on a three-path graph with group $S_3$, including tuples with equal separate conjugacy classes and different joint orbits. The child checked 576 covariance minors on the radius-one star. The grandchild enumerated all 24 proper signed coordinate rotations to verify cancellation of the linear term and preservation of orientation. These finite programs check specific steps in the written proofs. The parent and child requested their successors through the existing host relay. [Source](worker.c) · [Expected output](checks.txt) · [Relay](../../../../observable-normalization/transfer-increments/replay-guests.py)

| Guest | Executable SHA-256 | Kernel register head (47 events) |
|---|---|---|
| Parent | 32041e8af4cf7b03368e56053b9a2211887f22e7ff08e1c5f28cd74459ad1c74 | bbbd26bd858885d274e922f900b652c7911bcd2f7e9e87de77f5b3b309ff8034 |
| Child | d11ce6879640ce2765346a8a29aab12473a857d38022cf6d8ef62039d8b79280 | 410b4beac8be100b3f577b9324c1f6731cf7d52f1bdb59c029d7e4b98f17caac |
| Grandchild | 2b0a365c5ee1537684161d622b6c04b2471253355f35fad3e5ba1138b3fb27c0 | 0e205d0888fe4fab3e679d8800ae76c6860b227e01d420ace39a6a6a4890cd38 |

The generated record SHA-256 was e574a4359d0e80946c867ec1790ddc21bcb1d7f4e20a78064da99cbe25263045. Kernel file SHA-256 was d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f. Run the sibling Python checker with NumPy and SciPy. To replay the three guests from this directory use the pinned kernel with QEMU installed.
```sh
python check.py
python ../../../../observable-normalization/transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof checks.txt
```
