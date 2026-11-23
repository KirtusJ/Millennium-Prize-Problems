# Transfer on quotient histories and a test for single-slice averaging

## Which spectral bound passes to an exact quotient?

Let \(q\) map cover histories to quotient histories, \(\nu=q_*\mu\), and suppose \(q\) intertwines time reflection and positive time translation. Require the pullback of each admissible positive-time test to remain admissible. For the Osterwalder–Schrader form, change of variables gives
\[
 (F,G)_{\nu,\mathrm{OS}}=(F\circ q,G\circ q)_{\mu,\mathrm{OS}}.
\]
Pullback respects null vectors and extends to an isometry \(V:\mathcal H_\nu\to\mathcal H_\mu\). Its closed range contains the cover vacuum represented by the constant history. When both systems reconstruct a selfadjoint transfer semigroup, time-translation equivariance gives \(VT_\nu(s)=T_\mu(s)V\). The range reduces each \(T_\mu(s)\) by selfadjointness. A bound \(\|T_\mu(s)g\|\le e^{-s\Delta}\|g\|\) on the cover vacuum complement therefore holds on the quotient vacuum complement with the same time normalization. A nonzero test in the latter complement is a separate requirement. This extends G4's finite reflection-positivity comparison. [G4’s argument](../../g4/cross-lane-review.md) · [Osterwalder and Seiler](https://doi.org/10.1016/0003-4916(78)90039-8) · [Lüscher](https://doi.org/10.1007/BF01614090)

## A two-step defect

On a single time slice, let \(P\) be the orthogonal projection onto functions of the quotient links under product Haar measure. It averages over the finite central subgroup independently at each spatial edge. For a bounded selfadjoint cover transfer operator \(T\),
\[
 PT^2P-(PTP)^2=PT(1-P)TP,\qquad
 \langle f,[PT^2P-(PTP)^2]f\rangle=\|(1-P)Tf\|^2
 \quad(Pf=f).
\]
Equality for every such \(f\) holds exactly when \(T\) preserves \(\operatorname{ran}P\), equivalently when \(PT=TP\). For \(T=e^{-sH}\), \(s>0\), \(H\) selfadjoint and bounded below, spectral calculus then makes \(P\) a reducing projection for \(H\) as well. This test concerns a proposed description obtained by averaging signs at each slice. The OS isometry above uses complete histories.

Take the finite spatial Hamiltonian \(H=K+c-\sum_p\lambda_p t_p\) on product Haar \(L^2\), where \(K\) is a nonnegative sum of bi-invariant link Laplacians, \(c,\lambda_p\) are real, and \(t_p=\tfrac12\operatorname{Tr}(U_{\partial p})\) for \(SU(2)\). The graph and plaquette list are finite. Take simple plaquettes with nonzero, pairwise different mod-two boundaries. Gauge-invariant tests and the corresponding subspace are allowed. \(K\) commutes with \(P\), since central link multiplication is an isometry. Under edge signs each \(t_p\) gains its own nontrivial character. For a smooth \(Pf=f\), putting \(T=e^{-sH}\) and writing \(D_s(f)\) for the form above gives
\[
 \lim_{s\downarrow0}s^{-2}D_s(f)
   =\|(1-P)Hf\|^2
   =\int |f|^2 \sum_p\lambda_p^2 t_p^2\,dU .
\]
The first equality uses the strong first derivative of the semigroup on \(D(H)\). For the second, \((1-P)Hf=-\sum_p\lambda_p t_p f\), and integration over the edge signs kills all cross terms. Thus \(PHP\) acts as \(K+c\) on these tests, while a cover excursion through the omitted subspace returns at order \(s^2\).

For \(f=1\), every simple plaquette product is Haar when its other links are integrated or held fixed and a single incident link is integrated. Character orthogonality gives \(\int t_p^2\,dU=1/4\). Consequently the coefficient is \(\sum_p\lambda_p^2/4\), positive as soon as one coupling is nonzero. The constant is a Haar test. In the one-square model the Haar-centered, unit-norm adjoint test \(f=4t^2-1\) gives coefficient \(\lambda^2/2\). Indeed \(2t\,f=\chi_1+\chi_3\), where \(\chi_n\) denotes the \(SU(2)\) irreducible character of highest weight \(n\).

## Other finite central kernels

Let \(Z\) be a finite central subgroup of a compact group, with an irreducible unitary representation \(\rho\) of dimension \(d\). Write \(\tau_p=d^{-1}\operatorname{Tr}\rho(U_{\partial p})\) and use \(\operatorname{Re}\tau_p\) in the potential. If the central character of \(\rho\) is trivial, each potential term descends and commutes with \(P\). Otherwise the independent edge variables induce boundary characters \(\eta_p\) of \(Z^{E}\). Assume they are all nontrivial and pairwise different up to inversion. The same first-derivative argument gives the coefficient
\[
 \int |f|^2\sum_p\frac{\lambda_p^2}{2}
 \left(|\tau_p|^2+\mathbf 1_{\eta_p^2=1}\operatorname{Re}(\tau_p^2)\right)\,dU.
\]
Indeed \(\operatorname{Re}(\eta_p\tau_p)=(\eta_p\tau_p+\bar\eta_p\bar\tau_p)/2\). Averaging a product of characters over the edge center retains exactly its trivial terms. Repeated or inverse boundary characters require keeping the corresponding cross terms. For the fundamental representation of \(SU(3)\) with \(Z=\mathbb Z_3\), the second term vanishes and \(\int|\tau_p|^2\,dU=1/9\) for a simple plaquette. The constant-test coefficient becomes \(\sum_p\lambda_p^2/18\). [Finite character checks](check.py)

This Hamiltonian calculation specifies the regulator and Haar space used in the projection. An identification of any particular four-dimensional isotropic Wilson transfer matrix with \(e^{-sH}\) would require a separate argument. For a solvable question about the accessible sector of a continuous-time single-square model, the projected history can be calculated exactly. [Observable sector of the one-plaquette rotor](rotor.md)
