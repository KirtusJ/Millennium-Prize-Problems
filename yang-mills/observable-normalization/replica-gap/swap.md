# A bounded endpoint measurement and its relative variance

Use the real symmetric, gauge-averaged half-period kernel $K_n(x,u)$ of $T^n$. It includes the two spatial half-weights and all intermediate temporal integrations. Take two independent ordinary histories of period $N=2n$, recording the spatial slices $(x,u)$ and $(y,v)$ separated by $n$ steps. With respect to product Haar the four endpoints have density $A^2/Z_{2n}^2$, where

$$
 A=K_n(x,u)K_n(y,v),\qquad B=K_n(x,v)K_n(y,u).
$$

Switching $u,v$ exchanges $A,B$. Both squared integrals are $Z_{2n}^2$. Contraction around the single four-slab cycle gives $\int AB=Z_{4n}$. The exchange-invariant reading

$$
 H=\frac{(A-B)^2}{A^2+B^2}
 =1-\operatorname{sech}(\log A-\log B)
$$

lies in $[0,1]$ (use zero at $A=B=0$; the Wilson kernels here are strictly positive). Its expectation is exactly $1-Z_{4n}/Z_{2n}^2$. Indeed the exchange lets us replace its weight $A^2$ by $(A^2+B^2)/2$, leaving $\tfrac12\int(A-B)^2$. Repeat with period $4n$ for the second deficit. For small $s=|\log A-\log B|$, the equivalent reading $(1-e^{-s})^2/(1+e^{-2s})$ permits stable evaluation via expm1. Given an absolute error bound $\epsilon$ on the log ratio, use the increasing function $1-\operatorname{sech}s$ at $\max(0,s-\epsilon)$ and $s+\epsilon$ to enclose the reading. Unbiased estimates of the individual kernels need separate error analysis before insertion into this nonlinear expression.

For mean $\delta$, boundedness gives $\operatorname{Var}H\le\delta(1-\delta)$. There is a stronger low-temperature result at each fixed box. Normalize $\lambda_0=1$ and put $r=\lambda_1$. Choose a real orthonormal first multiplet $\psi_i$, $1\le i\le d$, and a positive normalized vacuum $\psi_0$. The kernels are continuous on the compact link space, and $\inf\psi_0>0$. Uniformly in $x,u$,

$$
 K_n(x,u)=\psi_0(x)\psi_0(u)+r^n\sum_{i=1}^d\psi_i(x)\psi_i(u)+o(r^n).
$$

In fact factor off one kernel at each end of the spectral remainder. Its supremum is bounded by $\sup_x\|K_1(x,\cdot)\|_2^2$ times the next spectral radius to power $n-2$. Put $F_i=\psi_i/\psi_0$ and sample four independent slices from $\psi_0^2\,dx$. Define

$$
 J=\sum_i [F_i(x)-F_i(y)][F_i(u)-F_i(v)].
$$

Under this limiting law $\mathbb E J^2=4d$ by orthonormality and zero means. Uniform expansion gives $H/r^{2n}\to J^2/2$ as a function of the endpoints. Their finite-period density also converges uniformly to the product vacuum density. Hence

$$
 \lim_{n\to\infty}\frac{\operatorname{Var} H}{(\mathbb E H)^2}
 =\frac{\mathbb E J^4}{16d^2}-1 .
$$

Thus an exact endpoint measurement at fixed box has bounded relative variance even when its mean is exponentially small. The cost of integrating the conditional kernels to the required precision remains open. Swap techniques for quantum Rényi entropies have an extensive history. Hastings et al. measured a ground-state subregion swap. Here a full thermal trace and gauge-projected slabs enter. [Hastings et al., Phys. Rev. Lett. 104, 157201](https://doi.org/10.1103/PhysRevLett.104.157201)

## An explicit SU(2) variance

At zero spatial coupling on a cubic torus of side $L\ge5$, the slice vacuum is product Haar and the first multiplet consists of all $d=3L^3$ fundamental plaquette characters $F_i=\operatorname{Tr}U_i$. Each has second moment $1$ and fourth moment $2$ by $2\otimes2=1\oplus3$. Distinct plaquette characters are pairwise independent, since each has a private Haar link. In any product of at most four characters, a face of odd multiplicity forces a private odd edge among the odd faces. Any two distinct elementary squares share at most one edge. Independent center changes on Haar links therefore kill that moment.

For the differences $U_i=F_i(x)-F_i(y)$, $\mathbb E U_i^2=2$, $\mathbb E U_i^4=10$ and $\mathbb E U_i^2U_j^2=4$ for $i\ne j$. The mixed odd fourth moments vanish by the same parity rule applied to the two slices. The second difference vector is an independent copy. Consequently $\mathbb E J^4=100d+96\binom d2$ and the limiting relative variance is **$2+13/(4d)$**. This also bounds the iterated limit with volume taken after low temperature. A joint limit requires a uniform rate for the kernel expansion. [Physical spectrum](electric.md) · [Independent Haar control](check_haar.cpp)
