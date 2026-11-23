# The thermodynamic pressure and large deviations of the Wilson action

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For the pure, isotropic four-dimensional fundamental SU(2) Wilson law with normalized Haar links, the program’s quantitative one-face estimate fixes the variation of the pressure under a change of coupling. It also fixes the cost of a macroscopic deviation of the **total** action, including correlations between faces. In units per site the rate is
$$
I(x)=x-c-c\log(x/c)\quad(x>0),\qquad c=9/2,
$$
and $I(x)=+\infty$ for $x\le0$. The proof below gives sufficient joint volume and coupling conditions, and a smaller-scale quadratic law.

## From the one-face estimate to pressure

Let $s_p=1-\tfrac12\mathrm{Tr}\,U_p$, $S_L=\sum_p s_p$ on an even periodic cube of side $L$, $V=L^4$, and $p_L(b)=V^{-1}\log\int e^{-bS_L}\prod_e dU_e$. There are $6V$ faces. A4’s filtered Ward comparison applies at second order, uniformly over even-periodic thermodynamic-limit states. For $F=\sqrt b\,\mathrm{Im}\,U_p$ in a common rooted frame, each color has second moment $1/2+O(b^{-1/8})$. The exact identity $2Y=|F|^2+Y^2/b$, with $Y=bs_p$ and the uniform action second moment, gives
$$
\sup_\mu|\mathbb E_\mu(bs_p)-3/4|\le C b^{-1/8}.
$$
This step uses the second-moment recursion, in addition to the quoted action covariance bound. The factor $3/4$ is half the sum over the three colors. [A4’s equation (4) and restoration of the single face](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/d8b59eba/yang-mills/observable-normalization/transfer-increments/local-action/README.md) · [Action moment bound](../pressure.md)

For clarity, the pressure limit has a direct surface estimate. Tile an $(mL)^4$ torus by $L^4$-site cubes and compare its action with a product of periodic $L$-box actions on **the same Haar variables**, assigning every positive link to its starting site and direction. For each face orientation at most $2L^3-L^2$ plaquette words per tile change: one of the two forward steps crosses its tile boundary. Each action changes by at most two. Consequently $|p_{mL}(b)-p_L(b)|\le24b/L$ for $b\ge0$. Comparison inside a common multiple yields a limit $p(b)$ and $|p_L(b)-p(b)|\le24b/L$.

The finite pressures are convex, differentiable and satisfy $p'_L(b)=-6\mathbb E_{L,b}s_p$ by symmetry. At every differentiability point of $p$, the two secant inequalities imply $p'_L(b)\to p'(b)$. Finite-volume measures have periodic-limit subsequences and $s_p$ is a bounded continuous cylinder. It follows that
$$
|b p'(b)+c|\le C b^{-1/8}
$$
almost everywhere at large $b$. The convex pressure is locally absolutely continuous. Integrating the error in $d b/b$ gives **a convergent additive constant** $C_W$ such that
$$
p(b)=-c\log b+C_W+O(b^{-1/8}).
$$
The argument gives an integrable thermodynamic representation of $C_W$ and leaves its numerical value undetermined. Chatterjee’s four-dimensional weak-coupling free-energy theorem treats $U(N)$ with its own action convention. Faria da Veiga and O’Carroll give Wilson stability bounds. Here the SU(2) remainder follows from the cited periodic-state moment estimate. [Chatterjee, Theorem 2.3](https://arxiv.org/pdf/1602.01222) · [Faria da Veiga and O’Carroll](https://arxiv.org/pdf/2205.07376)

## The macroscopic action law

Let $\beta\to\infty$ and $L\to\infty$ through even sides with $\beta/L\to0$. Define $X_L=\beta S_L/V$. At speed $V$ the exact log moment generating function per site is
$$
\Lambda_{\beta,L}(t)=p_L((1-t)\beta)-p_L(\beta).
$$
For $t$ in any compact subset of $(-\infty,1)$ the limit is $-c\log(1-t)$, with error $O_t(\beta^{-1/8}+\beta/L)$ uniform on that compact set. Here $C_W$ cancels. At $t=1$ the expression is $-p_L(\beta)\to+\infty$; monotonicity gives the same for $t>1$. These limiting functions also result by taking the volume limit first. The joint condition above is sufficient and comes from the seam comparison.

The limiting cumulant is differentiable on its open domain, diverges at its finite boundary, and its derivative ranges over $(0,\infty)$. A positive tilt below one gives exponential tightness. The Gärtner–Ellis theorem therefore gives the large-deviation upper bound on closed sets and lower bound on open sets with the good rate $I$ above. At $x>0$ the maximizing tilt is $1-c/x$, so a deviation to action density $x$ corresponds to the Wilson measure at coupling $\beta c/x$. For example, for $x>c$, $V^{-1}\log\Pr(X_L\ge x)\to-I(x)$; the corresponding lower-tail formula holds for $0<x<c$. The cumulant has the gamma form with shape $c$ per site. The proof uses the partition function of the full gauge law throughout. [Gärtner–Ellis hypotheses and conclusion, Theorem 4.2](https://warwick.ac.uk/fac/sci/maths/people/staff/stefan_adams/large-deviation-theory-ma4l3-notes.pdf)

## A smaller deviation window

Let $r=r_{\beta,L}\downarrow0$, with $\beta^{-1/8}=o(r)$, $\beta/L=o(r^2)$ and $Vr^2\to\infty$. For $Z=(X_L-c)/r$, the log moment generating function per unit speed $Vr^2$ is
$$
\frac{p_L((1-ur)\beta)-p_L(\beta)-urc}{r^2}.
$$
Integrating the derivative bound over this *short* interval gives $p((1-ur)\beta)-p(\beta)=-c\log(1-ur)+O_u(r\beta^{-1/8})$ for fixed real $u$. This factor $r$ matters; subtracting two independent pressure remainders would lose it. The finite-volume seam error is $O_u(\beta/L)$. Division by $r^2$ now gives $cu^2/2$. The limiting cumulant is finite and differentiable on all of $\mathbb R$, so the centered deviations have rate $z^2/(2c)=z^2/9$ at speed $Vr^2$. For example $L$ even of order $\beta^2$ and $r=\beta^{-1/16}$ satisfy all three conditions. The result describes bulk action fluctuations in these windows. Single physical-time correlations and a lower bound on the transfer gap require distinct information.

## Executed controls

Three recursively linked PCP OS guests enumerated torus seam incidences at seven tile sizes, checked all 4,096 binary cube link assignments at two tilted weights, and emitted the coefficient and quadratic-dual identities. The constrained cube has only even negative-face counts; its partition function keeps the closed-surface term. Lean accepted four declarations, and the verifier rejected a malformed request and three altered outputs. The SU(2) pressure and deviation conclusions are analytic consequences of the cited Ward input. [Worker](worker.c) · [Verifier](verify.py) · [Generated declarations](ActionDeviation.lean)
