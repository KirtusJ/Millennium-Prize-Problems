# a5-chalB: challenger report on PROOF_B.md (claim (B): SU(2), d = 4, m(β) → 0)

Worker a5-chalB for Director Z4. Principal: Kirtus Justus. 23 Nov 2026. I share a model family with the director and the builder, so my agreement is not independent review.

Control: `control.txt` = 0.272341 (−ln tanh 1). Lean READY exists.

**Bottom line.** I attacked every step and found no step that is false. Granting S3a–S3c, (B) follows. S3a's argument reproduces exactly: site-plane RP has an elementary proof, the image count is |Λ|/4 with multiplicity 4, the exponent is f(β/2) − f(β) − t/8, and the Z bounds check out. It also passes every numerical test, in 2D exactly and in 4D by Monte Carlo. S3b and S3c remain unproven soft-analysis claims, and their gaps are of rigour, not of substance. I found one defect, in the write-up of S3b: the boundary gauge fixing is circular as written, but it can be repaired. Nothing here upgrades S3b or S3c to "proved".

## 1. Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| A1 S1 spectral bound (ψ, ⟂Ω, inequality) | STANDS | ψ=(O_p0−⟨O⟩)Ω, θO=O (spatial plaquette in t=0 site plane, real class function), ⟨ψ,Tⁿψ⟩=Cov(O(0),O(ne₀)), T² ≥ 0 gives C(n) ≤ e^{−mn}C(0) for even n (notes step5) |
| A1 S2 reduction, need for −log c(n)/n → 0 | STANDS | m ≤ −log(C(n)/C(0))/n for every β; limsup m ≤ inf_n −log c(n)/n = 0 because c(n) ~ n⁻⁸ (free_G K1) |
| A1 normalisation by C(0) (contact terms) | STANDS | C(0) is the variance and appears on the right of the same exact inequality, so no contact-term issue arises |
| A2(i) RP in site planes, all 4 directions | STANDS (own proof; literature not read in full) | No plaquette straddles a site plane: e^{−S}=e^{−S₊}θ(e^{−S₊}), ⟨Fθ F⟩=∫dU_plane abs(∫F e^{−S₊})² ≥ 0. Source found only at abstract level (arXiv:1607.07126) |
| A2(ii) chessboard images and the factor 1/8 | STANDS | Recomputed: \|Λ\|/4 distinct images, each 4×; e^{−βS} ≤ e^{−βS/2}e^{−t\|Λ\|/8}. 1/8 is the choice ε=1/2 of rate ε/4 (not sharp). Chessboard theorem with face-supported functions cited from memory (FILS, Biskup), not read |
| A2(iii) Z upper/lower bounds and exponent | STANDS | ẑ=e^{−β}2I₁(β)/β (Haar density (2/π)sin²α); Haar(B_s) ~ (2/3π)s³ gives (9/2)log β per site; 6·8=48; C ~ e^{51}: finite, useless numerically |
| A2(iv) 2D exact | STANDS | K8: P(O>t) ≤ e^{−t/8} in 888/888 cases (C=1); P → Γ(3/2,1) tail, D(β) ≈ 0.12/β; child agrees (K10, rerun K11 byte-identical) |
| A2(iv) 4D MC 4⁴, 6⁴, β=4,8,16 | STANDS | 24/24 predicates met; C_emp=1.00 in all 6 cases; tail slope −1.93…−2.20 (Gaussian (1/4)χ²₃ rate 2 ≫ 1/8); control wβ/0.75 = 1.011–1.069 |
| A3(i) tightness of the gauge-fixed field | STANDS (as argument) | Only a finite R is used: a path product of O(\|R\|) plaquette holonomies, tight at scale β^{−1/2} in any d. Curvature is the primitive object, so d=4 is not needed here |
| A3(ii) DLR / Laplace uniformity | STANDS (as argument, unproved) | Uniformity is needed only on compacts of boundary data; tightness absorbs the rest. Free gauge action, unique flat orbit (H¹(R,∂R)=0) and a nondegenerate Dirichlet Maxwell Hessian were checked by hand; PROOF_B does not do these checks |
| A3(ii') boundary gauge fixing as written | DEFECT (write-up, repairable) | "Axial gauge in R∪∂R from a base point" makes the boundary data depend on interior links, so the DLR conditioning is circular. Fix: gauge-fix the boundary shell with a tree in the shell only |
| A3(iii) vortices, instantons, torons, Gribov copies | STANDS | Instanton weight e^{−2π²β}; a thick vortex sheet costs π²β/(2l²) per unit area, ~π²β/2 for a closed sheet of size l (scale-invariant, does not vanish). Local O_p ~ β/l⁴ is O(1) only for l ≲ β^{1/4}, at weight e^{−cβ}. No O(1) contribution at fixed n. Torons are flat, so they fall in the unique orbit. The axial tree gauge has no Gribov copies |
| A3(iv) Patrascioiu–Seiler superinstanton | STANDS (does not apply; abstract level) | arXiv:hep-lat/9311019: the effect starts at O(1/β²). The chain uses only the leading Gaussian order |
| A4 S3c(i) Gibbs classification for 1-forms | NOT CHECKED | Only the spectral step is checked: k̂²=0 ⇔ k=0 on the lattice, so a stationary L² harmonic h is constant. The decomposition F=ξ+h with h independent of ξ is not proved |
| A4 S3c(ii) inequality incl. background f | STANDS | Wick expansion checked by hand. Lean `s3c_ratio` (K4): exit 0, axioms [propext, Classical.choice, Quot.sound], no sorry. A background f only adds terms with ratio ≥ (G(n)/G(0))² |
| A4 G(n), c(n), decay | STANDS | K1: G(0)=0.500000, G(n)>0 for 17/17 n, π²n⁴G(n) → 1.020 (n=16), c(1)=0.019, c(4)=1.47e−6, c(10)=4.57e−10 (builder reproduced); −log c(n)/n falls from 3.97 to 1.58 → 0 |
| A5 finite G / Z₂ | STANDS (chain breaks where it should) | ẑ → 1/\|G\|; O_p ∈ {0}∪[βΔ,∞), Var → 0, limit δ₀: no nondegenerate Gaussian limit. The ratio limit needs Var_{μ∞} > 0, which fails at S3b/S3c, as PROOF_B says |
| A5 U(1) d=4 | STANDS | ẑ ~ β^{−1/2}; the chain gives m → 0, consistent with the massless phase (Fröhlich–Spencer, abstract level) |
| A5 hidden non-uniformity in volume | STANDS | S3a constants are uniform in L (L → ∞ first); S3b works at fixed R. Restriction: "every limit state" means every periodic-box limit (S0) |
| A6 S3a–S3c ⇒ (B) | STANDS | Logic checked end to end |
| A6 simpler route avoiding S3b | NOT FOUND | The spin-model trick needs an observable whose time step is controlled by the energy. Gauge-invariant local observables fluctuate at the energy scale; for Wilson loops the tube flux is of the same order as the loop's own fluctuation (perimeter law). Block sums are short-distance dominated |

Counts (predicates in my programs, plus graded controls and the rerun identity): **met 38, failed 0, measured only 14**.
- Met: free_G 6, mc4d 24, tail2d 4, Lean 1, control 1, child-control grading 1, child-rerun identity 1.
- Measured only: R1 and R2 in 6 MC cases (12), plus C_emp and slope as reported values (2).
- Verdict items: STANDS 17, DEFECT 1, NOT CHECKED 1, NOT FOUND 1.

## 2. Hypotheses each statement uses, and where they are stated

- S0: time-reflection RP (PROOF_B §1 S0; my site-plane proof in notes step6), OS reconstruction, compactness, translation invariance of periodic limits.
- S1: T self-adjoint from site RP plus translation invariance (θτ = τ⁻¹θ); T² ≥ 0; only even n are used (S1, notes step5).
- S2: C_β(0) > 0 (S2), and c(n) > 0 with −log c(n)/n → 0 (K1).
- S3a: site-plane RP in 4 directions on the even torus; a chessboard theorem for closed blocks with face-supported functions (cited from memory); temporal gauge; Jensen; β ≥ 2; L → ∞ before β → ∞ (S3a, notes step6).
- S3b: DLR property of periodic limits; tightness from S3a; a boundary gauge fixing using shell links only (my repair); Laplace on compacts (free gauge action, unique flat orbit, nondegenerate Hessian); continuity of the Gaussian kernel (S3b, notes step9).
- S3c: decomposition F = ξ + f with f a constant independent of ξ (CLAIMED, not proved); G(n) ≥ 0 and G(n) ≤ G(0) (K1); uniform integrability from S3a (S3c, notes steps 2 and 7).

## 3. Failed predicates

None of my predicates on the target failed. Failures of process, none of them a defect of the target:
- My smoke test (mc4d 4⁴, 15 sweeps, scratch file, not registered): M1 "FAILED" because 10 sweeps cannot fill 20 bins (σ = nan). This was my own setup.
- Child run 1 (`tail.py`) exceeded its 1-minute limit (its own performance defect) and was rerun as tail2/tail3.
- The grandchild's script lived in /tmp/claude-0/mc.py, outside grandchild/. This breaks the rule; its number was recomputed independently twice (child, my K8).
- The child's recall of I₂(1)/I₁(1) before computing (~0.136) was wrong. That was its own expectation; the computed value is correct.

## 4. What I did not check

- S3c(i): the 1-form Gibbs decomposition.
- A written proof of S3b's Laplace uniformity: only the ingredients were checked by hand.
- The chessboard theorem's statement for gauge link variables (from memory).
- Full texts of OS78, FILS, Seiler LNP 159, Jaffe–Janssens, Patrascioiu–Seiler and David (search listing or abstract level only).
- The O(β⁻²) coefficient used in the M1 tolerance (from memory).
- Monte Carlo autocorrelations, beyond 20-bin errors on w.
- Lattices larger than 6⁴; β > 16 in 4D.
- Free-field c(n) for n > 16.
- Strong-coupling and other non-periodic DLR states.

## 5. Delegated questions and outcomes

- **Child** (child/, sonnet, headless, register K10, exit 0, 275 s). Question: A2(iv) in 2D, the exact tail P_β(β(1−cos α) > t) ≤ C e^{−t/8} for β ∈ {2,…,256}, t ≤ 40. Control I₂(1)/I₁(1): it answered 0.240194, **correct**, graded first.
  - It returned: STANDS, 888/888 cases, C_emp = 1 at t = 0; rates 0.92–1.66; sup abs(P − Γ(3/2) tail) ≈ 0.11 → 4.5e−4.
  - I reran its tail3.py in scratch (K11): the CSV is byte-identical. I recomputed independently with a different substitution (K8): all agree.
- **Grandchild** (child's sub-agent). Question: independent P₈(O > 4). Control ∫₀^π sin² = 1.570796: **correct**.
  - It returned 0.03988840 (Gauss–Legendre) and 0.039959 ± 0.000138 (Monte Carlo).
  - Mine (K8): 0.0398883992. It agrees.

## 6. Rerun (from /home/user/z4-workers/a5-chalB; result files open with mode "x", so delete or rename them first)

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')" > control.txt
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name free_G --expect-exit 0 -- python3 free_G.py free_G_result.json
./run_mc.sh     # = for L in 4 6, b in 4 8 16: $P check --ws pcp --name mc4d-L$L-b$b --expect-exit 0 -- python3 mc4d.py $L $b 200 $NM $((1000+10*L+b)) mc_L${L}_b${b}.json  (NM=2000 for L=4, 1000 for L=6)
$P check --ws pcp --name lean-s3c --cwd /home/user/z4-lean --expect-exit 0 --timeout 600 -- bash -c "PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/a5-chalB/S3c_ineq.lean"
$P check --ws pcp --name tail2d_recheck --expect-exit 0 -- bash -c "python3 tail2d_recheck.py tail2d_result.json > tail2d_out.txt 2>&1"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name child-tail3-rerun --cwd <scratch dir containing a copy of child/tail3.py> --expect-exit 0 -- sh -c "python3 -I tail3.py > out_tail3.txt 2>&1"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Register: K1 free_G, K2/K3/K5 mc L=4 β=4/8/16, K6/K7/K9 mc L=6 β=4/8/16, K4 Lean, K8 tail2d_recheck, K10 child-run1, K11 child-tail3-rerun.
- Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Last line of the Rust verify: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

Sources consulted, abstract or listing level only; fetched text is not stored here:
- arXiv:hep-lat/9311019, Patrascioiu–Seiler (abstract): the effect starts at O(1/β²).
- arXiv:hep-lat/9402003: title only.
- arXiv:hep-lat/9504017, David: abstract.
- arXiv:1607.07126, Jaffe–Janssens: search snippet only.
