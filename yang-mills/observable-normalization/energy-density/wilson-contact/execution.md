# Verification and controls

Three measured PCP OS guests formed a root, child and grandchild hierarchy. The supervisor checked the admitted worker ELF and guest completion and accepted each child request before launching the next guest. The deterministic workers emitted the authored Lean source. Three fresh guests independently reproduced the same bytes. Host Lean 4.19.0 with Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked twenty declarations, each reporting only `propext`, `Classical.choice` and `Quot.sound`. [Pinned kernel and QEMU wrapper](../../smeared-plaquettes/action-curvature/execution.md)

From this directory run

```sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof WilsonContact.lean --qemu /path/to/qemu-wrapper
python check_bounds.py
g++ -O2 -std=c++17 -Wall -Wextra -pedantic check_wilson.cpp -o /tmp/check_wilson
/tmp/check_wilson
```

From the pinned Mathlib checkout run `lake env lean /absolute/path/to/WilsonContact.lean`. The replay returned

```text
w0.elf 4b9007c59523eaee26f1b784b138d6ba6032d412b78cb040f5488d2e9fd06a13 kernel register: 47 events, head 16bafa05e6fb991e67abc096abc74cbe5847e360af5fdd0cf7af47a797223cc9
w1.elf 4beb241dd033fcc3590b49ff404ded6761c03ee451d899725c1a73d38542a5c3 kernel register: 47 events, head 906de82f321cce28d08133ed28dade96b245f0e093bea7ca7a9120bda01af820
w2.elf 797c19b75ac8d8e06bbf741e690dab4ed4f48a751212db37e79c51f125df23e7 kernel register: 47 events, head 8bfc452c349ca78e0cda0195066b0c54b03a7d47f0becffac5dc11de2d13a04e
generated source SHA-256 ae6da93739208063ff8b6d1b057f6a27afd758c03d04b369b62262cee8453ccb
```

Lean covers integration by parts and the fourth-moment inequality as actual integrals on a closed one-parameter Gibbs orbit, orthogonal variance loss, the normalized finite conditional-fiber identity, both incidence coefficients, sparse Gram estimates and the score subtraction. It also sums the full alternating Toeplitz triangle at each length and bounds its remainder, including the zero-energy endpoint. The group-orbit application, conditional independence, Haar asymptotics, box estimates and continuum scaling remain analytical derivations in the notes. Mutating the Gibbs derivative sign failed the orbit identity. Reversing the sign of the Toeplitz boundary term failed its recurrence.

## Deterministic and statistical tests

The numerical controls compare a rescaled polar-coordinate integral with exponentially scaled Bessel functions, enumerate independent masks on even, odd and mixed-period lattices, and reject a mask that repeats the same orientation on adjacent layers. An independent two-by-two complex matrix calculation differentiates a rectangle in two link rotations. Transporting the second generator gives the correct trace; using the first generator unchanged gives a different answer. Direct alternating time matrices check the endpoint formula.

```text
mixed derivative, transported and untransported errors 2.1171953079601735e-13 0.8033628290377994
polar 0.0 0.25000000000000044 0.24999999999999986 R squared times minimum 0.0
polar 1.0 0.2217258034031503 0.2401937238700895 R squared times minimum 0.2217258034031503
polar 6.0 0.03688589549764224 0.12712101262486528 R squared times minimum 1.3278922379151208
polar 60.0 0.0004131050124377333 0.016251765698032324 R squared times minimum 1.4871780447758398
polar 600.0 4.163185738479786e-06 0.0016625017390109766 R squared times minimum 1.4987468658527228
polar 6000.0 4.166319357613564e-08 0.00016662500173640038 R squared times minimum 1.499874968740883
masks (4, 4, 4, 4) space-time size 128 plaquettes 1536
masks (3, 3, 3, 5) space-time size 30 plaquettes 810
masks (3, 4, 5, 4) space-time size 80 plaquettes 1440
alternating time matrices checked through length 80
```

The second program samples a **full periodic four-dimensional SU(2) Wilson box** with four sites in each direction and no frozen exterior. A full sweep updates every link sequentially with its six current staples. Below staple length one the sampler accepts Haar proposals with the exponential weight. Otherwise it proposes the radial deficit from a shape-$3/2$ gamma law and accepts the remaining square-root factor. Each conditional draw is exact in the mathematical algorithm. The finite Markov-chain averages are statistical. The two chains use distinct seeds and identity or independent Haar starts, with 180 burn-in sweeps each. There are 12 retained blocks of 32 sweeps per chain at zero coupling and 45 per chain at $\beta=2.2$.

The raw spatial test is a single $xy$ plaquette trace with cosine weight at its center, summed on each slice without the physical prefactor. Its mean is exactly zero by translation. On an even slice an $x$-link checkerboard hits each such face once, so this test checks a single mask's exact conditional-variance identity. The displayed time separation is two steps on a four-step temporal period. The paired residuals are the raw variance minus projected and conditional variances, and the raw minus projected two-point reading. The last row checks the score’s mean and its exact pairings with the same face and a distinct neighbor. Block standard errors are empirical; no positive separated signal is resolved at $\beta=2.2$. This finite run checks implementation and normalizations. It supplies no estimate of a continuum mass.

```text
beta 0 raw variance, projected variance, conditional variance, raw C(2), projected C(2): 7.8130425 0 8.0071254 -0.096185659 0
paired residuals and block SE: -0.19408286 0.1974765   -0.096185659 0.22028182
score mean, diagonal residual, off-diagonal, plaquette mean (and block SE): 0 +/- 0 -0.00026387235 +/- 0.0012964259 0 +/- 0 0.00026387235 +/- 0.0012964259
beta 2.2 raw variance, projected variance, conditional variance, raw C(2), projected C(2): 3.7057224 2.0631276 1.621996 0.0074887764 0.007179135
paired residuals and block SE: 0.020598824 0.043227985   0.00030964148 0.041412841
score mean, diagonal residual, off-diagonal, plaquette mean (and block SE): 0.0026117483 +/- 0.0051176333 0.0020829559 +/- 0.0028842078 0.0032033725 +/- 0.0032110863 0.57333798 +/- 0.00099489169
```
