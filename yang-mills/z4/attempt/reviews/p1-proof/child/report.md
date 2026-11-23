# T25 report: sec_proof.tex against PROOF_B_v2.md and L3_L4.md

Control: control.txt = `7`. The source line is L3_L4.md:74, "βS_R ≥ (λ/16)|φ|² − 7|ψ|²".
The line numbers below are those of sec_proof.tex. "Proof" says whether sec_proof.tex itself supplies a proof of the stronger form.
Statements that rest on the standard facts of tex §standard are marked "mod std".

## 1. Verdict table
| # | Item (tex line / label) | Source | Verdict | Evidence |
|---|---|---|---|---|
| 1 | eq-main (l.11), Prop spectral (l.121), Lemma Wick, Assembly (l.512): the ratio bound holds for **every n≥1** | v2 Thm B′: even n≥2 | STRONGER-PROVED | S1 proof (l.121) says "odd or even". ⟨v,Tⁿv⟩ only needs θO=O and τⁿO∈𝒜₊. G(n)>0 and the Wick inequality are proved for all n≥1. v2 gives no reason for "even". |
| 2 | Lemma G(4) (l.~490), l.63: G(n)=1/(π²n⁴)+O(n⁻⁶), c(n)=4/(π⁴n⁸)(1+O(n⁻²)) | v2: G(n)≥c n⁻⁵, c(n)≥c₀n⁻¹⁰ (L3_L4 has none) | STRONGER-PROVED | A polar-coordinate proof is written out. I did not re-derive its inequalities (|g−g₀|≤3\|k\|³ etc.). Numerically π²n⁴G(8)=1.0925 (tex 1.092) and G(1)=0.0688747 (check1). The arithmetic 14400/π² was reproduced. |
| 3 | Lemma G(4): "C_G is an absolute constant made explicit by the proof" | no source | STRONGER-UNPROVED | Only the main part 14400/π² (|k|≤1 part) is displayed. The two tail pieces are called "explicit" but no value is stated, so C_G is not given. |
| 4 | Lemma G(2): G(n+1)<G(n) strictly | v2: 0<G(n)≤G(0) | STRONGER-PROVED | Positive integrand strictly decreasing in n (one line). Monotonicity holds numerically for n=0..9. |
| 5 | Lemma rp (l.73): F,G bounded measurable; reflections about every a | v2 Lemma 1: functions of 𝒜₊ | STRONGER-PROVED | Same proof, plus translation invariance (l.81). |
| 6 | Lemma limit (l.87–89): μ invariant under rotations and reflections of ℤ⁴ and all gauge transformations; DLR for bounded measurable g | v2 Lemma 1′: translation invariance; DLR for continuous local g | STRONGER-PROVED | Short but complete (l.94): symmetries pass to weak limits; two measures agreeing on continuous local functions are equal. Mod std (monotone class). |
| 7 | Lemma flat (l.224): any group G, any dimension d′, any box | L3_L4 Lemma A: the 4-box R | STRONGER-PROVED | The proof is written dimension-free. The tex "box" is silently ∏[−N_i,N_i]+z, which needs even side lengths. The source also uses the lemma on 3-boxes without saying so. |
| 8 | "Each link of ℤ⁴ lies in **exactly** 6 plaquettes" (l.25) | L3_L4 l.71: "at most 6" | STRONGER-UNPROVED | No proof in the tex. It is elementary: 3 other directions × 2 orientations. |
| 9 | Thm L3 (l.283–293): βS_R ≥ c|φ|²−7M² for β≥β₀(M), c=min(λ_N/16, η/(2ν_Rπ²)) | L3_L4 §2(b) (l.74–83) | STANDS | The same bound and constants as 2(b). I re-derived the near/far computation line by line: 48δ²e^{8δ}≤min(λ/16,1) gives λ/8−48δ²e^{8δ}≥λ/16 and 6+48δ²e^{8δ}≤7. The grandchild counted this bound as a strengthening over 2(d) only. |
| 10 | Thm L3: sup_ψ‖K_β−K_∞‖_TV→0, so W may depend on ψ or on extra parameters | L3_L4 2(d): "for every bounded measurable W(φ,ψ)", W fixed first | STRONGER-PROVED | Stronger than the literal 2(d). The source states the uniformity in W only in 2(c) (l.~92 "possibly also depending on ψ and on an extra parameter") and in the §3(c) "Colour" remark. The tex proves it: l.316 bounds ∫\|f_β−f_∞\| uniformly, and the ratio bound is 2∫\|f_β−f_∞\|/∫f_∞. |
| 11 | Prop L4 existence (l.328): **every** sequence β_k→∞ with μ_k∈𝓛_{β_k} has a convergent subsequence | v2 L4: "along some β_k→∞" | STRONGER-PROVED | Tightness is uniform in β≥1 and μ (Cor tail). Prokhorov, diagonal extraction and Kolmogorov are mod std. L3_L4 §3(b) already reads "a subsequence (β_k,μ_k)". |
| 12 | Prop L4(d) (l.333): μ_∞(½\|F_p\|²>t)≤e^{60.2−t/8} for the limit | sources state only the finite-β tail and bounded moments | STRONGER-UNPROVED (partly) | The tex says "follows from Cor tail because {½\|F\|²>t} is open". But O_p≤½\|F\|², so {O_p>t}⊂{½\|F\|²>t} points the wrong way. A (1−ε) rescaling of t and ε→0 is needed and is not written. True, and a short step. |
| 13 | Lemma R (l.438): E\|f\|⁴<∞, "colours of f may be correlated", f constant per plaquette type; constancy by a direct L² argument | v2: spectral-measure argument, h "a random constant" | STRONGER-PROVED | Jensen gives E\|h\|⁴≤E\|F\|⁴. The constancy argument was re-computed: Σ_e‖v_e−u‖²=16‖u‖²−16‖u‖²=0. It uses only harmonicity and stationarity. |
| 14 | Lemma Wick (l.497): formula Cov=3/2 G²+G E\|f\|²+¼Var\|f\|², Var X₀≥3/8, Cov≥c(n)Var | v2 inequality | STANDS | Term-by-term ratios are ≥c(n) since G(n)/G(0)≤1. |
| 15 | Lemma G(1),(3), Lemma D, D*=60.1922, Cor tail, chessboard lemma, Lemma E, Lemma shell, Cor zero, forest gauge (as restated with the hypothesis B) | v2 and L3_L4 | STANDS | D*=60.192240 and c_H=0.15025785 recomputed. G(n)≥the Lemma G(3) bound for n=1..8. The tex forest-gauge lemma is weaker than v2's (it adds B). E3's hypothesis is s_p<π, which is more restrictive than the source's α(U_p)<π. |
| 16 | Prop L4(a)–(c), (e) | L3_L4 §3(a),(c) | STANDS | Same statements. The cube word identity eq-cube was verified mechanically (check1 P3). The 30 letters reduce to the empty word and all six printed words match the plaquette definition. |
| 17 | Prop L4(d) moments / joint convergence | L3_L4 §3(b) | STANDS | Moments via sup μ_k(O⁴)<∞ and uniform integrability, mod std. |
| 18 | Lemma D numerics l.435: C^{R_N}_{p₀p₀}=7/24, 0.49267, 0.49916 (N=1,2,3); l.261: λ₁=0.837722, λ₂=0.147122 | L3_L4: λ values, 7/24, "0.4927"; v2 M1 "0.4992" (length-6 label) | NOT CHECKED | "For orientation only". The values are quoted from prog1 and are not reproduced here. The extra digits 0.49916 are in neither source. |
| 19 | The theorem thm:main being proved (\ref in l.3) | — | NOT CHECKED | The statement is outside sec_proof.tex. The file itself (l.5–8) repeats v2's three restrictions (L=2^k, limit points only, "m→0 includes m=0"), so it adds no strengthening beyond items 1 and 2. |
| 20 | §standard (l.527+): ten facts used without proof (Polish regular conditional laws, Scheffé, Lévy downward, Weyl, Plancherel, Isserlis, …) | L3_L4 §6 lists six | NOT CHECKED | The tex lists more than the sources. These are textbook facts and I did not source-check any of them. |

Counts note: row 15 bundles about ten items, so the row counts below are by row, not by statement.

**Row counts (20 rows): STANDS 5 (rows 9,14,15,16,17), STRONGER-PROVED 9, STRONGER-UNPROVED 3 (rows 3, 8, 12), NOT CHECKED 3.**

## 2. Failed predicates
check1.py: 25 met, 0 failed, 0 measured only. These are P1, P2, P3a, six P3b, ten grid-convergence checks, G(0), G(1), n=8, monotone, lower-bound, and P5. No failure of my own expectation and no defect of the target on this run.
Tolerances: those for D* and c_H come from the digits printed in sec_proof.tex (5e-5 and 1e-6). The G-integral tolerances are 2e-3 relative between grids 64³ and 128³ and 5e-3 absolute for G(0) and π²n⁴G(8). I chose those myself. The grid check showed agreement to 1e-6 or better.
None of the predicates was "for all …" over a quantified case family. The cube identity is for the generic free-group word, and the n=1..8 and 0..9 checks are finite lists, not a proof for all n.

## 3. Not checked
- I did not re-derive the inequalities inside Lemma G(4), the free-energy upper integral, the chessboard iteration, E2/E3, or Steps 1–7 of Prop L4(e) beyond reading them.
- I did not re-run prog1 or the Monte Carlo of L3_L4 §5, nor λ_N or C^{R_N}.
- I did not check any of the standard facts (rows 18–20), and I did not see Theorem 1.1's own text.
- The claim in row 6 that the weak limit preserves rotation invariance on a torus embedded around the origin is one line in the tex; I did not examine it further.

## 4. Delegated question and outcome
- Grandchild task id: **T26**. It was admitted with `task-admit … --by principal --label p1-proof-child-grandchild --parent T25` and released with `task-release … --id T26` (events 50 and 51).
- Control answer: `6` (grandchild/control.txt). I re-checked it against L3_L4.md:71, "Each link lies in at most 6 plaquettes".
- Question: compare ONLY the statement of pf:thm-L3 with L3_L4 §2(d).
- It returned: (i) the explicit −7M² lower bound and the c with β₀ are not in 2(d); (ii) the TV/uniform-in-W form is stronger than 2(d); (iii) the K_∞ mean formula is not in 2(d); (iv) the tail statement is equal, with an added β≥β₀.
- My re-check against the files, with corrections:
  - Points (i) and (iii) are accurate for 2(d) as written, but both are in the source (§2(b) l.74–83, §2(c)). In my table they are STANDS relative to the source as a whole.
  - Point (ii) holds: 2(d) fixes W first, and 2(c) states uniformity in W.
  - I found nothing further stronger in the theorem statement. I read the grandchild's findings.md, not only its summary.

## 5. Commands to rerun
```
cd /home/user/z4-workers/p1-proof/child
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name check1 --expect-exit 0 -- python3 -I check1.py   # (delete check1_result.txt first; it is opened with mode "x")
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
PCP OS verify, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`.
Rust pcpos verify, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.` (the line before is the register SHA-256 4b4ff9d3…c766acb).
