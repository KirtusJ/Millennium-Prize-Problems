# The two-face coefficient

All operators below act on the finite product of SU(2) link groups. Write $\mathbf1$ for the normalized constant function, $P=1-|\mathbf1\rangle\langle\mathbf1|$, and $R=H_0^{-1}P$. The eigenvalue of the constant Haar vacuum is simple and isolated. The magnetic potential is smooth bounded multiplication. A Riesz contour around the ground eigenvalue gives the local analytic vacuum by the resolvent expansion and normalization with positive overlap. For every fixed Sobolev order the resolvent of this elliptic operator maps to two higher derivatives and the potential acts boundedly. Thus the expansion can also be used before applying the weighted kinetic operator, or in the first-moment quadratic form. All neighborhoods and remainder constants here may depend on the finite box. The same elliptic argument around any finite real coupling applies to the simple positive vacuum. [Regular perturbation theory, simple isolated eigenvalues](https://www.uni-goettingen.de/de/document/download/bd29ee33568ee39be7379307cd4c7e12.pdf/witt_lecture_1.pdf)

The vacuum equation for $H_0-\lambda S$, using $\langle S\rangle_0=0$, yields
$$
\Omega_\lambda=\mathbf1+\lambda S/h+
 \lambda^2\left(R S^2/h+c_2\mathbf1\right)+O(\lambda^3).
$$
For balanced weights the order-$\lambda$ output of $O$ is identically zero. After centering, its order-$\lambda^2$ coefficient therefore equals
$$
v_2=h^{-1}\big(W R S^2-P S_a S\big),\qquad S_a=\sum_p a_p x_p.
$$
Only the constant component is removed here. Since the shifted Hamiltonians converge in norm resolvent as $\lambda\to0$, convergence of the rescaled vectors implies weak convergence of their finite spectral measures, including their total masses. First moments follow separately from the Sobolev expansion and convergence of the kinetic quadratic forms after the bounded perturbation.

* For $p=q$, the character product $x_p^2$ has a constant component and an adjoint component with the same spin on all four links. On the latter $W/H_0=a_p$. Both components disappear from $v_2$.
* For distinct faces with no shared link, the eight exterior links are fundamental. On their product $W/H_0=(a_p+a_q)/2$. This cancels the two orders in $S^2$ against the corresponding terms in $S_a S$. Sharing a vertex alone changes nothing here.
* When $p,q$ share $e$, the two fundamental occurrences on $e$ split into spins $j=0,1$. Dual and fundamental representations of SU(2) are equivalent. Let $P_j$ be the spectral projection of $K_e$ on that sector. The other six links remain fundamental. The total kinetic energy is $h_j=\kappa(9/2+j(j+1))$. If $A=(a_p+a_q)/2$, the sum of the six exterior weights is $8A-2w_e$. On $P_j(x_px_q)$ the factor multiplying the vector in $v_2$ is therefore
$$
\frac{2}{h}\left(\frac{(3/4)(8A-2w_e)+j(j+1) w_e}{9/2+j(j+1)}-A\right)
=\frac{2}{h}\frac{j(j+1)-3/2}{9/2+j(j+1)}(w_e-A).
$$
The spin-zero and spin-one factors are $-2d_{pq}/(3h)$ and $2d_{pq}/(13h)$. [Clebsch–Gordan rule for SU(2)](https://www.dpmms.cam.ac.uk/~sjw47/RepThLecturesMich2012.pdf)

To find the norms, orient both faces along the common link, reversing a whole trace when necessary. With the six exterior links fixed, write $x_p=\operatorname{Re}(UA)$ and $x_q=\operatorname{Re}(UB)$ in unit quaternions. The common link $U$ is Haar. Its four real coordinates have covariance $I/4$. The common-link mean is $\operatorname{Re}(\bar A B)/4$, the normalized exterior-loop trace divided by four. Since the disjoint tails $A,B$ are independent Haar, the squared norm of this projection is $1/64$. Conditional instead on $U$, the two traces are independent and each has second moment $1/4$. Their product has squared norm $1/16$, leaving $3/64$ in spin one.

The half-integer link labels occur exactly on the six outer edges. These identify the unordered face pair: the perimeter is a $2\times1$ rectangle or the bent six-cycle of two perpendicular unit faces. In either case there is exactly one nearest-neighbor chord joining nonconsecutive perimeter vertices, namely the removed shared edge. This can be seen by taking that edge from $0$ to $e_1$ and the two length-three outer paths displaced by unit directions transverse to $e_1$, either opposite or perpendicular. At side at least five no additional chord appears through periodic identification. Thus distinct pairs have distinct half-integer link patterns. Peter–Weyl orthogonality makes the vectors orthogonal, even if their supports intersect. Their patterns are also distinct from the four fundamental links of a single excited face. The norm and moment formulas in the [main note](README.md) now follow by summing the squares with weights $1,h_j$ respectively.

The open two-face numerical control uses the same two shared-link sectors with a different volume and boundary. Its link, outer-path and angular integrals are described in the [execution record](execution.md). It does not test the generic-coupling determinant on the periodic boxes.
