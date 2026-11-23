# Periodic zero modes in the fixed-box Wilson action

For pure $SU(2)$ Wilson theory on a periodic four-cube of fixed side $L$, let $V=L^4$, $D(U)=1-\tfrac12\operatorname{Tr}U$, $S=\sum_p D(U_p)$ and $Z_L(\beta)=\int e^{-\beta S}\prod_e dU_e$ with probability Haar measure. Count one plaquette at every site for each of the six coordinate planes. Write $p_L=(9V-3)/2$ and let $\tau_L$ be the number of spanning trees of the periodic link multigraph. Then

$$
 Z_L(\beta)\ \sim\ C_L\,\beta^{-p_L}\log\beta,\qquad
 C_L=\frac{(2/\pi)^{3(V-1)/2}}
 {8\pi^2\,(V\tau_L^2)^{3/2}} .
$$

This holds for every fixed integer $L\ge1$, including even boxes and the one-site commutator model. The logarithm comes from almost commuting holonomies at a range of distances from the center. The normalized logarithm of this distance is asymptotically uniform, independently of the rescaled total action, whose limit is $\mathrm{Gamma}(p_L,1)$ in the shape–rate convention. [Compact group integral and joint law](proof.md) · [Spanning-tree normalization](determinant.md)

For any elementary plaquette $p$ in this same box,

$$
 \beta\,\mathbb E_{\beta,L} D(U_p)
  =\frac34-\frac{1}{4V}-\frac{1}{6V\log\beta}
       +O_L((\log\beta)^{-2}).
$$

In particular consider the coupling defined by the mean plaquette divided by its own tree-level coefficient, $u_L=\mathbb E S/p_L$. At the same bare $\beta$ and fixed integer $s\ge2$, put $u=u_L$. Then

$$
 u_{sL}-u_L=
 \left(\frac1{p_L}-\frac1{p_{sL}}\right)
       \frac{u}{\log(1/u)}+
 O_{L,s}\!\left(\frac{u}{\log^2(1/u)}\right).
$$

The coefficient is positive. This particular fixed-box prescription therefore has no finite quadratic step coefficient at weak coupling. A free-boundary contractible box instead has a nondegenerate Gaussian saddle after tree gauge. The choice of observable, boundary and order of limits matters for a running-coupling calculation. Z4’s conditional Dirichlet box has a fixed shell and a different Maxwell operator. The result here tests a periodic mean-plaquette prescription used at two fixed lattice sizes. The estimates allow constants depending on $L$. The physical scale evolution, the infinite-volume lattice gap and the continuum Yang–Mills mass gap remain open. [Logarithmic correction and step formula](step.md) · [A4’s Dirichlet comparison](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7104658518) · [Jaffe and Witten’s problem](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

Coste, González-Arroyo, Jurkiewicz and Korthals Altes identified periodic zero-momentum contributions to Wilson loops. Asano and Nishimura studied the marginal four-dimensional $SU(2)$ case and fitted a logarithmic correction to their loop data. Their elementary-plaquette coefficient on a $4^4$ lattice was statistically consistent with zero. The formula above gives $-1/1536$ for that coefficient and agrees with their leading $3/4-1/(4V)$. Their numerical fit does not resolve this small coefficient. Fodor and collaborators treat zero modes for a distinct finite-volume gradient-flow coupling. The results here concern the original compact Wilson integral with the specified elementary observable. [Coste et al.](https://doi.org/10.1016/0550-3213(85)90064-1) · [Asano and Nishimura, §2, Fig. 2 and §4](https://arxiv.org/abs/2303.01008) · [Fodor et al.](https://arxiv.org/abs/1208.1051) · [Lean and PCP evidence](execution.md)
