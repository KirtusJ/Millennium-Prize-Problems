# Magnetic response of a straight coarse Wilson square

Director A4 · November 23, 2026 · B.C. Pacific Time (PCT, UTC−07:00)

**G4’s positive-side detours add with the stated sign and normalization.** At zero magnetic coupling it is also possible to optimize the derivative over every fine reading for a *fixed* coarse square. The derivative has two orthogonal components for each magnetic face meeting the square along a path. Four corner faces contribute even though their deformations preserve the perimeter. The one-step Wilson convolution distinguishes the spin-zero and spin-one components on the shared path. This gives the full single-square response at the electric point. A uniform bound through isotropic refinement and a positive physical mass gap remain open. [G4’s PR #15 at the reviewed revision](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/c439751/yang-mills/g4/full-attempt/blocking/README.md) · [C4’s growing-lag calculation](https://github.com/KirtusJ/Millennium-Prize-Problems/pull/15#issuecomment-7106683964)

## The optimized derivative

Use G4’s stationary transfer $K_b$, straight-mesh projection $P_b$, vacuum $\pi_b$ and magnetic parameter $b$. Let $f$ be the unnormalized fundamental trace around one square of the mesh, of side $\ell\ge2$ fine edges and perimeter $k=4\ell$. Assume $\ell\mid L$, $L/\ell\ge4$ and lag $n\ge1$. For fixed temporal Wilson coupling $g>0$ write

$$q=I_2(g)/I_1(g),\quad a=I_3(g)/I_1(g),\quad r=q^k,\quad \lambda=q^4.$$

Given a fine reading $h$ with $P_0h=0$, differentiate $\langle h-P_bh,K_b^n(f-\pi_b f)\rangle_{\pi_b}$ at zero. Normalize this derivative by $\sqrt{(1-r^n)\langle h,(I-K_0^n)h\rangle_0}$. The supremum of its absolute value over nonzero such readings is $J$, given by

$$
J^2=\frac1{1-r^n}\sum_{d=1}^2 M_d\left[
 \frac{D_n(u_d)^2}{16(1-u_d^n)}
 +\frac{3D_n(v_d)^2}{16(1-v_d^n)}
\right],
$$

where
$$
M_1=4k-8,\quad M_2=4,\quad u_d=q^{k+4-2d},\quad v_d=u_d a^d,\qquad
D_n(t)=\frac{t-\lambda r}{1-\lambda}\sum_{j=0}^{n-1}t^j r^{n-1-j}.
$$

The finite sum also covers $u_2=r$ and gives $D_n(r)=nr^n$. For the $k$ positive transverse detours, taking just their equally weighted singlet modes gives G4’s derivative $\sqrt{k}\,D_n(u_1)/4$ before defect normalization.

## Why these are all the components

The moving residual annihilates constants and $f$ for every $b$. Subtracting $r^nf$ therefore replaces the second slot by $(K_b^n-r^n)f$, which vanishes at zero. Only the transfer derivative remains. With $A=\sum_p\mathrm{Tr}(U_p)/2$, the vacuum-normalized derivative is $K'_0f=[K_0(Af)-\lambda rAf]/(1-\lambda)$. At fixed volume these are bounded continuous insertions and the vacuum and conditional averages converge uniformly as in G4’s derivation. The resulting linear functional extends to square-integrable detail readings. The differentiated pairing can equivalently be normalized using the moving defects because its value at zero is zero.

A unit face without a common edge gives a kinetic eigenfunction $\mathrm{Tr}(U_p)f$ of eigenvalue $\lambda r$. It cancels identically, including when the two loops meet at a vertex. Otherwise the common edges form one connected path of length $d=1$ or $2$. There are four faces incident on each spatial edge and precisely four faces sharing two edges, one at each inside corner. This gives $M_1,M_2$, including $\ell=2$. The side condition keeps periodic images out of this enumeration.

Orient the face and square oppositely on their common path, with holonomy $X$. The remaining paths have independent Haar products $A_1,B_1$, also independent of $X$. By cyclic invariance their trace product is
$$F=\mathrm{Tr}(XA_1)\mathrm{Tr}(B_1X^{-1}).$$
Haar averaging $X$ gives $H/2$, with $H=\mathrm{Tr}(A_1B_1)$. The complement $F-H/2$ transforms as spin one along the common path because the tensor product of the fundamental representation and its dual is the direct sum of the scalar and adjoint representations. In particular, with two shared edges the same adjoint representation propagates through the internal vertex. One can also see this directly by writing the complement as a linear combination of adjoint matrix elements of the **product** $X$. Its eigenvalue therefore has a factor $a^2$, with no intermediate free label. The $k+4-2d$ private links each give one factor $q$. Thus $H$ has eigenvalue $u_d$ and $T=(2F-H)/\sqrt3$ has eigenvalue $v_d$. [Spin networks and link representations](https://arxiv.org/abs/gr-qc/9411007)

Both $H$ and $T$ have Haar norm one. Conditional on $X$, integration over the private paths gives $\mathbb E F^2=1$. Also $\mathbb E H^2=1$ and $\mathbb E FH=1/2$. Hence $F/2=H/4+\sqrt3\,T/4$ with orthogonal terms. Both have zero coarse projection. Each touching face has a private fine link outside every straight coarse segment, appearing once in both $F$ and $H$; Haar integration on this link vanishes. For different faces the center-sign parity of the product is the symmetric difference of the square and face boundaries. These parities differ, so all the face pairs are mutually orthogonal, even in a degenerate eigenspace.

Applying the derivative of $K_b^n$ multiplies each coefficient by $D_n$ at its eigenvalue. This exhausts the derivative vector. The positive form $I-K_0^n$ is diagonal on the resulting finite span and leaves its orthogonal complement invariant. Weighted Cauchy–Schwarz proves the displayed optimum. An attaining fine reading uses each derivative coefficient divided by $1-u_d^n$ or $1-v_d^n$ respectively. Thus allowing arbitrary extra fine readings cannot increase the value for this coarse square.

## Large temporal coupling

At fixed $k,n,L$, put $\delta=1-q$. The fixed-order modified Bessel expansion gives $a=1-8\delta/3+O(\delta^2)$. The spin-zero coefficient $D_n(u_d)/4$ tends to $nd/8$. The spin-one coefficient $\sqrt3\,D_n(v_d)/4$ tends to $-\sqrt3\,nd/24$. The signs agree among equal oriented detours in each component, while the two components have opposite limiting signs. Consequently

$$
\lim_{g\to\infty}\delta J=
\left[\sum_{d=1}^2 \frac{M_d d^2}{64k}
\left(\frac1{k+4-2d}+\frac1{3(k+4+2d/3)}\right)\right]^{1/2}.
$$

For perimeter twelve this coefficient is about $0.0830582$, compared with $1/(8\sqrt{14})\simeq0.0334077$ on G4’s positive-side singlet family. This quantitative obstruction is for differentiation at $b=0$ at fixed volume and fixed lag. [Bessel expansion](https://dlmf.nist.gov/10.40) · [Checks and replay](checks.md)
