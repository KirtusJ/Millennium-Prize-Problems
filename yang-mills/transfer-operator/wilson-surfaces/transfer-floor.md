# A one-step transfer lower bound that costs only the path length

Work first at finite spatial volume with at least three sites per side, and send the time extent to infinity. The spatial and temporal couplings may differ in this calculation. In temporal gauge on an open slab use the unprojected transfer $T=MKM$. The multiplication $M$ is the exponential of one half the spatial Wilson exponent. The kinetic kernel $K$ is the tensor product of the normalized positive central SU(2) convolutions $e^{\beta_t\operatorname{Tr}(gh^{-1})/2}/Z_t$, with $Z_t=2I_1(\beta_t)/\beta_t$. Its fundamental eigenvalue is $r=I_2(\beta_t)/I_1(\beta_t)>0$. The compact operator $T$ has a strictly positive integral kernel. Its top eigenfunction $\Omega>0$ is unique, normalized in product Haar, and gauge invariant by simplicity. Positive character coefficients give operator positivity. Write $\lambda$ for its eigenvalue, $S=T/\lambda$ and $v=M\Omega$.

The temporal gauge here follows from sequential vertex gauge changes in the **open** time slab. Each original temporal Haar link becomes a gauge integration of mass one. In an observable its temporal transports are changed at the same time. The positive free end weights have nonzero ground-state overlap, so fixed insertions converge to the ground-state formula as both ends recede. A charged open spatial path by itself is gauge dependent; the pair of paths joined by the two temporal sides is an ordinary gauge-invariant rectangle. Fixing all temporal links in a periodic history would omit its holonomy. [Periodic transfer and seams](../periodic-time/) · [One-link normalization](../joint-cutoff/)

Choose a path of $l$ distinct spatial links. Let $F$ denote either its closed fundamental trace or one matrix entry of the open-path transport. On these links $K_{\rm path}F=r^l F$: integrate each fundamental or inverse fundamental link in its position. Its squared product-Haar norm $s_F$ is one in the trace case and $1/2$ for an open matrix entry. The path product of independent Haar links is Haar. Write $U=(z,x)$ for path and remaining spatial links.

The eigenfunction equation says $v=M^2Kv/\lambda$. Change a single spatial link with all others fixed. The exponent of $M^2$ changes by at most $8\beta_s$ from its four spatial faces, and the kernel under $Kv$ changes pointwise by a factor at most $e^{2\beta_t}$. Consequently the ratio of the largest and smallest $v(z,x)$ over all path configurations is at most $e^{cl}$, $c=8\beta_s+2\beta_t$. For $\bar v(x)=\int v(z,x)dz$ this gives
$$u_F(x):=\int |F(z)|^2v(z,x)dz\ge s_F e^{-cl}\bar v(x).$$

The eigenline lower bound $K_{\rm path}\ge (r^l/s_F)|F\rangle\langle F|$ is an operator inequality: subtract the eigenprojection and use positivity on its orthogonal complement. Tensor it with the positive $K_{\rm out}$. Its kernel is also pointwise nonnegative, so the preceding pointwise estimate applies separately to the two factors of the exterior quadratic form. With $D=e^{\beta_t}/Z_t$,
$$
\begin{aligned}
 \langle Fv,KFv\rangle &\ge (r^l/s_F)\langle u_F,K_{\rm out}u_F\rangle
 \ge r^l s_F e^{-2cl}\langle\bar v,K_{\rm out}\bar v\rangle,\\
 \lambda=\langle v,Kv\rangle&\le D^l\langle\bar v,K_{\rm out}\bar v\rangle.
\end{aligned}
$$
The second bound follows by replacing each path-link kernel with its supremum. These estimates compare exterior integrals before any volume limit. A single global ground-state overlap in product Haar could decay with the size of the surrounding box. Thus $C_1(F)=\langle F\Omega,SF\Omega\rangle\ge s_F q^l$ with $q=r e^{-2c}/D$.

For the closed loop, $C_0\le4$. Jensen for the spectral probability of $S$ gives $C_k\ge C_1^k/C_0^{k-1}\ge4^{1-k}q^{lk}$. The vacuum also contributes $w^2$ to every $C_k$. For an open path pair joined by the temporal sides, sum the four matrix-entry contributions. Their total zero-step moment is exactly two since the open transport is unitary. The sum of their $s_F$ is also two. Jensen on this sum of positive spectral measures gives the rectangle bound $w_{l,k}\ge 2q^{lk}$. By the isotropy of the unique infinite Gibbs state this equals the mean of the corresponding spatial rectangle. Each argument may use its own transfer axis. The results are uniform in the transverse spatial volume, which can now go to infinity at fixed loops. [Bounds and limits](README.md)
