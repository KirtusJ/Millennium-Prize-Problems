**Proved range β_W < 1/12. Published range: mass gap β_W < 1/12 (SZZ 2204.12737), area law β_W < 1/6 (CNS 2509.04688). The published ranges are larger or equal; nothing new in the range. New: the pointwise (full or horizontal) Bakry–Émery method is capped at β_W < 1/8.**

# report.md — f1-strong (T63), Director Z4, principal Kirtus Justus

Control: control.txt = 0.272341 (−ln tanh 1).

## Verdict table
| item | verdict | evidence |
|---|---|---|
| H1 exact Hessian (β/2)[cos θ\|Y\|² + ⟨C,A⟩] | STANDS | derivation in STRONG_COUPLING.md §2; FD check P1, relative error 9.7e-6 ≤ 1e-5 |
| H2 sharp per-plaquette constant h(θ) = 2 sin(θ/2)(1 + sin(θ/2)) ≤ 4 | STANDS | eigen-decomposition of the Toeplitz matrix via the ansatz z⁴ = e^{−2iθ}; P2 error 4.9e-15 on 200 plaquettes |
| H3 Hess V ≥ −12β\|t\|² for all U, t (= SZZ (4.2) converted) | STANDS | H2 × 6 plaquettes per link; P4 32/32 configurations within the local bound |
| H4 π-flux has λ_min = −8β exactly | STANDS | Fourier argument; P3 L = 2, 4; child and grandchild FD give 7.99999866; spectrum rerun R1 |
| H5 horizontal restriction gives nothing at center-valued critical configurations | STANDS | critical-orbit argument; horizontal −8 on L = 2; one-link flip full = horizontal (M1) |
| any c < 12 (all directions or horizontal) | NOT CHECKED (MISSING proof) | per-plaquette route is sharp, so a global covariant-curl bound is needed; I have none |
| Theorem: Poincaré/LSI for β_W < 1/12, uniform in volume and boundary condition | STANDS (Bakry–Émery CITED) | SZZ Thm 1.4 and Cor 4.4/4.5; same range as SZZ |
| β_1 > 1/12? | DEFECT (of the hoped-for improvement) | not obtained; worst case π-flux, κ_H = 1 − 8β; ceiling of the method is 1/8 |
| published ranges table | STANDS for SZZ and CNS 2509.04688; NOT CHECKED for 2505.16585 and 2510.22788 | full text versus abstract only, see STRONG_COUPLING.md §1 |
| transfer-matrix gap from Cor 1.6 | NOT CHECKED | Cor 1.6's c1 depends on support sizes; the spectral step is CURVATURE_ROUTE S10 (CLAIMED there) |
| SU(N), N > 2, constant | NOT CHECKED | H2 uses Y² ∝ 1, which is special to SU(2) |

Verdict counts: STANDS 7 (one with a partial NOT CHECKED), DEFECT 1, NOT CHECKED 3.
Predicates (my programs, hess.py and rerun_child.py): met 6 (P1–P5, R1), failed 0, measured only 2 (M1, Haar statistics).
Register: checks K1 (hess-run1), K2 (child-run1) and K3 (rerun-child), all exit as expected.
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## Hypotheses used, and where each is stated
- SU(2), d = 4, V = −(β/2)Σ Re Tr Q_p, ⟨X,Y⟩ = −Tr XY, Ric = 1: brief; STRONG_COUPLING.md header.
- Normalization conversion β_W = 4β_SZZ (SU(2)): §header, from SZZ (1.2) and (1.3).
- H2 uses SU(2)-specific facts: Y² = −½\|Y\|²·1 and \|[X,Y]\| = √2\|X×Y\| (§2 H1, H2).
- H4 needs the π-flux configuration to exist: on Z⁴ or an even periodic torus (§2 H4). In a box with boundary conditions, the bound 1 − 8β is approached as the box grows (CLAIMED, not computed).
- H5 needs a critical configuration (center-valued links) (§2 H5).
- Theorem: Bakry–Émery for compact manifolds (CITED, SZZ Thm 1.4, Cor 4.4/4.5); finite box, any boundary condition (§3).
- Decay: SZZ Cor 1.6 under Ass. 1.1 (§3).

## Failed predicates
- None in my programs.
- The hoped-for statement "β_1 > 1/12" fails. This is a limit of the target method, not of my expectation: the per-plaquette constant is sharp at Q = −1, and the global truth is at least 8.
- Child's failures, kept in its results:
  - F1/F2: FD step too large for \|t\| ~ 14. The child's own expectation.
  - F2b: h² scaling invisible at the roundoff floor. The child's own expectation.

## What I did not check
- Any proof of c < 12. The gap between 8 (attained) and 12 (proved) is open.
- Whether sup c is exactly 8. Searches are not converged: mine stopped at 5.5–5.9 from Haar starts, the child's at ≤ 7.29.
- L ≥ 3 search.
- SU(N) with N > 2.
- The full texts of CNS 2505.16585 and Nissim 2510.22788.
- Osterwalder–Seiler.
- SZZ Sec. 4.3 in detail.
- The transfer-matrix step.
- Whether CNS's σ-model range transfers to a YM mass gap.
- Lean: not used. /home/user/z4-lean/READY exists, but I claim no Lean result.

## Delegated questions and outcomes
- **Child T69** (admitted under T63, released, event 142).
  - Question: item 4. Maximize c(U) = −λ_min(Hess V)/β, over all directions and horizontally, on the (Z/2)⁴ torus. Test the claims c ≤ 12 and c(π-flux) = 8.
  - Control (single plaquette Q = −1: 1 − 2β ×3, 1 ×9): graded **PASS** before I read anything else.
  - Outcome: c_max found 8 = c_H, at π-flux. 24 seeded random starts reached at most 7.29 and were not converged. 12 was never exceeded (771 configurations).
  - I reran its π-flux spectrum (−8:9, −6:36, −4:54, −2:36, 0:57) with my own code: R1 MET. This also matches my Fourier prediction.
  - Its random-start values are CLAIMED: I did not rerun them.
- **Grandchild T70** (admitted under T69 and released, according to the child).
  - Question: an independent pure-finite-difference recomputation of c at π-flux. Control passed according to the child.
  - Result: 7.99999866 for both the full and the horizontal value. The child reran it. I did not rerun the grandchild directly; the number is reproduced by my exact −8.

## Rerun commands
```
cd /home/user/z4-workers/f1-strong
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print('%.6f'%(-math.log(math.tanh(1))))"      # control
$P check --ws pcp --name hess-run1 --expect-exit 0 -- python3 hess.py result_hess_run1.txt   # (new name/file on rerun: mode "x"; ~325 s)
$P check --ws pcp --name rerun-child --expect-exit 0 -- python3 rerun_child.py result_rerun_child.txt
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-admit /home/user/z4-work/graph/attempt.jsonl --by principal --label f1-strong-child --parent T63
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-release /home/user/z4-work/graph/attempt.jsonl --by principal --id T69
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Note: hess-run1 took 324 s, slightly over the 5-minute guideline. That was the hill-climb part.
