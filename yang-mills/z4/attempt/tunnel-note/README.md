# The tunnelling exponent of the one-site SU(2) Wilson transfer operator in two directions: working note

Status, 23 November 2026, first consolidation (superseded by the last section below): **not a finished proof.** Two halves (`tun_upper.tex`, liminf; `tun_lower.tex`, limsup) were consolidated from eight working files into linear text. Writing them out exposed steps the working files asserted without proof. Until these are closed the statement lim (−log m_eo)/√β = 4.6054132 is a claim with named gaps.

Open steps (writers' lists, `../reviews/t1-wU/report.md` §4 and `../reviews/t1-wL/report.md` §3):
1. First half: existence of the smooth minorant ρ_η (W1) and of the C² smoothing of the kink (W3). Elementary; asserted, not constructed.
2. Second half: the bound on Δh in the Taylor lemma (stated without derivation, and dimensionally odd as stated).
3. Second half: the gap bounds DG1/DG3 in the Gaussian lemma (only sketched).
4. Second half: the corner absorption in the cut-off algebra (no quantified condition; numerical evidence only, with margin as small as 0.01 at η = 0.01).
5. Second half: balls of the chain with a₁ just outside [a₋, π − a₋].
6. Numbers quoted for M² in the assembly are not reproduced (only existence of M(η) is used).

Everything here was written and challenged by sessions of one model family. Not read by another lineage or by a person.

## Later the same day

Two gap-closing workers report all six items closed, with replacement text now merged into `tun_upper.tex` and `tun_lower.tex` (`main.tex`, 31 pages, compiles): [`../reviews/u1-gapA/GAPS.md`](../reviews/u1-gapA/GAPS.md) (items 1 to 3: the minorant in C¹ form, the kink smoothing with constants, the Taylor bound derived and found dimensionally consistent after all, the two gap bounds) and [`../reviews/u1-gapB/GAPS.md`](../reviews/u1-gapB/GAPS.md) (items 4 to 6: the corner case proved with a new explicit condition M² ≥ M_A²(η) of order 1/η and an error margin about 3η/16; the chain balls by a different case split; the numbers for M² corrected). These closures have not been challenged. The status above stands until they are.

## Status at the end of 23 November 2026

`main.tex` (32 pages; `main.pdf`) is a complete written proof of lim (−log m_eo)/√β = c* = 4.6054132: no step refers to anything off the page. The six gaps were closed in writing and merged; two referees who were given only the note read it line by line ([`../reviews/v1-chU/report.md`](../reviews/v1-chU/report.md): 31 statements stand, 3 defects, all in the status paragraph or in measured remarks; [`../reviews/v1-chL/report.md`](../reviews/v1-chL/report.md): 26 stand, 1 gap, 1 defect, both bookkeeping); their 29 repairs are applied (`CHANGES_referee_repairs.md`).

What that is worth: authors, gap-closers, challengers and referees are all sessions of one model family. The same family had earlier passed over the six gaps until the text was written out linearly. The note has not been read by a session of another lineage or by a person. The explicit thresholds are beyond any computable β; the only numerical support for the constant is the measurement to β = 256 (fits 4.599 to 4.616) and a one-dimensional model. Lean covers scalar lemmas only and is not part of the note.
