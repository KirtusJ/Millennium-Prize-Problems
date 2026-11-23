# Reproduction and formal scope

Three measured PCP OS guests emitted the authored Lean fragments in a root, child and grandchild hierarchy. A second three-guest execution reproduced the checked file. Host Lean 4.19.0 and Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked 12 declarations. Each reports only `propext`, `Classical.choice` and `Quot.sound`. The formal results include the integrated ordered-coupling error, a finite-product telescoping estimate and triangular limit, the integrated third-order characteristic-function error and the covariance form's row bound. Gauge conditioning, convergence of local conditional covariances, block averaging and identification of the full white-noise law have written mathematical arguments. The proof workers produce deterministic source. The numerical controls below check different parts of the derivation.

From this directory run

~~~sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof ContactLaw.lean --qemu /path/to/qemu-wrapper
python check_law.py
g++ -O2 -std=c++17 -Wall -Wextra -pedantic check_stars.cpp -o /tmp/check_stars
/tmp/check_stars
~~~

Run `lake env lean /absolute/path/to/ContactLaw.lean` from the pinned Mathlib checkout. Reversing the sign of the second-moment difference in the coupling bound fails. Quadrupling the lower covariance floor fails. [Kernel and guest configuration](../../smeared-plaquettes/action-curvature/execution.md)

~~~text
w0.elf 22c04d1bc8f86f5704c4f47e9e679461287631ecfa7b0e8a246f3fe8dab20703 kernel register: 47 events, head 983c45813c493c3296359b0615962df875ba5c70d8ee10b46f40ea2157e23fe7
w1.elf a44ecff8caaa793f1cf8e41b5df4066c875f719e4d00d4953c64c9fcab48dd3b kernel register: 47 events, head 444624c9e113e48333e8957f895ffcefe1c06a8c0b209a8a54c04876a72d470b
w2.elf c0c07c6a05a6e1c00949dc739ec425b289aa8b6db9d151cb9b0a5b545974a721 kernel register: 47 events, head 09a2b5f5848b7810b512e82e653f59eb7a69813e46f15513aa3b2158eb8f8262
generated source SHA-256 4b49d44729b0d9d7377570e515907889e8ad70197be627d0b6f9643a0f02b770
~~~

The numerical checks compare monotone gamma quantiles, independent Fourier quadrature and sampled exact curls, all six covariance eigenvalues, and every face of a periodic mixed-direction mask. The second control uses full periodic four-dimensional Wilson histories of side four. For each environment it redraws a temporal link 24 times and checks all six distinct entries of the oriented conditional covariance against the analytic matrix. The errors are averaged within 24 blocks of one sweep each. These tests check signs, orientations and finite-coupling normalizations.

~~~text
radial R, centered quantile squared error 0.25 1.2329106122671516
radial R, centered quantile squared error 1.0 0.615079751332501
radial R, centered quantile squared error 6.0 0.0054233612034036895
radial R, centered quantile squared error 30.0 0.00011657530734952178
radial R, centered quantile squared error 120.0 6.689282710130519e-06
Fourier d and contrast Gram error 0.7066242376583302 0.000211492331883667
scalar, three orientation differences, two zero-row-sum eigenvalues 0.125 0.10055201980486084 0.08832802970729127
mixed mask, selected links by orientation 64 64 64 64
beta 0.7 maximum absolute block-standardized covariance residual 1.44374
beta 3.5 maximum absolute block-standardized covariance residual 1.894
beta 12 maximum absolute block-standardized covariance residual 0.753527
~~~
