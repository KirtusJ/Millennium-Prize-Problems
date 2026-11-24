# Readability and structure review of `yang-mills/z4/infrared/main.tex`

Reviewer brief: first-time reader, mathematician, not a lattice gauge theorist. Readability and structure only.
Source read: `main.tex` (719 lines, second draft dated 24 November 2026). No file was edited.
Line numbers are those of `main.tex`. Every proposed replacement is meant to carry the same meaning and no
stronger claim; where a gloss needs a fact I could not confirm from the text, it is marked **[author to confirm]**.

Overall: the opening question (l.21-24) is the right kind of start and the theorems arrive early. The reader is
lost in four places: (a) the abstract and introduction count the open items differently from Section 3;
(b) Theorem 2 is followed by a glossary of symbols instead of a reading of its three hypotheses in words;
(c) the hypotheses that the whole paper turns on are inside a section called "Architecture", followed by a
dense subsection on an external construction; (d) the measurement subsections start with parameters instead of
a question, and use "mark", "stream", "two-time energy" without definition. There is no "idea in words" section.

---

## 1. Where the reader is lost, slowed or intimidated

### 1.1 Abstract (l.10-14)

Problems. Four sentences where one or two would do. "Two interacting estimates" reads as "two estimates that
interact with each other"; it means estimates for the interacting theory. "tolerates an exceptional set of
coarse fields" and "the return to such a set" use two undefined notions in the first 60 words. The count "two"
disagrees with Section 3, which says "three of them are open" (l.207) and lists three hypotheses.

Rewrite:

```latex
We ask how a mass gap could be recognised in a Yang--Mills theory known through its correlation functions,
and what would let a gap survive when a lattice is refined. We prove a spectral criterion for the first
question and, for the second, an inequality that reduces one refinement step to three estimates; we prove one
of the three for $\SU(2)$, the other two are open, and no mass gap is proved.
```

### 1.2 Introduction, second paragraph (l.26-32)

Problems. "no longer hypothetical in their first half" makes the reader work out which half. One sentence of
55 words with a semicolon carries the construction, its assessment and two negatives. "what the open
statements are up against" is colloquial and vague.

Rewrite:

```latex
The first question now has an object to be asked about. A continuum theory, obtained as a scaling limit of
Wilson lattice gauge theory for every simple compact gauge group, was submitted in formal form in October
2026~\cite{OAI}. Its assessors judge that it satisfies the Wightman axioms, and state that it proves neither a
mass gap nor uniqueness of the infinite-volume limit~\cite[p.~1]{YMG}. The problem of Jaffe and
Witten~\cite[\S4]{JW} asks for existence and a gap, so the gap is what is missing. This paper does not supply
it. It records what we can prove about the two questions, states what is open, and reports measurements of
the quantities that the open statements concern.
```

### 1.3 "The two questions", first paragraph (l.35-40)

Problems. "forget the vacuum" is a metaphor the reader must decode. "a family of vectors that spans" ends
without an object. "worth stating because it fits" sounds apologetic.

Rewrite:

```latex
The first question has an elementary answer. If $H\ge0$ is the Hamiltonian and $v$ a vector, the numbers
$\langle v,e^{-n\tau H}v\rangle$ are correlation functions at Euclidean time separation $n\tau$. Their
successive differences $d_{v,n}$ are non-negative, receive no contribution from the vacuum, and decay at a
rate set by the lowest positive energy present in $v$. The Hamiltonian has a gap exactly when one rate serves
for every $v$ in a set with dense span (Theorem~\ref{t:crit}).
```

### 1.4 "The two questions", second paragraph (l.42-51)

Problems. "coarse links" is used before any gloss. "The second requirement cannot hold uniformly" reads as a
proved statement about the transfer dynamics, but the support given is slowness "under local updates", which
Section 2 (l.179) says is a different dynamics; as worded this is stronger than what the paper shows.
"the two interacting estimates themselves" repeats the ambiguity of the abstract.

Rewrite (from "A function of a time slice" to the end):

```latex
Each coarse link is the product of two consecutive fine links. A function of the fine links at one time splits
into the part that can be predicted from the coarse links and the remainder. Suppose the predictable part
decays in time as it does on the coarse lattice, and the remainder decays within a few lattice steps. Then the
fine lattice inherits the coarse decay with a small loss. We do not expect the second supposition to hold on
every coarse background: under the local updates of Section~\ref{s:set} we measure backgrounds on which fine
fluctuations relax slowly (Section~\ref{s:local}). Theorem~\ref{t:inh} shows that the inheritance survives if
such backgrounds are put in an exceptional set to which the dynamics seldom returns, and
Theorem~\ref{t:ret} proves a return bound of that kind for $\SU(2)$. Two estimates for the interacting theory
remain open: decay of the remainder off the exceptional set, and the comparison of the predictable part with
the coarse lattice.
```

### 1.5 Paragraph after Theorem 1 (l.67-69)

Problem. "the problem of [JW] also requires the mass to be finite" is cryptic: the reader must infer that this
means "some spectrum above zero".

Rewrite:

```latex
In~(2) only the rate $r$ is common; the constants and the onset of the decay may depend on $v$. The criterion
holds trivially when $H=0$. It excludes spectrum in $(0,\Delta)$ and does not say that there is any spectrum
above $\Delta$, which the problem of~\cite{JW} also requires.
```

### 1.6 Paragraph after Theorem 2 (l.85-89) -- the most important fix

Problems. The theorem has eleven symbols and three hypotheses; the paragraph that follows names the objects
but never says in words what each hypothesis asks or what the conclusion gives. "centred", "transfer
semigroup", "vacuum representation", "coarse links", "exceptional set of coarse fields" all arrive undefined
in one sentence. The word "deficit" is introduced inside the theorem with no reason for the name, and the
reader is not told that a positive deficit is the thing wanted.

Rewrite:

```latex
In words. Split the space into a coarse part $P$, an exceptional part $B$ and a good part $G$. The first
hypothesis says that a function loses, within time $2a$, at least the fraction $\gamma$ of the squared norm of
its good part. The second says that the exceptional part overlaps with itself after time $\tau$ by at most
$\kappa$. The third says that the coarse part alone already has deficit $b$ at time $t$. The conclusion is
that the whole space has deficit at least $b-\kappa$, divided by a factor that tends to $1$ when
$a/\gamma\to0$.

In the application (terms are defined in Section~\ref{s:set}) $\mathcal K$ is the space of functions of one
time slice of the fine lattice with vacuum expectation zero, $S_s$ is the transfer semigroup at multiples $s$
of the mesh $a$, $P$ is the conditional expectation given the coarse links, and $B$ is the part of $Q$
supported on an exceptional set of coarse fields. On this space $\lambda$ is the gap of the lattice
Hamiltonian, so $d>0$ is a gap at that lattice. The proof uses only the spectral calculus of $S_a$, so it
holds for discrete time.
```

### 1.7 Theorem 3 and the paragraph after it (l.91-109)

Problems. "gate" appears in the title and never in the statement; the reader has to guess that the gate is
$A_\theta$. "holonomy" and "round distance" are used before Section 2. Nothing says why the centre is $-I$.
The paragraph after the theorem goes straight to the vacuum and the transfer matrix without a plain reading.

Edits. In the statement, after "lies within round distance $\theta$ of $-I$" add:

```latex
We call $A_\theta$ a \emph{gate}.
```

Replace l.106-109 by:

```latex
In words: whatever the field is at one time, the conditional probability that the chosen plaquette is within
$\theta$ of $-I$ at another time is at most $p_{6\beta}(\theta)$, which is of order $\theta^3$. The bound does
not depend on the spatial volume, on the time separation or on the rest of the field. (The holonomy of a
plaquette is the ordered product of the links around it; the round distance is the angle on $S^3$; see
Section~\ref{s:set}.) Corollary~\ref{c:vac} carries the bound to the vacuum on an infinite time axis, where it
becomes the second inequality of~\eqref{e:hyp}. That step uses the transfer-matrix representation
of~\cite{Lu77,OS78}, which we cite.
```

Add one sentence on why $-I$, with whatever is actually the reason. A wording consistent with Section 8.1,
**[author to confirm]**:

```latex
The gate is centred at $-I$ because the slowest local relaxation we measured is on backgrounds with coarse
holonomy $-I$ (Section~\ref{s:local}).
```

### 1.8 Proposition 4 in "Statements" (l.111-118)

Problem. A statement about Bessel ratios with a nine-digit enclosure appears among the main results with no
sentence on its role. This is the most intimidating item on page 2-3, and by Remark `r:haar` and the figure
caption it feeds only an auxiliary statement. Move the statement to Section 7 (see 4.3 below) and leave in
the introduction:

```latex
A fourth result, Proposition~\ref{p:haar} in Section~\ref{s:haar}, gives a sharp lower bound for the
conditional variance of a single link. It bounds one term of an auxiliary statement and is not an input of
Theorem~\ref{t:inh}.
```

### 1.9 "Architecture", opening paragraph (l.204-210)

Problems. (a) "its conclusion is available only where all its inputs are, and three of them are open":
Theorem 2 has three hypotheses and one of them is proved by Theorem 3, so "three" contradicts the theorem and
the abstract; the third open item (the budget) belongs to Corollary 2. (b) "Nothing below it in the figure is
proved" is false for the layout: the box "Spectral criterion, Thm 1" is drawn below Theorem 2 and is solid.
(c) "moments $d_{v,n}$": they are called "differences" everywhere else. (d) The paragraph explains the
legend before saying how to read the figure.

Rewrite:

```latex
Figure~\ref{f:arch} is the outline. Read it from the top. Theorem~\ref{t:inh} treats one halving of the mesh
and has three inputs: the return bound, which is Theorem~\ref{t:ret}; decay off the gates
(Hypothesis~\ref{h:mix}); and comparison with the coarse lattice (Hypothesis~\ref{h:coarse}).
Corollary~\ref{c:acc} chains the halvings and needs one more input, the budget (Hypothesis~\ref{h:budget}).
The three hypotheses are open, so every box on the path from Theorem~\ref{t:inh} down to the mass gap is open.
Theorem~\ref{t:crit} enters only at the bottom: it says what would have to be checked in a continuum theory.
Solid boxes are proved in this paper, dashed boxes are open, and the dotted box is cited.

This is one sufficient route to a gap in a box. A direct estimate of the differences $d_{v,n}$ in the
continuum theory would meet the criterion of Theorem~\ref{t:crit} without it.
```

### 1.10 Paragraph after Hypothesis 1 (l.255-260)

Problems. One sentence with a colon, a semicolon, a relative clause and "granting it"; "local quotient over
all functions on good backgrounds" is abstract; "the implication goes one way only" after "stronger than" says
the same thing twice.

Rewrite:

```latex
Hypothesis~\ref{h:mix} is about the transfer semigroup. One route to it uses the local updates of
Section~\ref{s:set}. A derivation in~\cite{RepoInh}, not reproduced or checked here, bounds
$\langle f,(I-S_{2a})f\rangle$ from below by the expected loss of $f$ under those updates. Given that, it
would suffice to bound the local quotient $\mathcal J(F)/\mathcal V(F)$ from below for every function $F$ on
every background outside the gates. We call this the \emph{auxiliary local mixing statement}. It is stronger
than Hypothesis~\ref{h:mix}: a function that the local updates relax slowly may still decay quickly in time.
```

### 1.11 Paragraph after Hypothesis 3 (l.275-279)

Problems. "on one trajectory" is undefined (a sequence of lattices? of couplings?). "Summability ... alone
would not" needs its verb.

Rewrite:

```latex
None of the three is known for any interacting lattice gauge theory in four dimensions. If all three held
along one sequence of lattices, Corollaries~\ref{c:acc} and~\ref{c:vac} would give
$\liminf_i d_i>0$ in a fixed physical box. Summability of the $\kappa_i$ and $\varepsilon_i$ would not be
enough for this; the budget is a separate condition (Remark~\ref{r:budget}). Section~\ref{s:rem} lists what
would still be missing after that.
```

### 1.12 Subsection 3.1 "The external construction ..." (l.281-308)

Problems. The first sentence (l.282-288) is 95 words with four semicolons and reads as a second-hand summary
of a paper the author says he has not read; it stands between the hypotheses and the proofs. The third
paragraph (l.302-308) is one sentence of 85 words. This is the most intimidating page for the stated reader.
Move the subsection to the end (see 4.2). Break the first sentence into a list:

```latex
According to its assessors~\cite[pp.~1, 3]{YMG}, the construction~\cite{OAI} does the following.
\begin{enumerate}
\item It obtains continuum correlation functions as a scaling limit of Wilson lattice correlation functions
at a fixed physical volume, and then an infinite-volume limit along a subsequence, not proved unique.
\item Any such limit decomposes into component theories, each satisfying the Osterwalder--Schrader axioms and
hence, by reconstruction, the Wightman axioms.
\item Renormalised local operators corresponding to gauge-invariant polynomials in the curvature are defined,
with an operator product expansion that is not shown to match perturbation theory.
\item There is no evidence for or against a mass gap.
\end{enumerate}
```

and the third paragraph into a list introduced by:

```latex
For this paper to bear on that statement, the following would have to be fixed and matched to the
construction. None of it is done here.
```

with items: group and lattice action; sequence of meshes, couplings and physical units; order of the limits;
class of observables; component theory selected; relation between the lattice transfer semigroup at fixed
regulator and the Hamiltonian of the limit.

### 1.13 Measurements, opening (l.543-546)

Problems. "streams" and "predicates" are undefined. "what the open hypotheses face" is vague. "None supports
them, and none is a bound" is the fourth statement of the same caveat (see Section 5).

Rewrite:

```latex
This section reports Monte Carlo estimates for $\SU(2)$. A \emph{stream} is an independent run of the sampler
with its own seed; errors are jackknife errors over streams. Each measurement tries particular test functions
in an inequality that an open hypothesis, or the auxiliary statement, would need for all functions. A trial
can therefore show that a constant is at most some value; it cannot show that a hypothesis holds, and none is
used in a proof. Programs, seeds, raw data, the pass rules fixed before each run and the rules that failed are
in~\cite{RepoData}.
```

("stream = independent run with its own seed" is **[author to confirm]**.)

### 1.14 Measurement 8.1 (l.548-594)

Problems. Starts with a disclaimer, then a line of parameters. "marks" is never defined. The construction of
the frozen background is one 60-word sentence with two parentheses. Items (i)-(iii) each start with the
observation but bury the point. "one-sided", "trial values" recur.

Rewrite of l.549-558:

```latex
\emph{Question.} On a coarse background with holonomy $-I$, how small can the local quotient
$\mathcal J/\mathcal V$ be? This concerns the auxiliary local mixing statement, not Hypothesis~\ref{h:mix}.

\emph{Setup.} Side $N=6$, $T=12$, $\beta=3.276133577$, a point on a line of constant renormalised coupling
determined in~\cite{RepoData}. The coarse links of one slice are held fixed (a \emph{frozen background}) and
the fine links are sampled around them. All coarse links are the identity except two. One is $-I$, so the
three coarse plaquettes through it have holonomy $-I$. An adjacent one is the quaternion $\mathbf i$, which
supplies a reference direction; four coarse plaquettes then have holonomy $\pm\mathbf i$. A \emph{mark} is a
gauge-invariant function of the fine plaquettes inside one coarse plaquette; the list of marks is
in~\cite{RepoData}. For each span of marks we select, on $16$ streams, the linear combination with the
smallest quotient, and report in Table~\ref{tab:local} its quotient on $16$ other streams.
```

("mark" gloss is **[author to confirm]**.)

Lead-ins for the three findings (replace the bare "(i)", "(ii)", "(iii)"):

```latex
(i) \emph{The slow combination is spread over the three $-I$ plaquettes.} In the basis of marks used, ...
(ii) \emph{No lowest value is reached.} The values decrease as the span grows, on both backgrounds, ...
(iii) \emph{The low quotient is not confined to $-I$.} Displacing the frozen holonomy from $-I$ by the round
distance $2/\beta$ leaves the quotient of the single plaquette mark unchanged within the errors (ratio
$1.004(11)$ in a repeated run). For the four-mark average the ratio is $1.034(13)$; one of that run's four
burn-in checks failed. Two displacements are not an interval.
```

Closing paragraph (l.592-594), shortened so that it states only what is specific to this subsection:

```latex
These values are upper bounds for the best constant in the auxiliary statement on these two backgrounds.
```

### 1.15 Measurement 8.2 (l.596-611)

Problems. Opens with a sentence fragment. "regressed on" and "coefficient of determination" are given without
saying what is being predicted from what; negative values of $R^2$ will puzzle a non-statistician until the
"over-fitting offset" remark four lines later. "the tested locally slow combination shows little measured
carry-over into the later observables that were tried" stacks four qualifiers.

Rewrite:

```latex
\emph{Question.} Does the combination that local updates relax most slowly also persist from one time slice
to the next?

\emph{Setup.} Same lattice and frozen slice as in Section~\ref{s:local}, with fresh streams. We try to predict
the $308$-mark combination selected there by a linear fit to the same $308$ marks one time slice later. The
later marks are taken in two gauge-invariant forms: with reference directions on the later slice, and
transported back along time-like links to the frozen reference (a mark of the second form is not a function
of the later slice alone). The rule fixed before the runs was: persistence is declared if the fraction of
variance explained on held-out streams exceeds $0.1$.

\emph{Result.} The fractions are $-0.013(2)$ and $-0.002(2)$. A held-out fraction can be negative because of
over-fitting: the same fit at a lag of three slices, where no correlation is seen, gives about $-0.017$. A fit
on $15$ marks gives $0.011(2)$ in the transported form. The correlation of the combination with its
transported copy is $0.083(6)$ at one slice, against $0.032(5)$ on a sampled background, and $0.016(6)$ at two
slices.

The rule was not met: these fits do not predict the combination from the next slice. This does not bound the
best prediction from the later slice and does not exclude other combinations that persist. It shows that
slowness under local updates and slowness in time are different properties, which is why
Hypothesis~\ref{h:mix} is stated separately from the auxiliary statement.
```

### 1.16 Measurement 8.3 (l.613-635)

Problems. "time extents two and four times the side" does not say which lattice has which, and l.628 then
speaks of "the longer time extent" as if both had both. "a common physical lag (one and two time steps)" needs
"respectively". "two-time energy" and $\mathcal E_N$ are never defined. Item 3's last two sentences are hard
to parse ("contained no such test ... could change it again").

Rewrite of the opening and of item 1's first sentence and item 3:

```latex
\emph{Question.} Can one function of the coarse links decorrelate more slowly on the finer of two lattices
than on the coarser? Hypothesis~\ref{h:coarse} would limit by how much.

\emph{Setup.} Sides $N=5$ and $N=10$ at couplings $3.196581051$ and $3.493705679$, matched
in~\cite{RepoData} at a fixed renormalised coupling. For each side there are ensembles with time extent $2N$
and with time extent $4N$. The lag is one time step on side $5$ and two on side $10$, the same physical time.
A test $f$ is a function of the links of side $5$, evaluated also on the coarse links of side $10$. Let $C_f$
be its connected two-time correlation, $\mathcal E_N(f)=C_f(0)-C_f(\mathrm{lag})$ on side $N$, and
$\mathsf R_N(f)=\mathcal E_N(f)/C_f(0)$, so that $1-\mathsf R_N$ is the correlation retained over the lag.
```

(The formula for $\mathcal E_N$ and the ensemble description are my reading; **[author to confirm]**.)

```latex
\item \emph{What this does not show.} Hypothesis~\ref{h:coarse} compares the smallest deficits of the two
lattices, and $\varepsilon_i$ is a difference of deficits; the values of one test do not measure it. The
result also depends on the span: the span of $16$ functions contained no test with a ratio this low, and a
larger span could contain a lower one.
```

### 1.17 Smaller sentences

| Line | Passage | Issue | Replacement |
|---|---|---|---|
| 134 | "They are trial values, one-sided by nature" | "one-sided by nature" is opaque | "Each is found by trying particular functions, so it bounds a best constant from one side only" |
| 276 | "on one trajectory" | undefined | "along one sequence of lattices" |
| 210 | "moments $d_{v,n}$" | called "differences" elsewhere | "differences $d_{v,n}$" |
| 330-331 | "The criterion is on the diagonal, for single vectors, and positivity is what excludes cancellation" | compressed | "The criterion uses only the diagonal quantities $d_{v,n}\ge0$, so no cancellation between vectors can hide slow decay" |
| 387 | "The example is a recurrence, not a lattice theory." | fine; keep | -- |
| 391-394 | Remark `r:reset` | "carrying two equally likely fine labels, the difference of the labels gives" is too compressed to follow | add one sentence first: "Take a coarse event $A$ of probability $\epsilon$ and attach to it a fine variable $\sigma=\pm1$, each sign with probability $\tfrac12$, that the dynamics keeps until an independent reset at rate $\ell$. Then $f=\mathbf 1_A\sigma$ lies in the range of $B$ and $\langle f,S_tf\rangle=e^{-\ell t}\|f\|^2$ for every $\epsilon$." **[author to confirm it is the intended example]** |
| 419 | "the sum of the six staples of the link" | "staple" undefined | "the sum of the six staples of the link (a staple is the product of the other three links of a plaquette through it)" |
| 513-516 | "Each of the three claims is that ... or vanish." | 60-word sentence stating the first-zero principle | "Each claim says that a $C^1$ function $\phi$ on $(0,\infty)$ with a definite sign near $0$ has no zero. If it had one, there would be a first zero $k_0$, and there $\phi'(k_0)$ would be zero or of the sign opposite to that of $\phi$ near $0$. In each case below we show that $\phi'$ has the same sign as $\phi$ at any zero." |
| 660-661 | "We cannot estimate the distance to any of these, and we do not know that this route is the right one." | good plain sentence; keep as the single closing caveat | -- |

---

## 2. Terms used before definition, or never defined

"Gloss" means a clause of at most ten words at first use; full definitions stay where they are.

| Term | First use | Defined | Proposed gloss and place |
|---|---|---|---|
| mass gap | l.10 (abstract) | never in words; implicit in Thm 1(1) | l.22: "... that it has a mass gap, that is, an interval $(0,\Delta)$ free of spectrum of the Hamiltonian?" |
| mesh | l.23 | never | l.23: "as the mesh (the lattice spacing) is halved" |
| fixed physical box | l.23 | never | l.23: "in a box of fixed physical size" ; in Section 2 add: "A \emph{fixed physical box} has side $Na$ constant as $a\to0$." |
| coarse lattice / coarse links | l.42-44 | l.168-169 | l.43, as in rewrite 1.4: "Each coarse link is the product of two consecutive fine links." |
| time slice / slice | l.43 | l.158 | l.43: "a function of the fine links at one time" |
| coarse fields / coarse backgrounds | l.12, l.47, l.87 | never; three names (fields, backgrounds, links) for one thing | choose one ("coarse background" = a configuration of the coarse links of a slice), define it in the "Coarse links" paragraph of Section 2, and use it throughout |
| exceptional set | l.12, l.48 | never as a set; only $B$ in Thm 2 and $A_\theta$ in Thm 3 | l.48: "an exceptional set, that is, a chosen set of coarse backgrounds on which no decay is assumed" |
| interacting estimates | l.13, l.49 | never | replace by "estimates for the interacting theory" (see 1.1, 1.4) |
| deficit | l.79 | l.79, formula only | add after l.79 or in the paragraph after (see 1.6): "the amount by which $\|S_t\|$ falls short of $1$" |
| inherited deficit ($b$) | Table 1, l.191 | never in text | Table 1: "$b$: deficit of the coarse part, $1-\|PS_tP\|\ge b$" |
| centred functions | l.85 | never | "functions with vacuum expectation zero" (see 1.6); also l.252 |
| transfer semigroup / transfer operator | l.86 | l.161-166 | l.86: forward pointer "(Section~\ref{s:set})" is enough once the "In words" paragraph precedes it |
| vacuum representation | l.86 | l.163 | drop from l.86 (not needed there; see 1.6) |
| gate | l.91 (title), l.130 | never; used as a defined term from l.130 on | Thm 3: "We call $A_\theta$ a \emph{gate}." |
| plaquette | l.92 | l.157, in passing | l.92: "the sum over plaquettes $p$ (unit squares of the lattice)" in Section 2; in Thm 3 write "$\sum_p$ over plaquettes" |
| coarse plaquette | l.94 | l.94 and l.170 | fine |
| holonomy | l.95 | l.171 (coarse plaquette only) | see 1.7 |
| round distance | l.95 | l.155 | see 1.7 |
| Wilson measure | l.92 | l.156 | fine (formula is in the theorem) |
| sharp constant | l.130 | never | "the constant $p_{6\beta}(\theta)$" |
| budget | l.128 (via Hyp 3), l.222 | l.267-273 | l.127: "a further summability condition, the budget" |
| colour | l.173 | l.173 | defined at first use, but the word collides with gauge "colour" for any reader who knows the physics; consider "update class". If kept, add "(a label for a class of updates; no relation to gauge colour)" |
| local quotient | l.178 | l.178 | fine; repeat the formula at l.258 (see 1.10) |
| local mixing (auxiliary) | Fig. 1, l.224 | l.258 | fine after rewrite 1.10; make the figure label "Auxiliary local mixing" to match Table 3 |
| good backgrounds | l.258 | never | "backgrounds outside the gates" |
| matched coupling / renormalised coupling | l.263, l.551 | never | l.263: "at the coupling that keeps a chosen renormalised coupling fixed (Section~\ref{s:cross})" |
| return weight ($\kappa$) | Table 1, l.268 | never in text | covered by the "In words" paragraph (1.6) |
| trajectory | l.276 | never | "sequence of lattices" |
| component theories / pure phases | l.285, l.328 | never | l.285: "component theories (the pieces of a decomposition into pure phases)"; or cut Remark `r:crit`(c) to "In a theory that decomposes into components the criterion may be applied in one of them" |
| contact terms | l.290 | never | cut the clause or gloss "terms supported where points coincide" |
| tilted law / tilt | Table 1 l.194, l.398 | l.399 implicitly | Table 1: "probability of a cap of radius $\theta$ under density $\propto e^{k\,u\cdot v}$" |
| staple | l.419 | never | see 1.17 |
| stream | l.544 | never | see 1.13 |
| predicates | l.544 | never (project jargon) | "pass rules" |
| frozen (coarse) background | l.548 (heading) | l.552, implicitly | see 1.14 |
| mark | l.556 | never | see 1.14 |
| span (of marks) | l.556 | never | "the linear span of a list of marks" at l.556 |
| training / held-out streams | l.570 | implicit l.557-558 | fine after rewrite 1.14 |
| burn-in check | l.588 | never | "equilibration check" or add "(a test that the sampler had equilibrated)" |
| coefficient of determination | l.601 | never | "fraction of variance explained" (see 1.15) |
| two-time energy, $\mathcal E_N$ | l.621-623 | never | see 1.16 |
| trial values | l.134, l.592, Table 3 | never | define once in the opening of Section 8 (see 1.13) and use only in Table 3 |

Symbol collisions that slow a first reading (none needs a change of mathematics):
$R$ is the Bessel ratio (l.114), the multiplication by $\mathbf 1_{A_\theta}$ (l.467) and, in sans-serif, the
two-time quotient (l.617); $p$ is a plaquette (l.92), $p_k(\theta)$ (l.101) and $p:=R'$ (l.505); $E$ is a
spectral measure (l.312), a spectral projection (l.344) and, as $\E$, expectation; $M$ is a number of gates
(l.482), $M_i$ a product (l.268) and $M_f$ a multiplication operator (l.442); $L$ is a bound in Prop. 4
(l.116), a spectral cut-off (l.344) and, as $\mathsf L$, the transfer operator; $G$ is the good projection
(l.74) and the gauge group (l.295); $d$ is the deficit and $d_{v,n}$ the differences. Cheapest fixes:
rename the multiplication operator of Corollary `c:vac` to $\chi$ or $M_\theta$; write $\varrho:=R'$,
$q:=R/k$ in Section 7; write $\mathsf G$ or "the gauge group" at l.295; rename the cut-off $L$ in the proof of
Theorem 2 to $\Lambda$ or $\mu$.

---

## 3. A plain-words paragraph for the refinement route

Yes. The natural place is a new short subsection between "The two questions" and "Statements" (it plays the
role of the "physical description" section). It replaces nothing and claims nothing. Draft (118 words):

```latex
\subsection{The idea in words}
Draw a square grid, and over it a second grid with squares twice as wide. A field on the fine grid gives one
on the coarse grid: multiply the two fine links under each coarse link. With six fine sites on a side there
are three coarse ones, and a coarse square has eight fine links on its boundary. Any observable of the fine
field is the sum of its best guess from the coarse field and a remainder, the detail that the coarse field
does not see. If the guess decays in time as on the coarse lattice, and the detail is forgotten within a few
steps except on rare coarse fields that seldom recur, then the fine lattice keeps almost all of the coarse
decay. Theorem~\ref{t:inh} makes this precise.
```

---

## 4. Section order and headings

4.1 **Rename Section 3 "Architecture" to "Outline and the open hypotheses".** "Architecture" does not tell the
reader that the three hypotheses, which are the content of the paper's open part, are stated there. Give the
hypotheses their own subsection heading ("The three open hypotheses") so that they appear in the table of
contents.

4.2 **Move subsection 3.1 ("The external construction and what compatibility would require") to the end, as
a subsection of "What remains".** It is about what would be needed after everything in Figure 1, it rests on a
second-hand reading, and at present it is the densest page and stands between the outline and the first
proof. Section 10 already repeats its last paragraph in brief (l.657-660); merged, the list appears once.

4.3 **Move the statement of Proposition 4 from "Statements" to Section 7**, leaving the two-sentence pointer
of 1.8. The main-results subsection then has exactly the three theorems the abstract names.

4.4 **Rename 1.2 "Statements" to "Main results"**, and insert the new "The idea in words" before it (Section 3
above).

4.5 **Move 1.4 "Sources of the results and status of verification" to the end and merge it with Section 9
"Machine-checked parts"** under a heading such as "Provenance and verification". It is an honest and
necessary statement, but as the last thing in the introduction it is a 13-line paragraph about sessions and
drafts before the reader has seen any mathematics. Keep one sentence in the introduction:

```latex
How the results were obtained, which parts are machine-checked, and the fact that the paper has not been
peer reviewed are set out in Section~\ref{s:disc}.
```

4.6 **Put a forward pointer before Theorem 3** rather than moving "Setting and notation" ahead of the
statements: "Terms used in Theorem~\ref{t:ret} are defined in Section~\ref{s:set}." Early theorems are worth
more than strict order.

4.7 **Move Table 1 to the head of Section 2**, before the four definition paragraphs, and add the missing
symbols ($\lambda$, $\Delta$, $r$, $\theta$, $K_i$, $M_i$, $\varepsilon_i$, $\mathcal E_N$). A reader looking
up a symbol looks for the table first.

4.8 **Rename the measurement subsections as the questions they answer**:
"How slow can local relaxation be on a frozen background?" (8.1);
"Does the locally slow combination persist in time?" (8.2);
"One test function on two lattices" (8.3).

4.9 **Remark `r:ret`**: four unrelated items (a)-(d) in one remark. Split off (a) as a corollary or a
separately titled remark ("Many gates"), because Hypothesis 1 ("exceptional projections $B_i$ built from
gates") and Section 10 ("gates wide enough") depend on it, and (b) as a remark titled "Size of the bound".

4.10 Keep "What is not claimed" where it is, shortened as in Section 5. A short list of non-claims straight
after the statements is the right single home for the caveats.

---

## 5. Repetition of disclaimers

The honest content should stay; each caveat needs one home (plus, at most, the abstract and the status table).

**(A) "No mass gap is proved."** Seven places: abstract l.14; l.31 "We do not supply it"; l.122 item 1;
l.207-208 "Nothing below it in the figure is proved"; l.278 "still not a mass gap"; Table 3 "Mass gap: not
proved"; l.654-661. Best single placement: l.122 (item 1 of "What is not claimed"). Keep also the abstract
clause and the Table 3 row, which are different kinds of object. In the introduction keep the short "This
paper does not supply it" because it completes the sentence before it. Cut l.207-208 (replaced by rewrite
1.9) and l.278-279 (replaced by the pointer in rewrite 1.11).

**(B) "We have not examined / verified / read the construction [OAI]."** Six places: l.123-125; l.205 "have
not verified"; Fig. 1 caption "cited, not verified here"; l.291; l.659-660 "a candidate that we have not
connected to these lattices"; bibliography l.697 "Not read by us". Best single placement: l.123-125. Keep the
bibliography note (it is a citation practice, not a disclaimer). In the figure, "cited" in the box is enough;
drop "not verified here" from the caption. Cut l.291, replacing it by "(all taken from the assessment)".

**(C) "The measurements support nothing / are not bounds / are not used in a proof."** Seven places:
l.133-134; l.545-546; l.549; l.592-594; l.608-609; l.631-634; Table 3 "trial values". Best single placement:
the opening of Section 8 (rewrite 1.13), which explains why a trial is one-sided, so the later subsections
need not repeat it. Item 5 at l.133 can shrink to "The measurements of Section~\ref{s:evid} are Monte Carlo
estimates on small lattices; none is used in a proof." In each subsection keep only the sentence that is
specific (what that particular measurement does not show): l.608-609 and item 3 at l.631 are specific and
should stay; l.592-594 becomes one sentence (see 1.14).

**(D) "This is about the auxiliary statement, not Hypothesis 1."** Five places: l.258-260; l.549;
l.593-594; l.609-611; Remark `r:haar` l.537-539, plus the figure caption l.245-246. Best single placement:
l.258-260 (rewrite 1.10), where the auxiliary statement is defined. Keep the half-sentence in the "Question"
line of 8.1 and the conclusion of 8.2 (which is the evidence for the distinction). Cut "and say nothing about
the constant $\gamma$ of Hypothesis 1" at l.593-594.

**(E) "Cited, not rederived / not reread / not reproduced / not recalibrated."** l.109 "which we cite and do
not rederive"; l.256 "which we neither reproduce nor verify here"; l.435-436 "without proof"; Fig. 1 caption
"uses the cited transfer-matrix representation"; Table 3 "proved from the cited transfer-matrix
representation"; bibliography l.694-695 and l.699 "not reread for this paper"; l.552 and l.615 "not
recalibrated here". Best placement for the transfer matrix: l.435-436, at the point of use, plus the Table 3
row; at l.109 write only "which we cite". For the calibration: say it once, in the opening of Section 8:
"Couplings are taken from the calibration in~\cite{RepoData} and were not recalibrated for this paper."

**(F) "Theorem 2 is conditional."** l.126-129; l.206-207; l.275. Best placement: l.126-129. Rewrite 1.9 says
it once in the outline in the form "the three hypotheses are open".

**(G) "Agreement among sessions is not peer review" and the verification status.** Only in l.137-150 and
Section 9; not repeated, but long. See 4.5.

Two sentences that sound defensive rather than informative and can go without loss: l.35 "worth stating
because it fits a theory known through correlation functions" (the rewrite 1.3 drops it); l.495 "and we make
no use of it" (the remark already says "crude").

---

## 6. Tables and figure

**Figure 1.**
- The caption defines a dashed arrow as "an implication that would hold if the open statement at its tail
  were proved". Two dashed arrows have proved statements at their tails: Prop. 4 -> auxiliary, and Thm 1 ->
  mass gap. The caption patches the first by a special clause and is silent on the second. Simpler rule:
  draw an arrow solid when its tail is proved and dashed when its tail is open; then Thm 1 -> gap and
  Prop. 4 -> auxiliary are solid, and the caption needs no exception beyond "Proposition 4 bounds one term of
  the auxiliary statement and does not imply it" (or draw that one arrow dotted with the label "one term").
- Box "Uniform in the volume; same theory as [OAI]" is two different open statements in a telegraphic label.
  Split into two boxes or write "Uniformity in the volume; identification with a continuum theory".
- Box "Positive deficit in a fixed physical box" is the only box on the main path without a numbered result.
  Add "Cor.~\ref{c:acc}, conclusion".
- The budget box points at the box "Thm 2, Cor 2", but the budget is an input of Corollary 2 only. Either
  give Corollary 2 its own box under Theorem 2, or say in the caption "Hypothesis 3 enters through
  Corollary 2".
- Label "Local mixing (auxiliary)" vs Table 3 "Auxiliary local mixing": use one.
- Proposed caption:

```latex
\caption{Outline. Solid boxes are proved in this paper; Corollary~\ref{c:vac} uses the transfer-matrix
representation of~\cite{Lu77,OS78}. Dashed boxes are open. The dotted box is cited. An arrow from $X$ to $Y$
means that $X$ is an input of $Y$; it is solid when $X$ is proved and dashed when $X$ is open.
Proposition~\ref{p:haar} bounds one term of the auxiliary statement and does not imply it.
Hypothesis~\ref{h:budget} enters through Corollary~\ref{c:acc}.}
```

**Table 1 (symbols).**
- Row "$\gamma$, $\kappa$, $b$, $d$": "inherited deficit" for $b$ is not used anywhere in the text and is
  easily confused with $d$. Write "$b$: deficit of the coarse part" and "$d$: deficit $1-\|S_t\|$ of the whole
  space".
- "bare coupling" for $\beta$: the text only ever calls $\beta$ the weight parameter of the Wilson measure;
  write "coupling parameter of the Wilson weight".
- "cap probability at tilt $k$": "tilt" is not defined; see Section 2.
- "its vacuum" for $\Omega$: write "its positive leading eigenfunction (the vacuum)".
- $\mathsf R(f)$ row: the formula uses "lag" in roman inside mathematics; give the words: "fraction of the
  correlation of $f$ lost over the lag".
- Missing: $\lambda$, $\Delta$, $r$, $\theta$, $K_i$, $M_i$, $\varepsilon_i$, $d_i$, $\mathcal E_N$.

**Table 2 (local quotient).**
- The notation ".0208(5)" is not explained. Add to the caption: "The digit in parentheses is the jackknife
  standard error in the last digit."
- Row labels: "frozen background with three $-I$ plaquettes" hides that this is the specially built
  background of the text; "background sampled from the measure, every coarse plaquette at distance $>1.1$ from
  $-I$" does not say whether it is one sampled background or many, nor whether it is then frozen. Suggested
  labels: "constructed background (three coarse plaquettes at $-I$)" and "one background sampled from the
  Wilson measure and then frozen; all coarse plaquettes farther than $1.1$ from $-I$" **[author to confirm
  one/many]**.
- Caption: "on the two backgrounds" / "on the first" forces the reader back to the rows; write "on the
  constructed and the sampled background respectively" and "on the constructed background". Add "smaller
  means slower relaxation".
- Proposed caption:

```latex
\caption{Local quotient $\mathcal J/\mathcal V$ (smaller means slower relaxation under the local updates) of
the combination selected on $16$ streams, evaluated on $16$ other streams. The digit in parentheses is the
jackknife standard error in the last digit. For comparison, the average of the four plaquette marks of one
coarse plaquette gives $.047$ on the constructed background and $.09$ on the sampled one, and a single
plaquette mark gives $.062$ on the constructed background.}
```

**Table 3 (status).**
- Clear. Two small points: "Theorem 3: proved; $\SU(2)$, periodic time" mixes status and scope, while the
  other rows give status only; either add a "Scope" column or write "proved for $\SU(2)$ on a lattice periodic
  in time". "Volume uniformity; continuum identification: open; not addressed" should match the figure label
  after it is changed.
- Caption "Status of every statement" duplicates l.654; cut the sentence at l.654 to "Table~\ref{tab:status}
  gives the status of each statement."

---

## 7. Twelve most valuable edits (also returned as the final message)

1. Abstract, l.10-14 -> the two-sentence abstract of 1.1.
2. After Theorem 2, l.85-89 -> the "In words" paragraph and the application paragraph of 1.6.
3. New subsection "The idea in words" before "Statements" -> the 118-word paragraph of Section 3.
4. Architecture opening, l.204-210 -> rewrite 1.9 (fixes "three of them are open" and "Nothing below it in the
   figure is proved").
5. Introduction, l.42-51 -> rewrite 1.4 (glosses coarse links; "cannot hold uniformly" -> "we do not expect
   ... we measure"; "interacting estimates" -> "estimates for the interacting theory").
6. Theorem 3: add "We call $A_\theta$ a \emph{gate}." and replace l.106-109 by the "In words" paragraph of 1.7.
7. Section 8 opening, l.543-546 -> rewrite 1.13 (defines stream and trial, states the caveat once).
8. Section 8.1, l.549-558 -> Question/Setup rewrite of 1.14 (defines frozen background and mark).
9. Section 8.3, l.614-618 -> Question/Setup rewrite of 1.16 (defines $\mathcal E_N$, says which lag is which).
10. Move Proposition 4's statement to Section 7 with the two-sentence pointer of 1.8; move 1.4 "Sources ..." to
    the end, merged with Section 9, leaving one sentence.
11. Subsection 3.1 -> move into "What remains" and turn its two long sentences into the lists of 1.12; rename
    Section 3 "Outline and the open hypotheses".
12. Figure 1 caption and arrows -> the caption of Section 6, with arrows solid when the tail is proved.
