# A time-zero measurement that detects a positive physical energy window

Fix a centered gauge-invariant spatial-slice probe \(A\), with any chosen physical normalization already included. Let \(T\) be the vacuum-normalized positive Wilson transfer, \(b\) the time spacing, and \(v=q(A)\) the time-zero state. Let \(\nu\) be the spectral measure of this state in physical energy \(E=-b^{-1}\log T\), with total mass \(M=\|v\|^2\). A zero-transfer component, if present, can be placed at \(E=\infty\). Choose positive integers \(k,\ell\), and a time-zero gauge-invariant witness \(H\) of positive finite variance, centered as well. In a regulator sequence \(A,H\) can depend on the cutoff. Use the same \(A\) and its normalization at both times within each measurement.

The observed quantity requires just two connected correlations:

\[
 W=\frac{|\mathbb E[\overline H(A_k-A_{k+\ell})]|^2}{\mathbb E|H|^2}.
\]

Since the guard retains \(H\), the same \(W\) is obtained with \(P A_k-P A_{k+\ell}\). The OS state of the difference is \(T^k(I-T^\ell)v\). In the reflected inner product the time-zero witness pairs with this state by ordinary expectation. Cauchy–Schwarz therefore gives

\[
 W\le \int e^{-2kbE}(1-e^{-\ell b E})^2\,d\nu(E).
\]

Both times serve a purpose. The difference suppresses weight approaching zero energy. The positive separation \(kb\) suppresses weight escaping to infinite energy. At the endpoints \(E=0,\infty\) the filter vanishes.

For \(0<d<D<\infty\), put
\[
 a=\max\{(1-e^{-\ell b d})^2,\ e^{-2kbD}\}.
\]
On the complement of \([d,D]\) the filter is at most \(a<1\), and everywhere it is at most one. Integration on the window and its complement gives
\[
             \nu([d,D])\ \ge\ \frac{W-a M}{1-a}.
\]

Thus, if \(kb\to t>0,\ \ell b\to u>0,\ \sup M<\infty\) and \(\liminf W>0\), some single compact interval **strictly inside** \((0,\infty)\) carries uniformly positive weight eventually. Choose \(d\) small and \(D\) large using an upper bound for \(\ell b\) and a positive lower bound for \(kb\) on the tail. The bound survives weak convergence of spectral measures by the closed-set inequality. A single positive correlator without the difference can be saturated by a zero-energy atom. A single equal-time variance can be saturated by escaping energies. The estimates also apply with several witnesses by choosing any linear combination on the plane.

## Testing the criterion on an actual program observable

Specialize C4's magnetic angle between two spatially separated packets to defining SU(2). Use its centered reading \(A=h_r-\mathbb E h_r\) for the time-zero witness as well. Write \(r=1/b\), \(C_r(k)=\langle v_r,T_r^k v_r\rangle\). The numerator is exactly \((C_r(k)-C_r(k+\ell))^2\), and \(M_r=\operatorname{Var}(h_r)\le1\). In the fast regime \(L/(r^3\sqrt{\log(2+r)})\to\infty,\ \beta/(r^{16}\log(2+r))\to\infty\), C4's written theorem identifies the limiting connected measure; its mass near zero is asymptotic to a positive multiple of \(\epsilon^8\). It therefore gives positive mass in \((0,\infty)\). For fixed \(t,u>0\) the limiting correlation difference is the integral of \(e^{-tE}(1-e^{-uE})\), strictly positive on that set. The displayed witness has positive limiting lower bound. The same result holds using the projected readings on the guarded mask. This application depends on C4's fast-trajectory theorem. [C4's trajectory conditions and proof](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/c156809fdae187a97771127698ba8dec8ecd2915/yang-mills/central-quotients/magnetic-smearing/connector)

In C4's other regime \(\beta=o(r)\) with \(L/r\to\infty\), the connected reading of the same angle at every fixed positive physical time tends to zero. For **any** time-zero witness of unit norm, \(W\le C_r(2k)\), since \((1-e^{-\ell bE})^2\le1\). Thus changing the boundary witness or projecting the angle cannot restore a positive signal there. On either trajectory the statement concerns this observable. Finding a probe and witness with \(\liminf W>0\) on a common interacting, physically scale-set trajectory remains open. Even a successful witness proves spectral weight **in** a positive window. A mass gap additionally requires exclusion of all sufficiently small positive energies for the physical theory. [C4's slow-trajectory argument](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/c156809fdae187a97771127698ba8dec8ecd2915/yang-mills/central-quotients/magnetic-smearing/connector/slow.md) · [Jaffe and Witten, §4](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf)

## Rounded times and an exact control

For rounded time steps in the fast-regime application, \(e^{-kbE}\) converges uniformly in \(E\ge0\) to \(e^{-tE}\). Indeed its time derivative has magnitude \(E e^{-sE}\), uniformly bounded for \(s\ge t/2\). The same applies at \(t+u\), and \(M_r\le1\) controls the integration error. On the slow trajectory, positivity lets one squeeze rounded readings between readings at fixed earlier and later physical times. C4's positive low-energy tail in the fast limit also gives weight arbitrarily close to zero. That limiting probe measure is gapless even though the finite-window test succeeds.

The exact control assigns transfer eigenvalues \(0,1/2,1\) respective masses \(1/4,1/2,1/4\). With \(k=\ell=1\) and the probe itself as witness, \(W=1/64\). For the transfer interval \([1/16,15/16]\), corresponding to a compact positive energy interval, the bound certifies mass at least \(1/85\). Its true mass is \(1/2\). The atoms at zero and infinite energy contribute nothing to the measurement. [Exact controls](control.py)

## Comparison with primary literature

- **Wilson locality.** Lüscher and Weisz, §§3.2–3.3, integrate the interior of a time slice after holding its boundary links fixed, using locality of the plaquette action. Our sparse mask yields a product of individual link kernels for the same reason. The spatial plaquette in the plane supplies a quantitative test of when this particular projection preserves the full half-cylinder quotient. Creutz's SU(2) heat-bath construction is the one-link calculation underlying the tilted Haar law. [Lüscher and Weisz](https://arxiv.org/pdf/hep-lat/0108014) · [Creutz](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.21.2308)
- **Site reflection.** Menotti and Pelissetto explicitly treat a reflection plane containing sites in the Wilson theory. That positivity is an input to the physical quotient. The conditional product identity uses the finite-link specification, half-space geometry and invariance of the exterior. [Menotti and Pelissetto](https://doi.org/10.1007/BF01221251)
- **Markov and OS quotient spaces.** Jorgensen, Neeb and Ólafsson, Definitions 2.1–2.2 and Lemma 2.3, realize the OS space on a subspace fixed pointwise by reflection under their Markov condition. Here the exterior retains links on both sides and reflection exchanges their positions. Our exterior retains its own reflected inner product and null space. The induction for the transported transfer uses the usual descent of a positive-time shift through the original OS quotient. [Definitions 2.1–2.2, Lemma 2.3 and §2](https://arxiv.org/pdf/1510.07445)
- **Lattice spectroscopy.** Blossier and coauthors, §2.1, Eq. (2.1), give the positive-transfer spectral representation of slice correlation matrices and optimize combinations of probes with a generalized eigenvalue problem. Here Cauchy–Schwarz bounds a filtered integral from a boundary overlap. Positivity of a measure suffices for the window estimate, including for a continuous spectrum. The physical hypotheses are the scale, total mass bound and a measured or proven overlap with controlled errors. [Blossier et al.](https://arxiv.org/pdf/0902.1265)
