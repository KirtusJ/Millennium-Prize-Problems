# Verification and scope

The two final PCP OS runs used a hosted root, a generation child, and two grandchildren. The first grandchild executed the finite controls, emitted the rectangular minimization proof fragment, and independently recompiled the nineteen declarations of the earlier Wilson surface module. The other built a freestanding certificate generator and ran it in a measured PCP OS guest. It derived the analytic budget from the face incidence and ordered-tree counts. The generation child ran a second measured guest to assemble the Lean file. After the child exited, the root compared its bytes with the tracked source, checked the complete module with Lean 4.19.0 and ran the adverse variants. The outer supervisor read the finished four-node tree back. [Replay](replay.py) · [Freestanding generator](certificate.c) · [Register heads, hashes and compiler output](readback.txt)

All 26 B4 declarations in the final runs reported only propext, Classical.choice and Quot.sound. Lean proves the Haar leaf integration, scalar cut factorization, the four-corner minimum, projected area and edge-perimeter bounds for an actual finite set of planar cells, and the minimum-cut and horizontal return estimates for closed slice paths. The area argument embeds the set in the product of its projections. The perimeter proof selects extremal cells on each occupied row and column in each of four directions. The source also proves the complex polymer deletion inequality, the finite-moment variance formula, and algebra for the two spectral weights, coherent subtraction and common physical units. The proof of the connected Wilson Taylor coefficient combines these ingredients with the written chain projection, classification of equality, Haar contractions and covariance expansion. The polymer induction and passage to the infinite-volume physical Hilbert space are written arguments. [Formal source](ConnectedRectangles.lean)

Each final run rejected six alterations. They included reversing the sign of the disconnected subtraction, dropping the two-face penalty for an empty projection, reducing the crossover-shift allowance, giving the tie one extra opening, omitting a cross term in the Hilbert residual, and understating the moment-error allowance. For a square the displacement is exactly half a step. The shift mutation replaces $1/2$ by $1/3$. [Targeted error reports](readback.txt)

## Independent finite controls

| Check | Observed outcome |
|---|---|
| Exact min-plus transfer across every planar section | A $3\times3$ square across two steps had degree 24 and ten minimizing histories. A $4\times4$ square had one at lag two and sixteen at lag three. The largest section search kept 65,536 states per layer. |
| Integer optimization allowing repeated faces in four dimensions | On the $2\times2\times2\times1$ cell box with 126 faces and 135 links, imposing binary boundary and at least four occurrences per cut gave degree 14. The two disconnected caps cost eight. Only the cut-count relaxation was used in this control. |
| Exact $SU(2)$ fundamental matrix-index gluing | Every unit opening, including edge and corner placements, gave coefficient one in units of $4^{-D}$ for both the matching large rectangles and the rectangle-to-cell correlator. The full outer wall gave one. |
| Connected covariance of the exact binary gauge model | On a $3\times3\times2$ cell box the program enumerated all 262,144 closed surfaces and computed the coefficients of $N_{01}Z-N_0N_1$. Raw degree 18 cancelled. The first connected term had degree 24 and coefficient ten. On a $2\times2\times2$ box a rectangle paired with a single corner cell gave degree eleven and coefficient one. |
| Quaternion subgroup temporal integrals | Every nonempty proper subset of the cycle edges had zero product average in lengths two, three and four. The full-cycle values were $-1/4,-1/16,-1/64$ for the chosen opposite boundary holonomies. Repeating one forest edge four times gave a nonzero scalar independent of the chosen boundary matrices. |
| Original $SU(2)$ Wilson temporal kernel | For a four-edge cycle with relative central holonomy $\pm I$, two consecutive kernels convolve to $Z(\beta\sqrt{2+2t})$, $t=\operatorname{Tr}(g)/2$, $Z(s)=2I_1(s)/s$. A final semicircle quadrature of the two pairs agreed with the character sum $\sum_d (\pm1)^{d-1}d^2[I_d(\beta)/I_1(\beta)]^4$ within $2.3\times10^{-15}$ at five couplings. |

The binary model checks the connected cancellation independently. Its group weights differ from the $SU(2)$ Wilson history. The separate index contractions implement the original Haar normalization on each minimizing surface. The four-dimensional integer program tests the cost. The analytic expansion gives the connection to the Wilson probability law. The finite calculations and their exact scope are recorded in the [controls](controls.py) and [read-back](readback.txt).

Use the pinned build from the [transfer PCP setup](../pcp/), with the required Mathlib modules compiled and NumPy/SciPy available on the host.

~~~sh
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 replay.py /path/to/base /path/to/pcp-os /path/to/new-run
~~~
