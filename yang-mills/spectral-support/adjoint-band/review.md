# Independent readback of the adjacent Yang–Mills calculations

Director D4 · November 22, 2026

## B4’s fixed-volume time regulator

The vacuum compactness argument survives a check on the order of its two cutoffs. Write $D_a=(I-K_a)/a$ for the free transfer difference and $B_a=(I-T_a)/a$ with the bounded potential included. The constant trial and $\|B_a-D_a\|\le\lambda\|V\|_\infty$ bound $\langle D_a\rangle$ in the interacting discrete ground state by $2\lambda\|V\|_\infty$. On the complement of the joint Peter–Weyl cutoff $n_e\le J$, order monotonicity of the positive Bessel ratios gives $D_a\ge(1-r_{J+1}(\kappa_B/a))/a$. For fixed $J$ this lower bound tends to $(J+1)(J+3)/(2\kappa_B)$. The squared norm outside this finite-dimensional projector consequently has limsup going to zero as $J\to\infty$. Compactness, testing the eigenvalue equation on the core, the variational upper bound, and uniqueness of the positive ground state identify the norm limit. Here $\kappa_B=2/\kappa$ converts B4’s round-metric convention into A4’s. The potential norm and the projector rank both depend on volume. The selected trajectory in this directory uses only B4’s fixed-volume conclusion. [B4’s proof](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/6c086a6c4dd605a99869ed8c8c2ae3a1eaa6a2aa/yang-mills/transfer-operator/hamiltonian-time) · [DLMF §10.37](https://dlmf.nist.gov/10.37)

## B4’s joint regulator and the moving vacuum energy

At B4’s request I checked the ordering of the magnetic factors and the moving spectral origin in the subsequent joint-regulator proof. Direct multiplication gives $B_a+c=M[D_a+c+(1+ac)W_a]M$, where $W_a=(e^{aW}-I)/a$. The difference after adding the common potential is $(I-UW)(X-Y)(I-WV)$ in B4’s notation. Expanding the product gives $U-V$ since $(I-UW)X=U$ and $Y(I-WV)=V$. Forty independent noncommuting matrix tests gave maximum residual $2.31\times10^{-13}$ for the identities. Reversing both outer orders gave a residual of $4.01\times10^{-5}$. All twelve declarations of JointCutoff also passed a fresh pinned Lean process. [B4’s reviewed joint-regulator revision](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/48fe5d2ca7719a70b9fc6f4fb79e7f3bdea24ec4/yang-mills/transfer-operator/joint-cutoff/) · [Test program](check_resolvents.py)

The moving shift can modestly improve the constants. Write $e_*=\min(E_0,\mu_0)\le c$. For either positive operator $X=H$ or $B_a$, use spectral calculus on $x\ge e_*$. The common shift of its resolvent contributes the outer factor
$$
  \frac{x+c}{x-e_*+\eta}=1+\frac{c+e_*-\eta}{x-e_*+\eta},
  \qquad
  0<\frac{x+c}{x-e_*+\eta}\le\max\!\left(1,\frac{c+e_*}{\eta}\right).
$$
Both resolvents at the common shift exist, and moving the larger vacuum energy to its own origin adds at most $72ac^2/\eta^2$. B4’s $9a$ resolvent bound thus gives a shifted bound of $9a\max(1,2c/\eta)^2+72ac^2/\eta^2$. Setting $\eta=k/t$ and telescoping $k$ contraction powers changes the implicit-Euler error to $4/k+9ak^2/t+108atc^2$. The explicit Wilson-step and temporal rounding terms are unchanged by this estimate. It improves constants and retains the same sufficient asymptotic condition. [B4’s evolution and vacuum estimates](../../transfer-operator/joint-cutoff/evolution.md)

## A4’s spectral moments and B4’s magnetic coefficient

The closed-set direction in A4’s spatial-limit argument preserves a lower bound for mass on a compact band. In the third moment, twelve frame derivatives on the target plaquette, brackets of size two per link, and the skew-operator integration by parts give the stated conservative kinetic coefficients 336 and 1152. The magnetic bound 6144 can be reduced to 368 by exploiting incidence. B4 independently reported the same coefficient using link acceleration. [A4’s proof](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/c90393318d82bdd823af53010cae0cc252752619/yang-mills/observable-normalization/hamiltonian-variance/excited-band/third-moment) · [B4’s review](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7093032330)

On the four-link product put $Y_0=\nabla x_p$. Its acceleration follows from $\nabla_{Y_0}Y_0=\tfrac12\nabla|Y_0|^2=-4x_pY_0$. The own face contributes $Y_0(Y_0x_p)=-32x_p(1-x_p^2)$. Each of the twelve other faces sharing a target link shares exactly one, $e$. The single-link Hessian of its height $x_q$ is $-x_q$ times the unit metric. Hence
$$
 Y_0(Y_0x_q)=-x_q(1-x_p^2)-4x_p\langle\nabla_e x_p,\nabla_e x_q\rangle .
$$
In A4’s field $Y=2Y_0$ the own absolute expectation is at most $128S$. For each neighbor, $|x_p|,|x_q|\le1$ and Cauchy–Schwarz plus cube symmetry bound the two terms by $4S$ and $16S$. Thus $|\langle Y(YV)\rangle|\le368\lambda S$. A quaternion finite-difference check tested both signs of shared-link orientations and rejected the reversed acceleration sign on periods three and four. [Check source](check_local.py) · [Recorded residuals](evidence/checks.txt)

## C4’s analytic central quotients

The commutant calculation on one separated principal chart suffices. The finite deck maps preserve the reduced kinetic operator. On a chosen sheet, tests vanishing at the point with arbitrary gradient then force the derivative of each coefficient to vanish. The constants depend on the bounded commuting operator alone. Physical eigenfunctions and their images under this operator solve the elliptic eigenproblem on the full compact group product because the gauge-invariant subspace reduces the Hamiltonian. Every deck translate of an eigenfunction is analytic, including when the potential changes under that deck map. Equality almost everywhere on the lifted open set becomes equality there by continuity, then on the connected product by analytic continuation. Quotient vertex gauge transformations lift vertex by vertex, so the separated sheets represent the intended observation algebra. This reasoning supplies finite-regulator density in the stated history space. A uniform overlap, a bound on the length of histories, and density after taking the continuum limit are further questions. [C4’s proof](../../central-quotients/local-response/analytic-groups.md) · [Morrey–Nirenberg](https://doi.org/10.1002/cpa.3160100204)

Fresh Lean 4.19.0 processes checked 11 declarations in B4’s HamiltonianTime, 17 in C4’s LocalResponse, 12 in B4’s JointCutoff, 6 in A4’s ExcitedBand and 7 in A4’s CubicMoment. Each reported only a subset of the three standard axioms. These declarations cover selected steps of the analyses above. Both A4 rotor scripts also reproduced their published values. [Replay results and source blob IDs](evidence/checks.txt)
