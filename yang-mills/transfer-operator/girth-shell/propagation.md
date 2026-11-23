# Propagation after removing the measured first excitation energy

Work on periodic cubic space with $L\ge8$. Let $r_1=\lambda_1/\lambda_0$ be the true vacuum-normalized top excited eigenvalue, $u=I_2(\beta_t)/I_1(\beta_t)$, and $\eta=(\beta_s/4)^4$. Put $B=A-10I=C^*C-12I$ and $\Delta=J-6I$ on dual cubes. The following comparisons use the Euclidean $\ell^2$ norm on the face coefficients. Write $b=\beta_s$, $z=\beta_t/4$, $D=\|M\|_\infty^2/Z$, $\delta=O(Dz^2+D^2z^4)$. For $b,z>0$ sufficiently small, with $\delta$ small, the previous two proofs give
$$
 r_1/u^4=v(b)+10\eta+O(b^6+\delta).
$$
The local plaquette-to-vacuum overlaps are also controlled. Define $V_te_f=(I-P_t)\chi_f\Omega_t$ and $Ue_f=(I-P_w)\chi_f w$. The columnwise vacuum bound gives $\|V_t-U\|\le C\sqrt{3L^3}\,Dz^4$, since $\|\chi_f\|_\infty\le2$. The exact matrix of connected two-time plaquette correlations is $V_t^* S_c^k V_t$ for $k\ge1$.

As $b\to0$, $\Gamma=U^*U\to I$ uniformly. Thus $W=U\Gamma^{-1/2}$ is an isometry with $UU^*=W\Gamma W^*$ and $\|U-W\|=O(b^2)$. Assume $\sqrt{L^3}Dz^4=o(1)$ so the overlap norms stay bounded. Comparing contractions gives, uniformly at positive integer $k$,
$$
 \left\|\frac{V_t^* S_c^k V_t}{r_1^k}-e^{k\eta B}\right\|
 \le C\left[b^2+\sqrt{L^3}Dz^4+k(b^6+\delta)\right].
$$
Indeed $S_c/r_1$ is a contraction and differs from $We^{\eta B}W^*$ in norm by $O(b^6+\delta)$. The one-step estimate follows by dividing the shell approximation by $r_1/u^4$, expanding $\Gamma/(v+10\eta)=I+\eta B+O(b^6)$, and using $\|B\|\le12$. The correction from $v=1+O(b^2)$ is $O(b^6)$. Both comparison operators are contractions since $B\le0$. Telescoping their powers costs at most $k$ times their one-step difference, including on the orthogonal complement of the shell. Replacing $V_t$ by $W$ at the two ends incurs the displayed overlap error. The estimate controls all normalized linear combinations of the plaquettes at once. [Transfer and vacuum estimates](transfer.md) · [Uniform spatial expansion](spatial.md)

In particular at $k\eta\to\tau<\infty$ with $k\delta\to0$, the face correlation with its measured decay removed approaches $e^{\tau B}$. The component in $\ker C$ has amplitude $e^{-12\tau}$. A cube observable is the sum of its six incident traces divided by $\sqrt{12}$. The exact intertwining $CB=\Delta C$ gives its normalized correlation matrix to the same order as
$$
 C e^{k\eta B}C^*/12=e^{k\eta\Delta}(I+\Delta/12).
$$
Here $\|C\|=\sqrt{12}$. In particular the alternating cube sum on an even torus vanishes identically. For a unit Fourier test of cube sums at momentum $p$, write $\omega(p)=2\sum_j(1-\cos p_j)$. The limiting expression is $(1-\omega(p)/12)e^{-k\eta\omega(p)}$.

There is an explicit joint long-wavelength version. Take integer $n\to\infty$, $L=n^2$, $\beta_s=n^{-6}$, $\beta_t=n^{-14}$. For fixed $t>0$ choose $k$ nearest to $tn^2/\eta$. Then $D\le e^3$, $k=O(n^{26})$, $k(b^6+\delta)=O(n^{-2})$, and the overlap error vanishes. For a fixed real wave vector $q$, take an allowed $p$ nearest to $q/n$. Then $np\to q$, $n^2\omega(p)\to |q|^2$, and the Fourier reading divided by $r_1^k$ converges to $e^{-t|q|^2}$. Spatial sides in wavelength units tend to infinity. This construction uses unmodified Wilson plaquettes and an explicit subtraction of the lowest excitation energy by division. On this trajectory $-\log r_1=4\log(4/\beta_t)+o(1)$ in lattice units. The propagating envelope does not give a finite relativistic mass or an interacting continuum vacuum.
