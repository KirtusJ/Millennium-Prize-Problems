# report p2-neg (worker T18): negative-results sections, `sec_negative.tex`

Control: `control.txt` = 0.272341 (−ln tanh 1), written first. Lean: `/home/user/z4-lean/READY` exists. I did not use Lean and claim no Lean result. The one Lean mention in the text (`A3C.step_chain`) is the a3-C worker's compile, and the text says so.
Deliverables: `sec_negative.tex` (three sections: `sec:routes`, `sec:shared`, `sec:CE`) and `main_test.tex`. pdflatex ran twice with no errors, no warnings and no overfull boxes. **main_test.pdf has 11 pages**; the dummy page and the bibliography take about half a page of that.

## 1. Verdict table

| item | verdict | one line of evidence |
|---|---|---|
| Lemma neg:lem-horizontal (only horizontal curvature enters for gauge-invariant f) | STANDS | Proof given. Bakry–Émery cited to SZZ23 Thm 1.4/(4.7). Upheld by the a4 challenger by argument only |
| Prop neg:prop-flat (κ_H = 1 at flat configurations; one plaquette at −1 gives 1−2β ×3; U(1) gives 0) | STANDS | My proof: on su(2)^4, \|Y\|² has eigenvalue 4 (×3) and 0 (×9), and the 9-dimensional gauge orbit is its kernel. Three programs in the sources agree; N9 is an exact arithmetic check |
| Obs neg:obs-curv (S6 false; κ_H ∈ [−2.30, −1.12]; 0/32 and 0/24 samples at or above 1/2) | STANDS | Union of a3-Acurv.PROOF S6 and a4-chalcurv A2. N5 and N6 met (K3). Child T19 found every entry |
| Obs neg:obs-curv-missing (strong mixing missing; the route is circular) | STANDS | Statement copied from a3-Acurv.PROOF S7. S8 and S9 are marked claimed from memory |
| Lemma neg:lem-Zminus (0 < Z⁻ ≤ Z) | STANDS | Proof from a3-Avort S2. Reflection positivity is cited at abstract level |
| Prop neg:prop-arealaw (KT02 eq. (11) ⇒ area law if F_L decays) | STANDS | KT02 was read in full text by the worker. TY85 was not read, and the text says so |
| Prop neg:prop-noarea (area law does not imply a gap) | STANDS | Tensor product with the free massless field. My proof is two lines |
| Obs neg:obs-vort (two breaks; Table 2) | STANDS | Numbers from a3-Avort.PROOF (iii) and report. N11 met (1.26 ± 1.05, 1.2σ) |
| Lemma neg:lem-decaygap (uniform decay ⇒ gap) | STANDS | Proof copied from a3-Afs S3 |
| Obs neg:obs-fs (S5 and S6 missing; Table 3) | STANDS | a3-Afs.PROOF TEST table. N10 and N13 met. The failed predicate P_D is reported as the worker's own expectation |
| Lemma neg:lem-cj (c_j = I_{2j} − I_{2j+2} = 2(2j+1)I_{2j+1}/β > 0) | STANDS | My proof. N7 met: relative difference 8.5e−16 over 55 cases (K3) |
| Obs neg:obs-dual (4 of 729 amplitudes negative; min −0.003086419753; MC −0.002892 ± 0.000237) | STANDS | a7-wild table and §4. The rational value −1/324 is stated as not proved |
| Lemma neg:lem-usc (upper semicontinuity of m under H1–H4) | STANDS (conditional) | c1-excl runner-up lemma. H2 is claimed as standard with no source read, and the text says so |
| Obs neg:obs-usc (zero set need not be closed) | STANDS as reported | c1-excl usc_test P3/P4. I did not rerun that program |
| Obs neg:obs-shared (six shared properties ⇒ no proof of (A) from them) | STANDS | a7-wild §3. Each property's status is given in the text. P5 is not written out in any source |
| Obs neg:obs-excl (Z_N large N; 5D SU(2)) | STANDS | FS82 (abstract only), FiveD11 §3 (read through a fetch agent), Cr79 (abstract). 5D masslessness is stated as not proved |
| Prop neg:prop-Cprime ((C′) ⇒ (C) with D = e^{2K′}) | STANDS | Chord argument from a3-C step 3. Proof given |
| Obs neg:obs-Cprime-free ((C′) fails lattice-locally in the free field while (C) holds) | STANDS | a3-C.PROOF steps 4, 6 and 9. All numbers were found by the child |
| Prop neg:prop-smear (Euclidean-time smearing does not force (C)) | STANDS | My proof gives the ratio ≥ ½e^{ξ/2}. The source states ≥ e^{ξ/2}/3, which is weaker, so the two are consistent |
| Obs neg:obs-matched (ξ(1−q) = 0.53, 0.68, 0.86; ~ξ^0.75) | STANDS (measured only) | N1–N4 met (slope 0.740). Grandchild T20 recomputed it, and I reran its program (K8): identical |
| Prop neg:prop-GFF (two-point functions do not exclude a GFF; χ²₃ has κ₄/κ₂² = 4) | STANDS | Elementary. N8 met in exact rationals |
| (E*) two-particle shift excludes free algebras; it needs an isolated shell | STANDS as argument | HYPOTHESIS_E (E-c*). The LW86 link is marked claimed and not read |
| Obs neg:obs-ising (calibration, Table 5) | STANDS (measured only) | c1-E.report rows (i)–(iii) and HYPOTHESIS_E §3 |
| a7-wild summary paragraph: "It is negative, −1/324" | DEFECT (of the source) | The same report, §5, says −1/324 is a guess from floats. I follow §5, and so does the ledger |
| Child T19 discrepancy #1 ("L = 16 is the writer's repair of c1-E") | DEFECT (of the child's output) | src/c1-E.report.md:16 reads "for L = 6, 8, 12, 16". The child's own docstring had expected this before it ran |
| Compile check (two pdflatex runs, every key in the bibliography) | STANDS | K11 and K12 exit 0. 11 pages. No warnings |

Verdict counts: **STANDS 24, DEFECT 2, NOT CHECKED 0** (the items not checked are listed in §4).
My program counts (negnum.py, final run K3): **met 14, failed 0, measured only 0**. Two earlier runs crashed on my own code defects (§3). Rerun of the child's programs: 2 of 2 outputs byte-identical.

## 2. Hypotheses each statement uses, and where they are stated

- Throughout: Wilson action exp((β/2)Σ Re Tr U_p), and an infinite-volume state at each β. The latter is assumed by the paper (ledger link 0), not proved. It is stated in sec:routes, opening paragraphs, and in Lemma neg:lem-usc (H1).
- neg:lem-horizontal: compact manifold with smooth V; bi-invariant metric −Tr(XY); P_t-stable invariant algebra. Stated in the lemma and its proof.
- neg:prop-flat: flat configuration on the periodic torus (i); a single plaquette with Q = −1 (ii). Stated in the proposition.
- neg:obs-curv: periodic 3⁴ and 4⁴ boxes; equilibrium samples with short thermalization; no seeds in the sources. Stated in the Observation.
- neg:lem-Zminus and neg:prop-arealaw: even L; L/R and L/T powers of 2; reflection planes through sites that do not bisect V; reflection positivity (OS78, abstract level); KT02 eq. (11). Stated in the statements and proofs.
- neg:prop-noarea: a decoupled free massless lattice scalar. Stated.
- neg:lem-decaygap: an RP state, 0 ≤ T ≤ 1, a dense set of local observables, a uniform rate m. Stated.
- neg:obs-fs: the Dobrushin–Shlosman criterion is claimed and not read. Stated after the lemma.
- neg:lem-cj: β > 0. Stated.
- neg:obs-dual: the periodic 2×1×1 lattice in d = 3, embedded into d = 4. Stated.
- neg:lem-usc: H1–H4. Stated, and H2 is flagged as claimed.
- neg:obs-shared: d = 4. U(1)'s lack of a gap is from Guth80/FS82, abstracts only. Stated per property.
- neg:obs-excl: FS82's hypotheses (N large; action not read); FiveD11's isotropic 5D Wilson action. Stated.
- neg:prop-Cprime: (C′) for β ≥ β₁; ξ ≥ 2K′; ξ/2^j ≥ 1. Stated.
- neg:prop-smear: the spectral measure wδ_m + δ_1 with m = 1/ξ < 1. Stated.
- neg:obs-matched: ξ comes from the published glueball mass and FHK93's scale, not from a measurement. Stated in the Observation and the caption.
- neg:prop-GFF (ii): independent copies of one GFF. For the plaquette application, independence of the colour components with equal variance is stated as not checked.
- (E*): an isolated one-particle shell. Stated.

## 3. Failed predicates and failed runs

- K1 `numbers-run1`: exit 1 before any predicate ran. **My defect**: the file name numbers.py shadowed the standard-library module `numbers` (ImportError). I renamed it to negnum.py with the same predicates.
- K2 `negnum-run2`: exit 1 after N1–N6 were met. **My defect**: the Bessel series overflowed in math.gamma at large k. I fixed it with a term recurrence. `result_negnum_2.txt` is kept.
- K3: all 14 met.
- Child: its single ABSENT token (+1.26 ± 1.05 searched for in a3-Avort.PROOF.md) was its own expectation. The number is in a3-Avort.report.md:39.
- The text keeps the source workers' failed predicates with their attribution: P_D (a3-Afs, own expectation); P2b (c1-E, own expectation); the S6 test (a3-Acurv, a defect of the target step).

## 4. What I did not check

- I reran none of the source workers' programs (curvature, vortex, zflux, dual_sign, mc_check, usc_test, test_c, Ising, the matched-measurement Monte Carlo). Every measured number is taken from the reports. Only the arithmetic derived from them was recomputed (negnum.py, plus the child and grandchild).
- No literature was read by me. Every citation status is copied from the worker reports and GROUNDING.md.
- I did not recompile Lean (A3C.lean).
- The B4 audit of the matched data: I know of it only from the ledger and MATCHED_MEASUREMENT.md.
- P5 of the shared properties (a finite-volume gap) is not written out in any source. My one-line Perron–Frobenius reason is not formalized.
- Keys BS83 and Sin81 are in the bibliography but not cited. No source tells me what they say.
- An exact-arithmetic evaluation of the negative dual amplitude.

### Disagreements between the ledger and the reports (I followed the reports)

1. The range of κ_H. Ledger: "−1.1 to −2.3". a3-Acurv report row S6: [−2.3, −1.2]. a3-Acurv PROOF: [−2.2, −1.5] at β = 4, 6 and [−2.30, −1.17] at β ≥ 12. a4-chalcurv: bottom line "−1.1 to −2.0", table down to −2.04. The text gives the union of the per-run values, [−2.30, −1.12], and says so in the table caption.
2. The ledger says "on 3⁴ and 4⁴" at β = 4…48. The 4⁴ periodic runs exist only at β = 4, 6 (builder) and 6, 24 (challenger). The table shows exactly this.
3. a3-C tags step 4 as "PROVED (numerically on the discriminator)" and step 10 as "PROVED (examples)". The ledger says "numerically" and "by examples". The text uses "numerical" and "by explicit examples". This is a difference of wording, not a correction.
4. The numbers ξ(1−q) = 0.53, 0.68, 0.86 and the exponent 0.75 appear only in the ledger. I recomputed them from MATCHED_MEASUREMENT.md (N1–N4).
5. The ledger says the dual-sign Monte Carlo was rerun bit-identical by the director (K43/K44). That rerun is not in a7-wild's report. The text says only "a separate Monte Carlo program".
6. Internal to sources, not to the ledger: c1-excl gives "below 0.002" (table) and "below 0.0015" (§5). The text gives both. MATCHED_MEASUREMENT.md gives two sets of N = 12 values: 160 configurations, and the pooled 840 rows. The text uses the pooled extension values, as the ledger does.

## 5. Delegated questions and outcomes

- **Child** (task **T19**, admitted under T18, run as register check K4 `child-run1`, exit 0 in 137 s, released afterwards).
  - Question: is every number in my tables (`child/TABLES.md`) present in the named source file, and is every derived number's arithmetic right?
  - Control: the Ricci constant of SU(2) in a3-Acurv's normalization. The known answer is 1. The child answered **1: correct**, graded before I read anything else.
  - Outcome: of 116 tokens, 115 were found and 1 was its own mislocation. All derived values agree. It reported discrepancies #2 (0.002 vs 0.0015) and #3 (two N = 12 data sets), which are real and are now handled in the text. Its #1 is false, as listed in the verdict table.
  - I reread `check_tables.py` and reran it in `child_rerun/` (K7): byte-identical output.
- **Grandchild** (task **T20**, admitted and released by the child under T19).
  - Question: recompute ξ(1−q) of Table T6 from MATCHED_MEASUREMENT.md alone.
  - Control: 1/(3.74·0.25) = 1.0695: correct.
  - Outcome: 9 of 9 values match.
  - I reran `recompute.py` in `child_rerun/gc/` (K8): byte-identical. It uses the same inputs as my N1–N3, so it is a check of arithmetic, not of the data.

## 6. Commands to rerun (from /home/user/z4-workers/p2-neg)

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$P init pcp --principal principal --principal-name "Kirtus Justus"
$R task-admit $G --by principal --label p2-neg-child --parent T18          # gave T19
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name negnum-run3 --expect-exit 0 -- python3 negnum.py result_negnum_3.txt   # use a new result name: mode "x"
mkdir -p child_rerun/gc && cp child/check_tables.py child_rerun/ && cp -r src child_rerun/src && cp child/grandchild/recompute.py child_rerun/gc/
$P check --ws pcp --name rerun-child-check-tables --cwd child_rerun --expect-exit 0 -- python3 -I check_tables.py
$P check --ws pcp --name rerun-grandchild-recompute --cwd child_rerun/gc --expect-exit 0 -- python3 -I recompute.py
$R task-release $G --by principal --id T19
$P check --ws pcp --name pdflatex-5 --expect-exit 0 -- pdflatex -interaction=nonstopmode -halt-on-error main_test.tex
$P check --ws pcp --name pdflatex-6 --expect-exit 0 -- pdflatex -interaction=nonstopmode -halt-on-error main_test.tex
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Register: K1 and K2 (negnum crashes, my defects), K3 negnum, K4 child-run1, K5/K6 and K9–K12 pdflatex, K7/K8 child reruns.

Last lines:
- `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

The director, I, the child and the grandchild are one model family. Our agreement is not independent review.
