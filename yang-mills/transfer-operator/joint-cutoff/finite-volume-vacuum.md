# An explicit time spacing for the vacuum without a known physical gap

For every finite periodic SU(2) spatial box in the [Wilson comparison](README.md), put $N=3L^3$, $B=6\lambda L^3$ and $s=2\kappa$. With physical time units fixed, its gauge-invariant Hamiltonian gap satisfies
$$
\Delta\ \ge d=\frac{e^{-sB}}{s\,2^N}.
$$
This lower bound can be very small. Its purpose is to choose an explicit time step that tracks the true vacuum, bounded correlations and the *relative* first gap along any specified sequence of finite boxes and couplings. At fixed nonzero $\kappa$ the displayed floor tends to zero as $L$ grows. A positive continuum mass gap remains open.

## Comparison of positive kernels

Use product Haar probability. On one link the heat kernel of $e^{-sH_{0,e}}$ at $s=2\kappa$ has the uniformly convergent central expansion
$$
p(u)=1+\sum_{n\ge1}(n+1)e^{-n(n+2)}\chi_n(u).
$$
The Peter–Weyl multiplicity and the trace of the unitary representation give the coefficient $n+1$ and $|\chi_n|\le n+1$. Since $(n+1)^2\le4^n$, $n(n+2)\ge3n$ and $e^3>16$, the absolute tail is at most $4/(e^3-4)<1/3$. Thus $2/3\le p\le4/3$. The product free kernel lies between $(2/3)^N$ and $(4/3)^N$. [SU(2) heat kernel, Lahoche and Oriti, equation (40)](https://pure.mpg.de/pubman/item/item_2178134_6/component/file_2178133/1506.08393.pdf)

For $0\le W\le B$, each multiplication by $e^{-sW/m}$ in a heat product of $m$ slices lies pointwise between $e^{-sB/m}$ and 1. Applying the positive free kernels successively and taking the Trotter limit yields $e^{-sB}e^{-sH_0}f\le e^{-sH}f\le e^{-sH_0}f$ for $f\ge0$. This order is pointwise on nonnegative functions. Equivalently the bounded potential multiplies each Brownian-bridge weight by a number in $[e^{-sB},1]$. For the continuous integral kernel $h$ of $e^{-sH}$ this gives
$$
m_0=e^{-sB}(2/3)^N\le h(x,y)\le M_0=(4/3)^N .
$$
Compactness of the group product and smoothness of the potential give the continuous heat kernel. All bounds here are for the full link space before restricting to gauge-invariant states. [Trotter and Feynman–Kac, Taylor, Chapter 11](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/chap11.pdf)

## Ground-state transform

Let $\Omega>0$ be the ground state. The normalized transition probability and a probability measure independent of its starting point are
$$
P(x,dy)=\frac{h(x,y)\Omega(y)\,dy}{\int h(x,z)\Omega(z)\,dz},\qquad
q(dy)=\frac{\Omega(y)\,dy}{\int\Omega(z)\,dz}.
$$
The two-sided kernel estimate implies $P(x,dy)\ge\varepsilon q(dy)$ with $\varepsilon=m_0/M_0=e^{-sB}2^{-N}$. After subtracting this common measure each row has mass $1-\varepsilon$. For a bounded real function $f$, the residual expectation lies between $(1-\varepsilon)\inf f$ and $(1-\varepsilon)\sup f$. Subtraction cancels the common integral. Therefore $\operatorname{osc}(Pf)\le(1-\varepsilon)\operatorname{osc}(f)$.

A real physical excited eigenfunction $\psi$ of energy $E_1$ gives $f=\psi/\Omega$, with $Pf=e^{-s\Delta}f$. Elliptic regularity makes both eigenfunctions continuous, and strict positivity on the compact link space bounds $f$. Orthogonality to $\Omega$ makes its oscillation nonzero. Thus $e^{-s\Delta}\le1-\varepsilon$ and $1-s\Delta\le e^{-s\Delta}$ gives $\Delta\ge\varepsilon/s$. The argument also bounds all nonconstant eigenmodes on the larger unrestricted space. The same oscillation estimate for two states with uniform invariant measure and off-diagonal transition probability $1/16$ is attained with $\varepsilon=1/8$ and nonconstant eigenvalue $7/8$. Deleting $\varepsilon$ from the lower bound would already fail in this example. [Lean finite-row estimate and oscillation inequality](JointCutoff.lean)

The Hamiltonian floor has a compact-group extension. On any compact connected group with a fixed bi-invariant metric, take the minimum $m_s>0$ and maximum $M_s$ of the one-link heat density of $e^{-sH_{0,e}}$ at a fixed $s>0$. Strict positivity and continuity on the compact group ensure both extrema exist. Tensorization and the same ground-state transform give $\Delta\ge e^{-sB}(m_s/M_s)^N/s$. This extension uses the Hamiltonian only. The Wilson time-spacing estimate below uses the all-label comparison proved for SU(2).

## A joint sequence in physical units

Index any sequence of finite boxes and finite positive $\kappa_n$, nonnegative $\lambda_n$ by $n\ge1$. Let $c_n=B_n+6/\kappa_n$, let $d_n$ be the explicit gap floor above, and fix a time unit $t_0>0$. One sufficient temporal spacing is
$$
a_n=\frac{t_0\,2^{-n-8}}{(1+t_0c_n)^2\,[1+(t_0d_n)^{-1}]} .
$$
Indeed $a_nc_n\le2^{-n-8}/4$ and $a_nc_n^2/d_n\le2^{-n-8}$. For the second inequality the ratio is the product of $2^{-n-8}$, $[t_0c_n/(1+t_0c_n)]^2$ and $1/(1+t_0d_n)$. These bounds imply the step and the vacuum separation hypotheses because $\rho_n\ge\Delta_n/(4c_n^2)$. If $\Delta_{a_n}$ denotes the normalized Wilson log gap, then
$$
\|P_{a_n}-P_n\|\le72\,2^{-n-8},\qquad
\frac{|\Delta_{a_n}-\Delta_n|}{\Delta_n}\le180\,2^{-n-8}.
$$
Also $a_n(1+t_0 c_n)^2\le t_0 2^{-n-8}$, so positive-time evolution converges in norm on the same pairwise comparison. Fixed lists of uniformly bounded insertions therefore have vanishing vacuum correlation error, even on trajectories where the Hamiltonian gap is shrinking at an unknown rate. A dyadic time step in units of $t_0$ is obtained by rounding this positive spacing down to the largest $t_0 2^{-k}$ below or equal to it. The same sufficient inequalities still apply. [Gap and vacuum estimates](README.md) · [Observable error](evolution.md)

The schedule compares the discrete and continuous times in each finite box. It carries any already established Hamiltonian correlation limit over to the Wilson sequence. The existence, Euclidean covariance and nontriviality of a spatial continuum limit, and a positive lower bound on its physical mass, require further estimates.
