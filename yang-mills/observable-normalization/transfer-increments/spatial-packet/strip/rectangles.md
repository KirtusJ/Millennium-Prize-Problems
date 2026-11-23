# Area bound for Wilson rectangle deficits and translated magnetic packets

Keep the fixed-coupling periodic-limit states, unit quaternion norm and plaquette normalization of the [strip proof](README.md). For a coordinate rectangle with side lengths $m,n\ge0$, denote its half-trace expectation by $W(m,n)$. Then
$$
  1-W(m,n)\le mn[1-W(1,1)],\qquad
  \|1-U_{m\times n}\|_2\le C\sqrt{mn/\beta}. \tag{1}
$$
This bounds the deficit from above. It gives no positive lower bound on a string tension.

For fixed $m$, take the reflected open staples with the middle segment replaced by $m$ successive tangent links. The endpoints $0,m e_i$ still lie in the reflecting plane. The Gram kernel is $W(m,s+t)$ and its mass is $W(m,0)=1$, since traversing a path and its inverse gives the identity. Every other step of the bounded-shift argument is independent of $m$. Hence $1-W(m,n)\le n[1-W(m,1)]$. Interchange the coordinate axes and apply the one-step-width estimate to get $1-W(m,1)\le m[1-W(1,1)]$. The identity for the norm of a unit quaternion and the first plaquette moment prove (1). Signed side lengths are handled by translations and reflection in either axis. These inequalities hold for all finite integer rectangles in each selected infinite-volume state.

## A translated packet at the seventh-root scale

C4 resolved the joint spectral measure of a packet for the positive time transfer and the three spatial translations. The additional estimate needed for true translates concerns reordering the paths used to carry color to the slice root. Let $D(z)$ denote the ordered three-axis spatial path with signed displacement $z$. Starting with $D(z)$ followed by the translate of $D(v)$, swap the third $z$-block with the first $v$-block, then the second $z$-block with the first $v$-block, then the third $z$-block with the second $v$-block. After this the pairs with a common axis combine or cancel exactly, leaving $D(z+v)$. In each exchange, write the old and new paths as $PABQ$ and $PBAQ$, with displacements $A,B$ on perpendicular axes and a common suffix starting at the same vertex. The ratio of the transporters is the conjugate by $P$ of the boundary of the rectangle with sides $|A|,|B|$, since the common suffix cancels. Using (1) and the triangle inequality gives
$$
 \|U(D(z)D_z(v))-U(D(z+v))\|_2
 \le C\beta^{-1/2}
    (\sqrt{|z_3v_1|}+\sqrt{|z_2v_1|}+\sqrt{|z_3v_2|}).
$$
Here $D_z(v)$ starts at $z$. When $z$ lies along the first axis, the two paths agree after free cancellation. Off that axis, for $|z|_1\le LR$, $|v|_1\le C R$, the bound is $C_L R/\sqrt\beta$. The common time trunk conjugates both paths and leaves the estimate unchanged.

The adjoint action of two unit quaternions on the same curvature vector differs by at most twice their distance times the curvature norm. The uniform $L^2$ bound on the scaled curvature and Cauchy–Schwarz give the same order of error per face in $L^1$. Summing against a packet of $\ell^1$ mass $O(R^2)$ costs $C_L R^3/\sqrt\beta$. The bounded, globally Lipschitz observable $X\mapsto e^{-s|X|^2}$ therefore has a covariance error of at most $C_{s,L}R^3/\sqrt\beta$ from changing the translated root. The [common-root comparison](README.md) costs $C_{s,L}R^{7/2}/\sqrt\beta$ for $|z|_1\le LR$, since translating the spatial profile only changes its support constant. Combining the two gives, for every integer lag $n\ge0$,
$$
 \sup_{\mu,\,|z|_1\le LR}
 \left|\langle\psi,T^n U(z)\psi\rangle - B_R(n,z)\right|
 \le C_{s,L} R^{7/2}/\sqrt\beta.
$$
Here $U(z)$ in the inner product is the spatial translation on the Wilson Hilbert space, $\psi$ is C4’s centered single-slice packet, and $B_R(n,z)$ is the free reference covariance.

Take $x=e^{-RE}$ and a smooth compactly supported bump in the rescaled momentum $P=Rk$ on the representative Brillouin cube. C4’s periodization tests every integer translate; its absolutely summed Fourier coefficients at $|z|_1>LR$ have total modulus tending to zero as $L\to\infty$, uniformly in $R$. For a fixed polynomial in $x$, choose $L$ to control this tail first. The estimate above then applies to its finitely many lags and all retained offsets. The free covariance limits and total-mass convergence at zero lag give the same weak limit as in C4’s proof whenever $R\to\infty$ and $R^7/\beta\to0$. The limiting measure has support $\varepsilon\ge|P|$ and zero mass on its boundary.

At $R=\lfloor c\beta^{1/7}\rfloor$, every prescribed finite list of open neighborhoods of strict interior points $\varepsilon>|P|$ has a positive state-uniform lower bound on its unnormalized spectral weight for all sufficiently large couplings. Indeed the continuum two-leg measure assigns each interior bump positive weight; approximate its energy test by a polynomial, control the momentum tail, and then choose a common $c$ small enough for the $C_{s,L}c^{7/2}$ error in every retained test. The endpoint conclusion locates spectral weight; the finite-coupling support and the physical correlation length remain undetermined. [C4’s joint measure, periodization and positivity proof at 667f247](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/667f24719eaaae9f5600e931031c54373672b284/yang-mills/central-quotients/tangent-curvature/periodic-limit/joint-momentum/README.md) · [Signed path controls and Lean scope](checks.md)
