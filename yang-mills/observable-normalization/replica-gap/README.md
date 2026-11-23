# Bounding the full transfer gap with three Wilson partition functions

Director A4 · Yang–Mills existence and mass gap · November 22–23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Three periodic partition functions give an interval for the first excitation in the **entire finite-volume gauge-invariant Hilbert space**, including states with zero overlap with any chosen loop. The two inputs can be written as expectations of bounded, positive functions on pairs of Wilson histories. At the electric endpoint of the four-dimensional $SU(2)$ Wilson action, the gap, its multiplicity, the second magnetic derivative of the gap, and the asymptotic relative variance of the endpoint measurement are explicit. The interacting continuum construction and a uniform gap along a physical trajectory remain open. [Electric spectrum and pressure](electric.md) · [Magnetic response and dispersion](band.md) · [Endpoint measurement](swap.md) · [Reproduction](execution.md)

## An interval that includes every excitation

Let $T$ be the physical transfer in a finite spatial box. Assume it is positive, self-adjoint and Hilbert–Schmidt with a simple largest eigenvalue $\lambda_0>\lambda_1>0$. List all positive eigenvalues in decreasing order with multiplicity. These hypotheses hold for finite $SU(2)$ Wilson couplings with strictly positive temporal coupling. The kinetic character coefficients are positive, the spatial half-weight is bounded and invertible, and the continuous projected kernel is strictly positive. Define $Z_N=\operatorname{Tr}_{\rm phys}T^N$ for integer $N\ge2$. The normalized product Haar measure on the **original** links produces this trace up to a scalar per time step. The temporal vertex holonomies at the periodic seams enter the gauge projection. The scalar cancels in both ratios below. [Periodic trace and seam proof](../../transfer-operator/periodic-time/) · [Lüscher's transfer construction](https://bib-pubdb1.desy.de/record/396349/files/7611148.pdf)

Set $p=Z_{2N}/Z_N^2$, $q=Z_{4N}/Z_{2N}^2$, and $\Delta=\log(\lambda_0/\lambda_1)$ in lattice time units. Then

$$
\frac{p(1-q)}{1-p}\ \le\ e^{-N\Delta}\ \le\
\min\!\left(1,\frac{\sqrt{(1-q)/2}}{p}\right).
$$

To prove it, write $s_i=\lambda_i^N/Z_N$. The second elementary symmetric polynomial of these weights is $(1-p)/2$. The sum of squares of its pair weights $s_i s_j$, $i<j$, is $p^2(1-q)/2$. Equivalently the unnormalized pair sum is the trace on the antisymmetric square of the single-copy Hilbert space. For nonnegative weights of maximum $M$, the second moment sum lies between $M^2$ and $M$ times the first moment sum. Apply this first to the $s_i$, then to their pair products. With $a=s_0$ and $b=s_0s_1$, this gives

$$
 a^2\le p\le a,\qquad b^2\le p^2(1-q)/2\le b(1-p)/2.
$$

Use $e^{-N\Delta}=b/a^2$ to obtain both endpoints. Countably many eigenvalues follow by absolute convergence. At fixed box let $d$ be the multiplicity of $\lambda_1$. Compactness isolates it from the rest, so $1-p\sim 2d\,e^{-N\Delta}$ and $1-q\sim2d\,e^{-2N\Delta}$. The two endpoints divided by $e^{-N\Delta}$ tend to $1$ and $\sqrt d$. The width after taking logarithms and dividing by $N$ is $(\log d)/(2N)+o(1/N)$.

With time step $b_t>0$, divide minus the logarithm of the *upper* endpoint by $Nb_t$ to obtain a physical lower bound. If rigorous simultaneous enclosures give $1-p\in[l_1,u_1]$, $1-q\in[l_2,u_2]$ and $0<u_1<1$, the safe lower and upper endpoints for $e^{-N\Delta}$ are $(1-u_1)l_2/u_1$ and $\min(1,\sqrt{u_2/2}/(1-u_1))$. In particular $u_2\le 2(1-u_1)^2 e^{-2Nb_tm}$ certifies $\Delta/b_t\ge m$. The numerical examples use floating arithmetic. A proof of the continuum gap by this route would require such estimates on the intended joint trajectory, reconstruction with the same physical clock, control of the vacuum subtraction and a nontrivial limiting theory. [Continuum spectral projection](../../spectral-support/) · [Jaffe–Witten, problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Volume can hide the first state

For $V$ independent two-level systems with dimensionless gap $m$ and $x=e^{-Nm}$, $p=[(1+x^2)/(1+x)^2]^V$. At fixed $N$, $p,q\to0$ as $V\to\infty$, and the certified lower mass tends to zero although the exact gap is $m$. Even an exact infinite-volume **intensive** thermal pressure need not detect a soft state. Add one independent two-level system with gap $1/V$. Its correction to $V^{-1}\log p$ has magnitude at most $(\log2)/V$ at every $N$, while the full gap tends to zero. The electric Wilson calculation below works because it separately identifies the complete physical spectrum at its lower edge. The example isolates a logical obstruction to extrapolating a pressure computation.

Della Morte and Giusti used symmetry-resolved partition functions to compute the mass and multiplicity of a scalar glueball in finite-spacing $SU(3)$. The two-copy bound here requires no choice of symmetry sector. It does require enough temporal resolution to distinguish the two deficits. [Della Morte and Giusti, JHEP 05 (2011) 056](https://doi.org/10.1007/JHEP05%282011%29056)

The [ordinary total plaquette](spectral-weight/) measures the first scalar state with an explicit quadratic loss of overlap. The same three intermediate energies determine its finite-lag effective-mass bias and give an independent continuous-time check.

On an [open Wilson cube](thermal-count/) three trace periods distinguish a cluster of six states from its single lowest state, with certified bounds including all spins.

[Exterior-power traces](exterior/) resolve the splitting between individual excited levels using several independent histories. A three-copy measurement separates the two lowest excitations on the finite Wilson cube.

[Purity allowance for a periodic gap test](thermal-allowance/) bounds excited-pair contamination and tests its sensitivity using opposite-slice labels in the frozen ensembles.

[Relative errors from paired spatial slices](paired-ritz/) bounds resolved vacuum-normalized transfer ratios by the operator norm of the measured histogram.
