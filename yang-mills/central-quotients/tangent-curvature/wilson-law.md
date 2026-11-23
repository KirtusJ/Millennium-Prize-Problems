# Local equations for the original Wilson curvature

Use the isotropic Wilson probability on a periodic spatial cubic lattice of side $L\ge3$ and periodic time of length $N$, with normalized product Haar measure on every original $SU(2)$ link. Write the group as unit quaternions. Put $x_p=\operatorname{Re}U_p=\operatorname{tr}(U_p)/2$, using positively oriented faces and the Wilson factor $\exp[-\beta(1-x_p)]$. The three standard unit imaginary quaternions have length one. First take $N\to\infty$ at fixed $\beta,L$ to obtain the transfer vacuum. Then take any sequence $\beta,L\to\infty$. Every patch or rooted path in a finite-dimensional distribution is kept fixed in lattice units in this second limit.

## A temporal-face estimate

More generally give the spatial and temporal faces respective couplings $\sigma=\beta a/b$ and $\gamma=\beta b/a$, $0<a\le b$. Let $P=3L^3$ and $z(\gamma)=\int \exp[-\gamma(1-\operatorname{Re}U)]\,dU$. The original periodic partition function is $z(\gamma)^{NP}\operatorname{Tr}_{\rm phys}(T_{\gamma,\sigma}^N)$. Integrating the temporal links supplies the gauge projection on each transfer step. The factor $z^{NP}$ restores the normalization of the one-link kinetic kernel. The normalized one-step operator $T=MKM$ is positive compact with a simple top eigenvalue and norm at most one. Its strictly positive top eigenfunction is gauge invariant. The logarithm of its physical trace per step tends to the log norm by this spectrum and trace class of a fixed positive power. The fixed-box Perron limit also gives the vacuum joint law of any bounded gauge-invariant cylinder observable. Equivalently, continuous cylinder observables in a compact-link subsequential time limit can first be averaged over local gauges. This determines their expectations from the gauge-invariant cylinder law. [Transfer conventions](../../transfer-operator/hamiltonian-time/) · [Original periodic history](../../transfer-operator/periodic-time/)

Let $u_{t,N}$ be the mean of $1-x_p$ for any temporal face. Keeping $\sigma$ fixed, finite-volume Jensen applied to the ratio of Boltzmann weights gives
$$
 \gamma u_{t,N}/2
 \le [\log {\cal Z}_{\gamma/2,\sigma}-\log {\cal Z}_{\gamma,\sigma}]/(NP).
$$
Send $N$ to infinity. The upper transfer norm at $\gamma/2$ is at most one. At $\gamma$ the product-bump estimate gives $-\log\|T_{\gamma,\sigma}\|/P\le C\sigma/\beta$ for sufficiently large $\beta$. In particular
$$
 u_t\le\frac{2}{\gamma}\left(\log\frac{z(\gamma/2)}{z(\gamma)}+C a/b\right).
$$
Integration with the radial Haar density proportional to $\sin^2\theta$, $0\le\theta\le\pi$, gives $c\gamma^{-3/2}\le z(\gamma)\le C'\gamma^{-3/2}$ for $\gamma\ge1$. Integrate over the cap $\theta\le1/\sqrt\gamma$ for the lower bound and use $1-\cos\theta\ge2\theta^2/\pi^2$ for the upper bound. Thus $u_t\le C''/\gamma$. The spatial result is $u_s\le C/\beta$. Both estimates are uniform in $L$. At $a=b$, all six types of faces have $\mathbb E[\beta(1-x_p)]\le C_0$. Spatial rotations and translations, and time translations, give the needed symmetry even though the time extent was taken to infinity first. [Spatial deficit and norm bound](../electric-disorder/wilson-readings.md)

## Rooting and linearizing on a fixed patch

Fix a root at the origin and compatible paths on a spanning tree of $\mathbb Z^4$, for instance paths moving the coordinates in order. At each site use the product along the root path as gauge change; write $U'_e$ for the resulting link. Every tree edge becomes one. At any other fixed edge $U'_e$ is the holonomy around a fixed closed walk. On a sufficiently large torus this walk lifts to a contractible walk and can be expressed as a finite product of conjugated elementary plaquettes and their inverses. Interchanging adjacent perpendicular unit steps and cancelling backtracks gives such an expression. For the bi-invariant angular distance, $d(1,q)^2\le(\pi^2/2)(1-\operatorname{Re}q)$. The triangle inequality and Cauchy–Schwarz therefore give $\mathbb E[\beta d(1,U'_e)^2]\le C_e$ with $C_e$ depending on the walk.

The local vector $A_e^\beta=\sqrt\beta\log U'_e$ is tight. At the single cut point one can choose any logarithm of length $\pi$. The curvature $F_p^\beta=\sqrt\beta\,\operatorname{Im}U'_p$ has $\mathbb E|F_p^\beta|^2\le 2C_0$ at **every** face, since rooting preserves its norm. The difference between scaled logarithm and scaled imaginary part on a given face tends to zero in probability. Taylor expansion of the four-factor plaquette word on bounded sets of $A^\beta$ gives
$$
 F_p^\beta=(dA^\beta)_p+o_{\mathbb P}(1).
$$
Here $d$ is the ordinary oriented cubical coboundary. Tightness removes the truncation. Hence the signed sum around each fixed cube tends to zero. Every subsequential joint limit satisfies $dF=0$ on the countable lattice. Tightness on all finite sets and diagonal extraction yield a joint limit along a subsequence of any sequence. The curvature bound survives by truncation, uniformly in the face.

Two different root paths to a face change its frame by the holonomy of a fixed closed walk, which tends to one by the same estimate. Conjugating a tight $F_p^\beta$ by this holonomy changes it by $o_{\mathbb P}(1)$. This applies jointly to any fixed finite set. The arbitrary gauge at the common root acts by the same global color rotation.

## Haar variation and the limiting identity

For a selected oriented edge $e$, choose a rooted tree avoiding that one edge. Such a choice exists since each lattice edge belongs to a square; a finite reroute and restriction to the finite patch suffice. Root paths for all endpoints, including the neighbors of $e$, are thus independent of the original variable $U_e$. Conditionally on other links, vary this one link so that $U'_e$ is multiplied on the left by $\exp(sX/\sqrt\beta)$, $X$ a fixed imaginary quaternion. This is a left Haar variation by a generator conjugated with a root path independent of $U_e$. It also leaves every other tree-gauged link fixed. Use it under the original finite periodic integral and then pass to the infinite-time vacuum at fixed $\beta,L$. The resulting terms are continuous bounded cylinder functions for these fixed parameters.

For a bounded $C^1$ function $f$ of finitely many scaled imaginary face vectors, with bounded continuous first derivatives, differentiation under Haar gives
$$
 \mathbb E\left[\left.\frac d{ds}f(F^\beta(U(s)))\right|_0\right]
 =\mathbb E\left[f(F^\beta)\sqrt\beta\sum_{p\ni e}D_{e,X}(1-x_p)\right].
$$
The operator $D$ here uses the unscaled generator. Write $\epsilon_{pe}$ for oriented incidence. Differentiating the plaquette word inserts $X$ at a positive occurrence and inserts $-X$ next to the inverse at a negative one. The resulting derivative of $\operatorname{Im}U'_p$ is bounded by $|X|$ and tends to $\epsilon_{pe}X$ in probability on the fixed patch. Cyclic scalar trace gives the **exact** scalar score
$$
 D_{e,X}(1-x_p)=\epsilon_{pe}\langle X,\operatorname{Im}(V_{pe}^{-1}U'_pV_{pe})\rangle.
$$
Indeed, for a positive occurrence written $A U B$ use $V=A$; for a negative occurrence $A U^{-1}B$ use $V=A U^{-1}$. This uses $\operatorname{Re}(Xq)=-X\cdot\operatorname{Im}q$. The short words $V$ tend to one. After multiplication by $\sqrt\beta$ each summand therefore differs from $\epsilon_{pe}X\cdot F_p^\beta$ by a term vanishing in probability. All these scores have uniform second-moment bounds. This gives the uniform integrability needed on the right; the left has bounded first derivatives and bounded insertions. Taking the subsequential limit in the rooted variables gives, by summing the single-edge identities,
$$
 \mathbb E[\partial_{dh} f(F)] = \mathbb E[\langle F,dh\rangle f(F)]
$$
for every compactly supported real three-color one-cochain $h$. The pairing sums over positively oriented cells and Euclidean colors. The avoidance tree may change between edge identities because all its limiting curvature marginals agree with those of the original root tree. [Identification of the limiting law](gaussian.md)
