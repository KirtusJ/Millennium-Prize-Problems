# A two-slice measurement using only ordinary windings

At each of two parallel time slices take the first $n$ windings of the **same** square. Let $F_m=1-W_{C^m}$ and let $G_{ij}(t)=\operatorname{Cov}(F_i(0),F_j(t))$ in the finite Wilson vacuum. These are covariances of the original, bounded trace readings. At every fixed $t>0$, on the all-degree trajectory or the explicit trajectory for degree $4n$, one obtains
$$
 \frac{\det G(t)}{G_{11}(t)^{n(n+1)/2}}
 \longrightarrow 2^{n(n-1)}
 \frac{\prod_{k=1}^n (2k+1)!/4^k}
 {(3/2)^{n(n+1)/2}}.
$$
For the once- and twice-wound pair the number is **$40/3$**. It needs one positive time separation and the vacuum means for centering. The regulator spacing, bare coupling, square size and unknown equal-time Gaussian variance drop out. For every fixed $n$ the limiting number is positive, so the regulated $n\times n$ two-slice matrix eventually has full rank. This is a result for varying windings observed at one separation. A statement about the number of eigenvalues in an energy interval requires further information.

**Finite group identity.** If $D=1-W_C$, then $F_m=1-T_m(1-D)$ with $T_m$ the Chebyshev polynomial, since an $SU(2)$ matrix has eigenvalues $e^{\pm i\theta}$. For $m=2$ this is $F_2=4D-2D^2$. On the centered power list $D,\ldots,D^n$, subtracting the respective means, the change of basis to the centered winding list is lower triangular, with diagonal $(-1)^{m+1}2^{m-1}$. Hence the Gram determinant gains the exact factor $2^{n(n-1)}$. Replacing $D^m$ by $(\beta D)^m$ multiplies that power Gram determinant by $\beta^{n(n+1)}$.

**Where the contact variance goes.** Write $q=|X|^2/2$ for the mesh Gaussian and $v$ for its one-color single-time variance. The radial Wick polynomials $P_k(q;v)$ are monic and are determined by
$$
 \sum_{k\ge0} P_k(q;v)\,\frac{z^k}{k!}
   =(1+zv)^{-3/2}\exp\!\left(\frac{zq}{1+zv}\right).
$$
In particular $P_1=q-3v/2$ and $P_2=q^2-5vq+15v^2/4$. Apply this triangular change of basis to $\beta D$ at both regulator slices **before** taking limits, and subtract its actual Wilson expectations. The determinant on centered powers is unchanged, even when $v$ is large. For Gaussian vectors at the two slices the scalar cross-covariance in each color is $K$. Gaussian integration of the product of the two generating functions gives $(1-zwK^2)^{-3/2}$. This follows by taking the determinant of the $2\times2$ one-color quadratic form and multiplying the three identical color factors. Matching coefficients gives
$$
 \mathbb E[P_k(q_1;v)P_l(q_2;v)]
 ={\bf1}_{k=l}\,k!(3/2)_k K^{2k}
 ={\bf1}_{k=l}\,\frac{(2k+1)!}{4^k}K^{2k}
 \qquad(k,l\ge1).
$$
The sharp-contour absolute-moment estimates include all these counterterms. Thus the transformed finite-$n$ matrix tends entrywise to this diagonal matrix with $K=K_R(t)>0$. Its determinant and the limit $\beta^2G_{11}\to(3/2)K_R^2$ prove the formula. The quartic vector already has an independent positive-time reading $15K_R^4/2$ after subtracting its cutoff Gaussian quadratic mixing. The finite-time Schur complement gives the same limiting reading from the measured matrix. The native worker enumerates the color weights of all bijections between the slots of two radial vertices for degrees one through three; the three integer weights before the factors $4^{-k}$ are 6, 120 and 5040. [Explicit comparison](explicit-scales.md) · [Guest and Lean scope](execution.md)

There is also a first correction visible before taking a Gram determinant. At fixed mesh with weak coupling, $C_{21}/(4C_{11})$ for the matrix $C=G(t)$ differs from one to leading order by $5v/(2\beta)$ with a minus sign. This follows exactly from $F_2=4D-2D^2$ and the identity $\operatorname{Cov}(q^2,q')=5v\,\operatorname{Cov}(q,q')$ at nonzero $K$. At fixed physical separation the equal-time $v$ diverges. A measurable limit that removes that factor is
$$
 \frac{1-G_{21}(t)/(4G_{11}(t))}{\mathbb E D}
 =\frac{\operatorname{Cov}((\beta D)^2,\beta D')}{2\,\mathbb E(\beta D)\operatorname{Cov}(\beta D,\beta D')}
 \longrightarrow \frac53 .
$$
In the numerator, subtract $5v$ times the quadratic covariance before passing to the limit; this mixed Wick reading tends to zero. Also $\mathbb E(\beta D)=3v/2+o(1)$ and the scaled quadratic covariance tends to $3K_R^2/2>0$. These facts justify the limit despite the divergent $v$. The correction measures the nonlinear relation between two characters of the **same** holonomy. Its computation leaves the first dynamical correction to the fixed-size interacting correlation undetermined.
