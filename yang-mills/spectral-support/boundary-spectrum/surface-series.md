# A uniform surface trial and its return-walk expansion

The area-order excess can be seen with just two plaquette weights. Every grounded face on a flat $m\times m$ side patch gets weight $5/3$. Each internal bond gets weight one. With $m=2048$ this gives a rigorous lower quotient **above 4.0816**. The limiting quotient exceeds 4.0848. The small $8\times8$ witness in the main result fits many more trials on moderate boxes. [Packing and area upper bound](README.md)

Write $A=I+L_m$, where $L_m$ is the square graph Laplacian, and $G=A^{-1}$. Let $\mu_m=\operatorname{tr}G/m^2$ and $\nu_m=\operatorname{tr}G^2/m^2$. If $S$ is the patch projection, its ground–ground block is $I-G$. The rank of $S$ is $2m(m-1)$. Write the weight as $1+c$ on ground faces and one on the others. Since the row sums of $S\circ S$ are its diagonal, the quadratic form of $6S\circ S$ is
$$
 6\{2m(m-1)+2c\operatorname{tr}(I-G)+c^2\operatorname{tr}[(I-G)^2]\},
$$
where the last trace is the trace of the squared matrix. The squared vector norm is $3m^2-2m+(2c+c^2)m^2$. At $c=2/3$ the quotient is exactly
$$
 Q_m=\frac{6(34-18/m-20\mu_m+4\nu_m)}{43-18/m}.
$$

The eigenvalues of the path graph Laplacian are $2-2\cos(\pi j/m)$, $0\le j<m$, as is verified by the half-shifted cosine eigenvectors. Thus $\mu_m$ and $\nu_m$ are left-corner Riemann sums on $[0,\pi]^2$ of the functions $a^{-1}$ and $a^{-2}$, respectively, where $a=5-2\cos x-2\cos y$. Let $\mu,\nu$ be their normalized integrals. Both integrands decrease along each coordinate and lie between zero and one. In one dimension the normalized left and right sums differ by the endpoint difference divided by $m$. Applying this to the two coordinates gives $\mu\le\mu_m\le\mu+2/m$ and $\nu_m\ge\nu$.

The full torus average equals the average over $[0,\pi]^2$ by symmetry. In the resolvent expansion every odd return-walk count vanishes and the number of closed walks of length $2k$ on the square lattice is $\binom{2k}{k}^2$. To count them choose $2j$ horizontal times, then order $j$ right and $j$ left steps and $k-j$ steps in each vertical direction. Summing over $j$ gives the stated binomial square. The Fourier adjacency has norm at most four, so the two series converge absolutely:
$$
 \mu=\sum_{k\ge0}\frac{\binom{2k}{k}^2}{5^{2k+1}},\qquad
 \nu=\sum_{k\ge0}(2k+1)\frac{\binom{2k}{k}^2}{5^{2k+2}} .
$$
Keep $0\le k\le16$. Bound the remaining first-series tail by $(16/25)^{17}/[5(1-16/25)]$ and drop the positive second-series tail for its lower bound. Exact rational arithmetic gives $\mu<0.25433$, $\nu>0.09024$. Using the unrounded bounds yields $Q_{2048}>4.08168$ and $\lim Q_m>4.08480$. The finite square with side 2048 therefore yields $n_N(4.0816)\ge6\lfloor(N-2)/2048\rfloor^2$. For any fixed threshold between 4 and 4.0848 a sufficiently large *fixed* patch gives an area-order lower bound. The same $6N^2/\delta$ upper bound applies. [Exact rational evaluation](check_series.py)
