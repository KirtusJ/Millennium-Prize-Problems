# What can fail when the number of plaquettes grows?

Let $G_{ij}=\langle f_i,f_j\rangle$ and $H_{ij}=\langle f_i,Sf_j\rangle$ for the projected local readings of the [plaquette theorem](plaquette.md). On the coefficient space modulo the kernel of $G$, the largest generalized eigenvalue of $(H,G)$ is the transmission of their **whole span**. For an independent packing of $k$ link pairs the proof yields $G-H\succeq\delta I$ in the specified plaquette coordinates. A bound $G\preceq C I$ independent of $k$ would give $H\preceq(1-\delta/C)G$. Pointwise estimates on the entries of $G$ allow its largest eigenvalue to grow.

For an exact control take a hidden spin $h=\pm1$ with symmetric stationary binary transition and nonconstant eigenvalue $\rho_k=k/(k+1)$. Add $k$ independent, uniform signs $e_i$ refreshed at every step. On the full state this is a positive self-adjoint Markov contraction with a unique stationary state. Use a trivial coarse algebra and readings $f_i=h+e_i$. All means vanish. At equal time $G=I+\mathbf1\mathbf1^\mathsf{T}$, and at one step $H=\rho_k\mathbf1\mathbf1^\mathsf{T}$. Every individual transmission is $\rho_k/2<1/2$. Even $G-H\succeq I$ holds for every $k$, yet the uniform sum has transmission $k\rho_k/(k+1)\to1$. This disproves extending the individual bound by enumerating more well-contracted readings. It leaves the Wilson covariance estimate open.

The coarse coupling obeys a general ceiling worth keeping when the local analytic deficit is small. For normalized $f\perp P$ put $r=\langle f,Sf\rangle$. Since $S^2\le S$,
$$
 \|PSf\|^2\le\|Sf\|^2-|\langle f,Sf\rangle|^2\le r(1-r)\le\tfrac14 .
$$
The bound with the coarse compression is $\|PSf\|^2\le ar$. The plaquette theorem gives the further upper bound $a(1-\delta/K)$, which need not improve $1/4$. For the erased path space, the stronger bound $a\theta^2$ does vanish under its stated growth condition. The Wilson proof still needs both collective transmission and a coupling estimate strong enough for the two-block gap criterion. [Path result](README.md) · [Two-block criterion](../../g4/full-attempt/physical-refinement/isotropic.md) · [Z4’s plane-sum convention](normalization.md)
