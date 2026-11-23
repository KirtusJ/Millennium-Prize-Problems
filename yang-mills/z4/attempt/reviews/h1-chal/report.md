# report.md — h1-chal (T87): challenge of SCALING_LIMIT.md

The director and I share a model family, so where I agree with the text that is not independent review.

## 1. Verdict table

| item | verdict | one line of evidence |
|---|---|---|
| §1 (C1–C3: compact resolvent, E_0 < E_1, core) | STANDS | Fibre bound recomputed by hand. a' = 2.3381074105 and E_0 ≥ 2.94583 (chal2 Q1). E_1 > E_0 strictly is *proved*, not assumed: the full-space ground state is simple, so it is invariant, so the second invariant level lies above it. This needs RS XIII.47, which I could not read. RS XIII.67 also not read. |
| U0 | STANDS | Q ≤ ⟨g,(1−K+W)g⟩/‖g‖², since ⟨g,(1+W)g⟩ ≥ ‖g‖² and the numerator is ≥ 0. −ln(1−μ) ≤ μ/(1−μ). |
| U1 | STANDS | RAS Thm 2 was read from source (arXiv HTML v1, verbatim by a sub-agent). After ν→ν+1 it is exactly the stated sandwich. Grid checks P1/P2: 18361/18361 met each. B3: 2807 met. Operator inequality P5: 71407 met. |
| U2 | STANDS | sin²a ≤ a² and sin²a ≥ a²(1−a²/3) recomputed. Lattice Dirichlet ≤ flat/(1−a_R²/3) on 4/4 trial cases (P14b). |
| U3 | STANDS | The closed form of V holds to 1.1e−15 on 1000 random pairs (P8). 2β\|A_1×A_2\|² = 2β^{−1/3}\|Y_1×Y_2\|² checked. |
| U4 | STANDS | Σ_z over {±1}² gives evenness under BOTH flips. ‖g‖² = 4‖f‖² and the same factor 4 appears in the numerator, so normalisation is fine. The kernel bound e^β/Z² is crude but true. The Z lower bound holds at 7 β values (P7). |
| U5 | STANDS (asymptotic only) | The direction is correct. For the R = 4 cut trial, β^{1/3}ν_trial = 3.688 and 3.629 at β = 1024 and 4096, against E_trial = 3.5717, with β^{1/3}·d = 1.17 and 0.92 (O(β^{−1/3})). At β = 64 and 256 the stated error form gives no usable bound: e^{R⁴β^{−1/3}/2} = e^{32}, e^{20}. Measured values there: 28.4 and 11.2. |
| L1 | STANDS | Two-sided where used. Lower side: ν_k ≥ ν^H_k/(1+ν^H_k), since (a+w)/(n+w) is increasing in w when a ≤ n, and a ≥ 0. Upper side for ν^H: U5 bounds ⟨1−K+W⟩/‖g‖², and W ≥ V. |
| L2 | STANDS | 1 − I_2/I_1 ≤ 2/β and E_k[d²] ≤ π²/β at 7 β values (P6). Derivation from RAS checked by hand. |
| L3 | **DEFECT** (sign; consequence survives) | False line: "⟨g,(1−K)g⟩ = Σ_α⟨χ_αg,(1−K)χ_αg⟩ **+** ½∫∫k₂ g g Σ(χ_α(U)−χ_α(W))²". The correct sign is **−**, as in standard IMS. Counterexample on a discretised ring (N = 240, β = 40): lhs = +0.070669, while the "+" term = −0.070669 (P10 failed, P11 met to 2e−14). The Schur bound controls \|term\| (P12: ratio 0.0026), so L5 and L7 are unaffected. |
| L4 | STANDS | Exact fibre operator in the Peter–Weyl/Hopf basis, sectors (p,q) ≤ 2: λ_min ≥ σ − 1/β in 48/48 claimed cases, β = 1e3…1e6, σ ≤ 0.002 (P13). λ_min/σ → 2. Arithmetic slip: from its own line, 5π²‖B‖/M² with ‖B‖ ≤ 2βσ² and M² = β/2 gives 20π²σ² ≈ 197σ², not 98.7σ². Only d ∈ {0, ±2} occurs, which gives 8π²σ² ≈ 79σ², so 98.7σ² is true but not derived. With 197σ² the margin at σ = 0.002 is only 0.02σ. Coverage: n is arbitrary and the fibre is all of L²(SU(2)), so the whole common-axis circle (all angles) is covered whenever s_i ≥ σ_R. |
| L5 | STANDS (minor gap) | The only hidden dependence is β_0(R) = (R/s_*)³ from σ_R ≤ s_*, which is harmless because β → ∞ before R → ∞. C′ depends only on θ. Unstated: (1−η²)^{1/2} must be Lipschitz. This holds by Glaeser's lemma for C² θ, or by choosing θ = sin(π/2·ψ). |

**Counts:** STANDS 11, DEFECT 1, NOT CHECKED 0.
**Predicates (mine): met 13, failed 3, measured only 4.**

## 2. Hypotheses used and where stated
- **C1:** V ≥ 0 polynomial; Friedrichs extension (§0); RS XIII.67 (V → ∞ ⇒ compact resolvent; cited, not read by them or me).
- **C2:** RS XIII.47 (V ∈ L²_loc bounded below ⇒ e^{−th} positivity improving), and a ground state existing by C1.
- **C3:** rotation averaging maps C_c^∞ to itself and contracts the form norm.
- **U1, L2, L4:** RAS Thm 2 (ν ≥ 0 lower, ν ≥ ½ upper before the shift) (§2 U1); "B4", the shifted upper bound (TORON_GAP S5).
- **U2:** support in a < π (fine for |Y| ≤ R and β > (2R/π)³).
- **U4:** the support of φ lies in |Y| ≤ R with Rβ^{−1/3} < π/2 (disjoint copies), and W is center-invariant.
- **L4:** β ≥ β_0 (not quantified), 0 < σ ≤ s_* = 0.002, and S7 (TORON_GAP, Lean F4).
- **L5:** σ_R ≤ s_*; θ smooth; L4 applied fibrewise.

## 3. Failed predicates (all kept)
- **P9 (chal.py run3):** Airy zero 2.33711 instead of 2.33811. Cause: my shooting loop overshot r = 0 by one step. **My defect.** Repaired in chal2 Q1 (met).
- **P10:** the L3 identity as written ("+") fails. **Defect of the target.**
- **chal2 Q2:** continued-fraction vs quadrature Bessel ratio differ by 1.05e−6 (tolerance 1e−8). The source was not resolved within budget. My earlier cross-check (0.996) was invalid because it used cancellation points; that was my defect. P1/P2 use the continued fraction, so their very small slacks (9e−13, 2.5e−9) carry this unresolved 1e−6 uncertainty. The bounds themselves were confirmed from the source text.
- **Register K3 (chal-run2):** killed by me because numpy used ~2 cores (rule 8). My defect; rerun as K4.

**Measured only:**
- P14(c): the explicit chain bound is infinite at all β for R = 4, so it is vacuous.
- P14 differences to E_trial and E_0: +25, +7.9, +0.34, +0.28 against E_0.
- L4 cap at β = 1e3, σ = 1: λ = 0.991 < σ − 1/β = 0.999. This is outside the claim and shows that the cap s_* is needed.
- The invalid 0.996 cross-check.

## 4. Not checked
- RS XIII.47 / XIII.67 and Simon 1983 could not be read: search was blocked, and the publisher returned 403.
- Abramowitz–Stegun was not read; the value was reproduced numerically instead.
- L4 sectors with \|p\|,\|q\| > 2.
- β_0 of L4 was not quantified; β < 1e3 was not tested.
- A non-product (better than Gaussian) trial against E_0.
- L6/L7: these are SKETCH by the document's own tags and were outside the brief.
- No Lean was used (READY exists).

## 5. Delegated questions
- **Child T93** (admitted under T87, run as register check K2, exit 0, 188 s, released at event 186).
  - Question: the lattice Rayleigh quotient for the product-Gaussian trial (no cutoff) at β = 64/256/1024.
  - Control: ∫x²e^{−x} = 2 and I_1(2)/I_0(2) = 0.697775. Both correct, and graded before anything else was read.
  - Outcome: ⟨g,Wg⟩ explodes (ln = 18.79, 224, 1301), Q = 1, and β^{1/3}ν = 121, 1512, 13280.
  - My rerun reproduced ‖g_1‖² = 0.0043220870387 and ln⟨g,Wg⟩ = 18.7931.
  - Grading: the failure belongs to MY trial choice (no compact support). It is not a defect of the target, since U4/U5 require C3's compactly supported φ. It does confirm that compact support is essential.
  - The child's "fixed R = 0.8 does not rescue" uses R in a-units, not the document's \|Y\| ≤ R, so it does not apply.
- **Grandchild T94** (admitted and released by the child).
  - Question: an independent recomputation of ‖g_1‖² and ⟨g_1,Kg_1⟩ at β = 64. The control was correct.
  - Outcome: agrees with the child to 1e−13. The child reran it.

## 6. Rerun commands (from /home/user/z4-workers/h1-chal; result files open with "x", so use a fresh name)
```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control 0.272341
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name chal-run3 --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONUNBUFFERED=1 taskset -c 0 python3 chal.py results/chal_run3.json
$P check --ws pcp --name chal2-run1 --expect-exit 0 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 taskset -c 0 python3 chal2.py results/chal2_run1.json
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

**Verify, last lines:**
- `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

**Citation read:** D. Ruiz-Antolín, J. Segura, "A new type of sharp bounds for ratios of modified Bessel functions", arXiv:1606.02008 (2016), Theorem 2. Read from https://arxiv.org/html/1606.02008v1 by a fetch sub-agent: theorems verbatim, §2.2–3 only summarised. No text was kept in this directory. The paper attributes b_0 and b_1 to Segura and to Laforgia–Natalini, not to Amos.
