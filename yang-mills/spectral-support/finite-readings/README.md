# What three Euclidean-time readings establish about a Yang–Mills gap

Director D4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For the interacting $SU(2)$ cubic Hamiltonian at fixed spatial mesh and $0\le\lambda/\kappa\le\sqrt3/512$, one fundamental plaquette assigns at least $3/4$ of **raw spectral mass** to $[5\kappa/2,7\kappa/2]$. Its adjoint character assigns at least $3/4$ to $[7\kappa,9\kappa]$. Each complementary tail has mass at most $1/16$. The intervals and masses hold in every periodic box of side at least three. In particular the full first excitation energy is at most $7\kappa/2$. These mass bounds use the unnormalized characters, centered in the true vacuum. [Loop proof and conventions](loops.md)

Three readings already exclude a proposed gap of $4\kappa$. Write $C_j=\langle f\Omega,e^{-j\tau(H-E_0)}f\Omega\rangle$ for the centered fundamental plaquette, and take $\tau=\log(2)/\kappa$ in physical units. Then
$$
-C_2+\frac{17}{16}C_1-\frac1{16}C_0\ \ge\ \frac1{128}.
$$
Using only the readings at $\tau,2\tau,3\tau$ gives margin $15/16384$ for the same coefficients. For the displayed zero-time version, each scalar reading can have absolute error strictly below $1/272$ while preserving a positive sign. A positive sign certifies some energy strictly between zero and $4\kappa$ even if the limiting vacuum is degenerate. At fixed couplings the inequality passes to any common limit of these three readings. B4’s time comparison provides simultaneous Wilson sequences with the same limits. In B4’s uniform small-coupling regime it applies along every joint time and volume path for these local readings. [Wilson vacuum schedule](../../transfer-operator/joint-cutoff/finite-volume-vacuum.md) · [B4’s joint local limit](../../transfer-operator/blocked-time/local-limit.md)

For $g=\lambda/\kappa\le1/768$, combine B4’s Hamiltonian lower bound with the band above to obtain
$$
 \frac{2\log 3}{13}\,\kappa\ \le\ \Delta_{\rm box}\ \le\ \frac72\,\kappa.
$$
Here B4’s parameter is $\kappa_B=2/\kappa$. The same lower and upper bounds hold for the gap in the corresponding limiting vacuum theory when using B4’s dense local correlation reconstruction and this surviving plaquette. The finite-time result supplies the upper constraint. The spatial continuum limit, its nontriviality, and a common positive gap on that limit for all compact simple gauge groups remain open. [B4’s lower-bound hypotheses](../../transfer-operator/blocked-time/) · [Jaffe–Witten problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Using other probe matrices

Let $T=e^{-\tau(H-E_0)}$, or a positive vacuum-normalized Wilson transfer measured over the same physical time, and $C_j=J^*T^jJ$ for a finite list of test vectors. With an unknown vacuum Gram, three readings are consistent with excited transfer values in $[0,q]$, $0<q<1$, precisely when the raw two-by-two block Hankel Gram is positive semidefinite and
$$
 0\ \preceq\ C_1-C_2\ \preceq\ q(C_0-C_1).
$$
This is an exact existence test for finite measured data. A failed upper inequality gives a witness to energies below the proposed gap. Passing it admits a realization with that gap for these readings. Higher-order tests become necessary and sufficient for the actual measured spectrum when every order is available. The full Hamiltonian conclusion requires a dense probe family in the sector under study. [Sharp tests, singular cases and proof](moment-problem.md) · [Exact complex rational implementation](moments.py)

For example, in the pure electric theory use the two centered probes $F+8F_A,F-8F_A$. With the same clock they have $u_F=1/8$ and $u_A=1/256$. **Each diagonal alone** at $j=0,1,2$ matches a positive measure at the two transfer values $1/1024$ and $133/2552$, both strictly below $1/16$, with weights $984064/16705$ and $101761/16705$. Both are genuine finite positive energies. The joint matrices at the same three times give the fundamental channel in the polarization $(1/2,1/2)$, with positive excess $7/128$ at $q=1/16$. They certify at least $56/225$ raw mass in the open interval $(1/16,1)$, and its actual mass there is one. [Exact checks](check_moments.py) · [Lean declarations](FiniteReadings.lean)

The same one-link analysis also controls the error of cutting off the electric representation on every link. It gives computable two-sided intervals for a finite-box Hamiltonian gap, and a joint spin and volume schedule at all fixed couplings. For an isolated square at $g=\kappa=1$ it encloses the infinite-dimensional gap between $3.113863811504$ and $3.113863811508$. The isolated square is an independent check of the truncation calculation. [Spin cutoff and certified example](spin-cutoff.md) · [Native and Lean execution](execution.md)
