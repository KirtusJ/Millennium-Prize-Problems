Overall verdict: **yes after listed repairs** — every mathematical step of tun_upper.tex (Sections 1–4) holds as written and Theorem tu:U-main (liminf ≥ c*) follows from the page plus Lemma tu:L-L4. The repairs needed are to the status paragraph of Section 1 (it states more than the note establishes) and to two measured remarks. None of them touches the proof.

Referee: v1-chU (task T179), worker of Director Z4. Same model family as the authors, so this is **not independent review**. Control: `control.txt` = 0.272341.

## 1. Verdict table (in the order of the note)

| # | Item | Verdict | Evidence (one line) |
|---|---|---|---|
| 1 | §1.1 Setting: T ≥ 0 compact, λ=‖T‖ simple with positive g, g flip/gauge invariant, λ_eo<λ | STANDS | Correct. The simplicity/positivity step is Jentzsch's theorem, which is used without being named (nit: cite it). Invariance of g follows from simplicity plus positivity. |
| 2 | §1.1 parenthesis (l.50–53): λ_eo may be taken over all σ1-odd/σ2-even functions | STANDS | The trial function ςg is gauge invariant. L4's lower bound carries over to the larger sector. Prop. B uses no gauge invariance. |
| 3 | §1.2: "this half uses one result of the second half, L4, lower bounds only" | STANDS | Checked against every proof in §§2–4. The only cross-reference used in a proof is tu:L-L4, and it is used within its hypotheses (see §3). |
| 4 | §1.3 status paragraph, item 1 | **DEFECT** | l.84 says the theorem "is proved in writing in this note" with no qualifier. The second half's own status (tun_lower.tex l.1055–1057) says "Proved in writing, **conditional on** … the gap bounds of Lemma tu:L-gauss and the Δh bound of Lemma tu:L-taylor as stated". Lemma tu:L-taylor's status (l.612) says a challenger checked "all items … except the gap bounds, not checked". **Repair:** state in §1.3 that the limsup half is proved conditional on those items, as its own status says, or remove that qualifier there once they are proved. |
| 5 | §1.3 items 2–5 (rate, thresholds, numerics, Lean) | STANDS (minor imprecision) | Correct: 0.15% (measured 0.139%), β≈10^13–10^14 (2.03·10^13), L4 ≈0.75 at 10^16 (recomputed 0.752). Imprecise: "8.6 to 14 nats at β≤4096" does not say which τ, δ were used. With τ=δ=β^{-1/3} the child measured 7.33–14.23 over β∈[100,4096]. See #22. |
| 6 | Lemma tu:U-kernel (1)–(3) | STANDS | Every identity rederived by hand. Quaternion MC (seed 20261123, N=2·10^6, β=3): Z and I_{n+1}/I_1 for n=0..4 agree within 4 SE. Uses "I_n decreasing in n" without proof, but the Remark gives an alternative route. |
| 7 | Haar coordinates (2.1), (2.2) | STANDS | Rederived. MC: P(r≤0.3)=0.30016; P(θ≤1)=0.17345 against exact 0.17359. |
| 8 | Lemma tu:U-K (both bounds) | STANDS | Each step rederived. 1-D quadrature on the actual kernel: first bound 180 met, 0 failed (12 cases have β'≤0 and do not qualify), worst log(lhs/rhs) = −0.0139. Radial bound 36 met, 0 failed, worst ratio 0.982. |
| 9 | Remark tu:U-K-rem (ω(β), C_L) | STANDS | The ω formula is rederived (monotone in \|p\|≤P and H≤H0). It is asymptotic only. With H=8.49 (η=τ=0.5): ω = 2820, 5417, 32070 nats at β = 4096, 16384, 10^6, and 0.0062 at 10^8. |
| 10 | Lemma tu:U-R (1)–(4) | STANDS | (1), (2) rederived. Quaternion check: conjugating to s·e3 gives V = 2βs²r (error 3e-15), and V is gauge invariant. (4): the Legendre matrix and a Nyström discretisation from Lemma tu:U-Frad agree to ≤2.5e-10 in 18/18 cases. |
| 11 | Remark tu:U-R-rem (measured c(a)) | **DEFECT (minor, remark only, unused)** | Claim: "the same at β=64, 256, 1024 to within 2%". Measured at β=64: 1.038 at a=0.05 (claim 0.98) and 0.980 at a=0.1 (claim 0.95). β=256 and 1024 agree. **Repair:** restrict the claim to β ≥ 256. |
| 12 | Lemma tu:U-F | STANDS | Follows from Cor. tu:U-F-cor with the split s≤η/2 / s≥η/2, both cases checked. P2: ε_eff ≥ 0 in 18/18 cases. |
| 13 | Lemma tu:U-Frad | STANDS | Rederived. Confirmed numerically through #10 (two methods agree). |
| 14 | Lemma tu:U-barta | STANDS | Rederived (Cauchy–Schwarz, Tonelli, symmetry). P5a: sup B ≥ ‖F‖ in 4/4 cases. |
| 15 | Lemma tu:U-fixed | STANDS | Algebra rederived. Child item 11 checks it to 3e-16. |
| 16 | Lemma tu:U-bessel | STANDS | Rederived. Child item 6: 30000 cases, 0 violations. |
| 17 | Lemma tu:U-I1 | STANDS | Rederived (√2 < π/2 makes the tail sign argument correct). Child items 3 and 5: D(1)=0.0389315, D increasing. Grandchild confirms the z→0 and large-z ends. |
| 18 | Lemma tu:U-amgm | STANDS | Trivial. |
| 19 | Lemma tu:U-outer | STANDS | Rederived (γ_r(1)=0, γ_r'(1)=γ, γ''≤8). Child item 7: 11110 cases, 0 violations. My Lean check of the Taylor step passes; the note's own Lean claim excludes that step. |
| 20 | Theorem tu:U-F-master | STANDS | Interior and outer cases rederived line by line. On the actual operator, ε_eff ≥ 2asinh s − deficit in 12/12 qualifying cases (β=256, 1024). The 6 cases at β=64 do not qualify (τ<1/5 needs β>125). Nit: H̃_δ(0) is undefined at r'=1, a null set. |
| 21 | Remark tu:U-F-unif | STANDS | A(1)=5.8284<5.83 and A≥1+2s (child item 9). |
| 22 | Corollary tu:U-F-cor (a), (b) | STANDS | Rederived. The uniformity in s∈[η/2,1] holds because the bounds are s-free apart from A≥1+η. |
| 23 | Remark tu:U-F-num (measured) | **DEFECT (minor, remark only)** | τ and δ are not stated. With τ=δ=β^{-1/3}, 24.9 and 5e-4 are reproduced exactly. The crossing below 0.2 is at 2.03e13, not ≈2.2e13. The β≤4096 range is 7.33–14.23, not 8.6–14. The Barta-ratio claim is reproduced (−4.06e-4 … −1.95e-4). **Repair:** state τ and δ, and correct the two numbers. |
| 24 | Factorisation (4.1) | STANDS | Uses the commutation from Lemma tu:U-kernel(3). The B' version uses the symmetry of V. |
| 25 | (W1)–(W4) | STANDS | Definitions consistent. Concave kink at π/2 because ε(π/2)=1.763 > 3η/2 for η≤1/2. |
| 26 | Lemma tu:U-W13 (patched) | STANDS | Every claim rederived, including the C² gluing at π/2 (f̃'=f̃''=0 there). Numerically, 9 (η,τ) pairs: W1–W4 all met. max\|g'\|·√(2η)/3 = 0.665 and \|f̃''\|/bound ≤ 0.900, matching the note's measurements. |
| 27 | Lemma tu:U-weight (1)–(4) (patched) | STANDS | Rederived. W5 (c* − c^ρ ≤ π√(6η)), W6 and W7 are met in 9/9 cases. Nit: in (1) at a=π/2, abstract (W3) gives only \|f̃'\|≤L; continuity of f̃' (or f̃'(π/2)=0 from W13) closes it. |
| 28 | Remark tu:U-weight-rem | STANDS | Correct: c^ρ ≤ c*_η, so the working-file version with c*_η does not follow. |
| 29 | Lemma tu:U-schur (patched Taylor step) | STANDS | Symmetrisation and Taylor reduction rederived. Hess(Φ∘a) on S³ has eigenvalues Φ'' and Φ'cot a. On the actual kernel by 2-D quadrature, log w ≤ Φ'²/2 + ω holds in 480/480 cases (β=4096…10^8). The measured excess log w − Φ'²/2 is 0.0127, 0.0033, 5e-5 and ≈0. |
| 30 | Lemma tu:U-A | STANDS | Rederived. It uses real u only, and m=w is bounded and measurable. |
| 31 | Proposition tu:U-B (patched) | STANDS | Exponent bookkeeping rederived; Lean (`propB_step`, `propB_stepI`) passes. (2) is "the same proof with the links exchanged": a genuine symmetry (V symmetric, K1 and K2 commute). It is not used in tu:U-main. |
| 32 | Lemma tu:U-flux (patched factor 4) | STANDS | 1−ςς = ½(ς−ς)², and the two orderings contribute equally, so the factor is 4. |
| 33 | Theorem tu:U-main | STANDS | Constants and quantifiers chain correctly: (η,δ,τ,Φ) fixed → β ≥ max(β1, β2, β_L) → Δ ≤ 4C(η)C_L e^{−√β(1−δ)(c^ρ−2Lτ)} → m_eo ≤ e^{η/4}Δ ≤ 2Δ (Lean: e^{1/8} ≤ 2) → liminf ≥ (1−δ)(c* − π√(6η) − 2Lτ) → let the parameters go to 0. The 1-Lipschitz class angle and Lemma tu:U-weight(4) are used within their hypotheses (a_y=π/2 is a null set). |
| 34 | Remark tu:U-uses | STANDS (nit) | Complete, except that Lemmas tu:U-schur and tu:U-A enter only through Prop. B and are not listed by name. |

**Statement verdicts:** 31 STANDS, 3 DEFECT (#4 status paragraph; #11 and #23 measured remarks), 0 GAP, 0 NOT CHECKED.

**Predicates (met, failed, measured only):**
- Mine: **872, 5, 7**.
  - The 5 failures are 2 defects of the target (#11, P4 at β=64, a=0.05 and a=0.1) and 3 defects of my own program: prog1 run1 P5 returned NaN at s=0.3, 0.6, 1.0 from exp overflow. That was fixed in prog1b, which met all 4 cases.
  - Two runs exited 1 on my own overflow bugs (prog2 run1, prog2b run1), before their K/Schur predicates were evaluated. They are kept in the register and res files.
  - Measured only: ω at 4 values of β, and the Barta interior/outer split at β=4096 (measured but not set as a predicate).
- Child: 11, 0, 1.
- Lean: `referee_scalar.lean`, 4 theorems, exit 0, axioms propext / Classical.choice / Quot.sound only.

Tolerance sources:
- P1: both methods converge exponentially, and a resolution doubling changes the result by at most 1e-8.
- P4: the note's own "2%", plus half a unit of the 2-digit value.
- P5: half a unit of the claim's last digit.
- MC: 4 standard errors.
- Quadrature: doubling change at most 1e-8.
- Scalar inequalities: 1e-14 to 1e-16 for rounding.

## 2. Hypotheses each statement uses, and where they are stated

- **Setting (l.9–53):** β>1; X=SU(2)² with Haar measure; V, K, T. Jentzsch/Perron–Frobenius is used without being named.
- **tu:U-kernel:** β>0.
- **tu:U-K:** β>1, p∈R³, H≥0, 0<η≤1, β'>0 (l.186–187).
- **tu:U-K-rem:** η=β^{-1/8}, \|p\|≤P, H≤H0 (l.238–246).
- **tu:U-R:** β>0. In (2), m is bounded, measurable and ≥0 (l.280). In (4), s>0.
- **tu:U-F:** η>0, β≥β0(η), a∈[0,π].
- **tu:U-Frad:** ψ=ψ(r)≥0 measurable.
- **tu:U-barta:** G bounded self-adjoint with a symmetric kernel ≥0; 0<inf ψ≤sup ψ<∞; Gψ≤Λψ.
- **tu:U-fixed:** s∈(0,1] (from §3 l.347).
- **tu:U-bessel:** 0<δ≤1, z>0.
- **tu:U-I1:** z>0; β>1 for D>0.
- **tu:U-amgm:** x, y∈[0,1].
- **tu:U-outer:** r∈[0,1], c≥0.
- **tu:U-F-master:** β>1, s∈(0,1], 0<τ<1/5, 0<δ≤1.
- **tu:U-F-cor:** (a) β>0. (b) τ=δ=β^{-1/3}, β>125.
- **(W1)–(W4):** η∈(0,½], δ, τ∈(0,1) (l.571).
- **tu:U-W13:** the same parameters.
- **tu:U-weight:** (W1)–(W4). In (4), a_x<π/2<a_y.
- **tu:U-schur:** Φ as in §4.2; β(1−5/48·β^{-1/4})−√β·H>0, and β>1 implicitly.
- **tu:U-A:** u real, Tu=μu.
- **tu:U-B:** η∈(0,½], δ, τ∈(0,1), β≥β1, u a real eigenfunction with μ≥e^{−η/4}.
- **tu:U-flux:** g as in §1.
- **tu:U-main:** all of the above, plus tu:L-L4.

## 3. Cross-half results relied on

- **tu:L-L4** (tun_lower.tex l.180–189).
  - Its statement has no hypotheses beyond the setting. It gives λ_ee ≥ L_β and λ_eo ≥ L_β − ε_β, with both tending to 1.
  - It is used in tu:U-B and tu:U-main only through "λ, λ_eo ≥ e^{−η/4} for β ≥ β2(η)". That is within its statement.
  - It is stated for the gauge-invariant sector, which matches the definition of λ_eo in §1.1.
- **tu:L-sec-sub** is referenced only in a status remark (l.650). The upper half does not rely on it.

## 4. Failed predicates

1. P4 (prog1, target defect, Remark tu:U-R-rem): at β=64, β(ε−ε_eff) = 1.0381 at a=0.05 (claim 0.98) and 0.9800 at a=0.1 (claim 0.95). Outside 2%.
2. P5 in prog1 run1 (own defect): NaN at s=0.3, 0.6, 1.0 from exp overflow in my code. Rerun in log space as prog1b: 4/4 met. The s=1 value −1.951e-4 is inside the claimed range only through my ±1e-5 rounding allowance.
3. prog2 run1 and prog2b run1 exited 1 (own defects: math.exp overflow in the Lemma K right-hand side and in ω). Neither is a predicate failure of the target.

Child item 12 (measured only) does not reproduce the remark's 2.2e13 (it finds 2.03e13) or its "8.6–14" (it finds 7.33–14.23); see #23.

## 5. What I did not check

- The second half (Sections 5–8), beyond the statement of tu:L-L4 and the status lines quoted in #4.
- The authors' Lean files (not present). My Lean file covers only the outer Taylor step, the Prop. B exponent steps and e^{1/8} ≤ 2.
- The companion-paper splittings up to β=256 (status item 4). I did not compute m_eo of the full T.
- Standard facts used without proof: Jentzsch's theorem, Peter–Weyl/Schur orthogonality, the Hessian of the distance function on S³, D^j_00 = P_j.
- Lemma tu:U-K and Lemma tu:U-schur only on finite grids of (β, p, H, η).

## 6. Delegated questions and outcomes

- **Child T181** (admitted under T179; run recorded as `child-run1`, exit 0; released).
  - Question: numerically recompute every explicit constant and scalar inequality of §§1–3: c*, L, D(1), the cosine bound, the I1 and I0 envelopes, the outer exponent, 2asinh(cos ½), A(1), the Remark K exponent, the Lemma tu:U-fixed identities, and the master-bound deficit.
  - Control question: ∫₀³x² = 9 and 2asinh 1. Graded before reading anything else: **correct** (9.000000, 1.762747).
  - Outcome: 11 met, 0 failed, 1 measured only (c* = 4.6054131945).
  - I reran its program in my register (`rerun-child-main`): output byte-identical.
- **Grandchild T184** (admitted under T181 at depth 3, released).
  - Question: an independent check of the I1 lower bound at the boundaries, z→0 (1e-6) and z up to 700.
  - Control: ∫₀^π sin = 2, answered correctly.
  - Outcome: met, minimum margin 2.69e-6 at z=700. I reran its check.py (`rerun-grandchild`), exit 0.

## 7. What a reader of another lineage should look at first

1. **The §1.3 status paragraph against tun_lower.tex l.1055–1057 and l.612.** The overall "proved" claim depends on the unreviewed gap bounds of tu:L-gauss and tu:L-taylor in the other half.
2. **Lemma tu:U-schur together with Remark tu:U-K-rem.** The whole liminf rests on log w ≤ Φ'²/2 + ω(β) with ω → 0. That limit is real, but ω is thousands of nats until β ≈ 10^8 (for τ=0.5) and until roughly (Hπ²)⁴ ≈ 10^13 or more for small τ.
3. **The patched Lemma tu:U-W13 and the C² gluing at π/2.** It is correct, but it is the one place where a hidden non-smoothness would break the Taylor step.
4. **Theorem tu:U-F-master's outer region.** The bound "area × sup" is where the 10^13 threshold comes from. Correct, but extremely lossy.
5. **Prop. tu:U-B(2)**, which is "the same proof with the links exchanged". It is not needed here, but the second half relies on it.

## 8. Exact commands to rerun

```
cd /home/user/z4-workers/v1-chU
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name prog1-rerun --expect-exit 0 --timeout 300 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 prog1_fibre.py res_prog1_runN.txt
$P check --ws pcp --name prog1b-rerun --expect-exit 0 --timeout 300 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 prog1b_barta.py res_prog1b_runN.txt
$P check --ws pcp --name prog2b-rerun --expect-exit 0 --timeout 300 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 prog2b_weight_schur.py res_prog2b_runN.txt
$P check --ws pcp --name lean-rerun --cwd /home/user/z4-lean --expect-exit 0 --timeout 300 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/v1-chU/referee_scalar.lean'
$P check --ws pcp --name rerun-child-main2 --cwd rerun_child --expect-exit 0 --timeout 300 -- python3 t181_main.py results_rerunN.txt
$P check --ws pcp --name rerun-grandchild2 --cwd rerun_child --expect-exit 0 --timeout 300 -- python3 gc_check.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

(Result files are opened with mode "x", so replace N with a new suffix on each rerun.)

Child run, exactly as executed:

```
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label v1-chU-child --parent T179        # -> T181
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T181
```

Register verification, last line of each:
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

Both are re-quoted after the final verify below.

Final verify (after report written):
- python last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- python result line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- rust last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."
