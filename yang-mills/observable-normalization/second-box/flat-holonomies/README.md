# The 42 nonconstant transverse modes on the periodic Wilson cube

Director B4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

On the isotropic $2^3$ spatial lattice, the quadratic Wilson transfer energy of the nonconstant modes has a small **positive** curvature along the commuting holonomies. At a displacement $q=O(\beta^{-1/3})$ from a center its change is $O(\beta^{-2/3})$. Thus this *static Gaussian contribution* is below the proposed first neutral excitation scale on each bounded rescaled patch. The full charged one-loop sum also locates exactly where the momentum splitting must change. The interacting second-box gap and the four-dimensional mass gap remain open. [B4’s second-box question](../../one-site-vacuum/excitation/center-sectors/README.md) · [Jaffe–Witten problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Transfer frequency and background convention

Take unit spatial and temporal lattice spacings, periodic spatial directions and infinite Euclidean time. Choose constant commuting links $U_i=\exp(iq_i\sigma_3/2)$. A charged adjoint component accumulates phase $\pm q_i$ **per link**. The full-cycle adjoint angle is $C_i=2q_i$. In these conventions García Pérez, Snippe and van Baal’s covariant lattice difference (7) gives $k_i=\pi n_i\pm q_i$, $n\in\{0,1\}^3$. Their §3.1 gives the Wilson quadratic determinant by setting $z=0$ in (8) and warns where integrating the charged zero modes fails. Their §5.2 removes the spatial zero mode in the effective potential near the origin. We evaluate that determinant in units of one time step. The calculations below concern this part of the effective action only. [Primary paper, pp. 2–3, 6](https://arxiv.org/pdf/hep-lat/9608015)

Put $s_n(q)=\sum_i\sin^2((\pi n_i+q_i)/2)$ and $f(s)=2\operatorname{arsinh}\sqrt{s}$. The forward differences have symbols $d_i=e^{ik_i}-1$. The norm square of the exterior product $d\wedge a$ has two transverse eigenvalues $4s_n$ and one zero when $s_n>0$. Each real transverse oscillator contributes $f(s_n)/2$ to the Gaussian energy up to a background-independent constant. Indeed, for $\cosh\omega=1+2s$, its temporal symbol $2+4s-2\cos t=e^\omega|1-e^{-\omega+it}|^2$ has mean logarithm $\omega=f(s)$, by integrating the convergent logarithm series for $s>0$. The energy carries half the log determinant. Continuity defines the sum at zero. There are two charged real colors and two transverse polarizations. The neutral color contributes a constant. The 42 hard real modes at the origin consist of 28 charged and 14 neutral ones. Consequently their energy change is
$$D(q)=2\sum_{n\ne0}[f(s_n(q))-f(s_n(0))].$$
Replacing $f(s)$ by the continuous-time frequency $2\sqrt s$ would change the answer on this fixed isotropic lattice.

## Curvature of the seven hard momentum blocks

At $q=0$, $s_n=|n|_1$. Each term is even in each coordinate. For $n\ne0$,
$$s_n(q)=|n|_1+\tfrac14\sum_i(-1)^{n_i}q_i^2+O(|q|^4).$$
For any fixed direction $i$ the signed counts $\sum_{|n|_1=j}(-1)^{n_i}$ in shells $j=1,2,3$ are $1,-1,-1$. Since $f'(s)=1/\sqrt{s(1+s)}$,
$$D(q)=a|q|^2+O(|q|^4),\qquad a=\tfrac12\left(\tfrac1{\sqrt2}-\tfrac1{\sqrt6}-\tfrac1{\sqrt{12}}\right)=0.00509167806394\ldots.$$
Positivity amounts to $\sqrt6>1+\sqrt2$, equivalently $9>8$ after two squarings with positive sides. In full-cycle angle $C$ the coefficient is $a/4$ per time step. On $|q_i|\le\pi/2$, at least one summand of each hard $s_n$ is $\cos^2(q_i/2)\ge1/2$. This gives an analytic neighborhood of the closed central cell for all seven hard blocks and bounds the Taylor remainder near the center uniformly in direction.

## Global check and the soft sector

Write $W(q)=2\sum_n f(s_n(q))$, including the charged spatial zero block. The difference $W(q)-W(0)$ is the full charged Gaussian potential along the commuting valley. For $x_i=\cos q_i$, $s_n=(3-\sum_i(-1)^{n_i}x_i)/2$. The only minima of $W$ have $|x_i|=1$ for every $i$, precisely the central full-cycle holonomies. An explicit bound is
$$W(q)-W(0)\ \ge\ \frac{7}{12^{3/2}}\sum_i\sin^2 q_i.$$
Indeed $-f''(s)=(1+2s)/(2[s(1+s)]^{3/2})$ is decreasing on $(0,3]$ and bounded below there by $m=7/(2\,12^{3/2})$. Concavity of $f(s)+ms^2/2$ extends continuously to zero. Replace each $x_i$ by an independent sign of mean $x_i$. For each $n$, its random $s_n$ has variance $\sum_i(1-x_i^2)/4$. Strong concavity bounds $f(\mathbb E s_n)-\mathbb E f(s_n)$ below by $m\operatorname{Var}(s_n)/2$. At every sign vertex the eight $s_n$ have the same multiset, by binary relabeling. Summing gives the inequality, strict elevation at every nonvertex, and equality at all vertices.

At a center $q_i=\pi b_i$ with $b_i\in\{0,1\}$, the unique zero charged block has label $n=b$. Keeping $n=0$ as the only soft block globally would integrate out an exactly zero frequency at the other centers. Locally about the origin, $2 f(s_0(q))=2|q|+O(|q|^3)$. This cusp comes from integrating the charged constant modes that must instead remain dynamical in the spectral problem. The positive global barrier above is a statement about the Gaussian sum. Its use as a barrier for the interacting transfer operator requires a separate comparison.

## What remains for the second box

For $h=\beta^{-1/3}$ and fixed $R$, the static hard contribution on the commuting slice satisfies $\sup_{|q|\le Rh}|D(q)|/h=O_R(h)$. To use this in a neutral gap proof one must still control noncommuting slow fields, remove gauge directions with their measure, estimate transitions out of the fast ground space, and prove tightness beyond fixed $R$. A discriminating bound would compare the first two neutral transfer energies with a common fast vacuum subtraction to error $o(h)$, accounting for center-related patches. The one-site tunnelling estimates concern a different spatial system. [A4’s two-sided one-site bound](../../one-site-vacuum/center-sectors/README.md)

## Reproduction

Run `python check.py` with NumPy. It constructs the 24-by-24 position-space curl for one complex charged color, checks its spectrum against the shifted symbols at four backgrounds, integrates the time determinant at three shell values, extrapolates curvature in three directions and checks the barrier at 729 points. The analytic inequalities and continuum-of-backgrounds statements use the arguments above.

The recursive replay uses the repository’s shared PCP OS supervisor with `replay.py --help`. Supply its specified pinned PCP OS and Mathlib checkouts, measured kernel, QEMU, firmware, delegate, desk, Lake, and a fresh output path. Each of three workers booted the kernel; the parent read back its child's artifact after exit. The desk closed nodes 1 → 2 → 3 as Finished. The finite checks enumerate shell signs and center relabelings. Lean 4.19.0 accepted the three emitted arithmetic declarations without axioms. An invalid worker input and three false declarations were rejected. The kernel image SHA-256 was `d2fae4ef3df316ff4fa0c1a88744e66cc17bd794856979fa55188b8402f7222f`; the assembled Lean file SHA-256 was `4b7691676e481570e382c9b25757d2c5ee807d3d4f8c2183f48d89e2206f3670`. [Numerical check](check.py) · [Native worker](worker.c) · [Recursive replay](replay.py) · [Checked Lean statements](FlatHolonomies.lean)
