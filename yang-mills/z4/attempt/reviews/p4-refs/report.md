# Report p4-refs (task T22): bibliography refs.tex

Control: `control.txt` = `0.272341` (−ln tanh 1).
Lean was not used. `/home/user/z4-lean/READY` exists, but this brief needs no Lean.

All records were fetched on 23 Nov 2026. The raw records are in the scratchpad, outside this directory: `/tmp/claude-0/-home-user-z4-workers-p4-refs/6dc79f77-5411-44fc-8826-924b80095d19/scratchpad/{raw1,raw2,gj.html}`. The extracted fields are in `results_run1.json` (fetch.py) and `results_run2.json` (fetch2.py).

## 1. Verdict table

STANDS means every field in the entry was confirmed against a fetched record. DEFECT means the brief's description of the item is wrong; the entry has been corrected.

| item | verdict | evidence |
|---|---|---|
| AC22 | STANDS | Crossref 10.1214/24-AOP1702: Ann. Probab. 53(1), 140–174, 2025. arXiv 2202.10375. The brief gave only the arXiv number; the paper was published in 2025. |
| ADC21 | STANDS | Annals page (citation_* meta tags): 194(1), 163–235, 2021; title form "$\phi_4^4$". Crossref's title has "$\lambda\phi_4^4$", which is a variant. |
| BCH26 | STANDS | arXiv API 2610.08144: Bastounis, Circelli, Hansen, "Navier-Stokes lost in translation: Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs" (6 Oct 2026). No journal data; INSPIRE has no record of it. |
| BS83 | STANDS | INSPIRE + Crossref 10.1007/BF01208780: CMP 91(3), 329–380, 1983. |
| CCK07 | STANDS (title differs from brief) | Crossref 10.1103/PhysRevD.76.094503: the published title is "Dual computations of non-Abelian Yang-Mills **theories** on the lattice", PRD 76, 094503 (2007). The brief's title is the arXiv title. |
| Ch18 | STANDS | arXiv API and INSPIRE: arXiv only, 2018. No journal_ref in either record. |
| Ch21 | STANDS | INSPIRE + Crossref 10.1007/s00220-021-04086-y: CMP 385(2), 1007–1039, 2021. |
| Cr79 | STANDS | INSPIRE + Crossref: PRL 43, 553–556 (1979). INSPIRE also lists an erratum, PRL 43, 890 (DOI …43.890.2), which I included. |
| FHK93 | STANDS | INSPIRE, arXiv and Crossref: NPB 392, 493–517 (1993). |
| FILS78 | STANDS | Crossref 10.1007/BF01940327: CMP 62, 1–34 (1978); full title "… I. General theory and long range lattice models". |
| FiveD11 | STANDS (identified) | arXiv, INSPIRE and Crossref: Knechtli, Luz, Rago, "On the phase structure of five-dimensional SU(2) gauge theories with anisotropic couplings", NPB 856 (2012) 74–94. |
| FS82 | STANDS | INSPIRE + Crossref 10.1007/BF01213610: CMP 83, 411–454 (1982). |
| GJ | STANDS | Crossref book 10.1007/978-1-4612-4728-9: Glimm, Jaffe, Springer New York, 1987. The Springer page gives the subtitle "A Functional Integral Point of View" and edition number 2. |
| GM82 | STANDS (year conflict noted) | Springer page and Crossref: CMP 82(4), 545–606, publication date 1982/01. INSPIRE says 1981. I followed the publisher. |
| Guth80 | STANDS | INSPIRE + Crossref 10.1103/PhysRevD.21.2291: PRD 21(8), 2291–2307 (1980). |
| IS07 | STANDS | arXiv + INSPIRE 0711.4930: no journal data. |
| IS08 | STANDS | arXiv + INSPIRE 0803.3019: no journal data. |
| JW | STANDS (partial) | INSPIRE record 540132: A. M. Jaffe, E. Witten, "Quantum Yang-Mills theory". The URL and access date come from the brief. The URL was **not fetched** because claymath.org is not on my network list. |
| KQR21 | STANDS (title differs from brief) | INSPIRE + Crossref 10.1007/JHEP08(2021)094: the published title is "Distributions in CFT. Part II. Minkowski space", JHEP 08 (2021) 094. |
| KT02 | **DEFECT (brief)** | arXiv, INSPIRE and Crossref agree on the title "Vortex waistlines and long range fluctuations" (PRD 65, 074501, 2002). It is **not** "computation of the vortex free energy"; that is a different paper, hep-lat/0002004 (LIT_ATTEMPTS.md line 62). The entry uses the true title. |
| LL10 | STANDS | Crossref monograph 10.1017/CBO9780511750854: Lawler, Limic, Cambridge University Press, 2010. |
| LTW04 | STANDS | INSPIRE, arXiv and Crossref: JHEP 06 (2004) 012. |
| Lu77 | STANDS | INSPIRE + Crossref 10.1007/BF01614090: CMP 54, 283–292 (1977). |
| LW86 | STANDS (title conflict noted) | Springer page and Crossref: CMP 105(2), 153–188, 1986. Their title lacks "II. Scattering states"; INSPIRE's title has it. I followed INSPIRE and the brief here. |
| OS73 | STANDS | INSPIRE, Crossref and Springer page: CMP 31(2), 83–112 (1973). |
| OS75 | STANDS | INSPIRE + Crossref 10.1007/BF01608978: CMP 42(3), 281–305 (1975); title "… II". |
| OS78 | STANDS | Crossref 10.1016/0003-4916(78)90039-8: "Gauge field theories on a lattice", Ann. Physics 110(2), 440–471 (1978). INSPIRE has "the lattice"; I followed the publisher. |
| Repo, RepoB4, RepoC4, RepoThread | NOT CHECKED | Written exactly as given; nothing fetched (per the brief). |
| Sin81 | STANDS | Crossref 10.1088/0031-8949/24/5/002: Phys. Scripta 24, 817–820 (1981); title uses "Non-Abelian". |
| SS23 | STANDS | INSPIRE + Crossref: PRD 107(3), 034510 (2023). |
| SZZ23 | STANDS | INSPIRE + Crossref 10.1007/s00220-022-04609-1: CMP 400(2), 805–851 (2023). |
| Te98 | STANDS | arXiv + INSPIRE hep-th/9812187: no journal data. |
| To07 | STANDS | arXiv + INSPIRE 0707.2179: no journal data. |
| TY85 | STANDS | INSPIRE + Crossref 10.1007/BF01206134: CMP 100, 313–341 (1985). |
| refs.tex compiles | STANDS | check_refs.py C5: amsart + hyperref + thebibliography + `\input{refs.tex}`, pdflatex exit 0, 1 overfull box. |

Totals: 33 brief keys, of which 32 STANDS and 1 DEFECT (KT02, a defect in the brief's description). 4 Repo entries NOT CHECKED. Compile: STANDS.

## 2. Per-entry record addresses, fields confirmed, fields left out

Address forms used:
- INSPIRE: `https://inspirehep.net/api/literature?q=<query>&fields=...` (exact URLs in results_run*.json under `inspire_url`)
- arXiv: `https://export.arxiv.org/api/query?id_list=<id>`
- Crossref: `https://api.crossref.org/works/<doi>`

| key | record address(es) | fields confirmed (source) | left out / note |
|---|---|---|---|
| AC22 | INSPIRE q=arxiv:2202.10375; arXiv API; Crossref works/10.1214/24-AOP1702 | authors, title, journal, vol 53, no. 1, pp 140–174, year 2025, DOI (Crossref, INSPIRE); arXiv id (arXiv) | — |
| ADC21 | INSPIRE q=arxiv:1912.07973; arXiv API; Crossref works/10.4007/annals.2021.194.1.3; https://annals.math.princeton.edu/2021/194-1/p03 | authors, title ($\phi_4^4$ per Annals page/INSPIRE/arXiv), vol 194, no. 1, pp 163–235 (Annals page, Crossref), year, DOI | "(2)" series marker (not in any record) |
| BCH26 | arXiv API 2610.08144 (my run1 + child + child rerun) | authors, title, year 2026 (arXiv `published`) | journal data (none exists in any record; INSPIRE has no record) |
| BS83 | INSPIRE q=a Borgs and a Seiler and j Commun.Math.Phys.,91; Crossref works/10.1007/BF01208780 | all | — |
| CCK07 | INSPIRE q=arxiv:0705.2629; arXiv API; Crossref works/10.1103/PhysRevD.76.094503 | authors (Crossref given names J. Wade, J. Daniel), published title (Crossref), vol 76, art. 094503, year 2007, DOI, arXiv | — |
| Ch18 | INSPIRE q=arxiv:1803.01950; arXiv API | author, title, year 2018, arXiv id | any later publication venue (not in either record) |
| Ch21 | INSPIRE q=arxiv:2006.16229; arXiv; Crossref works/10.1007/s00220-021-04086-y | all | — |
| Cr79 | INSPIRE q=doi 10.1103/PhysRevLett.43.553; Crossref works/10.1103/PhysRevLett.43.553 and works/10.1103/PhysRevLett.43.890.2 | all, including the erratum at p. 890 | — |
| FHK93 | INSPIRE q=arxiv:hep-lat/9208012; arXiv; Crossref works/10.1016/0550-3213(93)90682-F | all | — |
| FILS78 | INSPIRE q=t "Phase transitions and reflection positivity" and j Commun.Math.Phys.,62; Crossref works/10.1007/BF01940327 | all; title from Crossref | issue (not extracted in run1) |
| FiveD11 | INSPIRE q=arxiv:1110.4210; arXiv; Crossref works/10.1016/j.nuclphysb.2011.11.001 | all | — |
| FS82 | INSPIRE q=a Frohlich and a Spencer and j Commun.Math.Phys.,83; Crossref works/10.1007/BF01213610 | all | issue (not extracted) |
| GJ | Crossref works?query.bibliographic=Glimm Jaffe …; https://link.springer.com/book/10.1007/978-1-4612-4728-9 | authors, title, publisher "Springer New York", year 1987, DOI (Crossref); subtitle and edition 2 (Springer page) | ISBN; series |
| GM82 | INSPIRE q=a Gopfert and j Commun.Math.Phys.,82; Crossref works/10.1007/BF01961240; https://link.springer.com/article/10.1007/BF01961240 | all; year 1982 from publisher + Crossref (INSPIRE says 1981) | — |
| Guth80 | INSPIRE q=a Guth and t nonconfining; Crossref works/10.1103/PhysRevD.21.2291 | all | — |
| IS07, IS08, Te98, To07 | INSPIRE q=arxiv:<id>; arXiv API | authors, title, year (arXiv `published`), arXiv id | journal data (none in the records) |
| JW | INSPIRE q=t "Quantum Yang-Mills theory" and a Jaffe and a Witten (record 540132) | authors (A. M. Jaffe per INSPIRE, E. Witten), title | URL and access date taken from the brief, URL not fetched. Crossref query found no record (Q3 failed). |
| KQR21 | INSPIRE q=arxiv:2104.02090; arXiv; Crossref works/10.1007/JHEP08(2021)094 | all; published title | — |
| KT02 | INSPIRE q=arxiv:hep-lat/0108017; arXiv; Crossref works/10.1103/PhysRevD.65.074501 | all (Crossref spelling Kovács) | — |
| LL10 | Crossref works?query.bibliographic=Lawler Limic Random Walk … (item 10.1017/cbo9780511750854) | authors, title, publisher, year 2010, DOI | place of publication, series/number, ISBN |
| LTW04 | INSPIRE q=arxiv:hep-lat/0404008; arXiv; Crossref works/10.1088/1126-6708/2004/06/012 | all | — |
| Lu77 | INSPIRE q=a Luscher and j Commun.Math.Phys.,54; Crossref works/10.1007/BF01614090 | all; pp 283–292 from Crossref | issue |
| LW86 | INSPIRE q=a Luscher and j Commun.Math.Phys.,105; Crossref works/10.1007/BF01211097; https://link.springer.com/article/10.1007/BF01211097 | all; "II. Scattering states" from INSPIRE only | — |
| OS73 | INSPIRE q=a Osterwalder and a Schrader and j Commun.Math.Phys.,31; Crossref works/10.1007/BF01645738; Springer page | all | — |
| OS75 | INSPIRE (j …,42); Crossref works/10.1007/BF01608978 | all; title "II" from Crossref | — |
| OS78 | INSPIRE q=a Osterwalder and a Seiler and j Annals Phys.,110; Crossref works/10.1016/0003-4916(78)90039-8 | all; title and pages 440–471 from Crossref | — |
| Sin81 | INSPIRE q=a Singer and j Phys.Scripta,24; Crossref works/10.1088/0031-8949/24/5/002 | all; title from Crossref | issue |
| SS23 | INSPIRE q=arxiv:2211.15176; arXiv; Crossref works/10.1103/PhysRevD.107.034510 | all | — |
| SZZ23 | INSPIRE q=arxiv:2204.12737; arXiv; Crossref works/10.1007/s00220-022-04609-1 | all | — |
| TY85 | INSPIRE q=a Tomboulis and a Yaffe and j Commun.Math.Phys.,100; Crossref works/10.1007/BF01206134 | all; pp 313–341 from Crossref | issue |

Formatting choices that are not fetched fields:
- Journal abbreviations (Comm. Math. Phys., Phys. Rev. D, Nuclear Phys. B, Ann. Physics, Ann. Probab., J. High Energy Phys.).
- Initials reduced from the given names in the records.
- TeX for umlauts and accents: Fröhlich, Lüscher and Göpfert per Crossref; Kovács per Crossref.

## 3. Hypotheses each statement uses, and where they are stated

- "Every field comes from a fetched record" relies on two things:
  - the record files `results_run1.json` and `results_run2.json`, the scratchpad raw dirs, and `gj.html`;
  - check_refs.py C3 and C4, which look up the DOIs and arXiv ids and every number of two or more digits.
- C4 is a **weak** test. It checks that a number string appears somewhere in that key's serialized records, not that it appears in the right field. The field mapping was checked by me reading the records (section 2), not by a program.
- The single-digit edition "2" of GJ is not covered by C4. It comes from `gj.html`.
- "Compiles": amsart + `[T1]fontenc` + hyperref with pdflatex, TeX Live as installed (check_refs.py C5).
- Ordering: keys are sorted case-insensitively, with the four Repo* entries merged into that order (check_refs.py C2). The brief does not say where the Repo entries go.

## 4. Failed predicates (kept, with cause)

run1 (fetch.py, P1–P4): 68 met, 18 failed.

| failed predicate | cause | whose defect |
|---|---|---|
| OS73:P1/P2, OS75:P1/P2, OS78:P1/P2 | My INSPIRE title-phrase queries returned 0 hits | My query (my expectation). Fixed in run2. |
| Guth80:P1/P3 | The first INSPIRE hit was Ukawa–Windey–Guth PRD 21, 1013 | My hit selection. Fixed in run2. |
| GM82:P2 | INSPIRE year 1981 vs the brief's 1982 | A database inconsistency. The publisher (Springer page, Crossref) says 1982/01, so the brief is right and INSPIRE differs. |
| GM82:P3 | Title normalization ("3-dimensionalU(1)" in Crossref) | Crossref markup; not a defect of the target. |
| AC22:P3, BS83:P3 | Crossref HTTP 429 (rate limit at 0.4 s spacing) | My pacing. Rerun in run2 at 2.5 s: met. |
| KQR21:P4 | arXiv title "Distributions in CFT II. Minkowski Space" vs published "… Part II. Minkowski space" | A genuine title variant. I used the published title. |
| FILS78:P3, LTW04:P3, Sin81:P3, LW86:P3, CCK07:P3 | Crossref title differs from INSPIRE: "I." vs "1."; HTML markup; "Non-Abelian" vs "Nonabelian (Talk)"; missing "II. Scattering states"; added "theories" | Database variants. My predicate expected identical titles. Resolved per entry in section 2. |

run2 (fetch2.py, Q1–Q4): 15 met, 3 failed.
- OS75:Q2 and OS78:Q2: INSPIRE and Crossref titles differ ("2." vs "II"; "the" vs "a"). I followed Crossref/the publisher.
- JW_book:Q3: Crossref has no record of the Jaffe–Witten description; the entry rests on INSPIRE only.

check_refs.py (C1–C5): 68 met, 0 failed.

Child rerun (child/fetch_refs.py, rerun by me into the scratchpad): the same values as the child reported. The child's own P3 failed because of its own format expectation ("Phys. Rev. D 65" vs arXiv's "Phys.Rev. D65"); the child said so itself.

Overall: met 151, failed 21, measured only: every field value (section 2).

## 5. What I did not check

- The Clay PDF URL for JW: not fetched, because claymath.org is not on my network list. I also did not check that the PDF's author line reads "Arthur Jaffe" rather than INSPIRE's "Arthur M. Jaffe".
- zbMATH: not used.
- Issue numbers for FILS78, FS82, Lu77, Sin81 and TY85: not extracted, so left out.
- The ISBN and series for GJ and LL10, and LL10's place of publication.
- Whether Ch18, IS07, IS08, To07, Te98 or BCH26 later appeared in a journal or volume. No record I fetched says so.
- The Repo entries: given text only, nothing fetched.
- Which of the competing LW86 titles is printed on the article itself (INSPIRE has "II. Scattering states"; Springer and Crossref do not).
- Whether the KT02 citation in the paper means the right paper. The arXiv number the brief gives is "Vortex waistlines…". If the paper's text means "computation of the vortex free energy", the right reference may be hep-lat/0002004 instead. The author must decide.

## 6. Delegated questions and outcomes

- **Child (task T23, admitted under T22; released).**
  - Question: confirm the bibliographic records of FiveD11, BCH26, KT02 and CCK07.
  - Run: recorded in my register as check K1 (`child-run1`, exit 0, 68 s; tools included WebFetch and WebSearch).
  - Control: "the arXiv number of 'Yang-Mills for probabilists'". It answered `1803.01950`, which is **correct**; I graded this before reading anything else.
  - Returned: FiveD11 = Knechtli–Luz–Rago, NPB 856 (2012) 74–94. BCH26 = "Navier-Stokes lost in translation…". KT02 title = "Vortex waistlines and long range fluctuations". CCK07's published title adds "theories".
  - My checks: my own run1 fetched all four independently with the same values, and I reran its program (K6) with the same output. **Agrees.**
- **Grandchild (task T24, parent T23; admitted at seq 46, released at seq 47 of the task graph).**
  - Question: independently fetch arXiv 1110.4210 and report the authors and title.
  - Control: 17·23 = 391. Answered `391`, correct.
  - Returned: Knechtli, Luz, Rago; the same title. This matches my run1 record.

## 7. Commands to rerun (from /home/user/z4-workers/p4-refs)

Each result file uses mode "x", so new output names are needed.

```
S=/tmp/claude-0/-home-user-z4-workers-p4-refs/6dc79f77-5411-44fc-8826-924b80095d19/scratchpad
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name fetch-run1 --expect-exit 0 --timeout 290 -- python3 fetch.py $S/raw1 results_run1.json
$P check --ws pcp --name fetch-run2 --expect-exit 0 --timeout 290 -- python3 fetch2.py $S/raw2 results_run2.json
$P check --ws pcp --name gj-page --expect-exit 0 -- bash -c "curl -sL -A pcp-bib-worker/1.0 -o $S/gj.html https://link.springer.com/book/10.1007/978-1-4612-4728-9 && grep -oE '<meta (name|property)=\"[^\"]*\" content=\"[^\"]*\"' $S/gj.html | grep -iE 'title|edition|date|isbn|author|publisher|subtitle' | head -30"
$P check --ws pcp --name check-refs1 --expect-exit 0 -- python3 check_refs.py $S/latex1 check_run1.txt
$P check --ws pcp --name child-rerun --expect-exit 0 -- python3 -I child/fetch_refs.py $S/child_rerun
# child (task graph):
R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl
$R task-admit $G --by principal --label p4-refs-child --parent T22        # gave T23
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task,WebFetch,WebSearch' < PROMPT.txt"
$R task-release $G --by principal --id T23
$P verify --ws pcp
$R verify pcp/register.jsonl
```

Register verification, last lines:
- `$P verify --ws pcp` → `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` → `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
