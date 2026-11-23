# Cross-review e1-chalA4 (task T44): the single-plaquette action estimate

Target: `target/` (Director A4, OpenAI Codex lineage), files README.md, spectrum.md, checks.md, check_local.py, LocalAction.lean; sub-folders `odd-clover/` and `site-scalar/` were opened but they hold different results and were not reviewed. Control: `control.txt` = 0.272341. Lean READY present.

**What the author asked to have challenged:**
- **(i) common-root sign for adjacent pairs:** CLEARS. The only hypothesis it imports is the uniform face moment E|F_p|^2 <= C.
- **(ii) polynomial variation against the full moving paths:** CLEARS WITH A STATED GAP. The power count L^{3/2}/sqrt(beta) is correct as reconstructed. The term from root paths that contain the varied link is included and is subleading. The gap is the "strip bound", O(sqrt(w(e))/sqrt(beta)) in L^2 uniformly in w, time and state. It carries the leading error, it is imported from `../spatial-packet/strip/`, which is not in the copy, and I did not check it.

## 1. Verdict table

| Item | Verdict | Evidence (one line) |
|---|---|---|
| (i) Reflection sends re-rooted D_k to -D_j exactly, colour components included | STANDS | `prog/reflect_exact.py` (K3): 96/96 to 1.1e-15 with the root on plane s=a+j+k+1. The identity fails off that plane (48/48) and componentwise with an off-plane root (48/48). Dot products are invariant under re-rooting on the line (96/96). |
| (i) E D_j·D_k <= 0 for distinct pairs, and the line-average bound (2) | STANDS (CLEARS) | Derivation in §A1 below. Free field: X(d)<0 for d=1..15 (child T45, rerun by me; own quadrature K5). SU(2) MC on 8^4 at beta=16 and 64: every cross moment is negative, at >15 sigma for d=1. L·MS(L) = 1.29, 1.15, 1.01 for L=2,4,8 at beta=64. |
| (ii) Power count (3): ‖h‖_{1,√w} <= C L^{3/2}, ‖h‖_∞ <= C | STANDS | `prog/hodge2.py` (K7, 80^4 torus, M=∞): ‖h‖_{1,√w}/L^{1.5} = 0.70, 1.32, 1.72, 1.83, 1.83. Local exponent falls 2.41 → 1.51. ‖h‖_∞ saturates at 0.128. |
| (ii) Moving-path (root transporter) derivative included, O(L/√β) | STANDS | README bullet 2 ("Differentiating a root transporter…"). `prog/commutator.py` (K9): the derivative equals (2/√β) T×F exactly and is bounded by 2\|F\|/√β (200/200), and it is nonzero. |
| (ii) Leading error O(L^{3/2}/√β) through the strip bound | STANDS WITH A STATED GAP | The strip bound is imported (`../spatial-packet/strip/README.md`, not in the copy) and was NOT checked. The one-line "signed direct derivative … likewise" is not derived in the target. |
| Balance L ~ β^{1/4}, exponent 1/8 | STANDS | L^{-1/2} = L^{3/2}β^{-1/2} gives L = β^{1/4} and an error of β^{-1/8}. Target Lean `balance` passes (K11). |
| A3a: the error is absolute, informative only for n << β^{1/64} | STANDS | (3/2)G(n)^2 ~ 3/(2π^4 n^8) is greater than β^{-1/8} exactly when n << β^{1/64}. This is the window stated in spectrum.md. |
| A3b: n^8 ν(E<=u/n) → 3u^8/(2π^4·8!), tilted law Gamma(8,1) | STANDS | Rederived: J_l(0) = π^{-2}(l+1)^{-4}, so the tilted moments are (l+1)^{-8} = E e^{-lε} for Gamma(8,1). The weight is K0 u^8/8! with K0 = 3/(2π^4). Rerun: n=128 gives 0.0154084 against 0.0153990. |
| A3c: lag ratio ⌊n/2^d⌋ : n → 2^{8d} | STANDS | Follows from (1) and G ~ π^{-2}n^{-4} inside the window. Target cubature: 0.003899 against 2^{-8} at n=64. |
| A4: consistency with the 'attempt' inequality Cov/Var >= (G/G0)^2 | STANDS (consistent). Inclusion of dyadic states NOT CHECKED | The target bounds any constant background by Cβ^{-1/8}; it does not exclude one. |
| target/check_local.py runs from the copy | DEFECT (of the copy, not of the mathematics) | Exit 1 (K1): FileNotFoundError for `../spatial-packet/strip/check_strip.py`. The 156-word reflection check cannot be rerun from target/. The other two parts run and reproduce the posted numbers (K2). |
| target LocalAction.lean | STANDS (arithmetic only) | K11 exit 0. Axioms are propext, Classical.choice and Quot.sound; there is no sorry. It covers no Wilson-measure statement. |

**Predicate counts (own programs plus the target rerun): 30 met, 3 failed, 5 measured only.**

## 2. Hypotheses each statement uses, and where each is stated

- **(i) / eq. (2):**
  - Site-reflection positivity of the Wilson measure on even periodic tori, for real functions of the links in a closed half-space. This is not stated in the target; it cites `../../../central-quotients/tangent-curvature/reflection.md` and Menotti–Pelissetto.
  - The root-path ordering "time, axes 2, 3, then axis 1", so that lines along axis 1 share a prefix. Stated in README §"A finite-coupling bound".
  - A uniform face moment ‖F_p‖_q <= C_q (only q=2 for (2)). Imported from `periodic-limit/pressure.md`.
  - A state "specified on gauge-invariant functions" (D_j·D_k is gauge invariant). Stated in README.
- **(ii) / eq. (4):**
  - The Hodge/heat estimates (3). Stated in README, with walk bounds imported from `rate/heat.md`.
  - The strip bound O(√w(e)/√β) in L^2 for rooted prefix and detour errors. Imported from `../spatial-packet/strip/`.
  - ‖1−U_p‖_q = O_q(β^{-1/2}). Imported (pressure.md).
  - The Haar identity with a link-dependent generator that avoids the varied edge. Imported from `rate/ward.md`.
  - Face centres with |z|_1 <= C0 L.
  - M → ∞ taken after the torus limit.
- **(1):** (2) and (4) together, plus the exact identity 2Y = |F|^2 + Y^2/β (my check: |F|^2 = β(1−a0^2) = 2Y − Y^2/β) and the Wick coefficient 3G^2/2.
- **spectrum.md:**
  - (1), uniformly over all lags (needed at lags (l+1)n for every l).
  - The joint transfer representation, imported from `joint-momentum/README.md`.
  - The window n^8 β^{-1/8} → 0.

## 3. Failed predicates

1. **K1:** `target/check_local.py` expected exit 0, got exit 1 (missing external file). This is a defect of the target copy's self-containment, not of the mathematics.
2. **K6, hodge.py H3 (two cases, displaced and undisplaced):** the ratio of ‖h‖_{1,√w}/L^{1.5} between L=8 and L=4 was 1.247 and 1.271, against my tolerance of 1.2, on a 40^4 torus. This was my own expectation: the range was pre-asymptotic and the torus too small. On 80^4 (K7) the local exponent falls to 1.51 and the ratio saturates at 1.83. It is not a target defect.

## 4. What I did not check

- The strip bound (the leading error term in (ii)), the uniform face moments (pressure.md), the Ward identity derivation in `rate/ward.md`, the walk bounds in `rate/heat.md`, and the joint transfer representation. None of these is in the copy.
- The "signed direct derivative of a tested face … likewise costs O(√w/√β)" step, and the cube-identity term for k. I followed the power count but did not derive either.
- The constant C in (1), and whether "sufficiently large β" is effective.
- A Monte Carlo test of (1) itself, or of the Ward identity (4).
- The `site-scalar/` and `odd-clover/` results.
- The 'attempt' folder (outside my directory). The A4 assessment below uses only the brief's description of it.
- The "1.47" numerical derivative from the earlier post. I could not locate it inside my directory. I only verified that the target's text includes the moving-path term.

## 5. Delegated questions and outcomes

- **Child T45** (admitted under T44; refusal: none; released). Question: free one-colour field c(m) along axis 1, the pair cross moments X(d) = 2c(2d)+c(2d−1)+c(2d+1) for d=1..15, and N(L) for L = 2, 4, 8, 16. The run was `child-run1` (my register K4, exit 0, 72 s).
  - **Control graded first:** child/control.txt = 0.500000, which is correct (G(0) = 1/2).
  - **Returned:** X(1) = −0.093442. All 15 values are negative beyond the mesh error. L·N(L) = 0.431, 0.384, 0.359, 0.346.
  - **My check:** I reread main.py and quad.py and reran them in a scratch copy, with identical output. My own Gauss–Legendre program (`prog/free.py`, K5) gives c(1) = −0.0688747 and X_inf(1..3) = −0.093442, −0.003686, −0.000447, which agree.
- **Grandchild T46** (admitted with parent T45 at seq 93; released). Question: recompute c(1) and X(1) by a 4D torus sum at N = 32 and 48. Result: X(1) = −0.0934428 at N=48, agreeing with the child to 4e-7. The child reported that it reran this. I did not rerun torus.py myself.

## A1, my reconstruction (not the target's text unless quoted)

- **Reflection.** θ_s is the site reflection x1 ↦ 2s − x1, with s = a+j+k+1, the site plane strictly between the pairs.
- **Pairs.** D_j = F(a+2j) + F(a+2j+1), where F(x) = √β Im(W U_p W^{-1}). Here W is the straight axis-1 path from the root at x1=s, and U_p is the 12-loop based at x with steps [+1,+2,−1,−2].
- **Oddness.** The face based at x reflects to the reversed face based at 2s−x−1, and the rooted word maps to the exact inverse word. Hence θ(F^a(x)) = −F^a(2s−x−1) for each colour a, and θ(D_k) = −D_j. Both are in the same adjoint frame, because the root lies on the plane and is fixed by θ.
- **Positivity.** For real X measurable with respect to the links in {x1 >= s} (plane links included), E[θ(X)X] >= 0. Taking X = D_k^a, which lies in the closed half when j<k, gives E[D_j^a D_k^a] <= 0. Summing over a gives E D_j·D_k <= 0.
- **Re-rooting.** Moving the root to the original root conjugates every face on the line by one quaternion, so dot products are unchanged configuration by configuration (R3). Componentwise equality needs the root on the plane (R4).
- **Average.** ‖L^{-1}ΣF‖_2^2 <= L^{-2} Σ_j E|D_j|^2 <= C/L. All of this matches the target's text. The torus d=3 MC value (−0.141 at β=16, −0.233 at β=64, against −0.283 in the free field) is a wrap-around effect: the transport carries the axis-1 Polyakov loop. The sign is unaffected.

## A2, my reconstruction

The identity is E[(score along h)·Q] = E[∂_h Q], from invariance of Haar measure under U_e → exp(εT_e/√β)U_e. Here T_e is the root generator transported along a root path that avoids e. The score Σ_e h_e·(transported link derivative of the action) equals F(dh) up to errors.

The error terms:
- **Transport discrepancy:** Σ_e|h_e|·O(√w(e)/√β) = O(‖h‖_{1,√w}/√β) = O(L^{3/2}/√β). This uses the strip bound and is the leading term.
- **Moving paths of the other factors:** O(L/√β). Path length O(L), with ‖h‖_∞ <= C; time trunks do not contribute because h has only components 1 and 2.
- **Coexact part k:** O(L^{3/2}/√β).
- **Residual b:** O(L^3 M^{-3/2}) → 0.

Where L^{3/2} comes from: ‖h‖_1 ~ L (d*Δ^{-1} applied to a unit face decays like r^{-3} up to scale L), and the weight √w ~ √L multiplies it. Both are confirmed numerically (K7).

Balance: L^{-1/2} = L^{3/2}β^{-1/2} at L = β^{1/4}, which gives β^{-1/8}.

## A4

Any constant (random) background in Cov(Y, Y) at large n would have to be at most Cβ^{-1/8} by (1). The target therefore excludes a background only up to its rate, not identically; spectrum.md uses this only inside the window.

The mechanism is the odd reflection in (2): a line-constant random component of the vector F would contradict ‖A_L F‖_2 <= C L^{-1/2}. Together with the Ward reduction of the fourth moments, this removes a background in Y to O(β^{-1/8}).

So "Cov/Var = (G/G0)^2 + O(β^{-1/8})" is consistent with the attempt folder's ">=". Dyadic periodic 2^k tori are even periodic cubes, so their limits are included **if** the attempt folder uses periodic boundary conditions. I did not verify that.

## 6. Commands to rerun (from /home/user/z4-workers/e1-chalA4)

The result files are opened with mode "x", so move `results/*` aside first.

```sh
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
$P check --ws pcp --name target-check-local --expect-exit 0 -- env OPENBLAS_NUM_THREADS=1 python3 target/check_local.py
$P check --ws pcp --name target-check-local-partial --expect-exit 0 -- env OPENBLAS_NUM_THREADS=1 python3 -c "from runpy import run_path; m=run_path('target/check_local.py'); m['filter_checks'](); m['spectral_checks']()"
$P check --ws pcp --name reflect-exact --expect-exit 0 --cwd prog -- python3 reflect_exact.py
$P check --ws pcp --name free-own --expect-exit 0 --cwd prog -- env OPENBLAS_NUM_THREADS=1 python3 free.py
$P check --ws pcp --name hodge-powercount --expect-exit 0 --cwd prog -- env OPENBLAS_NUM_THREADS=1 python3 hodge.py
$P check --ws pcp --name hodge-powercount-N80 --expect-exit 0 --cwd prog --timeout 290 -- env OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 hodge2.py
$P check --ws pcp --name mc-beta16 --expect-exit 0 --cwd prog -- env OPENBLAS_NUM_THREADS=1 python3 mc.py 16 300 1500 16 ../results/mc_beta16.txt
$P check --ws pcp --name mc-beta64 --expect-exit 0 --cwd prog -- env OPENBLAS_NUM_THREADS=1 python3 mc.py 64 300 1500 64 ../results/mc_beta64.txt
$P check --ws pcp --name commutator --expect-exit 0 --cwd prog -- python3 commutator.py
$P check --ws pcp --name lean-localaction --expect-exit 0 --cwd /home/user/z4-lean --timeout 290 -- bash -c "PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/e1-chalA4/lean/LocalAction.lean"
# child (task T45, admitted with: pcpos task-admit /home/user/z4-work/graph/attempt.jsonl --by principal --label e1-chalA4-child --parent T44)
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-release /home/user/z4-work/graph/attempt.jsonl --by principal --id T45
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Last line of `$P verify --ws pcp`:
`result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`

Last line of `pcpos verify pcp/register.jsonl`:
`A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Caveat: I share a model family with the director; this review is independent of the target's author (Codex lineage), not of Z4.
