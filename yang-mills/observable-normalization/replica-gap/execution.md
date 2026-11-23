# Execution and scope

The root, child and grandchild PCP OS guests emitted the spectral, endpoint and magnetic parts of the authored Lean source. The host supervisor admitted and booted each requested child, checked its completion, and collected serial output. A second sequence of three boots reproduced every source byte. Lean ran on the host with Lean 4.19.0 and Mathlib c44e0c8ee63ca166450922a373c7409c5d26b00b. All thirteen theorem axiom reports listed only propext, Classical.choice and Quot.sound. Three separate mutations failed, doubling the claimed spectral lower endpoint, replacing the endpoint difference by a sum, and deleting one neighbor contribution from the mass curvature. [Lean source](ReplicaGap.lean) · [Freestanding workers](worker.c) · [Kernel provenance and replay settings](../smeared-plaquettes/action-curvature/execution.md)

The Lean results cover the finite exterior-trace identity and moment inequalities, the two-sided interval from normalized spectral moments, the finite symmetric endpoint measurement and its bounds, the error from combining magnetic pressures, the scalar vacuum curvature and fourth-moment constants, the regular-graph upper bound, the resolvent tangent identity, and the vacuum-subtracted band coefficient. The countably infinite spectrum, Wilson slab integration, spin-network support count, perturbation of the degenerate transfer, identification of all intermediate spins, and passage to the low-temperature limits have written proofs in this directory. The numerical controls address different steps.

From this directory run the following, supplying the pinned kernel and absolute path of the QEMU wrapper from the linked settings. With the pinned Mathlib checkout as working directory, run Lean on the absolute path to ReplicaGap.lean.

~~~sh
python ../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ReplicaGap.lean --qemu /path/to/qemu-wrapper
OPENBLAS_NUM_THREADS=1 python check_transfer.py
OPENBLAS_NUM_THREADS=1 python check_band.py
python check_sign.py
g++ -O3 -std=c++17 check_haar.cpp -o /tmp/check_haar && /tmp/check_haar
~~~

The replay produced the following register heads. The kernel file SHA-256 was d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f.

~~~text
w0.elf 4f53a462df2626861f7ca80c0fd9094ef9b88349bcb8229cf629b1c10f1702cf kernel register: 47 events, head 11f4549f57a46aeb77ebe8da628d6d0c8fde275d7a8f17ce8c4a91825599feef
w1.elf c3d746076c6b853e9a0f9f5e8791b254d19a4e32f76820ed96d9cca3f2beeb76 kernel register: 47 events, head b518f4b7142016fa82a33afabb279ed4381c79ac9f65faeaf5506fce6285656e
w2.elf ca2e8bebfe296ae04539eeb532fc8a660686cb539de56074d0884450c6679555 kernel register: 47 events, head 85b2690bafecef7840a108c0e96eefd091520a3cb42ead21c9193795161a8c60
generated source SHA-256 8b13f1924fcac8721b6c8c4ba0e3692f40f4dea6ce342435222606232954b462
~~~

## Transfer and sampling controls

The finite-group enumeration uses a periodic four-dimensional binary Wilson lattice with spatial shape two by one by one. Both spatial and temporal actions are present. The small sides deliberately permit winding and repeated links within faces. An explicit sum over all site holonomies on both time seams agrees with the two-step physical trace. The temporal-gauge sum with all seam holonomies set to the identity overestimates it by a factor of 1.762586643. Full eigendecomposition and the sum over every four-endpoint configuration independently check the gap interval and both deficits. At period 16 the interval is [0.117484984, 0.162813074] around the true 0.157167138. The SU(2) side-five claim uses a separate graph and group. [Enumeration](check_transfer.py)

On the electric SU(2) torus of side five, 20,000 independent quadruples of full Haar-link slices tested the asymptotic fourth-moment prediction. For the normalized squared reading, the mean was 1.00652 (block SE 0.01021, exact 1). Its second raw moment was 3.06303 (SE 0.07490, exact 3.00867). These sample the limiting vacuum endpoint law. They do not test the cost of evaluating a long conditional kernel. [Haar control](check_haar.cpp)

## Independent two-square SU(2) transfer

Two squares sharing one edge reduce to a theta graph with path lengths 3, 3 and 1. A physical basis is indexed by twice-spins a, b, c satisfying the triangle and parity rules at the two endpoints. The electric eigenvalue is the product of the three character ratios raised to their path lengths. A traced fundamental loop changes each of its two path labels by one. At the endpoints the recoupling coefficients are conjugate, giving a Wigner 6j square with the four dimension factors in the code. The two loop insertions build the magnetic multiplier independently of the perturbative resolvent. Exponentiate the finite magnetic matrix, sandwich it between the electric square roots, and take the two largest eigenvalues at spatial coupling zero and at four nonzero values. The cutoff applies to the spin labels before exponentiation. Degree two samples only one intermediate multiplication on either side of the first band, so these cutoffs include all states needed for that coefficient. This test has one neighbor per square. The full cubic answer uses twelve. [Matrix control](check_band.py)

~~~text
two adjacent squares, gamma=0.6, predicted 0.245082736, cutoffs 3,5 0.245082736 0.245082737
two adjacent squares, gamma=2, predicted 0.241334847, cutoffs 3,5 0.241334847 0.241334847
two adjacent squares, gamma=6, predicted 0.520872564, cutoffs 3,5 0.520872566 0.520872566
cubic lattice gamma=0.1, gap curvature 0.248128081, dispersion coefficient 0.000052008
cubic lattice gamma=1, gap curvature 0.088969721, dispersion coefficient 0.004555945
cubic lattice gamma=2, gap curvature -0.204768347, dispersion coefficient 0.013518279
cubic lattice gamma=8, gap curvature -1.307988376, dispersion coefficient 0.060919157
cubic lattice gamma=100, gap curvature -16.823078780, dispersion coefficient 0.789779459
spatial symbol, step 0.02, quadratic slope 1.333222227
spatial symbol, step 0.01, quadratic slope 1.333305556
gamma 1.30638009, sign 1, curvature near 2.30615466004e-09, enclosure width 1.24e-31
gamma 1.30638010, sign -1, curvature near -6.88812642481e-10, enclosure width 1.24e-31
~~~

Only the sign enclosure uses exact rationals. It sums fifteen positive terms in each Bessel series and uses a geometric majorant for the omitted tail; interval division and monotonicity then bound the curvature at each specified rational coupling. The displayed decimal evaluations of the curvatures, finite differences and Fourier slopes are rounded. [Sign certificate](check_sign.py)
