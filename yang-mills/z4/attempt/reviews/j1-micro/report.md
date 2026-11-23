# j1-micro report (T108): micro-review of A3_NOTES.md §§7–10 and sec_smallbox.tex against records/

Control: `control.txt` = 0.272341 (−ln tanh 1), written first. Lean was not used, and I make no Lean claim.
I share a model family with the director, so my agreement is not independent review.

Abbreviations:
- N§k:l means `inputs/A3_NOTES.md` section k, file line l.
- S:l means `inputs/sec_smallbox.tex`, line l.
- Record locations are file:line under `records/`.

## 1. WRONG and OVERSTATED items, with proposed replacement text

| # | where | verdict | the record says | proposed replacement |
|---|---|---|---|---|
| 1 | N§7:91 "a two-term fit in β^(−2/3) gives 1.97496" | WRONG | The E + cβ^(−2/3) fit gives 1.9728 ± 0.0014 (g2-numchal/report.md:19). 1.97496 comes from the β^(−2/3)+β^(−1) fit (:20). The paper (S:114) has this right. | "a two-term fit in β^(−2/3) and β^(−1) gives 1.97496" |
| 2 | N§7:93 "the data below double precision do not fix the form" | WRONG (wrong data named) | The data that fail to fix the form are those up to β = 64, which are above double precision (local exponents 0.93, 0.81, 0.72; g2-numchal:23). β ≥ 128 was NOT CHECKED (:24). | "is not established: the data up to β = 64 do not fix the exponent, and β ≥ 128 was below double precision there (see §9)" |
| 3 | S:94–95 "Measured center-odd splittings do not fix the form e^{−c√β}: they fall below double precision from β=128." | WRONG (stale) | The record says more than this. m_eo was measured at β = 96–256 in double-double arithmetic (i1-tunnel:18–19, 37–40). The fits favour c = 4.6054 but do not establish it (:15–16, 62). | "Measured center-odd splittings (double precision up to β = 64, double-double arithmetic up to β = 256) favour −log m ≈ c√β + qβ^{1/6} with c ≈ 4.60, but four to six points do not establish the form." |
| 4 | N§9:128 "q = −8.1 (predicted −8.99, about 12 per cent off …)" | WRONG (arithmetic) | (8.99−8.1)/8.99 = 9.9 % and (8.99−8.1)/8.1 = 11.0 % (arith P11; child Q14). The record's "12%" (i1-tunnel:100) refers to the free-fit q ≈ −7.9. With c fixed, −8.08 against −8.989 is 10.1 %. | "q = −8.1 (predicted −8.99, about 10 per cent off; the free fit's −7.8 is about 13 per cent off)" |
| 5 | N§9:128 "my size estimates … were too small by up to five orders" | WRONG (arithmetic) | Estimates 1e−18, 1e−24, 1e−30 against measured 1.46e−16, 4.13e−21, 5.40e−25 (i1-tunnel:20). The ratios are 10^2.16, 10^3.62 and 10^5.73 (arith P12). | "too small by two to almost six orders (factors 1.5·10², 4·10³, 5·10⁵ at β = 128, 192, 256)" |
| 6 | N§7:91 "agrees with the Peter–Weyl diagonalization to 4.6·10⁻⁹ or better at every β" | OVERSTATED | 4.6e−9 applies to m_e at the ten β = 2…1024 only. The second level agrees to 1.1e−8, and m_eo to 3.6e−5 relative for β ≤ 64 only (g2-numchal:12–13). | "agrees for m_e to 4.6·10⁻⁹ or better at all ten β from 2 to 1024 (second level 1.1·10⁻⁸; m_eo 3.6·10⁻⁵ relative, β ≤ 64)" |
| 7 | S:137–138 "The lattice spectrum was computed by two methods …, which agree to 4.6·10⁻⁹ or better." | OVERSTATED | Same as #6. | "The lowest center-even gap was computed by two methods (…), which agree to 4.6·10⁻⁹ or better at β = 2, …, 1024; the second level agrees to 1.1·10⁻⁸." |
| 8 | N§8:113 "challenged in h1-chal: 11 steps stand, 1 defect …, one constant derived wrongly (corrected to 79σ²), one partition function that was not Lipschitz (replaced)" | OVERSTATED (conflated) | See the four points after this table. | "upper half and lemmas L1–L5 challenged in h1-chal (11 of 12 items stand; 1 defect: a sign in the localisation identity, the bound used survives; the capped-fibre constant rederived as 79σ²). The lower half L6/L7 was written in full in LIMINF.md, whose author also replaced the L5 partition by a Lipschitz one; L6/L7 have not been challenged, and the m_e corollary is conditional." |
| 9 | S:81–84 "challenged once by a session of the same lineage: 11 steps stood, one sign defect was corrected …, one constant was rederived and one partition function replaced" | OVERSTATED (same as #8) | Same as #8. | "Its upper half and its lemmas up to tightness were challenged once by a session of the same lineage (11 of 12 items stood; one sign defect, the bound used survives; one constant rederived); the concluding liminf steps, written in full by another session of that lineage (which also replaced one partition of unity), have not been challenged." |
| 10 | N§8:116 "Lüscher's g^(2/3)/L with identical coefficients"; also N§8:115 "In Lüscher's normalisation" | OVERSTATED | The coefficients were matched against van Baal eq. (9) (h2-ground:9, 35, 50). Lüscher 1983 was read as an abstract only, and that abstract "gives no numbers" (h2-ground:29). The paper (S:163–165) has this right. | "the g^(2/3)/L form of Lüscher's expansion, with coefficients identical to the leading-order H_eff of van Baal eq. (9) (Lüscher 1983 read as abstract only)"; and "in the normalisation of van Baal's review" |
| 11 | N§9:128 "5.4032·10⁻²⁵ at β = 256 (the last digit at 256 not guaranteed …)" | OVERSTATED | The record says the "3rd digit [is] not guaranteed by my error bound": the Rayleigh-quotient bound is 1.6e−3 relative, about 2e−3 (i1-tunnel:19, 90). Separately, at β = 128 the N-change is 2.0e−4 relative (:18, 38), so the 5 digits of 1.4597e−16 also exceed the convergence test. | "5.40·10⁻²⁵ at β = 256 (relative error ≤ 2·10⁻³ by the worker's bound; the N-change 2.7·10⁻⁶ suggests less); 1.460·10⁻¹⁶ at β = 128 (N-change 2·10⁻⁴)" |
| 12 | N§9:128 "m_oo/m_eo = 2.00000" | OVERSTATED | 2.00000 for β = 64–192 and 1.99998 at β = 256 (i1-tunnel:21, 40). | "m_oo/m_eo = 2.00000 (β = 96–192) and 1.99998 (β = 256)" |
| 13 | N§10:136 the control sentence (β = 2: 1.6291 ± 0.0132 …; "The control at β = 1 failed its plateau rule") | OVERSTATED | All three exact controls failed the pre-registered plateau rule. That covers β = 1, β = 2, and β = 4 at both T values (i1-mc3:84–87). CTRL at β = 4, T = 24 failed with z = −44 (:90). β = 2 was "met only vacuously" (error 0.56) (:92). 1.6291 comes from the post-hoc ctrl0 analysis (t0 = 0, 2-point window) (:14, 95). | "Controls, all of which failed the pre-registered plateau rule and were recovered only by post-hoc analyses: the exact gap at β = 2 (1.6291 ± 0.0132 with t0 = 0; …) and at β = 4 (0.96904 ± 0.00380, differenced correlator at T = 48, …). β = 1 failed in both analyses." |
| 14 | S:141 "plateau rule fixed in advance; controls: the exact gaps at β=2 and 4 …" | OVERSTATED | Same as #13. As written, the controls appear to have passed under the pre-registered rule. They did not. | "plateau rule fixed in advance for the main runs; controls: the exact gaps at β = 2 and 4, reproduced only by post-hoc analyses (t0 = 0; a differenced correlator removing a center-sector floor) after the pre-registered analysis failed there, and the two-direction value at β = 256, …" |
| 15 | N§10:142 "falls from 0.28(4) at β = 16 to zero within errors from β = 1024" | OVERSTATED | At β = 1024 the value is +0.018 ± 0.011, which is 1.6σ (arith P14). The record calls it "consistent with zero at β=4096" (i1-mc3:63–65, 72). | "falls from 0.28(4) at β = 16 to 0.018(11) at β = 1024, and is zero within errors at β = 4096 and 16384" |
| 16 | S:141 "the E–T₂ splitting vanishes within errors from β=1024" | OVERSTATED | Same as #15. | "the E–T₂ splitting falls to 0.018(11) at β = 1024 and vanishes within errors at β = 4096 and 16384" |
| 17 | N§10:142 "The pre-registered checks were met: within 8 per cent … in all three channels, and the deviation shrinking from β = 64" | OVERSTATED (minor) | MONO was pre-registered for E and T₂ only. For A₁ it is "met (measured only)" (i1-mc3:51). | "… and the deviation shrinking from β = 64 (pre-registered for E and T₂; for A₁ measured only)" |

Details for #8 and #9:
- h1-chal challenged SCALING_LIMIT.md only. L6/L7 were "outside the brief" (h1-chal/report.md:53).
- The 79σ² correction (h1-liminf/report.md:16) and the replaced partition (:17; LIMINF.md:153) come from the LIMINF builder, not from the challenge.
- h1-chal itself rated L4 as STANDS ("98.7σ² is true but not derived", 79σ²) and L5 as STANDS (minor gap: the Lipschitz property was unstated) (h1-chal:19–20).
- No challenger has read L6/L7. Their author marks the m_e corollary "NOT CHECKED (conditional)" (h1-liminf:12).

**Internal consistency, notes against paper, and within the notes:**
- On #1 and #10, the paper is right and the notes are wrong.
- N§7:95 "Nothing is measured about the three-direction limit" contradicts N§10. It was true of g2-three (g2-three:21) and was superseded by i1-mc3.
- N§7:93 ("below double precision") conflicts with N§9's double-double measurement. That is #2 and #3.
- N§8 "van Baal pp. 11–15" against S:170 "pp. 11–12": both are supported. h2-ground:17 gives 11–15 for the whole Q4 row, and z > 0.9 is at pp. 11–12 (:58). The paper is the more precise of the two.
- Every other number shared by the notes and the paper agrees: 3.3505330/5.3254970, 1.974964, 1.97583, 0.19238/0.19331, 6.534885, 3.012539, 3.602838, 4.1167196, 1.89778/2.26965, 1.5·10⁻⁷, the MC table, 1.8σ, −2.39/−3.35, 27/30.

## 2. Counts

**Statement verdicts.** Over the 82 checked statements (17 rows in the table above, 46 MATCHES, 19 not checkable):
- WRONG: 5 (#1–#5)
- OVERSTATED: 12 (#6–#17)
- MATCHES: 46
- UNSUPPORTED by records but resting on other sources (not checkable here): 19 (§3)

These are counted at sentence-or-number-group granularity. The 46 MATCHES are listed below.

**MATCHES:**
- **N§7:**
  - Nyström/Funk–Hecke/Lanczos method; E₀ and E₁ reproduced (g2-numchal:12, 14–15).
  - Geometric extrapolation 1.97583 (:21); "± 0.00003" with 1.97496 (:20).
  - O(2) doublet, charge 2 (:16); 0.19238 against 0.19331 (:16); the child's unconverged grid (:17).
  - Continuum operator on R⁹ and E₀ 6.534885 (g2-three:20, 98); first gap 3.012539, J = 2, five-fold; scalar gap 3.602838 (:20).
  - Lattice converged to β = 4: 2.876, 1.6215, 0.969 (:18); β = 8 not converged (:19); 2.88, 2.04, 1.54 (:21; arith P7).
  - limsup proved (g2-conv:4, 16); five lemmas (SCALING_LIMIT:102–137); Γ-liminf sketched (g2-conv:5, 19).
  - Brief defect 3 ln β (g2-conv:14); coercivity coefficient 1 false, 1 − K ≤ 1, every β (SCALING_LIMIT:181).
- **N§8:**
  - 30/27/0/3 and the three reasons (h1-a4:36–41); wording slip "concavity" (:15); Lean scalar-only, exit 0 (:24–25).
  - 0.976 at β = 64 and 256 (:19); 3.3537/5.3316 (:1, 28).
  - Four-box/capped-arm architecture (SCALING_LIMIT); Lean of LIMINF nine lemmas (h1-liminf:26); the reviewers' lineage (h1-a4:4).
  - Constant modes (βL³)^(−1/3)h₃ (h2-ground:48); bare against renormalised g (:52); van Baal ε₁, read in full, 1.5·10⁻⁷ within rounding (:10, 28); LM abstract only (:30).
  - Ambroziński App. B (:13); z > 0.9 and z ≈ 2 (:17, 57–58); three NOT FOUNDs with weak search (:18–19, 101); "mass of the scalar glueball" caution (:14).
- **N§9:**
  - ε = arccosh(…) = 2 asinh(sin a) (i1-tunnel:11; arith child Q9); WKB relation (:12).
  - c = 4.6054132, d = 2.6828, E₀d = 8.99 (:13–14; arith P10).
  - Not proved: WKB, path (:12, 23); double-precision values reproduced (:17); m_eo at 96, 128, 192 (:18).
  - Local slopes 3.99/4.06/4.12/4.17 (:37–40); free fit 4.599/−7.8 (:49–50).
  - c = 4.7926 forced: residual 5–6× (:16; arith P13 for β ≥ 64, 96).
  - Child agreement (:110–111); brief's divergence remark wrong (:14).
- **N§10:**
  - 32 chains, four operators, plateau rule pre-registered (i1-mc3:22–25).
  - β = 4 differenced value and the floor defect (:15–16); β = 256 two-direction control, 1.8σ (:18; arith P9).
  - Child 1.620 (:14); all five table rows (:29–44); −0.7/−0.8/−1.6 % (:50; arith P8).
  - Approach from below; 1–2 % measurement, not proof (:70, 77).
- **Paper only:**
  - Setting V, K, projector (h1-a4:71–72); 27/30 and the slip; companion vacuum bound (:1).
  - Proof-sketch steps 1–4 (items 10, 12, 14, 17–23); log(λ₀/λ₁)β^{1/3} = 1.636 … 1.939 (h1-a4:164–169; arith P5).
  - 16–23 % and within 1.3 % (h1-a4:172; arith P6: 15.6 %, 23.1 %, 0.95 %, 1.27 %); approach from below.
  - Box derivation, A = 2(βL³)^{−1/3}Y (h2-ground:45–49; arith P15); e′ = 4^{−1/3}e and the 4^{1/3} normalisation (arith P16).
  - O(β^{−3/2}h^{−3}) = O(h^{3/2}) (arith P17); false start −2.39/−3.35, weight 2 (SCALING_LIMIT:175–181).

**Predicate counts (met, failed, measured only):**
- My arith.py: met 14, failed 4, measured only 0. The 4 failures are P11, P12, P14 and P18. All four are defects of the target text, not of my expectation; I expected them from reading and declared expect-exit 1 before the run.
- Child (T110), rerun by me: met 13, failed 1 (Q14, the same defect as #4), measured only 0.

## 3. Not checkable here (rest on sources outside records/)

1. The author's lineage "OpenAI Codex" (S:6, 45). h1-a4:4 says only "a different lineage".
2. "not read by a person" (S:7, 48, 84, 93; N§8).
3. The commits c5c1ea9, 4966c89, dd2927a and the repository folder (S:50–52; N§8:109).
4. The Remark on all center sectors: e^{−C√β} ≤ log(λ₀/λ_χ) ≤ e^{−c√β} (S:87–93; N§8:109; N§9:126).
5. "The proof does not give a numerical value for e₁−e₀" (S:53).
6. "four-point fit with one residual degree of freedom"; endpoint deletion 1.97503 and 1.97489, "A4's replay" (S:114, 134–135; N§7:91).
7. A4's audit at 1860ed3: "D₄ permits but does not force" the splitting, and the doublet is the lowest non-scalar branch (proved) while its position below the scalar rests on numerics (S:128–131; N§7:94). **Note:** the record g2-numchal:16 says the opposite ("as charge 2 under D₄ requires"). The correction rests entirely on the non-local audit.
8. "Director A4 posted … before the lower half here was complete" (N§8:109).
9. The director's own reruns: "Lean file … exit 0" and "scalar program (digest identical)" (N§8:113). The nine-lemma count itself MATCHES.
10. "It is the first lower bound on a gap at weak coupling in this program" (N§8:116).
11. "I first recorded it here with free constants c, C, in which form it is true and follows from A4's inequality (2)" (N§7:97).
12. The status of a builder and a challenger "running" (N§7:99).
13. "None of this has been read by anyone but its author" (N§7:99). This is a statement about the time of writing.
14. vB00 "read in full" and the page locators: these come from h2-ground's own reading. I did not reread vB00 (no network).
15. Lüscher 1983 and LM84 contents beyond what h2-ground quotes.
16. CHANGES_revision4.md's claims about main.tex and refs_add.tex, and the record `../reviews/i1-sec/`, which is not here.
17. "The exponential chart need not cover…" and other §1–6 material. These are outside my brief and not checked.
18. The convergence of the h₃ Rayleigh–Ritz values beyond what g2-three reports (upper bounds only, g2-three:143). The paper calls them "measured" and does not mention the one-sidedness, which is not wrong.
19. The claim that the second proof's sessions are "of the first lineage". The records say only "same model family as the director".

## 4. Hypotheses each statement uses, and where stated

- **One-site limit (S:38–43):**
  - k = 2, 3; center-even, gauge-invariant sector; h = β^{−1/3}; K normalised.
  - β large: escape, ε, m ≤ β.
  - DLMF Bessel facts.
  - Positivity improvement and form core.
  - Stated in h1-a4:70–88 and S:10–34.
- **Second proof:**
  - κ₀ = 1, center-even sector (SCALING_LIMIT §0).
  - Ruiz-Antolín–Segura Thm 2.
  - Reed–Simon XIII.47/67 and Rellich–Kondrachov, cited from memory (g2-conv:36–42; h1-liminf:28–40).
- **Box heuristic (S:150–172):**
  - constant links; small A;
  - T ≈ e^{−H} (not proved);
  - bare g = g(L) at leading order (h2-ground:77–81).
- **Tunnelling heuristic (N§9):**
  - Born–Oppenheimer; the path a₂ = 0;
  - Gaussian kernel to O(1/β);
  - E₀ from the two-direction continuum (i1-tunnel:73–74).
- **MC (N§10, S:141):**
  - GEVP level identification by channel;
  - odd-sector floor negligible for β ≥ 64 (empirical);
  - jackknife over independent chains (i1-mc3:110–121).
- **My arithmetic:** the record values copied by hand, as cited in arith.py.

## 5. Failed predicates (kept)

| predicate | value | whose failure |
|---|---|---|
| arith P11 | 9.90 % / 10.99 %, against "about 12" | defect of the target (#4) |
| arith P12 | 2.16, 3.62, 5.73 orders, against "up to five" | defect of the target (#5) |
| arith P14 | 1.64σ at β = 1024, against "zero within errors" | defect of the target (#15, #16) |
| arith P18 | 1.99998 at β = 256, against "2.00000" | defect of the target (#12) |
| child Q14 | as P11 | defect of the target |

The child's recompute.py exits 0 even though Q14 failed. It prints the failure but does not set the exit code. That is a weakness of the child's program, not of the target.

## 6. What I did not check

- No mathematics was rechecked; I compared summaries with records only. Nor did I re-check any record against its own programs (none are in records/).
- Notes §§1–6 and the rest of the paper.
- Whether the records themselves are right. Example: g2-numchal's "D₄ requires" against A4's audit.
- No network. The literature claims are taken from h2-ground as recorded.
- No Lean.

## 7. Delegated questions and outcomes

**Child T110** (label j1-micro-child, admitted under T108, released, graph event 224). Run as check K1 `child-run1`, exit 0, 78.5 s. Model: sonnet.
- **Question:** independent recomputation of 14 arithmetic claims (Q1–Q14: the 4^{1/3} conversions, 1.5e−7 against the rounding, e₁−e₀, the β^{1/3} products, the MC percentages, 1.8σ, the identity for ε, c, d, E₀d, the continuous-time c, and the "12 %").
- **Control:** Σ1/n² = 1.644934. I graded it first, before reading anything else: **correct**.
- **Outcome:** Q1–Q13 reproduced; Q14 NOT REPRODUCED (9.9 % and 11.0 %). I reread recompute.py and reran it in child_rerun/ as K3: results.json is identical. Each value agrees with my independent arith.py.

**Grandchild T112** (label j1-micro-grandchild, admitted by the child under T110 at graph event 221, released at event 222).
- **Question:** d by the substitution a = π sin²(t/2).
- **Control:** ∫₀^π sin = 2, passed.
- **Outcome:** 2.6827994012 at 100, 200 and 400 nodes, which matches my 2.6827994. I read its result.json; I did not rerun it myself. The child reports a rerun.

**Child process gap:** the child's report does not quote its register verify lines. Its register (child/pcp) has 3 events.

## 8. Registers

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Checks:
  - K1 child-run1 (exit 0);
  - K2 arith1 (exit 1, expected 1);
  - K3 child-rerun (exit 0).

## 9. Rerun commands (from /home/user/z4-workers/j1-micro; result files use mode "x", so move results/arith1.json and child_rerun/results.json away first)

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label j1-micro-child --parent T108          # gave T110
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T110
mkdir -p results && OMP_NUM_THREADS=1 $P check --ws pcp --name arith1 --expect-exit 1 -- python3 arith.py results/arith1.json
mkdir -p child_rerun && cp child/recompute.py child_rerun/ && $P check --ws pcp --name child-rerun --cwd child_rerun --expect-exit 0 -- python3 recompute.py
$P verify --ws pcp ; $R verify pcp/register.jsonl
```
