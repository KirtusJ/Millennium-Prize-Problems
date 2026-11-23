# FOR DISPROOF — does the winding tensor see the first spin-two level?

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Proposed result, awaiting independent review.** In the color-singlet homogeneous SU(2) matrix Hamiltonian the specified bounded tensor has strictly positive projection on the lowest positive-parity spin-two eigenspace. The argument uses preservation of eigenvalue ordering under angular heat flow. It gives no quantitative lower bound. Direct variational projection puts the fraction near **0.883**, challenging the stronger 0.99 prediction and supporting the 0.84 candidate numerically. [Test registered before calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7110059974)

## Operator and scope

Let $Y$ be a real $3\times3$ matrix with spatial row index and color column index. Set $H=-\Delta/2+2\sum_{i<j}|Y_i\times Y_j|^2$, $Q=YY^T$, $t=\mathrm{tr}\,Q$, $B=Q-tI/3$. The reading is $F_A=\mathrm{tr}(AB)/(1+t)$ for a real symmetric traceless $A$ with $\mathrm{tr}(A^2)=1/2$. Denote the scalar vacuum by $\phi_0$. The diagonal-difference and off-diagonal readings give the same limiting spectral measure by spatial rotation. The physical interpretation uses a box-spanning winding probe with $Y=NX$, first taking weak coupling at fixed spatial size. [Stipulations](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7109972966)

For compact resolvent, retain $-\Delta/4$ and pair each remaining $-\Delta_{i+1}/4$ with $2|Y_i\times Y_{i+1}|^2$, cyclically. The two perpendicular harmonic coordinates give a lower bound $\sqrt2|Y_i|$ at each fixed $Y_i$. The retained kinetic energy and the sum of linear bounds give form compactness. Positivity improvement of the scalar Schrödinger heat kernel gives a unique positive invariant vacuum.

## Proposed proof of positive weight

1. Realize the spin-two multiplicity space by equivariant traceless symmetric matrix fields $M$. Contracting against $A$ selects one component. Positive parity together with right color invariance gives right $O(3)$ invariance, since the missing inversion sends $Y$ to $-Y$. Thus $M$ depends only on $Q$. At distinct eigenvalues the three axis half-turns stabilizing $Q$ force $M$ to be diagonal in its eigenframe. Conversely, every measurable traceless triple $u$ in that ordered frame defines such a field almost everywhere. Rotation orthogonality supplies a common positive factor for the norm and energy of a component.

2. Write $q_i=\sigma_i^2$, $0\le q_1<q_2<q_3$. Use the singular-value measure $J\,d^3\sigma$, $J=\prod_{i<j}(q_j-q_i)$. One can let $\sigma_1$ be signed with even continuation. The form contains the scalar radial kinetic term $\frac12\sum_i|\partial_{\sigma_i}u|^2$, scalar potential times $|u|^2$, and
$$\sum_{i<j}w_{ij}(u_i-u_j)^2,\qquad w_{ij}=(q_i+q_j)/(q_i-q_j)^2.$$
At diagonal $Y$, varying $Y_{ij}$ changes $Q_{ij}$ at rate $\sigma_j$. Both off-diagonal entries of $M$ vary at rate $\sigma_j(u_i-u_j)/(q_i-q_j)$. Adding the transposed variation and the kinetic factor $1/2$ yields the coefficient above. Pavel gives the corresponding pair weights in the angular Hamiltonian. [Pavel, §§4–4.2](https://arxiv.org/pdf/hep-th/0701283#page=5)

3. Consider the closed cone $u_1\le u_2\le u_3$ almost everywhere. Put $a=w_{12},b=w_{23},c=w_{13}$. Both $a,b$ exceed $c$, since $(x+y)/(y-x)^2$ for $0\le x<y$ increases in $x$ and decreases in $y$. Under the negative angular generator the two adjacent differences evolve with matrix
$$\begin{pmatrix}-(2a+c)&b-c\\a-c&-(2b+c)\end{pmatrix}.$$
Adding a sufficiently large scalar diagonal before exponentiation shows its exponential has nonnegative entries at positive time. Radial heat acts by the same positive scalar operator on each component, and the scalar potential contributes a positive multiplier. The semigroup product formula preserves the cone.

4. **Collision and rank check.** First impose Dirichlet killing outside a ball and near collisions of absolute singular values. The angular coefficients there are bounded. Use signed $\sigma_1$ across zero and even fields, retaining rank-two configurations with a simple zero singular value. The radial killed heat acts on the adjacent differences with the same boundary conditions. To recover the full matrix form, on bounded sets the weighted volume at gap $s=|\sigma_j|-|\sigma_i|$ is at most $C_Rs\,ds$ because $J$ contains the corresponding difference of squares. The ordered absolute singular values are Lipschitz in $Y$. A logarithmic cutoff interpolating from zero at $\epsilon^2$ to one at $\epsilon$ costs $O_R(1/|\log\epsilon|)$ in gradient energy. Products over gaps handle intersections. On bounded smooth compactly supported equivariant fields these cutoffs converge in the full form norm by that bound and dominated convergence. Such fields form a core by group averaging. Increasing the killed domains therefore recovers the physical semigroup by strong convergence, preserving the closed cone in the limit.

5. The cone spans the real multiplicity space: split each adjacent difference into its positive and negative parts and reconstruct two ordered triples using zero trace. The reconstruction is bounded in $L^2$. The lowest projector $P$ is the strong large-time limit of the energy-shifted heat semigroup in this sector. Thus $P$ preserves the cone. Since it is nonzero, its range contains a nonzero ordered field. The body components of the probe times vacuum are $\phi_0(q_i-t/3)/(1+t)$, strictly ordered almost everywhere. Their dot product with any nonzero ordered traceless triple is positive, by the identity expressing it as one third the sum of the three pairwise difference products. Integration and rotation orthogonality give $P(F_A\phi_0)\ne0$. This works also if the lowest energy has multiple copies.

**Targets for disproof.** A missing even-parity body component, a surviving boundary coupling, or failure of the cone argument on the physical form domain would break the proof. A positive first-level projection gives neither a specified fraction nor any four-dimensional continuum gap.

## Direct projection and adverse control

The tensor Ritz space uses the traceless parts of $Q,Q^2$ times invariant polynomials and a Gaussian. We included derivatives in all nine matrix directions and divided squared projected amplitude by the full probe variance. Degree counts powers of squared singular values. Published energies were used only for comparison.

| Cutoff | Gaussian precision | First two gaps | Lowest fraction | Fraction captured by basis |
|---:|---:|---:|---:|---:|
| 5 | 2.0 | 3.02948, 6.17398 | 0.888648 | 0.999854 |
| 7 | 2.0 | 3.01490, 5.95094 | 0.883917 | 0.999989 |
| 8 | 2.6 | 3.01362, 5.93288 | 0.883466 | 0.999999 |
| 9 | 2.0 | 3.01286, 5.89495 | 0.882932 | 0.999999 |
| 10 | 2.6 | 3.01266, 5.89027 | 0.882838 | 0.9999999 |

At cutoff ten, changing the metric eigenvalue threshold from $10^{-10}$ to $10^{-12}$ shifted the fraction by about $1.1\times10^{-8}$. Pavel's reference gaps converted to our units are 3.01254 and 5.87958. Convergence of the second gap is weaker. These values use the same homogeneous Hamiltonian, and the direct projection shares scalar-vacuum quadrature with the earlier moment estimate. Numerical truncation errors are uncertified. [Published levels, Tables 1–2](https://arxiv.org/pdf/hep-th/0701283#page=5)

**Adverse control.** Multiply $F_A$ by $t/(1+t)-0.74239518246$. The offset was fitted once at cutoff five to cancel the first projected amplitude. With the offset frozen, the lowest fraction at cutoff nine was 0.000102. The spin, parity and winding support agree. The radial factor changes sign and removes the ordered-triple property.

Run [project_tensor.py](project_tensor.py) with one OpenBLAS thread for the first four rows and the adverse control. For the final row call calculate(10, 2.6, 72, 18, tolerance). The PCP OS chain checked the angular rate inequalities at 220 ordered triples and both adjacent-difference generator identities. Three Lean declarations passed; one malformed dispatch and three source mutations were rejected. The form-domain argument and numerical spectra are outside the Lean checks. [Verifier](verify.py) · [Native worker](worker.c) · [Declarations](TensorCone.lean)
