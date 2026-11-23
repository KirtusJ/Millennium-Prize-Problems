# CHANGES — third revision (p9-rev3, task T62)

The original sources are kept in `orig/`. The full unified diff is in `rev3.diff`. Nothing outside the items below was changed.

| # | Point | File | Change |
|---|---|---|---|
| 1 | N1/N3 | sec_proof.tex, proof of `pf:lem-chess` | `\theta_aS` (3 occurrences; the symbol was never defined) → `\theta_rS`. I added a definition: `\theta_rS:=\{t':t\in S\}` under the induced action `t'_j=2r-1-t_j` on block indices, which is already stated in the file. In the Iteration step I also wrote out the action at doubling i: `t_1 ↦ -2^{i+1}+1-t_1`. The file defines only `\theta_r` (the reflection `x_j ↦ 2r-x_j`), so no other notation needed adapting. |
| 2 | N2 | sec_proof.tex, §`pf:sec-transfer` | `(\tau F)(U)=F(U_{\cdot-e_0})` → `F(U_{\cdot+e_0})` with `(U_{\cdot+e_0})_b:=U_{b+e_0}`, which moves the support forward. In Prop. `pf:prop-spectral` I added "since `\tau^nO_{p_0}=O_{p_n}`, … `=\mu(\theta v\cdot\tau^nv)=`". The identity `\theta\tau=\tau^{-1}\theta`, the definition of T and the proof of Lemma `pf:lem-transfer` already hold under the corrected convention and needed no change. |
| 3 | N4 | sec_reduction.tex (paragraph on even lags); sec_proof.tex (after Lemma `pf:lem-transfer`) | One sentence in each: the reported bond-plane positivity `T ≥ 0` on the site-reflection space for the Wilson periodic-limit states, citing comment 7105972084. The sentence says that it is not proved or used here and that H0 alone does not give it. |
| 4 | N5 | refs.tex; sec_proof.tex (start of §`pf:sec-chess`, and Outline Part II); main.tex (Related results) | New entry `BhattEtAl26`, with fields as read from the PDF. Added the attribution sentences, which cite Lemma 139 and Theorem 140, and the reported joint-event bound in one sentence. |
| 5 | N1/N3 provenance | sec_provenance.tex; main.tex Disclosure; sec_paperreview.tex | New item (V7), "verified by two groups at their stated scope" (comments 7105946691, 7105949912). Removed "the chessboard estimate" from "What was not verified". Added "Certification of the whole proof remains open". In the Disclosure, the chessboard estimate and the tail were moved to "verified", while the Laplace limit and `thm:conditional` stay not verified. Added a "Third revision" paragraph that ends "The text after this revision has not been seen by the reviewers." |
| 6 | N3 | main.tex (Related results) | One sentence on the reported full dissemination for every even L ≥ 4: not read. |

Build: three runs of `pdflatex main.tex`, each with exit 0. There are 0 errors, 0 LaTeX warnings and no undefined references. The PDF has 53 pages.
