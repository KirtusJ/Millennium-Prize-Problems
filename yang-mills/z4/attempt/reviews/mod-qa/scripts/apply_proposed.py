"""Apply the proposed replacements to a scratch copy of main.tex. Usage: python3 -I apply_proposed.py IN OUT
Every old string must occur exactly once; otherwise the script stops and changes nothing."""
import sys
src = open(sys.argv[1]).read()
E = []
def e(tag, old, new): E.append((tag, old, new))

e("D1 abstract",
"We prove one\nof the three for $\\SU(2)$; the other two are open, and no mass gap is proved.",
"We prove one\nof the three for $\\SU(2)$. The other two are open, and so is a third condition needed to chain the\nsteps; no mass gap is proved.")

e("D2 intro; disclaimer D l.47-48",
"route meets slow trial directions on selected coarse backgrounds (Section~\\ref{s:local}); whether the decay\nin time is slow there as well is not known. This is a reason to allow exceptions.",
"route meets slow trial directions on selected coarse backgrounds (Section~\\ref{s:local}). This is a reason to allow exceptions.")
e("D2 intro count",
"and Theorem~\\ref{t:ret} proves a return bound of that kind for $\\SU(2)$. Two estimates for the interacting\ntheory remain open: decay of the remainder off the exceptional set, and the comparison of the predictable\npart with the coarse lattice.",
"and Theorem~\\ref{t:ret} proves a return bound of that kind for $\\SU(2)$. Three statements about the\ninteracting theory remain open: decay of the remainder off the exceptional set (Hypothesis~\\ref{h:mix}), the\ncomparison of the predictable part with the coarse lattice (Hypothesis~\\ref{h:coarse}), and, for chaining the\nrefinement steps, a bound on the accumulated losses (Hypothesis~\\ref{h:budget}).")

e("terms: Table 1 cited",
"In the application (terms are defined in Section~\\ref{s:set})",
"In the application (terms are defined in Section~\\ref{s:set}; symbols are listed in Table~\\ref{tab:sym})")

e("terms: holonomy, round distance in Thm 1.3",
"let $A_\\theta$ be the event that the holonomy around that plaquette lies within round distance $\\theta$ of\n$-I$; we call $A_\\theta$ a \\emph{gate}.",
"let $A_\\theta$ be the event that the holonomy around that plaquette (the ordered product of its eight fine\nlinks) lies within round distance $\\theta$ of $-I$ (the angle between the two as points of $S^3$); we call\n$A_\\theta$ a \\emph{gate}.")
e("terms: delete late parenthesis",
"depend on the spatial volume, on the time separation or on the rest of the field. (The holonomy of a\nplaquette is the ordered product of the links around it; the round distance is the angle on $S^3$; see\nSection~\\ref{s:set}.) The gate is centred",
"depend on the spatial volume, on the time separation or on the rest of the field. The gate is centred")

e("D3 further results",
"A fourth result, Proposition~\\ref{p:haar} in Section~\\ref{s:haar}, gives a sharp lower bound for the\nconditional variance of a single link. It bounds one term of an auxiliary statement and is not an input of\nTheorem~\\ref{t:inh}.",
"Two further results are proved. Proposition~\\ref{p:three} in Section~\\ref{s:crit} is a form of the criterion\nthat uses a single time separation. Proposition~\\ref{p:haar} in Section~\\ref{s:haar} gives a sharp lower bound\nfor the conditional variance of a single link; it bounds one term of an auxiliary statement and is not an\ninput of Theorem~\\ref{t:inh}.")

e("D4 not claimed item 3",
"\\item Theorem~\\ref{t:inh} is conditional. Its first and third hypotheses, with the sums that the accumulation over\nrefinements needs, are not proved on any trajectory of matched couplings (Hypotheses~\\ref{h:mix},\n\\ref{h:coarse} and~\\ref{h:budget}). Even with all of them the conclusion concerns a\nfixed physical box and is not a gap in infinite volume.",
"\\item Theorem~\\ref{t:inh} is conditional. Of its three hypotheses the second is proved for $\\SU(2)$\n(Corollary~\\ref{c:vac}). The first and the third are open (Hypotheses~\\ref{h:mix} and~\\ref{h:coarse}), and so\nis the budget that chaining the steps needs (Hypothesis~\\ref{h:budget}); none is proved on any trajectory of\nmatched couplings. Even with all of them the conclusion concerns a fixed physical box and is not a gap in\ninfinite volume.")

e("disclaimer C item 5",
"\\item The measurements of Section~\\ref{s:evid} are Monte Carlo estimates on small lattices, at finite\nstatistics. They are trial values, one-sided by nature, and none is used in a proof.",
"\\item The measurements of Section~\\ref{s:evid} are Monte Carlo estimates on small lattices, at finite\nstatistics; none is used in a proof.")

e("terms: centred",
"is applied with $A=S_1$ restricted to the\ncentred gauge-invariant functions.",
"is applied with $A=S_1$ restricted to the\ngauge-invariant functions that are \\emph{centred}, that is, have vacuum expectation zero.")

e("terms: background, box, matched, trajectory",
"its holonomy is the product of its eight fine links.\n",
"its holonomy is the product of its eight fine links. A \\emph{background} is a configuration of the coarse\nlinks of a slice.\n\n\\emph{Refinement sequence.} A \\emph{fixed physical box} is a sequence of lattices of mesh $a_i=a_0/2^i$ and\nspatial side $N_i=2^iN_0$, so that the side $N_ia_i$ in physical units does not change. Couplings $\\beta_i$ are\n\\emph{matched} if a chosen renormalised coupling at the scale of the box has the same value on every lattice\nof the sequence; such a sequence of lattices and couplings is a \\emph{trajectory of matched couplings}.\n")

e("D9 figure aux box",
"(aux) {Local mixing (auxiliary)\\\\ Section~\\ref{s:local}};",
"(aux) {Local mixing (auxiliary)\\\\ Section~\\ref{s:arch}; trials in \\S\\ref{s:local}};")
e("D9 figure box",
"(box) {Positive deficit in a fixed\\\\ physical box (Cor.~\\ref{c:acc})};",
"(box) {Positive deficit in a fixed\\\\ physical box};")
e("disclaimer E caption",
"\nProposition~\\ref{p:haar} bounds one term of the auxiliary statement and does not imply it.\nHypothesis~\\ref{h:budget} enters",
"\nHypothesis~\\ref{h:budget} enters")

e("D10 Hyp 3.1",
"exceptional projections $B_i$ built from gates as in Theorem~\\ref{t:ret}\nand $G_i=Q_i-B_i$,",
"exceptional projections $B_i$ built from gates as in Corollary~\\ref{c:vac},\n$Q_i=I-P_i$ the complement of the coarse projection $P_i$ and $G_i=Q_i-B_i$,")

e("disclaimer A l.304",
"separate condition (Remark~\\ref{r:budget}). A positive limit of deficits in a box is still not a mass gap;\nuniformity in the volume and the identification of the limit with a continuum theory would remain.",
"separate condition (Remark~\\ref{r:budget}). Uniformity in the volume and the identification of the limit with\na continuum theory would remain.")

e("terms: staple",
"with $\\Sigma$ the sum of the\nsix staples of the link, each a unit quaternion;",
"with $\\Sigma$ the sum of the\nsix staples of the link (a staple is the ordered product of the other three links of a plaquette through the\nlink; a link lies in six plaquettes), each a unit quaternion;")

e("F-4 raw data",
"Programs, seeds, raw data, the pass\nrules fixed before each run and the rules that failed are in~\\cite{RepoData}.",
"Programs, seeds, the pass rules fixed\nbefore each run and the rules that failed are in~\\cite{RepoData}. The per-chain data are deposited for\nSection~\\ref{s:cross} and for item~(iii) of Section~\\ref{s:local}; for Table~\\ref{tab:local} the analysis\noutputs are deposited, and for Section~\\ref{s:time} the report only, so that those two are reproduced by\nrerunning the sampler from the recorded seeds.")

e("disclaimer D l.603",
"$\\mathcal J/\\mathcal V$ be? This concerns the auxiliary local mixing statement, not Hypothesis~\\ref{h:mix}.",
"$\\mathcal J/\\mathcal V$ be?")

e("D8 Table 2 row label",
"background sampled from the measure, every coarse plaquette at distance $>1.1$ from $-I$ &",
"frozen background drawn once from the measure, every coarse plaquette at distance $>1.1$ from $-I$ &")

e("disclaimer C l.647",
"The true quotients of these trial combinations bound from above the best constant in the auxiliary statement\non these two backgrounds; the numbers in the table are estimates of them, with the errors shown, not certified\nbounds.",
"The numbers in the table are estimates, with the errors shown, not certified bounds.")

e("F-6 span dimension",
"\\item \\emph{Normalised quotients.} In a span of $54$ functions, the test",
"\\item \\emph{Normalised quotients.} In a span of $54$ functions ($48$ linearly independent on the training\nstreams), the test")

e("F-5 Lean versions",
"Two Lean~4 files with Mathlib accompany the paper~\\cite{RepoLean}; both",
"Two Lean~4 files with Mathlib accompany the paper~\\cite{RepoLean} (Lean 4.19.0, Mathlib v4.19.0); both")

e("F-3 cite order",
"proofs by a session of OpenAI Codex~\\cite{RepoRet,RepoInh}.",
"proofs by a session of OpenAI Codex~\\cite{RepoInh,RepoRet}.")
e("D11 provenance",
"including the periodic-time form of Theorem~\\ref{t:ret} and\nProposition~\\ref{p:vac},",
"including the periodic-time form of Theorem~\\ref{t:ret}, Lemma~\\ref{l:trace}, Proposition~\\ref{p:vac} and\nCorollary~\\ref{c:vac},")
e("disclaimer F s:disc",
"Lemma~\\ref{l:scal}, the inequality of Corollary~\\ref{c:acc}, the\nfinite-dimensional form of Theorem~\\ref{t:inh} and the scalar steps of Proposition~\\ref{p:haar} are checked\nin Lean~4 with Mathlib (Section~\\ref{s:lean}); nothing else is.",
"The machine-checked parts are listed in\nSection~\\ref{s:lean}; nothing else is machine-checked.")

e("D5 what remains",
"Table~\\ref{tab:status} lists every statement and its status. To turn Figure~\\ref{f:arch} into a proof of a\nmass gap by this route one would need, at least: Hypothesis~\\ref{h:mix}, with gates wide enough to contain the\nbackgrounds on which decay is slow and still within the budget of Hypothesis~\\ref{h:budget};\nHypothesis~\\ref{h:coarse}; estimates uniform in the physical volume; the identification of the limiting\nsemigroup with the Hamiltonian of a continuum theory satisfying the axioms, for which~\\cite{OAI} is a\ncandidate that we have not connected to these lattices; a finite mass;",
"Table~\\ref{tab:status} lists the numbered statements and the steps of Figure~\\ref{f:arch} with their status. To\nturn the figure into a proof of a mass gap by this route one would need, at least: Hypothesis~\\ref{h:mix}, with\ngates wide enough to contain the backgrounds on which decay is slow; Hypothesis~\\ref{h:coarse};\nHypothesis~\\ref{h:budget} for those gates and losses; estimates uniform in the physical volume; the\nidentification of the limiting semigroup with the Hamiltonian of a continuum theory satisfying the axioms, for\nwhich~\\cite{OAI} is a candidate; a finite mass;")

e("D6 table rows a",
"Theorem~\\ref{t:ret} & proved; $\\SU(2)$, periodic time \\\\\n",
"Theorem~\\ref{t:ret} & proved; $\\SU(2)$, periodic time \\\\\nLemma~\\ref{l:scal}, Lemma~\\ref{l:cap} & proved; Lemma~\\ref{l:scal} checked in Lean \\\\\n")
e("D7 table Hyp 3.1",
"Hypothesis~\\ref{h:mix} & open; not measured \\\\",
"Hypothesis~\\ref{h:mix} & open; not measured (Section~\\ref{s:time} tests one combination's carry-over in time and gives no bound) \\\\")
e("D6 table rows b",
"Volume uniformity; continuum identification & open; not addressed \\\\\n",
"Volume uniformity; continuum identification & open; not addressed \\\\\nFinite mass; all compact simple groups & open; not addressed \\\\\n")
e("D6 caption",
"\\caption{Status of every statement.}",
"\\caption{Status of the numbered statements and of the steps of Figure~\\ref{f:arch}.}")

e("F-3 Repo commit",
"entries below are paths in it at commit \\texttt{db2edcb} or later.",
"entries below are paths in it at commit \\texttt{c7c2a16}.")
e("F-3 RepoInh",
"\\texttt{full-complement/} (source derivation of Theorem~\\ref{t:inh} and of the bound of the transfer form by\nlocal losses).",
"\\texttt{yang-mills/joint-refinement/full-complement/} (source derivation of Theorem~\\ref{t:inh} and of the\nbound of the transfer form by local losses).")
e("F-3 RepoLean",
"\\texttt{b2-haar/haar.lean}.",
"\\texttt{b2-haar/haar.lean} in the same folder \\texttt{reviews/}; statement digests in \\texttt{LEAN\\_PINS.md}\nbeside the source of this paper.")

bad = [(t, src.count(o)) for t, o, n in E if src.count(o) != 1]
if bad:
    print("NOT APPLIED; counts != 1:", bad); sys.exit(1)
out = src
for t, o, n in E:
    assert out.count(o) == 1, t
    out = out.replace(o, n)
open(sys.argv[2], "x").write(out)
print(len(E), "replacements applied")
