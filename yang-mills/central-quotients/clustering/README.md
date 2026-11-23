# Testing a mass gap with spatial correlations

Director C4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A mass threshold makes a quantitative prediction about two separated observables. This note gives the prediction and an inverse test that measures how much spectral weight a violation forces below the threshold. Both work at finite regulator. Applied to the three-dimensional spatial $SU(2)$ Wilson Hamiltonian, the test also gives an unconditional spacetime clustering bound for arbitrary bounded local physical operators in B4's small-magnetic-coupling interval. The physical mass and the existence of a nontrivial continuum theory on the weak bare-coupling trajectory remain open. [Yang–Mills problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## The inverse test at equal time

Let $Q\ge0$ be the Hamiltonian above the vacuum, $\Omega$ a normalized ground state, and $P_0$ its entire zero-energy projection. Take bounded self-adjoint $A,B$, and set $a=(1-P_0)A\Omega$, $b=(1-P_0)B\Omega$. Write $E_Q$ for the spectral projections and
$$
 C(s)=\operatorname{Re}\langle a,e^{-sQ}b\rangle,\quad
 V=\|a\|\|b\|,\quad W_A(m)=\|E_Q((0,m))a\|^2 .
$$
Define $W_B$ with $b$. If the vacuum is unique, $C(0)$ is the real connected equal-time correlation. The matrix elements measured below are real symmetrizations. For real multiplication probes and a real transfer vacuum the Euclidean correlation itself is real.

For a candidate threshold $m>0$, choose an observation time $T>0$ and set $q=e^{-mT}$. Let $\mathcal E_0$ be the computable commutator error in the [filter theorem](filter.md). Then
$$
 |C(0)|\le\mathcal E_0+\sqrt{W_A(m)W_B(m)}
       +q\sqrt{(\|a\|^2-W_A(m))(\|b\|^2-W_B(m))}.
$$
In particular, two translates of the same local observable in a translation-invariant vacuum have identical spectral masses. If $V>0$, their fraction below $m$ satisfies
$$
 \boxed{\quad \frac{W_A(m)}{V}\ \ge\
  \max\!\left(0,\frac{|C(0)|/V-\mathcal E_0/V-q}{1-q}\right).\quad}
$$
An energy exactly equal to $m$ belongs to the high interval. The connected projection removes a degenerate vacuum before the test. If $A,B$ commute throughout $|t|<T$ under relative time evolution, $\mathcal E_0=0$. For lattice loops, the previously proved propagation bound gives an explicit error at every spatial cutoff. [Compact-link propagation theorem](../locality/) · [Exact two-spin test](controls.md)

## The forward prediction in space and Euclidean time

Suppose the real cross spectral measure $\operatorname{Re}\langle a,E_Q(dE)b\rangle$ vanishes on $(0,m)$. A full gap of at least $m$ suffices. Suppose the larger of the two commutator norms in the two probe orders on $0<t<T$ is bounded by $D t^p e^{-d+ht}$ with $p\ge1$, $h\ge0$, $d>0$. Put
$$
 T=\frac{d}{\sqrt{h^2+m^2}},\qquad
 c_p=\frac1\pi\int_0^{\pi/2}\sin^{p-1}\theta\,d\theta.
$$
Here the commutator estimate must hold up to this value of $T$. For every Euclidean separation $s\ge0$,
$$
 \boxed{\quad |C(s)|\le (V+c_p D T^p)
   \exp\!\left[-\sqrt{(ms)^2+\frac{m^2d^2}{h^2+m^2}}\right].\quad}
$$
This applies without Lorentz covariance. With exact commutation for $|t|<T$ the result is $|C(s)|\le V\exp[-m\sqrt{s^2+T^2}]$. Thus in a limiting theory with speed at most $v$, translated fixed probes of separation $r$ obey $|C(0)|\le V e^{-mr/v}$ whenever they have no cross weight below $m$. A spatial decay exponent $\gamma=\liminf_{r\to\infty} -r^{-1}\log(|C(0;r)|/V)$ can consequently give an **upper** threshold $v\gamma$ for the probe's positive-energy spectral infimum. Use a nonzero channel and a sequence of translated probes with bounded fixed variance. A spatial upper bound alone does not establish a lower mass gap. Classical precedents are Fredenhagen's relativistic cluster theorem and the Lieb–Robinson exponential clustering theorem of Nachtergaele and Sims. [Fredenhagen (1985)](https://doi.org/10.1007/BF01213409) · [Nachtergaele and Sims (2006)](https://arxiv.org/abs/math-ph/0506030)

In the interacting $SU(2)$ interval $\beta^2\le1/384$, the resulting uniform bound on the Hamiltonian has exponent at least $\sqrt{(6s/b_{\rm lat})^2+[0.7(R-2)]^2}$ for separation $R>2$ in units of spatial mesh $b_{\rm lat}$. It covers all bounded local gauge-invariant operators, including electric spectral projections of arbitrary cutoff. At small $\beta$ the guaranteed spatial rate improves to $2\log(1/\beta)-\log\log(1/\beta)+O(1)$ per lattice spacing. [Constants, prefactors and limits](strong-coupling.md)

Three strictly positive Euclidean readings also give a test for a **finite band separated from zero**. Its Wilson version uses actual integer transfer steps, with explicit time-rounding and real-time comparison errors. A free-field control gives a certified nonzero lower bound on the mass in that band from three separated readings. [Positive-time band and Wilson history](three-readings.md) · [Free-field control](controls.md) · [PCP execution and formal coverage](execution.md)
