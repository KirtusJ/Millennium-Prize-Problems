inventory: PROVED in Lean — L1 (x(1−x^r) ≤ r(1−x) for real r ≥ 0 via Real.rpow; final scalar step, plain and positive-part), L2 (accumulation, multiplied, divided and positive-part forms), L3 (finite-dimensional real operator version from spectral data: the three operator deductions (A),(B),(P), the Pythagoras split (Q), the composed inequality, and the operator-norm form d = 1 − ‖S_t‖ ≥ (b−κ)_+/(1+2a/(γt))), L4 (3-state reset example identities) / LEFT AS HYPOTHESIS — the three operator hypotheses themselves (I−S_{2a} ⪰ γG, ‖BS_τB‖ ≤ κ, ‖PS_tP‖ ≤ 1−b); P, B being self-adjoint idempotents with BP = 0; spectral data (orthonormal eigenbasis, λ_i ≥ 0) in place of H; the step‑wise inputs d_i ≥ (b_i−κ_i)_+/K_i and b_i ≥ d_{i−1}−ε_i of L2. NOT formalised: infinite dimension, spectral projection 1_{[0,L]}(H) and the limit L↓λ, the complex case, the conditional-expectation structure of P and R.

# Report f2-lean (task T238): Lean formalisation of target/inheritance.md

Worker f2-lean, task T238. Control: `control.txt` = 0.272341 (−ln tanh 1).
Lean was ready (`/home/user/z4-lean/READY` exists). Lean file: `/home/user/z4-workers/f2-lean/Inheritance.lean`. Axioms: `axioms_printout.txt`, 18 lines, each `[propext, Classical.choice, Quot.sound]`. Exit 0. `grep -c sorry` gives 0.

## 1. Verdict table

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | x(1−x^r) ≤ r(1−x), x∈[0,1], **real** r ≥ 0 | STANDS | `F2Lean.xr_le` (Real.rpow; x = 0 handled, including r = 0). Numerical N1: 200000 cases, 0 fail. |
| 2 | Final scalar step: b ≤ 1−x+x(1−x^r)/γ+κ ⇒ 1−x ≥ (b−κ)/(1+r/γ), also the (·)_+ form | STANDS | `scalar_step`, `scalar_step_pos`; also `exp_rpow_ratio`: e^{−2aλ} = (e^{−tλ})^{2a/t}. N2: 200000/200000 qualify, 0 fail. |
| 3 | Accumulation d_n ≥ M_n^{−1}(d_0 − Σ_{i=1}^n M_{i−1}(ε_i+κ_i))_+ | STANDS; the M_{i−1} index is correct and sharp | `accum_mul`, `accum`, `accum_pos`. Only K_i > 0 is needed. K_i ≥ 1, κ_i ≥ 0 and ε_i ≥ 0 are not needed. The (·)_+ form also needs d_0 ≥ 0, which matters only for n = 0. Equality holds whenever every hypothesis is tight (child: 506/506 exactly). With M_{i−2} the bound is false (counterexample below). With M_i it is true only when K ≥ 1, because it is then weaker. N3 found 634 failures of the M_i form for K in (0.3, 4). |
| 4 | Finite-dimensional operator version of the main inequality | STANDS (finite dimensions, real scalars, spectral-data interface) | `gated_main` and `gated_main_norm`, built from `S_lower`, `S_eig_quad`, `B_step`, `P_step`, `pyth`, `S_norm_le`, `S_eig`. N4: 1863 random instances, 0 fail. |
| 5 | The text's ‖BS_τB‖ step: e^{−τL}‖BE‖² ≤ ‖BS_τB‖ ⇒ ‖Bv‖² ≤ e^{τL}κ | STANDS (at vector level, rank-one E) | `B_step`. Lean proves c‖EBv‖² ≤ ⟨Bv,S Bv⟩ ≤ κ‖Bv‖² and ‖EBv‖ ≥ ‖Bv‖². This gives c‖Bv‖⁴ ≤ κ‖Bv‖², and then c‖Bv‖² ≤ κ. The case Bv = 0 uses κ ≥ 0, which is derived from the hypothesis. |
| 6 | Reset-process example: ‖BS_tB‖ = e^{−ℓt} regardless of the mass of the event | STANDS (algebraic identities proved; the operator-norm statement is assembled in the text, not in Lean) | `reset_example`: f = (1,−1,0) is centered, has zero coarse mean on A, vanishes off A, satisfies S_t f = e^{−ℓt} f, and has Rayleigh quotient e^{−ℓt} for every p. Also S_t = e^{−ℓt} on all centered g. |
| 7 | Author's target/Checks.lean, rerun | STANDS | Check K2 exit 0. All 5 declarations use only the 3 standard axioms. |
| 8 | The three operator hypotheses (Wilson inputs) | NOT CHECKED | They are hypotheses by design. |
| 9 | Infinite-dimensional spectral argument (E = 1_{[0,L]}(H), L↓λ) | NOT CHECKED in Lean | It is replaced by an eigenvector of the smallest eigenvalue in finite dimension. |

Counts (met, failed, measured only): **8 met, 0 failed, 3 measured only**.
- Met: N1, N2, N3 (M_{i−1}), N4, Inheritance.lean pass, Checks.lean rerun, child test_c rerun, grandchild check rerun.
- Measured only: N3 failure count of the M_i variant for K<1, the minimum slacks, and the child's C'' counterexample.

### Exactly what each declaration proves (namespace F2Lean)
- `xr_le x r : 0≤x → x≤1 → 0≤r → x*(1 - x^r) ≤ r*(1-x)`. Here `^` is Real.rpow, so r is any real r ≥ 0.
- `scalar_step b κ γ r x : 0<γ → 0≤r → 0≤x → x≤1 → b ≤ 1-x+x*(1-x^r)/γ+κ → (b-κ)/(1+r/γ) ≤ 1-x`.
- `scalar_step_pos`: the same hypotheses give `max (b-κ) 0/(1+r/γ) ≤ 1-x`.
- `exp_rpow_ratio t a λ : t≠0 → exp(-t*λ)^(2a/t) = exp(-(2a)*λ)`.
- `M K n := ∏_{j<n} K(j+1)`, so M 0 = 1 and M n = K_1⋯K_n.
- `accum_mul` assumes `∀i, 0<K(i+1)`, `∀i, (b(i+1)-κ(i+1))/K(i+1) ≤ d(i+1)` and `∀i, d i - ε(i+1) ≤ b(i+1)`. It proves `d 0 - Σ_{i<n} M K i*(ε(i+1)+κ(i+1)) ≤ M K n * d n`. Summation index i+1 = the text's i, and the weight M K i is the text's M_{i−1}.
- `accum`: the same statement divided by M_n.
- `accum_pos` uses the text's hypothesis `max(b-κ)0/K ≤ d` and `0 ≤ d 0`. It proves `max(d0 - Σ …) 0 / M K n ≤ d n`.
- L3 setting: E is a real inner product space and `e : OrthonormalBasis ι ℝ E` with ι finite. `lam : ι→ℝ`. `S e lam s w := Σ_i (exp(-s*lam i)*⟪e i,w⟫)•e i`.
  - `S_quad`: ⟪w,S_s w⟫ = Σ e^{−sλ_i}⟪e_i,w⟫².
  - `S_lower`: e^{−sλ_{i0}}⟪e_{i0},w⟫² ≤ ⟪w,S_s w⟫, i.e. S_s ⪰ e^{−sλ}vv*.
  - `S_eig_quad`: ⟪v,S_s v⟫ = e^{−sλ_{i0}}.
  - `S_eig`: S_s e_{i0} = e^{−sλ_{i0}} e_{i0}.
  - `S_norm_le`: if t ≥ 0 and λ_{i0} is minimal, then ‖S_t w‖ ≤ e^{−tλ_{i0}}‖w‖.
- `B_step`: B is a linear map with ⟪Bx,y⟫=⟪x,By⟫ and B∘B=B, and `∀u, ‖B(S_τ(Bu))‖ ≤ κ‖u‖`. It proves `0 ≤ κ ∧ e^{−τλ_{i0}}‖B e_{i0}‖² ≤ κ`. No sign condition on τ is used.
- `P_step`: the same statement for P with 1−b in place of κ. It proves `e^{−tλ}‖Pv‖² ≤ 1−b`.
- `pyth`: P and B are self-adjoint idempotents with B∘P = 0. It proves ‖v‖² = ‖Pv‖² + ‖v−Pv‖² and ‖v−Pv‖² = ‖v−Pv−Bv‖² + ‖Bv‖², i.e. ‖Qv‖² = ‖Gv‖² + ‖Bv‖².
- `gated_main` hypotheses:
  - λ_i ≥ 0, P and B as in `pyth`;
  - 0 ≤ a, 0 < t, τ ≤ t, 0 < γ;
  - h1: ∀w, γ‖w−Pw−Bw‖² ≤ ⟪w,w⟫ − ⟪w,S_{2a}w⟫;
  - h2: ∀u, ‖BS_τBu‖ ≤ κ‖u‖;
  - h3: ∀u, ‖PS_tPu‖ ≤ (1−b)‖u‖.

  It proves `(b−κ)/(1+2a/(γt)) ≤ 1 − e^{−tλ_{i0}}` for **every** eigen-index i0.
- `gated_main_norm` adds the hypothesis that λ_{i0} is minimal. It proves `∀w, ‖S_t w‖ ≤ (1 − (b−κ)_+/(1+2a/(γt)))‖w‖`, which is the text's conclusion d = 1−‖S_t‖ ≥ (b−κ)_+/(1+2a/(γt)). Together with `S_eig`, ‖S_t‖ = e^{−tλ_min}.
- `reset_example p ℓ t`: weights π = (p,p,1−2p), 𝔼f = Σπ_i f_i, S_t f = e^{−ℓt}f + (1−e^{−ℓt})𝔼f, and f = (1,−1,0). It proves:
  - 𝔼f = 0;
  - p f₀ + p f₁ = 0;
  - f₂ = 0;
  - S_t f = e^{−ℓt}f;
  - Σπ_i f_i (S_t f)_i = e^{−ℓt} Σπ_i f_i²;
  - Σπ_i f_i² = 2p;
  - ∀g with 𝔼g = 0, S_t g = e^{−ℓt}g.

### What target/Checks.lean already proves (not duplicated)
- `gated_deficit`: the final scalar step after linearisation, (b ≤ d + rd/γ + κ ⇒ (b−κ)γ ≤ d(γ+r)).
- `weighted_step`: a single multiplied step of the accumulation, with no induction or telescoping.
- `rare_suppression`, `sum_weighted_rows`, `gaussian_floor`: arithmetic used in other files.

Checks.lean does not contain the rpow inequality (item 3 of PRIOR_REVIEW "for the author"), the telescoped accumulation, or any operator step. I added these.

### Remarks on the target (no defect found)
- The accumulation needs only K_i > 0. The text does not claim more. Its M_{i−1} indexing is exactly the unrolled recursion and is attained with equality.
- In the main inequality, a > 0 is used only as a ≥ 0 and τ > 0 is not used. The inequality τ ≤ t and H ≥ 0 are both used: they give e^{−(t−τ)L} ≤ 1. That κ ≥ 0 follows from the norm hypothesis.
- In finite dimension the inequality holds at every eigenvalue, not only the lowest. The lowest is the binding one.
- I used a rank-one E = vv*, so the text's ‖BE‖ device is not needed. The vector argument in `B_step` gives the same bound.

## 2. Hypotheses used and where stated
- **inheritance.md ¶1:**
  - H ≥ 0 self-adjoint and S_t = e^{−tH}. In Lean: spectral data with λ_i ≥ 0 (`hlam`).
  - P is an orthogonal projection, Q = I−P, B = RQ is an orthogonal projection inside Q, G = Q−B. In Lean: `hPsa`, `hPid`, `hBsa`, `hBid`, `hBP` (B P = 0). G is only defined as Q − B. The conditional-expectation origin of P and R is not formalised.
- **inheritance.md ¶2 display:**
  - a>0, t>0, 0<τ≤t, γ>0. In Lean: `ha : 0≤a`, `ht`, `hτt`, `hγ`.
  - I−S_{2a} ⪰ γG (h1), ‖BS_τB‖ ≤ κ (h2, stated pointwise), ‖PS_tP‖ ≤ 1−b (h3, pointwise).
  - "Stated pointwise" is the definition of the operator-norm bound. The equivalence `ContinuousLinearMap.opNorm_le_iff` is not invoked in the file.
- **Proof paragraph:** spectral theorem S_τ ⪰ e^{−τL}E, and the limit L↓λ. In Lean these are replaced by `S_lower` (proved from the spectral data) and an eigenvector at λ_min (finite dimension).
- **Accumulation paragraph:**
  - K_i = 1+2a_i/(γ_i t), M_i, M_0 = 1. In Lean: `M`, and only K_i > 0 is assumed.
  - b_i ≥ d_{i−1}−ε_i is the paragraph's own input. In Lean: `hb`.
  - d_i ≥ (b_i−κ_i)_+/K_i is the main inequality applied at step i. In Lean: `hd`.
  - d_0 ≥ 0 is used for the (·)_+ form.
- **Reset paragraph:** a stationary reset process, a coarse event of mass 2p, and two equiprobable labels. In Lean: explicit weights. The constraint p ∈ (0,1/2) is not used, because the identities are algebraic.

## 3. Failed predicates
None of my predicates failed.
- One variant was expected to fail and is informational: the M_i-indexed accumulation fails 634 times out of 20000 in N3 when K_i < 1. This was my own expectation and is not a defect, because the text uses M_{i−1}.
- The child's C'' (M_{i−2}) fails 495 times out of 4000. Exact counterexample: n=2, K=(2,3), ε=(0.1,0.05), κ=(0.02,0.01), d_0=0.5. Here d_2 = 13/300 < 4/75 = RHS(C''), while RHS(C) = 13/300 exactly. This was expected and is not the target's formula.
- Lean compile errors during development (wrong rewrites) were my own mistakes. Each was fixed before the final run.

## 4. Not checked
- No infinite-dimensional or unbounded H. No functional calculus, spectral projection 1_{[0,L]}(H), or limit L↓λ.
- Complex Hilbert spaces: Lean is over ℝ only.
- The Lean statement assumes S is given by spectral data. It is not derived from an operator H.
- The equivalence of the pointwise bound with the operator norm is not proved in the file.
- The three operator hypotheses, including the Wilson / 24-colour input and the return estimate.
- The comparison b_i ≥ d_{i−1} − ε_i and the "sufficient conditions" sentence (Σ a_i/γ_i < ∞): this is a remark, not a theorem, and was not formalised.
- For L4: Lean does not prove that B f = f for B = RQ, stationarity or reversibility of the reset process, or ‖BS_tB‖ = e^{−ℓt} as an operator-norm equality. That last step follows from the proved Rayleigh quotient together with S_t = e^{−ℓt} on centered functions.
- Last paragraph of inheritance.md (fixed-orbit measurements) and inheritance_ungated.md were not checked.

## 5. Delegated questions and outcomes
- **Child T240** (`f2-lean-child`, parent T238; admitted at event 479 and released by me at event 486).
  - Question: numerical test of L2's indexing (M_{i−1} against M_i and M_{i−2}) on random sequences.
  - Control: (1+1)(1+1/2)(1+1/3)(1+1/4). Answer 5 is correct, and I graded it first.
  - Returned:
    - C (M_{i−1}) holds 4000/4000 in exact Fractions, with equality 506/506.
    - C' (M_i) holds, since K ≥ 1 in its cases.
    - C'' fails 495 times.
  - I reread test_c.py and reran it as check K5 in child_rerun/. The output is byte-identical.
  - I agree, with one qualification: C' holds only because the child sampled K ≥ 1. With K < 1 it fails (my N3).
- **Grandchild T241** (`f2-lean-grandchild`, parent T240; admitted at event 480 and released at event 481 by the child).
  - Question: the exact n=2 equality case.
  - Control: the same product. Answer 5 is correct.
  - Returned: d_2 = 13/300 = RHS(C), RHS(C') = 0, RHS(C'') = 4/75 (fails).
  - I reran it as check K6 (identical output) and checked by hand: d_1 = 0.19, d_2 = 0.13/3, and RHS(C) = (0.5 − 0.12 − 2·0.06)/6 = 13/300.

## 6. Rerun commands
```
cd /home/user/z4-workers/f2-lean
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
# result files are opened with mode "x": move results_numtest.txt, child_rerun/results_test_c.txt, child_rerun/grandchild/result.txt away first
$P check --ws pcp --name numtest --expect-exit 0 -- python3 numtest.py
$P check --ws pcp --name author-checks-lean --expect-exit 0 --cwd /home/user/z4-lean -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/f2-lean/Checks_copy.lean'
$P check --ws pcp --name inheritance-lean --expect-exit 0 --cwd /home/user/z4-lean -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/f2-lean/Inheritance.lean'
$P check --ws pcp --name child-test_c-rerun --cwd child_rerun --expect-exit 0 -- python3 test_c.py
$P check --ws pcp --name grandchild-check-rerun --cwd child_rerun --expect-exit 0 -- python3 grandchild/check.py
# child (already run as check K3):
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Last line of `$P verify --ws pcp`:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Last line of `pcpos verify pcp/register.jsonl`:
`A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

The register holds 8 events: init plus checks K1–K6 and the child run, recorded as K3.
