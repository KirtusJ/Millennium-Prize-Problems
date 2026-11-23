# b1-style report: format and understatement of OpenAI, "Finite time blowup for Navier–Stokes"

Worker b1-style, task T2. Child T3 (sonnet), grandchild T4. Control: `control.txt` = 0.272341.
Source read: `navier-stokes.pdf`, sha256 0e779481…228f, 166 pp., pdfTeX, CreationDate 8 Sep 2026 (local copy in /tmp/b1-style-dl, not in this directory).
**Headline finding: the PDF says nothing at all about Lean, about AI, about who did the work, or what it does not claim.** It has no acknowledgements and no limitations section. The brief assumes the paper describes its formal verification. It does not. That material lives off the paper, in the repo and the blog. I could reach neither: github.com returned 403 through the proxy, and openai.com is outside my allowed network.

## Verdict table

| Item | Verdict | Evidence (one line) |
|---|---|---|
| F1 Title avoids solve/Millennium/prize/Clay | STANDS | title is "FINITE TIME BLOWUP FOR NAVIER–STOKES" (P3 met) |
| F2 Abstract is one sentence, no prize words | STANDS | 31 words, 1 sentence (P2, P4 met) |
| F3 Author line is the corporate name only | STANDS | p.1 line 3: "OPENAI". No persons, affiliations, e-mail or date |
| F4 Paper describes its Lean formalization | DEFECT (of the brief's premise / of the paper's self-containment) | 0 occurrences of "Lean", "github", "axiom", "commit" in 166 pp. (P5 failed) |
| F5 Paper states AI use / human roles | DEFECT (same) | 0 occurrences of " AI ", "GPT", "language model", "Acknowledg" (P6 failed) |
| F6 Paper names the Millennium problem | STANDS (it does, once, in the body) | p.1: "This establishes alternative (C) in the Millennium problem statement…" |
| F7 Section/page structure | STANDS (measured) | 10 sections and 3 appendices. Spans 2,3,18,21,17,11,15,12,16,10 / 18,13,8 pp.; refs 2 pp. (P8 14/14) |
| F8 22 numbered references, journal-style with DOIs | STANDS | P9 met in v2 (v1 failure was my regex) |
| C1 arXiv:2610.08144 exists, Bastounis–Circelli–Hansen | STANDS | fetched myself: 25 pp., v1 6 Oct 2026, math.AP |
| C2 Its §3.2 concerns a printed-vs-Lean estimate discrepancy | STANDS, but the locator in the brief is partly wrong | §3.2 / Ex. 3.3 = pressure-flux bound (10.19). The m+4 vs m+5 derivative mismatch on (8.19) is §3.1 / Ex. 3.1 |
| C3 The printed estimates the critique cites exist in our copy | STANDS | (8.19) p.95 has ‖N⁻¹F‖_{C^m} ≤ C_m‖F‖_{C^{m+4}}. (10.19) is on p.123 |
| C4 The Lean side of the critique (PressureFlux.lean, commit f9e8bc5) | NOT CHECKED | github 403 |
| R1 Repo README: Lean version, axioms, declaration names | NOT CHECKED | github 403 (curl, API and WebFetch all refused) |
| R2 Blog post on AI role ("GPT-6 Astra", 17 h of formalization, "will not claim the prize") | NOT CHECKED | web-search snippets only (secondhand) |

Verdict counts: STANDS 10, DEFECT 2, NOT CHECKED 3.

Program predicates (style_audit_v2.py, run K3): 7 met, 2 failed (P5, P6), 21 measured only. Run K2 with v1: 6 met, 3 failed.

## 1. FORMAT

- **Title.** "FINITE TIME BLOWUP FOR NAVIER–STOKES". It is a noun phrase that names the phenomenon, not the problem. It has no "solution", "Millennium" or "Clay". It echoes Tao's 2016 title "Finite time blowup for an averaged three-dimensional Navier–Stokes equation" (ref. 22).
- **Author line.** "OPENAI" alone, on line 3 of p.1, also used as the even-page running head. There are no personal names, affiliations, contact, date or arXiv number.
- **Abstract.** One sentence, 31 words: "For every positive viscosity, we construct a solution of the three-dimensional incompressible Navier–Stokes equations that starts from rest and develops unbounded velocity in finite time while maintaining uniformly bounded kinetic energy." (p.1). That one sentence states the full content: quantifier, object, initial datum, the blowup, and the energy bound. It does not mention forcing, the prize, Lean or AI. **Not understated in one respect:** the force is left out of the abstract. A reader learns that the solution is forced only from Theorem 1.1.
- **Contents.** On p.1, then the introduction starts on the same page. Page spans are: 1 Introduction 2; 2 Physical description 3; 3 Proof outline 18; 4 Leading-order flow 21; 5 Base-flow corrections 17; 6 Auxiliary torus 11; 7 Oscillatory realization 15; 8 Mean corrections 12; 9 Residual improvement 16; 10 Compact forcing and whole-space breakdown 10; App. A 18; App. B 13; App. C 8; References 2. Total 166 pp.
- **Main theorem placement.** Theorem 1.1 is on p.1, line 6 of the introduction. Four sentences of motivation come first. It is displayed in italics as a self-contained statement with all quantifiers: ν>0, f ∈ C_c^∞(R³×(0,∞)), compact K, sup‖u‖_{L²}<∞, limsup‖u‖_{L∞}=∞. Then comes a "Consequently…" sentence on non-existence of a bounded-energy global smooth solution.
- **Relation to the official statement.** One sentence: "This establishes alternative (C) in the Millennium problem statement for Navier–Stokes as stated by Fefferman in [13]." (p.1). (D) on T³ is deferred to Corollary 10.6 (p.125), which notes the erratum to [13]. The official alternatives are not quoted, and (A)/(B) and the unforced problem are not discussed. There is no sentence naming a gap. The authors treat (C) as a theorem matched to the official wording, by citation alone.
- **Numbering.** Theorem, proposition, lemma, corollary and definition are numbered within sections (Theorem 3.1, 4.6; Corollary 7.3; Remark B.9). Equations are numbered (s.n). There is one remark in the whole paper (B.9). The body also contains a notation table (symbol, meaning, where defined), at line 997 of the text extraction; I did not pin down its page.
- **Figures/tables/footnotes.** There are 6 figures and they are schematic. Captions flag that: Fig. 2 says "The specific pulse arrangement shown is schematic; active locations, spacing, and aspect ratios are illustrative." (p.5). There are no numbered tables and no footnotes found.
- **References.** 22 numbered entries in AMS style (author, title in italics, journal volume (year), pages, DOI/URL). Historical originals are included (Euler 1757, Navier 1827, Stokes 1845). Fefferman's problem statement is cited by URL [13].
- **Appendices.** A–C hold the profile and moment constructions (39 pp.).
- **Lean citation.** None in the PDF: no commit hash, no file or declaration names, no axiom report, no Lean version. Bastounis et al. compare against the "cited Lean declarations at commit f9e8bc5" (2610.08144 §3.1). The citation of those declarations is therefore outside the PDF I read, presumably in the repo. I did not verify that.
- **Length.** 166 pp., letter size. Sentences are short, there are no hedging adverbs, and the outline section (§3, 18 pp.) is written as an argument a referee can follow without the body.

## 2. UNDERSTATEMENT (devices, each with locator)

1. **Title names the phenomenon, not the prize** (p.1, title). The words "solve", "solution of the problem" and "prize" are absent from the title and abstract. "Prize" appears only inside ref. 13's title. "Millennium" appears once, in the body.
2. **The claim is tied to the official text by citation, not by adjectives.** "This establishes alternative (C) in the Millennium problem statement … as stated by Fefferman in [13]." (p.1). The paper uses no "breakthrough" or "first" for itself, and says nothing about significance: counts of "remarkabl", "breakthrough", "novel" and "we believe" are all 0.
3. **Physical intuition is separated from proof.** §2 is "Physical description"; §3 says "All estimates used below are proved for the viscous equations." (p.7).
4. **Schematics are labelled as schematic** (Fig. 1 and 2 captions, pp.4–5).
5. **Prior work is credited specifically, and the paper's own difference is stated as a difference, not a superiority.** "Our construction also exploits dynamical amplification, with a different role for the amplified disturbances…" (pp.2–3). Albritton–Brué–Colombo, Córdoba–Martínez-Zoroa(–Zheng), Tao and Buckmaster–Vicol are each given one exact sentence on what they did.
6. **No hedges.** The paper does not use "we expect", "we believe", "it seems" or "perhaps" (all 0). Its understatement is *absence of claims*, not hedging.

**Where it does NOT understate, or where the restraint is really omission:**
- It never says it does **not** prove the unforced problem (A)/(B). "Unforced" occurs once, describing Escauriaza–Seregin–Šverák (p.2).
- The abstract omits the force, which is the one hypothesis the public dispute turns on (forced vs unforced). This omission favours the stronger reading.
- There is no statement of AI involvement, no human author, no acknowledgements and no statement on the use of AI. Responsibility sits with a corporation.
- The printed proof and the formal proof are never related in the paper. A reader cannot tell from the PDF which statements were formally checked, against which commit, or with what axioms. "Formally verified" and "proved in the text" are not separated *because the first is never mentioned*.

## 3. KNOWN CRITICISM (delegated to the child, then rerun by me)

- arXiv:2610.08144v1 (6 Oct 2026, math.AP), A. Bastounis, F. Circelli, A. C. Hansen, "Navier–Stokes lost in translation – Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs", 25 pp. Fetched and read by me, sha256 3282e2c4…538b.
- **§3.1, Example 3.1 (pp.4–6):** Lemma 8.6, eq. (8.19), prints a C^{m+4} → C^m inverse bound. The Lean declarations at commit f9e8bc5 (per the critics) need m+5 derivatives. Their summary: "The Lean code produced by OpenAI often has stronger conditions on bounds on the derivatives of various functions than the corresponding results in the NL paper." (§3.1). I confirmed that (8.19) in our copy reads C^{m+4} (p.95).
- **§3.2, Example 3.3 (pp.7–10):** this is where the brief points. It concerns the pressure-flux bound (10.19), not the m+4/m+5 issue: "In the following example the AI autoformalisation results in a Lean proof of a different bound obtained by a substantively different mathematical argument." (§3.2). The Lean estimate (NavierStokes/R3/PressureFlux.lean, per the critics) depends also on A_R. The critics say it cannot be converted to (10.19) via (10.17). I confirmed that (10.19) in our copy has the form C_T R⁻¹[(B_R+1)B_R^{1/2} + R^{-3/4}B_R^{3/4}] (p.123). **I did not check the Lean side.**
- Note against the critics' presentation: their Fig. 4 caption cites "ChatGPT-6 (Astra Ultra)" as sharing their concern (p.9–10). That is not independent evidence.
- Other criticism: the child found press coverage only (TechCrunch 2026-10-08, reporting "at least two discrepancies" from this preprint). Search snippets also show a public dispute over whether forced blowup meets the Clay formulation and over credit (Buckmaster/Alpöge). I read none of these; NOT CHECKED.
- **What a careful imitator should do differently:** (i) put the formal-check map *in the paper*: each printed theorem/lemma next to its declaration name, file, commit hash, and #print axioms output; (ii) where the formal statement is weaker or different (more derivatives, extra parameters), print the formal statement and say so; (iii) never let "Lean-verified" stand for "the printed proof is verified"; (iv) state the forcing/scope hypothesis in the abstract.

## 4. STYLE SHEET for our paper (rules, each traced)

1. Title: a noun phrase naming what was found, e.g. "An upper bound on the lattice mass gap at weak coupling, and four routes that fail". It must not contain mass-gap "solution", "Millennium", "prize" or "Clay". (§1 title; §2.1)
2. Author line: real responsible names and roles, not a corporate or program name alone. (§2, "does not understate", authorless)
3. Abstract, at most 4 sentences, one job each: S1 the one theorem with its quantifiers; S2 that the end-to-end mass-gap attempt failed, and at which step; S3 the four broken routes and the no-go observation in one clause; S4 the review status (one AI model family, no independent review). (§1 abstract; §3(iv))
4. Put every hypothesis that changes the meaning (lattice, gauge group, weak-coupling regime, finite volume) in the abstract. The OpenAI abstract omitted the force. (§2 "does not understate")
5. Display the theorem on p.1, with all quantifiers, followed by one "Consequently" sentence and no more. (§1 Theorem 1.1)
6. Immediately after it, quote the relevant clause of the official Jaffe–Witten statement and add one sentence naming the gap: "This is not the mass gap; it is an upper bound and closes in the direction opposite to what the problem asks." (§1 relation; §2 omission of (A)/(B))
7. State negative results as theorems or numbered observations with precise hypotheses ("Route 2 fails because …, at step …"), not as hedged prose. (§2.6 no-hedge style)
8. The no-go observation gets its own numbered statement and an explicit sentence on what it does not exclude. (§2, unforced case left unspoken)
9. Section plan: 1 Introduction with theorem and scope (2 pp.); 2 Heuristic picture, labelled heuristic; 3 Outline readable without the body; 4 The theorem's proof; 5 The failed attempt end to end; 6–9 Routes 1–4, each ending in "where it breaks"; 10 The no-go observation; 11 What is not claimed; 12 Formal checks and provenance; appendices. (§1 contents, §3 outline)
10. Have a section titled "What is not claimed" (the model paper lacks one). (§2)
11. Credit each prior result in one exact sentence of what it did. Say "different", not "better". (§2.5)
12. Label every schematic figure as schematic in its caption. (§2.4)
13. Do not use "breakthrough", "novel", "first", "remarkable", "we believe", "solve" or "resolves". Do use "we prove", "fails at", "does not". (§2.2, §2.6)
14. Disclosure paragraph on p.1 or 2: every author-side reader and checker belongs to one AI model family; no independent human or other-family review has occurred; the principal is accountable. (§2 omission; §3)
15. The disclosure also states what the AI did and what humans did, by step. (§2 omission)
16. Formal checks: a table mapping each printed statement to its Lean declaration, file path, program commit hash, Lean 4.19.0 and Mathlib version, and the verbatim #print axioms line (propext, Classical.choice, Quot.sound). (§3(i))
17. Where a formal statement differs from the printed one (stronger hypotheses, extra parameters), print both and say which is proved. (§3, 2610.08144 §3.1–3.2)
18. Write "formally checked (Lean, decl X @ commit h)" and "proved in the text" as distinct labels, and never write "verified" alone. (§2, §3(iii))
19. Cite program files and registers by path and commit hash or sha256, in the references or a provenance appendix. (§1 Lean citation absent)
20. Numerical evidence goes in tables with seed, tolerance and its source, and is never called proof. (rules of program; §2.3 physics vs proof)
21. References: numbered, AMS-style with DOIs. Cite the official problem statement by URL and date. (§1 refs)
22. Number theorems within sections. Use few remarks and no footnotes. (§1 numbering)
23. Keep sentences short and declarative, and keep the outline section self-sufficient. (§1 length)

## 5. WHAT DOES NOT TRANSFER

- The OpenAI paper can be terse because it claims a positive result. Ours reports a failure. Brevity about scope would read as concealment, so ours needs the scope section the model omits.
- Its corporate author line and silence on AI fit nothing we can defend. Our provenance (one model family, no review) *is* the main caveat.
- "This establishes alternative (C)" has no analogue. We establish nothing about the mass gap, and must not borrow a sentence shaped like that.
- Our only theorem bounds the gap from **above** (it closes at weak coupling). Displayed on p.1 in the same way, it could be misread as progress toward a gap. The display must carry the direction-of-bound warning.
- The model keeps its formal verification off the paper. Imitating that would hide exactly what 2610.08144 shows goes wrong.
- 166 pages of construction signal weight. Our paper should be as short as its content.
- Its absence of hedging works because every sentence is a proved statement. Our heuristic and failed-route sections must say they are heuristic and failed.

## Hypotheses used and where stated (paper)

- Theorem 1.1 (p.1): ν>0; force f ∈ C_c^∞(R³×(0,∞);R³), so it is forced and smooth; zero initial datum; R³ whole space. Conclusion: bounded L², unbounded L∞ as t↑1, plus non-existence of a bounded-energy global smooth solution with that force.
- Corollary 10.6 (p.125): T³, smooth force compactly supported in time, periodic pressure (Fefferman erratum).
- Construction parameters 0<h<1/100 (p.4, §3.1).

## Failed predicates

- P5 (Lean mentioned in body): FAILED. This was my expectation, taken from the brief, and it was wrong about the PDF. Whether it is a defect of the target (no in-paper formal map) is a judgement; I say yes.
- P6 (AI-use statement present): FAILED. The brief's expectation was wrong. The absence is a disclosure defect of the target.
- P9 in run v1: FAILED because of a defect of **my** regex: reference "1845." matched, and "3.  ," continuation entries were missed. It was fixed in v2 (22 refs, met).
- Disclosure: before run 1 I had already grepped and knew P5/P6 would fail. I set `--expect-exit 1` accordingly. The predicates themselves were left as the brief implied.
- The child's check.py P1 failed (title case/en-dash, its own expectation). It was kept in its register.
- Tolerances: none. All tests are exact string/integer tests. Page numbers come from the printed contents and running heads.

## What I did not check

- The Lean repository (README, toolchain, axioms, declarations, commit f9e8bc5), because github.com returned 403 for curl, the API and WebFetch.
- The OpenAI blog post and any statement there on AI role, human roles, or "will not claim the prize". openai.com is not in my allowed network.
- Whether another version of the PDF exists that cites Lean. I read only the cdn copy with sha256 0e779481….
- The mathematics of the paper (pp.24–164 only skimmed for structure). The header counts in result files are upper bounds, since they include line-initial cross-references.
- Press criticism (TechCrunch, ScienceNews, TNW, NYU Shanghai RITS). I saw them as search hits only.

## Delegated questions and outcomes

- **Child T3** (admitted with parent T2 and released by me; run as check K1 in pcp, exit 0, 62 s, sonnet, WebFetch+WebSearch granted). Question: item 3 alone. Control: number of Fefferman alternatives. Answer "four", graded **correct** before I read anything else. Outcome: it found 2610.08144 and correctly noticed that the brief's §3.2 locator mixes up §3.1 (m+4/m+5, (8.19)) and §3.2 ((10.19)). **I reran this:** I fetched the arXiv PDF myself, located both examples, and confirmed both printed equations in the OpenAI PDF. The child's claims stand. The child's "Remark 3.2 declaration names" (underscores inferred) were not used.
- **Grandchild T4** (admitted with parent T3 and released by the child, per graph lines). Question: independently confirm the existence, title and authors of arXiv:2610.08144. Control: arXiv:1706.03762 → "Attention Is All You Need". That is correct, though the control.txt holds a multi-line dump, not a single line. Outcome: matched. I superseded it with my own fetch.
- Independence: child, grandchild and I share a model family. Agreement among us is not independent review.

## Register verification (last lines)

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp` → `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl` → `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## Rerun commands (from /home/user/z4-workers/b1-style)

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
mkdir -p /tmp/b1-style-dl/arx
curl -sSL -o /tmp/b1-style-dl/ns.pdf https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf
pdftotext -layout /tmp/b1-style-dl/ns.pdf /tmp/b1-style-dl/ns.txt
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name style-audit-run1 --expect-exit 1 -- python3 -I style_audit.py /tmp/b1-style-dl/ns.txt /tmp/b1-style-dl/ns.pdf result_style_audit_run1.txt
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name style-audit-run2 --expect-exit 1 -- python3 -I style_audit_v2.py /tmp/b1-style-dl/ns.txt /tmp/b1-style-dl/ns.pdf result_style_audit_run2.txt
   (result files open with mode "x": delete or rename first, or pass a new result path)
curl -sSL -o /tmp/b1-style-dl/arx/bch.pdf https://arxiv.org/pdf/2610.08144 && pdftotext -layout /tmp/b1-style-dl/arx/bch.pdf /tmp/b1-style-dl/arx/bch.txt
grep -n "^3\.[12]\.\|Example 3\.[13]\|(8\.19)\|(10\.19)\|f9e8bc5" /tmp/b1-style-dl/arx/bch.txt
grep -n "(8\.19)\|(10\.19)" /tmp/b1-style-dl/ns.txt
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-admit /home/user/z4-work/graph/attempt.jsonl --by principal --label b1-style-child --parent T2
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task,WebFetch,WebSearch' < PROMPT.txt"
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-release /home/user/z4-work/graph/attempt.jsonl --by principal --id T3
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

## Fetch log

| URL | Result |
|---|---|
| https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf | 200, 2 959 204 B, sha256 0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f |
| https://api.github.com/repos/openai/NavierStokesAndEuler (+ /commits) | 403 (proxy: GitHub access not enabled for this session) |
| https://github.com/openai/NavierStokesAndEuler | 403 (curl and WebFetch) |
| WebSearch "OpenAI NavierStokesAndEuler Lean formalization Navier-Stokes blowup" | snippets: openai.com/index/navier-stokes-solution, thenextweb.com, sciencenews.org, rits.shanghai.nyu.edu (not fetched) |
| https://arxiv.org/pdf/2610.08144 | 200, 1 710 171 B, sha256 3282e2c4103b955d635173749e7bf887fef7af7dd39e1abdb750b951030c538b |
| child: arxiv.org abs/pdf 2610.08144, techcrunch.com (via its tools) | see child/report.md |

Quotations from the papers: 9 in all, each at most 2 sentences.
