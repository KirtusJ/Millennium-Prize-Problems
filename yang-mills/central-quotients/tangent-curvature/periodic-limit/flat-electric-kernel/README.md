# The gauge-projected electric step on the periodic two-site Wilson cube

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For two spatially constant SU(2) link triples on the periodic $2^3$ cube, the exact temporal Wilson action minimized over all eight site rotations is eight times the smallest eigenvalue among eight real symmetric $4\times4$ matrices. Near the trivial connection the integrated kernel also admits a relative estimate. Dividing by the value at the trivial connection, it equals a **single global SU(2) orientation integral** times $1+O_R(\beta^{-2/3})$ if both triples have angles at most $R\beta^{-1/3}$. This holds for noncommuting constant triples and for arbitrarily unequal values of the kernel on that patch. The estimate is pointwise in the two boundary configurations. Controlling the transfer after integration over nonconstant spatial boundary fields remains open.

## Exact action and its minimizer

Use isotropic lattice units and normalized site Haar measure. Write $U_i,V_i$ for the link matrices in the two spatial slices. Let $g_x$ be the temporal link at site $x$. With every positive spatial link counted, put
$$
 S(g)=\sum_{x,i}\bigl[1-\tfrac12\operatorname{ReTr}
 (g_x^\dagger U_i g_{x+e_i} V_i^\dagger)\bigr],\qquad
 K_\beta(U,V)=\int e^{-\beta S(g)}\prod_x dg_x.
$$
A background-independent normalization cancels in all kernel ratios. Spatial plaquette factors lie outside this electric kernel. Sint derives the temporal-link integration by projecting the transfer onto gauge-invariant states, equations (3.5)–(3.9). His composition formula (3.10) explicitly integrates the intermediate spatial fields. That integral cannot be recovered by evaluating the kernel on constant boundary data alone. [Sint, *On the Schrödinger functional in QCD*](https://arxiv.org/pdf/hep-lat/9312079)

Represent each $g_x$ by a real unit quaternion, with inner product $\langle a,b\rangle=\operatorname{ReTr}(a^\dagger b)/2$. Write $R_iv=U_ivV_i^\dagger$ and $B_i=(R_i+R_i^T)/2$. Translation by one site is an involution on this cube, so the two orientations of each paired site sum cancel the skew part of $R_i$. For the orthonormal Walsh transform $\widehat g_k=8^{-1/2}\sum_x(-1)^{k\cdot x}g_x$, define
$$
 H_k=3I-\sum_i(-1)^{k_i}B_i,\qquad
 S=\sum_k\widehat g_k^T H_k\widehat g_k .
$$
Parseval gives $\sum_k|\widehat g_k|^2=8$. The least eigenvalue thus gives a lower bound $8\min_k\lambda_{\min}(H_k)$. A minimizing unit eigenvector $v$ gives the legal site rotations $g_x=(-1)^{k\cdot x}v$, attaining this bound even for noncommuting triples.

For commuting backgrounds choose $U_i=\exp(i C_i\sigma_3/4)$ and $V_i=\exp(i D_i\sigma_3/4)$, where $C,D$ give the full-cycle adjoint angles. In the two complex quaternion coordinates the symmetric part acts by $\cos((C_i-D_i)/4)$ and $\cos((C_i+D_i)/4)$. Minimization over $k$ gives
$$
 \min S=8\min_{\eta=\pm1}\sum_i\left[1-\left|\cos((C_i-\eta D_i)/4)\right|\right].
$$
The Weyl sign is common to all coordinates. For $C=(\pi,\pi,0)$ and $D=(\pi,-\pi,0)$ the minimum is eight. Choosing the sign independently in each coordinate would incorrectly give zero. For fixed boundaries, compactness and the positive Haar measure of each open neighborhood imply $-\beta^{-1}\log K_\beta\to\min S$.

## Integrating site rotations near a center

Set $S_0=S|_{U_i=V_i=I}$, $Z(t)=\int e^{-tS_0}$ and $M=\sum_i\|I-B_i\|$. For $U_i=\exp(i X_i\cdot\sigma/4)$ and $V_i=\exp(iY_i\cdot\sigma/4)$,
$$
 M\le \sum_i(|X_i|+|Y_i|)^2/32.
$$
Indeed $I-B_i=(I-R_i)^T(I-R_i)/2$ and the displacement operator norm of a rotation is at most the length of its generating path. Let $u=\widehat g_0/|\widehat g_0|$, defined off a Haar-null set, and put $A(u)=8u^T H_0u$. This is the exact action for eight identical rotations $u$. A pointwise comparison valid for every boundary triple is
$$
 |S-S_0-A(u)|\le M S_0 .
$$
To see it, the lost zero-mode norm is $8-|\widehat g_0|^2=\sum_{k\ne0}|\widehat g_k|^2$. The perturbation of each hard block has norm at most $M$, and $0\le u^TH_0u\le M$. Thus the error is at most $2M$ times the lost norm. The unperturbed hard eigenvalues are $2|k|_1\ge2$.

Under product Haar, $u$ is uniform on the unit three-sphere independently of $S_0$. Common left multiplication preserves $S_0$ and rotates $u$ transitively. Average over that multiplication to obtain the independence. Consequently, writing $F_\beta=\int_{SU(2)}e^{-\beta A(u)}du$, one has the finite-$\beta$ bounds for $M<1$
$$
 F_\beta Z(\beta(1+M))\ \le\ K_\beta(U,V)\ \le\ F_\beta Z(\beta(1-M)).
$$
For $M\le1/2$ and $\beta\ge1$, both rescaled $Z$ factors divided by $Z(\beta)$ equal $1+O(M)$ with an absolute constant on this fixed graph. Here are the details. Fix one site rotation by common left multiplication. $S_0$ is half the sum of squared neighbor differences, with its only minimum at seven identity rotations in this chart. Its Hessian there is the positive pinned graph Laplacian on three color components. Taylor expansion, a $t^{-1/2}$ rescaling in 21 real directions and Gaussian domination give $Z(t)\sim c t^{-21/2}$ with $c>0$. Compactness bounds the integral outside the chart exponentially. The inequality $x e^{-x}\le (2/e)e^{-x/2}$ now bounds $|t(\log Z)'(t)|$ by $(2/e)Z(t/2)/Z(t)$, uniformly for $t\ge1/2$. Integration in $\log t$ proves the ratio claim. In particular the $O_R(\beta^{-2/3})$ error in the opening statement is relative even when $F_\beta$ is very small.

One check of the rescaling is exact at finite coupling. Take $V_i=I$ and $|X_i|=t$ in all three directions. Then $B_i=\cos(t/4)I$, regardless of the three color axes, and
$$K_\beta=e^{-24\beta(1-\cos(t/4))} Z(\beta\cos(t/4)).$$

## A regular holonomy and the center give different local kernels

For commuting triples near zero put $A_-=8\sum_i(1-\cos((C_i-D_i)/4))$ and $A_+=8\sum_i(1-\cos((C_i+D_i)/4))$. The squared length of one complex component of a Haar unit quaternion is uniform on $[0,1]$. Hence
$$
 F_\beta=e^{-\beta\min(A_-,A_+)}
 \frac{1-e^{-\beta|A_+-A_-|}}{\beta|A_+-A_-|},
$$
with the last fraction equal to one at coincidence. For $C=c/\sqrt\beta$, $D=d/\sqrt\beta$ this gives
$$
 \lim_{\beta\to\infty}\frac{K_\beta(C,D)}{Z(\beta)}
 =e^{-(|c|^2+|d|^2)/4}
 \frac{\sinh(c\cdot d/2)}{c\cdot d/2}.
$$
For general color triples $X_i=c_i/\sqrt\beta$, $Y_i=d_i/\sqrt\beta$, Taylor expansion inside the compact orientation integral gives $\int_{SO(3)}\exp[-\tfrac14\sum_i|c_i-Rd_i|^2]dR$ with normalized Haar measure. The coefficient follows from the eight links per direction and the fundamental link angle $|X_i|/4$. On the larger slow scale the prefactor already matters on the diagonal: for fixed nonzero $c$ and $C=D=\beta^{-1/3}c$, $K_\beta(C,C)/Z(\beta)\sim\beta^{-1/3}/|c|^2$.

At a fixed regular commuting $C$ (at least one $C_i\notin 2\pi\mathbb Z$), the corresponding near-diagonal ratio is
$$
 K_\beta(C,C+\xi/\sqrt\beta)/K_\beta(C,C)\ \longrightarrow\ e^{-|\xi|^2/4}.
$$
At $D=C$ the only zero block components are the two real coordinates of the constant diagonal quaternion. All other eigenvalues have a strictly positive gap depending on $C$. For $D=C+\delta$ those same two components have eigenvalue $A_-/8$. Subtracting $A_-$ from the action shifts every block eigenvalue by $-A_-/8$. The two soft components still vanish and all remaining eigenvalues differ from their $D=C$ values by relative $O_C(|\delta|)$. The diagonal $D=C$ action vanishes on the circle of constant diagonal rotations and has positive normal Hessian: the quadratic form just described has that circle's tangent as its entire kernel on the product of tangent spaces. The same Laplace and logarithmic-derivative argument as above, now with 23 normal directions, shows the integrated residual changes by a factor $1+O_C(|\delta|)$. Finally $\beta A_-\to |\xi|^2/4$. This regular estimate loses uniformity when approaching a center. The global orientation integral supplies the missing limit there.

Van Baal and Koller retain the nine constant components in the small-volume Hamiltonian and separate the charged constant-mode contribution to the static potential. Here the electric calculation explains independently why the regular scalar Gaussian cannot be used uniformly in the central patch. To extract the neutral excitation one still needs both nonconstant spatial boundaries, their gauge quotient and the interaction with their fast state. [Van Baal and Koller, equations (4.1)–(4.6)](https://doi.org/10.1016/0003-4916(87)90032-7) · [A4’s frozen magnetic comparison](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/72d7cdb/yang-mills/observable-normalization/second-box/transverse-plaquettes/README.md)

## Checks

At 160 seeded pairs of non-Abelian background triples, direct temporal plaquette traces agreed with Fourier reconstruction to maximum absolute error $2.85\times10^{-14}$. The test evaluated the minimizing quaternion field in position space and checked the remainder inequality for every pair. It also checked the common-sign counterexample, three exact temperature rescalings and six global orientation integrals. These finite comparisons test the representation and normalizations. The asymptotic estimates above use the analytic bounds. [Run with NumPy and SciPy](check_kernel.py)

A root, child and grandchild each booted the measured PCP OS kernel at source revision `92623fa6759bbb4e4f27ce5aa381de213a55ae0c`. They checked 96 real-space hopping identities, the common Weyl witness and 11,375 instances of the hard-mode remainder bound. Each supervisor read back its child’s result after exit. All three desk nodes closed as Finished. Lean 4.19.0 checked the two emitted numerical declarations and the algebraic center-exponent identity. One invalid task and three corrupted Lean declarations were rejected. To replay, run `python verify.py --help` for the pinned worker inputs. [Native worker](worker.c) · [Recursive replay](verify.py) · [Checked declarations](FlatElectric.lean)
