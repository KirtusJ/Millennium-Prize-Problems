# Report T23 (refs check)

Control: control.txt = 1803.01950; verified afterwards against arXiv API and INSPIRE record (title+author match). Written from memory first, as instructed, then confirmed.

| key | verdict | evidence |
|---|---|---|
| FiveD11 | CONFIRMED (identification) | http://export.arxiv.org/api/query?id_list=1110.4210: Knechtli, Luz, Rago, "On the phase structure of five-dimensional SU(2) gauge theories with anisotropic couplings"; Nucl. Phys. B 856 (2012) 74-94, doi 10.1016/j.nuclphysb.2011.11.001 (Crossref/INSPIRE) |
| BCH26 | CONFIRMED exists and authors match; publication data UNCONFIRMED | http://export.arxiv.org/api/query?id_list=2610.08144: Bastounis, Circelli, Hansen, "Navier-Stokes lost in translation: ..."; no journal ref, INSPIRE 404 |
| KT02 | CONFIRMED | Crossref https://api.crossref.org/works/10.1103/PhysRevD.65.074501: "Vortex waistlines and long range fluctuations", PRD 65, 074501 (2002) |
| CCK07 | CONFIRMED with a title variant | arXiv title matches; journal PRD 76, 094503 (2007), doi 10.1103/PhysRevD.76.094503. Crossref title says "Theories" additionally ("...Yang-Mills theories on the lattice"). |

Mismatches against the task's claims: none on identity or journal. The "five-dimensional SU(2)" guess is right. Minor: CCK07 published title differs by one word from the quoted title; BCH26 has no journal data.

## Predicates (fixed in fetch_refs.py docstring before first run): 4 met, 1 failed
- P0 control, P1, P2, P4: met.
- P3 FAILED: my string test looked for "Phys. Rev. D 65" but arXiv writes "Phys.Rev. D65 (2002) 074501". Failure was my own formatting expectation, not a defect of the target; the content is confirmed by INSPIRE (journal Phys.Rev.D, vol 65, artid 074501) and Crossref. The predicate was not edited after the fact.
- Also: INSPIRE API 404 for 2610.08144 (target not indexed; not a predicate).
- Counts: met 4, failed 1, measured only: all field values (no further predicates).

## Not checked
Journal landing pages, page numbers for KT02/CCK07 (they use article numbers), any publisher-side check of the CCK07 title variant, BCH26 publication status beyond arXiv/INSPIRE, zbMATH.

## Grandchild
Task id T24 (label p4-refs-grandchild), admitted, released after return. Control: 17*23 -> grandchild/control.txt = 391 (correct, reread). Question: arXiv 1110.4210 authors/title. Answer in grandchild/answer.md: Knechtli, Luz, Rago; same title as mine — agrees with my own fetch (rerun by comparison against out1/records.json). It reported journal_ref UNCONFIRMED on arXiv, consistent with mine; I got the journal from Crossref/INSPIRE.

## Rerun
cd /home/user/z4-workers/p4-refs/child
python3 -I fetch_refs.py out2   # new dir required (mode 'x')
python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name fetch_refs2 --expect-exit 0 -- python3 -I fetch_refs.py out2

## PCP verify (last lines)
- python verify: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
- rust verify: A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.
