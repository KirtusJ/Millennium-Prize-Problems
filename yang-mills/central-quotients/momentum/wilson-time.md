# Carrying the joint momentum measure to the Wilson time regulator

At fixed spatial mesh the \(SU(2)\) Hamiltonian momentum-band result transfers to a genuine sequence of anisotropic Wilson lattice theories with growing spatial boxes and shrinking temporal spacing. B4's explicit time schedule already suffices for the **entire joint momentum measure**. Although each normalized Fourier sum can have operator norm of order \(\sqrt N\), spatial Parseval controls the average error without a factor of \(N=L^3\). This uses the zero-temperature Wilson transfer vacuum at each regulator.

## The time and vacuum inputs

Use B4's unit-round convention \(H=-(2\kappa_B)^{-1}\sum_e\Delta_e+\lambda\sum_p(1-x_p)\). The Wilson couplings at temporal spacing \(a\) are \(\beta_t=\kappa_B/a\) and \(\beta_s=a\lambda\). In the half-speed convention of the adjoint refinement, \(\kappa=2/\kappa_B\). Let \(T_a\) be B4's positive injective physical transfer, \(\widehat T_a=T_a/\|T_a\|\), and \(Q_a=-a^{-1}\log\widehat T_a\) defined by spectral calculus. Both \(Q_a\) and \(Q=H-E_0\) act on the same finite-box Gauss-law Hilbert space. The metric and magnetic coefficient must coincide on both sides. [B4's comparison](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/10820b4698c3554026244c0cbcf1602f1b9dbdd3/yang-mills/transfer-operator/joint-cutoff)

For box \(n\), put \(B_n=6\lambda L_n^3,\ c_n=B_n+6/\kappa_B,\ s=2\kappa_B\), and \(d_n=e^{-sB_n}2^{-3L_n^3}/s\). For fixed time unit \(t_0>0\), take
\[
 a_n=\frac{t_0\,2^{-n-8}}{(1+t_0 c_n)^2[1+(t_0d_n)^{-1}]} .
\]
The underlying minorization is on the full link product. If the heat kernel \(h_s(x,y)\) lies between \(m_0=e^{-sB_n}(2/3)^{3L_n^3}\) and \(M_0=(4/3)^{3L_n^3}\), the transformed row \(h_s(x,y)\Omega(y)\,dy/\int h_s(x,z)\Omega(z)\,dz\) dominates \(m_0/M_0\) times \(\Omega(y)dy/\int\Omega\). Subtracting this common measure contracts the oscillation of bounded real functions by \(1-m_0/M_0\). Applying it to an excited eigenfunction divided by the positive vacuum gives the finite-box gap floor \(d_n\). This auxiliary floor can vanish with volume. It sets the time resolution even when the physical bulk gap is unknown. [B4's one-link estimate and finite-volume proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/10820b4698c3554026244c0cbcf1602f1b9dbdd3/yang-mills/transfer-operator/joint-cutoff/finite-volume-vacuum.md)

B4's vacuum projections converge pairwise in norm on this sequence. Choose the positive normalized vacua, so \(v_n=\|\Omega_a-\Omega\|\to0\): their real inner product \(z\) is nonnegative, \(v_n^2=2(1-z)\) and \(\|P_a-P\|^2=1-z^2\). Also, for each fixed \(t>0\), \(h_n(t)=\|e^{-tQ_a}-e^{-tQ}\|\to0\). B4 states the latter comparison at \(\lfloor t/a\rfloor\) actual time steps. Writing \(m=\lfloor t/a\rfloor\ge1\), one has \(\sup_{0\le x\le1}|x^{t/a}-x^m|\le1/(em)\) by differentiating in the exponent. This passes to the common physical clock. At \(t=0\) set \(h_n(0)=0\). [Evolution bound and rounding](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/10820b4698c3554026244c0cbcf1602f1b9dbdd3/yang-mills/transfer-operator/joint-cutoff/evolution.md)

## An averaged error bound

Write \(M=\|f\|_\infty\). Use the local centered columns \((1-P)F_{x,j}\Omega\) and their Wilson counterparts \((1-P_a)F_{x,j}\Omega_a\). Each has norm at most \(M\). Their difference has norm at most \(2Mv_n\) by contraction of \(1-P_a\) and \(\|P-P_a\|\le v_n\). Let \(A_k:\mathbb C^3\to\mathcal H\) have their unitary spatial Fourier transforms as columns, and define \(A_{a,k}\) in the same way. Hilbert-space Parseval on the periodic box yields
\[
 \frac1N\sum_k\|A_k\|_{\rm HS}^2,\ 
 \frac1N\sum_k\|A_{a,k}\|_{\rm HS}^2\le3M^2,\qquad
 \frac1N\sum_k\|A_{a,k}-A_k\|_{\rm HS}^2\le12M^2v_n^2 .
\]
Telescope \(A_{a,k}^*e^{-tQ_a}A_{a,k}-A_k^*e^{-tQ}A_k\) across the two columns and then the transfer. The transfers are contractions, and \(\|X^*SY\|_1\le\|X\|_{\rm HS}\|S\|\|Y\|_{\rm HS}\). Cauchy–Schwarz in \(k\) gives
\[
 \frac1N\sum_k\left\|\int e^{-tE}(d\mu_{a,k}-d\mu_k)\right\|_1
 \le 12 M^2 v_n+3M^2h_n(t).
\]
At \(t=0\) this also controls the difference of static matrices. The constants treat all three orientations and any momentum-dependent choice of complex polarization.

## Spectral windows and simultaneous limits

For any continuous function \(\phi\) of energy having a limit at infinity, the same averaged trace-norm difference tends to zero with \(e^{-tE}\) replaced by \(\phi(E)\). Approximate \(\phi\) uniformly by polynomials in \(e^{-t_0E}\), using the compact interval \([0,1]\). The two mean trace masses are each at most \(3M^2\), so the approximation cost is uniform in the number of sites. In particular choose \(0<\ell'<\ell<R<R'\) and continuous \(0\le\phi\le1\), equal to one on \([\ell,R]\) and supported inside \((\ell',R')\). If \(\mu_k([\ell,R])\succeq wI\) on at least \((1-\delta)N\) momenta, then for any fixed \(0<\eta<w\),
\[
 \mu_{a_n,k}([\ell',R'])\succeq(w-\eta)I
 \quad\text{on at least }(1-\delta-o(1))N\ \text{momenta}.
\]
The conclusion follows by Markov's inequality for the trace-norm errors. The enlargement avoids any assumption about atoms at endpoints. For the fixed-mesh Hamiltonian, the earlier theorems give the constants simultaneously for all volumes. [General momentum window](README.md) · [Adjoint choice and constants](adjoint-refinement.md)

The mean Wilson trace mass above \(T\) is asymptotically at most \(3b/[T(1-e^{-1})]\). Use \(1-e^{-E/T}\) as a majorant times \(1/(1-e^{-1})\) on this tail, the averaged comparison at \(t=0,1/T\), and \(1-e^{-E/T}\le E/T\) on the Hamiltonian side. The order is first \(n\to\infty\) at each fixed \(T\), then \(T\to\infty\). This supplies tightness without transferring an unbounded Wilson moment. Test also against any continuous bounded function of momentum. On the compactified momentum–energy space, products of continuous momentum functions and polynomials in \(e^{-t_0E}\) are uniformly dense. Therefore any Hamiltonian subsequence with a joint weak limit gives the **same** Wilson limit, and conversely. Its positive-energy momentum marginal and matrix density bounds are those proved for the Hamiltonian. [Thermodynamic measure argument](infinite-volume.md)

There is a stronger path if individual good momenta must be preserved without losing an additional \(o(N)\) set. Replace \(a_n\) by \(a_n/(1+N)^3\). B4's explicit comparison bounds give \(Nv_n\to0\) and \(Nh_n(t)\to0\) at each fixed \(t>0\). Indeed the vacuum error is proportional to \(a c_n^2/d_n\), and the evolution bound at fixed \(t\) is \(O_t(a^{1/3}+ac_n+a c_n^2)\). Centered columns in any one momentum cost at most \(O(M\sqrt N)\); their differences cost \(O(M\sqrt N\,v_n)\). The resulting Laplace and static comparison errors now tend to zero uniformly in \(k\). On any Hamiltonian good set with a uniform static cap the polynomial approximation above is also uniform there, since the Wilson static matrix is close. This preserves that entire good set in the enlarged band. In a regime with a known volume-independent Hamiltonian gap \(\Delta\), every momentum has the static cap \(b/\Delta\), so the stronger path transfers the band to every momentum.

Both paths leave the spatial lattice spacing fixed for the thermodynamic band conclusion. B4's time estimate compares a finite Wilson box with its own finite Hamiltonian box. Removing the spatial cutoff, proving a common Euclidean-invariant field limit and excluding the full interval of small positive physical energies remain separate obligations.

A finite-dimensional control checks the averaged inequality and its limitation. With 256 spatial labels at \(t=0.7\), the mean trace-norm error was \(0.02698063\), below the \(0.36299453\) bound, while the coherent zero-mode error was \(4.17829241\). Increasing the number of sites from 8 to 256 preserved the mean and multiplied the maximum by 32. [Reproducible control](check_wilson.py)
