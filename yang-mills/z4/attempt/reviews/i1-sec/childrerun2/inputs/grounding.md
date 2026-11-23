# report — h2-ground (task T95), external grounding for the small-volume SU(2) spectrum

Control: `control.txt` = 0.272341 (−ln tanh 1). Lean READY exists, but I did not use it (no proof was asked for).

## 1. Verdict table

| item | verdict | one line of evidence |
|---|---|---|
| Q1a Leading-order H_eff normalisation | STANDS | van Baal, hep-ph/0008206 eq.(9) at lowest order: L·H = −(g²/2)Σ∂²/∂c² + (1/4g²)Σ_{ij,a}(f^a_ij)². With c = g^{2/3}x this becomes g^{2/3}[−½Δ + ½Σ_{i<j}|x_i×x_j|²], which is the brief's normalisation. |
| Q1b e_0 = 4.1167196 (ours) | STANDS | van Baal p.11: ε₁ = 4.116719735. Ours (= 4^{-1/3}·6.534885 = 4.11671959) differs by −1.5e-7. The rounding of 6.534885 allows ±3.2e-7. |
| Q1c gap 1.8977806 (J=2 → E⁺+T₂⁺) | NOT CHECKED | No reachable source gives the digits. Lüscher–Münster (LM) 1984 full text not read. Wosiek hep-th/0203116 Fig.6 only plots the LM levels. |
| Q1d gap 2.2696457 (A₁⁺) | NOT CHECKED | Same as Q1c. |
| Q1e no J=1 level in the bosonic SU(2) spectrum | STANDS (secondary) | Ambroziński arXiv:1408.2655 App. B reproduces the LM proof that no j=1 states exist. This fits our ordering (J=2, then J=0). |
| Q1f wording in van Baal's review | DEFECT (of the secondary source's wording, not of our numbers) | p.11 calls ε₁ = 4.1167 the lowest-order "mass of the scalar glueball". The same ε₁ enters eq.(12) as a ground energy, and numerically it equals our ground energy e_0, not a gap. A reader must not take 4.1167 as m(A₁⁺)L/g^{2/3}. |
| Q2 conversion m = e_gap(βL³)^{-1/3} = e_gap β^{-1/3}/L ↔ g^{2/3}/L | STANDS | q2_conversion_v2.py and q2_v3_extra.py: P1, P2b, P3, P4, P5 met. P2 and P6 failed; both failures were my own expectation (§3). |
| Q3 published spectrum of the k=2 operator | NOT FOUND | Child T96 found nothing qualifying. My own leads did not help: Wosiek's D=2 is the one-vector case; D=4 is our k=3. Grandchild T97 independently recomputed e_0(k=2) = 3.35053305; I reran it and it reproduced. |
| Q4 validity range of the small-volume expansion | STANDS (as literature statement) | van Baal p.11–15: boundary effects from z = m₀L > 0.9, instantons at z ≈ 5–6. LM abstract: crossover z ≈ 2. |
| Q4 theorem: uniform lower bound on the finite-torus gap at weak coupling | NOT FOUND | Only rigorous *asymptotic* expansions are cited (Bloch perturbation theory; Koller–van Baal NPB273). Search coverage was impaired (§5). |
| Q5 proof of β^{1/3}(1−λ_j) → e_j for the one-site Wilson transfer operator | NOT FOUND | 2 web searches. arXiv/INSPIRE API phrase queries returned empty or 0 hits, including queries that should have matched something. |

Counts (predicates in my programs): **met 11 (P1×2, P3, P4, P5×3, P2b×2, P6b, plus the rerun AGREE), failed 3 (P2×2, P6), measured only 2 (ratios; P6c sign).**
Verdict counts for the items above: STANDS 6, DEFECT 1, NOT CHECKED 2, NOT FOUND 3.

### Q1–Q5 detail table (source, locator, how read, numbers)

| Q | source (address; authors; title; year) | locator | how read | ours | theirs | difference |
|---|---|---|---|---|---|---|
| Q1 | arxiv.org/abs/hep-ph/0008206; P. van Baal; "QCD in a finite volume"; 2000 | eq.(9) p.10 (H_eff); text after eq.(12) p.11 (ε₁) | full text (arXiv PDF → pdftotext) | e_0 = 4.1167196 | ε₁ = 4.116719735 | −1.35e-7 (−1.50e-7 from 6.534885); within rounding |
| Q1 | doi:10.1016/0550-3213(83)90436-4; M. Lüscher; "Some analytic results concerning the mass spectrum of Yang-Mills gauge theories on a torus"; NPB219 (1983) 233 | abstract | abstract (INSPIRE rec. 183485) | — | the abstract says outright that no numbers for the low-lying levels are given; expansion parameter g^{2/3} | — |
| Q1 | doi:10.1016/0550-3213(84)90038-5; M. Lüscher, G. Münster; "Weak-coupling expansion of the low-lying energy values in the SU(2) gauge theory on a torus"; NPB232 (1984) 445 | abstract | abstract only (INSPIRE rec. 191526) | gaps 1.8977806, 2.2696457 | not obtained | — |
| Q1 | arxiv.org/abs/hep-th/0203116; J. Wosiek; "Spectra of supersymmetric Yang-Mills quantum mechanics"; 2002 | eq.(38); Fig.6 | full text | normalisation V = (g²/4)Σ_jk(x_j×x_k)² = ours at g=1 | LM levels plotted only (E1..E3 between ≈4 and ≈8) | not quantifiable |
| Q1 | arxiv.org/abs/hep-th/0407021; M. Campostrini, J. Wosiek; "High precision study of the structure of D=4 SYM QM"; 2004 | p.~8 (nF=0 = zero-volume YM; agrees "very well" with LM) | full text | — | digits only at van Baal's website (ref.[36]), which is outside my allowed network | — |
| Q1 | arxiv.org/abs/1408.2655; Ambroziński (thesis); "Four dimensional supersymmetric YM QM with three colors"; 2014 | App. B | full text (grep) | no J=1 level | no j=1 bosonic SU(2) states (proof after LM) | consistent |
| Q1 | arxiv.org/abs/2211.10870; Butt, Draper, Shen; "Simulating the Femtouniverse on a Quantum Computer"; 2022 | Table I | full text | — | full H_eff (with α, γ) at finite g, not leading coefficients | not comparable |
| Q2 | own derivation + q2_conversion_v2.py | §Q2 below | — | m = e_gap β^{-1/3}/L | LM/van Baal: m = ε g^{2/3}/L | exact match with β = 4/g², h₃ = 4^{1/3}h_vB |
| Q3 | child T96 report; grandchild T97 | child/report.md | child's searches (INSPIRE titles, empty arXiv API) | e_0(k=2) = 3.3505330 | NOT FOUND; T97 recomputed 3.35053305 | 5.5e-8 (recomputation, not literature) |
| Q4 | van Baal hep-ph/0008206 | pp.11–15; Fig.5 | full text | — | z > 0.9 boundary effects; z₀ = 5–6 instantons; E_sph = 72.605/(Lg²) | — |
| Q4 | Lüscher–Münster NPB232 | abstract | abstract | — | crossover z ≅ 2 | — |
| Q5 | searches only | — | — | — | NOT FOUND | — |

### Q2 derivation (conventions)

Lattice units a = 1, Wilson action S = β Σ_P (1 − ½ tr U_P), β = 4/g², spatial box L³, temporal spacing 1. Constant links are U_i = exp(i A_i·σ/2), with A_i ∈ R³ and the coupling absorbed into A.

- **Spatial plaquettes.** U_P = exp(i (A_i×A_j)·σ/2 + O(A³)), so 1 − ½tr U_P = |A_i×A_j|²/8 (1 + O(A²)). This is P1, checked numerically. There are L³ plaquettes per plane, so V = (βL³/8) Σ_{i<j} |A_i×A_j|².
- **Temporal plaquettes.** 1 − ½tr(U(A+Ȧ) U(A)⁻¹) = |Ȧ|²/8 (1 + O(A²)). This is P2b; it holds only for small A, which is the weak-coupling regime. So the Lagrangian is L = (βL³/8) Σ|Ȧ_i|² − V, with mass M = βL³/4.
- **Hamiltonian.** H = −(2/(βL³)) Δ_A + (βL³/8) Σ_{i<j} |A_i×A_j|².
- **Rescaling.** Put A = sY with s = 2(βL³)^{-1/3}. Then H = (βL³)^{-1/3} [−½Δ_Y + 2Σ|Y_i×Y_j|²] = (βL³)^{-1/3} h₃ exactly (P3).
- **Gaps.** m = e_gap (βL³)^{-1/3} = e_gap β^{-1/3}/L in lattice units.
- **Matching to Lüscher.** With β = 4/g², β^{-1/3} = 4^{-1/3} g^{2/3} (P4). Also h₃ = 4^{1/3} h_vB. Together these give m L = e_gap(h_vB) g^{2/3}, which is Lüscher's g^{2/3}/L form, with identical coefficients.
- **Caveats.**
  - g here is the bare lattice coupling. LM/van Baal use the renormalised g(L); the two agree at leading order only.
  - Replacing the transfer operator by e^{−H} needs energies ≪ 1 in lattice units, i.e. β^{-1/3}/L ≪ 1. That limit is Q5, which I found nowhere proved.

### Q4 paragraph

- Lüscher–Münster put the crossover from small- to large-volume behaviour at z = M(0⁺)L ≅ 2 (NPB232 abstract, read as abstract).
- van Baal: the boundary identifications of the fundamental domain affect the low-lying glueballs as soon as z = m₀L > 0.9, through tunnelling along the vacuum valley (hep-ph/0008206, p.11–12).
- Instanton (sphaleron-barrier) effects matter only from z₀ ≈ 5–6, i.e. L ≈ 5–6 correlation lengths (same source, p.15).
- The barrier height is E_sph = 72.605/(L g²) (same source, p.14).
- The zero-momentum reduction also requires z not much above 2π, the scale of the integrated-out modes (same source, p.15).
- Beyond these sizes, the electric-flux energies switch on, and the √n string behaviour appears only at much larger volumes (same source, p.15–16).
- On rigorous results: the only ones cited are rigorous *asymptotic* statements.
  - Bloch degenerate perturbation theory is called a rigorous framework for H_eff (same source, p.9, ref.7 = Lüscher NPB219).
  - The semiclassical tunnelling expansion is called rigorously determined (p.11, refs 26–30; Koller–van Baal NPB273 (1986) 387, title read only).
- **No theorem giving a uniform lower bound on the finite-torus gap at weak coupling was found.**

## 2. Hypotheses used by each statement, and where stated

- **H_eff at leading order** (van Baal eq.(9)):
  - nonzero-momentum modes integrated out (Bloch perturbation theory, p.9);
  - α_i, γ_i set to 0 (p.11);
  - c = O(g^{2/3}) (p.10);
  - zero-momentum fields away from the fundamental-domain boundary, i.e. small z (p.11–12);
  - energies below E_sph (p.14).
- **ε₁ = 4.116719735**: the eigenvalue of the lowest-order H_eff with all α_i, γ_i = 0 (p.11).
- **Q2 conversion**:
  - constant links;
  - small A, i.e. weak coupling (P2b);
  - temporal continuum limit, i.e. transfer operator ≈ e^{−H} (assumed, not proved: Q5);
  - bare β = 4/g² against the renormalised g(L), equal only at leading order.
- **The grandchild's e_0(k=2)**:
  - Rayleigh-Ritz upper bound in the even-k sector (all-k checked equal only at N=6);
  - conditioning cutoff 1e-12.

## 3. Failed predicates

1. **K1 (q2_conversion.py) did not run**: sympy is not installed. This was my environment assumption; no predicate was evaluated, and the run is kept in the register.
2. **P2 (eps 0.1 and 0.01; worst r = 0.57, 0.44)** — my own expectation. With random |A| ~ 1 the A-chart on SU(2) is not flat, so the temporal plaquette is not |Ȧ|²/8. P2b, at |A| = 0.1 (the weak-coupling regime), is met with r ≈ 8e-4. This is not a defect of the target.
3. **P6 (|ours − ε₁| ≤ 1e-7; actual −1.35e-7)** — my own expectation. 4.1167196 is a conversion of the 7-digit 6.534885, so its rounding error is ±3.2e-7, not ±5e-8. P6b, with the correct tolerance, is met. Not a defect.

## 4. What I did not check / could not read

- **Lüscher–Münster full text.** Not reached: there is no arXiv version, and ScienceDirect gives the abstract only. So their digits for the E⁺, T₂⁺ and A₁⁺ gaps (Q1c, Q1d) are **not checked**.
- **Koller–van Baal papers** (NPB273 (1986) 387; NPB302 (1988) 1; Ann. Phys. 174 (1987) 299): titles only.
- **Two hosts outside my allowed network, not fetched:**
  - van Baal's Leiden website (lorentz.leidenuniv.nl: journal scans, susyYM data);
  - OSTI.
- **Q3 sources never read:** B. Simon 1983 and Savvidy.
- **e_1(k=2) = 5.3254970** and the k=3 gaps: I did not recompute these.
- **Search coverage for Q4/Q5 was weak.** After the first queries, INSPIRE returned total 0 for every title query, and arXiv API phrase queries returned empty. So NOT FOUND means "not found in this search".

## 5. Delegated questions and outcomes

- **Child T96** (admitted under T95, then released; event 196).
  - Question: Q3, the published spectrum of −½Δ + c|Y₁×Y₂|² on rotation invariants.
  - Control: −ln tanh 2. Expected 0.036635, answered 0.036635 — graded **PASS** before I read anything else.
  - Outcome: **NOT FOUND**, after INSPIRE title queries (search.py, 8 queries) and empty arXiv API responses. It found only the Koller–van Baal 3+1 series (titles).
- **Grandchild T97** (admitted under T96 and released by the child).
  - Question: an independent Rayleigh-Ritz value of e_0(k=2), in the invariant variables (r₁, r₂, cosθ) with exact Gamma-function matrices.
  - Control: −ln tanh 3. Expected 0.004958, answered 0.004958 — correct.
  - Outcome: 3.35053305 at N = 22. The harmonic-oscillator test gives 3.0000000000.
  - I reread rr.py (the kinetic quadratic form and the potential 2r₁²r₂²(1−c²) are correct) and reran it in my register (K5). It reproduced 3.35053305 and AGREE = True. The only difference was in the 5th decimal of the w = 0.6 scan entry, from single-thread ill-conditioning.
  - Both the child and the grandchild share my model family, so their agreement is not independent review.

## 6. Exact commands to rerun

```
cd /home/user/z4-workers/h2-ground
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name q2-conversion-v2-rerun --expect-exit 1 -- python3 q2_conversion_v2.py   # needs q2_results.txt moved away (mode "x"); exits 1 because P2, P6 fail by design
$P check --ws pcp --name q2-v3-extra-rerun --expect-exit 0 -- python3 q2_v3_extra.py             # needs q2_v3_results.txt moved away
$P check --ws pcp --name child-rr-rerun2 --cwd child/grandchild --timeout 280 --expect-exit 0 -- env RESULTS=/home/user/z4-workers/h2-ground/rr_rerun_parent2.txt OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I rr.py
# child (as run): G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
#   $R task-admit $G --by principal --label h2-ground-child --parent T95   -> T96
#   $P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
#   $R task-release $G --by principal --id T96
# sources: curl -sL -o <scratch>/vb.pdf https://arxiv.org/pdf/hep-ph/0008206 ; pdftotext -layout ; likewise hep-th/0203116, hep-th/0407021, 1408.2655, 2211.10870
# INSPIRE: curl -s "https://inspirehep.net/api/literature/191526" ; ".../183485"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Register checks: K1 (exit 1, sympy missing), K2 (exit 1, P2/P6 failed), K3 (exit 0), K4 child-run1 (exit 0, 288 s), K5 child-rr-rerun (exit 0).
- Last line of `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- Last line of `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
