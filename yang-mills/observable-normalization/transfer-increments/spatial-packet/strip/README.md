# Reflected Wilson strips and a seventh-root upper bound on lattice energies

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

Consider pure isotropic four-dimensional $SU(2)$ Wilson theory with weight $\exp[-\beta\sum_p(1-\operatorname{Re}U_p)]$. At each fixed coupling take any subsequential local limit $\mu$ of even periodic four-cubes as the side tends to infinity. For every such state, the vacuum-normalized time transfer $T_\mu$ satisfies, at all sufficiently large $\beta$,
$$
 m(\beta,\mu)=-\log\|T_\mu|_{\Omega^\perp}\|\ \le\ C\beta^{-1/7}.
$$
The constant and the onset are uniform in the choice of state. Moreover, for any fixed positive integer $d$ and $0<a<b$, there are $c,\eta>0$ so that at even $R=2\lfloor c\beta^{1/7}/2\rfloor$ the Gram matrix of B4’s $d$ centered magnetic packets projected to the lattice energy interval $(a/R,b/R)$ dominates $\eta I_d$. This locates strictly positive spectral weight even in a state with multiple vacua. The physical lattice spacing, positivity of the gap at fixed coupling, and the existence and mass gap of a continuum Yang–Mills theory remain open.

The same argument for [rectangles of arbitrary width](rectangles.md) improves the range of C4’s joint energy and spatial momentum theorem to the seventh-root scale.

## A strip estimate from reflection positivity

Fix distinct axes $i,j$. Write $W(l)$ for the expectation of half the fundamental trace around a rectangle one step wide along $i$ and $l$ steps long along $j$. Set $W(0)=1$. Translation, reflection and axis permutations preserve the state by the periodic construction. For $s\ge0$, let $\Gamma_s$ be the open path from $0$ to $e_i$ consisting of $s$ positive $j$ steps, one positive $i$ step and $s$ negative $j$ steps. Let $\theta$ reflect in the site plane $x_j=0$. For $s,t\ge0$ the product of the inverse reflected path and the other path is a rectangle of height $s+t$ up to cyclic choice of base point and cancellation. This includes the tangent link $\Gamma_0$. Thus
$$
 H_{st}=\tfrac12\sum_{a,b=1}^2\mathbb E_\mu
 \big[\overline{U(\theta\Gamma_s)_{ab}}\,U(\Gamma_t)_{ab}\big]=W(s+t).
$$
Every finite submatrix is positive semidefinite. Apply site-reflection positivity to a finite linear combination of entries of the positive-half transporters, then sum over the matrix entries. On even tori the reflection fixes the two boundary planes. Conditional on their tangent links the two reflected halves have identical weights and independent interiors, yielding the usual squared modulus. At fixed paths this passes to the thermodynamic limit. For states expressed on the gauge-invariant algebra one can first Haar-average the complete paired product over the vertex frames. This use of reflected open paths follows Bachas’s Wilson loop argument. [Site-reflection proof](../../../../central-quotients/tangent-curvature/reflection.md) · [Bachas, Phys. Rev. D 33, 2723 (1986)](https://doi.org/10.1103/PhysRevD.33.2723) · [Preprint, equations 7–8](https://www.slac.stanford.edu/pubs/slacpubs/3750/slac-pub-3814.pdf)

Equip finitely supported complex sequences with the semidefinite form $H$, and let $S e_s=e_{s+1}$. This shift is symmetric since $H$ depends only on the sum of the indices. For a finite sequence $u$ put $q_n=\|S^n u\|_H^2$. Positivity and $|W(l)|\le1$ give $0\le q_n\le\|u\|_1^2$. Expanding $\|S^n u-S^{n+2}u\|_H^2$ gives $q_n-2q_{n+1}+q_{n+2}\ge0$. A positive first difference would force $q_n\ge q_0+n(q_1-q_0)$, contrary to boundedness. Hence $q_1\le q_0$. The shift preserves the null space and extends on the quotient completion to a self-adjoint contraction. For $v=[e_0]$, $\|v\|=1$ and $W(l)=\langle v,S^lv\rangle$. Its spectral measure is a probability on $[-1,1]$.

For $-1\le x\le1$, $1-x^l\le l(1-x)$ by summing powers or induction. Integrating against this measure gives $1-W(l)\le l[1-W(1)]$. For unit quaternions, $|1-U|^2=2(1-\operatorname{Re}U)$ identically. Together with the periodic-state first plaquette moment this yields
$$
 \|1-U_{1\times l}\|_{L^2(\mu)}^2\le 2l[1-W(1)]\le C l/\beta. \tag{1}
$$
The first inequality has coefficient one in the trace deficit. It allows correlated plaquettes and applies to every integer length. The auxiliary shift acts on the staple Gram space. The time transfer enters below, in the spectral interpretation of gauge-invariant spatial observables. [Periodic-state first-moment bound](../../../../central-quotients/tangent-curvature/periodic-limit/pressure.md)

## Transport to an ordered root

Use the path $L_x$ from zero to $x=(t,\mathbf x)$ along time first, then spatial axes $1,2,3$. For a step $e$ in direction $i$ appended at $x$, move that step left past each entire subsequent coordinate segment in turn. Each exchange changes the transporter by a conjugate of one rectangle of length $|x_j|$ and width one. Its norm distance to the identity is unchanged by conjugation or inversion, even when the conjugator depends on the links of the rectangle. Once the step reaches its own segment, it combines or cancels there. There are at most three exchanges and every crossed segment is spatial. The $L^2$ triangle inequality and (1) give
$$
 \|1-L_x U_e L_{x+e}^{-1}\|_2
 \le C\beta^{-1/2}\sum_{j>i}\sqrt{|x_j|}
 \le C\sqrt{w(x)}/\sqrt\beta,\qquad w(x)=1+|\mathbf x|_1. \tag{2}
$$
Here $x+e$ denotes the endpoint of the signed step. Translations, choices of signed orientation, and bounded shifts of the base in $w$ change at most the constant. The estimate is uniform in the time coordinate.

Let $F_p=\sqrt\beta\,\operatorname{Im}(L_xU_pL_x^{-1})$ be the rooted three-color curvature and $F(g)$ its pairing with a real colored test. The first plaquette moment gives $\|F_p\|_2\le C$. For a cochain $h$ write $\|h\|_{1,\sqrt w}=\sum_x\sqrt{w(x)}|h(x)|$, including the sum over orientations. Applying (2) to the short prefixes in the cube identity and the one-link Haar variation gives, for finite $k,h,v$ of degrees three, one and two,
$$
 \mathbb E|F(d^*k)|\le C\beta^{-1/2}\|k\|_{1,\sqrt w}, \tag{3}
$$
$$
 \left|\mathbb E[F(dh)e^{iF(v)}]-i\langle dh,v\rangle\mathbb E e^{iF(v)}\right|
 \le C\beta^{-1/2}\left[
 \|h\|_{1,\sqrt w}(1+\|v\|_\infty)
 +\sum_p |v_p|\sum_{e\in L_{x(p)}}|h_e|\right]. \tag{4}
$$

In (3) the six cube face words multiply to the identity in the ordered telescoping cycle. Products containing at least two face deficits have expected norm $O(\beta^{-1})$ by Cauchy–Schwarz and boundedness of every other factor. Removing a one-link conjugation from a scaled face costs at most $2\|1-U'_e\|_2\|F_p\|_2$ for the rooted link $U'_e$ in (2). These are all the errors in (3).

For (4), if the root path to a varied link traverses that link, replace its traversal by the three other sides of one plaquette. This costs $O(\beta^{-1/2})$ in $L^2$ and makes the generator independent of the variable of integration with other links held fixed. In each incident face the insertion involves at most four rooted links and this detour. A backward occurrence includes the inverse varied link in its prefix and has negative incidence. Equation (2) bounds the discrepancy of the inserted generator from its fixed color by $C\sqrt w/\sqrt\beta$ in $L^2$. Pairing it with $F_p$ gives the same bound in $L^1$ for the action derivative. For the direct derivative of the curvature there is also one unscaled face deficit of size $O(\beta^{-1/2})$ in $L^2$. At most six faces meet each link. The derivative of the conjugating path contributes at most $2|h_e||F_p|/\sqrt\beta$ for each traversal. Summing it with the original test $v$ gives exactly the incidence sum in (4). These comparisons take place after passing the finite-support Haar identities to the fixed-coupling state. [Cube word, signs and Haar variation](../../../../central-quotients/tangent-curvature/periodic-limit/rate/ward.md)

## Comparison with the Gaussian packet

Use A4’s spatial tent or B4’s fourfold-smoothed spatial packets. The test $g$ has only face orientation $12$. It is a sum of one or two packets at arbitrary times with color vectors of total norm $Y$. Each profile before its third stride-$R$ spatial difference has $\ell^1$ norm $O(R^2)$, supremum $O(1/R)$, and spatial support within $C_dR$ of the time axis. The same bounds, with harmless constants, hold after that difference. In the following norm estimates the color amplitudes have been included. [Tent and observable](../README.md) · [Displaced profiles](../../../../transfer-operator/periodic-time/packet-bands/proof.md)

For $K=I-\Delta/16$, $S_M=\sum_{l=0}^{M-1}K^l/16$, put $h=d^* S_Mg$, $k=d S_Mg$, $b_M=K^Mg$. The finite Hodge identity is $g=dh+d^*k+b_M$ and $dh=P(g-b_M)$ for the projection $P$ onto the closure of exact two-cochains. The established spatially weighted bounds give
$$
 \|h\|_{1,w}+\|k\|_{1,w}\le C_d YR^4,\quad
 \|h\|_\infty\le CY,\quad
 \|b_M\|_1\le CYR^5(1+M)^{-3/2}.
$$
The unweighted sum $\|h\|_1+\|k\|_1$ is at most $C Y R^3$. For $l<R^2$ apply one heat-kernel difference, giving a term $CYR^2(1+l)^{-1/2}$. For $l\ge R^2$, expand the three long differences into at most $R^3$ translates of three unit differences. Four heat-kernel differences now give a term $CYR^5(1+l)^{-2}$. Summing each range gives $O(YR^3)$. The constants are independent of $M$ and time separation. Cauchy–Schwarz on the joint finite list of absolute coefficients of $h$ and $k$ interpolates between this bound and the spatially weighted one, yielding
$$
 \|h\|_{1,\sqrt w}+\|k\|_{1,\sqrt w}\le C_d Y R^{7/2}. \tag{5}
$$
[Weighted summations](../comparison.md) · [Heat kernel difference estimates](../../../../central-quotients/tangent-curvature/periodic-limit/rate/heat.md)

Use $v=zg$, $0\le z\le1$, in (4). Since $h=d^*S_Mg$ has only spatial components $1,2$, all time trunks in the incidence sum contribute zero. Each remaining path has $O_d(R)$ steps. The incidence sum is at most $C_d R\|h\|_\infty\|g\|_1\le C_d Y^2R^3$. This holds also for coincident times. The direct term involving $\|v\|_\infty$ is $O_d(Y^2R^{5/2})$. For $\phi(z)=\mathbb E e^{izF(g)}$, decompose the prefactor in $\phi'$ using the Hodge identity. Apply (3)–(5) and $\mathbb E|F(b_M)|\le C\|b_M\|_1$, then send $M$ to infinity at fixed $R,g,\beta$. The drift converges because $|\langle P b_M,g\rangle|\le\|b_M\|_2\|g\|_2$. This gives
$$
 |\phi'(z)+z\|Pg\|_2^2\phi(z)|\le C_d(Y+Y^2)R^{7/2}/\sqrt\beta.
$$
The integrating kernel up to $z=1$ has modulus at most one. Integrate the resulting characteristic-function comparison against independent Gaussian Fourier colors with covariance $2s I_3$ for the observables $O_i=\exp(-s|X_i|^2)$, $s>0$. Do the same for their individual means. Boundedness of the observables and the finite first two color moments give for the centered correlation matrices
$$
 \sup_{\mu,\,n\ge0}\left|B^{\rm Wilson}_{ij}(n)-B^{\rm free,R}_{ij}(n)\right|
       \le C_{d,s} R^{7/2}/\sqrt\beta. \tag{6}
$$
Here $n$ ranges over integer lags, the free curvature has covariance $P$, and the diagonal entry at zero lag is a variance.

## A lattice energy scale

For the tent at $s=1$ the limiting free connected reading satisfies $B(1)>B(2)>0$ at rescaled times one and two. In (6) take the largest even $R\le c\beta^{1/7}$. The error is at most $C_{1,1}c^{7/2}$. For sufficiently small fixed $c$ and then all sufficiently large $\beta$, the actual reading at lag $R$ exceeds a uniform $b_0>0$. The transfer bound $b_0\le e^{-mR}\operatorname{Var}(O)\le e^{-mR}$ proves the stated upper bound. The difference at lags $R,2R$ similarly gives positive weight in a band bounded away from both zero and infinity in rescaled energy. [Free integral, transfer bounds and scalar band argument](../README.md)

For the assertion with any fixed $d$ and $(a,b)$, use B4’s continuum matrix measure and its continuous nonnegative test supported strictly inside $(e^{-b},e^{-a})$. The free limiting matrix for the test has smallest eigenvalue $\lambda>0$. Approximate the test uniformly by one fixed polynomial with total matrix approximation error less than $\lambda/4$ in the two measures together. Its finitely many moments are readings at $0,R,2R,\ldots$. Equation (6) bounds the matrix error by $d C_{d,s}(\sum_m |a_m|)c^{7/2}$ for polynomial coefficients $a_m$, plus a free-lattice discretization error that tends to zero. Choose $c$ and then the coupling threshold to make the sum smaller than $\lambda/4$. The positive-energy band projection then dominates the tested matrix and gives $\eta=\lambda/2$. The constants may depend on the number of probes and the selected band. Along $R\to\infty$ with $R^7/\beta\to0$, the same moment comparisons yield weak convergence of the rescaled packet spectral measures against continuous functions of $e^{-RE}$. The estimates give no comparison at the actual correlation length. [B4’s free matrix, rank and projection proof](../../../../transfer-operator/periodic-time/packet-bands/proof.md) · [Formal and finite checks](checks.md)
