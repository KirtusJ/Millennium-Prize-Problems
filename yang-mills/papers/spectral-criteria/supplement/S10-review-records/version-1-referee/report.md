# g2-fid report: referee and fidelity check of main.tex (worker under T244, Director Z4)

Control: `control.txt` = 0.272341 (−ln tanh 1). Lean was ready (`/home/user/z4-lean/READY` exists).
The director and I are the same model family, so my agreement is not independent review. Neither is the child's; it is a lower-tier Claude model.

Summary. The four proofs are correct as mathematics. Every scalar constant recomputes. **The problems are in the surrounding sentences**:
- Theorem t:ret was changed from the source's time vacuum to periodic time. The change is honest at main.tex:80–82. But main.tex:63, Remark r:ret(c), the solid arrow in Figure 1 and main.tex:221–222 still treat t:ret as if it supplied the second hypothesis of Theorem t:inh. It does not, because t:inh needs a semigroup S_s = e^{−sH}.
- Three numerical or descriptive sentences in Section 'Measurements' do not match their records.
- Remark r:haar's "three to four orders of magnitude" is wrong by about four orders.

## 1. Defects, gaps and fidelity errors first (each with the replacement text I propose)

**D1. OVERSTATED: main.tex:63, Introduction (what t:ret supplies).** Text: "Only the second is proved here, for a narrow exceptional set."
Why: the second hypothesis of t:inh is ‖BS_τB‖ ≤ κ for S_s = e^{−sH}, a semigroup on a slice space. Theorem t:ret is proved for a periodic lattice with T slices. Its two-slice kernel at lag n is not e^{−nH} of any vacuum semigroup on that space. main.tex:81–82 and :510 admit that the vacuum passage is not done. Source return.md:3,12 states the vacuum version and gives the passage by slab convergence; main.tex drops it.
Replacement: "None of the three is proved here. For a narrow exceptional set, Theorem~\ref{t:ret} proves the analogue of the second for the two-slice law of a lattice with periodic time; its passage to the vacuum transfer semigroup is not carried out."

**D2. DEFECT: Remark r:ret(c), main.tex:373–376 (lag condition and semigroup).** Text: "…bounds ‖BS_τB‖ for the two-slice operator of the periodic lattice at any lag of at least one time step."
Why, part 1: on a periodic lattice a lag of T, or any multiple of T, makes the two slices equal. The proof (main.tex:344, "because the two slices are distinct") then fails. return.md:12 says "requires the slices to be distinct modulo the period."
Why, part 2: that two-slice operator is not S_τ of Theorem t:inh. See D1.
Replacement: "…bounds $\|BK_nB\|$, where $K_n$ is the two-slice operator of the periodic lattice at lag $n$, for every $n\not\equiv0\pmod T$. $K_n$ is not a semigroup in $n$, so this is not yet the second hypothesis of Theorem~\ref{t:inh}."

**D3. OVERSTATED: Figure 1, main.tex:192, and main.tex:221–222 (Architecture).**
Why: the solid arrow `(ret) -- (inh)` asserts that a proved statement feeds t:inh. It feeds t:inh only after the open vacuum passage. Also, the sentence "If both held, together with Theorem t:ret and a summable choice of gates, Corollary c:acc would give a positive lower limit…" omits that passage.
Repair: make that arrow dashed. Replace the sentence with: "If both held, together with Theorem~\ref{t:ret} passed to the vacuum semigroup (not done here), a summable choice of gates, and $\sum_iM_{i-1}(\varepsilon_i+\kappa_i)<d_0$, Corollary~\ref{c:acc} would give a positive lower limit of the deficits in a fixed physical box." The same edit applies to Table 2, row t:ret ("proved for periodic time; not yet an input of Theorem t:inh").

**D4. WRONG: Remark r:haar, main.tex:417–418.** Text: "…and it is three to four orders of magnitude below the losses measured in Section s:evid."
My values: R'(6)/β² = 3.437e-3 at β = 3.276133577 (recompute.py M1). The measured local losses are J1 = 0.0077296(394) and J4 = 0.0029112(117) (records/e2-repair/report.md:59). The ratios are 2.25 and **0.85**: the same order, not 10³–10⁴. The "three to four orders" holds only for the derived floor on a mark's loss, J ≥ 1/(165888β²) = 5.616e-7 (records/e2-score/report.md:13). Against that floor the ratios are 5.2e3 and 1.4e4.
Replacement: "…It is a bound on a loss, not on the quotient of loss by variance. The floor it yields for the local loss of the marks of Section~\ref{s:local}, $\mathcal J\ge1/(165888\beta^2)$ (derived in~\cite{Repo}, not in this paper), is three to four orders of magnitude below the measured losses."

**F1. WRONG: Section 'Measurements', main.tex:430–431 (frozen background).** Text: "all equal to the identity except two, chosen so that one coarse plaquette has holonomy −I and a neighbouring one supplies a reference direction."
Record: one coarse y-link is set to W = −I and one coarse z-link to B = i. **Three** coarse plaquettes (xy000, xy200, yz204) have holonomy −I, and four have holonomy ±i (records/c2-grow/report.md:11–12; records/b2-matrix/report.md:33). The reference direction is B itself. The text's own observation (i), at main.tex:450–451, already speaks of "three coarse plaquettes".
Replacement: "all equal to the identity except two: one coarse link equal to $-I$, so that the three coarse plaquettes through it have holonomy $-I$, and one adjacent coarse link equal to $\mathbf i$, which supplies a reference direction (four coarse plaquettes then have holonomy $\pm\mathbf i$)."

**F2. WRONG (two different marks conflated): Table 1 caption, main.tex:446, against observation (iii), main.tex:455–456.**
- The caption's "single mark used first gives .047 and .09" is the four-face mark f4/r4: .0464(7) on the −I background (b2-matrix:33) and .0864 on chain.skel0 (b2-matrix:35).
- Observation (iii)'s "the quotient of the first single mark … ratio 1.004(11)" is Q1, the **one-face** mark r1 ≈ .062 (e2-repair:59,63).
- For the .047 mark the ratio at 2/β is Q4 = **1.034(13)**, which is 2.6σ above 1. The record also warns that Q4 should not be quoted to better than about 2 per cent (e2-repair:63–67).
- "up to 2/β": only δ = 0 and δ = 2/β were measured for the single mark (e2-repair:57–60). δ = 1/β was measured only for optima over different lists (b2-matrix:37).
Replacement for (iii): "(iii) Displacing the frozen holonomy from $-I$ by round distance $2/\beta$ leaves the quotient of the one-face mark ($\approx.062$) unchanged within the errors (ratio $1.004(11)$ in a repeated run); for the four-face mark of the caption the ratio is $1.034(13)$. So the low quotient is not confined to the narrow gates that Theorem~\ref{t:ret} controls."

**F3. WRONG / OVERSTATED: Section 'Comparison across a factor of two', item 1, main.tex:478–481.** Text: "fails for a frozen test unless c ≤ 0.005: the stationary variance of the same function of coarse links is 0.0034 times smaller on the finer lattice."
Record (records/e2-cross/report.md:11,18):
- E_f/E_c = 0.00407 ± 0.00005, so the comparison is defeated for every c ≥ 0.0042, not merely for c > 0.005.
- Var_f/Var_c = 0.0034 holds for that one test. It is a test from the 16-function slice-averaged span, not from the 54-function span introduced at main.tex:474. "0.0034 times smaller" inverts the ratio; the variance is about 294 times smaller.
- For the 54-span test of item 2, Var_f/Var_c = 1.18 (f2-cross2:17). So the variance ratio is not a property of "the same function of coarse links" in general.
Replacement: "An unnormalised comparison of two-time energies, $\mathcal E_{10}(f)\ge c\,\mathcal E_5(f)$, fails for every $c\ge0.0042$: one frozen test from an earlier span of $16$ slice-averaged functions has $\mathcal E_{10}/\mathcal E_5=0.00407(5)$, because its stationary variance on the finer lattice is $0.0034$ times that on the coarser. Any comparison of the kind in Hypothesis~\ref{h:coarse} must be normalised by the variance."

**F4. OVERSTATED: item 2, main.tex:487–488.** Text: "…and that a loss ε_i of several per cent of R per halving of the mesh has to be expected at this scale."
The record covers one test and one matched pair, at finite periodic time, with the coupling-match uncertainty inherited. The record says explicitly that it is "not a spectral bound" (f2-cross2:28). ε_i in Hypothesis h:coarse is a loss between deficits, not between values of R for one test.
Replacement: "…it shows that the comparison is not an identity; for this one test the quotient $\mathsf R$ drops by about six per cent under one halving of the mesh. This does not measure $\varepsilon_i$."

**F5. OVERSTATED (minor): Section 'Persistence in time', main.tex:465.** Text: "at two steps nothing is [resolved]."
Record: at t = 2 the transported form gives ρ = .0162(55), which is 2.9 se (d2-time:41). The record's wording "it is gone by t = 2" (d2-time:15) is itself generous.
Replacement: "at two steps it is $0.016(6)$, a fifth of its one-step value." Also at main.tex:460, "In the same ensemble" should read "In the same setting (fresh streams)". d2-time used fresh seeds (d2-time:34).

**F6. OVERSTATED: Introduction, 'Sources…', main.tex:116–117.** Text: "Sessions of Claude … attacked Theorems t:inh and t:ret and Proposition p:haar … and found no defect."
The attacks (y1-g4ret, b2-haar, f2-lean) were on the **source** statements:
- return.md, which states the time-vacuum version, has operator-norm form and has no T ≥ 2 clause;
- inheritance.md, where B = RQ.
They were not on Theorem t:ret as stated here: periodic time, T ≥ 2, distinct slices, exchange by reflection of the periodic time axis.
Replacement: "…attacked the source derivations of Theorems~\ref{t:inh} and~\ref{t:ret} (in the time-vacuum form of~\cite{Repo}) and Proposition~\ref{p:haar} and found no defect; the periodic-time statement of Theorem~\ref{t:ret} given here was checked only in a later referee pass by a session of the same family."

**F7. UNSUPPORTED here: main.tex:113–115, 118–119 (attributions).**
- "Theorem t:crit … and the monotonicity statements of p:haar were proposed … by OpenAI GPT models": no record here shows it. b2-haar mentions only unnamed "auditors".
- "Theorems t:inh and t:ret were proposed with proofs by a session of OpenAI Codex": return.md and inheritance.md carry no author line. The brief says only "another lineage".
- "parts of which a session of OpenAI Codex reduced again … and corrected": e2-repair:11 credits "G4", whose lineage is not named in any record here.
No change is needed if the repository supports these claims. I could not confirm them from records/.

**F8. OVERSTATED (minor): Section 'Machine-checked parts', main.tex:497 ("Corollary c:acc").**
Lean (`accum`, `accum_mul`, `accum_pos`) proves the inequality. It does not prove the second sentence of the corollary, that M_n stays bounded iff Σa_i/γ_i < ∞.
Replacement: "…Corollary~\ref{c:acc} (its inequality; not the boundedness criterion)…". Also, haar.lean does not take "the three differential relations as hypotheses". It is pure algebra in real variables with the derivative formulas written in as expressions.
Replacement for main.tex:500–501: "the algebra at the zeros in the proof of Proposition~\ref{p:haar}, with the derivative formulas entered as algebraic expressions in real variables, …".

**F9. OVERSTATED: Table 2, main.tex:527.** Text: "Table local gives upper bounds for the best possible rate on two backgrounds."
J/V is the local 24-colour quotient on a frozen coarse background. γ in Hypothesis h:mix is a form inequality for the physical transfer I − S_{2a} on the whole centred space. The local quotient bounds the constant of the *sufficient* local inequality of inheritance.md:8, not γ.
Replacement: "open; Table~\ref{tab:local} gives upper bounds, on two frozen backgrounds, for the constant of a local inequality that would suffice for it."

**G1. GAP (statement completeness): Theorem t:ret, main.tex:70.** "for every square-integrable function g of a slice": the proof uses g(x)² as |g|², so g must be real.
Replacement: "for every real square-integrable function $g$ of a slice". The hypothesis N ≥ 6 is unused in the proof; any even N ≥ 2 works. It is harmless and kept from return.md:3.

**G2. GAP: Remark r:ret(a), main.tex:369.** c must satisfy θ ≤ π, because p_k is defined only for θ ≤ π. return.md:20 says this.
Add: "with $c>0$ such that $\theta\le\pi$".

**G3. GAP (quantifier): Corollary c:acc, main.tex:312.** The statement is for a finite n, then speaks of "M_n stays bounded".
Replacement: "For an infinite sequence with $a_i,\gamma_i>0$ and $t>0$ fixed, and $K_i=1+2a_i/(\gamma_it)$, $\sup_nM_n<\infty$ if and only if $\sum_ia_i/\gamma_i<\infty$."

## 2. Verdict table

### (A) Referee
| item | verdict | evidence |
|---|---|---|
| Thm t:crit statement and proof | STANDS | Line by line: the spectral measure is positive; (1)⇒(2) gives d ≤ r^n‖v‖²; (2)⇒(1) uses [α,ω] ⊂ (0,Δ), and a bounded projection that vanishes on a set with dense span is zero. Remarks (a)–(c) are correct as stated. |
| Lemma l:scal | STANDS | 1−x^ρ ≤ −ρ log x and −x log x ≤ 1−x; x = 0 and ρ = 0 are covered. Lean `xr_le` reran with exit 0. |
| Thm t:inh | STANDS | Every step justified: S_s ≥ e^{−sL}E; ‖EB‖² = ‖BEB‖ ≤ e^{τL}κ; ‖Pv‖² ≤ e^{tL}(1−b); the split ‖Qv‖² = ‖Gv‖² + ‖Bv‖² because ran B ⊂ ran Q. The scalar step is correct. It generalises inheritance.md (any B ≤ Q instead of B = RQ); the generalisation is justified by the proof. Finite-dimensional version in Lean (`gated_main`, reran). |
| Cor c:acc | STANDS (inequality); GAP G3 (quantifier) | The telescoping is correct and needs only K_i > 0. main.tex drops the source's (·)_+; this is valid and weaker. |
| Lemma l:cap | STANDS | Layer-cake rearrangement over concentric superlevel caps; polar measure (2/π)sin²r dr; d/dk = Cov of two non-increasing functions of r ≥ 0. |
| Thm t:ret, conditional bound | STANDS | k = β‖Σ‖ ≤ 6β; dist(XUY, −I) = dist(U, −X⁻¹Y⁻¹); tower property. With T = 2 both temporal staples go to slice x and the count is still 6. |
| Thm t:ret, exchange step | STANDS | Reflection t ↦ s₁+s₂−t (mod T) preserves Haar measure and ½Tr U_p (SU(2) traces are real) and swaps the two slices. No translation is needed. Changed relative to the source (vacuum reversibility → periodic reflection); the change is justified for periodic time. |
| Thm t:ret, hypotheses changed vs return.md | Justified, but downstream OVERSTATED (D1–D3) | Time vacuum → periodic time with T ≥ 2: the proof covers it, and the vacuum passage is dropped openly (main.tex:81). Operator norm ‖RS_τR‖ → bilinear row form: equivalent for a self-adjoint kernel. Distinct-mod-period: in the theorem as "distinct slices", missing in Rem. (c) (D2). |
| Thm t:ret, envelope C = π²√e/4 and derivation | STANDS | Ratio of the two bounds = C(1+k)^{3/2}θ³ exactly (Q1). Grid of 1647 cases, all qualifying, 0 violations (Q2). |
| Rem r:ret(a): 3π²√e/32 c³/N | STANDS (GAP G2) | Q4: relative deviation 2e-15; value 1.525521254. |
| Rem r:ret(b): 0.00307, 0.156, 0.935 | STANDS | p_{6β}(θ) = 0.003072388, 0.156180437, 0.934803630 (Q3; child identical; return.md:18 identical). These are exact p_{6β}, not the cubic envelope; the envelope gives 0.050, 3.2 and 87. |
| Prop p:haar: Z, mean, covariance, Riccati p = 1−3R/k−R² | STANDS | DLMF 10.29.2 recurrences checked; ODE versus termwise series derivative at k = 0.5, 2, 6: relative deviation 7e-59 (Q6). |
| p', q', w' formulas; identities at a zero (−2Rq; p'' = −2p²+6(p−q)/k²; w'' = p(4−2w), w < 3/2) | STANDS | 200 + 50 exact rational random checks (Q6); Lean `a_at_zero`, `b_at_zero`, `c_*` reran. |
| Series orders −k²/48, −k/16, k/2 | STANDS | Exact Fraction series (Q5): R = k/4 − k³/96 + k⁵/1536; next terms +k⁴/384, +5k³/384, −k³/8. Child identical. |
| First-zero argument and the three monotonicities | STANDS | The zero set is closed and bounded away from 0, so it has a least element. The sign arguments are correct; p > 0 holds because p is a variance. Lean `first_zero` reran. |
| Reduction β²m(k) ≥ R'(L) | STANDS | Uses p < q, p decreasing, k²p increasing, β ≥ 1. Lean `d_reduction` reran. |
| R'(6) enclosure (33 terms, rational) | STANDS | [0.036885895497642221 ± 1e-45] (Q7); child and grandchild agree to 15 digits by different methods. |
| Rem r:haar "three to four orders" | DEFECT (D4) | R'(6)/β² = 3.4e-3 against J4 = 2.9e-3. |
| Intro/architecture claims about t:ret as input of t:inh | OVERSTATED (D1, D3) | See above. |

### (B) Fidelity
| sentence | verdict | record |
|---|---|---|
| Table 1, all eight quotients and the mark counts 15/49/181/308 | MATCHES | c2-grow:53–58 (.02083, …, .01543(40); .05894(76), .05333(53), .05095(40), .04283(44)) |
| 16 training and 16 held-out streams; β = 3.276133577; N = 6, T = 12 | MATCHES | c2-grow:6,8 |
| clear background "every coarse plaquette at distance > 1.1" | MATCHES | min angle 1.142692 (b2-matrix:35, c2-grow:7) |
| frozen background "one coarse plaquette −I" | WRONG (F1) | c2-grow:11–12 |
| caption .047 / .09 versus (iii) ratio 1.004(11), "up to 2/β" | WRONG (F2) | e2-repair:59,63; b2-matrix:33,35 |
| (i) 81 per cent on three plaquettes | MATCHES | c2-grow:38 (.32 + .25 + .25 = .81); "opposite signs on neighbouring plaquettes" is supported only for the 11-mark optimum (b2-matrix:41) |
| (ii) decreasing more slowly / still decreasing | MATCHES | c2-grow:37,40,76 |
| time: R² −0.013(2), −0.002(2); bias ≈ 0.017; 15-mark 0.011(2); ρ 0.083(6) against 0.032(5); 1.5 per cent | MATCHES | d2-time:6–14,38–39,52 |
| time: "at two steps nothing is"; "same ensemble" | OVERSTATED (F5) | d2-time:41 |
| cross setup (N, β, T = 2N/4N, lag 1/2 steps, 54 functions) | MATCHES | f2-cross2:3–8; e2-cross:9 |
| cross item 1 (c ≤ 0.005; "0.0034 times smaller"; which span) | WRONG (F3) | e2-cross:11,18 |
| cross item 2: 0.941(5), 0.936(3), α > 0.95 excluded | MATCHES | f2-cross2:17 (bounds 0.9507 and 0.9412) |
| cross item 2: "ε_i of several per cent has to be expected" | OVERSTATED (F4) | f2-cross2:28 |
| cross item 3: span of 16 showed no such test | MATCHES | e2-cross:13; f2-cross2:19 |
| Lean: both compile, no sorry, three axioms | MATCHES (rerun) | K2: exit 0; 30/30 `#print axioms` lines show [propext, Classical.choice, Quot.sound]; one unused-variable warning in haar.lean:29 |
| Lean: Inheritance.lean contents | MATCHES except F8 | `xr_le`, `scalar_step(_pos)`, `accum*`, `gated_main(_norm)` (finite dimension, orthonormal eigenbasis, λ ≥ 0) |
| Lean: haar.lean contents | MATCHES except wording F8 | `a_at_zero`, `b_at_zero`, `c_*`, `d_reduction`, `first_zero`; it also contains an unmentioned alternative proof B (`s_root`, `riccati_gives`) |
| "Theorems crit and ret not formalised"; "nothing else is" | MATCHES | Lean files read |
| Intro "found no defect" | OVERSTATED (F6) | y1-g4ret:1; b2-haar:1 |
| Intro GPT/Codex attributions | UNSUPPORTED here (F7) | no record |
| "What is not claimed" items 1, 3, 4, 5 | MATCHES | consistent with the proofs; item 5 is accurate in substance |
| "What is not claimed" item 2 (assessors' statement about [OAI]) | NOT CHECKED | no network; the cited source was not available |
| "proof of t:crit … has not been attacked"; "no person other than the author" | NOT CHECKED (unverifiable here) | — |
| Table 2, row Hyp. mix | OVERSTATED (F9) | inheritance.md:8 |
| Any sentence claiming mass-gap progress | none found | Abstract, :23, :95, :172–173, :223–225 and :514–515 are explicit. The nearest risk is D1/D3: they make the proved part look like one hypothesis of t:inh, which it is not yet. |

**Verdict counts.**
- (A): 18 items. 15 STANDS, 1 DEFECT (D4), 1 STANDS with a GAP (c:acc; plus G1 and G2 noted under t:ret), 1 justified change with downstream OVERSTATED (D1–D3).
- (B): 22 rows. 13 MATCHES (2 of them with a caveat), 3 WRONG (F1–F3), 4 OVERSTATED (F4, F5, F6, F9), 1 UNSUPPORTED (F7), 1 NOT CHECKED (+1 unverifiable).
- Overall finding list: 4 DEFECT/OVERSTATED in the theorem framing (D1–D4), 9 fidelity items (F1–F9), 3 GAPs (G1–G3).

## 3. Hypotheses each statement uses, and where they are stated
- **t:crit:** H ≥ 0 self-adjoint; τ > 0; D with dense span; 0 < r < 1; integer n ≥ 0 (main.tex:28–33).
- **l:scal:** 0 ≤ x ≤ 1; ρ ≥ 0 (:274).
- **t:inh:**
  - H ≥ 0; P an orthogonal projection; B an orthogonal projection with ran B ⊂ ran Q;
  - a, t, γ > 0; 0 < τ ≤ t; κ ≥ 0; b real;
  - the three inequalities e:hyp (:44–50).
  - The source additionally has B = RQ with R a coarse event (inheritance.md:3).
- **c:acc:** K_i > 0; d_i ≥ (b_i−κ_i)/K_i; b_i ≥ d_{i−1} − ε_i (:307–308). The boundedness clause needs an infinite sequence and a_i, γ_i > 0 (unstated; G3).
- **l:cap:** k ≥ 0; v a unit vector; 0 ≤ θ ≤ π (:327–328).
- **t:ret:**
  - SU(2); Wilson action ½Tr with β ≥ 0; periodic lattice; even N ≥ 6 (unused); T ≥ 2;
  - x, y distinct slices; g square-integrable (real is needed; G1).
  - Source: time vacuum, any positive integer lag (return.md:3).
- **p:haar:** k > 0; for the last claim L > 0, β ≥ 1, 0 < k ≤ Lβ (:85–90).

## 4. Failed predicates
- **K3**, my recompute.py run1: exit 1, a KeyError on `wp[0]` in the Q5 test. This was **my own defect**, not a defect of the target. results_run1.txt is kept and partial. I fixed it with `.get` and reran as K4 (run2): 7 met, 0 failed.
- No predicate failed against the target.
- The child reports one expected non-pass: its control.py rerun exits 1 because mode "x" refuses to overwrite control.txt. This is a property of the rule, not of the target.

Own predicate counts: **met 7 (Q1–Q7), failed 1 (K3, own bug, superseded by K4), measured only 2 (M1, M2)**.

## 5. What I did not check
- The assessors' description of [OAI]/[YMG] (no network).
- The raw data behind any record. I compared main.tex against the reports only and did not reduce data.
- Whether the repository supports the lineage attributions (F7).
- The time-reflection invariance of the Wilson measure beyond the argument written in the D/table rows above (no numerical test).
- p_k envelope beyond the grid k ≤ 400 numerically. The proof covers all k, and I checked it by hand.
- Whether the 54-function test of item 2 is gauge invariant. I relied on f2-cross2:21.

## 6. Delegated questions and outcomes
- **Child T245** (`g2-fid-child`, parent T244). Admitted at event 490, released at event 493. Run recorded as K1 (exit 0, 98 s).
  - Question: independent numerical recomputation of S1–S5. These are the envelope C and its derivation, the three p-values, 3π²√e/32, the series orders and the Riccati identity, and the R'(6) rational enclosure.
  - Control: I_1(1) to 9 decimals. I graded it first: **0.565159104, correct.**
  - Returned: S1–S5 PASS, with values identical to mine (C = 4.068056677; 0.003072388 / 0.156180437 / 0.934803630; exact series coefficients; R'(6) = 0.0368858954976422…).
  - I reread s1_s2_s3.py and s4_s5.py (predicates in their docstrings; the tail ratio 9/(34·35) is valid for j ≥ 33). I reran both as K5 and K6: output identical to the child's run1 files.
  - Deviation: mpmath is not installed, so it used decimal at 60 digits instead. Its S1 grid stopped at k ≤ 200.
- **Grandchild T246** (`g2-fid-grandchild`, parent T245). Admitted and released by the child (event 492).
  - Question: R'(6) by an independent method (continued fraction plus Richardson differentiation). Control I_1(1): OK.
  - Result: 0.036885895497642, agreeing with the series value to 15 digits.
  - The child reports rerunning it. I did not rerun the grandchild myself; its number agrees with my own exact enclosure.

## 7. PCP record
- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Checks: K1 child-run1, K2 lean-both, K3 recompute (failed, own bug), K4 recompute-fix, K5/K6 child reruns.

## 8. Exact commands to rerun
```
cd /home/user/z4-workers/g2-fid
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"          # control
$P check --ws pcp --name recompute-new --expect-exit 0 -- python3 recompute.py <newtag>   # writes results_<newtag>.txt (mode x)
$P check --ws pcp --name lean-new --expect-exit 0 -- bash lean/run_lean.sh
#   (runs: cd /home/user/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/g2-fid/lean/Inheritance.lean ; same for lean/haar.lean)
$P check --ws pcp --name child-rerun-s123-new --cwd child --expect-exit 0 -- python3 s1_s2_s3.py <newtag>
$P check --ws pcp --name child-rerun-s45-new  --cwd child --expect-exit 0 -- python3 s4_s5.py <newtag>
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
# child session itself (as run):
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label g2-fid-child --parent T244
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T245
```
