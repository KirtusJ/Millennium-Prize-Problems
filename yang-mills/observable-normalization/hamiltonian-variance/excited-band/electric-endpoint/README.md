# The fundamental plaquette band starts at an electric energy

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Z4’s corrected lower endpoint holds. Keeping the exact plaquette variance and sharing one energy budget between its electric and magnetic parts yields the stronger uniform choice $L=\kappa/18$. On the same finite periodic SU(2) Hamiltonian boxes as the [original band estimate](../), let $M_j=\int E^j\,d\nu(E)$ for the centered fundamental trace. For every $g=\lambda/\kappa>0$ and $\kappa>0$,
$$
 M_1\ge (2\kappa/9)M_0,\qquad
 \nu([\kappa/18,\,4D_*/A])\ge A^2/(8D_*) ,
$$
with $A=9\kappa/[8(1+B)]$ and the [previous second-moment bound](../third-moment/) $D_*$. At $g=0$ the spectral measure has unit weight at $3\kappa$. This provides a guaranteed band; it allows additional spectral weight below the band. [Z4’s challenge and independent review](../../../../z4/reviews/r7-wild/report.md)

Put $x=\operatorname{Tr}U_p/2$, $u=\mathbb E(1-x)$, $S=\mathbb E(1-x^2)$ and $K=K_e$ for one incident link. The [finite-box ground-state calculation](../../) gives $K+gu\le B=\min(g,17\sqrt g/8+3/16)$. Z4 observes that $M_0=4\operatorname{Var}x\le8u\le8B/g$, also $M_0\le4$. With $K_F=\min(4,8B/g)$, $A/(4K_F)$ leaves at most $A/4$ in the low-energy term of the moment extraction. This verifies Z4’s use of the improved norm budget. The following calculation avoids a separate numerical or piecewise maximization of $K_F(1+B)$.

Retaining both moments of $x$ gives $M_0=4(2u-u^2-S)$, while the energy form gives $M_1=4\kappa S$. The sphere integration by parts yields $3-4S\le4\sqrt{KS}$. If the left side is nonnegative, squaring gives $9\le(16K+24)S-16S^2$. If it is negative, $24S>18$. Thus in both cases $9\le(16K+24)S$.

Multiplying the joint energy budget by $u\ge0$ and completing the square in $\sqrt g\,u$ gives $uK\le289/256+3u/16$. Since $u\le2$,
$$
 (2u-u^2)(K+3/2)
 \le (2-u)(289/256+27u/16)
 \le 99/32 .
$$
The last inequality follows by completing the square. Since $S(K+3/2)\ge9/16$, division by the positive $K+3/2$ gives $2u-u^2\le(11/2)S$. This proves the claimed relation between $M_0$ and $M_1$.

For $U=4D_*/A$ and $L=\kappa/18$, the integrated pointwise estimate gives $M_1\le L M_0+D_*/U+U\nu([L,U])$. The two terms before the band are at most $M_1/4$ and $A/4$, respectively. Since $A\le M_1$, this leaves at least $A/2$ for $U\nu([L,U])$. The upper endpoint exceeds $L$ by its explicit formula.

On the specified trajectory $\kappa=2/(\beta b)$ the guaranteed lower edge is $1/(9\beta b)$, so it diverges whenever $\beta b\to0$. This conclusion concerns the band guaranteed by the estimates. It supplies neither a full spectral gap nor a lower bound for a reading at fixed positive physical time. The original $A/16$ band remains valid with its original asymptotics. [Lean coverage and replay](execution.md)
