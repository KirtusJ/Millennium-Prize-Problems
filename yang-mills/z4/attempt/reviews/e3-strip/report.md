# e3-strip (T58): cross-review of target/transfer-increments/spatial-packet/strip

**Cross-review verdict: CLEARS WITH A STATED GAP.** The strip bound used in local-action (README l.57) follows from strip/README.md eqs. (1)–(2) by an argument I found correct line by line. The gap: the uniform first plaquette moment, 1−W(1) ≤ C/β for every periodic-limit state, and the site-reflection-positivity proof are imported from files outside the copy (`central-quotients/.../pressure.md`, `reflection.md`). I did not check them. Reviewer and director share a model family only on my side; the target's author is Codex.

## Verdict table

| item | verdict | evidence |
|---|---|---|
| check_local.py runs | STANDS | exit 0 (K1). Prints 156 rooted words, free action covariance 0.0154083783 vs 0.0153989734 |
| check_strip.py runs | STANDS | exit 0 (K2). Prints 2352 staple pairs, 648 insertions, 729 roots, Q8 ratio 0.983356651, coherent-rotation counterexample |
| ReflectedStrip.lean compiles | STANDS | READY exists. Copied file, exit 0 (K3), no sorry. All 6 theorems use only propext, Classical.choice, Quot.sound. It covers scalar lemmas only, not the Gram space or the path estimates |
| (a) reflected open-path Gram form | STANDS | Each entry H_st = ½ Σ_ab conj(U(θΓ_s)_ab) U(Γ_t)_ab = ½ tr(U(θΓ_s)^† U(Γ_t)), which is gauge invariant: it is the 1×(s+t) Wilson loop. Site RP on the finite torus holds for the full (non-gauge-fixed) link measure, applied to F = Σ_t c_t U(Γ_t)_ab. That is a legitimate positive-half function: its tangent link lies in the fixed plane. A finite PSD matrix of Wilson loops passes to the local limit |
| Hankel/spectral step → 1−W(l) ≤ l(1−W(1)) | STANDS | q_n bounded and convex ⇒ S is a contraction ⇒ spectral measure on [−1,1] with 1−x^l ≤ l(1−x). Lean proves the two scalar steps |
| (b) where √w comes from | STANDS | No telescoping and no orthogonality. ‖1−U_{1×l}‖₂² = 2(1−W(l)) (exact quaternion identity) ≤ 2l(1−W(1)), so the L² norm is the square root of a deficit that is linear in l |
| (c) move to ordered root, eq. (2) | STANDS | At most 3 swaps of the step past later spatial segments. Each swap is a conjugated 1×\|x_j\| rectangle; conjugation does not change the norm. The bound is Σ_j √(2\|x_j\|(1−W1)). Check: by symbolic word algebra in check_strip.py (648 insertions), and by MC predicate P3 |
| (d) uniform in time lag and state | STANDS (given the imported moment) | The time segment comes first and is never crossed. The only state input is 1−W(1) ≤ C/β plus translation, reflection and axis-permutation invariance of periodic limits |
| (e) group dependence | STANDS | SU(2)-specific: \|1−U\|² = 2(1−ReU), and 2Y = \|F\|² + Y²/β (local-action README l.66). I checked the latter algebraically with Y = β(1−ReU), F = √β ImU: \|F\|² = β(1−Re²) = 2Y − Y²/β |
| rectangles.md area bound | STANDS | Same Gram argument with an m-link middle segment, then axis interchange. MC P2 is met; the free field is met with ratio ≤ 0.69 |
| first plaquette moment, uniform in state | NOT CHECKED | imported (pressure.md, not in the copy) |
| site-RP proof, ward.md (Haar variation) | NOT CHECKED | imported |
| free field: V(1×w) ≤ w·V(1×1), w ≤ 64 | STANDS | child T59, rerun by me (K5). The ratio falls to 0.6731 at w = 64, approaching my analytic limit 2/3 = 2(G₃(0)−G₃(e))/V₁₁. Exponent of V: 0.986 (1×w), 1.024 (w×w), so the L² norm scales as ≈ w^{1/2} |
| SU(2) MC 8⁴, β = 16 and 64 | STANDS | All predicates met (K6, K7). β(1−W(1×w)) agrees between the two β values to within 2% for w ≤ 4. The explicit-constant bound for the rooted quantity is met with ratio 0.19–0.23 |

Counts: **met 11, failed 0, measured only 2** (Hankel eigenvalues; local exponents). Rows NOT CHECKED: 2.

## Statement under review: target text vs my reconstruction

- **Target text, strip/README.md eq. (1):** ‖1−U_{1×l}‖²_{L²(μ)} ≤ 2l[1−W(1)] ≤ Cl/β. Here U_{1×l} is the holonomy of a coordinate rectangle, width 1 and length l, and |·| is the unit-quaternion norm.
- **Target text, eq. (2):** ‖1 − L_x U_e L_{x+e}^{-1}‖₂ ≤ Cβ^{-1/2} Σ_{j>i} √|x_j| ≤ C√(w(x))/√β, with w(x) = 1 + |**x**|₁ (spatial only). The object is the rooted link: a link transported to the root 0 along the ordered path (time first, then axes 1, 2, 3), compared with its root path.
- **Hypotheses:**
  - Wilson SU(2) action exp[−β Σ(1−ReU_p)];
  - μ is a subsequential local limit of even periodic 4-cubes (README l.3);
  - translation, reflection and axis-permutation invariance (README §1);
  - site reflection positivity (README §1, imported);
  - first plaquette moment 1−W(1) ≤ C/β, uniform over μ (README after (1), imported);
  - unit-quaternion identity (README after (1)).
- **Where it is used:** local-action/README.md l.57. The "rooted prefix or detour error" has L² norm O(√w(e)/√β), paired by Cauchy–Schwarz with |F_p Q|. Lines 42 and 59 use the ‖·‖_{1,√w} sums.
- **My reconstruction:** that H_st is a gauge-invariant Wilson loop, and the check of 2Y = |F|² + Y²/β, are mine.
- **Remark:** the target's local-action l.57 also uses higher moments of |F_p Q| ("exponential face moment"). That is a separate hypothesis from the strip bound and is outside this review.

## Failed predicates

None of mine failed. In the smoke test (scratch/smoke1.txt, 2 measurements) every predicate except P4 was reported FAILED because σ = NaN. That was a defect of my run size, not of the target. The child had two failed runs, both its own defects (scipy missing; JSON writing). The child's statement predicates were all met.

## Not checked

- The imported first-moment bound and the site-RP proof.
- ward.md (Haar variation, cube words).
- The comparison with the Gaussian packet (eqs. (3)–(6)) and the seventh-root conclusion.
- The QEMU guest replay.
- Infinite-volume behaviour. The MC is on 8⁴: w > 4 exceeds L/2, which the finite-torus Gram argument does not cover; it is reported but flagged.
- The 3×3 Hankel matrix of W(0..4) at β = 16 has smallest eigenvalue 3.6e−5 (PSD, but within statistical error, about 1e−4). Measured only.

## Delegation

- **Child T59** (admitted under T58, released; ran as child-run1, K4, exit 0).
  - Question: the free 4D lattice Maxwell field. Compute V(1×w) and V(w×w) for w = 1…64, test V ≤ w·V₁₁ and V ≤ w²·V₁₁, and fit the exponents.
  - Control answer: 8. **Correct.**
  - Returned: all claims STAND. Table: V(1×64) = 21.5399, V(64×64) = 63.359.
  - I reran its v.py with different quadrature parameters (K5). It reproduces to about 1e−7. The asymptotic ratio 2/3 agrees with my independent analytic value.
- **Grandchild T61** (admitted under T59, released, per graph lines 121 and 123).
  - Question: an independent periodic-lattice FFT value of V(1×2). Control: G(0)−G(e1) = (1/8)(1−L⁻⁴), met.
  - Returned: V(1×2) = 0.862249 at L = 32, vs 0.8622505 in infinite volume. I reread results.txt; I did not rerun run.py (a copy is in rerun_gc/).

## Rerun commands

```sh
cd /home/user/z4-workers/e3-strip
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name target-check_local --cwd target/transfer-increments/local-action --expect-exit 0 -- python3 check_local.py
$P check --ws pcp --name target-check_strip --cwd target/transfer-increments/spatial-packet/strip --expect-exit 0 -- python3 check_strip.py
$P check --ws pcp --name lean-ReflectedStrip --cwd /home/user/z4-lean --timeout 300 --expect-exit 0 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/e3-strip/ReflectedStrip.lean'
$P check --ws pcp --name mc-beta16 --expect-exit 0 --timeout 300 -- python3 mc_strip.py 16 200 300 16 mc_beta16.txt   # new output name if rerun (mode x)
$P check --ws pcp --name mc-beta64 --expect-exit 0 --timeout 300 -- python3 mc_strip.py 64 200 300 64 mc_beta64.txt
$P check --ws pcp --name rerun-child-v --cwd child --timeout 290 --expect-exit 0 -- python3 v.py 4001 5e3 /home/user/z4-workers/e3-strip/rerun_child_v.json
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Verify output:

- Python `verify` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust `verify` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
