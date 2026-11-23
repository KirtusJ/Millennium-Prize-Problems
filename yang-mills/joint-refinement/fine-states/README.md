# Fine states at one fixed physical time

**G4, for disproof by Z4 and the other directors.** In the isotropic four-dimensional SU(2) Wilson regulator one can bound the part of the fine space orthogonal to a finite set of magnetically weighted electric states. For every spatial side $N$ and bare coupling $\beta>0$ an explicit choice of maximum link representation gives a fine-to-fine norm at most $N^{-6}$ and a coarse-to-fine norm at most $N^{-3}$ on that discarded space, at physical time $\ell$. The remaining space contains geometrically fine states built from low link spins. Its dimension grows under subdivision. Its norm is the open part of the argument.

A full calculation in the nonzero-mode quadratic Wilson model bounds both blocks through arbitrarily many adjacent refinements. A compact electric control shows exactly how much of Z4’s spatially averaged winding probe can escape the coarse algebra even at low spin. [Quadratic model](gaussian.md) · [Normalization and winding counterexample](winding.md) · [Previous fixed-scale attempt](../../g4/full-attempt/physical-refinement/isotropic.md)

## The interacting cutoff

Use periodic cubic space, $N\ge2$, spacing $\ell/N$, $d=3N^3$ spatial links and normalized product Haar measure. Write $T=AKA$ with $A=\exp[-\frac\beta2\sum_p(1-\frac12\operatorname{Tr}U_p)]$ and $K=\bigotimes_e K_e$ the product of normalized temporal convolutions. On unrestricted link space this compact positive operator has a strictly positive continuous kernel. Its simple top eigenfunction $\Omega$ is invariant under gauge transformations and spatial center flips by uniqueness and positivity. Restriction to the physical center-neutral sector therefore keeps the same norm $\lambda$. In temporal gauge, imposing the vertex gauge projection gives the physical transfer on this invariant subspace. Set $H=T/\lambda$ and $S=H^N$. [Lüscher’s Wilson transfer construction](https://doi.org/10.1007/BF01614090)

On one link, let $n=2j$ denote the nonnegative integer labeling the SU(2) representation. Schur orthogonality divides the character integral by $n+1$. Substituting $\chi_n(\theta)=\sin((n+1)\theta)/\sin\theta$ in the Haar integral with density $2\sin^2\theta/\pi$ gives the normalized convolution multiplier $k_n=I_{n+1}(\beta)/I_1(\beta)$. Indeed the integral before division is proportional to $I_n-I_{n+2}=2(n+1)I_{n+1}/\beta$. The positive Bessel series gives
$$k_n\le (\beta/2)^n/(n+1)!$$
term by term since $(m+1)!/(m+n+1)!\le 1/(n+1)!$. Let $\Pi_L$ retain $n\le L$ on every link, $\tau_L=\sup_{n>L}k_n$, and $T_L=AK\Pi_L A$. Each object respects the gauge and center projections. Earlier local-quantum-number truncation work controls Hamiltonian dynamics under assumptions on the initial state. Here the estimate uses the Euclidean kernel and is relative to its actual vacuum eigenvalue. [DLMF, modified Bessel series](https://dlmf.nist.gov/10.25.E2) · [Tong et al., 2022](https://arxiv.org/abs/2110.06942)

**Local comparison.** For a specified edge $e$, separate its four incident spatial plaquettes, $A=A_eA_{\rm rest}$. Even at $N=2$ opposite parallel links are distinct and each incident face is counted once. Then $e^{-4\beta}\le A_e\le1$, and $A_{\rm rest}$ is independent of that link. Removing these four factors gives $A_e^{-1}TA_e^{-1}=K_e\otimes B$, with $B=A_{\rm rest}K_{\rm rest}A_{\rm rest}$. Since $\|K_e\|=1$, $\|B\|\le e^{8\beta}\lambda$. This comparison is performed on unrestricted link space before taking physical compressions.

The commuting link projections obey $0\le I-\Pi_L\le\sum_e(I-\Pi_{e,L})$. Each summand of $AK(I-\Pi_L)A$ is bounded above in the corresponding sum by the positive operator $A_e[K_e(I-\Pi_{e,L})\otimes B]A_e$ of norm at most $\tau_L e^{8\beta}\lambda$. Hence
$$0\le T-T_L,\qquad \|T-T_L\|/\lambda\le\epsilon=d e^{8\beta}\tau_L.$$
For example, take $L\ge \max(e\beta,(8\beta+\log d+3\log N)/\log2)$. For $n>L$, the factorial bound and $n!\ge(n/e)^n$ give $k_n\le2^{-n}$, hence $\epsilon\le N^{-3}$ along any trajectory $\beta=\beta_N$. The cutoff varies with $\beta$ and $N$. The sharper rational factorial estimate gives the following ceilings at the five previously used couplings, using $\beta\le7/2$ throughout. The odd sizes also satisfy the spin estimate. Straight two-to-one geometric blocking requires an even fine size. [Matched couplings](../../g4/full-attempt/physical-refinement/isotropic.md) · [Rational computation](wilson.py)

| Fine side $N$ | Retained $L=2j_{\max}$ | Upper bound on relative one-step error, rounded up |
|---:|---:|---:|
| 5 | 21 | 0.004663 |
| 6 | 22 | 0.000588 |
| 7 | 22 | 0.000934 |
| 8 | 22 | 0.001393 |
| 10 | 23 | 0.000191 |

## How the cutoff meets spatial blocking

Use the true neutral vacuum complement $\mathcal H_0$. The coarse projection in Haar coordinates is obtained by taking conditional expectation on the coarse straight-link orbit algebra in $L^2(\Omega^2\,dU)$ and conjugating by multiplication by $\Omega$ back to Haar coordinates. Restrict it to centered functions and call it $P$; write $Q=I_{\mathcal H_0}-P$. In formulas acting on the full space extend both projections by zero off $\mathcal H_0$. This construction identifies the coarse marginal of the fine vacuum. Comparing it to the vacuum of a separately simulated coarse Wilson action takes an additional estimate.

Let $R$ project onto $\operatorname{Ran}(QA\Pi_L)$ with the electric domain restricted to the physical neutral sector including its vacuum direction, and set $U=Q-R$. This range is finite dimensional. For $u=Uu$, orthogonality gives $\Pi_L A u=0$, hence $T_Lu=0$ and $\|Hu\|\le\epsilon\|u\|$. This is a statement about the **weighted and projected range**. Bare electric label cutoffs need not commute with the magnetic factor or with $Q$.

Since $0\le H\le I$ and $N\ge2$, $H^N\le H^2$, giving $\|USU\|\le\epsilon^2$. Put $a=\|PSP\|$, $b_R=\|RSR\|$ and $\eta_R=\|PSR\|$. Factoring through $S^{1/2}$ gives
$$
 \|PSU\|\le\sqrt a\,\epsilon,\qquad
 b_R\le\|QSQ\|\le b_R+\epsilon^2,\qquad
 \eta_R^2\le\|PSQ\|^2\le\eta_R^2+a\epsilon^2 .
$$
For the second inequality apply the row bound to $S^{1/2}[R,U]$. The last follows by adding $PSRSP$ and $PSUSP$. Lower bounds follow by restriction. Thus the fine-block and squared coupling corrections are at most $N^{-6}$ after retaining the indicated range. A proof would still need bounds on $b_R,\eta_R$ and the inherited coarse compression with uniform room in the two-block inequality. [Two-block criterion](../../g4/full-attempt/physical-refinement/isotropic.md)

**Finite matrices for disproof.** Write $T_L/\lambda=XX^*$ using the retained Peter–Weyl states and their electric eigenvalues, for example $X=A V D^{1/2}/\sqrt\lambda$ in an orthonormal retained basis $V$. With $Z=X(X^*X)^{(N-1)/2}$ one has $(T_L/\lambda)^N=ZZ^*$. Telescoping between positive contractions bounds the physical-time operator error by $N\epsilon$. With $G_P=Z^*PZ$ and $G_Q=Z^*QZ$, the finite answers for the full fine block and coupling are $\|G_Q\|$ and $\|G_Q^{1/2}G_PG_Q^{1/2}\|^{1/2}$, each within $N\epsilon$ of the corresponding target. This route needs the true blocked vacuum inner products. A bound on the complete neutral gap can alternatively bypass that projection: if $r_L$ is the ratio of the two largest eigenvalues of the finite neutral matrix $X^*X$, min–max gives $(1-\epsilon)r_L\le\lambda_1/\lambda\le r_L+\epsilon$ for $\epsilon<1$. The finite matrices grow exponentially in the number of links even before one addresses quadrature. No values of these growing four-dimensional residual matrices are supplied here.

An interacting one-square SU(2) control checks the formulas in character quadrature. Four electric convolutions act on the plaquette character with eigenvalue $k_n^4$. The sign of its trace defines a two-cell coarse algebra. At $\beta=1.6$, four time steps, and $L=2$, increasing the number of nodes from 48 to 192 gives $b$ from $9.743$ to $9.758$ in units of $10^{-9}$, and $\eta$ from $1.2966$ to $1.2971$ in units of $10^{-8}$. Both Gram identities and the tail bounds are checked at each size. These are floating controls for a smaller compact system. [Executable check](wilson.py)

## What would close the residual

Work on the centered physical space. For $0<h<1$ let $E=\mathbf1_{(h,1]}(S)$ and $\delta=\|QE\|$. Its square is the maximum lost blocked variance as a supremum over all unit vectors in this band. Spectral calculus gives $\|QSQ\|\le h+(1-h)\delta^2$. Also $\|PSQ\|\le h/2+(1-h)\delta$: subtract $hI/2$ from $\min(S,hI)$ when compressing off diagonal, and bound $(S-hI)_+Q$ on $E$. For the top eigenvector $v$ of the centered compact transfer, if its eigenvalue $r>h$, then $PSP\succeq r|Pv\rangle\langle Pv|$ and $\|Pv\|^2\ge1-\delta^2$. Thus $r\le\max(h,a/(1-\delta^2))$ for $\delta<1$. This is useful only if the coarse contraction beats the worst lost variance. Checking a finite list of winding probes does not bound that supremum. [Projection/restriction estimates for finite Markov chains, Jerrum et al.](https://arxiv.org/abs/math/0503537)

The proof attempt stops at uniform control of the retained fine states in the interacting vacuum. A4’s fixed-box exterior estimate and Z4’s two-site tensor energies address a different order of limits. C4’s one-site enclosure demonstrates an actual small-regulator electric truncation with controlled magnetic integrals. Neither supplies the growing retained matrices. [Z4’s two-site measurements](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/22e08d0/yang-mills/z4/attempt/A3_NOTES.md) · [C4’s enclosure](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/5c35197/yang-mills/spectral-support/finite-readings/periodic-vacuum/center-sectors/README.md) · [Checks and PCP evidence](checks.md)
