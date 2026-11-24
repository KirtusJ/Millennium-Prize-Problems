OVERALL VERDICT: I did not falsify the mixed-score argument. All 6 items STAND (6 STAND, 0 DEFECT, 0 NOT CHECKED). The proof gives an absolute floor J_s(F) >= 1/(165888 beta^2) for beta >= 1. It is not a floor on the ratio J/Var (see the caveat below).

Worker e2-score, task T229. Child T232, grandchild T234. The director and I are the same model family, so my agreement is not independent review.

## Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| (1) last corner Y_3, mixed derivative = A_ab/4 in colours 0,2,3 | STANDS | From replicas.rs: g3 = U_x(0,0)·w·[v·U_y(2,1)·U_x(1,2)*·z*]·w*·U_x(0,0)*, so the free content is {w+,v+,z−,w−} (G1). Colour 3 updates (v,z) and not w (G2). Y_3 has the form Re(B'·v·Q·z*·R) (G3). FD check: other marks' mixed derivatives are exactly 0 and Σ(DEY_j)² = 2+Y_j² on the actual marks, err 7.5e-8 (B1). Holds in 81/81 cells × orientations (H1). |
| (2) Σ_ab A_ab² ≥ 2 pointwise | STANDS | Exact identity Σ A_ab² = 2 + Y², err 3e-15 on 1e5 samples, min 2.000000 (A1). Proof: A = −(3×3 imaginary block of the 4×4 orthogonal map x ↦ M w x N C u). Frobenius² = 4 − 1 − 1 + O_00², and O_00 = Y. |
| (3) ‖Z‖ ≤ 72β (β ≥ 1) | STANDS | The step is the second-moment adjoint identity ‖D*b‖² = ‖Db‖² − ∫(Ds)b², not a sup bound on s·t. I checked it line by line. Per (a,b): ≤ (√(1+6β)+β)² + 6β(1+6β); the max of this over β² is 55.29, at β=1 (C1). So each term is ≤ 8β, and the triangle inequality over 9 terms gives 72β. Numerically ‖Z‖/β ≤ 6.90 (20 exteriors) and → √6 with zero staples. |
| (4) IBP, E Z = 0 | STANDS | ⟨1, E*D*A⟩ = ⟨DE1, A⟩ = 0; the group is compact and the density is smooth and positive. Quadrature: E Z = 1e-14 and E[(Y−EY)Z] = E[2+Y²] to 1e-10 (C2). MC within 4 SE in 20/20 cases (child; I reran it). |
| (5) counting 3/24 → 1/(165888β²) | STANDS | replicas.rs: j += (f−g)²/48 summed over 24 colours, so J = (1/24)Σ_c E Var_c. Colours 0,2,3 give 3 × 1/(20736β²). 8·20736 = 165888. Floors: 5.616449e-7 (β=3.276133577) and 5.215257e-7 (β=3.399810242). |
| (6) family J(Σ a_l F_l) ≥ Σ\|a_l\|²/(165888β²) | STANDS | In all 24/24 colours the selected pairs are disjoint and no 4D plaquette meets two pairs; 648/648 pairs share exactly one face (G4). So the cross terms vanish exactly (diagonal.md), and each cell's F_l obeys the floor (H1, 81/81). The coefficients are fixed on the skeleton fibre. |

Counts over all predicates: 13 met, 0 failed, 3 measured only (colour-1 mixed-derivative excess, B2 colour-1 Σ(4DEF)², the zero-staple Var ratios).

## Hypotheses each statement uses, and where they are stated
- Site indexing x = c0 + n·c1 + n²·c2 + n³·t, and the action exp(β Σ Re U_p) with 6 plaquettes per link in 4D: replicas.rs, frozen() and draw(). wilson_mc.rs is not in my directory, so I could not check these. That is an assumption of mine.
- Frozen links are the spatial links on slice 0 whose other two spatial coordinates are even: replicas.rs frozen(), fixed.md. B is the xz coarse face, built from frozen links only: fixed.md.
- Colour pairs (the odd-y x-link and the odd-x y-link of each plaquette): replicas.rs colours().
- β ≥ 1, used for √(1+6β) ≤ √7·β: score.md (coarse-plaquette-floor).
- |Ds| ≤ 6β and |Es| ≤ β (one shared face): score.md.
- |A|, |DA|, |EA|, |DEA| ≤ 1, from quaternion products: score.md.
- J is defined with the raw exterior (pointwise in the off-slice environment) and with exact two-copy colour refresh: fixed.md, diagonal.md.
- Factorization of each colour over its pairs: diagonal.md. I checked it here (G4).

## Failed predicates
- Target: none.
- My own failures, all kept:
  - Docstring G1 first expected g0 = {u+,w+}. That was my mistake (u enters P(0,0) conjugated). I corrected it before the first run, and orientation does not matter to the claim.
  - Run e2b-run1 (K2) exited 1. My helper slice pulled in code that used an undefined `pred`. Fixed in e2_lib2.py and rerun as K4 (PASS).
  - The child's first run K1 exited 1 on a JSON serialization bug in its own code. That was its defect, not the target's.

## Caveat for the auditor (not a defect of the stated claim)
- The floor is absolute, about 5.6e-7. The measured J_4 is 7e-4 to 3e-3, so the bound is 3 to 4 orders of magnitude slack.
  - In the pair model the slack grows with β: Var(Y/4)·20736β² ranges from 240 to 23845. Var falls roughly like β^-0.9, not β^-2.
- A relative floor J/Var additionally needs an upper bound on λ_max(D^-1/2 C D^-1/2). diagonal.md and score.md both say this is open. Nothing here bears on it.
- Colour 1 cannot be credited this way: there Σ(4·DEF)² can be as low as 0.46 < 2 (B2). The auditor does not credit it.

## What I did not check
- The conditional sampler in replicas.rs (the exactness of the β ≥ 8 envelope draw), the fixed.md numbers, and the measured J_4 values.
- wilson_mc.rs. It is absent, so the indexing and the 6-plaquette staple are assumed.
- Lean: /home/user/z4-lean/READY exists, but I did not use Lean, so there is no Lean result.
- Off-slice / temporal colours. colours() iterates only x < n³ (slice 0). I assumed this is the intended slice.
- Coverage limits: geometry was checked on n=6 only, and the numerical ‖Z‖ on 5 random exteriors × 4 β (|h| ≤ 5). The uniform statement rests on the analytic inequality, which I checked by hand and with C1.

## Delegated questions and outcomes
- **Child T232** (admitted under T229, released after return). The question was the numerical ‖Z‖_{L²(μ)}/β, E Z, the IBP identity, and Var(Y) vs the floor, for β ∈ {1, 3.3, 10, 30} with 5 exteriors each.
  - Control (6∫x²−1 = 1): its answer was 1.000000, correct. I graded this first.
  - Result: exact heat-bath Gibbs, 1e5 samples per case. Max ‖Z‖/β = 6.898 and min ratio = 240.3. All 20/20 cases pass.
  - I reread its Z expansion (zscore.py lines 58–64); it is identical to mine. I reran it in rerun_child/ (K5) and got identical numbers.
- **Grandchild T234** (parent T232). The question was the zero-staple case at β=1, recomputed independently by importance sampling (2e6 samples).
  - Result: ‖Z‖/β = 5.1337. My 1-D quadrature gives 5.1336, and the IBP identity holds (z = −0.16).
  - The child reran its check.py.

## Exact rerun commands
```
cd /home/user/z4-workers/e2-score
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name e2-run2 --expect-exit 0 -- python3 e2.py e2_run2.txt
$P check --ws pcp --name e2b-run3 --expect-exit 0 -- python3 e2b.py e2b_run3.txt
$P check --ws pcp --name e2c-run2 --expect-exit 0 -- python3 e2c.py e2c_run2.txt
mkdir rerun_child2 && cp child/zscore.py rerun_child2/ && $P check --ws pcp --name child-rerun2 --cwd rerun_child2 --expect-exit 0 -- python3 zscore.py
(cd child/grandchild && mkdir ../../rerun_gc && cp check.py ../../rerun_gc/ && cd ../../rerun_gc && python3 check.py)
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Result files are opened with mode "x", so use new names. Seeds are fixed: 20261124 and 7 (e2.py), 11 (e2b.py), and 100+e / 10000(bi+1)+e (zscore.py).

Register last lines:
- `$P verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

## For the auditor
I tried to falsify the claim in the order you asked, and failed on every point.
- **Transported last corner.** It is exactly as you state: w enters twice, via the transport out and back, and v and z once each. Colour 3 never moves w, so Y_3 is bilinear in (v, z).
- **Three-colour counting.** It is exact (1/48 per squared difference = (1/24)·Var per colour), and the colour factorization holds for all 24 colours.
- **‖Z‖ ≤ 72β.** This is the place most likely to break, and it holds. The proof avoids the dangerous s·t·A term through the identity ‖D*b‖² = ‖Db‖² − ∫(D²log ρ)b², which absorbs s² exactly.
- **Not proved.** The argument gives no relative (J/Var) floor and no uniformity under refinement.
