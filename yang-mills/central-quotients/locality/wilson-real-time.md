# From one Euclidean time to real-time Wilson words

B4's positive, injective $SU(2)$ Wilson transfer $T_a$ and the Hamiltonian act on the same finite-box physical Hilbert space. Write $Q_a=-a^{-1}\log(T_a/\|T_a\|)$ and $Q=H-E_0$. Their vacua can be aligned with distance $v_a=\|\Omega_a-\Omega\|$. The following comparison carries the Hamiltonian locality estimate to real-time vacuum readings of $Q_a$ on a chosen simultaneous sequence. The unitary $e^{-itQ_a}$ is the spectral continuation of the normalized Euclidean transfer. [B4's positive-time estimate](../../transfer-operator/joint-cutoff/evolution.md) · [Finite-box vacuum estimate](../../transfer-operator/joint-cutoff/finite-volume-vacuum.md)

## Quantitative comparison on a vector

For any two nonnegative self-adjoint generators on the same Hilbert space, let
$$
 \epsilon_s=\|e^{-sQ_a}-e^{-sQ}\|,\quad D_s(E)=(1-e^{-sE})/s,\quad
 C_s(T)=8(s+\sqrt{Ts}).
$$
For $\|\psi\|\le M$, $m=\|Q^{1/2}\psi\|^2<\infty$ and $|t|\le T$,
$$
 \boxed{
 \|(e^{-itQ_a}-e^{-itQ})\psi\|
 \le \sqrt{C_s(T)m}
    +TM\,\epsilon_s/s
    +\sqrt{C_s(T)(m+M^2\epsilon_s/s)} .\ }
$$
Only the Hamiltonian form energy of the vector appears. $Q_a$ may have unbounded energy on that vector.

For $E\ge0$, $0\le E-D_s(E)\le sE^2/2$, by integrating $1-e^{-u}\le u$. The phase difference $r=|e^{-itE}-e^{-itD_s(E)}|$ is bounded by 2 and by $|t|sE^2/2$. With $y=\sqrt{|t|s}\,E$, these bounds imply $r^2\le2y$ by splitting at $y=2$. For $sE\le1$, $D_s(E)\ge E/2$. For $sE\ge1$, $D_s(E)\ge(1-e^{-1})/s\ge1/(2s)$. Together they give $r^2\le C_s(T)D_s(E)$ at all energies. The spectral theorem bounds the error of each unitary relative to its own bounded-generator phase. The quadratic form of $D_s(Q)$ costs at most $m$, while $D_s(Q_a)$ costs at most $m+M^2\epsilon_s/s$. Finally, Duhamel for the two bounded self-adjoint generators $D_s(Q_a),D_s(Q)$ gives the middle term. This proof does not assume the generators commute.

The form budget matters. For the one-dimensional generators $Q=n,\ Q'=n+\pi$, the positive-time difference tends to zero at each fixed $s>0$. At real time one their unitary difference has norm two for every $n$. Appending an identical zero eigenvalue gives the same example with a common vacuum. [Numerical control and noncommuting matrix comparisons](checks.py)

## Energy of a string of loop insertions

Write any vector in ground-state coordinates as $\psi=\Omega h$. The positive elliptic finite-box vacuum is smooth and bounded away from zero. Integration by parts and $H\Omega=E_0\Omega$ give
$$
 \|Q^{1/2}\psi\|^2=\kappa\sum_{e,i}\int\Omega^2 |D_{ei}h|^2.
$$
The closed form extends the identity by density. For a smooth bounded scalar multiplier $B$, set $L_B=(\kappa\sum_{e,i}\|D_{ei}B\|_\infty^2)^{1/2}$. After insertion the norm and square-root energy budgets $(M,D)$ can be replaced by
$$
 (\|B\|M,\;\|B\|D+L_B M).
$$
Hamiltonian real-time propagation preserves both. Start at $(1,0)$ for the vacuum and apply this recursion from the right in a word. Telescope the two operator products, replacing one time interval at a time, with Hamiltonian factors on the right and Wilson factors on the left. At each replacement multiply the boxed error for that intermediate Hamiltonian vector, $m=D^2$, by the product of the remaining multiplier norms on the left. Two vacuum replacements add at most $2v_a\prod_j\|B_j\|$. The same budgets apply uniformly in the individual times in a compact interval. Taking differences of orders gives a commutator with arbitrary finite spectator words. For linear combinations one may use absolute coefficient sums. This bound handles polynomially growing insertions by choosing the time step after specifying their budgets.

## Selecting a simultaneous time sequence

All estimates below are in a common fixed system of units. For $0<a\le s/2$, $ac\le1/36$, put $N=\lfloor s/a\rfloor$, $k=\lceil(s/a)^{1/3}\rceil$, $c=6\lambda L^3+6/\kappa_B$, $\kappa_B=\beta b$. B4's estimate for the integer power, plus $1/(eN)$ for the fractional step, yields the convenient envelope
$$
 \epsilon_s \le 301(a/s)^{1/3}+7ac+144asc^2 .
$$
Indeed the terms involving $N$ cost at most $6a/s$. The time-shift term costs $3a/s$, and the two $k$-terms cost at most $292(a/s)^{1/3}$. The fractional-step bound follows from $\sup_{x\ge0} x e^{-Nx}=1/(eN)$. [B4's finite-volume constants](../../transfer-operator/joint-cutoff/evolution.md)

For box $n$, specify a finite collection of words, their time range $T$, and a desired total absolute error $\delta_n>0$. Compute the insertion budgets above. First halve a positive $s$ until the sum of all terms at $\epsilon_s=v_a=0$ is below $\delta_n/2$. Next take $a$ sufficiently small on a dyadic grid. Use the displayed envelope and B4's vacuum bound to test the full error against $\delta_n$. More explicitly, with a time unit $t_0$, define
$$
 s_0=2\kappa_B,\quad d=e^{-s_0 6\lambda L^3}2^{-3L^3}/s_0,\qquad
 a_*(j)=\frac{t_0\,2^{-j-8}}{(1+t_0c)^2[1+(t_0d)^{-1}]} .
$$
For $a\le a_*(j)$, B4's projector estimate gives $v_a\le\sqrt2\,72\,2^{-j-8}$. Increase $j$ and round $a_*(j)$ down to the dyadic grid until all error and size inequalities hold. Termination follows from positivity of $d$ in each finite box and the envelope at fixed $s$. This rule uses only box parameters, test budgets and tolerances. There is no assumed uniform spectral gap. A growing finite collection can exhaust countably many selected tests.

Take $\delta_n\to0$. For these words any Hamiltonian vacuum correlations that converge have the same real-time limits along the resulting anisotropic Wilson sequence. Outside the finite cone the Hamiltonian commutator with bounded spectators already tends to zero under the support and prefactor hypotheses, so its Wilson vacuum matrix element tends to zero there whether or not the individual words converge. The argument supplies a time sequence for the specified tests. Isotropic time removal, operator-norm locality of every discrete logarithm, existence of nonzero limiting correlations and the Clay gap require further estimates.
