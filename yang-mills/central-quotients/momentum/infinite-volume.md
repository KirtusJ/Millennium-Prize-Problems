# What survives in a thermodynamic subsequence

Keep the spatial mesh, \(\kappa,\lambda,G,v,f\) fixed. For \(L\to\infty\) put the finite-volume momentum measures on the common Brillouin torus \(\mathbb T^3\) and energy half-line,
\[
 \nu_L=N^{-1}\sum_k\delta_k\otimes\mu_k .
\]
Use probability Haar measure \(dk\) on this torus. Every sequence has weakly convergent subsequences of these finite positive matrix measures. For **every** such limit \(\nu\) the momentum marginal at strictly positive energies is absolutely continuous with respect to \(dk\). With \(R=2\sqrt{c/a}\) as in the [finite-volume theorem](README.md), the density of \(\nu(dk,(0,R])\) is at least \(3a/(4R)\,I_3\) almost everywhere. At least \(1-\delta\) of the Brillouin torus, in Haar measure, retains the matrix lower bound \(a/(2R)\,I_3\) on the common closed energy interval \([\ell,R]\) specified there. These conclusions allow the sets of good finite-volume momenta to vary arbitrarily with the box.

**Passage to a common measure.** The trace masses are bounded by \(C_0\) and the energy tails by \(3b/T\) above \(T>0\). Tightness and positivity give a weakly convergent subsequence, first for the finitely many matrix entries by polarization, with a positive matrix limit. The third moment bounds the tail of the first moment by \(3c/T^2\). For any continuous nonnegative \(h(k)\), weak convergence with continuous energy truncations therefore passes the first moment to the limit. The momentum-grid Riemann sums converge to Haar. Monotone truncation from below gives the upper bound for the third moment as well. As inequalities of measures in the momentum variable,
\[
 aI_3\,dk\ \preceq\ \int E\,\nu(dk,dE)\ \preceq bI_3\,dk,\qquad
                 \int E^3\,\nu(dk,dE)\ \preceq cI_3\,dk .
\]
The first inequality also proves absolute continuity of the positive-energy marginal when combined with its upper bound: for a Haar-null set \(A\), the first-energy integral of the trace over \(A\) is zero. Exhaust \(E>0\) by \(E\ge1/n\). Any singular part of the static momentum marginal can consequently occur only at \(E=0\).

Integrating \(E\le R\mathbf1_{(0,R]}+E^3/R^2\) proves the first density floor. For the closed interval let \(s(k)\) denote the density of the absolutely continuous part of the static trace marginal. It integrates to at most \(C_0\). Take absolutely continuous parts in the measure inequality from \(E\le\ell+R\mathbf1_{[\ell,R]}+E^3/R^2\). Positivity is preserved by this operation, as seen on quadratic forms. Almost everywhere the window density \(W(k)\) satisfies
\[
 R W(k)\succeq(a-c/R^2-\ell s(k)) I_3 .
\]
The set \(s(k)>a/(4\ell)\) has Haar measure at most \(4\ell C_0/a\). This yields the asserted window. One may check the scalar inequalities on a countable dense set of polarizations to use a common full-measure set. If there is a common finite-box gap \(\Delta>0\), the open strip \(0<E<\Delta\) receives zero mass in the weak limit, giving the stronger \([\Delta,R]\) conclusion almost everywhere.

The absolute continuity here concerns **spatial momentum** after integrating positive energy. An energy law at a given momentum may be atomic. A singular zero-energy contribution, several subsequential limits, and a lack of continuum rotational covariance are all compatible with these estimates. The conclusion constructs subsequential two-point spectral measures at fixed spatial mesh. Reconstruction of a continuum gauge field still requires a common limit for its full positive-time test algebra.
