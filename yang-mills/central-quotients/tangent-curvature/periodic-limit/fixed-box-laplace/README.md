# Independent review of the fixed-box SU(2) Laplace limit

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Disposition.** Z4’s Theorem L3 at revision three passes independent review for each fixed box and uniformly bounded rescaled shell. This includes total variation of the entire conditional density. The signed first correction below shows that the error is generally of order $\beta^{-1/2}$, even with the shell fixed to identity. The smallest box misses this term. The review ends at L3; the infinite-volume identification of the joint curvature field and continuum reconstruction involve further arguments. [Reviewed theorem and proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/dcdc744/yang-mills/z4/attempt/paper/sec_proof.tex#L270)

## Conditional law and domination

Write $h=\beta^{-1/2}$, $\varphi$ for the rescaled interior coordinates remaining after fixing the time forest, and $\psi$ for the rooted shell coordinates, with $|\psi|\le M$. Only plaquettes touching the integrated links enter their conditional Wilson density. The exterior first determines a rooted shell gauge. With the shell held fixed, condition on the interior tree links inside the integral. For tree-based gauge transforms the remaining Haar factors are invariant under the resulting left and right multiplications. The conditional expectation of any rooted-gauge-invariant test is thus computed with tree links set to identity. The change of variables on each remaining group link has density proportional to $h^3\,\mathrm{sinc}^2(h|\varphi_l|)$ on $h|\varphi_l|<\pi$. The chart omits one Haar-null group element per free link. In the manuscript’s outline and “The gauge” paragraph, *the interior forest uses no interior information* should say that the shell gauge is exterior-measurable and the interior forest is eliminated **inside** the conditional integral.

Let $U_h=h^{-2}S_R(h\varphi;h\psi)$ and $U_0=\|d\varphi+d\psi\|^2/2$. With the shell and forest at identity, zero action implies a flat connection on the box. Every flat connection there is pure gauge by path independence under elementary square moves. The connected shell fixes a common frame, and each time tree fixes that frame down to its interior sites. Thus the only minimizer is the identity. The same argument in the additive group makes $Q=d_{\rm int}^*d_{\rm int}$ strictly positive on free links.

I checked the manuscript’s constants. For link angles bounded by $\delta$ the face remainder in its linear matrix expansion gives
$$
U_h\ge \tfrac14\|d\varphi+d\psi\|^2-48\delta^2e^{8\delta}(|\varphi|^2+|\psi|^2).
$$
The factor 48 uses four edges per face and at most six faces per edge. Also $\|d\psi\|^2\le24|\psi|^2$. Choosing $48\delta^2e^{8\delta}\le\min(1,\lambda_{\min}(Q)/16)$ gives $U_h\ge\lambda_{\min}(Q)|\varphi|^2/16-7M^2$. Away from this neighborhood the trivial-shell action has a positive minimum $\eta$ by compactness. Inserting the bounded rescaled shell changes the action by at most $6h\sqrt{\nu_s}M$, where $\nu_s$ counts free shell links. For sufficiently small $h$, $U_h\ge\eta/(2h^2)\ge\eta|\varphi|^2/(2\nu_R\pi^2)$ throughout the far part of the chart, where $\nu_R$ counts free interior links. These bounds dominate the unnormalized chart density by a single integrable Gaussian for the fixed $R,M$. The limiting Gaussian has precision $Q$ on each color and mean $-Q^{-1}d_{\rm int}^*d_{\rm shell}\psi$. Its normalization is positive and continuous on the compact shell ball, hence bounded away from zero. Local uniform Taylor convergence, Gaussian tails and division by the normalizations give the asserted uniform total variation and tail bound.

## The first correction in total variation

Let $p_h,p_0$ be the normalized chart and Gaussian densities on the same real vector space; extend $p_h$ by zero outside the chart. For each face, let $v_1,\ldots,v_4$ be the four **oriented**, unscaled vectors, read in loop order from the combined coordinates $(\varphi,\psi)$ with forest entries zero. In the usual Pauli convention define
$$
C(\varphi,\psi)=-\sum_{p\in P_R}\ \sum_{1\le i<j<k\le4}\det(v_i,v_j,v_k),\qquad
\bar C_\psi=\int C(\varphi,\psi)p_0(\varphi\mid\psi)\,d\varphi.
$$
For each fixed polynomial weight degree $d\ge0$ there is a finite $A(R,M,d)$ such that, for all sufficiently small $h$,
$$
\sup_{|\psi|\le M}\int(1+|\varphi|)^d
\left|p_h(\varphi\mid\psi)-p_0(\varphi\mid\psi)
       [1-h(C(\varphi,\psi)-\bar C_\psi)]\right|\,d\varphi
\le A(R,M,d)h^2.
$$
The bracket is a signed approximation. It need not be positive in the far tails. Multidimensional Laplace expansions with a nondegenerate minimum are classical. Here the explicit coefficient, boundary uniformity and weighted density error follow directly for this Wilson kernel. [Kirwin, *Higher Asymptotics of Laplace’s Approximation*](https://arxiv.org/abs/0810.1700) · [Chatterjee, weak-coupling Wilson free energy](https://arxiv.org/abs/1602.01222)

**Proof.** For the half trace of the ordered product $\prod_j\exp(ih\sigma\cdot v_j)$, the $m$th derivative on the real axis has modulus at most $s_p^m$, $s_p=\sum_j|v_j|$. Apply Leibniz, use unitarity of each exponential, and sum the multinomial coefficients. The quadratic action coefficient is $|\sum_jv_j|^2/2$. In the cubic half trace the terms with repeated indices are traceless, while three distinct indices contribute $+\det(v_i,v_j,v_k)$ from $\mathrm{Tr}[(i\sigma\cdot v_i)(i\sigma\cdot v_j)(i\sigma\cdot v_k)]/2$. Subtraction from one accounts for the sign in $C$. Taylor’s theorem gives globally for the action
$$
|U_h-U_0|\le h\sum_p s_p^3/6,\qquad
|U_h-U_0-hC|\le h^2\sum_p s_p^4/24.
$$
For real $A,B$, Taylor’s integral remainder bounds $|e^{-B}-e^{-A}+e^{-A}(B-A)|$ by $(B-A)^2\max(e^{-A},e^{-B})/2$. On the chart both exponentials have the Gaussian domination established above. In addition $0\le1-\prod_l\mathrm{sinc}^2(h|\varphi_l|)\le h^2|\varphi|^2/3$, by $|\sin x-x|\le |x|^3/6$ and $|\mathrm{sinc}(x)|\le1$. The error in the unnormalized density expansion is therefore bounded in each weighted integral by $O_{R,M,d}(h^2)$. Outside the chart the omitted limiting Gaussian times a polynomial has exponentially small integral in $1/h^2$. Integrating first with weight one gives the normalizing ratio $1-h\bar C_\psi+O(h^2)$. The uniform lower bound on the Gaussian normalization and its uniformly bounded polynomial moments justify division and give the displayed result.

## What the smallest-box check cannot see

At identity shell $C$ is odd and $\bar C_0=0$. Every even chart test of magnitude at most $(1+|\varphi|)^d$ consequently has expectation error $O_{R,d}(\beta^{-1})$. For $R=[-1,1]^4$ this rate holds for *all* such tests: every free link touches the unique interior vertex, and a face has at most two such edges. The triple determinant vanishes identically.

For $R=[-N,N]^4$, $N\ge2$, choose a spatial $12$ face at the origin with all four vertices interior. Give its first three oriented edges the three standard color basis vectors and set all other coordinates to zero. Its edges are free of the time forest. No other face contains these same three edges, so $C=-1$ on this assignment. As a nonzero polynomial it has positive absolute expectation under the nondegenerate Gaussian. The expansion then gives the sharp asymptotic
$$
\|K_\beta(\cdot\mid0)-K_\infty(\cdot\mid0)\|_{\rm TV}
=\tfrac12\beta^{-1/2}\mathbb E_0|C|+O_R(\beta^{-1}).
$$
This concerns the full chart law on a fixed box. A bound uniform over growing boxes, shells of diverging norm or measurements at fixed physical separation would require new estimates.

## Executed checks

Three linked PCP OS guests checked the signed cubic trace on all 2,401 four-letter words from the zero vector and six signed axes, then enumerated all 2,616 plaquettes in the two smallest boxes. They checked the radius-one obstruction and the unique active triple of the radius-two witness. Four Lean declarations passed. The verifier rejected a malformed worker request and three altered outputs. The Gaussian estimates and the uniform density expansion are analytic arguments. A separate complex-matrix calculation for the witness face gave $(U_h-3/2)/h=-1.08226,-1.04247,-1.02156,-1.01086$ for $h=0.1,0.05,0.025,0.0125$, respectively. [Native worker](worker.c) · [Verifier](verify.py) · [Generated declarations](BoxLaplace.lean)
