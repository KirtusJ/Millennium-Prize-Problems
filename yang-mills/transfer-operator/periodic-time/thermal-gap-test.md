# Testing a vacuum energy floor with a periodic correlator

Director B4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

A finite-period measurement can disprove a proposed vacuum energy floor if the measured excess exceeds an independently bounded thermal contribution. Without such control, even the entire absolute two-point function at one period can agree across models with arbitrarily different vacuum gaps.

## Finite-regulator inequality

Let the Hamiltonian have a unique vacuum at energy zero, with $Z(T)=\operatorname{Tr}e^{-TH}<\infty$ at period $T$. Use a bounded self-adjoint slice observable $O$, its thermally connected periodic autocorrelation $C_T$, and lags $0<t\le T/4$. On a lattice use actual integer lags in the chosen time units. Put
$$
q=1-Z(T)^{-1},\quad D=\|O-\langle0|O|0\rangle I\|,\qquad
R_m=\frac{\cosh[(T/2-2t)m]}{\cosh[(T/2-t)m]},\quad m>0 .
$$
If every excited energy is at least $m$, then
$$
C_T(2t)-R_m C_T(t)\le(1-R_m)qD^2. \tag{1}
$$
A known spectral range $[a,b]$ of $O$ gives $D\le b-a$. An independent lower bound on the thermal purity $P=Z(2T)/Z(T)^2$ gives $q\le1-P$, since the largest probability of the Gibbs state is its vacuum probability and $\sum_i p_i^2\le\max_i p_i$. The purity is invariant under shifting the zero of energy. Use the same normalization on both sides of (1) if a reported correlator is rescaled. Correlated measurement errors and errors in the auxiliary bounds must be included before declaring a violation.

**Proof.** Shift the observable by its vacuum expectation, writing $A=O-O_{00}I$, so that $A_{00}=0$ and the connected covariance is unchanged. Write $C_T(s)=V(s)+B(s)$. In the thermal trace, $V$ consists of both orderings of transitions between the vacuum and an excited state. A transition of energy $E$ has kernel $e^{-sE}+e^{-(T-s)E}$. The ratio of that kernel at $2t$ and $t$ decreases with $E$: its logarithmic derivative is $a\tanh(aE)-b\tanh(bE)$ with $a=T/2-2t<b=T/2-t$. Thus $V(2t)\le R_m V(t)$ under the proposed floor. The thermal Lehmann representation and its periodic kernel are reviewed by Meyer in §4. [Meyer, QCD at non-zero temperature from the lattice](https://inspirehep.net/files/4def05e01580c6de78da1364c3df066d)

The remainder $B$ contains the excited-to-excited trace and subtraction of the squared thermal mean. Its time-independent diagonal contribution is the Gibbs variance of the diagonal entries $A_{ii}$, including the zero vacuum entry. Every off-diagonal excited pair has a nonnegative coefficient multiplying $\cosh[(T/2-s)|E_i-E_j|]$. Consequently $0\le B(2t)\le B(t)\le B(0)$. With $Q=I-|0\rangle\langle0|$, the uncentered excited trace at zero is $\sum_{i>0}p_i\|QA|i\rangle\|^2\le qD^2$. The mean subtraction can only decrease this bound. These positive sums converge by boundedness and finite thermal trace. Combining the bounds yields (1).

Even without assuming a gap, the vacuum-pair contribution at lag $t$ from $0<E<m$ is at least
$$
\max\left(0,\frac{C_T(2t)-R_m C_T(t)}{1-R_m}-qD^2\right).
$$
Indeed high-energy pairs satisfy the ratio bound above and each low-energy pair has ratio at most one. A diagonal reading equal to the excited-space projection has $D=1$, $C_T(t)=q(1-q)$ for every $t$ and $V=0$. This shows that a universal constant multiplying $qD^2$ in (1) cannot be reduced below one as $q\downarrow0$. At fixed regulator, $q\to0$ as $T\to\infty$ and $R_m\to e^{-tm}$ for fixed $t$. Along a refinement the product $qD^2$ needs its own bound, particularly for rescaled field insertions.

## Identical periodic data with different vacuum gaps

Fix one period $T$ and one frequency $\omega>0$. For each integer $n>1$, set $M=(\log n)/T$. Give a unique vacuum energy zero, $n$ states energy $M$ and $n$ states energy $M+\omega$. Let the observable exchange corresponding members of each excited pair with amplitude one and annihilate the vacuum. Its mean is zero and its norm is one. Since $ne^{-TM}=1$, the complete connected function is
$$
C_T(s)=\frac{e^{-s\omega}+e^{-(T-s)\omega}}{2+e^{-T\omega}},\qquad 0\le s\le T,
$$
independent of $n$, while the true vacuum gap $M$ grows without bound. A two-state system at energies $0,\omega$ has exactly this function when its transition amplitude squared is $(1+e^{-T\omega})/(2+e^{-T\omega})$. Here the reading couples directly to the vacuum. Both families obey the same observable norm upper bound. This finite-dimensional example isolates the missing information in a single thermal correlator. It makes no claim about realizability by a Wilson regulator.

For $T=4$, $t=1$, $\omega=\log 2$ the readings are $C_T(1)=10/33$, $C_T(2)=8/33$. At $M=\log 4$ the proposed floor is the exact gap, yet the observed ratio $4/5$ exceeds the vacuum-pair threshold $R_M=8/17$. The correction in (1) covers the excess with $q=17/33$. Thus exact data and mean subtraction alone would still permit a false rejection.

## Checks and application

Three host-dispatched PCP OS guests checked the following integer-arithmetic controls. For transfer eigenvalues $(1,1/2,1/4)$, period four and floor $\log 2$, all 729 symmetric three-by-three readings with independent entries in $\{-1,0,1\}$ satisfied (1) using the maximum absolute row sum of $O-O_{00}I$ for $D$. Some failed when the thermal allowance was set to zero. The other checks covered the five integer lags of the equal-correlator family for $M=\log k$, $2\le k\le12$, with multiplicity $k^4$, and the strict false rejection at $k=4$. The first replay ended early in the last guest. An unchanged replay returned three zero exits and matched the combined check text, SHA-256 `36d61cf4d03945550a54af94ce7acd2acdaf4f755d05a36a04e1eb4542287576`. These finite examples exercise the inequality; the general result follows from the trace argument.

A4’s frozen-ensemble determinants test distinct thermal transition frequencies. Applying (1) to those ensembles would additionally require a controlled thermal occupation bound, an observable normalization bound, and joint error control in the same units. No such ensemble-specific bound is established here. A continuum conclusion requires a common trajectory, physical units and control of the regulator limits. [A4’s periodic data analysis](../../observable-normalization/thermal-transitions/README.md) · [Replica purity in the electric regime](../../observable-normalization/replica-gap/electric.md)
