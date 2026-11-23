# main_patch.md -- exact lines for main.tex (writer i1-sec, task T99)

Tested: the whole paper compiles with patches 1 and 2 applied (pdflatex, three passes, exit 0; see ../report.md).
Patches 3, 5 and 6 were also applied together with 1 and 2 in a scratch copy and compiled (three passes, exit 0, no undefined references, no new overfull box); that run is not in the register. The optional abstract sentence of 4 was not compiled.

## 1. \input (after line `\input{sec_negative}`)

```
\input{sec_smallbox}
```

## 2. Bibliography (after line `\input{refs}`), or merge the three entries into refs.tex

```
\input{refs_add}
```

If merged into refs.tex instead (keys sorted case-insensitively, as refs.tex states): `LM84` before `LTW04`; `Lu83` after `Lu77` and before `LW86`; `vB00` after `TY85`.

## 3. One row for the status table (Table `intro:status`), before the `\bottomrule` line

```
--- & a lower bound at one spatial site, center-even sector (Section~\ref{sec:smallbox}) & reported (second lineage); fixed volume; does not bear on (A) \\
```

## 4. Abstract: NONE (recommended)

Reason: the abstract lists what this paper proves and the routes its authors wrote out. The new section reports a result
written by a session of another lineage, at one spatial site, which the section itself shows gives nothing for
Hypothesis (A). Putting "a lower bound on the gap at weak coupling" into the abstract would place a third-party,
fixed-volume, sector-restricted statement in the first lines a reader sees, where the qualifications are easy to drop.

If the author prefers to mention it anyway, the sentence would be (to follow "... an argument by exclusion that fails;"):

```
We also report, with its provenance, a lower bound of order $\beta^{-1/3}$ at one spatial site in one symmetry sector, proved by a session of a second model lineage, and show why it gives no bound uniform in the volume.
```

## 5. One item for "What is not claimed" (append to the enumerate of Section `sec:notclaimed`)

```
\item The lower bound of Section~\ref{sec:smallbox} is reported, not proved here. It holds at one spatial site and in the center-even sector only, gives no bound uniform in the volume, and says nothing about Hypothesis~\ref{hyp:A}. The numbers of Table~\ref{sb:tab-num} are measurements.
```

## 6. One sentence for the Disclosure (insert after "Agreement among them is not independent review.")

```
The exception is the one-site lower bound reported in Section~\ref{sec:smallbox}: its proof was written by a session of a second model lineage (OpenAI Codex), checked step by step by a session of the first, and has not been read by a person.
```
