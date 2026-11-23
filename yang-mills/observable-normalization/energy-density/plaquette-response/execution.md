# Reproducing the finite-box response checks

Three fresh PCP OS guests emitted the three sections of the authored Lean proof. The root requested the spectrum worker, which requested the limit worker. The host supervisor launched each guest, checked the kernel measurement and admitted ELF, and accepted proof lines after successful exit and kernel self-tests. A second three-guest run reproduced the source. Lean verification ran on the host with Lean 4.19.0 and Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`. [Kernel and QEMU wrapper](../../smeared-plaquettes/action-curvature/execution.md)

From this directory run

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof PlaquetteResponse.lean --qemu /path/to/qemu-wrapper
OPENBLAS_NUM_THREADS=1 python check_response.py
```

From the pinned Mathlib checkout run `lake env lean /absolute/path/to/PlaquetteResponse.lean`. The measured replay returned

```text
w0.elf a8915e5874f74430d62dfb0727dc6a2195a51368cbddd2dc293c16363009edd2 kernel register: 47 events, head 6768c89217e63996dd3222fbea79db5d18f34844a65cdc84a28f629176a88917
w1.elf bdf21f7569a3e76f4453d9974a4080f275e538a65a17be08c584320ca00956a2 kernel register: 47 events, head 42d3966f4baca1da397c24ecc08cc66da95d588afb65f8117e5858320b5c5fb7
w2.elf 51a8a8d43cea25c0e1aee9a38c53290506d64ea0312bd3f3a4731e6aa18330e6 kernel register: 47 events, head 32218d5b22da72899add44d6fd2b531f90fcb29986fd903e6ebe848d0aab6259
generated source SHA-256 4a4a7af3bbe1845af7f96e70de78183842ed8f74a72dde32f1679e266a89fa1a
```

Sixteen declarations checked with only `propext`, `Classical.choice` and `Quot.sound`. Lean covers the Casimir and Haar coefficient arithmetic, the two masses and first moment, the zero-defect implication, propagation of local equality along paths, scaled injectivity under a norm perturbation, affine testing, the incidence identities, monotonicity and the axial characteristic equation. The operator perturbation argument, Haar projection, torus Fourier diagonalization and continuum smearing estimate are mathematical derivations in the accompanying notes. No Lean construction of the four-dimensional continuum theory is included.

Two falsification controls were rejected. Replacing the spin-one factor $2d/13$ by $2d/9$ fails for $d=1$. Replacing the third independent face equation in `recoverIncident` by a repeat of the first allows $w=0$, $a=1$, $b=c=-1$.

## Numerical controls

The torus check enumerates every adjacent pair, checks uniqueness of the six exterior links and explores the whole link-face incidence graph. It constructs a sparse matrix directly from the pair defects, compares its Gram matrix entry by entry with the independent incidence polynomial, then computes its lowest eigenvalues. Columns after the side length give link and pair counts followed by the first positive computed and predicted spatial eigenvalues.

The second test uses an open pair of SU(2) plaquettes with a common link. The three links on each exterior path combine into independent Haar variables when the shared link is fixed. The two holonomies $X,Y$ then have independent Haar marginal law. Use $x=\operatorname{Re}X$, $y=\operatorname{Re}Y$, $z=\operatorname{Re}(\bar X Y)$. Conditional on $x,y$, the last coordinate is $xy+\sqrt{(1-x^2)(1-y^2)}u$ with $u$ uniform on $[-1,1]$. The marginal laws of $x,y$ are semicircular. With each exterior path contributing three identical link Casimirs, the kinetic operator is $3C_X+3C_Y+C_{\rm shared}$. The shared-link Casimir differentiates $x,y$ while fixing $z$. The three sphere-coordinate differential operators are implemented explicitly. Product Gauss–Chebyshev and Gauss–Legendre cubature integrates the polynomial matrix entries. Odd conditional powers of $u$ vanish, and the remaining square-root factors give polynomials within the quadrature order.

The script computes the interacting ground eigenvector in polynomial spaces of total degrees four and five (35 and 56 monomials). With $\kappa=1$ the balanced observable assigns one to the common link, zero to exterior links and $1/4$ to each face. Each positive-energy band includes eigenvalues within $0.2$ of its limiting center. Repeating with the larger basis changed each reported band weight or moment by less than $4\times10^{-8}$. The two-face calculation tests the shared-link factors independently of the periodic-volume geometry. Its truncation does not certify a finite-coupling mass bound.

```text
torus 5 375 2250 0.29962989766685993 0.29962989766686055
torus 6 648 3888 0.2016721399597534 0.2016721399597533
torus 7 1029 6174 0.14493889218368544 0.14493889218368522
lambda, spin-zero and spin-one band weights, first moment (all divided by lambda^4)
0.16 0.0004327387787 6.89042312e-05 0.002398394599
0.08 0.0004337048528 6.923204351e-05 0.002402481078
0.04 0.0004339470042 6.931427898e-05 0.002403504748
0.02 0.0004340075817 6.933485555e-05 0.002403760794
predicted 0.00043402777777777775 6.934171597633136e-05 0.002403846153846154
```
