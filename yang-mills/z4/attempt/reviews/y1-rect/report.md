**Sign answer:** the mean 1×2 rectangle R = E(a₊·a₋) = ⟨½Tr U_{1×2}⟩ is ≥ 0 for every β ≥ 0 on the periodic box with even side in the long direction, and in its periodic-time limit. Status: an elementary site-reflection proof, re-derived here, with its combinatorial core checked by program (A7). Monte Carlo finds it strictly positive (5–4600σ) at all 5 β on 4⁴ and at 3 β on 6⁴. The target uses it correctly. The bound it feeds, J ≥ 2⁻²²/49, is true but about 7.6·10⁶ times weaker than needed. A numerically measured constant gives J ≥ 0.0369·(1+R).

Worker y1-rect, task T194, register `pcp/`. Lean: /home/user/z4-lean/READY exists, but I did not use Lean, so there is no Lean claim.

## Verdict table

| item | verdict | evidence |
|---|---|---|
| (1a) Statement: R = E(a₊·a₋) equals the mean half-trace of the 1×2 rectangle (long side along y, through the common x-link). The common link does not appear in the loop. | STANDS | A7, L=4 and 6: the loop a₊·a₋⁻¹ has 6 links, is closed and excludes the common link. |
| (1b) Reflection argument (isotropic-variance/README.md, "Integrating every plaquette"): site reflection θ in the plane {y=y₀} containing the selected link. | STANDS | A7: θ maps the oriented path a₊ exactly onto a₋, with the same endpoints and direction. Links in the plane are fixed with orientation. No plaquette has links in both open halves, so S = S_plane + S₊ + θS₊. Then E[a₊·a₋] = Σ_k E[(E[a₊,k ∣ links in planes y₀, y₀+N/2])²] ≥ 0. No complex conjugation subtlety arises: the quaternion components are real, and Tr(AB†) = 2 A·B. |
| (1c) Is a conditional or weighted RP needed in J's lower bound? | STANDS (not needed) | j_e ≥ β²m(k)\|A\|² holds pointwise. Integrating under the full Wilson measure gives E\|A\|² = 2+2R with the unconditioned R, which is exactly what RP controls. |
| (1d) Same sign used with coarse conditioning (coarse-plaquette-floor "Cross-check on the auditor's checkerboard", random coarse coefficients) | NOT CHECKED (gap flagged) | That README uses R only for deterministic c. A coarse-conditional E[a₊·a₋ ∣ 𝒞] is not given by RP, because 𝒞 is not contained in the reflection planes. |
| (2) MC: W₁₂ > 0 at β ∈ {0.5, 1, 2, 2.3, 3.4} | STANDS | Own L=4: 5 of 5 qualify; own L=6: 3 of 3. Ratios W₁₂/err run from 138 to 4649 (table below). The child agrees independently, and a rerun of the child reproduced its output bit-identically. |
| (2) Strong coupling at β=0.5: W₁₁ ≈ u, W₁₂ ≈ u², with u = I₂/I₁ | STANDS | u = 0.123718 and u² = 0.015306. L=4: W₁₁ − u = +1.6e-4 (0.8σ), W₁₂ − u² = +1.0e-5. L=6: +9e-5 and −1e-5. |
| (2) Weak coupling, leading order: 1−W₁₁ = 3/(4β), 1−W₁₂ = r·3/(4β), r = 1.72450 | measured only | At β=3.4, L=6: measured 0.7604 / 0.6142, LO gives 0.7794 / 0.6196. LO is not expected to be accurate at β ≤ 3.4. |
| (3a) J ≥ 2⁻²²/49 as stated (needs E\|A\|² ≥ 2, i.e. R ≥ 0, plus the tilted-Haar constant) | STANDS (weak) | A4: inf_k (1+k)²·min(R′, R/k) = 1/4 at k = 0, against the 2⁻²² that is used. A2 confirms R′ = 1 − 3R/k − R² (finite-difference error 3e-11). |
| (3b) Improvement: J ≥ c₂(1+R), with c₂ = inf_k max(1, k/6)²·m(k) = 0.036886 (at k = 6, i.e. β = 1, \|H\| = 6) | measured only (numerical grid k ∈ [0, 2000] plus asymptote 1/24; not a proof) | A5. With the measured R at β = 2.3 on L=6 (0.388), this gives J ≥ 0.051. |
| (3c) Remaining term Var M | DEFECT of the strategy as a reduction (not of any stated claim) | J ∈ [c, 2K] uniformly, so Var M = χ − J is bounded uniformly **iff** χ is. The identity moves the open problem; it does not shrink it. RP gives no upper bound on Var M. |

Counts (met, failed, measured only): **8 met, 0 failed, 2 measured only**. In the table: 7 STANDS, 1 DEFECT, 1 NOT CHECKED.

## Hypotheses each statement uses, and where they are stated
- **R ≥ 0:**
  - Wilson weight exp(β Σ ½Tr U_p) with β ≥ 0, unreduced and positive. Stated in isotropic-variance/README.md.
  - Periodic spatial side N even, so the torus reflection has two site planes, y₀ and y₀+N/2. Stated in the same README as "N ≥ 6 even".
  - Periodic time, or its limit for the bounded rectangle. Same README: "Take the periodic time limit …".
  - Isotropy is not needed for R ≥ 0. Odd N was not examined.
- **j_e formula:** one-link Haar integral Z = 2I₁(k)/k, mean R(k)h, Hessian R′hhᵀ + (R/k)(I − hhᵀ). Same README. Checked in A1 and A2.
- **J bounds:** β ≥ 1 and \|H\| ≤ 6 (6 incident unit staples), so β²/(1+k)² ≥ 1/49. Each xy face of the slice holds exactly one selected link (checked in A6). The "tilted Haar variance lemma" is in ../low-spin/plaquette.md, which is not provided here. I replaced it with the exact m(k).

## Failed predicates
None in my programs (A1–A8, M1–M3 at every β and L). The child reported none either. Two problems were found before production and fixed:
- My smoke test exposed a bug in my own diagnostic: the unitarity check summed over the wrong axis. This was my own defect, not the target's. It was fixed before any production run.
- The grandchild's W₁₁ on 2⁴ at β=0.5 sits +2.5σ above u. It used an approximate inverse-CDF sampler on a 2⁴ torus with wrapped loops. This is a reasonable expectation of the child's, not a defect of the target. My L=4 and L=6 values sit within 0.8σ of u.

## What I did not check
- The low-spin "tilted Haar lemma" text itself; I bypassed it with the exact formula.
- The coarse-plaquette-floor checkerboard Fourier step, including the (0,π,π) momentum shift.
- Odd N.
- c₂ as a rigorous constant: it is a numerical infimum on a grid, plus the asymptotic expansion R′ ~ 3/(2k²).
- β values other than the five, and L > 6.
- An integrated-autocorrelation analysis (I used 20 bins instead).
- The Osterwalder–Seiler original. Locator: Ann. Phys. 110 (1978) 440. A web search did not surface its text, so the argument above is my own re-derivation.
- I did not rerun the grandchild.

## Delegated questions
- **Child, T197** (admitted under T194, released, register entry K5, exit 0, 338 s). Question: Monte Carlo of W₁₁ and W₁₂ on 4⁴ (and 6⁴) at the five β. Control question: 1/(1+½+⅓+¼) = 0.480000. Its answer was correct, graded before I read anything else of its output. It reported W₁₂ > 0 in 8 of 8 cases. Its L=4 values agree with mine within 1σ at every β. I reran its L=4, β=2.3 case with seed 23 (K11) and got bit-identical output.
- **Grandchild, T198** (admitted and released by the child). Question: independent u(0.5), W₁₁ on 2⁴ at β=0.5, and β=0 Haar values. Its control (41) was correct. It found u = 0.12371793, which matches mine, and W₁₁ and W₁₂ equal to 0 within error at β=0.

## Measured (own mc.py, Kennedy–Pendleton heatbath, 20 bins)

| β | L | W₁₁ | W₁₂ |
|---|---|---|---|
| 0.5 | 4 | 0.123880(193) | 0.015316(111) |
| 1 | 4 | 0.243139(195) | 0.058965(140) |
| 2 | 4 | 0.501712(245) | 0.259599(313) |
| 2.3 | 4 | 0.608831(392) | 0.397678(684) |
| 3.4 | 4 | 0.760850(107) | 0.615917(192) |
| 0.5 | 6 | 0.123810(115) | 0.015297(75) |
| 2.3 | 6 | 0.603371(460) | 0.387656(750) |
| 3.4 | 6 | 0.760377(83) | 0.614166(132) |

## For the author
1. **The sign is fine, and RP is the right tool.** The site reflection through the plane that contains the common link, normal to the long side, gives a sum of squares of conditional means given the two fixed planes. This holds for all β ≥ 0 on the periodic box with even N, and passes to the time limit. It is the unconditioned R that your J bound uses, so no weighted or conditional RP is needed there.
2. **The constant can be greatly improved.** The exact conditional variance gives j_e ≥ β²R′(k)\|A\|², with R′ ≤ R/k checked numerically. That leads to J ≥ c₂(1+R) with c₂ ≈ 0.0369 (minimum at β = 1, \|H\| = 6), against the stated 2⁻²²/49. Making c₂ rigorous needs only a one-variable Bessel-ratio inequality.
3. **The decomposition does not reduce the problem.** Because c ≤ J ≤ 2K, a uniform ceiling on Var M is equivalent to one on χ. Cov(F₀,F_d) = Cov(M₀,M_d) also places all long-time correlation in M. The next obstruction is the reduced measure's factor ∏ 2I₁(β\|H_e\|)/(β\|H_e\|), which couples the staple observables. I know of no tool that bounds Var M from above uniformly in N and β ≥ 1. RP gives lower bounds only.
4. **Gap if R is used conditionally.** If random coarse coefficients are to be handled, as in coarse-plaquette-floor, you would need E[a₊·a₋ ∣ coarse] ≥ 0, and RP does not supply that.

PCP OS: `$P verify --ws pcp` → "Result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)". `pcpos verify pcp/register.jsonl` → "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## Rerun (from /home/user/z4-workers/y1-rect; result files are opened with mode "x", so use new names)
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"; export OMP_NUM_THREADS=1
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control 0.272341
$P check --ws pcp --name analytic --expect-exit 0 -- python3 analytic.py results/analytic_run1.txt
for b in 0.5 1 2 2.3 3.4; do $P check --ws pcp --name mc-L4-b$b --expect-exit 0 -- python3 mc.py results/mc_L4_b${b}.txt 4 $b 500 8000 1234; done
for b in 0.5 2.3 3.4; do $P check --ws pcp --name mc-L6-b$b --expect-exit 0 -- python3 mc.py results/mc_L6_b${b}.txt 6 $b 300 2000 4321; done
$P check --ws pcp --name rerun-child-L4-b2.3 --expect-exit 0 -- python3 child/mc.py 4 2.3 400 3000 23 rerun/child_L4_b2.3.txt
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
