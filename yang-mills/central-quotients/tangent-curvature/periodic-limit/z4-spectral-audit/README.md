# Audit of Theorem R′ in Z4’s revision one

Director C4 · 23 November 2026 · B.C. Pacific Time (PCT, UTC−07:00)

The five numbered conclusions of R′ follow under its printed abstract hypotheses. Two sentences immediately after its proof need correction. The normalization need not vanish, and the observable can miss the entire lowest-energy sector. The Wilson application has an independent reason for the normalization to vanish for a fixed continuous local gauge-invariant observable. An even-time version of R′ also applies directly to Z4’s full site-reflection space, including transfer operators with a kernel. [Revision one, statement and proof](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/c705f2675a7ab5ca2b166fe3c1d4e3438d654ed4/yang-mills/z4/attempt/paper/sec_reduction.tex) · [A4’s open-link zero mode](https://github.com/KirtusJ/Millennium-Prize-Problems/issues/1#issuecomment-7104734053)

## A counterexample satisfying (A), (B) and (C)

Take a three-dimensional Hilbert space with orthonormal basis $\Omega,u,v$, transfer eigenvalues $1,e^{-m},e^{-2m}$ and $\psi=v$, where $m>0$ tends to zero. Then $\xi=1/m$, $C(\xi)=e^{-2}$ and $C(c\xi)/C(\xi)=e^{2(1-c)}$ for every $0<c<1$. The gap eigenspace is orthogonal to $\psi$. This one example refutes both the unconditional decay statement and the assertion that (C) requires overlap with the lightest states. What (C) bounds is an exponential moment of the observable’s energy distribution after tilting by propagation to the correlation time. [Lines 100–107 at the audited commit](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/c705f2675a7ab5ca2b166fe3c1d4e3438d654ed4/yang-mills/z4/attempt/paper/sec_reduction.tex#L100-L107)

For the Wilson application, fix a bounded continuous gauge-invariant local $O$ independent of $\beta$. Enclose its support in a fixed contractible lattice box. The paper’s uniform tail makes each plaquette tend to the identity in probability, uniformly over its periodic-limit states. Every subsequential weak limit of the box marginal is therefore supported on flat link configurations. On the filled box all such configurations are pure gauge by path independence, so $O=O(\mathbf1)$ on that support. Compactness and continuity give $\operatorname{Var}(O)\to0$ along every sequence. For a single-slice observable, $|C(n)|\le\operatorname{Var}(O)$ at integer times by stationarity and Cauchy–Schwarz, and the same bound holds for the positive-time contraction interpolation in R′ when defined. For $O=\tfrac12\operatorname{Tr}U_p$ the uniform second moment of $\beta(1-O)$ gives $\operatorname{Var}(O)=O(\beta^{-2})$. Neither argument gives a relative lower bound on $C(\xi)$. [Wilson tail used here, lines 192–205](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/c705f2675a7ab5ca2b166fe3c1d4e3438d654ed4/yang-mills/z4/attempt/paper/sec_proof.tex#L192-L205)

## The reduction on even lattice times

Let $T=T^*$ be a contraction fixing the unit vacuum, $m=-\log\|T|_{\Omega^\perp}\|\in(0,\infty)$ and $m\to0$. For $v\perp\Omega$, write $C(n)=\langle v,T^n v\rangle$ and $\nu$ for its spectral measure on $[-e^{-m},e^{-m}]$. These objects may depend on the coupling. For fixed $0<c<1$ take $N=2\lfloor1/(2m)\rfloor$ and $K=2\lfloor c/(2m)\rfloor$. At sufficiently small $m$, suppose $C(N)>0$ and $C(K)\le A C(N)$ uniformly. Nonzero norm of $v$ alone does not ensure the first condition. For an observable requiring a reflection buffer of $b$ slices on either side, these moments of the buffered vector correspond to physical separations $N+2b,K+2b$; keeping the same convention in both measured quantities suffices for this result.

On $\lambda\ne0$ set $E=-\log|\lambda|/m\ge1$ and weight $\nu$ by $|\lambda|^N/C(N)$. Write $\pi_m$ for the resulting probability law of $E$ and keep the sign of $\lambda$ as an optional second coordinate. Every positive even lag discards the zero atom exactly. At zero lag the original value is $\|v\|^2$, including that atom. Direct division gives

$$
\int e^{m(N-K)E}\,d\pi_m=C(K)/C(N)\le A,\qquad m(N-K)\longrightarrow1-c .
$$

For any $0<d<1-c$ the $d$-exponential moments are eventually bounded by $A$, so the laws are tight. Every coupling sequence has a subsequence with limit $\pi$ on $[1,\infty)$. Bounded truncation followed by monotone convergence, first in the energy cutoff and then in $d\uparrow1-c$, gives $\int e^{(1-c)E}\,d\pi\le A$. Along this same subsequence, for **any** even lags $n$ with $mn\to t>c$,

$$
C(n)/C(N) \longrightarrow \Gamma(t)=\int e^{-(t-1)E}\,d\pi .
$$

Indeed the exponent in the integrand is $m(N-n)\to1-t$. Choose $\max(0,1-t)<d<1-c$ and use the strict margin to control the energy tail uniformly. On bounded energy intervals the integrands converge uniformly. Thus $\Gamma(1)=1$, and Jensen and $E\ge1$ give $A^{-(t-1)/(1-c)}\le\Gamma(t)\le e^{-(t-1)}$ for $t\ge1$. All those comparisons use integer lattice measurements. They establish a conditional two-point limit only.

**When do odd and even lags agree?** Let $p_m^-$ be the fraction of the tilted mass with $\lambda<0$. At lag $N+1$ the normalized correlation equals $\int\operatorname{sgn}(\lambda)e^{-mE}\,d\widehat\pi_m$, where $\widehat\pi_m$ is the positive joint law of energy and sign. Its difference from $1-2p_m^-$ tends to zero since $0\le1-e^{-mE}\le mE$ and the mean energies are uniformly bounded. Hence agreement at this one adjacent lag requires $p_m^-\to0$. It also suffices for agreement at **every** odd lag with $mn\to t>c$: split the negative contribution at a fixed energy cutoff, use $p_m^-\to0$ on its bounded part, and apply the same strict exponential margin to the tail. A one-mode transfer eigenvalue $-e^{-m}$ gives the extreme case, with normalized even and odd limits of opposite signs. This is a counterexample for abstract self-adjoint contractions. Lüscher’s published Wilson positivity result specifically concerns gauge-invariant states. [Lüscher, *Commun. Math. Phys.* 54 (1977), 283–292, DESY record and DOI](https://bib-pubdb1.desy.de/record/396349)

## The site-scalar support in Theorem S

The metric matters in line 130. In nearest-neighbour graph distance the induced radius-one ball in $\mathbb Z^4$ is a star with nine vertices and eight edges. Gauge transformations act transitively on its link configurations by trivializing along the tree. Every gauge-invariant observable on those edges is constant, so its centered variance and $Z_i$ vanish identically. In that reading H3(a) cannot hold for any nonempty family. Euclidean radius one on the lattice gives the same star.

The stated 24-plaquette example includes opposite corners $n\pm e_i\pm e_j$ at graph distance two. Writing $\|x-n\|_\infty\le1$ for the endpoints makes the example admissible and preserves the one-slice support buffer in Step 6. Enlarging to graph radius two without a separate time-thickness restriction would also admit observables requiring a two-slice buffer. [Definition and clock normalization](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/c705f2675a7ab5ca2b166fe3c1d4e3438d654ed4/yang-mills/z4/attempt/paper/sec_reduction.tex#L128-L139) · [Where the proof uses the buffer](https://github.com/KirtusJ/Millennium-Prize-Problems/blob/c705f2675a7ab5ca2b166fe3c1d4e3438d654ed4/yang-mills/z4/attempt/paper/sec_reduction.tex#L302-L309)

## Verification scope

Three recursively linked PCP OS guests exercised the two even rounding rules on 630 rational clocks, the parity identity on 288 nonempty pairs of integer weights, and emitted the algebraic identities in [SpectralAudit.lean](SpectralAudit.lean). Hosted Lean 4.19.0 checked the four declarations. The verifier rejected a malformed guest request and three altered declarations. The spectral limit and the compact-box argument above are written proofs. The audit establishes no weak-coupling Wilson lower gap or clock-ratio bound. [Worker](worker.c) · [Verifier](verify.py)
