# m1-wild (T128) report: the two-direction rung, checked by a third method and read as a 2+1-dimensional regime

Worker m1-wild, child of Director Z4. Brief: wildcard, seed word "ledger". Control: `control.txt` = 0.272341 (−ln tanh 1).

## The one thing

**Statement.** The two-direction continuum operator of sec_smallbox.tex,
h₂ = −½(Δ₁+Δ₂) + 2|x₁×x₂|² on rotation-invariant L²(ℝ³×ℝ³), was recomputed here by a third method: a Legendre × 3D-oscillator radial basis with dense diagonalisation in each l-parity sector. The folder's two methods were the Peter–Weyl lattice method plus continuum Rayleigh–Ritz, and Nyström/Lanczos. The results:

| quantity | paper (Table sb:tab-num) | here (L=28, N=22; change from L=22, N=18) |
|---|---|---|
| e₀ | 3.3505330 | 3.35053304 (1·10⁻⁸) |
| e₁ = e₂ (doublet) | 5.3254970 | 5.32549702, split 1·10⁻¹⁰ (1·10⁻⁸) |
| e₁ − e₀ | 1.974964 | 1.97496398 |
| **first excited charge-0 (scalar) level** | **not given** | **5.72540816; scalar gap 2.37487512** |
| next levels | not given | 7.1265747 (doublet), 7.2365582 (doublet) |

So three numbers in the paper are confirmed by an independent method, to 8 digits. A fourth item was left open in the paper: "that [the doublet] lies below the first excited scalar level rests on the numerics." It now rests on two methods, and the margin is wide. The first nondegenerate level above e₀ is 0.400 above the doublet. A nondegenerate level must have O(2) charge 0, because charges ±q pair up under the reflection x₁↔x₂.

**Proposal (the part worth the director's attention).** The paper treats h₂ only as the one-site, k = 2 member of a family whose physical case is k = 3. But h₂ is exactly the lowest-order constant-mode Hamiltonian of SU(2) on a small *spatial 2-torus in 2+1 dimensions*. There the spatial gauge field has two components, and the constant modes A₁, A₂ ∈ su(2) are x₁, x₂.

The paper's own heuristic derivation (sb:sub-why, with L³ replaced by L²) gives H = (βL²)^(−1/3) h₂ on an L² spatial torus. In that setting the O(2) that mixes x₁ and x₂ is the *spatial rotation group*. The doublet of "charge two" is then the spin-2 glueball, and the 2.374875 level is the 0⁺ scalar.

So the k = 2 rung has the same standing as the k = 3 rung: it is the lattice form of the known small-volume regime, here in 2+1 dimensions. I propose to:

1. Say this in sec_smallbox, "Two directions".
2. Add the scalar gap 2.374875 and the second and third levels to Table sb:tab-num.
3. Redirect the search behind "nor a published spectrum of h₂" to the 2+1-dimensional small-volume literature. The candidate I found and did not read: García Pérez, González-Arroyo and Okawa, arXiv:1211.0807, which announces a companion paper "Small volume physics in the 2+1 dimensional Yang–Mills theory". That is where a published h₂ spectrum, normalised as above, would be found or found missing.

**Evidence.** `h2spec.py`, register check K2 (`h2spec-run1`), result `h2spec_result1.json`. Predicates P0–P5 were fixed in the docstring before the run: 6 met, 0 failed. Truncations (16,14), (22,18) and (28,22) agree to 8·10⁻⁷ on the lowest 6 levels, and the basis orthonormality error is 3·10⁻¹⁴. The 2+1-dimensional reading is a derivation on paper, not a program result. The literature search was two web searches plus one reading of the abstract and HTML of hep-lat/9608101 and arXiv:1211.0807 through a fetch agent. Neither contains h₂ or its eigenvalues: 9608101 is the three-sphere; 1211.0807 gives one-loop electric-flux energies. "Not found" is weak evidence.

**What this does not do.** It says nothing about Hypothesis (A). The 2+1-dimensional reading is at fixed volume, exactly like the 3+1-dimensional one.

## Smaller observations (one line each)
1. G(n) re-derived independently (child T130 and grandchild T131, reran by me): G(0) = 0.5, G(1) = 0.0688747458, π²n⁴G(8) = 1.0924. These match sec_proof.tex:505 ("G(1)=0.0688747, π²n⁴G(n)=1.092 at n=8"); n²(π²n⁴G−1) falls from 8.47 at n=4 to 5.92 at n=8, consistent with the stated O(n⁻⁶).
2. The tail bound e^{60.2−t/8} (Lemma 3, Cor. pf:cor-tail) is vacuous at every t ≤ 2β when β ≤ 240, since O_p ≤ 2β. It is correct and serves only uniform integrability as β → ∞, but readers may misread it as quantitative.
3. By hand, the scalings in sec_smallbox are consistent: h = β^(−1/3), H = (βL³)^(−1/3)h₃, the 4^(1/3) change of normalisation, e′ = 4^(−1/3)e, and 3.012539/2 = 1.5063 on 2³. So is the Wick inequality with a constant background: it needs exactly G(n) > 0.

## Verdict table
| item | verdict | evidence |
|---|---|---|
| e₀(h₂) = 3.3505330 | STANDS | 3.35053304, third method, K2 |
| e₁(h₂) = 5.3254970, exact doublet | STANDS | 5.32549702, split 1·10⁻¹⁰, K2 |
| e₁ − e₀ = 1.974964 | STANDS | 1.97496398, K2 |
| doublet below first excited scalar ("rests on numerics") | STANDS | scalar level 5.725408 > 5.325497, margin 0.40, K2 |
| G(0) = ½, G(n) > 0 (n ≤ 8), π²n⁴G → 1 | STANDS (n ≤ 8, measured) | child g130.py, my rerun K3 gives identical numbers; grandchild G(1) agrees to 1·10⁻¹² |
| G(n) = π⁻²n⁻⁴ + O(n⁻⁶) as n → ∞ | NOT CHECKED (asymptotically) | trend only, n ≤ 8 |
| h₂ = 2+1D small-torus constant-mode Hamiltonian; doublet = spin 2 | NOT CHECKED by program | derivation on paper, parallel to sb:sub-why |
| "no published spectrum of h₂" | NOT CHECKED | 2 searches and 2 papers read, none has it |

Counts: met 6 (my P0–P5) + 5 (child, reran) = 11; failed 0; measured only 2 (child's asymptotic trend; my convergence estimate is self-consistency, not a bound).

## Hypotheses each statement uses
- h₂ spectrum: the 3D oscillator radial functions with l = 0…28 and n < 22 span the low states well enough, judged by convergence between truncations (h2spec.py docstring). Quadrature on [0, 9] with 600 Gauss–Legendre points; truncation beyond r = 9 is checked only through the orthonormality error of 3·10⁻¹⁴. Charge assignment: nondegenerate means charge 0. The doublet's charge 2 is taken from the paper; my program shows only that it is degenerate.
- G(n): the child's exact k₀ integral (the hint), which it checked against a brute 4D grid at n ≤ 2; cubic symmetry; an h⁴ Richardson extrapolation (child report, "Hypotheses used").
- 2+1D reading: the constant-mode truncation and T ≈ e^{−H}, as in sb:sub-why. Heuristic.

## Failed predicates
None of mine. The child reports none. Its P_c1 ("decreasing toward 1") was not tested in code, and the sequence rises from n=2 to n=3. That is a slip in the child's own expectation, not a defect of the target.

A process failure of my own: the first version of h2spec.py imported scipy, which is absent. It failed before any result was written and was rewritten to use numpy only. That run was not in the register.

## What I looked at and what I did not
Read: README, THEOREM_B.md, paper/main.tex, sec_reduction.tex (§1–2), sec_smallbox.tex in full, Def. pf:def-G, grep hits in A3_NOTES §7–9 and reviews_index j1-micro and i1-tunnel. Not read: A1_REDUCTION, the A1 and A2 ledgers beyond grep, GROUNDING beyond grep, sec_negative, sec_general, sec_provenance, the Lean files, most of reviews_index, and C4's or the Codex groups' proofs. Not checked: the 3-direction numbers, the tunnelling constant 4.6054, D* = 60.19, any proof step.

## Delegated questions
- Child T130 (admitted under T128, released): compute G(n), n ≤ 8; check G(0) = ½, positivity, π²n⁴G → 1. Control ∫₀¹x² = 0.333333, answered correctly; I graded it first. Outcome: as in smaller observation 1. I reran its program in a fresh directory: identical numbers.
- Grandchild T131 (admitted under T130 by the child, released by it): G(1) by a Schwinger/Bessel integral, 0.0688747458405, agreeing to 1·10⁻¹². Control ∫₀^{π/2}cos = 1.000000, correct. The child reran it. I did not rerun it; I used only the agreement with the paper's value.

## Rerun commands
```
cd /home/user/z4-workers/m1-wild
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name h2spec-run1 --expect-exit 0 -- env OMP_NUM_THREADS=1 python3 h2spec.py h2spec_result1.json   # result file must not exist (mode "x"); ~107 s
mkdir -p child_rerun && cp child/g130.py child_rerun/
$P check --ws pcp --name child-g130-rerun --cwd child_rerun --expect-exit 0 -- env OMP_NUM_THREADS=1 python3 -I g130.py   # remove child_rerun/g130_result.txt first
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Last lines of the verifies:
- Python: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Task graph: T128 (mine), T130 (child, admitted and released), T131 (grandchild, admitted and released by the child).
