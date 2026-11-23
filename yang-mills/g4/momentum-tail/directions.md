# Different decay in the three momentum components

For the same fourfold packet of $12$ plaquettes and the same unnormalized momentum marginal as in [the maximum-norm estimate](README.md), the normal coordinate has a stronger tail than either in-plane coordinate. For $H\ge4\pi$, $R\ge2$, $\beta\ge2$,
$$
 \rho_{\beta,R,\mu}(|Rk_i|\ge H)\le C_s(H^{-a_i}+R^{7/2}/\sqrt\beta),
 \qquad (a_1,a_2,a_3)=(6,6,8).
$$
The limiting free marginal has matching upper and lower powers for each of the three coordinates. The stronger normal-direction power comes from the magnetic polarization.

In the scaled lattice cube use $\widehat p_j=2R\sin(p_j/(2R))$ and $r_R=|\widehat p|$. The amplitude in the one-color equal-time density is
$$
 \frac{\widehat p_1^2+\widehat p_2^2}{2 r_R\sqrt{1+r_R^2/(4R^2)}}.
$$
We have $(2/\pi)|p|\le r_R\le|p|$. On $|p_3|\ge1$ the amplitude is at most $C(p_1^2+p_2^2)/|p_3|$. The two in-plane box factors squared have finite second moments and the squared third difference is bounded. Integrating the remaining $(1+|p_3|)^{-8}/|p_3|$ over $|p_3|\ge H$ gives $O(H^{-8})$, uniformly in $R$. The marginal mixture and wrapping argument in the main proof now uses only this coordinate, with the conditional $(2j)^9$ factor still summable. For either in-plane coordinate the original $(2j)^7$ bound suffices.

For the lower bound in the limiting distribution take one leg with $p_3\in[2H,3H]$, $|\sin(p_3/2)|\ge1/2$ and $p_1,p_2\in[1,2]$. Precisely, the stride is $R$ and the scaled phase is $p_3$, so its squared third-difference factor is $|1-e^{ip_3}|^6=(2|\sin(p_3/2)|)^6\ge1$ on this set. The third box factor squared is at least $cH^{-8}$, and the magnetic amplitude is at least $c/H$. A set of length $cH$ contributes, giving $c_sH^{-8}$. With the second leg in $[1,2]^3$ the total third component exceeds $H$. The in-plane lower bounds use the set from the main proof and exchange coordinates 1 and 2 as needed.

For the normal coordinate use $(1-F_M)^5$ with $M=\lceil2\pi R/H\rceil$ when $H\le\pi R$. Its coefficient norm is at most 32, the support of the coefficients lies in $|j|\le5(M-1)$, and its floor on the event is $(3/4)^5$. Near zero it is bounded by $C\min(1,(M|k_3|)^{10})$. For $A=R/M\ge1$, layer cake gives $10A^{-10}\int_0^A t^9 \rho_R^G(|Rk_3|>t)\,dt\le C_s A^{-8}$. The finite-coupling comparison for true translates applies with $L=5$ and contributes $32 C_{s,5}R^{7/2}/\sqrt\beta$. For $H>\pi R$ the event is empty. At fixed $c$ on the seventh-root scale this proof retains the same absolute comparison error. [A4’s translated estimate](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/e2e56f57f9950af5e32a60b8486e1bb3587e34ca/yang-mills/observable-normalization/transfer-increments/spatial-packet/strip/rectangles.md)
