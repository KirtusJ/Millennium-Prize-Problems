# A second spectral moment uniform in the magnetic coupling

Director A4 · November 22, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

For the interacting SU(2) Hamiltonian on periodic cubic boxes of side at least three, write $M_j=\int E^j\,d\nu_p(E)$ for the centered unnormalized plaquette trace. The electric coefficient $\kappa$ uses the half-length generators of the [Hamiltonian note](../../). For every magnetic coupling $\lambda\ge0$ and every box,

$$M_2\le 86\,401\,\kappa^2.$$

The constant is an explicit upper estimate. The smaller direct estimate from the [positive-energy interval proof](../) remains available. That result now applies with

$$
 D_* = \kappa^2\min\{(6+8\sqrt B)^2,\;86401\},\qquad
 A=\frac{9\kappa}{8(1+B)},\qquad B=\min\{g,17\sqrt g/8+3/16\},\quad g=\lambda/\kappa .
$$

In particular $\nu_p([A/16,4D_*/A])\ge A^2/(8D_*)$. At large $g$ the upper endpoint grows at most as $\kappa\sqrt g$ and the guaranteed weight is at least a constant times $1/g$. The displayed lower endpoint has order $\kappa/\sqrt g$. With the same $D_*$ and guaranteed weight the [subsequent electric-scale estimate](../electric-endpoint/) raises it to $\kappa/18$. This improves the earlier upper endpoint of order $\kappa g$ and the weight of order $g^{-3/2}$. It does not locate the bottom of the spectrum.

## Third moment as a local double commutator

Use the **unit-round** product metric in the calculation, so $H=-\gamma\Delta+V$ with $\gamma=\kappa/4$ and $V=\lambda\sum_q(1-x_q)$. Write $F=2x_p$, $Q=H-E_0$, and $f=F-\langle F\rangle$. The normalized ground state and all functions acted on below are smooth on a finite product of compact groups. Define the vector field $Y=\nabla F$, the scalar $h=\Delta F/2=-6F$ and the skew differential operator $T=Y\cdot\nabla+h$. Only the four links of $p$ occur in $T$. Integration by parts gives $T^*=-T$ on the common smooth domain. Since $Q(f\Omega)=[H,F]\Omega=-2\gamma T\Omega$,

$$
 M_3=4\gamma^2\langle T\Omega,Q T\Omega\rangle
 =2\gamma^2\langle\Omega,[T,[T,H]]\Omega\rangle .
$$

Expanding the nested commutator gives the second equality using $H\Omega=E_0\Omega$. Both kinetic and magnetic terms contribute. The magnetic commutator in this identity persists even though $[V,F]=0$.

## Kinetic term and its constants

Let $D_i$, $1\le i\le12$, be the orthonormal invariant fields on the four links of $p$, and put $K_N=\sum_i\|D_i\Omega\|^2\le16B$. All other link derivatives commute with $T$. The skew operators $P_i=[T,D_i]$ and $R_i=[T,P_i]$ are first order. Expanding the square and integrating by parts gives the exact contribution for direction $i$,

$$
 \langle[T,[T,-D_i^2]]\rangle
 =2\operatorname{Re}\langle R_i\Omega,D_i\Omega\rangle+2\|P_i\Omega\|^2.
$$

Here and below operator brackets without a state inside an expectation are evaluated in $\Omega$. To bound the coefficients, write $T=\sum y_jD_j+h$. Every ordered invariant derivative of $F$ has absolute value at most 2. Each differentiation inserts a unit quaternion generator in the same four-link word, including when a link is inverted. The absolute trace of the resulting unitary product is at most 2. Hence the $y_j=D_jF$ and their first two derivatives are bounded by 2; $h$ and its first two derivatives are bounded by 12.

In this frame the structure constants within one link are $0,\pm2$ and those across distinct links vanish. For fixed $i,k$, at most one $j$ contributes to $[D_j,D_i]^k$. Thus the coefficient $p_i^k=\sum_j y_j[D_j,D_i]^k-D_i y_k$ and its first derivatives have magnitude at most 6. The scalar $p_i^0=-D_i h$ and its derivatives are bounded by 12. For $R_i$, each vector coefficient is bounded by
$12(2\cdot6+6\cdot2)+2(2\cdot6\cdot2)=336$.
The last term counts the two ordered pairs contributing to one structure-constant output. The scalar coefficient is bounded by $12(2\cdot12+6\cdot12)=1152$. Both vector coefficient norms are therefore at most 1200 (use $336\sqrt{12}<1200$), and both scalar magnitudes are at most 1200.

It follows that each $\|P_i\Omega\|^2,\|R_i\Omega\|^2$ is bounded by $2\cdot1200^2(1+K_N)$. Applying $2|\langle r,d\rangle|\le\|r\|^2+\|d\|^2$ and summing the twelve displays bounds the kinetic double commutator for $-\Delta$ above by $C_K(1+K_N)$ with $C_K=72\cdot1200^2+1$.

## Magnetic term and localization

Put $S=\langle1-x_p^2\rangle$. By cubic symmetry it is the same for every face. The nested potential commutator is multiplication by

$$Y(YV)=\operatorname{Hess}_N V(Y,Y)+\langle\nabla_N V,\nabla_Y Y\rangle ,$$

where $N$ denotes the four-link product. At most 16 plaquettes touch these links. The restricted Hessian of each $x_q$ has operator norm at most 12, and that of $F$ has norm at most 24. Indeed, in the orthonormal bi-invariant product frame the Hessian entries are the symmetrized ordered second derivatives. Their magnitudes are at most 1 and 2 respectively, and the matrix has size 12. Equivalently the spectator links in a neighboring plaquette are held fixed in this step.

On each common link $|\nabla_e x_q|^2=1-x_q^2$. Thus $\langle|Y|^2\rangle=16S$. Cauchy–Schwarz for a sum of at most 16 restricted gradients gives $\langle|\nabla_N V|^2\rangle\le16^2\cdot4\lambda^2 S$. It follows that the first Hessian term is bounded in absolute expectation by $16\cdot12\lambda\cdot16S$. The second is bounded by $24\sqrt{1024\lambda^2 S}\sqrt{16S}$. Together they give $|\langle Y(YV)\rangle|\le6144\lambda S$. This step retains the small factor $S$ in both terms.

## Interpolation and the upper endpoint

We now have
$$
 M_3\le\frac{\kappa^2}{8}
 \left[\frac{\kappa}{4}C_K(1+16B)+6144\lambda S\right]
 \le C_3\kappa^3(1+B),\qquad C_3=C_K+1536 .
$$
The ground-state trial estimate gives $\lambda S\le2\kappa B$ because $1-x_p^2\le2(1-x_p)$. For $g\le1$ one has $S(1+B)\le2$. For $g\ge1$, write $u=\sqrt g$. Then $B\le5u/2$, $Su^2\le2B$, and $1+B\le7u/2$ give $S(1+B)\le35/2\le18$.

Positive spectral support implies $M_2^2\le M_1M_3$. To see this, integrate $E(M_1E-M_2)^2\ge0$ and divide by $M_1>0$. Since $M_1=4\kappa S$, this gives $M_2^2\le72 C_3\kappa^4\le86401^2\kappa^4$. All constants were obtained before any spatial-volume limit.

On B4’s bare tree-level spatial trajectory with spacing $b$ the upper scale $\kappa\sqrt g$ is of order $1/b$. The bound therefore still permits excitation energies to diverge in physical units. Tightness in a fixed physical window under simultaneous spatial refinement would require new information. [Regulator matching and conversion](../../../../transfer-operator/hamiltonian-time/) · [Guest replay and independent rotor control](execution.md)
