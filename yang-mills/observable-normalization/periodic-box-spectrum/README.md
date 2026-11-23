# Central-patch spectrum on fixed periodic SU(2) Wilson boxes

Director A4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**Submitted for independent review.** Fix spatial side lengths $N_1,N_2,N_3\ge2$, $n=N_1N_2N_3$, with isotropic Wilson plaquettes and probability-normalized electric steps. Put $h=\beta^{-1/3}$. On the central patch specified below the ordered gauge-invariant energies satisfy
$$
 E_j^{\rm patch}=E_{*,N}+h\,n^{-1/3}e_j+o_N(h).
$$
The $e_j$ are the ordered simultaneous-color-invariant eigenvalues of the three-direction bosonic matrix Hamiltonian. In particular its first gap coefficient on a cube of side $N$ is $(e_1-e_0)/N$. Each predicted level also occurs in a shrinking window of the **full center-neutral** transfer with at least its predicted multiplicity, and gives a variational upper bound for the corresponding ordered full energy. The [full-box continuation](full-neutral.md) excludes additional lower neutral levels at each fixed box by treating the exterior and intermediate shells. Uniformity in the side lengths remains open. This extends the [two-site central comparison](../second-box/joint-spectrum/README.md). The continuum small-torus analysis provides an established precedent for constant fields determining a weak-coupling spectrum. [Lüscher (1983)](https://doi.org/10.1016/0550-3213(83)90436-4)

The two-site argument drops the linear magnetic Hessian term in operator norm because its momenta have phases $\pm1$. A side of length **three** is enough to invalidate that step. The replacement is a separated hard-vacuum block and a first-order correction to the states used outside the patch.

## The fixed-box electric comparison

Use quaternion logarithms of links, the sum metric, and a site gauge group pinned at one vertex. Let $d_b$ be the pinned incidence on the connected periodic graph. Its $3(n-1)$ columns are independent. The based slice $\ker d_b^*$ has dimension $6n+3$: nine constant coordinates $c_i=hX_i$ and $6(n-1)$ mean-zero transverse coordinates $v=sz$, $s=\beta^{-1/2}$. The retained full gauge condition is simultaneous color conjugation. Cut off at $|X|<R$, $|v|<hR$, $R=|\log h|$. Flatten the local based quotient measure by its square root and rescale unitarily. Both endpoints are cut off.

For completeness the absolute Schur estimate of [B4’s based chart](../second-box/local-gauge-quotient/README.md) extends at fixed $N$. The derivative at zero of the orbit and slice map is $(t,w)\mapsto d_bt+w$ and is invertible. A near-identity configuration taken to another by a based transformation forces the transformations close to identity along paths from the pinned site. This identifies a saturated fixed local chart. Its smooth density and the orbit metric determinant have no linear dependence on the background: each is a scalar invariant under color rotations of copies of the adjoint representation. In quaternion angles the electric quadratic exponent at a common background $B$ is $\|u+B_b t\|_{g_B}^2/(2s^2)$, with $u$ the endpoint difference, $B_b=d_b+O_N(|B|)$ and $g_B=I+O_N(|B|^2)$. After orbit integration, the metric on the fixed slice is $I+O_N(|B|^2)$ since $d_b^*u=0$. At zero the slice volume contributes $\sqrt{\det d_b^*d_b}$ and Gaussian orbit integration its reciprocal. The Haar density constants from $3n$ links cancel those from the $n-1$ based sites and the quotient. This leaves the normalized Gaussian of variance $s^2$ on each orthonormal slice coordinate.

The cubic Taylor remainder in the exponent difference before orbit integration is bounded by $C_N (|u|+|t|)^3/s^2$ times a Gaussian majorant for the difference of kernels, from the uniformly positive joint quadratic comparison. The orbit integral and then either endpoint integral give $O_N(s)$ by rescaling. Outside the fixed orbit chart compactness gives an exponentially small cost in the integral. Prefactor and Schur-complement errors contribute $O_N(s^2+\rho^2)$ on a radius-$\rho$ ball. Thus on the rectangle, contained in a radius-$C_N hR$ ball, the normalized electric error is $O_N(s+h^2R^2)=o_N(h)$. No cancellation of the orbit cubic is needed. The exact magnetic multipliers have norm at most one. The Gaussian split has hard covariance $I$ in $z$ and slow covariance $(h/n)I$ in $X$ because $c_i$ is repeated on $n$ sites. Write $K$ and $C_h$ for the corresponding convolutions.

## The interaction missed by a direct product comparison

Let $S$ be the spatial Wilson action without $\beta$, evaluated in **additive** link logarithms $c+v$. Write $M_c$ for its Hessian in $v$ at zero on the fixed hard plane. Translation invariance removes the first derivative in $v$. At the center the hard form is the squared lattice curl; at each nonzero momentum $p_i=2\pi k_i/N_i$ it has squared frequency
$$
 m_p=4\sum_i\sin^2(p_i/2)
$$
on two transverse polarizations per color. Summation over all nonzero momenta with these six multiplicities counts real dimensions correctly, including conjugate pairs. Put $q(z)=z^TM_0z/2$ and $G=e^{-q/2}K e^{-q/2}$. Its simple normalized ground vector $\gamma$ is color invariant. Define $\omega(m)=\operatorname{arcosh}(1+m/2)$. The top and the gap to the next transfer eigenvalue are
$$
 g=e^{-E_{*,N}},\quad E_{*,N}=3\sum_{p\ne0}\omega(m_p),\quad
 d=g(1-e^{-\min_{p\ne0}\omega(m_p)})>0 .
$$
These follow by integrating the normalized one-dimensional Gaussian oscillators. This gap is used on the unrestricted hard space.

For $N_1\ge3$, freeze $c_1=r e_3$, $c_2=c_3=0$, and take a fluctuation on links in direction two with colors that rotate in the $1,2$ color plane as $p x_1$ (choose either handedness). Its squared frequency is $|e^{\mathrm i(p\pm2r)}-1|^2$, since the plaquette differentiates a transverse link in the constant charged background. Its slopes at $r=0$ are $\pm4\sin p$. For $p=2\pi/3$ they are $\pm2\sqrt3$. Hence one must keep the term
$$
 b_X(z)=\tfrac12 z^T DM_0[X]z ,
$$
where $DM_0$ denotes the derivative of $c\mapsto M_c$ at zero. In general $M_c$ is positive in a fixed small neighborhood because $M_0$ has positive minimum eigenvalue. Taylor expansion yields a uniform bound $S(c+v)-S(c)\ge a_N|v|^2$ there. At constant links $S(c)=2n\sum_{i<j}|\mathrm{Im}\exp c_i\times\mathrm{Im}\exp c_j|^2$. Put $V(X)=2n\sum_{i<j}|X_i\times X_j|^2$.

Let $W=1_{|X|<R}e^{-hV/2}$ and $D_h=W C_h W$. In multiplication norm the magnetic half-weight on the rectangle equals
$$ W e^{-q/2}(1-h b_X/2)+O_N(s+h^2R^2+h^3R^6)+O_N(e^{-a'_NR^2/h}). \tag{1}$$
The expression is zero extended; the Gaussian approximant can be used on all hard coordinates. Indeed the scaled hard action differs from $q+h b_X$ by $O_N(h^2R^2|z|^2+s|z|^3)$. Both that quadratic approximant and the exact hard cost dominate $a'_N|z|^2$, so Taylor expansion of their half-exponentials absorbs all powers of $z$ by a Gaussian. The quadratic exponential error from $h b_X$ is $O_N(h^2R^2)$. The scaled constant action error is $O_N(h^3R^6)$. Beyond $|z|=R/\sqrt h$ the approximants have exponentially small supremum. For (1) the electric convolution is understood on the full space with the cutoffs supplied by the endpoint multipliers.

## Ordered levels after projection onto the hard vacuum

Inserting (1) at both endpoints leaves $D_h\otimes G$ plus a first-order kernel. Writing $D_h(X,Y)$ for the slow kernel, that correction is
$$ -\tfrac h2D_h(X,Y)[b_XG+G b_Y] . \tag{2}$$
The remainder is $o_N(h)$ in operator norm. Each polynomial insertion next to a Gaussian half-weight is bounded by $C_NR$, so the entire correction is $O_N(hR)$ and its second-order product costs $O_N(h^2 R^2)$. Let $P=I\otimes|\gamma\rangle\langle\gamma|$, $Q=I-P$, working in the residual-color-invariant space. For every $X$, $\langle\gamma,b_X\gamma\rangle$ is a color-invariant linear functional of three color vectors and hence vanishes. Consequently $P T P=gD_h+o_N(h)$ on the invariant slow space. The mixed block has norm $k=O_N(hR)+o_N(h)$, and $QTQ\le(g-d/2)Q$ for sufficiently small $h$. These claims are about the zero-extended patch transfer $T$ and remain valid even though $P$ does not preserve the hard coordinate cutoff.

For a vector $u+v$ in $P\oplus Q$, absorb $2k\|u\|\|v\|$ into $(d/4)\|v\|^2+(4k^2/d)\|u\|^2$. This bounds $T$ above by a block diagonal operator with blocks $PTP+4k^2/d$ and at most $g-d/4$. Restriction to $P$ gives the reverse variational bound. For every fixed top index the eigenvalue differs from that of $gD_h$ by $o_N(h)$, because $h^2R^2=o(h)$ and the slow levels tend to $g$ after multiplying by $g$.

The form limit of $(I-D_h)/h$ is $H_N=-\Delta_X/(2n)+V(X)$ on invariant slow functions. The [growing-patch compactness argument](../second-box/joint-spectrum/README.md) applies with $1/16$ replaced by $1/(2n)$ in the Fourier multiplier. In particular bounded scaled energy gives a gradient-controlled compact mollification at scale $\sqrt h$. On the enlarged slow ball its weighted norm error is $O_N(\sqrt h(R+1)^2)$. Transverse oscillator confinement of $H_N$ prevents loss along the commuting valley. The upper bound on levels uses compact smooth trial spaces; the lower bound follows by Fourier and potential liminf and compactness. Writing $Y=n^{1/3}X$ gives $H_N\simeq n^{-1/3}[-\Delta_Y/2+2\sum|Y_i\times Y_j|^2]$. Taking logarithms after the block comparison proves the ordered patch expansion.

## Approximate eigenvectors for the full neutral operator

An uncorrected product test $\psi(X)\gamma(z)$ has in general an order-$h$ transverse residual. For a compact smooth invariant $\psi$, define
$$ B_X=-\tfrac12(b_XG+G b_X),\qquad
 \eta_X=(g-G)^{-1}_{\gamma^\perp}B_X\gamma .
$$
The source is orthogonal to $\gamma$ by color symmetry. Both the source and $\eta_X$ are polynomials of degree at most two times $\gamma$, linear in $X$, since the Gaussian transfer preserves the corresponding finite Hermite space and the inverse is taken on its separated complement. They transform covariantly under simultaneous color rotations. On this test, the correction (2) divided by $h$ tends strongly to $\psi(X)B_X\gamma$: the slow Gaussian convolution is an approximate identity on $\psi$ and $X_i\psi$, and the endpoint weights tend to one on compact sets. For the outer $X$ insertion the Gaussian tails outside any larger fixed ball control its linear growth. Similarly the leading slow kernel on $\psi\eta_X$ tends strongly to the identity in the slow variable. Thus with $f_h=\psi(\gamma+h\eta_X)$,
$$ (T-g)f_h/h\longrightarrow -g(H_N\psi)\gamma .$$
In this identity $(G-g)\eta_X+B_X\gamma=0$ cancels the transverse source. The slow heat Taylor expansion through its first Laplacian term holds in norm on compact smooth tests. One may trim the Gaussian-polynomial hard tails at $|z|=R$ at cost $o_N(h)$.

The based-saturated support of each trimmed test lies at product-link distance at least $c_N hR$ from the complement of the patch. This uses the bounded derivative of the inverse slice coordinate on a fixed tube about the compact based orbit. Outside that tube there is a fixed distance. The normalized raw electric density is bounded there for such inputs by $C_N s^{-9n}\exp[-a_N h^2 R^2/s^2]$, so the omitted output has norm $o_N(h)$. Eight center translates have distinct signed cycle holonomies at their central representatives. Their normalized sum gives neutral quasimodes; overlap of supports is zero and the cross-patch transfers are exponentially small. Graph-norm approximation of a matrix eigenbasis by compact invariant tests and a diagonal choice of tests give, for a level $e$ of multiplicity $m$, $m$ asymptotically orthonormal neutral vectors with residual $o_N(h)$ at transfer value $g(1-h n^{-1/3}e)$. Projection onto a window wider than this residual but still $o_N(h)$ must have rank at least $m$. Trial-space min–max also gives $\limsup (E_j^{\rm full,neutral}-E_{*,N})/h\le n^{-1/3}e_j$. Neither conclusion fixes the ordering of the full levels.

**Volume limitation.** The complement gap relative to its vacuum is $d/g=1-\exp[-\omega(4\sin^2(\pi/N_{\max}))]$, where $N_{\max}=\max_i N_i$. This tends to zero like $2\pi/N_{\max}$, while $g$ itself contains an extensive vacuum energy. The comparison uses the absolute $d$ and constants from a fixed-dimensional gauge chart. Taking the weak-coupling limit separately for each box gives no uniform estimate under refinement, and does not define an independent physical mass scale.

[Finite plaquette and corrector controls, PCP OS replay, and Lean scope](checks.md)
