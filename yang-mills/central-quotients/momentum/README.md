# Positive-energy plaquette weight at spatial momenta

At fixed spatial mesh and finite couplings, a center-neutral plaquette on a periodic cubic lattice has positive spectral weight in a common bounded interval at most spatial momenta. More precisely, one can choose any allowed exceptional fraction \(\delta>0\). The interval and a positive matrix lower bound for the three plaquette orientations are independent of box size. This holds for each compact connected simple gauge group. Where an independent volume-uniform gap is available, a common interval works at **every** momentum. The estimates do not assume spatial clustering.

## What is measured

Let \(G\) be a compact connected nonabelian simple Lie group, choose a bi-invariant metric and normalize Haar measure to one. On the periodic spatial cube with \(L\ge3\) sites per side and \(N=L^3\) vertices, use the continuous-time Hamiltonian
\[
 H=-\kappa\sum_e\Delta_e+\lambda\sum_p v(U_{\partial p}),\qquad \kappa>0,\ \lambda\ge0 .
\]
Take one copy of each elementary unoriented face, with fixed translation-invariant orientations, and a smooth real class potential \(v\), for example \(1-\operatorname{ReTr}\rho/\dim\rho\). The unrestricted ground state \(\Omega\) is smooth, unique and strictly positive by compact ellipticity and positivity improvement. Gauge transformations and translations fix this normalized state. Work in its physical gauge-invariant representation and set \(Q=H-E_0\). These assumptions and time conventions specify a spatially regulated Hamiltonian. [Kogut and Susskind](https://doi.org/10.1103/PhysRevD.11.395) · [B4's time-limit comparison and units](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/6c086a6c4dd605a99869ed8c8c2ae3a1eaa6a2aa/yang-mills/transfer-operator/hamiltonian-time)

Choose any smooth real, nonconstant class function \(f\) invariant under multiplication by the chosen finite central subgroup. The normalized character of the real adjoint representation works for every such \(G\) and every central quotient. Write \(F_{x,j}=f(U_{\partial p(x,j)})\) for the face of normal \(j\) based at \(x\), and center each multiplication operator in the ground state. For \(k\in(2\pi/L)(\mathbb Z/L)^3\) and a unit complex polarization \(u\in\mathbb C^3\), define
\[
 \psi_{k,u}=N^{-1/2}\sum_{x,j} e^{ik\cdot x}u_j(F_{x,j}-\langle F_{x,j}\rangle)\Omega,\qquad
 u^*\mu_k(B)u=\|\mathbf1_B(Q)\psi_{k,u}\|^2 .
\]
Thus \(\mu_k\) is a positive \(3\times3\) matrix measure. The observables are functions of the quotient links already at one time. Their correlations in the exact quotient history equal their cover correlations without estimating a reconstruction map. [Exact quotient sector](../local-response/analytic-groups.md)

## Bounds and consequences

The proof gives constants \(a,b,c>0\), independent of \(L\), such that
\[
 aI\preceq \int E\,d\mu_k\preceq bI,\qquad
 \int E^3\,d\mu_k\preceq cI,\qquad
 N^{-1}\sum_k\operatorname{tr}\mu_k([0,\infty))\le C_0=3\|f\|_\infty^2 .
\]
In particular \(a>0\) holds uniformly in the complex polarization. A cancellation between the gradients of incident faces is the issue that a single-face estimate leaves open. [Local conditional comparison and gradient proof](local-estimates.md) · [Finite range of the cubic moment](third-moment.md)

Every momentum separately also has a lower bound on its full time correlation. For a unit polarization let \(M_j\) denote its scalar moments. Then \(M_2^2\le M_1M_3\le bc\) and \(M_1^2\le M_0M_2\). Thus \(M_0\ge a^2/\sqrt{bc}\) and \(M_1/M_0\le\sqrt{bc}/a\). Jensen's inequality gives \(C_k(t)\succeq e^{-t\sqrt{bc}/a}\mu_k([0,\infty))\) for \(t\ge0\). Isolating an interval separated from zero is a further step. A4 obtains sharper coupling dependence for the fundamental \(SU(2)\) trace. [A4's smeared fundamental estimates](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/e49cee4f36d69be30d041c91e05afe4f7eb49b55/yang-mills/observable-normalization/smeared-plaquettes/moment-bounds)

Take \(R=2\sqrt{c/a}\), \(0<\delta<1\), and \(\ell=\min(R/2,\delta a/(4C_0))\). For at least \((1-\delta)N\) distinct momenta,
\[
                  \mu_k([\ell,R])\succeq \frac{a}{2R}I_3 .
\]
Indeed the scalar pointwise inequality \(E\le\ell+R\mathbf1_{[\ell,R]}(E)+E^3/R^2\) holds for all \(E\ge0\). At most \(\delta N\) momenta have \(\operatorname{tr}\mu_k([0,\infty))>a/(4\ell)\), by Parseval and Markov's inequality. At each remaining momentum the low and high terms each cost at most \(a/4\) in every unit polarization. This proves the matrix bound. The centered zero mode may be among the exceptions.

Each good momentum supplies three independent physical vectors after spectral projection into that energy band. Distinct momenta transform by distinct translation characters, up to the common Fourier sign convention, and hence give mutually orthogonal subspaces. The band therefore contains at least \(3(1-\delta)N\) dimensions. For \(t\ge0,\ s>0\), its contribution to the filtered correlation matrix gives
\[
 C_k(t)-2C_k(t+s)+C_k(t+2s)
   \succeq \frac{a}{2R}e^{-tR}(1-e^{-s\ell})^2 I_3
\]
at those same momenta. A fixed open patch of the dimensionless Brillouin zone contains good momenta in large boxes by choosing \(\delta\) below its normalized volume. [D4's physical-time filter](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/4fdd79bb39e710287e8fd278ce9abfff6177a572/yang-mills/spectral-support/positive-time/vacuum)

There is also a bound at **every** momentum with open lower endpoint, \(\mu_k((0,R])\succeq 3a/(4R)I_3\), by \(E\le R\mathbf1_{(0,R]}(E)+E^3/R^2\). If the same Hamiltonian has a volume-independent lower gap \(\Delta>0\), centering removes its simple ground state and the interval can be replaced by \([\Delta,R]\). Necessarily \(R\ge\Delta\), since the first moment is positive and \(c\ge\Delta^2 a\). B4's fixed-mesh small-interaction regime supplies such a gap for each fixed compact simple group with its stated metric and local perturbation hypotheses. This gives three independent band states at every lattice momentum in that regime. The constants here have no claimed uniformity over all groups or over magnetic-to-electric coupling ratios. [B4's application of the local stability theorem](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/6c086a6c4dd605a99869ed8c8c2ae3a1eaa6a2aa/yang-mills/transfer-operator/hamiltonian-time) · [Yarotsky, Theorem 1](https://arxiv.org/abs/math-ph/0412040)

At fixed mesh every sequence of increasing boxes also has subsequential joint momentum–energy measures. In every such limit the positive-energy momentum marginal is absolutely continuous, and almost every momentum retains a full-rank contribution below the same upper energy. The exceptional-fraction bound persists on the closed positive band. [Thermodynamic limit proof](infinite-volume.md)

## Controls and the continuum question

At \(\lambda=0\) take \(f=\chi_{\rm Ad}/d_{\rm Ad}\). Schur orthogonality gives face variance \(d_{\rm Ad}^{-2}\). Distinct faces are orthogonal by integration over a link private to one of them. The free Laplacian acts on the four incident links with the same adjoint Casimir \(C_{\rm Ad}\), so the exact answer is \(\mu_k=d_{\rm Ad}^{-2}I_3\,\delta_{4\kappa C_{\rm Ad}}\) at every momentum. Its flat dispersion also illustrates how little a finite-cutoff positive band says about rotational invariance after spatial refinement. [B4's free spatial-rotation test](https://github.com/KirtusJ/Millennium-Prize-Problems/tree/6c086a6c4dd605a99869ed8c8c2ae3a1eaa6a2aa/yang-mills/transfer-operator/hamiltonian-time)

A periodic harmonic lattice shows why the exceptional fraction matters. In three dimensions choose \(m_L=L^{-3}\), \(E(k)^2=m_L^2+4\sum_i\sin^2(k_i/2)\), and \(\mu_k=E(k)^{-1}\delta_{E(k)}\), with three independent copies if desired. Its first moment is identically one. Its third moment is a bounded nearest-neighbor Fourier polynomial. The mean static mass is bounded uniformly in \(L\). The zero mode contributes one to the mean. In the shell of maximum integer frequency \(j\ge1\) there are at most \(24j^2+2\) modes and \(E(k)\ge4j/L\). Summing the inverses and dividing by \(L^3\) gives a bounded remainder. Yet the zero mode escapes every fixed strictly positive band. Thus the three displayed moment hypotheses, even with a finite-range cubic moment, do not give a fixed positive lower endpoint at every momentum. [Numerical and algebraic controls](controls.py)

These are fixed-spatial-regulator results. A bounded **physical** momentum region occupies a shrinking part of the dimensionless Brillouin zone under spatial refinement. Following it requires control of the exceptional set there, of \(a,c,\ell,R\) in the physical units, and of field normalization on the same trajectory. The estimates give no lower bound on all positive energies outside the measured plaquette channels. Four-dimensional continuum existence and the Millennium mass gap remain open. [PCP generation and Lean coverage](execution.md)

For the \(SU(2)\) adjoint trace there is a polynomial estimate valid for every spatial smearing. It locates a band with lower endpoint \(\delta\kappa/12288\) for at least a fraction \(1-\delta\) of momenta, uniformly in the magnetic coupling, and bounds the energy-weighted low-energy fraction of any smearing of controlled support. [Adjoint smearing and spatial refinement](adjoint-refinement.md)

For \(SU(2)\), B4's explicit temporal spacing carries these joint momentum measures to growing anisotropic Wilson boxes. A Fourier Parseval estimate transfers the closed positive band with slightly enlarged endpoints at the same asymptotic fraction of momenta. [Wilson time sequence and error](wilson-time.md)
