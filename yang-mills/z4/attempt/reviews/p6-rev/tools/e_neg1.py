E = [
(r"""Five routes to Hypothesis~(A) were written out as chains of steps.""",
 r"""Four routes to Hypothesis~(A), and an argument by exclusion, were written out as chains of steps."""),
(r"""$-2.0$, $-1.5$ (Monte Carlo by one program). The lemma was rechecked by a second worker by
argument only.""",
 r"""$-2.0$, $-1.5$ (Monte Carlo by one program). The lemma was checked a second time, by argument
only."""),
(r"""Part (ii) was computed exactly and confirmed by finite differences in three separate programs
(builder, challenger, and the builder's child).""",
 r"""Part (ii) was computed exactly and confirmed by finite differences in three separate programs."""),
(r"""\begin{hypothesis}[Step S6]\label{neg:hyp-S6}
For large $\beta$, $\kappa_H(U)\ge 1/2$ except on configurations containing plaquettes with
$\operatorname{Re}\Tr Q_p<0$; such configurations have density $e^{-c\beta}$, so a local
perturbation argument applies.
\end{hypothesis}""",
 r"""\begin{hypothesis}[Step S6]\label{neg:hyp-S6}
There is $\beta_0<\infty$ such that, for every $\beta\ge\beta_0$, every box and every configuration
$U$ with $\operatorname{Re}\Tr Q_p\ge0$ for all plaquettes $p$, $\kappa_H(U)\ge 1/2$.
\end{hypothesis}

As written in the source, S6 also asserted that configurations with a plaquette of negative trace
have density $e^{-c\beta}$, ``so a local perturbation argument applies''; that part is not a
precise statement and is not tested here. The form above is the part that can be tested."""),
(r"""\begin{observation}\label{neg:obs-curv}
Step S6 is false on every periodic box tested. On the periodic lattices $3^4$ and $4^4$ at
$\beta\in\{4,6,12,24,48\}$, $\kappa_H$ of equilibrium configurations lies in
$[-2.30,-1.12]$ (Table~\ref{neg:tab-curv}). No sample of either program has $\kappa_H\ge1/2$:
$0$ of $32$ (builder) and $0$ of $24$ (challenger). At $\beta=4$ and $6$ the fraction of
plaquettes with $\operatorname{Re}\Tr Q_p<0$ is $0.002$ and $0.000$. Status: Monte Carlo by two
separate programs. The sources do not give the seeds. Thermalization was short ($30+4k$
sweeps in the builder's program; cold start plus $300$ sweeps in the challenger's).
\end{observation}""",
 r"""\begin{observation}\label{neg:obs-curv}
Status: Monte Carlo by two separate programs, measured only. On the periodic lattices $3^4$ and
$4^4$ at $\beta\in\{4,6,12,24,48\}$, $\kappa_H<0$ in every equilibrium sample: $56$ of $56$
($32$ from program~1 and $24$ from program~2), with values in $[-2.30,-1.12]$
(Table~\ref{neg:tab-curv}). Relation to Step~S6: S6 is a statement about $\beta\ge\beta_0$ with
$\beta_0$ unspecified. The samples at $\beta=4$ and $6$ do not bear on it; at $\beta=4$ the
fraction of plaquettes with $\operatorname{Re}\Tr Q_p<0$ is $0.002$, about one plaquette of the
$486$ of a $3^4$ torus per sample. The samples at $\beta=12$, $24$, $48$ do bear on it: if their
configurations have no plaquette of negative trace (this fraction is recorded only at $\beta=4$
and $6$, where it is $0.002$ and $0.000$), they show that S6 fails on these boxes for every
$\beta_0\le48$. No sample bears on $\beta>48$ or on larger boxes. The sources do not give the
seeds. Thermalization was short ($30+4k$ sweeps in program~1; cold start plus $300$ sweeps in
program~2).
\end{observation}"""),
(r"""builder & $3^4$ periodic & $4$, $6$ & $8$ each & $-2.2$ to $-1.5$ \\
builder & $3^4$ periodic & $12$, $24$, $48$ & $4$ each & $-2.30$ to $-1.17$ \\
builder & $4^4$ periodic & $4$ & $2$ & $-1.60$, $-1.88$ \\
builder & $4^4$ periodic & $6$ & $2$ & $-1.53$, $-1.58$ \\
challenger & $3^4$ periodic & $4$ & & $-1.79$ to $-1.46$ \\
challenger & $3^4$ periodic & $6$ & & $-1.96$ to $-1.39$ \\
challenger & $3^4$ periodic & $12$ & & $-1.52$ to $-1.12$ \\
challenger & $3^4$ periodic & $24$ & & $-1.93$ to $-1.12$ \\
challenger & $3^4$ periodic & $48$ & & $-2.04$ to $-1.55$ \\
challenger & $4^4$ periodic & $6$ & $2$ & $-1.77$, $-1.26$ \\
challenger & $4^4$ periodic & $24$ & $2$ & $-1.15$, $-1.67$ \\
\midrule
challenger & $4^4$ open & $4$ & & $-2.40$ to $-1.67$ \\
challenger & $4^4$ open & $6$ & $3$ & $+0.16$, $-0.32$, $-0.04$ \\
challenger & $4^4$ open & $12$, $24$, $48$ & & $+3$, $+9.6$, $+23$ \\""",
 r"""1 & $3^4$ periodic & $4$, $6$ & $8$ each & $-2.2$ to $-1.5$ \\
1 & $3^4$ periodic & $12$, $24$, $48$ & $4$ each & $-2.30$ to $-1.17$ \\
1 & $4^4$ periodic & $4$ & $2$ & $-1.60$, $-1.88$ \\
1 & $4^4$ periodic & $6$ & $2$ & $-1.53$, $-1.58$ \\
2 & $3^4$ periodic & $4$ & not recorded & $-1.79$ to $-1.46$ \\
2 & $3^4$ periodic & $6$ & not recorded & $-1.96$ to $-1.39$ \\
2 & $3^4$ periodic & $12$ & not recorded & $-1.52$ to $-1.12$ \\
2 & $3^4$ periodic & $24$ & not recorded & $-1.93$ to $-1.12$ \\
2 & $3^4$ periodic & $48$ & not recorded & $-2.04$ to $-1.55$ \\
2 & $4^4$ periodic & $6$ & $2$ & $-1.77$, $-1.26$ \\
2 & $4^4$ periodic & $24$ & $2$ & $-1.15$, $-1.67$ \\
\midrule
2 & $4^4$ open & $4$ & $3$ & $-2.40$ to $-1.67$ \\
2 & $4^4$ open & $6$ & $3$ & $+0.16$, $-0.32$, $-0.04$ \\
2 & $4^4$ open & $12$, $24$, $48$ & $9$ in total & $+3$, $+9.6$, $+23$ \\"""),
(r"""\caption{Horizontal curvature $\kappa_H$ of equilibrium configurations, $\SU(2)$. The
challenger ran $20$ periodic samples on $3^4$ in total. The builder's own summary row gives
$[-2.3,-1.2]$ and the director's ledger gives $-1.1$ to $-2.3$; the union of the per-run values
of both programs is $[-2.30,-1.12]$.}""",
 r"""\caption{Horizontal curvature $\kappa_H$ of equilibrium configurations, $\SU(2)$. Program~2 ran
$20$ periodic samples on $3^4$ in total; the source does not record them per row. The open-box
count at $\beta=4$ is $6$ (at $\beta=4$ and $6$ together) minus $3$. Program~1's own summary row
gives $[-2.3,-1.2]$ and an earlier summary gives $-1.1$ to $-2.3$; the union of the per-run values
of both programs is $[-2.30,-1.12]$.}"""),
(r"""The challenger found the mechanism, measured only.""", r"""Program~2 also measured a mechanism (measured only, not proved)."""),
(r"""The inequality is \cite[(11)]{KT02}, read in full text by the worker; \cite{KT02} attribute it""",
 r"""The inequality is \cite[(11)]{KT02}, read in full text; \cite{KT02} attribute it"""),
(r"""is not closed. It is false for $\Z_2$ at
$\beta=0.6$ (Table~\ref{neg:tab-vort}). For $\SU(2)$ the data neither support nor refute it:
the errors are as large as the differences, and at $\beta=2.4$,
$F_4-F_3=+1.26\pm1.05$, the wrong sign at $1.2$ standard errors.""",
 r"""is not closed. It is false for $\Z_2$ at
$\beta=0.6$ (Table~\ref{neg:tab-vort}). For $\SU(2)$ the comparison the step concerns is $F_4$
against $F_2$ ($2\mid4$): $F_4-F_2=-0.20\pm0.47$ at $\beta=1.8$ and $-0.25\pm1.04$ at
$\beta=2.4$ (errors combined in quadrature, treating the runs as independent). Both differences
have the sign the step predicts, and neither is resolved from zero. The data neither support nor
refute the step. (The value $F_3$, with $3\nmid4$, does not bear on it.)"""),
(r"""Status: $\SU(2)$ values, Monte Carlo by one program (Metropolis with a step size adapted during
the run, so not strictly detailed balance); $\Z_2$ values, Monte Carlo by one program, rerun bit
for bit by a second worker; the three-dimensional""",
 r"""Status: $\SU(2)$ values, Monte Carlo by one program (Metropolis with a step size adapted during
the run, so not strictly detailed balance); $\Z_2$ values, Monte Carlo by one program, rerun bit
for bit by a second session. The $\Z_2$ coupling convention is not stated in the source (it
quotes a transition at $\beta_c\approx0.44$); the three-dimensional"""),
(r"""$z(L,\beta)\ge z^*$ implies $K(kL,\beta,\gamma)$. No inequality of any kind is known connecting
a periodic-box, one-sector number to a condition uniform over exterior configurations, even at
strong coupling.""",
 r"""$z(L,\beta)\ge z^*$ implies $K(kL,\beta,\gamma)$. No inequality connecting a periodic-box,
one-sector number to a condition uniform over exterior configurations, even at strong coupling,
was found in the sources read for this route (those cited in this section); no systematic
literature search was made."""),
(r"""factor $2$ of $1/(2\beta)=0.217$ at $L=4,6$'' failed; that was the worker's expectation, which
ignored the finite temporal extent.""",
 r"""factor $2$ of $1/(2\beta)=0.217$ at $L=4,6$'' failed; that was an expectation of the program's
author, which ignored the finite temporal extent."""),
(r"""Not every $\SU(2)$ amplitude is nonnegative. On the periodic $2\times1\times1$ lattice in three
dimensions, $4$ of the $729$ spin configurations considered have $A<0$, $141$ have $A>0$ and
$584$ have $A=0$.""",
 r"""Not every $\SU(2)$ amplitude is nonnegative. Take the periodic $2\times1\times1$ lattice in three
dimensions: side $2$ in direction $0$ and side $1$ in directions $1$ and $2$, so two sites, $0$ and
$1$, each the corner of three plaquettes $(01)$, $(02)$, $(12)$. The $729=3^6$ configurations
considered assign a spin in $\{0,\tfrac12,1\}$ to each of the six plaquettes (this reading of the
source's ``$2\times1\times1$'' and of its count $729$ is ours; the source does not spell it out).
Of them, $4$ have $A<0$, $141$ have $A>0$ and $584$ have $A=0$."""),
(r"""four dimensions with the same amplitude (proved by the worker: those links occur in no character).""",
 r"""four dimensions with the same amplitude (proved: those links occur in no character)."""),
(r"""\begin{lemma}\label{neg:lem-usc}
Assume \textup{(H1)} a unique infinite-volume Gibbs state $\mu_\beta$ for every $\beta$;
\textup{(H2)} the specification is continuous in $\beta$ and in the boundary condition;
\textup{(H3)} reflection positivity, so that $C_F(n)=\langle\psi_F,T^n\psi_F\rangle$;
\textup{(H4)} vectors of local positive-time observables are dense. Then""",
 r"""\begin{lemma}\label{neg:lem-usc}
Assume \textup{(U1)} a unique infinite-volume Gibbs state $\mu_\beta$ for every $\beta$, or, more
generally, a choice of state $\beta\mapsto\mu_\beta$ that is weakly continuous in $\beta$;
\textup{(U2)} the specification is continuous in $\beta$ and in the boundary condition;
\textup{(U3)} reflection positivity, so that $C_F(n)=\langle\psi_F,T^n\psi_F\rangle$;
\textup{(U4)} vectors of local positive-time observables are dense. Then"""),
(r"""(H1), (H2) and compactness give weak continuity of $\beta\mapsto\mu_\beta$, so each $C_F(n)$ is
continuous.""",
 r"""(U1), (U2) and compactness give weak continuity of $\beta\mapsto\mu_\beta$ (under the second
form of (U1) it is assumed), so each $C_F(n)$ is continuous."""),
(r"""with limit $-\log\|T|_{\overline{\mathrm{span}}}\|$. By (H4) the infimum over $F$ is $m$.""",
 r"""with limit $-\log\|T|_{\overline{\mathrm{span}}}\|$. By (U4) the infimum over $F$ is $m$."""),
(r"""(H1) is the standing assumption of the paper and is not known at large $\beta$; (H2) is claimed
as standard, with no source read.""",
 r"""(U1) is a hypothesis of this lemma only; the rest of the paper works with arbitrary limit points
in $\cL_\beta$ and does not assume it. Uniqueness is not known at large $\beta$, and no continuous
choice of limit point is known either. (U2) is claimed as standard, with no source read."""),
(r"""\begin{observation}\label{neg:obs-usc}
Under \textup{(H1)--(H4)} nothing beyond upper semicontinuity follows from continuity of the
correlations. An abstract continuous family of spectral measures has zero set
$\{m=0\}=(1,\infty)$, which is not closed, and a correlation length equal to $1$ up to the
transition and infinite after it (checked by one program). It is not a lattice model. No theorem
of the form ``the gap vanishes $\Rightarrow$ the free energy is non-analytic'' was found.
\end{observation}""",
 r"""\begin{observation}\label{neg:obs-usc}
Continuity of every correlation in $\beta$ does not give more than upper semicontinuity of the
gap. For $\beta>0$ let $\nu_\beta$ be the measure on $[0,1]$
\[
\nu_\beta:=\delta_{e^{-1}}+\max(0,\beta-1)\,2\,\mathbf 1_{[1/2,1)}(x)\,dx,
\]
read as the spectral measure of $T$ for one vector. Its moments
$a_n(\beta)=\int x^n\,d\nu_\beta=e^{-n}+\max(0,\beta-1)\,(1-2^{-n-1})\,2/(n+1)$ are continuous in
$\beta$ for every $n$, while $m(\beta)=-\log\max\operatorname{supp}\nu_\beta$ is $1$ for $\beta\le1$
and $0$ for $\beta>1$. So $\{m=0\}=(1,\infty)$ is not closed, and the correlation length is $1$ up
to $\beta=1$ and infinite after it. Status: exact for this family; a grid check by one program
agrees. The family is abstract, not a lattice model, and it does not show that $\SU(2)$ has such a
jump. No theorem of the form ``the gap vanishes $\Rightarrow$ the free energy is non-analytic''
was found in the sources read.
\end{observation}"""),
(r"""(as stated in their abstracts). Consequently no argument that uses only P1--P6 proves (A).""",
 r"""(as stated in their abstracts). Consequently an argument that derives (A) for $\SU(2)$ from
P1--P6 alone, and from nothing else, would apply verbatim to $\U(1)$ and give a gap there at weak
coupling, which is false; no such argument exists."""),
(r"""All three are local. None has a known global consequence for the gap.""",
 r"""All three are local. For none of them did the sources read for this section give a global
consequence for the gap."""),
(r"""Observation~\ref{neg:obs-curv-missing}. No inequality monotone in the dimension is known, and""",
 r"""Observation~\ref{neg:obs-curv-missing}. No inequality monotone in the dimension was found in the
sources read, and"""),
(r"""The principle ``a lattice gauge theory with no continuous global or one-form symmetry has a
gap except at isolated couplings'' fails.""",
 r"""Status: item~(1) is cited from an abstract; item~(2) is numerical, and the masslessness of its
weak-coupling phase is not established. The principle ``a lattice gauge theory with no continuous
global or one-form symmetry has a gap except at isolated couplings'' fails, by item~(1) as cited;
item~(2) is consistent with this but does not establish it."""),
(r"""A Monte Carlo by one program on $4^5$ (200 Metropolis sweeps,
one seed per start, written by a sub-worker and rerun bit-identical by the worker) gives a""",
 r"""A Monte Carlo by one program on $4^5$ (200 Metropolis sweeps,
one seed per start, rerun bit-identically by a second session) gives a"""),
]
