# What a fixed physical-energy window sees

Let $\nu_c$ be the spectral measure of the centered spatial plaquette sum in the [moment estimates](README.md). Its mass is $V_c=M_0(c)$ and $M_1(c)\ge a\|c\|_2^2>0$ for nonzero $c$. The probability law

$$
 P_c^{(1)}(dE)=E\,\nu_c(dE)/M_1(c)
$$

belongs to the normalized vector $Q^{1/2}f_c\Omega/\sqrt{M_1(c)}$. It assigns zero weight to the whole zero-energy sector at each regulator. Its first moment is $M_2(c)/M_1(c)\le d/a$. The underlying plaquette vector has a different spectral law, $\nu_c/V_c$.

## Escape for bounded spatial support

Let $u=\mathbb E(1-x_p)$. The diagonal variance obeys $V_p\le\mathbb E(F_p-2)^2\le8u$. Ground-state translation and cube symmetry give the same bound on all faces. Cauchy–Schwarz gives $V_c\le8u\|c\|_1^2$ even when distant faces are positively correlated. The constant trial gives $u\le1$ when $g>0$; at $g=0$ product Haar gives equality. At $g\ge1$ the product trial also gives $gu\le B\le5\sqrt g/2$ and $1+B\le7\sqrt g/2$. Hence $u(1+B)\le9$ throughout. For $E_*>0$ put $N_c=\|c\|_1^2/\|c\|_2^2$. Then

$$
 P_c^{(1)}([0,E_*])\le\frac{E_*V_c}{M_1(c)}
 \le 450\frac{E_*N_c}{\kappa},\qquad
 \int e^{-tE} dP_c^{(1)}(E)\le\frac{450 N_c}{e\kappa t}\quad(t>0).
$$

The second inequality uses $E e^{-tE}\le1/(et)$. Both bounds are invariant under an overall multiplicative normalization of $c$. Thus if $E_*N_c/\kappa\to0$ in a common physical clock, the normalized energy-weighted law loses all weight below that fixed energy. When $\kappa\to\infty$ and $N_c/\kappa\to0$ in fixed units, its autocorrelation tends to zero at every fixed positive physical time. A single plaquette has $N_c=1$. A fixed number of plaquettes also qualifies, by $N_c\le|\operatorname{supp}c|$.

On B4’s bare tree-level trajectory with spatial spacing $b$, $\kappa=2/(\beta b)$ in this convention. Thus $E_*\beta b N_c\to0$ suffices. No running law for $\beta$ is assumed. For a prospective renormalized observable to keep a fraction $\eta>0$ of its *energy-weighted* norm below $E_*$, it is necessary that $N_c\ge\eta\kappa/(450E_*)$. This is a necessary condition and supplies no candidate continuum field. A small amount of high-energy raw weight can dominate an energy-weighted measure, so this deduction leaves the raw finite-energy weight open. [Hamiltonian matching and bare spatial trajectory](../../../transfer-operator/hamiltonian-time/)

## A statement for orthonormal spatial modes

Let $P$ be the number of faces and choose any orthonormal basis of coefficient vectors $c_1,\ldots,c_P$, including a Fourier basis with fixed coordinate-plane polarizations. The trace of the covariance matrix in that basis satisfies $\sum_j V_{c_j}\le8uP$. As $M_1(c_j)\ge a$, one obtains without a support restriction

$$
 \frac1P\sum_j P_{c_j}^{(1)}([0,E_*])\le 450 E_*/\kappa .
$$

Consequently the fraction of basis vectors retaining at least $\eta$ in that window is at most $450E_*/(\eta\kappa)$. The statement is an average over modes. It leaves room for an exceptional fixed momentum or a prescribed physical smearing.

At fixed spatial cutoff another use of the same trace bound is constructive. For any $0<\epsilon<1$, at least a fraction $1-\epsilon$ of these unit modes have $V_{c_j}\le K=8u/\epsilon$. For each such mode the *raw* spectral measure has mass at least $a^2/(8d)$ in $[a/(4K),4d/a]$. The proof uses the pointwise inequality $E\le L+E^2/U+U\mathbf1_{[L,U]}(E)$ with the displayed endpoints. At positive finite $g$, strict positivity of the vacuum implies $u>0$. At $g=0$, $u=1$. Any individual normalized smearing with a known uniform static susceptibility upper bound $K$ satisfies the same window conclusion with that $K$. Without such control the all-mode covariance floor and relative positive-time lower bound still hold.

Neither large raw variance nor a finite energy-weighted moment establishes a gap. For example the measures $m\delta_{1/m}$ have first moment one and bounded second moment, while all their support approaches zero. In the other direction, $\delta_1+m^{-1/2}\delta_m$ has a raw atom of weight one at fixed energy while its energy-weighted probability there tends to zero. These controls distinguish the two limiting questions. The spatial continuum theory, its full observable space and a common lower bound on its strictly positive energies remain open.
