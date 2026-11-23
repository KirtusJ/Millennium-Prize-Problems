# Color-singlet spectral measurements at positive physical time

Take a compact simple visible Lie algebra with dimension $d$ and the metric specified by the character action. In an orthonormal basis $T_a$ put $f_{abc}=\langle[T_a,T_b],T_c\rangle$. Invariance makes $f$ totally alternating. The symmetric positive operator with quadratic form $\sum_b\|[X,T_b]\|^2$ commutes with all adjoint rotations. Its eigenspaces are ideals, so it equals $cI$ on a simple algebra, with $c>0$ and $S=\sum f_{abc}^2=dc$. A group with Abelian Lie algebra has $S=0$.

Choose one real smooth radial compact spatial profile $\psi$ with $J_0=\int\psi\ne0$. At each slice take $X_1,X_2,X_3$ to be the $23,31,12$ magnetic curvatures, transported to a common point of the slice and separately smeared with the weights $r^{-1}\psi(\mathrm{center}(p)/r)$. The common temporal rooting used to compute joint moments leaves all scalar invariants on a slice unchanged. Under either of the stated ordinary-profile conditions (radial profiles have the needed face-center reflection symmetry), the [physical-scale theorem](physical-scale.md) gives
$$
 \mathbb E[X_i^a(t)X_j^b(0)]_{\rm lim}=\delta_{ij}\delta_{ab} C(t),\qquad
 C(t)=\int|\widehat\psi(p)|^2\frac{p_1^2+p_2^2}{2|p|}
                 e^{-|p||t|}\frac{d^3p}{(2\pi)^3}.
$$
Indeed cross-orientation integrals contain $p_i p_j$, $i\ne j$, and their angular integral vanishes. The three diagonal integrals agree. The limiting time processes for distinct colors or orientations are jointly Gaussian and independent. Put $v=C(0)>0$ and let $\mu$ be the positive pushforward of the integral weight under $p\mapsto |p|$. It has no atoms, $C(t)>0$ at every finite $t$, and $\mu(dE)=[|J_0|^2 E^3/(6\pi^2)+O(E^5)]dE$ near zero.

The following original-link operators are gauge invariant at every spacing. For the fourth-order subtraction one may replace $v$ everywhere by the measured $v_r=(3d)^{-1}\sum_i\mathbb E|X_i|^2$; moment convergence gives the same limits. Use the connected correlation in the finite-box vacuum, subtracting its actual mean before taking spectral measures.

| Time-slice observable | Limiting connected correlation | Limiting physical-energy measure |
| --- | --- | --- |
| $Q=|X_1|^2/2$ | $(d/2)C(t)^2$ | $(d/2)\mu^{*2}$ |
| $T=\langle X_1,[X_2,X_3]\rangle$ | $dc\, C(t)^3$ | $dc\,\mu^{*3}$ |
| $W=H-cv(|X_1|^2+|X_2|^2)+dcv^2$, $H=\|[X_1,X_2]\|^2$ | $3dc^2 C(t)^4$ | $3dc^2\mu^{*4}$ |
| $H$ without the subtraction | $4dc^2 v^2 C(t)^2+3dc^2 C(t)^4$ | $4dc^2 v^2\mu^{*2}+3dc^2\mu^{*4}$ |

For $T$ each orientation has only one factor at each time, hence Wick contraction joins all three factors across the two slices, leaving $\sum f_{abc}^2 C(t)^3$. In $H$, let $L_{abcd}=\langle[T_a,T_b],[T_c,T_d]\rangle$ multiply $X_1^a X_2^b X_1^c X_2^d$. Replacing each same-orientation pair by its Wick-ordered version subtracts the two quadratic terms displayed in $W$ and adds $dc v^2$. The quartic tensor symmetric in the two equal-orientation pairs is $K=(L+L')/2$, $L'_{abcd}=L_{adcb}$. Jacobi and invariance give $L-L'=\langle[T_a,T_c],[T_b,T_d]\rangle$, a permutation of $L$. All three tensors have the same squared norm, $\|L\|^2=dc^2$, since $\sum_{ab}f_{abi}f_{abj}=c\delta_{ij}$. Therefore $\langle L,L'\rangle=\|L\|^2/2$ and $4\|K\|^2=3dc^2$. The two pairings for each orientation in the cross-slice Wick product give the fourth-order covariance in the table. The subtracted quadratic component is orthogonal to it at all time separations. A subtraction coefficient $h$ instead of $cv$ leaves an additional $4d(cv-h)^2 C(t)^2$ in the connected reading.

For the [microscopic group commutator](cube.md), independent color vectors of variance $v=1/2$ give one half of $H$. Thus its variance is $(4+3)dc^2(1/2)^4/4=7dc^2/64$. This uses a genuine group commutator for the microscopic measurement; $T,H,W$ in the table are Lie-algebra contractions of coherently smeared link data.

For the normalized fundamental trace on $SU(N)$, $d=N^2-1$ and $c=2N^2$. To check the factors, complete the traceless anti-Hermitian basis by $iI$. After multiplication by $-i/\sqrt N$ this is a trace-orthonormal Hermitian matrix basis, complete also as a complex basis of matrices. Entrywise completeness gives $\sum_{a\,{\rm traceless}} T_a M T_a=-N\operatorname{Tr}(M)I+M$. In particular $\sum T_a^2=-(N^2-1)I$ and $-\sum[T_a,[T_a,X]]=2N^2 X$ for traceless $X$. For the normalized adjoint trace of any compact simple Lie algebra, the Wilson metric is minus its Killing form divided by $d$, giving $c=d$. This dependence on normalization matters already for the two different trace actions on the local algebra of $SU(2)$ and $SO(3)$.

All operators in the table have finite-regulator moments; joint moment convergence yields the displayed connected readings, including zero time and their total spectral masses. For $E=-r\log\widehat T_{\rm transfer}$, the measures converge after $E\mapsto e^{-E}$: every integer Laplace moment converges by the nearest-step error $O(1/(rj))$ at integer $j\ge1$, and polynomials are dense on $[0,1]$. The limiting convolutions exhaust the mass at time zero. Their small-energy masses are
$$
        \mu^{*n}([0,\epsilon])\sim
           \frac{(|J_0|^2/\pi^2)^n}{(4n)!}\epsilon^{4n}.
$$
This follows by integrating the product of the $n$ densities over an energy simplex. The three pure channels $Q,T,W$ thus have powers eight, twelve and sixteen with the coefficients in the table. All three have positive raw weight on every sufficiently small fixed physical energy window; a positive physical vacuum gap along these rapidly weakening trajectories is excluded in the measured sector. The high-order signals and their Lie factors are present in a Gaussian field. They do not establish scattering or a nonzero renormalized self-coupling. For arbitrary $\beta,L\to\infty$ the same second-order symmetric-profile choice as in the $SU(2)$ result gives $\min(\beta^{1/13},L^{1/3})\Delta_{\rm lattice}\to0$ for every fixed nontrivial visible compact simple group.

## A ratio using a single positive separation

At any fixed physical $t>0$ one can test the color contractions without fitting $v$, the profile amplitude or the Casimir. Use the **unsubtracted** $H$ and $Q_\Sigma=(|X_1|^2+|X_2|^2)/2$. Form the $2\times2$ matrix $M_r(t)$ of their connected cross-slice readings and let $C_{T,r}(t)$ be the centered cubic reading at the same separation. In the limiting law $M_{11}=dC(t)^2$, $M_{12}=M_{21}=2cv\,d C(t)^2$, and $M_{22}$ is the unsubtracted row of the table. Therefore
$$
          \lim \frac{\det M_r(t)}{C_{T,r}(t)^2}=3 .
$$
The denominator has a strictly positive limit when the group is non-Abelian and the profile is nonzero. Adding any fixed multiple of $Q_\Sigma$ to $H$ leaves the determinant unchanged. This result uses the common radial profile and the invariant metric in the definitions of all three insertions. It compares distinct accessible gauge-invariant measurements of one Wilson ensemble. The ordinary winding-trace determinant involves different observables.

For $SU(2)$ the Lie bracket of unit imaginary quaternions is twice their vector cross product. Accordingly the cubic coefficient here is 24, and D4's determinant of three sharp loop circulations has coefficient 6 for diagonal circulation covariance. The smearing and normalization are different. For $SU(3)$ there is a second independent cubic reading with the opposite charge-conjugation parity. [D4's ordinary trace words](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/0947647fab6af00e87e7b601baf36a2130630224/yang-mills/spectral-support/ordinary-loop/singlet-sector.md) · [Symmetric cubic and imaginary Wilson trace](charge-conjugation.md)
