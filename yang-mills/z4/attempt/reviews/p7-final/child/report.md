# T54 report (statement and definitions)
Control: `pdfinfo paper/main.pdf` -> 47 (control.txt).

| Item | Verdict | Evidence |
|---|---|---|
| A. Word scan | STANDS | 19 hits in scan_reviewed.tsv; 0 "must change". Hits are bibliography, provenance/disclosure ("not reviewed", "director"), or math/hash substrings (F_4, \frac4, a4 in hex) |
| LaTeX errors == 0 (P1) | STANDS | 0 lines starting "!" in build/main.log |
| Undefined refs/cites == 0 (P2) | STANDS | 0 in final log |
| No overfull > 15pt (P3) | STANDS | only 1 overfull box at all: 2.17pt, line 20 |
| Thm 1.1 on page 1 (P4) | STANDS | pdftotext page 1 line 31: "Theorem 1.1. Let Op = ..." |
| New PDF page count | STANDS | 47 (equals shipped main.pdf) |

## Failed predicates
- scan.py heuristic: 8 hits came out "must change" (sec_negative 230/233, sec_paperreview 7, sec_proof 307/483/488, main.tex 8). All 8 were my heuristic's defect (own expectation): substring matches in math, or factual review-status disclosure. scan2.py applies a manual-reading override; the override is my judgement, not an independent one. scan.tsv is kept unmodified.
- mech.py P1-P4: none failed.

## Not checked
- Word scan is substring, case-insensitive; "Z4/A4..." hits inside math were judged by reading, not by a parser. Only .tex under paper/ scanned (no PDF text).
- Whether the new PDF equals the shipped one beyond page count; warnings other than overfull/undefined; underfull boxes.
- Whether provenance wording itself is accurate.
- Scan and mech programs were run directly (result files are x-mode, so rerun needs fresh names); the PCP register records K1 (`true`, a placeholder, not evidence), K2/K3 (checks of the result files), K4 (grandchild agreement). Programs themselves are not registered.

## Delegated question
Grandchild task T55 (admitted, released): independent recount of overfull hboxes from build/main.log. Control 0.4375 correct. Result: 1 overfull total, 0 over 15pt, max 2.17381pt, 0 errors. Agrees with mech.json. I reread grandchild/result.txt and checked it via K4.

## Rerun
    cd /home/user/z4-workers/p7-final/child
    pdfinfo paper/main.pdf | grep Pages
    sed -i 's/"scan.tsv"/"scan_r2.tsv"/' scan.py && python3 -I scan.py      # (x-mode: use new names)
    rm -rf build; sed 's/mech.json/mech2.json/' mech.py > /tmp/m.py; python3 -I /tmp/m.py
    python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
    /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl

## Counts
met: 5 (P1-P4, scan complete) + grandchild agreement; failed: 1 heuristic (my own, 8 false must-change); measured only: 19 hit verdicts (manual).

## PCP OS last lines
- python verify: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- rust verify: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
