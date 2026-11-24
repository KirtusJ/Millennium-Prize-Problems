# Referee report (ref2-math), main.tex second draft, 24 Nov 2026

Reviewer is a separate context of the author's model family; not independent review.
Program: check.py; output: results.txt (command: `python3 check.py`, no arguments, seeds 1 and 2 fixed in file).

## DEFECT / GAP items first

### D1 DEFECT (main.tex 165-166 and 436-437): "strictly positive", "injective", S_n = e^{-nH}
The operator for which (e:trace) holds for ALL bounded slice functions on the periodic lattice is NOT injective
on L^2 of the slice configurations. Reason: a gauge transformation on the sites of ONE time slice (it moves that
slice's spatial links and the adjacent time-like links) preserves the periodic Wilson measure, so for j != 0 mod T
E_T[f(x_0) g(x_j)] = E_T[(Pi f)(x_0) (Pi g)(x_j)], Pi = average over slice gauge transformations. Via Prop. p:vac,
<f, S_j f> = 0 for every f with Pi f = 0, hence S_1 f = 0 (j = 2). So S_1 has an infinite-dimensional kernel,
H = -log S_1 does not exist on L^2(Omega^2), and Theorem t:inh as stated (S_s = e^{-sH}) is not applicable there.
Luescher's strictly positive operator is the temporal-gauge one L_0; the operator in (e:trace) is L_0 Pi. The two
"standard facts" hold for different operators.
Computed (P5, toy Z_3 gauge theory, 2 spatial sites, T=3, 9 slice states): brute force -0.0063564423 = trace
formula with gauge-averaged kernel; that kernel has eigenvalues {0 x6, 15.42 x2, 105.46}; the strictly positive
L_0 (min eigenvalue 1.71) gives 0.01756, i.e. (e:trace) fails for it.
What survives: L >= 0 (semidefinite), Jentzsch, Prop. p:vac, and both norm bounds of Cor. c:vac are unaffected.
Replacement, line 161-166:
 "... $\mathsf L$ denotes the transfer operator of [Lu77,OS78], with the time-like links integrated, on $L^2$ of
 the slice configurations with Haar measure; it is self-adjoint, positive semidefinite, vanishes on the orthogonal
 complement of the gauge-invariant functions and is strictly positive on the gauge-invariant functions. ...
 $S_1f=\Lambda_0^{-1}\Omega^{-1}\mathsf L(\Omega f)$ is a self-adjoint positive contraction with $S_11=1$. On the
 closed subspace of gauge-invariant functions of $L^2(\Omega^2)$, which $S_1$ preserves, $S_1$ is injective and
 $S_n=e^{-nH}$ with $H=-\log S_1\ge0$ self-adjoint; the vacuum representation used with Theorem t:inh is this
 subspace."
Replacement, line 436-437: "a self-adjoint, positive semidefinite integral operator $\mathsf L$ with continuous,
 strictly positive kernel, strictly positive on the gauge-invariant functions".
Line 85: "$\mathcal K$ consists of the centred gauge-invariant functions of a time slice".
Remark r:ret(c), replace "It is restricted to the gauge-invariant functions without change" by "Theorem t:inh is
 applied on the gauge-invariant functions, where $H$ exists; the bound restricts to them without change".
(The commutation claim there is correct: Omega is gauge-invariant; site transformations at even sites act on coarse
links as coarse gauge transformations, others act trivially, so P commutes with them; A_theta is conjugation-invariant.)
Alternative fix: state Theorem t:inh for a positive contraction semigroup S_n = S_1^n with E the spectral projection
of S_1 for [e^{-L},1]; the proof goes through verbatim without injectivity (tested, P4, including near-singular S).

### G1 GAP (line 474-475): one-slice right side
Prop. p:vac is stated for two slices, j >= 1. The right side of (e:ret) is a one-slice expectation. It follows
from the proposition with f = |h|^2, g = 1, j = 1 (S_1 1 = 1), but this is not said.
Replacement: "... using Proposition p:vac for both sides (for the right side with $f=|h|^2$, $g=1$, $j=1$, as
$S_11=1$)". Also the proof of p:vac needs T-j >= 2 for the trace-norm limit; harmless as T -> infinity.

### D2 DEFECT (minor, line 536): wrong reference
"the two couplings of Section s:local": that section has one coupling (3.276133577). 0.00319 is for
beta = 3.399810242 of Remark r:ret(b). Computed: 0.0034367 and 0.0031912.
Replacement: "which is $0.00344$ at the coupling of Section s:local and $0.00319$ at that of Remark r:ret(b)".

### D3 DEFECT (minor, lines 206-207 and arrow in Fig. f:arch): count of inputs
"Theorem t:inh is an implication ... three of [its inputs] are open" contradicts s:not(3) ("first and third
hypotheses", two). Hypothesis h:budget is an input of Corollary c:acc, not of Theorem t:inh.
Replacement: "The route through Theorem t:inh and Corollary c:acc is an implication: its conclusion is available
only where all inputs are, and three of them are open."

### G2 GAP (line 375-376): liminf claim, hypotheses in surrounding text only
Needed and used: the two step inequalities for every i >= 1; M bounded; the series of h:budget convergent.
With eps_i of either sign (Cor. allows real eps_i) partial sums may exceed the total, but they converge to a
limit < d_0, so liminf d_n >= (d_0 - sum)/sup M > 0 still holds. The claim STANDS; the proof does not say this.
Replacement for end of proof: "Under Hypothesis h:budget the partial sums converge to a limit $s<d_0$, so
$\liminf d_n\ge(d_0-s)/\sup_nM_n>0$."

### G3 GAP (wording, Remark r:ret(d))
Bound is correct. But conjugation invariance is not what makes the event a translate: for any measurable A,
{U : XUY in A} = X^{-1} A Y^{-1} has Haar measure mu(A) by bi-invariance. Conjugation invariance makes the event
independent of the base point and gauge-invariant. Also needs the link to occur once in the holonomy.
Replacement: "... so for a measurable set $A$ of holonomies (conjugation-invariant, so that the event does not
depend on the base point) the event is a two-sided translate of $A$ for the link, and the conditional probability
of return is at most ...".

### G4 (wording, Remark r:crit(d))
"cannot establish a gap" is false when dim H is finite (a finite set can span). Add "in infinite dimension".

## Verdicts
1. p:vac STANDS (trace placement, cyclicity, HS/trace class, Jentzsch, norm and trace-norm limits, identification
   <Omega, M_f (L/Lambda_0)^j M_g Omega> = int Omega^2 f S_j g = <f-bar, S_j g>, all follow; uses L >= 0 only).
   c:vac STANDS for both norm bounds (P is an orthogonal projection in L^2(Omega^2); multiplication by a
   coarse-measurable indicator commutes with it; A_theta is coarse-measurable since the plaquette has even corners;
   B = RB = BR so BS_nB = B(RS_nR)B; density and quadratic-form norm fine; complex h supplied by t:ret). G1.
   Injectivity / e^{-nH}: DEFECT D1. Integer multiples in t:inh: STANDS once H exists (S_s defined for real s).
2. h:budget, c:acc last sentence: STANDS with G2. r:budget: STANDS, exact (P1): equality at every step i <= 60,
   partial sums = d_0(1-2^{-n}), total d_0 exactly, M_60 = 2.38423, sum kappa = 0.39514, d_i -> 0.
3. t:ret complex form STANDS (chain: |.| <= E[1 1 |g(x)||g(y)|] <= AM-GM, exchange by time reflection, tower).
   Six staples per link in four dimensions correct, distinct also for T = 2; U occurs once (N >= 6).
   Envelope: 0 violations of 420. r:ret(a) arithmetic correct. r:ret(b): 0.003072, 0.15618, 0.93480, matches.
   r:ret(d) e^{12 beta} correct (e^{6beta}/e^{-6beta}); G3.
4. r:crit(a) STANDS. (d) G4.
5. t:crit, l:scal, t:inh (0 violations of 4000 qualifying random instances, min slack 4.7e-8), l:cap (0 of 48;
   monotone in k), p:haar (identities rederived by hand; R'(6) = 0.036885895498; 0 violations of 4000 grid
   points for p<q, p'<0, w'>0 on (0,60]), r:reset: NONE FOUND.

## Sentences claiming more than proved
Only those in D1 (lines 165-166, 436-437, and through them "becomes the second inequality of (e:hyp)", line 108,
which is true only on the gauge-invariant subspace), D3 and G4. No sentence claims a mass gap.

## Hypotheses used and where stated
gauge-invariant subspace for existence of H: NOWHERE (D1). T-j >= 2: nowhere (harmless). kappa >= 0, tau <= t,
gamma > 0: statement. Even corners of the coarse plaquette: surrounding text (Setting). Convergence of the budget
series: implicit in h:budget. Link occurs once in holonomy: implied by N >= 6, not said.

## Not checked
The Lean files; references Lu77/OS78 themselves (not reread; D1 rests on my own argument and the toy computation,
not on the papers); Section s:evid numbers and data; main.pdf against main.tex; the 33-term tail bound (I used 80
rational terms); the derivation in RepoInh; the SU(2) four-dimensional transfer kernel itself (only a Z_3 toy).
No failed predicates in check.py; no package installed.
