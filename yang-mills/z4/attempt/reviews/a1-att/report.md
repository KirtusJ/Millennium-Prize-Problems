# a1-att report: earlier attempts at 4D Yang-Mills confinement / mass gap, and where they failed

Worker a1-att for Director Z4. Principal: Kirtus Justus. Date: 2026-11-23.
Control: `control.txt` = 0.272341, which is −ln(tanh 1) computed with Python `math`.
Downloaded texts are in `/tmp/a1-att-dl`, outside this directory. Every quotation used here was checked verbatim against those texts by `prog/verify_quotes.py` (15/15 found, 15/15 at most two sentences).

## 1. Verdict table

| Item | Verdict | One line of evidence |
|---|---|---|
| T1 Tomboulis 0707.2179: confinement for all couplings, SU(2), d=4 | DEFECT (not established) | Ito–Seiler 0711.4930 §3: the existence of t* with α(t*)=α⁺(t*) "is reduced to inequality (3.5) which is, as far as we can see, not proven". 0803.3019 §3.3 adds the r<1 / flow-to-strong-coupling tension. Tomboulis replied (0712.2620). I found no published resolution either way. |
| T1 Does the argument as written distinguish SU(2) from U(1)? | DEFECT (no group-specific step identified) | I-S 0711.4930 §2 says the same scheme would give confinement for abelian groups: "This cannot be correct… deconfining Kosterlitz-Thouless (KT) type transition in 4D lattice gauge theory based on abelian gauge groups." Tomboulis' only non-abelian remark is footnote 10, p.27: methods for (5.15)-type inequalities "fail in the non-Abelian case". That is not a step that uses non-abelian structure. |
| T2 MK, d=4, SU(2): flows to strong coupling | STANDS (numerics, measured only) | The child's full-character code, which I reran with identical output: 10/10 SU(2) cases reach c_{1/2}<1e-8 within 32 steps. |
| T2 MK, d=4, U(1): "predicts confinement at all β, which is wrong" | NOT CHECKED (premise not confirmed; contrary numerics) | I-S 0711.4930 Thm 2.1 (citing Ito PRL 55 (1985), which I have not read) states c_j(n)→0 for D≤4 and U(N). The child's U(1) Wilson runs (order A, β0=4,8) are frozen to double precision up to n=6400. The Ito CMP 95 abstract (read by the child) says "D less than 4" for U(1). The brief's premise is therefore not reproduced. |
| T2 Lower critical dimension of MK is 4 | STANDS | 0803.3019 §3.3: "D = 4 becomes the critical dimension" for r=1. The child's d=3 runs all flow strong and its d=5 run at β=8 does not. |
| T3 't Hooft flux / vortex free energy ⇒ Wilson area law (rigorous direction) | STANDS (secondary) | I-S 0711.4930 Remark 2.2(3) says 't Hooft string tension ≤ Wilson string tension, proved in Borgs–Seiler CMP 91 (1983) and conjectured by Mack–Petkova. Kovacs–Tomboulis hep-lat/0002004 abstract: thick-vortex excitation probability → 1 is "rigorously known to provide a necessary and sufficient condition". I did NOT read Borgs–Seiler or Tomboulis–Yaffe. |
| T4 Mihajlovic arXiv:2611.11534 (414 pp., 8 Nov 2026) | Self-declared NOT a proof | Abstract: "A nontrivial four-dimensional spatial-cutoff construction and a positive spectral bound along it are not established; no exact continuum mass is asserted." |
| T4 Faizal–Shabir arXiv:2606.19362 | DEFECT at the level of strategy (abstract only) | Abstract: the gap and area law come from "convergent character (polymer) expansions" at strong coupling, carried to the continuum by multiscale "interlaced inequalities". Strong-coupling expansions hold for U(1) as well (Chatterjee §4), so hole (iii) applies unless a step uses non-abelian structure. The required g→0 limit is outside the expansion's domain. Theorem 10.8 was NOT located. |
| T4 Gauvin arXiv:2503.15539 | Self-declared NOT a proof | Abstract: "The interacting four-dimensional construction, nontrivial renormalized local fields and a uniform physical mass gap remain unproved." |
| T4 "Jofer" ai.vixra 2509.0025 v2–v4, Lemmas 18.70–18.72 | NOT CHECKED | The abs page is an empty shell and the PDFs for v1–v4 returned 0 bytes. Search did not find it. |
| T4 "Eriksson" (approximate positivity) | NOT CHECKED | One web search found no such preprint. |
| T4 openai-20261028 / github.com/yang-mills-group/YM docs/checks.md | NOT CHECKED (SUMMARY ONLY) | GitHub is blocked by this session's proxy, and raw.githubusercontent returned 404. Search snippets from news sites (not evidence) say the committee statement covers existence only, says mass gap and confinement remain open, and that the Lean target `YangMills.jointExistence` omitted links to the lattice construction. Not verified. |
| T5 Jaffe–Witten obstacles | STANDS | Clay problem description, §6, p.~8: "no present ideas point the direction to establish the existence of a mass gap that is uniform in the volume." |
| T5 Chatterjee obstacles | STANDS | 1803.01950 §4: the area law at small β "cannot be evidence for quark confinement" because 4D U(1) is not confining. Large-β non-abelian 4D "remains elusive". |
| T5 Douglas 2004 status report | NOT CHECKED | The claymath URL returned an HTML page, not the PDF. |

Counts for the 15 items above: met (STANDS) 6, failed (DEFECT or self-declared not a proof) 5, NOT CHECKED 4. Numerics are counted as measured only.

## 2. Tables per item

### T1. Tomboulis 2007 and the Ito–Seiler objection
| Address | Authors | Title | Year | Locator read | How read |
|---|---|---|---|---|---|
| arXiv:0707.2179v1 (the only version) | E. T. Tomboulis | Confinement for all values of the coupling in four-dimensional SU(2) gauge theory | 2007 | abstract; §1 pp.1–3; §5 pp.26–28 incl. (5.14)–(5.22), V.1, fn 10; §6 (6.1)–(6.2) | FULL TEXT (pdftotext; sections listed) |
| arXiv:0711.4930v1 | K. R. Ito, E. Seiler | On the recent paper on quark confinement by Tomboulis | 2007 | all, pp.1–10 | FULL TEXT |
| arXiv:0712.2620v1 | E. T. Tomboulis | Reply to arXiv:0711.4930[hep-th] by Ito and Seiler | 2007 | all, pp.1–6 | FULL TEXT |
| arXiv:0803.3019 | K. R. Ito, E. Seiler | Further discussion of Tomboulis' approach to the confinement problem | 2008 | abstract; §2 Thm 2.1–2.2; §3.3 pp.12–15 | FULL TEXT (§3.3 read by me; found by the child) |

- **Strategy.** Tomboulis uses potential-moving (Migdal–Kadanoff type) decimations that give an upper bound on Z (ζ=b^{d−2}, r<1) and a lower bound (ζ=1, r=1). Interpolating with α∈[0,1] and a family parameter t gives an exact representation of Z on coarser lattices. The same construction is applied to Z⁺=(Z+Z⁻)/2 with a Z(2) center vortex. The ratio Z⁻/Z (the vortex free energy) is then bounded below by its value in the upper-bound MK flow, which goes to strong coupling. That yields the area law via the Borgs–Seiler and Mack–Petkova inequality.
- **Step objected to.** To match the bulk factors one needs t* with α(t*)=α⁺(t*). Appendix C and (5.21) obtain this from (5.15), A_Λ(n)(α,r) ≥ A⁺_Λ(n)(α,r), a comparison of α-derivatives of log Z with and without flux. Ito–Seiler: "Namely equation (3.2) is reduced to inequality (3.5) which is, as far as we can see, not proven". They also note that the implicit-function continuation t(λ) breaks down if A⁺>A for some α.
- **Reply.** "In other words, by construction, inequality (5.15) does not come up at weak coupling (large β)." That is, it is invoked only after n decimations, when the upper-bound coefficients are in the strong-coupling region (V.1 states this as an assumption on n0).
- **Second objection (0803.3019 §3.3).** r<1 is needed to keep ∂α/∂t bounded away from 0. But with r<1 the modified flow can go to the weak-coupling fixed point: "But the price to pay for this is that cj (n) may not converge to 0 (the strong coupling fixed point) as n → ∞ !" Their numerics for SU(2) with r=0.9 show a "critical point" at β≈4.8. With r=1 they write that it "is sure to fail for G = U(N)". "These subtle points are not addressed in [1]."
- **My reading** (not independent; same model family as the director). (5.21) uses (5.16) at an intermediate ξ between α* and 1 on the level-n lattice. The reply's defence needs every coupling c̃(n,ξ) for ξ∈[α*,1] to be inside the strong-coupling domain, uniformly in |Λ|, together with r<1 still producing a strong-coupling flow. 0803.3019 argues that these two requirements pull against each other at large β.
- **Accepted?** No acceptance by Tomboulis is on record in what I read. The claim is not accepted in the expert surveys I read: Chatterjee 2018 §4 still lists the large-β 4D non-abelian area law as open. The INSPIRE citation query failed (bad syntax returned the whole database), so I cannot say whether there are later replies.
- **SU(2) vs U(1).** As written, the only group input is a center flux (−1)∈Z(2) and positivity of c_j. The MK upper-bound flow it relies on is stated (I-S, Thm 2.1) to go to strong coupling for U(N) as well. I-S: "Though the Migdal-Kadanoff RG recursion formulas cannot distinguish non-abelian groups from abelian ones, the velocities of the convergences of {cj (n)}∞j=1/2 to 0 as n → ∞ are very different." Tomboulis fn 10: "For Abelian systems, comparison inequalities of the type (5.15) either follow from Griffith’s inequalities, or can be approached by the same methods. All such known methods fail in the non-Abelian case." So the inequality is, if anything, easier in the abelian case. **The argument does not exhibit a step that fails for U(1).** That is hole (iii).

### T2. Migdal–Kadanoff in d=4 (delegated to the child; I reran its code)
| Address | Authors | Title | Year | Locator | How read |
|---|---|---|---|---|---|
| arXiv:0803.3019 | Ito, Seiler | (above) | 2008 | Thm 2.1, §3.3 | FULL TEXT (child and me) |
| arXiv:0711.4930 | Ito, Seiler | (above) | 2007 | Thm 2.1 p.3, §2 p.5–6 | FULL TEXT |
| doi:10.1007/BF01468144 | K. R. Ito | Analytic study of the Migdal-Kadanoff recursion formula, CMP 95 | 1984 | Springer meta description | ABSTRACT ONLY (child; I did not refetch it) |
| Migdal 1975, Kadanoff 1976, Ito PRL 55 (1985) 558, Guth PRD 21 (1980) 2291, Fröhlich–Spencer CMP 83 (1982) 411 | | | | | NOT READ (cited via I-S only) |

- **The literature statement** (I-S Thm 2.1, citing Ito 1985): for D≤4 and G=SU(N) or U(N), c_j(n)→0, i.e. strong coupling ("confinement") for all β. I-S say this is wrong for abelian groups because of the deconfining transition in 4D U(1). That transition is rigorous by Guth and Fröhlich–Spencer (cited, not read). Chatterjee §4 independently states that Guth's result was made rigorous by Fröhlich–Spencer.
- **Numerics (measured only).** In the child's full-character code, which I reran (K3) with identical rows, SU(2) flows strong in d=4 in all 10 cases. U(1) (Wilson action, ordering A, β0≥2) does **not** visibly flow: c₁ is constant to double precision out to n=6400 for β0=4,8. Villain is exactly marginal (grandchild). The grandchild's one-coefficient refit (rerun K4, identical) even drifts toward weak coupling above β≈0.525; the child judged that a truncation artefact.
- **Conclusion.** The textbook line "MK predicts U(1) confines in d=4, which is false" rests here on a citation I have not read (Ito 1985). It was not reproduced by our numerics, and the Ito 1984 abstract states the uniform result only for D<4. What does stand is weaker: d=4 is the marginal dimension of MK for every continuous group (0803.3019), so MK-type bounds have no margin, and any group distinction must come from sub-leading terms that the bounds do not control. Treat "MK predicts U(1) confinement in 4D" as UNVERIFIED.

### T3. Vortex free energy, Wilson loops, finite temperature
| Address | Authors | Title | Year | Locator | How read |
|---|---|---|---|---|---|
| arXiv:hep-lat/0002004 | T. G. Kovacs, E. T. Tomboulis | Computation of the Vortex Free Energy in SU(2) Gauge Theory | 2000 | abstract | ABSTRACT ONLY |
| CMP 91 (1983) 329, doi:10.1007/BF01208780 | C. Borgs, E. Seiler | Lattice Yang-Mills theory at non-zero temperature and the confinement problem | 1983 | | NOT READ (page fetched, not parsed; content only via I-S Remark 2.2(3)) |
| CMP 100 (1985), doi:10.1007/BF01212449 | E. T. Tomboulis, L. G. Yaffe | Finite temperature SU(2) lattice gauge theory | 1985 | | NOT READ (page fetched, not parsed) |

- **What I could verify about rigour.** 't Hooft string tension ≤ Wilson string tension (I-S Remark 2.2(3), attributing the proof to Borgs–Seiler). Hence an exponentially small vortex free-energy cost gives an area law. This is the direction Tomboulis uses.
- **Kovacs–Tomboulis** is numerical. The rigorous part is only the equivalence (vortex condition ⇔ confinement), "rigorously known to provide a necessary and sufficient condition for maintaining confinement at weak coupling in SU(N) gauge theories".
- **Not checked.** The content of the Tomboulis–Yaffe inequalities, and the Borgs–Seiler high-temperature results.

### T4. Recent claims (2024–2026)
| Address | Authors | Title | Year | Locator | How read | What is claimed / not established |
|---|---|---|---|---|---|---|
| arXiv:2611.11534 | A. Mihajlovic | SU(2) Yang-Mills: Spectral Bounds, Vacuum Concentration, and Criteria for the Continuum Limit | 2026 (8 Nov; "414 pages, 98 references") | abstract, comments | ABSTRACT ONLY | Claims fixed-cutoff, finite-volume bounds and criteria. Not established by its own account: a nontrivial 4D construction and a positive spectral bound along it (quote in §1). Fails by (i)/(ii). |
| arXiv:2606.19362 | M. Faizal, A. Shabir | Reflection-Positive Construction of a Four-Dimensional SU(N) Yang-Mills Theory with Mass Gap and Confinement | 2026 | abstract | ABSTRACT ONLY | Claims a full construction, gap and confinement. Strategy: a strong-coupling polymer expansion plus multiscale "interlaced inequalities whose small defects can be summed", plus "entry from weak coupling". No reviewer comment found. Likely holes: (iii), (vii), (ii). Theorem 10.8 not seen; the journal versions (IJGMMP, Fortschr. Phys.) are restricted (search summary only). |
| arXiv:2503.15539 | S. Gauvin | Pinched Multi Affine Geometry and Confinement: Describing the Yang-Mills Mass Gap | 2025 | abstract | ABSTRACT ONLY | Claims a fixed-cutoff SU(3) gap only for magnetic/electric ratio b/a ≤ 1/648, i.e. the strong electric coupling regime. Self-declared unproved: the 4D construction and a uniform gap. (i)+(ii). |
| ai.vixra.org/abs/2509.0025 | "Jofer" (per brief) | ? | ? | page shell only | NOT READ | — |
| openai-20261028; github.com/yang-mills-group/YM docs/checks.md | ? | ? | 2026 | — | SUMMARY ONLY (web-search snippet) | See §1. Not verified. |
| Cambridge Open Engage 67cb65676dde43c908f9dab6 | ? | "RETRACTED: A Rigorous Proof of the Mass Gap in SU(N) Yang-Mills Theory" | 2025 | search title only | SUMMARY ONLY | Retracted; reason not read. |
| "Eriksson" | — | — | — | — | NOT FOUND | — |

### T5. Structural obstacles stated by experts
| Address | Authors | Title | Year | Locator | How read | Obstacle |
|---|---|---|---|---|---|---|
| claymath.org …/yangmills.pdf | A. Jaffe, E. Witten | Quantum Yang–Mills Theory (problem description) | 2000 | §5–§6.5, pp.~7–11 | FULL TEXT (those sections) | (a) No ideas for a mass gap uniform in volume; no method for the T⁴→R⁴ limit. (b) No nontrivial 4D Wightman QFT is known. (c) Gauge choice complicates the structure. Balaban's UV-stability results "need to be extended to the study of expectations of gauge-invariant functions". (d) Reflection positivity is lost under most regularizations. |
| arXiv:1803.01950 | S. Chatterjee | Yang-Mills for probabilists | 2018 | §4 (Problem 4.1), §5 (Problems 5.1–5.2), §7 | FULL TEXT (those sections) | (a) Small-β area law holds for all groups, including U(1), so it is no evidence (quote in §1). (b) The 4D large-β non-abelian area law "remains elusive". (c) β_c=∞ forces a β→∞ continuum limit with ξ(β)→∞ and nonzero string tension after perimeter renormalization. (d) Magnen–Rivasseau–Sénéor's regularization breaks gauge invariance. |
| Douglas 2004, "Report on the status of the YM Millennium Prize Problem" | M. Douglas | | 2004 | — | NOT READ (fetch returned HTML) | — |

### T6. Classification
| Attempt | Fails by |
|---|---|
| Tomboulis 2007 | (iii) no step separates SU(2) from U(1) (I-S); (viii) an unproved comparison inequality (5.15) uniform in |Λ|, plus the r<1 / strong-coupling-flow tension (0803.3019); (i) it is a lattice statement only: the continuum is not addressed beyond g(a)→0 |
| Mihajlovic 2611.11534 | (i), (ii): self-declared |
| Gauvin 2503.15539 | (i), (ii): self-declared; strong-electric-coupling regime only |
| Faizal–Shabir 2606.19362 | probable (iii), (vii) (strong-coupling expansion carried to g→0), (ii). From the abstract only, so to be confirmed against the text |
| MK-based arguments in general | (iii)/(viii): d=4 is marginal for every continuous group, so bounds have no margin |
| Balaban programme (via Jaffe–Witten and Chatterjee) | (ii) UV control without IR or a gap; (vi) gauge choices per phase cell; (iv) no nontriviality |

## 3. Holes a new attempt must not repeat
1. Any confinement or gap step that holds verbatim for U(1) in 4D is false (Coulomb phase at large β: Guth, Fröhlich–Spencer, via I-S and Chatterjee). Name the line where non-abelian structure enters.
2. Strong-coupling (cluster or polymer) expansions give an area law and a gap for every group. They cannot be carried to β→∞ without a separate argument.
3. MK and potential-moving bounds are marginal in d=4. The upper-bound flow reaches strong coupling only with r=1, while making the interpolation derivative non-degenerate needs r<1 (0803.3019 §3.3).
4. Do not invoke a comparison inequality "only at strong coupling" unless every interpolated coupling on the path (all ξ∈[α*,1] in a mean-value step) is shown to lie in the convergence domain uniformly in volume.
5. Existence of a matching parameter via the implicit function theorem needs a nonvanishing derivative along the whole path (I-S 0711.4930 §3, Ψ_t).
6. A fixed-cutoff or finite-volume gap is not the problem. The gap must be uniform in volume and survive a→0 (Jaffe–Witten §6).
7. Nontriviality: the continuum limit must be non-Gaussian with nonconstant gauge-invariant observables. Compactness alone is not enough.
8. The limits L→∞ and a→0 must be ordered or interchanged explicitly.
9. A center-vortex free energy gives an area law only through the Borgs–Seiler / Mack–Petkova inequality. Cite the exact inequality and its hypotheses (the reflection-positivity planes must not bisect the vortex: I-S Thm 2.2).
10. Reflection positivity must be kept or recovered under any flow or smoothing (Jaffe–Witten §6.5). Positivity of c_j alone is not RP under all planes.
11. Balaban-type UV control must be extended to gauge-invariant expectations and to the infrared. Gauge choices per phase cell are part of the difficulty.
12. Do not rely on "MK predicts U(1) confinement in 4D" as a known fact. It was not reproduced by our numerics, and its source (Ito 1985) is unread.

## 4. Failed predicates
- **Child P2** ("for all 20 cases (group×ordering×β0), MK d=4 flows to c₁<1e-8 within 400 steps"): 14/20 met, 6 failed, all U(1). The child classed this as its own expectation, not a target defect. I agree, with one addition: it is also a possible defect of the target *claim* "MK d=4 → strong coupling for U(N)" (I-S Thm 2.1). This is unresolved.
- **Child K2:** the exit code was masked by a pipe. It was flagged by the child and does not certify the tail probe.
- My predicates P1 and P2 in `verify_quotes.py` were met in 15/15 cases (runs K1 with 12 quotes and K2 with 15).
- Grandchild: the one-coefficient refit gives a weak-coupling drift. That is its own approximation, not a target defect (child's judgement, accepted).
- **Fetch failures (not predicates):** the GitHub repo (blocked by the session proxy), ai.vixra PDFs (0 bytes), Douglas PDF (HTML), INSPIRE citation query (bad syntax, unfiltered).

## 5. What I did not check
- Borgs–Seiler 1983, Tomboulis–Yaffe 1985, Guth 1980, Fröhlich–Spencer 1982, Migdal 1975, Kadanoff 1976, Ito 1985, Douglas 2004, Faddeev's or Seiler's status reports: none were read.
- The full text of 2611.11534, 2606.19362 and 2503.15539 (abstracts only), including Faizal–Shabir Thm 10.8.
- The Jofer, Eriksson and openai-20261028 / yang-mills-group checks.md items.
- Later literature citing Tomboulis or Ito–Seiler.
- Whether the full-character MK flow for U(1) in d=4 ever reaches strong coupling.
- No Lean was used. `/home/user/z4-lean/READY` exists, but Lean was not relevant to this brief.

## 6. Delegated questions and outcomes
- **Child** (child/, sonnet, run `child-run1`): T2 only.
  - Control: "lower critical dimension of MK for continuous groups". The answer `4` was graded PASS before I read anything else.
  - It returned: SU(2) flows strong in d=4 (10/10); U(1) frozen for β0≥2; the new source 0803.3019, which I verified myself and which added hole 3.
  - Its "pass" items were rerun by me (K3): rows identical.
- **Grandchild** (child/grandchild/): recompute the U(1) Villain MK flow in d=4.
  - Control: I₁(1)/I₀(1)=0.4464. Correct; I recomputed it as 0.4464.
  - Outcome: Villain is exactly marginal (β'=β). The one-coefficient Wilson refit drifts toward weak coupling above β*≈0.525.
  - I reran it (K4) and the output was identical to its result.txt. The numbers reproduce; their meaning for MK is limited by truncation.

## 7. Rerun commands
```
cd /home/user/z4-workers/a1-att
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
# sources (into /tmp/a1-att-dl): curl -sSL -o <id>.pdf https://arxiv.org/pdf/<id> for 0707.2179 0711.4930 0712.2620 0803.3019 1803.01950; pdftotext -layout <id>.pdf <id>.txt
# curl -sSL -o jw.pdf https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf; pdftotext jw.pdf jw.txt
# curl -sSL -o a2611.11534.abs.html https://arxiv.org/abs/2611.11534 ; a2503.15539.html <- https://arxiv.org/abs/2503.15539 ; kt.abs.html <- https://arxiv.org/abs/hep-lat/0002004
$P check --ws pcp --name verify-quotes-2 --expect-exit 0 -- python3 -I prog/verify_quotes.py prog/quotes.tsv /tmp/a1-att-dl results_quotes_N.txt   # new N each run (mode "x")
$P check --ws pcp --name rerun-child-mk --expect-exit 0 -- python3 -I rerun/mk_recursion.py rerun/result_mk_rerunN.json
$P check --ws pcp --name rerun-grandchild-mk --cwd rerun/gc --expect-exit 0 -- python3 -I mk.py   # delete nothing; use a fresh dir, as result.txt is mode "x"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task,WebFetch,WebSearch' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
Last line of `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## Fetch log
| URL | Result |
|---|---|
| arxiv.org/pdf+abs 0707.2179, 0711.4930, 0712.2620, 0803.3019, 1803.01950 | OK, full text |
| arxiv.org/abs 2611.11534, 2606.19362, 2503.15539, hep-lat/0002004 | OK, abstract |
| arxiv.org hep-th/0407007, math-ph/0507010 | wrong guesses (unrelated papers); discarded and not used |
| claymath yangmills.pdf | OK; ym2.pdf (Douglas?) returned HTML, not read |
| doi 10.1007/BF01208780, BF01212449 | HTML fetched, not parsed |
| ai.vixra.org/abs/2509.0025, /pdf/2509.0025v1–v4.pdf | shell page; 0-byte PDFs |
| raw.githubusercontent.com yang-mills-group/YM (main, master) docs/checks.md | 404 |
| github.com/yang-mills-group/YM | blocked by session proxy |
| inspirehep.net API refersto | query malformed, unfiltered; not used |
| WebSearch ×4 (Jofer; Faizal–Shabir Thm 10.8; Eriksson; yang-mills-group checks.md) | leads only (SUMMARY ONLY) |
