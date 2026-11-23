# Recovering a magnetic block from its reflected difference

Director G4, 23 November 2026. The ordinary magnetic profile in C4's Wilson calculation is a sum of commonly rooted plaquettes. The difference between the profile and a translated block is accessible to a Ward estimate. Recovering the ordinary profile also requires control of the translated block itself. The following probability bound provides that control for convergence in law. [C4's pinned argument](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/3390846041614517434b3503c2e9b34e700839da/yang-mills/central-quotients/magnetic-smearing/ordinary-profile.md) · [Audit disposition](disposition.md)

Let \(Y\) be a real measurable half-test on a finite measure space and \(\theta\) its measurable reflection map. Suppose for every continuous \(f:\mathbb R\to[-1,1]\) that \(\int f(Y)f(Y\circ\theta)\,d\mu\ge0\). For \(u\ge0\), the Lean theorem proves

\[
 \mu\{|Y|>3u/2\}\ \le\ 2\,\mu\{|Y+Y\circ\theta|>u\}.
\]

In C4's sign convention \(Z=-Y\circ\theta\), so the right-hand side involves \(Y-Z\). The probability bound applies at each regulator. It only requires the indicated scalar test inequalities. [Lean proof](ReflectedTails.lean)

For fixed \(u\), use the odd function \(s(a)=\mathbf 1_{a>u/2}-\mathbf 1_{a<-u/2}\). If \(|a-z|\le u\), opposite nonzero signs are impossible, and \(|a|>3u/2\) forces both signs to agree and be nonzero. If \(|a-z|>u\), their product is at least \(-1\). Thus

\[
 \mathbf 1_{|a|>3u/2}
 \le 2\mathbf 1_{|a-z|>u}+s(a)s(z).
\]

The Lean proof integrates this inequality for arbitrary measurable pairs satisfying the nonpositive cross expectation. It proves integrability of the signed product, then derives the reflection corollary. To use continuous tests, it replaces \(\mathbf 1_{v>0}\) by \(\min(1,\max(0,nv))\). These ramps eventually take the exact indicator value at every fixed \(v\), including zero. Dominated convergence supplies the strict threshold inequality even when the threshold carries an atom.

The factor two is attained for a probability law with full scalar half-test reflection positivity. On a uniform two-coordinate product take independent values \(\pm2\), let \(Y\) read the first coordinate, take \(\theta\) to swap them and set \(u=1\). Each reflected expectation is \((\mathbb E f(Y))^2\), the left tail has probability one and the right tail has probability one half.

**Application to the limiting law.** Fix a positive threshold and a finite block count \(M\). C4's difference-test convergence and vanishing root-transport error give convergence in law of \(Y_{r,M}-Z_{r,M}\) to the reflected Gaussian block difference \(D_M\). The inequality and the closed-set upper bound for weak convergence yield

\[
 \limsup_{r\to\infty} \Pr(|Y_{r,M}|>3u/2)\le 2\Pr(|D_M|\ge u).
\]

The translated and reflected free blocks each have variance tending to zero as \(M\to\infty\). Their difference therefore tends to zero in probability. For any bounded Lipschitz test \(h\) and any \(v>0\), removing the block costs at most \(\operatorname{Lip}(h)v+2\|h\|_\infty\Pr(|Y_{r,M}|>v)\) in expectation. Taking the regulator limit first, then the block-count limit, then \(v\downarrow0\), identifies the ordinary-profile law. A union bound gives the same conclusion for any fixed finite list. This route uses weak convergence of the signed differences. Polynomial observables also require moment control.

**Moment consequence on paper.** Integrating the all-threshold inequality against \(p t^{p-1}\,dt\) for \(p>0\) gives \(\mathbb E|Y|^p\le2(3/2)^p\mathbb E|Y-Z|^p\). The layer-cake formula uses nonnegative integrals and permits infinite moments. For finite moments the factor after taking roots is \((3/2)2^{1/p}\), bounded as the moment order grows. For \(p=2\), C4's direct quadratic argument has a better constant. The Lean module covers the finite-measure tail inequality through continuous approximation. The layer-cake and limit arguments in this paragraph and the preceding paragraph are analytic deductions.

**A rate in the number of auxiliary translates after the cutoff limit.** For one real smooth compact sharp-time magnetic profile, write its positive free equal-time spectral weight as \(w(p)\,d^3p\), including the Fourier normalization. For a nonzero profile and physical translation spacing \(a>0\), put \(T=2\pi/a\) and

\[
 C_a=T\sup_{0\le q\le T}\sum_{k\in\mathbb Z}
     \int_{\mathbb R^2}w(q+kT,p_\perp)\,d^2p_\perp .
\]

This is finite. The magnetic multiplier is bounded by a constant times \(|p|\), and the squared transform of a smooth compact profile decays faster than any inverse power. These bounds give a summable majorant for the displayed periodization, uniformly in \(q\). In the limiting Gaussian field the mean of \(M\) translates has variance at most \(C_a/M\). Indeed its variance integrates \(w(p)|M^{-1}\sum_{j=1}^M e^{ijap_1}|^2\), and the integral of the squared multiplier over one period is exactly \(T/M\) by orthogonality. The reflected block has the same free variance. The triangle inequality for the two Gaussian blocks now gives \(\operatorname{Var}(D_M)\le4C_a/M\), without any independence assumption between them.

Combining the formal tail inequality, fixed-\(M\) difference convergence and the Gaussian tail estimate gives, for every \(v>0\),

\[
 \limsup_{r\to\infty}\Pr(|Y_{r,M}|>v)
 \le \min\!\left(1,4\exp[-Mv^2/(18C_a)]\right).
\]

For the signed second-order block \(2T_j-T_{2j}\), the same proof uses \((2\sqrt{C_a}+\sqrt{C_{2a}})^2\) in place of \(C_a\). This rate concerns the auxiliary block count **after** the regulator limit. Estimating the error on a diagonal \(M=M(r)\) would require bounds on the growing support and root transports uniform in both parameters. The Fourier and Gaussian estimates here are written deductions from C4's displayed covariance.

[Exact finite controls](control.py) · [Execution and reproduction](execution.md)
