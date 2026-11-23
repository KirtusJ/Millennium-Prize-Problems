# r11-lit4 report: literature reader for Z4's two-dimensional controls, Lüscher, plaquette and Teper

Worker of Director Z4, 23 November 2026. Control: `control.txt` = 0.272341 (−ln tanh 1). Page numbers are PDF pages, with the printed page added where it differs.

## 0. Fetched files (hypothesis first)

| File | URL id | Size (bytes) | Pages | Found on page 1 | Match |
|---|---|---|---|---|---|
| ref/cmr.pdf | hep-th/9411210 | 1 809 259 | 247 | Cordes, Moore, Ramgoolam, "Lectures on 2D Yang-Mills theory, equivariant cohomology and topological field theories" | MATCH |
| ref/witten.pdf | hep-th/9204083 | 528 230 | 90 | Witten, "Two dimensional gauge theories revisited" | MATCH |
| ref/levy.pdf | math/0101239 | 874 029 | 113 | Thierry Lévy, "Yang-Mills measure on compact surfaces" | MATCH |
| ref/luscher_fetch_challenge.html | DESY 396349 | 248 | 0 | a JavaScript bot-challenge page, not the PDF | **FETCH FAILED** (not retried by any other route) |
| ref/plaq.pdf | hep-lat/9605031 | 136 358 | 16 | Karsch, Lütgemeier, Patkós, Rank, "The O(g⁶) coefficient in the thermodynamic potential of hot SU(N) gauge theories and MQCD" (BI-TP 96/19) | **MISMATCH**: a three-dimensional SU(N) study. It has no 4D SU(2) plaquette at β = 2.2–2.5 |
| ref/teper.pdf | hep-th/9812187 | 256 292 | 28 | Teper, "Glueball masses and other physical properties of SU(N) gauge theories in D=3+1: a review of lattice results for theorists" | MATCH |

## 1. Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| Z4 §2: continuum gap g²L·C₂/2 for 2D YM on a cylinder (Z4 marks it "quoted") | **STANDS** (now READ) | CMR PDF p.21 (printed 20): H = (e²/2) L C₂(R). The coupling is the one in I = (1/4e²)∫Tr f² (p.17, eq. 3.2), and T_a is an orthonormal basis for that same form (p.19) |
| U(1), charge 1, β = N²: gap 1/2 | **STANDS** | β = 1/(g²a²) matches β(1 − cos θ_p) to (1/4g²)F² (derivation below); e = g, C₂ = 1, so gap = 1/2. qcheck A1: M(64) = 0.500061048820197; A4: β·(−ln I₁/I₀) → 0.50000025 at β = 10⁶ |
| SU(2), spin 1/2, β = 4N²: gap 3/8 | **STANDS, no factor** | In the convention T_a = σ_a/2, (1/4g²)F^aF^a, β = 2N/(g²a²) = 4/(g²a²): C₂ = 3/4, e = g, so 3/8. In Witten's normalization (p.60, C₂(α_n) = (n²−1)/2, so 3/2 for the doublet) the same action forces e² = g²/2, and the product again gives 3/8 (qcheck A3). Mixing the two conventions gives 3/4. That is the only trap |
| Z4's M(64) values 0.500061048820…, 0.375011444266… | **STANDS** | Reproduced to 12 decimals with mpmath, 50 digits (qcheck A1, A2) |
| Transfer eigenvalues c_r^N; lattice partition function | **STANDS for the heat-kernel weight; Wilson weight NOT FOUND** | CMR p.22 (printed 21), eqs. 3.13, 3.16: the cylinder amplitude is the heat kernel, the disk amplitude is the plaquette weight, and with this weight the lattice theory is exact (p.23, eq. 3.18). Lévy PDF p.28 (printed 14) credits the heat-kernel choice to Migdal. Neither source states the Wilson-weight character expansion that Z4 uses |
| Q2: Lüscher 1976/77 transfer matrix (statement, gauge, anisotropy, gauge-invariant subspace) | **NOT CHECKED** | The fetch returned a bot-challenge page. Nothing is asserted about B4's or G4's use of the transfer matrix |
| Z4's plaquette controls 0.5688, 0.6024, 0.6522 "from memory" at β = 2.2, 2.3, 2.5 | **NOT FOUND**: director's citation DEFECT | hep-lat/9605031 is a 3D paper. Its SU(2) table (p.7, Table 1) has β₃ = 6–14 on a 16²×64 lattice. The memory values stay unsourced. 0.5688 lies 3.4σ from Z4's measured 0.56935(16); not resolved here |
| Plaquette PT, c₁ = 3/4 for SU(2) in d = 4 (the subtraction Z4 uses) | **STANDS** (READ) | Karsch et al. p.6, eq. 3.1: c₁ = (N²−1)I_d with I_d = (1/d)(1 − 1/V). Their ⟨P⟩ is ⟨1 − (1/2N)Tr(U+U†)⟩, which is Z4's 1 − P |
| Z4's β²(1 − 3/(4β) − P) = 0.172(1) at β = 8, 8⁴ | **measured only: not confirmed, not contradicted** | Through O(β⁻³): c₂ = 2.5 I² + 48α₄ (α₄ = −0.000103) gives 0.15123, plus c₃/β with c₃ = 0.143055 (p.6, quoted from its ref. [14]), minus the finite-V shift 0.00146. Prediction 0.16765, against 0.172(1). Closing the 0.0044 gap needs c₄ ≈ 0.28, which the source does not give |
| Teper SU(2) a√σ for β = 2.2–2.6 | **READ** | p.12, Table 10: 0.467(10) at 2.2 (8³×10); 0.3687(22) at 2.3 (10⁴); 0.2673(15) at 2.4 and 0.186(3) at 2.5 (the preferred single values, p.11); 0.1326(30) at 2.6 (20⁴) |
| Teper SU(2) continuum 0++/√σ | **READ** | p.4, Table 1: 3.74 ± 0.12 (2++: 5.62 ± 0.26) |
| Physical size of 8⁴ and the matched pair | **derived from READ values** | L√σ = 2.950(18) at β = 2.3 and 1.488(24) at β = 2.5. The 2.3/2.5 spacing ratio is 1.982(34), so 8⁴ at 2.3 ≈ 16⁴ at 2.5. The 2.4/2.6 ratio is 2.016(47) |
| Director's arXiv ids | **1 DEFECT** | hep-lat/9605031 is not a 4D SU(2) plaquette table. The other four arXiv ids match |

**Counts.** The 13 items: STANDS 9 (6 Z4 statements, 3 Teper READ or derived), DEFECT 2 (plaquette citation, hep-lat id), NOT CHECKED 1 (Lüscher), measured only 1 (the 0.172 coefficient).
**Program predicates.** Met 15, failed 1, measured only 3. The parts:
- extract.py: E1–E3. 13 checked, 12 met, 1 failed. Plus 2 measured only (E2 and E3 for plaq, no expectation fixed).
- qcheck.py: A1–A4 met, M1 measured only.

## 2. Hypotheses used by each statement, and where they are stated

- **Gap g²LC₂/2.** Hypotheses:
  - spatial circle of length L and temporal gauge A₀ = 0;
  - Hilbert space of L² class functions with normalized Haar measure;
  - coupling defined through (1/4e²)∫Tr f²;
  - C₂ taken with respect to a basis orthonormal for that same Tr;
  - additive vacuum constants dropped (the counterterm ambiguity, CMR p.18, eq. 3.6).

  Source: CMR pp.19–21; Witten pp.59–60 (eq. 4.40, with the extra constant t).
- **Z4's trajectory β ↔ g.** Hypotheses:
  - Wilson action β Σ(1 − Re χ_F(U_p)/N);
  - the naive continuum limit, matched at tree level, as derived in this report (not in a source).

  Z4 states it in Z4_README §2.
- **c_r^N spectrum.** Hypotheses:
  - character expansion of the plaquette weight;
  - gauge invariance on the circle.

  Z4_README §2. The heat-kernel analogue is in CMR p.22.
- **Plaquette PT.** Hypotheses:
  - Wilson action;
  - weak-coupling expansion on a finite periodic lattice;
  - α_d has a weak volume dependence (Karsch p.6).

  The infinite-lattice α₄ was used for 8⁴. That is an assumption of this check.
- **Teper numbers.** Hypotheses:
  - continuum extrapolation m/√σ linear in a²σ (p.3, eq. 2), with a⁴ consistency checks;
  - string tension from torelon masses (p.11);
  - lowest-β points dropped until the fit is acceptable (p.11).

## 3. Failed predicates

- **E1 (levy).** Page 1 has fewer than 200 characters: it is a title page. This is my expectation, not a defect of the target.
- **Identity predicate on hep-lat/9605031** (not a program predicate). The expected paper is not the one at that id. This is a defect of the director's brief.
- **Lüscher fetch.** Failed at the site.

## 4. Not checked

- Q2 in full: Lüscher's statement, groups, positivity, self-adjointness, gauge, anisotropy, gauge-invariant subspace. The comparison with the B4 and G4 lanes was not made either.
- The Wilson-weight (rather than heat-kernel) character expansion in a source.
- The provenance of the director's memory plaquette values.
- c₄ for the 4D SU(2) plaquette.
- Teper's tables other than SU(2) Wilson.
- Lévy beyond the heat-kernel remark.
- Whether β = 2.2 lies in Teper's scaling window (his 0++ fit reaches β = 2.0, p.11).

## 5. Delegated question and outcome

- **Question.** Q4 went to a general-purpose sub-agent in child/, with the control question 7√2 = 9.899495 (answered correctly) and teper.pdf only.
- **What came back.** The values in §1. The harness blocked its report.md, so the report is in its final message; its notes.md records this.
- **Parent checks.** I checked 3 numbers against ref/text/teper.txt: 3.74 ± 0.12 (p.4); 0.3687(22) (p.12); 0.186(3) and 0.2673(15) (p.11). All three agree. I reran its program: child register K2, exit 0, run2.json identical to run1.json. Child verify: PASS.
- **Caveat.** Its P4 windows are narrow enough to look chosen after seeing the answer, so I treat P4 as measured, not as a test.

## 6. One quotation per source

- CMR p.21: "The Hamiltonian is diagonalized in the representation basis and is the quadratic Casimir"
- Witten p.60: "C2(αn) = (n² − 1)/2"
- Lévy p.28: "A. Migdal [Mi], who suggested first to use the heat kernel"
- Karsch et al. p.7: "calculated on a 16² × 64 lattice"
- Teper p.11: "β = 2.2 to β = 2.6 are from [20]" (via the sub-agent)

## 7. Rerun

```
cd C:/Users/donke/z4-workers/r11-lit4 ; export PYTHONUTF8=1
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name extract --expect-exit 1 -- python -I scripts/extract.py ref ref/text/extract_result_rerun.json
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name qcheck --expect-exit 0 -- python -I scripts/qcheck.py C:/Users/donke/AppData/Roaming/Python/Python314/site-packages results/qcheck_run2.json
cd child && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name teper --expect-exit 0 -- python -I teper_su2.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```

The first run of extract was registered with `--expect-exit 0` (K1, exit 1), so it shows as a mismatch: the E1 failure on Lévy. qcheck K2 exited 0. results/qcheck_run1.json has SHA-256 20d61c2a…c6464c.

PCP verify (main register), last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
