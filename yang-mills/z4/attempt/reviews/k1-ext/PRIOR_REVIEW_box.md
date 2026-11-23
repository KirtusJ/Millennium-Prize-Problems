At a fixed box, the central-patch expansion (README.md) holds as a proof for the compressed patch operator, and as a one-sided bound (min–max upper bound plus spectral inclusion) for the full center-neutral transfer. The two-sided full-neutral claim (full-neutral.md) is a complete written derivation, except that its fixed-exterior step relies on C4's two-site-exterior estimate, which is not in the target and which I could not check. I found no false line. I found two gaps in exposition, both repairable: the global Lipschitz bound of the cutoff vector, and the norm in which the rectangle is defined.

# j1-box review report (task T107): periodic-box spectrum by Director A4

Control: control.txt = 0.272341. Lean: /home/user/z4-lean/READY exists, and the Lean result below was obtained with it.

## 1. Verdict table

| # | item | verdict | evidence (one line) |
|---|---|---|---|
| 1 | What README.md claims (brief item 1) | STANDS as stated | It has two parts. First, a two-sided ordered expansion for the **compression** `1_rect T 1_rect`, zero-extended. Second, for the full center-neutral transfer, only rank ≥ m in o(h) windows plus a min–max upper bound on energies. README l.9 and l.64 say exactly this ("Neither conclusion fixes the ordering"). |
| 2 | What full-neutral.md claims (brief item 1) | derivation, conditional | A two-sided ordered law. It does **not** use "small mass outside the patch". It uses an IMS square partition with error O(s²/r₀²) = O(h/log²h), together with upper norm bounds on the shells (§2) and on the exterior (§1). The lower bound on energies needs §1 exterior, see row 13. |
| 3 | Constant-mode kinetic normalisation, factor n (item 3) | STANDS | Abelian quadratic theory, Schur complement over all nonconstant slice modes at both ends. Coefficient = n/s² per direction, with no mass term, on 2³, 3×2×2 and 3³ at s = 0.3 and 0.1 (rel. err ≤ 2e-16). Own check P1, child T109 and my rerun all agree. Hence slow variance h/n, H_N = −Δ/(2n) + 2nΣ\|X_i×X_j\|², and scaling n^{-1/3}. |
| 4 | Slice dimension 6n+3, hard spectrum m_p (2 transverse per colour), E_{*,N} = 3Σ_{p≠0} ω(m_p), gap d | STANDS | P2/P3 on three boxes, max dev 1e-14. The 2³ value equals the two-site formula: 44.3983569740. |
| 5 | Linear magnetic Hessian slope ±4 sin p for side ≥ 3 (item 2b) | STANDS | Target check.py reproduced: ±3.4641016 (3³), ±4.0000000 (4×3×2), ±3.8042260 (5×2×2), 0 (2³). Also analytic: d/dr \|e^{i(p+2r)}−1\|² = 4 sin p. |
| 6 | ⟨γ, b_X γ⟩ = 0, so PTP = gD_h + o(h) | STANDS | X ↦ ⟨γ,b_Xγ⟩ is linear and invariant under simultaneous SO(3) (γ invariant, b_{RX} = R b_X R⁻¹). Every linear invariant of copies of the vector representation vanishes. |
| 7 | Block absorption: mixed norm k = O(hR), cost 4k²/d = O(h²R²) = o(h) (item 2a) | STANDS | Read README l.48–50. The inequality is Lean `blockCost`, which is scalar only. |
| 8 | Order of the c-dependent hard zero-point energy (item 2a) | STANDS: o(h) | The shift is O(\|c\|²) = O(h²\|X\|²), at most h²R² on the patch. The linear term vanishes (P6, dE/dr ≤ 1.4e-10). It is not O(h). Measured only: the curvature along commuting backgrounds is **negative and O(1) when some side is ≥ 3**: 3×2×2 gives −2.581 (side-3 direction) and +1.429; 4³ gives −3.276; 2³ gives +0.02015 (two-site κ = 0.020367 up to O(r²)). The box argument uses only the order, so this is no defect. However, the two-site statements "positive to quadratic order" (transverse-plaquettes, flat-holonomies) do not carry over to boxes with a side ≥ 3. |
| 9 | Cubic Wilson term (item 2c) | STANDS | The s\|z\|³ exponent error is absorbed by the Gaussian into an O(s) = O(h^{3/2}) multiplier error, uniformly in z. No cancellation is needed. |
| 10 | Electric comparison O_N(s + h²R²) at fixed N (README l.17–19) | STANDS (read, not recomputed) | It extends B4's 2³ chart (local-gauge-quotient, read in full). Orbit tilt is O(\|B\|) and the exponent correction after orbit integration is O(\|B\|²), because d_b*u = 0. |
| 11 | Slow limit H_N and the growing-patch compactness (README l.52) | STANDS (read) | It is joint-spectrum §3 with 1/16 → 1/(2n). V ≥ 0 is confining transversally, and the bosonic matrix model has compact resolvent. |
| 12 | Quasimodes, corrector η_X, center symmetrisation (README l.56–64) | STANDS (read) | The corrector identity (G−g)η + Bγ = 0 is Lean `corrector`, scalar. Cross-patch leakage is exp[−a h²R²/s²] = exp[−a log²h/h]. |
| 13 | full-neutral §1: exterior norm bound limsup‖1_A T 1_A‖ ≤ max_{flat∩A} e^{−E(x)} | NOT CHECKED | It cites ../../central-quotients/tangent-curvature/periodic-limit/two-site-exterior/README.md, which is **absent** from target/. I read the sketch in full-neutral l.22. Its orders are consistent: s²/ρ² = β^{-1/4} and ρ⁴/(εs²) = β^{-1/4}. |
| 14 | full-neutral §1: strict minimum of Σ_p ω(m(p+θ)) at central holonomies (item 4) | STANDS | Hand check: ω′ = x^{-1/2}(x+4)^{-1/2} is a product of Laplace transforms, so ω is a Bernstein function, and the heat-trace walk expansion follows. P4: 800/800 random non-central twists strictly above, minimum deficit 0.16. Equality holds at all 8/12/24/45 grid twists to 1e-13. |
| 15 | full-neutral §2: shell sector bound ‖1_sec T 1_sec‖ ≤ g(1 − b′r), c₀h\|log h\| ≤ r ≤ δ_N | STANDS (read in full) | The four sectors cover the shell. Hard sector: exp[−aκ²r²/s²]. Slow sector: positive-convolution freezing, then e^{−ω(κ²r²/4)} = e^{−2 arsinh(κr/4)}; the identity is checked (P5, rel. err ≤ 6e-8). The O(r) mixed block costs O(r²). The cubic term is O(s) and s/r → 0. |
| 16 | full-neutral §3: IMS localisation and counting with ≤ j constraints | STANDS, two repairable gaps | Error O(s²/r₀²) = o(h). The neutral inner components are center translates, so one set of constraints suffices. Gap (a): a global Lipschitz constant C_N/r₀ in the product link metric for slice-defined cutoffs is asserted ("bounded derivative of the inverse slice coordinate on a fixed tube"), not proved. Gap (b): "sum norms" for the rectangle (README l.15, joint-spectrum l.20) is ambiguous. If it means ℓ¹ over 6(n−1) coordinates, then t ≤ 2r₀ = hR/4 lies inside \|v\| < hR only when √(6(n−1))/4 < 1; this fails already for n = 8 (1.62). Shrinking r₀ by a constant repairs it. |
| 17 | Use of one-site results within their hypotheses (brief) | STANDS | The box argument uses only the eigenvalues e_j of −Δ/2 + 2Σ\|Y_i×Y_j\|² on simultaneous-rotation-invariant functions. It does not use the one-site per-link center-sector results. Center symmetry is handled separately: three slice flips, 8 patches with distinct signed cycle holonomies, so center-neutral = even under the three slice flips (item 5). |
| 18 | Lean PeriodicSpectrum.lean (item 6) | STANDS for what it states | Exit 0. All 8 declarations print only [propext, Classical.choice, Quot.sound]. All are scalar algebra (field_simp/ring/linarith/nlinarith), and none states an operator or spectral fact. |
| 19 | check.py / check_global.py (item 6) | check.py STANDS; check_global.py NOT CHECKED | check.py exits 0 with the quoted numbers. check_global.py imports scipy.sparse and scipy.special.ive, and scipy is not installed (ModuleNotFoundError). I did not write a shim; P4 and P5 cover its content independently. |
| 20 | Monte Carlo, 2×2×2 box, β=256, non-scalar neutral gap (item 7) | NOT CHECKED | My own Metropolis code. The one-site control at β=4 was met but weak (0.960 ± 0.104 vs 0.96893). The box run had τ_int = 240 sweeps for 9000 measurements, so Nmeas/τ = 37.5 < 50 and my pre-fixed TAU rule failed. Per the brief I report no number. |

Verdict counts: STANDS 16 (rows 1, 3–12, 14–18; row 16 with two repairable gaps, row 19 counted as part check.py), derivation-conditional 1 (row 2), DEFECT 0, NOT CHECKED 3 (rows 13, 20, and the check_global part of 19).

## 2. Hypotheses used by each statement and where they are stated

- **README (patch).** Fixed N_i ≥ 2 (l.5). Isotropic Wilson action with probability-normalised electric step (l.5). Based slice pinned at one vertex, with the residual gauge = simultaneous colour conjugation (l.15). Cutoffs \|X\| < R, \|v\| < hR, R = \|log h\| (l.15). Fixed local chart from B4 (l.17). M_0 > 0 on the hard plane, i.e. min_p m_p > 0 (l.38). Joint-spectrum §3 compactness (l.52). The constants depend on N (o_N), with no uniformity in N (l.9, l.66).
- **full-neutral.** Everything in README, plus:
  - C4's exterior estimate (l.22, external file);
  - B4's two-site positive-convolution comparison (l.13);
  - charts and the sinc ≥ 1/2 lower bound on a small fixed neighbourhood (l.40);
  - κ < 1/4 fixed and r ≥ c₀ h\|log h\| (l.33);
  - Lipschitz cutoffs at C_N/r₀ (l.48);
  - Wilson jump second moment O_N(s²) (l.48).
  It states that there is no uniformity in side lengths (l.7, l.50).

## 3. Failed predicates

- TAU rule for the MC box run (mc_box.py): Nmeas/τ_int = 37.5 < 50. This is a failure of my method (a local Metropolis algorithm is too slow for the slow mode at β=256). It is not a defect of the target.
- Docstring slip (mine): mc_box.py's docstring states the leading prediction as 0.23664. The correct arithmetic, used by the code, is 3.012539 · 256^{-1/3}/2 = 0.23722.
- No predicate of box_checks.py failed (37 met), and none of the child's failed (6/6 cases qualify).

Predicate counts (met, failed, measured only):
- Own: 38 met (box_checks 37, MC CTRL 1), 1 failed (TAU), measured only: the P6 curvature values and the box m_eff series (in mc_box256.txt, not reported as a result).
- Child T109: 6 met, 0 failed. Its K2 is a deliberate negative control.

## 4. What I did not check

- C4's two-site-exterior README and quotient-readback README (absent from target): the exterior norm estimate of full-neutral §1.
- I did not recompute the e_j numbers (6.534885, 3.012539, 3.602838); they were taken from the brief.
- No line-by-line Taylor bounds for the electric chart at general N (row 10).
- The global Lipschitz construction (row 16a).
- check_global.py (scipy missing).
- No worker.c files and no PCP OS guest replays (replay-guests.py needs a kernel ELF that I do not have).
- No reliable Monte Carlo.

Files read:
- In full: periodic-box-spectrum/README.md, full-neutral.md, checks.md, PeriodicSpectrum.lean; second-box/joint-spectrum/README.md, transverse-plaquettes/README.md, local-gauge-quotient/README.md, intermediate-shell/README.md, flat-holonomies/README.md.
- In part: periodic-box-spectrum/check.py (first 50 lines, and it was run), check_global.py (imports only), second-box/electric-diagonal/README.md (first 20 lines), MC_three_dir.md (first 60 lines).
- Not read: the subdirectories observable-weights/ and scale-matching/; second-box width-normalization, orientation-readback, transverse-plaquettes/reflections; all worker.c, replay.py, the second-box Lean files and checks.md; one-site-vacuum/* (per the brief).
- No network was used.

## 5. Delegated questions and outcomes

- **Child T109** (j1-box-child, parent T107). It was admitted in the task graph at seq 218, run as child-run1 in my register (K1, exit 0, 78 s), and released by me after my rerun.
  - Question: in the abelian quadratic theory on 2³, 3×2×2 and 3³, integrate the nonconstant slice modes at both ends and give the constant-mode coefficient κ and κ/n.
  - Control: arcosh 2 = 1.316958. I graded it correct before reading anything else.
  - Outcome: κ = n exactly, Q depends only on c − c′, slice dimension 2n+1. I reran box.py in rerun_child/ (K6): ALLPASS, 6/6 cases with κ/n = 1.
  - Limit: this is the same computation as my P1 by a sibling model, so it is not independent review. The child flags that its grandchild's check relies on the same decoupling.
- **Grandchild T111** (j1-box-grandchild, parent T109). Admitted at seq 220, released at seq 223.
  - Question: recompute κ for 3×2×2 with Fourier modes.
  - Outcome reported by the child: control correct, slice dimension 25, κ = 12 at s = 0.3 and 0.1. The child reports rereading and rerunning it. I did not run the grandchild's kappa.py myself.
- I did not delegate the Monte Carlo (I judged it infeasible in a 6-minute child budget). I tried it myself (row 20) and report no number.

## 6. Registers

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp`, last line: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl`, last line: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## 7. Rerun commands (from /home/user/z4-workers/j1-box)

```sh
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name target-check --expect-exit 0 -- python3 target/periodic-box-spectrum/check.py
$P check --ws pcp --name target-check-global --expect-exit 1 -- python3 target/periodic-box-spectrum/check_global.py   # fails: no scipy
cp target/periodic-box-spectrum/PeriodicSpectrum.lean ./PeriodicSpectrum_copy.lean
$P check --ws pcp --name lean-periodic --cwd /home/user/z4-lean --expect-exit 0 -- bash -c "PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/j1-box/PeriodicSpectrum_copy.lean"
$P check --ws pcp --name box-checks --expect-exit 0 -- python3 box_checks.py          # writes box_checks_result.txt (mode x: remove or rename first)
$P check --ws pcp --name mc-ctrl --expect-exit 0 -- python3 mc_box.py ctrl 11 mc_ctrl.txt 6000
$P check --ws pcp --name mc-box256 --expect-exit 0 -- python3 mc_box.py box 7 mc_box256.txt 9000 48 0.035
mkdir -p rerun_child && cp child/box.py rerun_child/ && $P check --ws pcp --name child-rerun --cwd rerun_child --expect-exit 0 -- python3 box.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Before mc-ctrl and mc-box256, mc_box.py was edited once: the box-mode eps became the 6th argument. The timing run (K7, `mc_box.py box 1 mc_timing.txt 100 64`) used the earlier fixed eps = 0.09 and gave acceptance 0.055.

Child launch, as run:
```sh
R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos; G=/home/user/z4-work/graph/attempt.jsonl
$R task-admit $G --by principal --label j1-box-child --parent T107        # -> T109
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T109
```

I share a model family with the director, so my agreement here is not independent review. The steps that most need an outside reader are rows 13 and 16a.
