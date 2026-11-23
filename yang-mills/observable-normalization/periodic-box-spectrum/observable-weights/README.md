# Which observables see the ordered neutral levels?

Director A4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Disposition submitted for review.** On a fixed periodic SU(2) Wilson box, the centered single spatial plaquette energy $Y=\beta(1-\mathrm{Re}\,P_{ij}(x))$ has nonzero limiting variance. Yet its spectral weight in the first neutral excitation, and throughout a fixed interval above the collapsing soft levels, tends to zero as $\beta\to\infty$. Its limiting spectrum is explicitly a sum of pairs of nonconstant-mode frequencies. Bounded center-neutral functions of three based spatial winding loops can instead detect **every** soft eigenspace, including the first. These results use the [fixed-box ordered spectrum](../full-neutral.md), its [quasimodes and transfer normalization](../README.md), and vacuum subtraction. The box is fixed before taking weak coupling.

## Vacuum and spectral projector identification

Write $h=\beta^{-1/3}$, $s=\beta^{-1/2}$ and $n=N_1N_2N_3$. In a based slice the links have quaternion logarithms $hX_i+sz_i(x)$, where $z$ is mean-zero and transverse. Denote by $J_h$ the following contraction from the model space into the full neutral Hilbert space, on globally color-invariant functions. Restrict to the growing central rectangle of the parent proof, undo its unitary coordinate and density changes, and sum its eight disjoint center translates with factor $1/\sqrt8$. For every fixed model vector $u$, $\|J_h u\|\to\|u\|$. The slow Hamiltonian is $H_N=-\Delta/(2n)+2n\sum_{i<j}|X_i\times X_j|^2$. Use $\varphi_0>0$ for its normalized ground state, $\epsilon_j=n^{-1/3}e_j$ for its eigenvalues, and $\gamma$ for the normalized hard Gaussian ground vector.

Up to phase the exact normalized vacuum satisfies $\|\Omega_\beta-J_h(\varphi_0\gamma)\|\to0$. More generally, for a fixed slow eigenvalue $\epsilon$, the full spectral cluster at vacuum-unsubtracted energy $E_{*,N}+h\epsilon+o(h)$ approaches the lifted eigenspace $(\ker(H_N-\epsilon))\gamma$ in projection norm, using the orthogonal projection onto the span of the lifted vectors. Indeed the corrected quasimodes from the parent proof have residual $o(h)$, and the corrections vanish in norm. For graph-norm approximants a diagonal choice approaches the original eigenbasis; compact support and the Gaussian cutoff can be taken along that sequence. Intervals of radius $c h$ separating neighboring model levels then have the exact limiting rank by the full ordered-energy law, and orthogonal leakage of each quasimode is $o(1)$ by the residual bound. Equal finite ranks and asymptotic orthonormality give projection-norm convergence. This last step would fail with spectral inclusion alone.

Let $K_\beta=T/\lambda_0$ be the positive vacuum-normalized transfer. For every fixed invariant $u$,
$$ \|K_\beta J_hu-J_h(I\otimes G/g)u\|\longrightarrow0, $$
where $G$ is the central hard Gaussian transfer with top eigenvalue $g=e^{-E_{*,N}}$. On compactly supported smooth tests this follows by the local electric and magnetic comparison, the $O_N(h|\log h|)$ hard coupling, and the fact that the slow Gaussian is an approximate identity. Output outside the patch is negligible by the full-space Wilson jump bound in the parent proof. Extend by density and contractivity ($\lambda_0\to g$). Iteration applies at each fixed integer time.

## A local plaquette produces two hard oscillators

On compact sets in $(X,z)$,
$$ s^{-1}\,\mathrm{Im}\,P_{ij}(x)\to Z=(\nabla_i z_j-\nabla_j z_i)(x),\qquad Y\to |Z|^2/2. $$
The constant slow terms cancel at first order. All second-order link terms are $O(h^2)=o(s)$ on compact sets. Near identity, $1-\mathrm{Re}\,P=|\mathrm{Im}\,P|^2/(1+\mathrm{Re}\,P)$. Center translations leave the plaquette unchanged. A bounded continuous clipping of $Y$ therefore sends the true vacuum to the lift of the corresponding clipped Gaussian observable on $\varphi_0\gamma$, with error tending to zero in norm. This follows first on compact sets and then by approximation in $L^2$.

At the next order on compact rescaled sets, $Y=|Z|^2/2+2\sqrt h\,Z\cdot(X_i\times X_j)+O_N(h)$. The constant-link commutator supplies $2h^2 X_i\times X_j$ in the plaquette amplitude. In the limiting product model the displayed cross term creates one hard oscillator with a slow color vector. Squaring that term gives order $h$. Assigning an order-$h$ asymptotic to an exact finite-coupling spectral projection would also require control of the vacuum and of the projector at the corresponding order. The [numerical control](check.py) imports the [shared quaternion routines](../../second-box/transverse-plaquettes/check.py) from the repository. [Z4's independent expansion and finite-box tests](../../../z4/attempt/reviews/l1-obs/report.md)

Removing the clipping requires a tail estimate. Let $S$ be the entire spatial Wilson action before multiplication by $\beta$. The exact eigenfunction equation with $T=e^{-\beta S/2}K_{\rm electric} e^{-\beta S/2}$ implies
$$ \|e^{\beta S/2}\Omega_\beta\|\le1/\lambda_0 . $$
Since $Y\le\beta S$, the vacuum expectation of $e^Y$ is uniformly bounded at large $\beta$ on this fixed box. This gives uniform integrability of all polynomial moments, including the squared norm of the difference between $Y$ and its clipping. The model Gaussian also has finite polynomial moments. Hence $(Y-\langle Y\rangle)\Omega_\beta$ approaches the lift of $\varphi_0 (|Z|^2-\mathbb E|Z|^2)\gamma/2$. Its hard factor is orthogonal to $\gamma$.

More precisely, let $p_i=2\pi k_i/N_i$, $d_i=e^{\mathrm i p_i}-1$, $m_p=\sum|d_i|^2$, $\omega_p=\operatorname{arcosh}(1+m_p/2)$, and set
$$ a_p=\frac{|d_i|^2+|d_j|^2}{2n\sinh\omega_p}\quad(p\ne0),\qquad k(t)=\sum_{p\ne0}a_p e^{-t\omega_p}. $$
A real hard oscillator has ground variance $1/(2\sinh\omega_p)$ and its coordinate times the ground state has relative transfer eigenvalue $e^{-\omega_p}$. The curl annihilates the longitudinal mode. Unitarity of the discrete Fourier transform therefore gives $k(t)$ as the same-color covariance of $Z$ at the two times. Conjugate momenta in this sum account for the real modes; they carry no additional degeneracy factor. Different colors are independent. Wick contraction (or expansion in Hermite polynomials of degree two) yields
$$
 \lim_{\beta\to\infty} C_{Y,\beta}(t)=\tfrac32 k(t)^2,\qquad
 \mu_{Y,\infty}=\tfrac32\sum_{p,q\ne0}a_p a_q\,\delta_{\omega_p+\omega_q}.
$$
Here $C_{Y,\beta}(t)=\langle (Y-\langle Y\rangle)\Omega_\beta,K_\beta^t(Y-\langle Y\rangle)\Omega_\beta\rangle$. The measure statement is weak convergence in compactified energy $[0,\infty]$: push forward by $e^{-E}$, use all integer moments including zero on $[0,1]$, then polynomial density. At zero time the limiting variance $3k(0)^2/2$ is strictly positive. The earlier [single-face periodic-limit transform](../../transfer-increments/local-action/spectrum.md) has the corresponding integral over momenta; the result here keeps the finite box and identifies the soft neutral sector explicitly.

The smallest energy carrying limiting weight is $E_{ij}=2\operatorname{arcosh}[1+2\sin^2(\pi/\max(N_i,N_j))]$. A mode with momentum only in the perpendicular direction has zero weight. For every $0<b<E_{ij}$, the **total** centered plaquette weight in $[0,b]$ tends to zero. This also holds after division by the plaquette variance. For every sequence of times $t_\beta\to\infty$ in lattice steps, $C_{Y,\beta}(t_\beta)\to0$: positivity bounds it by the covariance at an arbitrary fixed earlier time, whose limit tends to zero as that earlier time grows. No rate for individual soft matrix elements follows from this convergence.

## Center-neutral probes with positive soft spectral weight

Choose the three straight winding holonomies $H_i$ through a common base site, and define the three gauge-covariant vectors
$$ V_i=\frac{(\mathrm{Re}\,H_i)\,\mathrm{Im}\,H_i}{N_i h}. $$
A center flip multiplies both numerator factors by the same sign. Site gauge transformations rotate all three vectors simultaneously at the base. Each bounded continuous simultaneous-rotation-invariant $f$ therefore gives a gauge-invariant neutral observable $f(V)$. For fixed box lengths $V_i\to X_i$ on compact rescaled sets: the linear winding sum is $N_i hX_i+O_N(s)$, and the group-product remainder is $O_N(h^2)$. Boundedness gives vacuum-vector convergence to $J_h(f(X)\varphi_0\gamma)$ as above.

Write $w=(f-\langle f\rangle_{\varphi_0})\varphi_0$ for real $f$, and $P_\epsilon$ for the slow eigenspace projection. On the clock $h\lfloor\tau/h\rfloor\to\tau>0$ the limiting connected covariance is
$$
 \sum_{\epsilon>\epsilon_0}\|P_\epsilon w\|^2\,e^{-\tau(\epsilon-\epsilon_0)}.
$$
For each finite collection of separated levels, the projector convergence proves convergence of its masses. Their limiting sum exhausts $\|w\|^2$ by completeness, which also equals the limiting full variance. This controls the discarded tail without a bound uniform in the eigenvalue index. A single example $f(X)=1-e^{-|X_i|^2}$ has positive variance and positive limiting covariance at every finite slow time, since $\varphi_0$ is positive.

More strongly, the vectors $f\varphi_0$ with bounded smooth compactly supported invariant $f$ are dense in the slow invariant Hilbert space. Division by $\varphi_0$ identifies it with invariant $L^2(|\varphi_0|^2dX)$; approximate by compact smooth functions for this finite smooth measure and average over color rotations. Centering takes the orthogonal projection off the vacuum. Thus some $f(V)$ has positive limiting spectral weight in any specified non-vacuum soft eigenspace. For any unit vector in that eigenspace such vectors can approximate it to arbitrary accuracy in the model limit. This substantiates visibility of the first gap for this **family of box-spanning, coupling-dependent probes**. No particular simple trace is asserted to isolate the first excitation.

A second geometry explains why summing amplitudes before squaring changes the answer. In a whole periodic $ij$ plane parallel transport each $\mathrm{Im}\,P_{ij}(x)$ to one base along fixed lattice paths and average. The result transforms by a single color rotation and is neutral under the center. On compact rescaled sets its leading $s$ curl telescopes to zero in the plane, while the constant-field commutator contributes $2h^2 X_i\times X_j$. The mixed and cubic terms are $O_N(hs+s^2+h^3)$; conjugation along the bounded paths changes an $O_N(s+h^2)$ amplitude by $O_N(h(s+h^2))$. Consequently division by $h^2$ followed by a bounded continuous function of the squared norm yields a soft limit depending on $4|X_i\times X_j|^2$. Path independence at subleading order is not required. This observable uses a full spatial plane even though its individual plaquettes are contractible.

## A volume check with a specified order of limits

For cubes $N\ge3$ the lowest active momentum shell has four members for a fixed plaquette orientation. Writing $m=4\sin^2(\pi/N)$, $\omega=\omega(m)$, its total one-leg weight is $2m/(N^3\sinh\omega)$. The threshold atom therefore has mass $\tfrac32[2m/(N^3\sinh\omega)]^2$. After the fixed-box weak-coupling limit, $2N\omega\to4\pi$ and $N^8$ times this mass tends to $24\pi^2$. For $N=2$ the two momentum signs coincide, leaving two active modes rather than four.

With side $\ell$ and spacing $a=\ell/N$, the first atom of this **iterated Gaussian limit** lies at physical energy approaching $4\pi/\ell$ and has mass approaching $24\pi^2/\ell^8$ for $a^{-4}Y$. This calculation concerns the first atom only. Its threshold goes to zero as $\ell$ increases. The interacting continuum problem requires control along an independently scale-set joint limit, with renormalized observables of fixed physical support; neither the winding family nor this order of limits supplies that control. [Native replay, Lean scope and numerical controls](checks.md)
