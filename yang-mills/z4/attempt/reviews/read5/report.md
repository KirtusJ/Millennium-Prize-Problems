Report of a first-time-reader sub-agent (same model family as the director; not independent review), as handed back; saved by the director. Line numbers are those of the fifth draft (main_draft5.tex is close but not identical).

**Control answer:** the denominator in Theorem t:inh is `1+2/(m\gamma)` — "1 − ‖A^m‖ ≥ (b−κ)_+ / (1+2/(mγ))", glossed in the text as `1+2a/(γt)` for t = ma.

**Read this first**
- `main.tex` changed while I was reading (940 lines at 03:25, 941 lines at 03:31 UTC). Line numbers below are for the 03:31 version. Section 8 itself was not touched by that edit (now lines 618–799).
- That edit already fixed three things I had noted: the undefined `C` in Lemma l:cap, `μ_Haar(A)` in Remark r:ret(d), and the unquantified ε_i in Hypothesis h:coarse.
- I did not edit anything under `/home/user/Millennium-Prize-Problems`. Proposals are in:
  - `/home/user/z4-workers/read5/sec8.tex`
  - `/home/user/z4-workers/read5/intro.tex`
- I share the author's model family. Where I agree with the paper, that is not independent review.

## 1. Places a non-specialist reader stops

**Undefined at first use**
- L10, L22: "mass gap" is never defined in the introduction; the precise form first appears at L836–837.
- L21–24: "lattice gauge theories", "fixed physical box", "mesh" (defined at L199).
- L27–28: "Wilson lattice gauge theory", "submitted in formal form" (to whom, and formal in what sense?), "Its assessors", "Wightman axioms".
- L39: "forget the vacuum" is an idiom, and "vacuum" is not yet introduced.
- L44–49: "links", "local updates", "slow trial directions", "backgrounds", "the dynamics".
- L95: `(b-\kappa)_+` is never defined.
- L99: "transfer semigroup".
- L116–121: β is never named as a coupling; "plaquette", "holonomy" and "round distance" come before Section 2.
- L134: "local quotients" (defined at L209).
- L141: "an auxiliary statement" (defined at L297).
- L154: "trajectory of matched couplings" (L202).
- L175: "plaquette" is never defined as an elementary square.
- L180–183: `\mathsf T_0` is used here but only defined in Lemma l:trace (L477–480).
- L201: "renormalised coupling at the scale of the box".
- L204–206: "colour" and "coarse cells" — the 24 classes are only given by pointing to the repository, so `\mathcal J` cannot be reconstructed from the paper.
- L226: "tilt".
- L312: `d_0` is not said to be the deficit of the coarsest lattice at time t.
- L319: "in the literature" has no citation.
- L344: "pure phases".
- L465: `s_x`, `s_y`.
- L495: "slabs". L499: "isotypic component of spin n/2".
- L517: `P_\Omega` and `\Lambda_1`.
- L621: "started hot or cold". L638: "single-mark runs" before "mark" is defined (L653). L657: "sweeps". L727: "coefficient of determination", with no warning that held-out values can be negative.
- L790: "a different statistic" is not named.
- L836: "non-trivial component theories".

**Sentences I read twice or more**
- L12–14: "three estimates … one of the three … the other two … and so is a third condition" — "third" collides with "three".
- L26: "now has an object to be asked about".
- L40: "a family of vectors that spans" — spans what?
- L47–48: the "natural way to prove the second supposition" sentence.
- L63–65: "two losses, which must both be small…".
- L83: "requires the mass to be finite".
- L118–121: `x` is introduced inside the definition of Γ_θ and then again with `y` (reordered in `intro.tex`).
- L158: "the largest value over the conditional laws that one link can have".
- L162: "limits a constant from one side" (also L629).
- L182: "The operator of the periodic lattice with its time-like links integrated".
- L289: Hypothesis h:mix is a single sentence, and it uses `P_i` before Hypothesis h:coarse defines it.
- L343–347: Remark r:crit (b) is unexplained and (d) has two semicolons.
- L430–435: Remark r:reset — `\E` used as an operator, "two equally likely fine labels", and `S_t` clashing with `S_n`. I read it three times.
- L588–591: the first-zero principle.
- L648–651: the description of background A (three readings).
- L761–763: "time extents two and four times the side" — which lattice has which? The source report suggests 2N for the base runs and 4N for the longer ones.
- L823–832: one nine-line sentence. L838: "which neither it nor the assessment states in this form". L858–864: a parenthesis inside a long sentence.

**Unexplained numbers and apparent inconsistencies**
- L550: β = 3.399810242 appears with no stated origin; no measurement in Section 8 uses it.
- L652 against L682: the selection rule says "farther than π/4" (0.785), the caption says "greater than 1.1". Both can be true, but it reads as a contradiction.
- L655: 15 marks on 3 plaquettes but 49 on 7 — the number of marks per plaquette changes without comment.
- L707 against L670: `.0216(5)` and `.0208(5)` for the same 15 marks at −I, plus `.0207(2)` displaced; it is not said why the reference is the earlier run.
- L727–728: the rule compares with the coefficient of determination on background B, and that value is never reported; the B numbers at L742 are correlations.
- L731, L734, L742: "in the two forms" never says which value is which form. `d2-time/report.md` gives later-slice first, transported second for the first two pairs. For L742 the report only confirms that 0.032 is the transported value.
- L785–786: "0.951 and 0.941" — 0.936 + 2×0.003 is 0.942; the source has 0.9412 from unrounded values, so the number is right but looks wrong. It also coincides with the ratio `0.941(5)`.

**Symbol clashes**
- `A`: operator and background A.
- `R = I_2/I_1` and `\mathsf R(f)`.
- `r`: rate (L74) and polar angle (L126).
- `C`: operator (L478) and correlation `C_f`.
- `E`: spectral measure, spectral projection (L382), and `\E`.
- `g`: function and gauge transformation `g_x`, `g_y` (L491), where `x`, `y` are also slices.
- `m`: steps and the exponent at L517. `ℓ`: L432 and L570. `d`: `d_{v,n}`, `d`, `d_i`.

**Forward references without warning**
- L134–137 (Section 8.1, Corollary c:vac), L141, L288 ("as in Corollary c:vac"), L321, L414.
- The figure node "Local mixing (auxiliary), Section 3" points at the section it sits in.

**Repetition**
- The refinement idea is told three times: L43–54, L56–65 and L103–107.
- "exact value limits a constant from one side / an estimate is not a bound" appears at L162, L629–631 and L684.
- "one lattice, one coupling, two backgrounds" appears at L135, L893, L872.

## 2. Section 8 replacement
File: `/home/user/z4-workers/read5/sec8.tex`. It compiles in a scratch copy with exit 0 and no overfull boxes.

**What changed in structure**
- A new Table `tab:runs` holds the design of the main runs: lattice, coupling, streams, lengths, selection and held-out split.
- Every subsection follows the same order: Question, What we found, Setup, results, checks that failed, what this does not show.
- Conventions and common limits are bulleted.
- The comparison values that were in the caption of `tab:local` are now a short paragraph under it.
- A new small Table `tab:cross` holds the two evaluations of the one test with ratio below one.
- Existing labels are kept.

**Numeral check** (script `/tmp/claude-0/-home-user/4daa3903-136b-5384-a87a-779ce1a94b2a/scratchpad/nums.py`, old lines 618–800 against the new file)
- It strips comments, `\ref`/`\label`/`\cite`, `\SU(2)`, tabular column specifications and subscripts.
- Numerals: 162 tokens, 110 distinct, in both texts; **difference: none**.
- Number words (one to ten, twice, half, halves, both, single): the new text has two more "one", one more "both" and one more "single". They come from the new linking sentences and the `tab:cross` header ("the one fixed test", "one frozen slice" repeated in the lead, "gives both evaluations", "single-mark" in the `tab:runs` caption). None carries a new quantity.

**Caveats on this replacement**
- It is longer: 2352 → 2866 words, and the paper goes from 18 to 20 pages. Easier to scan, not shorter.
- The "What we found" sentences are new prose. I kept them to what the old text states, but they are summaries, which is where errors hide; please read them as closely as the numbers.
- `tab:cross` assigns 0.951 to the held-out pair and 0.941 to the longer ensembles. The old text gives them only "on both pairs" in that order; `f2-cross2/report.md` line 17 confirms the assignment.
- I did not resolve the ambiguities ("in the two forms", "time extents two and four times the side"); the old wording is kept.
- Subscripts (`R_5`, `R_{10}`) were excluded from the count: the new table header repeats them.

## 3. Abstract and Section 1 replacement
File: `/home/user/z4-workers/read5/intro.tex`. It compiles with `sec8.tex` in the same scratch copy.

- **Length:** abstract 84 → 88 words; Section 1 1729 → 1678 words. So it is only marginally shorter; the gain is in order and tone. A real cut would mean moving the three theorem statements out of the introduction, which I did not presume to do.
- **Opening:** starts from the supposition and the two questions as a numbered pair, then says in its own paragraph that no mass gap is proved.
- **One addition:** a one-sentence definition of "mass gap", taken from L836–837.
- **Merged:** the two tellings of the refinement idea become one, with suppositions (a), (b), (c); the hypotheses of Theorem t:inh are then mapped to them.
- **Softened:** "the gap is what is missing" becomes "a gap is what would still be missing"; "A continuum theory … was submitted" becomes "A construction of a continuum theory … was submitted".
- **Verbatim:** Theorems t:crit and t:inh, and the "What is not claimed" list.
- **Reworded, not changed:** in Theorem t:ret only the sentences introducing `x`, `y` and Γ_θ are reordered.
- **Defined:** `(s)_+`.

## 4. Layout (original PDF at 60 dpi, plus the log of a scratch compile)
- **Overfull lines:** none. Underfull lines only in Table 3 and in bibliography entries [7] and [8].
- **Bibliography [7], [8]:** long `\texttt` paths leave visibly stretched lines. Fix: `\raggedright` in the bibliography, or `\path{}`/`\url{}` for the paths.
- **Figure 1 (p. 6):**
  - Node text hyphenates inside 31 mm boxes ("de-cay", "Wight-man", "tri-als"). Fix: add `\raggedright` and `\hyphenpenalty=10000` to the `prov` style, or widen to about 34 mm.
  - The top row of four boxes is cramped against the "Refinement inequality" node.
  - The budget arrow enters Theorem t:inh although the caption says it enters through Corollary c:acc; a separate "Accumulation" node would match.
- **Captions:** all three sit flush under the bottom rule ("TABLE 1" touches the rule). Fix: `\setlength{\abovecaptionskip}{6pt}` or captions above the tables.
- **Table 2 (p. 13):** the caption (11 lines) is longer than the table, with a large gap after it. `sec8.tex` shortens it.
- **Table 3 (p. 17):** the first column wraps and hyphenates ("Corol-lary", "iden-tification"). Fix: `>{\raggedright\arraybackslash}` on both columns, about 0.40/0.54 widths.
- **Bad breaks:**
  - Theorem 1.1 breaks between pages 2 and 3 with its two items alone on page 3.
  - Page 16 opens with a two-line orphan from Section 9.
  - Remark 6.5(b) breaks mid-item across pages 10–11.
- **Walls of text:**
  - p. 14: Sections 8.2 and 8.3, with no display or list.
  - pp. 10–11: Remark 6.5 is one paragraph holding (a)–(d).
  - p. 16: Section 10, one sentence of nine lines.
  - p. 8: Remark 4.1 (a)–(d) inline.
  - Fix for Remarks 4.1 and 6.5: make them `enumerate` lists.
- **Page 1:** only four lines of the introduction under the table of contents. Acceptable; it disappears if the table of contents drops subsections (`\setcounter{tocdepth}{1}`).

## 5. Sentences that can be read as claiming more than they should
- **L12–13 and L152:** "We prove one of the three for SU(2)" / "the second is proved". What is proved is `‖BA^jB‖ ≤ p_{6β}(θ)` for gate-built `B`, with a constant near 1 unless θ is narrow (L550–551). It is not shown that such a `B` is one for which the first hypothesis can hold. Suggest: "for exceptional sets of a particular kind (gates)".
- **L26–28:** "The first question now has an object to be asked about. A continuum theory … was submitted" reads as asserting the theory exists.
- **L31:** "the gap is what is missing" reads as "only the gap".
- **L36, L40:** "the answer is…", "A gap is the same thing as a common rate". The criterion gives an empty window (0, Δ); it does not give positive mass (said only at L82).
- **L47:** "inherits the coarse decay with a small loss" — smallness is exactly what is open.
- **L48:** "that route meets slow trial directions … This is a reason to allow exceptions", next to L163 "No measurement is evidence for or against a hypothesis". The measurements are used as motivation; say so explicitly.
- **L244:** "This is one sufficient route to a gap in a box." Suggest: "would be sufficient if the three hypotheses held".
- **L549:** "which is summable over dyadic N". Summable κ_i is not the budget (the paper says so at L322), and the gates shrink like N^{-4/3}. Add that caveat at this spot.
- **L690:** the heading "The selected combination is collective" is an assertion; the body says it is convention-dependent, for one span on one background.
- **L713:** "These points indicate that quotients like those at −I are also found…", after two failed checks. Suggest: "are compatible with". I kept "indicate" in `sec8.tex` because I was told not to change claims.
- **L743:** "so the larger correlation on A is not particular to the selected combination" — an inference from two estimates.
- **L747–748:** "recover at most a few per cent" reads as a bound.
- **L772–774:** "has a much smaller variance … decays slightly faster", "therefore fails" — stated as facts from estimates. Add "in these estimates".
- **L784:** "So this test retains about 7 per cent" — same.
- **L872:** "whatever backgrounds turn out to have slow decay in time" presumes such backgrounds exist.
- **L886–891:** the status table says "proved" with no reminder that nothing has been independently reviewed (L865–867). A footnote or column note would do.
- **L905–906:** "an upper bound on the gap of four-dimensional SU(2) lattice gauge theory" is stated as a result of another manuscript with no status. Suggest: "a manuscript claiming…".

## Not checked
- I did not verify any proof. The reading for sense turned up the items in section 1 and no mathematical error, but that is not a check.
- I did not rerun any Lean file, Monte Carlo program or reduction, and did not recompute any number against the deposit. The exception is the three look-ups in `d2-time/report.md` and `f2-cross2/report.md` named above.
- I did not read the references, `README.md`, `LEAN_PINS.md` or the earlier drafts.
- The layout was judged from 60 dpi renders and the log of a scratch compile, not at print resolution.
- Line numbers will move again if the manuscript is still being edited; the two replacement files were spliced by section markers, not line numbers.
- I could not remove a stale render folder in my scratchpad (a safety check blocked the `rm`); nothing in the repository is affected.