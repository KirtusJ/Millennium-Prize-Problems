# r10-lit2: literature check against the primary sources (Q1–Q4)

Worker of Director Z4, 23 November 2026. Principal: Kirtus Justus. Control: `control.txt` = 0.272341 (−ln tanh 1). The worker, its sub-agent and the director are all one model family, so none of this is independent review. Quotes are kept to one short sentence per source. Page numbers are PDF pages.

**Fetched files.** All five fetches succeeded, and pypdf extracted text from every file (it printed fontTools warnings only). A replay through PCP produced byte-identical text.

| arXiv id | bytes | pages | text |
|---|---|---|---|
| 2205.07376v2 (Faria da Veiga–O'Carroll, 26 Aug 2024) | 744 630 | 54 | ok |
| 2611.11534v1 (Mihajlovic, arXiv 8 Nov 2026; manuscript "Version 5", 5 Nov 2026) | 2 819 183 | 414 | ok |
| 1006.4518v3 (Lüscher) | 195 981 | 21 | ok |
| 1101.0963v2 (Lüscher–Weisz) | 265 323 | 28 | ok |
| 0810.2183 (Makeenko) | 279 724 | 32 | ok |

## 1. Verdict table

| Item | Verdict | Evidence (one line) |
|---|---|---|
| LITERATURE.md row: FdV–O'C "directly comparable" with C4, A4 and Z4's b⁻⁵ | **DEFECT** | The paper's plaquette field is Im Tr(U_p − 1)/(a²g) (eq.30, p.11). It vanishes identically for SU(2) (K3: max \|Im Tr U\| = 0 on 10⁴ Haar samples). For SU(N≥3) it starts at cubic order. It is not the action density. |
| FdV–O'C main theorems, as restated below | STANDS (as read) | Thms 1–4, pp.28–31. Bounds are uniform in L, a and g ≤ g₀. Proofs were read only in outline (§VI). |
| FdV–O'C "uniform in a" and "subsequential UV limit" in d = 4 | STANDS, but empty in d = 4 | In d = 4 the action coefficient a^{d−4}/g² equals 1/g², so the measure does not depend on a (Remark 20, p.32). The a⁻⁴ is the unit conversion in eq.30. The limits come from Bolzano–Weierstrass on bounded numbers (Thm 3, p.29). No running g(a) is imposed. |
| C4 sup E exp[β(1−x_p)/8] ≤ C | STANDS, independent of FdV–O'C | That paper bounds the real part only through the free energy (Thms 1–3), which gives no pointwise exponential moment. Its generating function concerns the imaginary part. |
| A4 contact variance ~ b⁻⁵ with coefficient 1/18 | STANDS, independent | FdV–O'C has no smeared, centred square of the action and no variance lower bound. Its a⁻ᵈ is a pointwise upper bound for the Im-part field. |
| Z4 S1′ (b⁻⁵) | STANDS, consistent, independent | Same power counting: the field has dimension 2, so its coincident 2-point function goes as a⁻⁴, and its smeared square as b⁻⁵. The paper treats neither composites nor smearing. |
| D4 electric scale vs Mihajlovic §§40–41 | **Overlap: same leading law** (prior art to cite) | Thm 40.1 (p.235): relative entropy per plaquette ≥ (3/2) log(1/g²) − const. §41.4 (p.239): fidelity → 0 when g → 0 and gJ → 0, so the retained one-link dimension must grow like g_YM⁻³. In D4's variable g_D4 = β²/2 = 8/g_YM⁴ this is g_D4^{3/4} = g^{d/4}, with entropy (d/4) log g. The conversion is my reading of the conventions. |
| B4 vs Mihajlovic | Different, no contradiction | Mihajlovic's strong-coupling gap is isotropic Euclidean with β_W < 1/3 (Thm 10.10, p.97–98, attributed to Bhattacharjee–Bhattacharya [5]). His Hamiltonian results take s = g² ≤ 1, a disjoint regime from B4's κλ ≤ 1/384. His finite-box gap (1.2) is explicitly not volume-uniform. |
| A4 vs Mihajlovic | Similar in kind, different statement | Thm PT.1 (p.102–103) is an adjacent-layer covariance ≥ L_β, uniform in volume, at fixed spacing, on the Euclidean Wilson measure. A4's floors are Hamiltonian. A4's bands were not compared constant by constant. |
| Anything in Mihajlovic contradicting the repository | NONE FOUND | In the pages read (1–10, 97–103, 176, 234–239). It states the same open wall: no 4D spatial-cutoff construction and no gap along it (abstract, p.1). |
| Lüscher / Lüscher–Weisz facts used in S6′ | STANDS | Flow eq.(1.1); E eq.(2.1); √(8t) at p.4; t²⟨E⟩ at leading order (2.32). Finiteness to all orders in perturbation theory, dimensional regularization (LW abstract, §§6–7). On the lattice it is "expected" only (LW §8.4, p.25). |
| LITERATURE.md: the flowed density "has an unambiguous continuum limit" | **DEFECT (overstated)** | This is established perturbatively, order by order, in dimensional regularization. Lüscher 2010 shows lattice scaling numerically only (§3). Nothing nonperturbative is proved. |
| LITERATURE.md: "self-intersecting loops mix", attributed via Makeenko | **DEFECT (not in source)** | There are zero hits for "intersect" in 0810.2183. Makeenko covers smooth loops (§1.2), cusps (§1.3–1.4) and light-cone loops (§1.7) only. |
| Makeenko statements (perimeter, cusp, BNS) | STANDS | §1.2 p.2 eq.(1.3); §1.3 p.3 eq.(1.4); §1.4 eq.(1.5). Checked against the pages myself. |
| Flowed free benchmark (my program) | STANDS (6 met) | ⟨B²⟩ is finite. The equal-time variance of the smeared flowed B² is finite for every t > 0. It tends to c_flow·∫f²·t^{−5/2}. |

## 2. Q1–Q4 in detail, with the hypotheses each statement uses

### Q1 Faria da Veiga–O'Carroll (2205.07376)

- **Setting** (abstract p.1; §I pp.2–3):
  - Wilson action Σ_p 2Re Tr(1 − U_p)·a^{d−4}/g² (eq.6–7).
  - Finite lattice Λ ⊂ aℤᵈ, d = 2, 3, 4, with a ∈ (0,1].
  - L even. G = U(N) or SU(N); the explicit Weyl and GUE/GSE constants are for U(N) (eq.75–78).
  - g² ∈ (0, g₀²]. Free or periodic boundary conditions. Thm 4 needs periodic.
- **Scaling** (p.7, eq.17): A^c = a^{(d−2)/2} A^{u,c}. The scaled plaquette field is Tr F^s_p = a^{d/2} Tr F^u_p = a^{(d−4)/2} Im Tr(U_p − 1)/g (eq.30, 32, p.11).
- **"Thermodynamic and ultraviolet stable"** (Thms 1–3, pp.28–29): the scaled free energy (1/Λ_r) ln[(a^{d−4}/g²)^{N²Λ_r/2} Z] lies between constants c_ℓ and c_u. These constants are independent of L, a and g ≤ g₀. The bound is per lattice site, not per physical volume (p.11).
- **Generating function** (Thm 4, p.31; multireflection): \|G_r(J)\| ≤ ∏_j \|z_u(rJ_j)/z_ℓ\|^{…}, with \|z_u(J)\| ≤ (a^{d−4}/g²)^{−N²/2} exp(c′_u + π²N\|J\|²/8). The bound is Gaussian in J and uniform in L, a, g and the plaquette positions. Cauchy bounds then bound the r-point scaled correlations.
- **The a⁻ᵈ statement**:
  - Remark 19, p.32: the unscaled coincident two-plaquette correlation is ≤ const·a⁻ᵈ.
  - pp.12 and 38: for d = 4 it equals a⁻⁴·M(g) with M bounded.
  - In d = 4 this is the conversion factor of eq.30 applied to an a-independent lattice expectation (Remark 20).
- **Scope**: on p.2 they say "this ﬁniteness properties do not lead directly to the construction of the UV limit". The same page says they cannot fully answer the existence and gap questions. No gap is claimed.
- **Plainly**:
  - In d = 4 the theorems are uniform-in-coupling bounds on a lattice model that does not depend on a.
  - The field they bound is the imaginary part of the trace. That is zero for SU(2), and for U(N) it is the abelian part. It is not the action density that C4, A4 and Z4 use.
  - None of the three lane statements is implied by the paper, and none is stronger than it. They are statements about a different observable.
  - The earlier row in LITERATURE.md, which came from a search summary, was wrong to call them directly comparable.

### Q2 Mihajlovic (2611.11534)

- **Status**: unrefereed preprint, 414 pages, arXiv v1 dated 8 Nov 2026.
  - No formal verification is claimed for its own results. Its "certified" results are exact-rational and interval checker programs (§1.4 p.10, §40.4 p.236).
  - Lean appears only in a cited Zenodo archive [5], which is not externally validated (p.408).
- **Results read**:
  - §1.2 p.8 table.
  - Finite-box gap (1.2) / Thm 24.1, p.9: Δ ≥ (3s/8a)(π/16)^{3L³} e^{−48πL³/s}, which says itself that it is not uniform under refinement.
  - Thm 28.1 (p.176–177): a local floor, volume-independent for a fixed number of deleted links.
  - Thm 40.1 (entropy, p.235).
  - Thm 41.1 and §41.4 (fidelity, pp.237–239).
  - Thm 10.10 (forest gauge, β_W < 1/3, p.97–98).
  - Thm PT.1 (p.102–103).
- **Hypotheses**:
  - SU(2). Hamiltonian H = (s/2a)ΣC_e + (4/(sa))Σ(1 − F_p) on a periodic spatial L³ lattice, with 0 < s = g² ≤ 1 (§§40–41).
  - The vacuum input ν(1 − F_p) ≤ 3s/4 (Lemma 31.1, not read).
- **Overlaps**:
  - D4: same leading statement (see the table). Mihajlovic gives lower bounds (necessity). D4's statements were read only through input/README_rounds.md, so I cannot say whether D4 also claims the matching upper order.
  - B4: different statements in a different regime.
  - A4: Thm PT.1 is a Euclidean analogue of A4's positive-time floor, with constants β⁴e^{−100β}/2048. The two are of the same kind, at fixed spacing.
- **What remains open, in its own words**: the abstract says a nontrivial 4D spatial-cutoff construction and a positive spectral bound along it are not established. §1.3 p.10 lists the premises of the continuum transfer, condition (1.3), as unsupplied.
- **Conclusion**: no contradiction with the repository was found. It is prior art that D4 must cite for the entropy and electric-cutoff fidelity laws.

### Q3 Lüscher (1006.4518) and Lüscher–Weisz (1101.0963)

- **Definitions**:
  - Continuum flow: dB_μ/dt = D_νG_νμ with B|₀ = A (eq.1.1–1.2, p.1).
  - Wilson flow on the lattice: eq.(1.4), p.2. Existence, uniqueness and smoothness hold on a finite lattice.
  - E = ¼G^aG^a (eq.2.1, p.3).
  - At leading order the flow is the heat kernel e^{−tp²}, with mean-square smoothing radius √(8t) in 4D (p.4).
- **Leading order**:
  - ⟨E⟩ = 3(N²−1)g²/(128π²t²)·(1 + c̄₁g² + …) (eq.2.32, p.8), or 3(N²−1)α/(32πt²) (eq.2.34).
  - SU(2): t²⟨E⟩ = 9g²/(128π²) = 0.0071244·g² = 0.089525·α.
  - Lüscher's checks of this result are one loop only (p.8). In his conclusions an all-order analysis "will probably be required" (p.17).
- **All orders**:
  - LW abstract p.1: for any matter multiplet, the correlation functions of the flowed field are finite to all loop orders once the 4D theory is renormalized in the usual way. Proof: power counting plus the BRS symmetry of the (D+1)-dimensional theory (§§6–7, conclusions p.26). Dimensional regularization.
  - Gauge-invariant local fields and Wilson loops at t > 0 need no renormalization (§8.2, p.24), with E(t,x) = ⟨E⟩ + c_E(t){¼F²}_R + O(t).
  - On the lattice this is only "expected" (§8.4, p.25).
- **S6′ rewritten with the flowed density** (conjectural, not a result):
  - **Setting**: lattice SU(N), spacing b, coupling trajectory β(b), Wilson flow V_t.
  - **Observable**: E_b(t,x) is a lattice discretization of ¼G^aG^a of the flowed field. O_{b,t}(f) = b³Σ_x f(bx)(E_b(t,x) − ⟨E_b(t)⟩) on one time slice, with C_{b,t}(τ) its connected Euclidean-time correlator at fixed physical t, f and τ.
  - **Existence and nontriviality**: 0 < c ≤ t²⟨E_b(t)⟩ ≤ C, and v ≤ C_{b,t}(2τ) together with C_{b,t}(τ) ≤ V, uniformly as b → 0 along the trajectory. By S5(e) this places a fixed weight in a fixed physical window.
  - **Gap in this sector**: C_{b,t}(τ) ≤ K e^{−mτ} for τ ≥ τ₀, with m > 0 uniform in b and volume. S5(f, g) cover the finite-sum case.
  - **Caveat 1**: a 4D-flowed field at time x₀ depends on links at all times through the heat-kernel tails. Exact reflection positivity, and with it the transfer-matrix reading, needs either the 3D (spatial-only) flow on a slice or a separation τ ≫ √(8t) with tail control.
  - **Caveat 2**: the gap needs this for every gauge-invariant local field, not one sector.
  - **What the literature establishes**: perturbative finiteness of every such correlator at t > 0, order by order, in dimensional regularization. The value of t²⟨E⟩ at one loop. Numerical lattice scaling of t₀ (Lüscher §3).
  - **What nobody has proved**: any of the bounds above nonperturbatively in 4D along b → 0, and the lattice version of the all-order theorem. Order by order, perturbation theory gives power-law decay (massless gluons), not a gap.
- **Free benchmark** (`scripts/flow_bench.py`, `results/flow_bench_run1.txt`, PCP K1):
  - ⟨B₃²⟩ = 1/(48π²t²) with the 3D spatial flow.
  - ⟨F₁₂²⟩ = 1/(128π²t²) with the 4D flow. This equals Lüscher's leading order with N²−1 → 1, i.e. t²⟨E⟩ = 3/(128π²).
  - The equal-time variance of the Gaussian-smeared flowed B₃² is finite and positive for every t > 0. In units of t, t·Var = 2.2347·10⁻⁵, 6.1107·10⁻⁴, 8.9142·10⁻³, 9.0206·10⁻², 0.77809, 6.3547 for σ/√t = 0.5, 1, 2, 4, 8, 16.
  - For σ ≫ √t: Var → c_flow·∫f²·t^{−5/2}, with c_flow = √π/(640π²) = 2.806·10⁻⁴. The deviation is about 1.8·t/σ².
  - So S1′'s b⁻⁵ becomes (√t)⁻⁵: flow time takes the place of b². The divergence returns as t → 0 at fixed f, as it must.

### Q4 Makeenko (0810.2183), delegated

- **Smooth loops** (§1.2, p.2, eq.1.3): finite after charge renormalization, up to exp(−const·L/a). This is attributed to Gervais–Neveu, Polyakov, and Vergeles–Dotsenko (1980). The factor is the mass renormalization of a heavy test particle, and it is absent in dimensional regularization (p.3).
- **Cusps**: "An additional logarithmic divergence appears for cusped loops" (p.3), first found by Polyakov (1980).
- **Multiplicative renormalization**: W = Z(g;θ)W_R, attributed to Brandt–Neri–Sato (1981) (eq.1.4). It holds only without light-cone segments. γ_cusp = −a d ln Z/da (eq.1.5). Its linear growth at large θ is due to Korchemsky–Radyushkin (eq.1.6).
- **Square loop normalized by its mean** (my inference, not in the source): the perimeter factor and the four corner factors are numbers fixed by geometry and cutoff, so they cancel in W/⟨W⟩. Contact terms with other operators, products of loops, and lattice artefacts do not cancel. ⟨W/⟨W⟩⟩ = 1, so this normalization is non-minimal and is not the local Z(g,θ). Makeenko's θ is Minkowskian (cosh θ); the Euclidean right-angle value is not evaluated there.

## 3. Failed predicates

- **flow_bench trial run (scratch; result file deleted; recorded in notes.md step 6)**: P5 and P6 failed. The cause was my own defect: in D_t = −[(G″ − G′/r)sin²θ + 2G′/r] I had dropped the factor 2 on G′/r. After the fix, with the predicates unchanged, run1 met all six.
- The sub-agent reported none. Its harness blocked it from writing report_child.md, so I saved its text.
- No failure is a defect of a source.

## 4. What I did not check

- The proofs in FdV–O'C §VI, and whether Thm 4 holds for SU(N) as well as U(N). The explicit constants are U(N).
- Mihajlovic outside pp.1–10, 97–103, 176–177 and 234–239, including Lemma 31.1, §§33–38 and Part VI. Also whether D4 claims matching upper bounds.
- A4's band constants against Thm PT.1.
- The Lüscher–Weisz BRS argument line by line.
- Lattice flow finiteness (open in the source itself).
- Brandt–Neri–Sato's own paper on self-intersections (not fetched).
- Benchmark predicate P4 is nearly tautological, because the quadrature grids scale with √t and σ.

## 5. Delegated question and outcome

- **Question**: Q4 (Makeenko: perimeter, cusp, multiplicative renormalization, attributions, and what they mean for a mean-normalized square loop).
- **Control**: the number of components of F for SU(2) in 4D. It answered 18, which is correct.
- **What came back**: the statements in Q4 above, and a PCP verify PASS.
- **My checks**:
  - I reran its script (predicates pass) and replayed child/pcp (PASS).
  - I checked two statements against pp.2–3 (eq.1.3 with its attributions; eq.1.4 BNS with the light-cone restriction). Both were found.
  - I confirmed zero hits for "intersect".
- Its point on mean normalization is its own inference. I agree with it, but we share a model family.

## 6. Commands to rerun

```
cd C:/Users/donke/z4-workers/r10-lit2 ; export PYTHONUTF8=1
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name extract_pdfs --expect-exit 0 -- python -I scripts/extract.py ref txt_replay2
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name flow_bench --expect-exit 0 -- python -I scripts/flow_bench.py run2
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name imtr_check --expect-exit 3 -- python -I scripts/imtr_check.py   # refuses: result exists
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
(cd child && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp && python -I scripts/find_terms.py)
```

**Counts (met, failed, measured only)**:
- flow_bench run1: 6, 0, 3 (trial run: 4, 2, 3, own defect).
- imtr_check: 2, 0, 0.
- extract replay: 5 of 5 files identical.
- Child find_terms: 5, 0, 0 (its claim, rerun by me).

**Verdicts** (15 rows):
- 8 STANDS.
- 3 DEFECT, all in input/LITERATURE.md, none in the lanes.
- 1 overlap requiring citation (D4 vs Mihajlovic).
- 3 comparison rows with no contradiction (B4, A4, and the general search of Mihajlovic).
- 0 NOT CHECKED rows; the unchecked parts are listed in §4.

PCP verify, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
