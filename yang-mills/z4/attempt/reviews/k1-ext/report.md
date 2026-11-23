Overall verdict: I found no defect in the exterior bound limsup‖1_A T 1_A‖ ≤ max_{F=0, x∈A} e^{-E(x)} of target/two-site-exterior/README.md. On (2): the README proves it for the periodic 2³ box only, and full-neutral.md §1 uses it on every fixed box N₁N₂N₃. No step of the proof depends on the 2³ box, and full-neutral.md §1 supplies the dimension extension and the general-N strict minimum on the flat locus, so what is used matches what is proved.

Worker k1-ext (task T116), cross-review for Director Z4. Principal: Kirtus Justus. Date: 2026-11-23. I share a model family with the director, so my agreement is not independent review. The author of the target is of a different lineage.

## 1. What the README proves, what full-neutral §1 needs

**(1) Proved in target/two-site-exterior/README.md (inequality (1), section "Transfer and local norm bound").**
- Box: the periodic 2³ spatial lattice only. X = SU(2)²⁴, and the final line says "All constants here refer to the fixed two-site-per-direction spatial regulator".
- Operator: T = M K M on the full L²(X, Haar). This is the temporal-gauge transfer on all functions, not only gauge-invariant ones. M = e^{-βS/2}, S = |F|²/2 with F the 24 quaternion plaquette differences, and K is the product of the 24 normalized one-link Wilson electric convolutions.
- Region: any closed A ⊂ X.
- Statement: limsup_{β→∞} ‖1_A T 1_A‖ ≤ max_{p∈A, F(p)=0} e^{-E(p)}, where E(p) = Σ arsinh σ_j(D_p) runs over all 72 singular values. The coordinates have generators iσ/2, and an empty maximum counts as 0.
- What is bounded: the operator norm, not only a form on a subspace. The absolute-value step |⟨f,Tf⟩| ≤ ⟨|f|,T|f|⟩ and self-adjointness of 1_A T 1_A give the full norm.
- Uniformity: none in rate. The compactness argument gives a limsup only, with no power rate (the README says so). The threshold in β depends on A.
- Hypotheses: isotropic Wilson action; unit time step; X compact; F smooth; normalized electric kernel with second distance moment O(s²); scales ρ = β^{-3/8}, ε = β^{-1/4}, s = β^{-1/2}.

**(2) Needed by full-neutral.md §1 and §3.** The same inequality on every fixed box N₁N₂N₃ with N_i ≥ 2, with E = ½Σω(σ_j²) in quaternion-angle units and ω(x) = 2 arsinh(√x/2). It is applied to A = the complement of a fixed open neighbourhood of the eight central flat orbits. Combined with the strict minimum of E on the flat locus, it gives ‖1_A T 1_A‖ ≤ g − η_N/2 for large β. This is the fixed exterior deficit used in §3 ("the exterior lies a fixed distance below g").

**Do they match?**
- Normalization: yes. ½ω(σ_fn²) = arsinh(σ_fn/2) = arsinh(σ_README), with σ_fn = 2σ_README. My predicate P2b checks this term by term, with error 0.
- Box size: the README states (1) for 2³ only. full-neutral §1 says the README's argument gives the bound "on any fixed box", which credits the README with more than it states. full-neutral then supplies the extension itself: partition, magnetic affine bound, kinetic domination, translation of b, nonflat balls and compactness, each with N-dependent constants.
- What the extension needs: X = SU(2)^{3n} compact, F smooth, the per-link kernel facts (identical for every link), and a partition with bounded overlap. None of these depends on the box. The general-N curl spectrum and the strict minimum are supplied in full-neutral §1 (curl formula and heat-trace walk argument). My P1, P3 and P4 confirm both numerically on 3×2×2 and 3×3×2.
- Rate: none is needed. §3 uses only a fixed deficit at fixed N.

## 2. Verdict table

| # | Item | Verdict | Evidence (one line) |
|---|---|---|---|
| 1 | Match of scope: README (2³) vs full-neutral §1 use (every fixed box) | STANDS | No step of the README proof of (1) depends on the box. full-neutral §1 repeats each step with O_N constants and supplies the general-N flat-locus minimum. |
| 2 | Partition (IMS) error C s²/ρ² = β^{-1/4} | STANDS | Hand check: the identity Σ_jη_j(x)η_j(y) = 1 − ½Σ(η_j(x)−η_j(y))², Lipschitz constant O(1/ρ) from bounded overlap, kernel second moment O(s²), Schur test. s²/ρ² = β^{-1/4} as in PRIOR_REVIEW row 13. |
| 3 | Kinetic domination on a ball: (1+O(ρ²+s²)) × Gaussian of variance 4s²/(1−Cρ²) | STANDS | Hand check: 1−cos(d/2) ≥ (d²/8)(1−d²/48); d² ≥ (1−Cρ²)\|z−z'\|²; normalizer (8πs²)^{3/2}(1+O(s²)); Haar flattening 1+O(ρ²). |
| 4 | Magnetic affine bound \|F\|² ≥ (1−ε)\|b+Dz\|² − Cρ⁴/ε, with βρ⁴/ε = β^{-1/4} | STANDS | Algebra is the Lean identity affineRemainder (scalar). P7: the Taylor remainder satisfies \|r\|/ρ² ≈ 0.22, stable over ρ = 0.2, 0.1, 0.05 at 60 base points, so C is uniform. |
| 5 | Affine model: range part of b removed by translation, orthogonal part decreases the norm, SVD separates the variables | STANDS | Child claims C and D, rerun by me: norm independent of b to 3e-16; orthogonal factor exactly exp(−\|c\|²/2); 2D value 0.192574 equals the exact value. |
| 6 | 1D oscillator: top eigenvalue e^{-arsinh σ}; norm 1 at σ = 0, not attained | STANDS | Child A and B and grandchild: grid matches to 2e-16 at σ = 0.25, 1, √2, √3, 3. Analytic σ = 1 gives √2−1. At σ = 0 the norm on a finite box rises 0.880 → 0.997 as the box grows. |
| 7 | Perturbed σ' = σ√((1−ε)/(1−Cρ²)) gives local norm ≤ e^{-E(p)} + O(β^{-1/4}) uniformly in p | STANDS | arsinh is 1-Lipschitz, the singular values are uniformly bounded on compact X, and there are 72 coordinates. |
| 8 | Ball in {S ≥ b₀}: norm ≤ e^{-βb₀} | STANDS | M ≤ e^{-βb₀/2} at both ends and ‖K‖ ≤ 1. |
| 9 | Compactness: worst ball centres, flat and nonflat limits, continuity of E across rank changes | STANDS | Weyl continuity of singular values. A is closed, so limits stay in A. No inverse of D is used. |
| 10 | Norm of 1_A T 1_A versus a form on a subspace | STANDS | Absolute-value and kernel-positivity step on the full L²(A). It is the operator norm. |
| 11 | Flat locus = commuting triples up to conjugation; simultaneous diagonalization | STANDS | In SU(2) the centralizer of a non-central element is a maximal torus, so every commuting triple lies in one torus. |
| 12 | Curl singular values √(Σ sin²((p_j+qθ_j)/2)), two per (p, q) plus one zero | STANDS | P1: real-space SVD equals the Fourier formula, max error 1.0e-14 on 2³, 3×2×2 and 3×3×2. Target check.py (with shim): 2e-15. |
| 13 | E and rank at regular and enhanced-stabiliser holonomies, e.g. φ = (c,0,0) | STANDS | P3: rank 6n−6 at central points and 6n−2 at all non-central sampled points, including (c,0,0) and (c,c,0). E − E_* at φ = (0.3,0,0) is 0.595. |
| 14 | Strict minimum of E on the 2³ flat locus (pairing f(a−t) + f(a+t), f concave) | STANDS | P4: 36 of 48 sampled points are non-central, and min(E − E_*) = 0.047 > 0. P5: along (c,0,0), E rises strictly to c = π/2 (by +2.088) and then falls. M1: E − E_* ≈ 2\|φ\| near the centre. |
| 15 | Gauge quotient near non-central flat points (U(1) stabiliser) | STANDS | Not used: (1) is proved on the full link space. Gauge directions are zero singular values with factor 1 (free convolution). P6: singular values change by 1.3e-15 under a site gauge. |
| 16 | Vacuum lower bound: λ₀ → e^{-E_*} by trial at one centre | STANDS | Hand check: quartic terms βs⁴u⁴ → 0 for fixed support; β → ∞ is taken before the supremum over trials. Not used by full-neutral §1. |
| 17 | Exponential exclusion at fixed distance (weight e^{aD/s}) | STANDS | Hand check: ‖WTW⁻¹ − T‖ = O(a); W = 1 on A^c; Neumann series. Not used by full-neutral §1. |
| 18 | Centre-character splitting, upper bound | STANDS | Hand check: exact form-defect identity, then exterior and distance-tail estimates. Not used by full-neutral §1. |
| 19 | Path connection and pointwise T^m ≥ e^{-C/s}; splitting lower bound | STANDS | Hand check of the chain of balls, ‖u‖_∞ = O(s^{-36}), and signed mass. Target check_paths.py: 60 configurations and 660 contractions pass. The word-reduction constant is checked only numerically (49·defect). Not used by full-neutral §1. |
| 20 | Lean file TwoSiteExterior.lean | STANDS | Rerun exit 0; axioms: none, none, and [propext, Classical.choice, Quot.sound]. Content: centralRank is (42:ℕ)=42 and orthogonalPairs is (56:ℕ)=56, both tautologies; the counts are computed only in worker.c. affineRemainder is a real scalar ring identity. |
| 21 | worker.c | STANDS | Compiled with gcc -nostdlib -static; modes 0, 1 and 2 exit 0. It checks the shell counts 18/18/6, regular rank 46, the 56 orthogonal sign pairs, and an integer form of the identity. |
| 22 | Citations: Sint hep-lat/9312079 §3; García Pérez–Snippe–van Baal hep-lat/9608015 §3.1; Klein–Rosenberger arXiv 1706.06357 | STANDS | Read (see §5). The locators match the use. GPSvB §3.1 gives the charge-shift structure k → k + sC/N, s = 0, ±1. |
| 23 | verify.py replay | NOT CHECKED | It imports replay from ../../local-response, which is absent from target/. |
| 24 | Identity of target/two-site-exterior with the path cited in full-neutral (../../central-quotients/…/two-site-exterior/README.md); README link ../second-box-holonomy/README.md; GitHub links (A4); DOI 10.3233/ASY-151343 | NOT CHECKED | The files are absent, and GitHub is not in my network list. The DOI was not fetched. |

**Verdict counts:** STANDS 22, DEFECT 0, NOT CHECKED 2.

**Predicate counts (met, failed, measured only):**
- Own program own/e_path.py: 8, 0, 1.
- Target check.py: 2 runs. With the numpy shim it asserts and passes; without the shim it exits 1 on the missing scipy import, which was the expected exit.
- Target check_paths.py: 1 pass.
- Child (as rerun by me): 20, 0, 1.
- Grandchild: 1 analytic value with 4 grid agreements, all met.

**Points to state plainly (not defects):**
- (a) full-neutral §1 credits the README with "any fixed box"; the README states 2³ only. The gap is closed by full-neutral's own sketch, at the same level of detail as the README.
- (b) The README's sentence that Lean "accepted the two count declarations" describes n = n tautologies. The counts are verified only in C.
- (c) Lean covers only the scalar case of the affine identity. The vector case follows from the same algebra with inner products, but that is not formalized.
- (d) (1) has no rate. This suffices for the fixed-N use in full-neutral §3.

## 3. Hypotheses each statement uses, and where they are stated

**README (1)**
- Isotropic SU(2) Wilson transfer on periodic 2³ with unit time step, and electric convolution normalized to preserve constants: README paragraph 1.
- X compact with product Riemannian metric and generators iσ/2: section "Transfer and local norm bound", paragraph 1.
- T = MKM with symmetric, positive, continuous kernel: same paragraph.
- Scales ρ = β^{-3/8} and ε = β^{-1/4}: paragraphs 3 and 5.
- Partition with bounded overlap: paragraph 3.
- Smoothness of F: implicit (polynomial in the links).

**README wells**
- Flat ⇔ commuting holonomies: section "The wells", paragraph 1.
- Curl formula: same paragraph.
- Strict concavity of arsinh√x: same paragraph.

**README claims 2 and 3**
- (1) plus the vacuum asymptotics: section "Exponential exclusion".
- Gaussian distance tail of K: same section.
- Path lemma with constants L and B': section "Connecting low-action configurations".

**full-neutral §1**
- Box N_i ≥ 2: header.
- Conventions of the central-patch README: header (that file is context; I did not re-verify it).
- The README's (1): §1 paragraph 1.
- Dimension extension: §1 paragraph 1.
- Curl spectrum at general N: §1 paragraph 2.
- ω as a Bernstein function and the walk expansion: §1 paragraph 3 (PRIOR_REVIEW row 14).

## 4. Failed predicates

- **Own program:** none. Before the recorded run I made one unrecorded dry run of the same program into own/trial_dry.txt. Its output is identical in all predicates to the recorded run own/results_e_path_run1.txt.
- **Target checks:** check.py fails without scipy (ModuleNotFoundError, exit 1). This is an environment defect, not a defect of the target. It passes with a numpy shim for scipy.linalg.eigvalsh (shim/scipy/linalg.py).
- **Child (its own report):** no failed predicates. It reported two process faults of its own:
  - Its first run used several BLAS threads, contrary to the 1-core rule. My rerun used OMP_NUM_THREADS=1 and gave the same numbers in 14 s.
  - Its rerun of the grandchild script failed because that script opens its output with mode "x" and the file already existed. This is expected behaviour, not a defect. My rerun in a fresh copy passed.

## 5. What I did not check; sources read

**Not checked**
- verify.py replay (module absent).
- Whether the target copy is byte-identical to the README at the path cited by full-neutral.
- The A4 central-patch documents and full-neutral §§2–3, beyond confirming that they use only a fixed exterior deficit.
- The link ../second-box-holonomy/README.md.
- GitHub links.
- DOI 10.3233/ASY-151343.
- The exact constant in the word-reduction bound (only check_paths.py was run).
- A numerical test of inequality (1) itself: not feasible in 72 dimensions. My program checks its inputs (E, ranks, Taylor remainder), and the child checks the oscillator model.

**Sources read** (fetched by a web-fetch sub-agent; PDF text extracted into my scratchpad, outside this directory; no paper text copied)
- arxiv.org/abs/hep-lat/9312079 and the PDF: S. Sint, "On the Schroedinger functional in QCD", 1993 (Nucl. Phys. B421 (1994) 135). Section 3: temporal-gauge transfer T₀, gauge projector, T = T₀P. Equation numbers (3.3)–(3.8) were seen in that section.
- arxiv.org/abs/hep-lat/9608015 and the PDF: M. García Pérez, J. Snippe, P. van Baal, "Improved action and Hamiltonian in finite volumes", 1996. §3.1, "The SU(2) effective potential": abelian constant background with charge-shifted momenta.
- arxiv.org/abs/1706.06357 (abstract): M. Klein, E. Rosenberger, "Harmonic Approximation of Difference Operators" (J. Funct. Anal. 257 (2009)).

## 6. Delegated questions and outcomes

**Child: task T120.** Admitted under T116 (child_admit.log) and released (child_release.log).
- Question: numerically verify, for k(u,v) = (8π)^{-1/2} exp(−(u−v)²/8 − σ²((u−b)²+(v−b)²)/4):
  - A: the top eigenvalue is e^{-arsinh σ};
  - B: the norm is 1 at σ = 0;
  - C: the norm does not depend on b;
  - D: the 2D version, with the range part of c removed by translation and the orthogonal part contributing exp(−|c|²/2).
- Control: arsinh(1) = 0.881374. I graded it first and it is correct (ln(1+√2) = 0.8813736).
- Outcome: A, B, C and D STAND. 20 met, 0 failed, 1 measured only. I reran its program in rerun_child/ (K10, exit 0) and the numbers reproduce. Independent spot values: e^{-arsinh 3} = 1/(3+√10) = 0.1622777 and e^{-arsinh √3} = 2−√3 = 0.2679492.

**Grandchild: task T121.** Admitted and released by the child (child/notes.md).
- Question: analytic Gaussian-ansatz eigenvalue at σ = 1.
- Control: ln 2 = 0.693147, correct.
- Outcome: α = 1/√2 and λ = √2−1, matching the grid to 6e-15. I reread its algebra (v² coefficient 3/8 + α/2) and reran its script in rerun_grandchild/ (K11, exit 0).

## 7. Commands to rerun (from /home/user/z4-workers/k1-ext)

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"            # control 0.272341
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name target-check-noshim --expect-exit 1 --cwd target/two-site-exterior -- python3 check.py
$P check --ws pcp --name target-check-shim --expect-exit 0 --cwd target/two-site-exterior -- env PYTHONPATH=/home/user/z4-workers/k1-ext/shim python3 check.py
$P check --ws pcp --name target-check-paths --expect-exit 0 --cwd target/two-site-exterior -- env PYTHONPATH=/home/user/z4-workers/k1-ext/shim python3 check_paths.py
cp target/two-site-exterior/TwoSiteExterior.lean TwoSiteExterior_rerun.lean
$P check --ws pcp --name lean-rerun --expect-exit 0 --cwd /home/user/z4-lean --timeout 600 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/k1-ext/TwoSiteExterior_rerun.lean'
$P check --ws pcp --name own-e-path --expect-exit 0 --timeout 300 -- python3 own/e_path.py /home/user/z4-workers/k1-ext/own/results_e_path_run1.txt   # use a new output name: mode "x"
gcc -O1 -nostdlib -static -fno-stack-protector -o wrk/worker target/two-site-exterior/worker.c
#  task.bin bytes: wrk/m0 = 00 00 00, wrk/m1 = 01 04 03, wrk/m2 = 02 04 03
$P check --ws pcp --name worker-mode0 --expect-exit 0 --cwd wrk/m0 -- ../worker   # likewise worker-mode1 (wrk/m1), worker-mode2 (wrk/m2)
$R task-admit $G --by principal --label k1-ext-child --parent T116
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T120
$P check --ws pcp --name rerun-child-gauss --expect-exit 0 --cwd rerun_child --timeout 300 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 check_gauss.py
$P check --ws pcp --name rerun-grandchild --expect-exit 0 --cwd rerun_grandchild -- env OMP_NUM_THREADS=1 python3 check.py
$P verify --ws pcp
$R verify pcp/register.jsonl
```

**Last lines of the verify commands:**
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
