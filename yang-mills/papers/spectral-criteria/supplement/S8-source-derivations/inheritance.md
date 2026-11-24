# Refinement with an exceptional set of coarse fields

At one regulator let $S_t=e^{-tH}$ be the positive vacuum-normalized transfer, with $H\ge0$ self-adjoint on centered gauge-invariant slice functions. Put $P=\mathbb E[\cdot\mid\mathcal C]$ on this space, $Q=I-P$. For a coarse event $A$ let $R$ multiply by $\mathbf1_A$ on the **uncentered** space. Conditional expectation commutes with $R$. Thus $B=RQ$ is an orthogonal projection into centered functions with zero coarse mean, and $G=Q-B$ is the complementary good fine projection. Both restrict to the centered space.

Suppose for $a>0,\ t>0,\ 0<\tau\le t$ that
$$I-S_{2a}\succeq\gamma G,\qquad \|B S_\tau B\|\le\kappa,\qquad
\|P S_t P\|\le1-b,\qquad \gamma>0.$$
The first inequality must hold as a form on the entire centered space. A sufficient Wilson input is a conditional 24-colour inequality, uniform over the good coarse data, for every slice function. Indeed the expectation of the local losses on the good set controls $\|Gf\|^2$; all remaining local losses are nonnegative, and the two-endpoint argument bounds the physical loss from below. The [Wilson return estimate](return.md) supplies the second hypothesis for narrow plaquette gates, since the range of $B$ is contained in the range of $R$ and $S_\tau$ is positive. Then the fine contraction deficit obeys
$$d=1-\|S_t\|\ \ge\ \frac{(b-\kappa)_+}{1+2a/(\gamma t)}.$$

**Proof.** Let $\lambda=\inf\sigma(H)$ and $L>\lambda$. Take any unit $v$ in $E=\mathbf1_{[0,L]}(H)$. The short-time form gives $\gamma\|Gv\|^2\le1-e^{-2aL}$. By the spectral theorem $S_\tau\succeq e^{-\tau L}E$. Thus $e^{-\tau L}\|BE\|^2\le\|B S_\tau B\|\le\kappa$. Since $v$ lies in $E$, this bounds $\|Bv\|^2\le e^{\tau L}\kappa$. Also $S_t\succeq e^{-tL} E$. Testing on $Pv/\|Pv\|$ gives $1-b\ge e^{-tL}(1-\|Qv\|^2)$; this remains true when $Pv=0$. Combine the two orthogonal parts of $Qv$. With $x_L=e^{-tL}$ and $r=2a/t$,
$$b\le 1-x_L +x_L(1-x_L^r)/\gamma+e^{-(t-\tau)L}\kappa.$$
The last factor is at most one. Let $L\downarrow\lambda$ and use $x(1-x^r)\le r(1-x)$ for $x\in[0,1]$. This proves the claim without an eigenvector at the spectral endpoint. [Ungated inequality](../full-complement/inheritance.md)

**Accumulation.** Write $K_i=1+2a_i/(\gamma_i t)$ and $M_i=\prod_{j=1}^iK_j$ with $M_0=1$. If the actual coarse comparison gives $b_i\ge d_{i-1}-\varepsilon_i$, then
$$d_n\ge M_n^{-1}\Big(d_0-\sum_{i=1}^n M_{i-1}(\varepsilon_i+\kappa_i)\Big)_+.$$
Sufficient conditions for positive limiting deficit are $\sum_i a_i/\gamma_i<\infty$ and total weighted losses strictly below $d_0$. At a fixed physical time choose a positive lattice lag $\tau_i\le t$, for example one step once $a_i\le t$. A summable Wilson gate cost can be made small by narrowing the gates. That choice also changes the good-field mixing obligation.

**Why event probability alone is insufficient.** Consider the stationary reversible reset process $S_t=e^{-\ell t}I+(1-e^{-\ell t})\mathbb E$ with $\ell>0$. Give a coarse event arbitrarily small positive mass and at least two equiprobable fine labels there. The signed difference between the labels has zero coarse mean, lives on the event and retains the fraction $e^{-\ell t}$ of its correlation. Hence $\|B S_t B\|=e^{-\ell t}$ regardless of the stationary rarity. The Wilson one-link estimate uses the conditional chance of returning at a different time. No return estimate for an arbitrary coarse event follows from its marginal size alone.

The current four-dimensional fixed-orbit measurements concern local updates. A small local quotient on a frustrated orbit can obstruct uniform local mixing while the physical process leaves a sufficiently small surrounding gate rapidly. The unresolved mathematical targets are a useful lower bound on $G$ outside specified gates and the independently controlled inherited compression at the same physical time. [Fixed-orbit results](../full-complement/fixed.md) · [Finite-state controls](checks.py)
