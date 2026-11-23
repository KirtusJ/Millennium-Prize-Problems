# Reproduction and scope

A measured PCP OS root, child and grandchild emitted the authored proof segments. A second three-guest deployment reproduced the Lean file byte for byte. Host Lean 4.19.0 on Mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked twelve declarations. The axiom reports list only `propext`, `Classical.choice` and `Quot.sound`. [Pinned kernel and guest settings](../../smeared-plaquettes/action-curvature/execution.md)

The kernel checks the derivative of the arcsine primitive, the integral of the singular double kernel with both endpoints, integrability of the product against a locally integrable density on the compact interval, composition by Fubini, and the differentiated inverse followed by the forward integral with its endpoint term. It also checks the integrated sign-averaging minimum and the algebra of the weak-noise coefficient. The original Wilson conditional law, its identification with the Abel equation, large-argument estimates and Gaussian equal-time law are analytical arguments in the notes. Three modified files failed independently: halving the singular-kernel integral, doubling the inverse endpoint term, and reversing the sign of the conditional variance loss.

From this directory run

~~~sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof StarReconstruction.lean --qemu /path/to/qemu-wrapper
python check_reconstruction.py
python check_equal_time.py
python check_reconstruction.py --table /tmp/star_inverse_table
g++ -O2 -std=c++17 -Wall -Wextra -pedantic check_wilson.cpp -o /tmp/check_star_inverse
/tmp/check_star_inverse /tmp/star_inverse_table
~~~

From the pinned Mathlib checkout run `lake env lean /absolute/path/to/StarReconstruction.lean`. The separate guest replay returned

~~~text
w0.elf 9544a6a26a85ffec27dddb61b73e62a064cc4658a17552e56df020dc371ee293 kernel register: 47 events, head c1203653f18d1362846ca12b3f35be48ad151bdfae5b04f9803168f6ff3b173c
w1.elf f75176e304ea469edc2ac13b1b65127ae303214c1b41ed3c23af64661e79f64a kernel register: 47 events, head 4a42d9bbef958d05e8c505f16b38c435fed5e24153d1bcc76a0d71546ebc380c
w2.elf e2c735885103da378460994ecfd0fa0c5c983a5b865425d910aefeb73a2cc157 kernel register: 47 events, head 2b056f32439b3295dfb85bedd91c711c1a3c947f949e065eb0d7117bbacd064a
generated source SHA-256 11c16780f6646ec94df0dfef41deaab72a144a79baac5652811a3c3c77001425
~~~

The inverse quadrature removes the square-root endpoint singularity and scales out the Bessel exponential. Twenty exact rational Taylor coefficients computed from the SU(2) semicircle moments give a separate small-radius control. Independent forward quadratures compare the reconstructed conditional means to the Bessel variance and measure conditional fluctuations. For the latter, the target at large fixed staple radius is $R^4\operatorname{Var}_R h(X)\to27/32$. The equal-time test integrates the complex electric Fourier projection with the staggered phases and diagonalizes the resulting six-by-six real covariance independently of its symmetry decomposition.

~~~text
R, reconstructed mean, absolute mean error, R^4 variance 1.0 0.22172607687937482 2.7347622552631456e-07 0.03516193051137945
R, reconstructed mean, absolute mean error, R^4 variance 4.0 1.1750134955924085 1.1706509095432693e-09 21.399071085181294
R, reconstructed mean, absolute mean error, R^4 variance 15.0 1.4443144542580295 1.8038237570294768e-10 2.1009978003056733
R, reconstructed mean, absolute mean error, R^4 variance 60.0 1.4871780447758496 1.1965983759409937e-12 0.9959735458202579
R, reconstructed mean, absolute mean error, R^4 variance 180.0 1.4957982694552403 3.921085678371128e-12 0.8901743688769508
R, reconstructed mean, absolute mean error, R^4 variance 500.0 1.4984954841821603 5.539124714459831e-11 0.8600201340223466
x, inverse x^-2 residual 20.0 0.03212660020897873
x, inverse x^-2 residual 80.0 0.007257792557024967
x, inverse x^-2 residual 250.0 0.0022727192834398786
x, inverse x^-2 residual 750.0 0.0007525161114358379
d, eigenvalues, squared Frobenius norm 0.7066242325434863 [0.35331211627174314, 0.35331211627174314, 0.43112525581883787, 0.43112525581883787, 0.43112525581883787, 1.0] 1.8072658616234105
scaled raw variance, exterior variance, irreducible fraction 0.0011766053786610746 0.0005255637119944079 0.553322021532422
~~~

The Wilson control samples full periodic $4^4$ boxes with 90 burn-in sweeps, including all six current staples when updating a link. For each of 28 subsequent sweeps it fixes each temporal link's environment and makes 24 fresh draws of that link. The ordinary-trace reading uses the tabulated inverse of its six measured face traces. The table spacing is 0.01, with a separate midpoint interpolation control. Paired first moments are checked against the exact conditional mean using the dispersion of the sweep averages and an interpolation allowance. These finite histories test the estimator and the size of its noise. The limiting equal-time constants follow from the analytical argument.

~~~text
largest checked midpoint interpolation error 2.499781260494345e-05
beta 1.2 mean errors 2.49427e-05 -0.00171411 conditional noise h,W^2 0.106442 4.40387 beta^4 noise of h 0.220718
beta 4 mean errors -7.19438e-06 0.012009 conditional noise h,W^2 8.33368e-06 12.8854 beta^4 noise of h 0.00213342
beta 12 mean errors -3.90401e-07 0.0150111 conditional noise h,W^2 4.37499e-08 14.0055 beta^4 noise of h 0.000907198
~~~
