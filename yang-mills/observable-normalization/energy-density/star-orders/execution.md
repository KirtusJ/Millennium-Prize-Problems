# Verification, finite boxes and numerical precision

A measured PCP OS root requested a child, which requested a grandchild. The three guests emitted the authored Lean segments. Three fresh guests reproduced the source byte for byte. Lean 4.19.0 with Mathlib at `c44e0c8ee63ca166450922a373c7409c5d26b00b` checked thirteen declarations, each reporting only `propext`, `Classical.choice` and `Quot.sound`. [Kernel and replay setup](../../smeared-plaquettes/action-curvature/execution.md)

The kernel checks the geometric enclosure and its rational endpoints given the torus moments, separation of the variances, the degree bound given divisibility, both the mixed-pole recursion and the resulting rectangular cancellation, the four actual residues, the squared-coefficient identity, the quartic tail factor given the odd eigenvalue asymptotic, the quadratic leakage bound, integration of the characteristic-function error, and the exponential action comparison. Three altered conclusions failed: an extra necessary pole, a reversed residue sign, and a halved quartic tail coefficient. The original-link Gaussian limit, Hermite expansion, Fourier asymptotics, application of the input Ward bounds and transfer conclusions have written analytical arguments.

~~~sh
python ../../transfer-increments/replay-guests.py /path/to/kernel.elf32 --proof StarOrders.lean --qemu /path/to/qemu-wrapper
python check_orders.py
python finite_box.py
g++ -O2 -std=c++17 -Wall -Wextra -pedantic check_wilson.cpp -o /tmp/check_star_orders
/tmp/check_star_orders
~~~

Run `lake env lean /absolute/path/to/StarOrders.lean` from the pinned Mathlib checkout. Replay returned

~~~text
w0.elf 865f6f2714ced9da44320fcb29cd366835404142473332337474a6a551b8e669 kernel register: 47 events, head d036c39fb4d343f04a2a0c3ac571b09fdf558c16ee0838a6e11002b27190d5f6
w1.elf 2d7e4cd66da80b3614920ccbd4664096c9dcb5b4b8abad9b8257a4434c0d8de1 kernel register: 47 events, head 6cda9bb388deafb025846aeae539599809cc8b1f8af98511d03aac81e5c9f530
w2.elf 00d835bb00ac32c25e1fb9b1161493ab950dee4d9dd189d0fc7159b9cfb9708b kernel register: 47 events, head 99253553d1406c8a5e8c2900ef8159efa66451c4d9864e2fae4e775fb2f51a07
generated source SHA-256 8f627cc218168a9c72a229626c30cb014d6544d876a1f6ddc03d93a9df405966
~~~

The analytic controls compute an exact rational enclosure, integrate the three Gaussian radial blocks independently by a tensor Laguerre rule, and check both the quadratic nulls and a nonzero fourth-order overlap. An independent temporal quadrature resolves the pair-sum numerator of order $|k|^4$ directly and compares to all six eigenvalues of the earlier signed matrix. The two-star Laplace transform is summed at 160 decimal digits so that algebraic cancellations remain resolved through order six even at step 256. The last control deliberately perturbs one weight.

~~~text
rational interval for d 5285/8192 6439/8192
independent radial quadrature: largest quadratic residual, quartic overlap 8.881413872538749e-16 0.014185498006779118
d and distinct variances 0.7066242375573288 0.3533121187786644 0.43112525414755704
order, step, covariance, scaled/target 1 1 0.0654634236 0.307143912
order, step, covariance, scaled/target 1 8 1.46086816e-8 1.14993719
order, step, covariance, scaled/target 1 64 7.58693416e-16 1.00195751
order, step, covariance, scaled/target 1 256 1.15555358e-20 1.00012206
order, step, covariance, scaled/target 2 1 8.5575892e-8 0.431280986
order, step, covariance, scaled/target 2 8 9.30971841e-22 1.32064233
order, step, covariance, scaled/target 2 64 2.51425924e-36 1.00391864
order, step, covariance, scaled/target 2 256 5.83253951e-46 1.00024413
order, step, covariance, scaled/target 3 1 5.60684225e-19 0.327163769
order, step, covariance, scaled/target 3 8 5.5077148e-40 1.51767226
order, step, covariance, scaled/target 3 64 7.73003629e-62 1.00588371
order, step, covariance, scaled/target 3 256 2.73119673e-76 1.00036622
damaged/undamaged covariance at n=24 1.16592956e+9
large-step u,v amplitudes relative to analytic limits 1.0002136742733705 1.0000610269631371
~~~

## Wilson measurement

The compiled program uses full periodic SU(2) histories on $4^4$. At each $\beta$ it runs four randomly seeded chains, with two identity and two independent Haar initial configurations, 200 burn-in sweeps and 76 blocks of 32 subsequent full heat-bath sweeps per chain. The same four numerical inverse source strengths and the same rounded $d$ are used at both couplings. Each sweep contributes all 256 temporal stars. Reported uncertainties are delete-one-block jackknife standard errors; they do not bound thermalization, long autocorrelations, finite volume or the difference from the zero-mode-deleted Gaussian model.

Conditionally on the other links, let $R$ be the staple radius, $Z(R)=2I_1(R)/R$ and $m=I_2/I_1$. The one-link mean of $e^{-sS}$ is $J_s=e^{-6\beta s}Z((1+s)R)/Z(R)$. The mean of $S e^{-sS}$ is $J_s[6\beta-Rm((1+s)R)]$, obtained by differentiating in $s$. The time-zero integrated estimate uses this same-link product. The one-step product may instead use separate conditional link means because no face contains both temporal links. A precomputed table of radius values is linearly interpolated and spot-checked against Bessel evaluation. The raw mean and the one-step raw product have paired controls against integration. The time-zero and time-one quantities below are connected covariances with the ordinary action $S$; the program uses the sampled means for centering.

~~~text
beta 2.3 mean difference, equal-time mixed, projected one-step mixed, raw minus projected one-step, integrated equal-time mixed
3.78324e-05 +/- 0.000112592   0.000707908 +/- 0.000560137   0.000267715 +/- 7.91563e-05   -5.32699e-05 +/- 0.000209662   0.00102512 +/- 0.000315614
beta 8 mean difference, equal-time mixed, projected one-step mixed, raw minus projected one-step, integrated equal-time mixed
-0.000144341 +/- 0.000214729   0.00156815 +/- 0.000824228   0.000122836 +/- 9.94127e-05   -6.16729e-05 +/- 0.000357984   0.00114428 +/- 0.000344814
zero-mode-deleted Gaussian, L, lag, mixed covariance 4 0 -9.40500291419788e-05
zero-mode-deleted Gaussian, L, lag, mixed covariance 4 1 -4.584244476052435e-06
zero-mode-deleted Gaussian, L, lag, mixed covariance 8 0 -3.8095002374838316e-06
zero-mode-deleted Gaussian, L, lag, mixed covariance 8 1 -1.626296161211238e-07
~~~

The second control evaluates the zero-mode-deleted Gaussian on the same periodic geometry by a full four-momentum sum. If $K$ is its one-color single-star covariance and $M$ the cross covariance, Gaussian tilting gives the single-source mixed covariance
$$
 -\tfrac32\det(I+K/r_i)^{-3/2}\operatorname{tr}[M^T(r_iI+K)^{-1}M] .
$$
The calibrating weights remain those of the infinite lattice. The torus itself consequently produces a finite residual even in this Gaussian comparison. The Wilson values, the zero-mode-deleted reference and the infinite-lattice zero have different hypotheses. A single box at two finite couplings cannot determine a renormalized interaction or a nonzero continuum coefficient. The $t^{-16}$ autocorrelation follows from the analytic limit. These mixed-correlation runs do not resolve that autocorrelation numerically.
