# Verification of the staple response

A measured PCP OS root requested a child, which requested a grandchild. The supervisor verified each register and completion and collected the authored Lean fragments from the three guest serial outputs. Three new guests reproduced the same bytes. Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked eleven declarations with only `propext`, `Classical.choice` and `Quot.sound` in the axiom reports. [Pinned kernel and emulator configuration](../../smeared-plaquettes/action-curvature/execution.md)

The Lean results include product-fiber integration for squared insertions with varying fiber laws, extraction of a spectator weight, polynomial variance normalization, exact reciprocal remainders, the Wick coefficient given the fourth-moment contraction, strict positivity given a nonzero projected entry, and the limit of a finite sum of squared rescaled entries. The identification of Wilson conditional laws, the application of the program's rooted Gaussian theorem, the time Fourier integral and the physical trajectory selection are written analytical arguments. Flipping the sign of the random staple deficit in the reciprocal expansion failed the Lean check. Doubling the Wick coefficient also failed.

~~~sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof StapleResponse.lean --qemu /path/to/qemu-wrapper
python check_response.py
python check_slab.py
~~~

Run `lake env lean /absolute/path/to/StapleResponse.lean` from the pinned Mathlib checkout.

~~~text
w0.elf 9c06b984c0ec3e955a0bc7aab267e401e8c27a08d5222f3662b8f69e230c4cc8 kernel register: 47 events, head 4b4807a1b997fe9d5c745dc5cd010850f0c6030897b402e9303bc93c133dbdba
w1.elf 4787c7e2acd2f775ea331f92adda1eef4f1e39f9fe90a695fee77fba174de096 kernel register: 47 events, head 26630de28cc4cdba1d008c01437b18c849ebbfc24568ca16073fc98034d4bfe8
w2.elf 4fd07d10f1f8689aafb479326d437229be583301e56225fe2641e20316c571c1 kernel register: 47 events, head f92a498c280bd97d3da6a8116238aef43be744976e5164562b260c402e8e3353
generated source SHA-256 7e8b05b28b7572751bde5fe4643dbcd0366bfb7529a817a249ca10eff889b87b
~~~

The first control integrates the exact Haar radial density at high precision and compares it to the Bessel expression. It tests the scaled environment correction at three fixed deficits. For the temporal kernel, a full complex midpoint quadrature with all signed staggered phases is compared to a sign-averaged octant quadrature. At large separation the latter resolves the origin by integrating in a window of radius proportional to the inverse separation. The large-step values test the normalization independently of the analytic angular integral.

~~~text
beta, scaled variance corrections at staple deficits 0,3,7 100 -0.031341472792745226 -0.09447179022108522 -0.17964168912275424
beta, scaled variance corrections at staple deficits 0,3,7 1000 -0.031259117839973365 -0.09382167061800496 -0.17733586524989914
beta, scaled variance corrections at staple deficits 0,3,7 10000 -0.031250911490886844 -0.09375716201827422 -0.1771085539603013
complex-grid vs octant largest entry difference 4.1926452476470644e-08
n, coefficient, n^8 coefficient / asymptote 1 2.242077784362643e-05 0.27955041152293775
n, coefficient, n^8 coefficient / asymptote 2 6.232713862414799e-07 1.9894206202277132
n, coefficient, n^8 coefficient / asymptote 4 2.302331015527083e-09 1.8812960997167112
n, coefficient, n^8 coefficient / asymptote 16 1.9279537386215103e-14 1.0324426347324434
n, coefficient, n^8 coefficient / asymptote 64 2.854959890421102e-19 1.0019574146675583
n, coefficient, n^8 coefficient / asymptote 256 4.348342951074284e-24 1.0001219804761432
~~~

The second control fixes noncommuting boundary and temporal spectator links on a periodic spatial cube of side three. It integrates the original product of the six plaquette factors over the selected temporal link, using a polar quadrature axis fixed independently of the staple. Both the centered first moment and the subtracted second moment vanish to numerical precision. Slab reversal inverts every three-link path and preserves the insertion. Omitting inversion of the temporal spectators fails this geometry check.

~~~text
beta, actual staple norm, boundary kernel residual 0.35 0.882231377370883 2.498001805406602e-16
beta, actual staple norm, boundary kernel residual 2.0 5.041322156405046 4.0592529337857286e-16
beta, actual staple norm, boundary kernel residual 5.0 12.603305391012615 3.6637359812630166e-14
~~~
