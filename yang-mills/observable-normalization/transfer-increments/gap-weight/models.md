# Fixed local observables testing the correlation-time criterion

Let $n=\xi\to\infty$, $m=1/n$. In gap units place fractions $p$ and $1-p$ at energies $1$ and $B>1$. The normalized reading at time $t$ is
$$
 L(t)=e^{-t}[p+(1-p)e^{-(B-1)t}].
$$
Each row below specifies a family at every sufficiently large $n$. In each, the raw spectral weight below **every fixed** $K\ge1$ eventually equals $p$.

| $p$ | $B$ | Consequence |
|---|---|---|
| $n^{-2}$ | $1+2\log(1+n)$ | The sharp upper bound is attained at $K=1$, with $R=\sqrt e\,(1+n)/2$. Both lattice energies tend to zero. |
| $e^{-n/4}$ | $n$ | $R\to\sqrt e$. Although the gap weight is exponentially small in $n$, it dominates both readings. |
| $n^{-2}$ | $1+3\log n$ | The probability of the upper atom after one correlation time is $O(n^{-1})$, yet $R\sim\sqrt{en}$. A tight full-time law and even weak convergence to $\delta_1$ permit failure of (C). |
| $n^{-2}$ | $1+\log\log n$ | For each fixed $T\ge0$, the best ratio under positive time smearing on $[0,T]$ grows as $\sqrt{e\log n}$. |

For the last row, $(\log n)^{-t}$ dominates $n^{-2}$ at both fixed times $t=2T+1/2$ and $t=2T+1$. Their ratio gives the stated asymptotic by the [endpoint minimization](README.md). For the third row the cutoff-normalized reading has a further explicit threshold. For $t>2/3$, $L(t)/L(1)\to e^{1-t}$, at $t=2/3$ it tends to $2e^{1/3}$, and for $0<t<2/3$ it diverges. This distinguishes the information in the full-time weak limit from the exponential moment in (C).

## A single three-state spin realizes all four laws

Take uniform measure on three spin states. Identify its $L^2$ space isometrically with Euclidean coordinates by dividing function values by $\sqrt3$. Put
$$
 u=(1,1,1)/\sqrt3,\qquad
 f=(1,-1,0)/\sqrt2,\qquad g=(1,1,-2)/\sqrt6 .
$$
The centered observable has values $\sqrt3 f$ for every parameter. Set $v=\sqrt{1-p}\,f+\sqrt p\,g$ and define the one-site Hamiltonian in lattice units by
$$
 H=m\big[I-uu^\top+(B-1)vv^\top\big].
$$
It has vacuum $u$, energy $mB$ on $v$, and energy $m$ on the remaining centered direction. The squared components of $f$ in these two excited spaces are $1-p$ and $p$.

This also defines an ordinary reversible spin process. The rows of $H$ sum to zero. The product $v_1v_2=-1/2+2p/3$ is nonpositive for small $p$. For either other pair, $|v_i v_3|\le |v_3|=\sqrt{2p/3}$. In all four rows $(B-1)\sqrt p\to0$, so every off-diagonal entry of $H$ is strictly negative for sufficiently large $n$. Uniformization of the continuous-time generator $-H$ gives an entrywise positive stochastic matrix $P=e^{-H}$. Explicitly, for $c>\max_i H_{ii}$, $I-H/c$ is stochastic with positive entries and $P=e^{-c}\sum_{j\ge0}c^j(I-H/c)^j/j!$. Symmetry gives stationary uniform measure. The spectral transfer is positive definite.

At every site of the infinite cubic spatial lattice take an independent copy with this step. Products of the vacuum and the two local centered eigenfunctions, with finitely many nonconstant factors, form an orthonormal basis of the product $L^2$ space: cylinder functions are dense and expand in this basis on each finite set. The transfer eigenvalues are $e^{-m(j+B l)}$ for counts $j,l\ge0$. The constant is the only vacuum, the overall gap in lattice units is exactly $m$, and the same site reading has the two-atom law above. Equivalently all finite periodic spatial boxes have this same gap before passage to the product state. The examples test locality, time-transfer positivity and the order of the spatial limit. The site dynamics are independent in space. Establishing the corresponding spectral weights for the interacting Wilson measure requires a separate argument. [Product-chain spectral background, Levin, Peres and Wilmer, chapter 12](https://www.stat.berkeley.edu/~aldous/260-FMIE/Levin-Peres-Wilmer.pdf)
