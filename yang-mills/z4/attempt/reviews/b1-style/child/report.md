# T3 report — presentation criticism of OpenAI Navier–Stokes paper (item 3)

**Control (control.txt):** four (alternatives (A)–(D)).

## Answers
- **(a) FOUND.** arXiv:2610.08144 exists: "Navier-Stokes lost in translation: Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs"; authors Alexander Bastounis, Fabian Circelli, Anders C. Hansen; submitted 6 Oct 2026. Locator: https://arxiv.org/abs/2610.08144 (citation_* meta tags). Independently rechecked by grandchild (T4) and by me.
- **(b) FOUND, but premise only partly right.** §3.2 ("When a statement and its proof in the NL paper are both mistranslated into Lean") does discuss a paper-vs-Lean discrepancy, but about a *different* estimate than the one the claim implies. Quote (§3.2, p. 7): "In the following example the AI autoformalisation results in a Lean proof of a different bound obtained by a substantively different mathematical argument." The m+4 vs m+5 derivative discrepancy is in **§3.1**, Example 3.1.
- **(c) FOUND.** 
  - §3.2 / Example 3.3 (pp. 7–10): printed estimate (10.19) (pressure-flux bound in Lemma 10.5's proof), vs Lean `exists_uniform_actual_pressure_flux_bound`, NavierStokes/R3/PressureFlux.lean line 576, commit f9e8bc5; also mentions `exists_uniform_canonicalCutoffFlux_bound`, `canonicalCutoffFlux_bound`. Paper's own figure: Lean bound additionally depends on A_R and has R^{-7/4}.
  - §3.1 / Example 3.1 (pp. 4–6): printed estimate (8.19) (Lemma 8.6, C^{m+4}) vs Lean `norm_derivativeWord_inverse_le` (NavierStokes/SmoothFamilyTorusInverse.lean; C^{m+5}); Remark 3.2 names `inverse_finiteJets` and `mixedJet_inverse_bound` (names as rendered in the PDF text; underscores inferred from spaced rendering).
  - Authors' summary for §3.1: "The Lean code produced by OpenAI often has stronger conditions on bounds on the derivatives of various functions than the corresponding results in the NL paper."
- **(d) FOUND (secondary only).** 
  - TechCrunch, 2026-10-08, https://techcrunch.com/2026/10/08/openais-math-solutions-arent-meeting-the-fields-standards-yet/ : reports "at least two discrepancies" from that paper; quotes Terence Tao, but his quote concerns AI-solved problems generally, not this paper's presentation.
  - aiweekly.co summary https://aiweekly.co/node/17452 (abstract-level: SCI hierarchy claim, mistranslation examples).
  - Other independent criticism of presentation beyond 2610.08144: NOT FOUND (I did not read other search hits: YourStory, Scientific American, NYU Shanghai, johndcook; only a standard search was run; those cover credit dispute/scope, not examined).
  - Caveat: the paper itself quotes a "ChatGPT-6 (Astra Ultra)" figure captions as agreeing with its concern; that is not independent evidence.

## Predicates and failures
check.py (predicates in docstring) FAILED on P1 (title string not found): **my expectation was wrong** — PDF running head is uppercase with an en dash. check2.py fixes P1 only (case-insensitive substring); all P1–P6 true. Check1 kept in the register as a failed run. No tolerances. "For all" predicates: none.

## Grandchild
Question: independently confirm arXiv:2610.08144 exists, its title/authors. Task id **T4** (admitted, released). Control first: arXiv:1706.03762 -> "Attention Is All You Need" (grandchild/control.txt). Outcome: same title/authors/date as mine; I reran grandchild/fetch.py (check K3, exit 0) and it matched.

## PCP verify last lines
- python verify: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- rust verify: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.

## Rerun
```
cd /home/user/z4-workers/b1-style/child
curl -o /tmp/b1-style-child-dl/pdf/2610.08144.pdf https://arxiv.org/pdf/2610.08144 && pdftotext -layout /tmp/b1-style-child-dl/pdf/2610.08144.pdf /tmp/b1-style-child-dl/pdf/p.txt
python3 -I check2.py /tmp/b1-style-child-dl/pdf/p.txt
python3 -I grandchild/fetch.py 2610.08144
```
