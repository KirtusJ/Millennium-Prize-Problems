# The momentum thresholds and the zero at full staggering

For $k+l=Q$ on the torus, $p_j(Q)=p_j(k)+e^{ik_j}p_j(l)$. The Euclidean triangle inequality bounds $|p(Q)|$ by $|p(k)|+|p(l)|$. On the positive axis $2\operatorname{arsinh}(s/2)$ is increasing and subadditive, as follows by expanding the hyperbolic sine of a sum and using $\cosh\ge1$. Thus $E\ge\omega(Q)$. The configuration $k=0$ attains the kinematic lower boundary.

For $Q_j\in[-\pi,\pi]$ the mean of $A(k)$ and $A(l)$ is
$$
 6-2\sum_j\cos(Q_j/2)\cos(k_j-Q_j/2)
 \le 6+2\sum_j\cos(Q_j/2).
$$
Use $\cosh\omega=1+A/2$ and $2\cosh((u+v)/2)\le\cosh u+\cosh v$ for $u,v\ge0$ to obtain the upper endpoint in the main result. Setting every $k_j=\pi+Q_j/2$ attains it, with $k=l$ modulo $2\pi$. All intervening energies occur by continuity on the connected torus.

For $Q\ne Q_c$ the weight $F(k,Q-k)$ is positive for almost every $k$. When the diagonal has rank three, the second transverse plane maps to a plane which the first projection cannot annihilate. In rank two the kernel of the diagonal is a coordinate axis. For almost every $l$ that axis lies outside the second transverse plane, so the same dimension argument applies. In rank one the surviving coordinate axis has nonzero projection onto both transverse planes for almost every $k$. In every case the factors $h$ are positive away from isolated momenta. Each open interval meeting the interior of the kinematic range has a nonempty open preimage, hence positive intensity. Taking closures proves the stated fiber support. At $Q_c$ every entry of the diagonal is zero. The zero concerns the continuous momentum intensity. Every neighborhood of the corresponding energy interval above $Q_c$ still has positive joint measure from nearby momenta.

## How fast the signal returns

For a continuous nonnegative energy test $\varphi$ on the global energy range, define
$$
 I_\varphi(Q)=\int \varphi(E)e^{-E}F(k,Q-k)\,dk .
$$
Write $Q=Q_c+z$ on the torus. Expanding $1-e^{iz_j}$ gives $-iz_j+O(|z|^2)$. The projections have norm one off their isolated singularities, and $0\le h\le1$. Therefore along any converging unit direction, dominated convergence gives a quadratic leading form in $z$. This argument also gives a uniform $o(|z|^2)$ remainder by compactness of the direction sphere. Reflections and permutations of the spatial axes preserve the Wilson star, the isotropic transfer and the centered scalar observable. Hence the limiting momentum intensity has those symmetries. Its continuous representative inherits them everywhere. At $Q_c$ the quadratic form is consequently scalar, with
$$
 I_\varphi(Q_c+z)=\kappa_\varphi |z|^2+o(|z|^2),\qquad
 \kappa_\varphi=\frac1{1536}\int \varphi(E_c)e^{-E_c}
     h(k)h(l) R(k)_{11}R(l)_{11}\,dk ,
 \quad l=Q_c-k,\quad E_c=\omega(k)+\omega(l).
$$
The expression follows by taking $z$ along axis one. The two diagonal projection entries are positive almost everywhere. Thus $\kappa_\varphi>0$ if $\varphi$ is positive somewhere in $(\operatorname{arcosh}7,2\operatorname{arcosh}4)$. The limiting weight of a radius-$\epsilon$ momentum ball about $Q_c$ for this test is asymptotic to $4\pi\kappa_\varphi\epsilon^5/[5(2\pi)^3]$. A ball centered at a momentum of positive intensity instead has leading order $\epsilon^3$.

## A finite-support Wilson observable

Let $\psi$ be a nonzero real smooth compactly supported profile on $\mathbb R^3$. Give each translated insertion the coefficient $a_M(r)=M^{-3/2}(-1)^{r_1+r_2+r_3}\psi(r/M)$. Form the finite sum of the centered one-slab vectors $v_M=\sum_r a_M(r)U(r)v$. For each fixed integer $M$ the torus eventually contains its support without wrapping. For every continuous energy test $\varphi$ on the compactified lattice energy axis (equivalently continuous in $e^{-E}$),
$$
 \lim_{M\to\infty} M^2
 \lim_{\beta,L\to\infty} \beta^4\langle v_M,\varphi(-\log S)v_M\rangle
       =\kappa_\varphi\int_{\mathbb R^3}|\nabla\psi(y)|^2\,dy .
$$
The formula extends to signed tests by linearity. First use weak convergence with the fixed trigonometric weight $|\widehat a_M(Q)|^2$. Near $Q_c$, Poisson summation gives $M^{3/2}\widehat\psi(Mz)$ plus periodized translates at $M(z+2\pi t)$, $t\ne0$. On the centered fundamental cube these translates are uniformly $O_N(M^{3/2-N})$ for every $N>3$ by rapid decay. Globally $I_\varphi(Q_c+z)=O(|z|^2)$ there. Change variables $u=Mz$, use dominated convergence, and apply Plancherel to $|u|^2|\widehat\psi(u)|^2$ with measure $du/(2\pi)^3$. This proves the formula with the displayed normalization. The limits are ordered. The estimates give no arbitrary growing-support rate at finite coupling.

The nonzero weight recovered by this operation has support $[\operatorname{arcosh}7,2\operatorname{arcosh}4]$, by the same open-preimage argument for the formula for $\kappa_\varphi$. Dividing by the answer at $\varphi=1$ yields its probability law. This is a momentum-selective lattice energy threshold of one observable. Its lower endpoint in physical energy units scales as $1/b$. [Integrated spectral law](edges.md)

An explicit finite stencil gives a second normalization check. In each axis take the centered binomial coefficients $\binom{2m}{m+r}$ for $|r|\le m$, modulate by the full alternating sign, and normalize the three-dimensional product in $\ell^2$. Its squared Fourier weight around $Q_c$ is a product of densities proportional to $\cos^{4m}(z_j/2)$. Under this weight each $\sin^2(z_j/2)$ has the $\operatorname{Beta}(1/2,2m+1/2)$ law. Thus $m\mathbb E|z|^2\to3$: use the first two beta moments to replace $z_j^2$ by $4\sin^2(z_j/2)$ with $O(m^{-2})$ error. The bound on the fourth moment also makes $m\mathbb E[|z|^2\mathbf1_{|z|>\delta}]\to0$ for each $\delta>0$. The rescaled spectral reading therefore tends to $3\kappa_\varphi$ after the fixed-stencil cutoff limit. [Numerical finite-stencil checks](execution.md)
