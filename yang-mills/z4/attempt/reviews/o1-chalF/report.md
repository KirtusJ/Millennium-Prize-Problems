I could not break the proof of Lemma F (η-form) in LEMMA_F.md: every step holds; the only defect is one wrong sentence in the header ("M_in, M_out … → 0"; M_in actually → 1), which §3(b) of the same file already states correctly.

Worker o1-chalF, task T140, challenger. I share a model family with the author (n1-lemF) and the director, so my agreement is not independent review. The steps were re-derived by hand (my derivations are in the evidence column), then checked numerically with my own program `chal_F.py` (runs 4 and 5) and against a lower-tier child (T142) and its grandchild (T143).

## Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| I1 kernel e^{β⟨U,U'⟩}/Z, = e^β e^{−β\|U−U'\|²/2} | STANDS | ½tr(U⁻¹U') = ⟨U,U'⟩ for unit quaternions, and \|U−U'\|² = 2−2⟨U,U'⟩ |
| I2 Z = 2I₁(β)/β | STANDS | re-derived (integration by parts); Q1 passes at β=1,64,1024 (rel < 1e-9). At β=4096 my coarse quadrature fails (see failed predicates) |
| I3 dU = d²w dφ/(2π²), φ'-integral → 2πI₀(βRR'), prefactor 1/(πZ) | STANDS | δ(√(ϱ²+r)−1)ϱdϱ = 1; total 2π² = \|S³\|; my Nyström operator built from it reproduces ε_eff from the Legendre reduction to < 1e-7 (Q7, 24/24) |
| I4 Schur/Barta: ψ>0, Fψ ≤ λψ ⇒ ‖F‖ ≤ λ | STANDS | the brief's worry: ψ = e^{−βαr/2} ∈ [e^{−βα/2},1] is bounded and bounded below on compact S³, so ψ, 1/ψ ∈ L^∞ ⊂ L² and no truncation is needed. Cauchy–Schwarz + Tonelli (nonnegative integrands) + kernel symmetry is complete. Discrete check Q9: λ ≤ max B, 24/24 |
| I5 flat fixed point, log A = 2 asinh s | STANDS | re-derived Gaussian integral (precision βA, mean w/A, bracket α/2−s²−c/A = 0); Lean `fixed_point`, `two_arsinh_eq_log` re-run exit 0; Q4 |
| I6 e^{−z}I₀(z) ≤ H̃_δ(z) | STANDS | [0,δ] Gaussian extended to [0,∞) gives [2πz(1−5δ²/48)]^{−1/2}; [δ,π] gives ((π−δ)/π)e^{−z(1−cosδ)} ≤ e^{−z(1−cosδ)}; Q2 on 2400 points, max ratio 0.99988 |
| I7 I₁(z) ≥ e^z(1−1/(2z))/√(2πz) − ½ | STANDS | re-derived (both factors ≥ 0 only for t ≤ √2 < π/2; negative tail beyond π/2); Q3, min margin 1.6e-9 > 0 |
| I8 AM–GM (1−r)(1−r') ≤ RR' ≤ 1−(r+r')/2 | STANDS | Lean `amgm_pair` exit 0; Q5 |
| I9 Φ(r) ≤ −(r²/64)(1−A⁻²)² | STANDS | own derivation: g(1)=0, g'(1)=γ=(r/2)(1−A⁻²) < ½, g'' ≤ 1/μ³ ≤ 8 on [½,1], step h=γ/8 gives −γ²/16. Q6: true Φ / bound ∈ [8.02, 64] (the bound is ≥ 8× conservative). Lean covers only `weak_duality` and the trivial identity `quad_step`, not g''≤8 or Taylor |
| Thm 1 inner region (r ≤ τ) | STANDS | uses the I₀ UPPER bound only (via I6+I8, with H̃ decreasing and RR' ≥ (1−r)(1−r')) and the I₁ LOWER bound only (for 1/Z); 1/√z prefactor and AM–GM correct; extension from the disc to R² is legitimate (nonnegative integrand, indicator ≤ 1); the tail P(\|W'−w/A\| > √τ) = e^{−βAτ/2} is exact for a 2-D Gaussian. Q11in 18/18, margin ≥ 0.615 nat at β=4096 |
| Thm 1 outer region (r > τ) | STANDS | I₀ ≤ e^z; w·w' ≤ ρ\|w'\|; q=(R',\|w'\|) unit; area π; prefactor β e^β/(2I₁) ≤ β√(2πβ)/(2D). Q11out 18/18; pointwise B ≤ bound with margin 5.6–14 nats, including ρ = 0.99, 0.999, 0.9999, 1 |
| Thm 1 combined bound ‖F‖ ≤ A⁻¹max(M_in, A M_out) | STANDS | Q10: holds in all 18 qualifying cases (β ∈ {256,1024,4096} × 6 s), compared with the exact ‖F‖ (Legendre and Nyström agree to 10 digits). β=64 does not satisfy the hypotheses (τ=¼ ≥ 1/5, so M_in=∞): measured only, trivially valid |
| Corollary (a): ε_eff ≥ 0, so for s ≤ η/2 the claim holds | STANDS | ‖e^{−V/2}‖ ≤ 1, ‖K‖ ≤ ∫k = 1, and 2asinh s ≤ 2s ≤ η |
| Corollary (b): uniform on [η/2,1] with τ=δ=β^{−1/3} | STANDS | M_in does not depend on s (its A-term is ≤ e^{−βτ/2}); log M_in = O(β^{−1/3}) → 0; A M_out ≤ 5.83·β^{3/2}√(2π)/(2D)·exp(−β^{1/3}(1−(1+η)⁻²)²/64) → 0, uniformly in s, because A ≥ 1+2s ≥ 1+η. So log max → 0⁺ |
| Header line "M_in, M_out of Theorem 1, which → 0 uniformly" | DEFECT (wording, repairable) | false as written: M_in → 1 and A·M_out → 0. What tends to 0 is log max(M_in, A·M_out). §3(b) states it correctly. Fix: "log max(M_in, A·M_out) → 0" |
| brief's question: small s₀, gain ≈ r²s²/4 | STANDS (not uniform as s₀ → 0, and not claimed to be) | 1−A⁻² ≈ 4s, so the exponent is ≈ β^{1/3}s₀²/4, against (3/2)log β: this needs β^{1/3} ≳ 6 log β/s₀². Fine for fixed s₀; the η-split handles s < s₀. This is why β₀ is huge |
| claim β₀(0.2) "≈ 10¹⁴ (estimate)" | STANDS (order of magnitude) | the first grid point (10^{k/20}) with max over s∈[0.1,1] of the deficit ≤ 0.2 is β = 2.24e13, worst s = 0.1. Quoted deficits reproduced: 24.94 (quoted 24.9) at s=0.1, β=1e12; 5.4e-4 (quoted 5e-4) at s=1, β=1e11 |
| claim "at β ≤ 4096 valid but useless, deficit 6.5–14" | STANDS (with a clarification) | valid in 18/18 cases; my deficits are 8.58–14.23 nats with τ=β^{−1/3}. The quoted 6.5 is from β=64 with τ=0.15 (author's check_lemF.py line 165), not τ=β^{−1/3} |
| §4 numerics (−log B_sup ≤ ε_eff; −log B_sup − ε = −O(1/β)) | STANDS | β=4096: −4.1e-4 (s=0.1) to −1.95e-4 (s=1); β·(ε_eff−ε) ∈ [−1.14, −0.65] over all 24 cases; agrees with TUNNEL_THEOREM §1(iii) |
| §5 rate (log β/β)^{1/4} | NOT CHECKED | tagged CLAIMED by the author; outside the lemma |
| Lean (LemmaF.lean: 5 decls; Tunnel.lean: 2 decls) | STANDS | rerun from /home/user/z4-lean (READY present): exit 0, no sorry, axioms only propext, Classical.choice, Quot.sound |

Step counts: 17 STANDS, 1 DEFECT (wording only), 1 NOT CHECKED.
My program predicates (unique across runs 4 and 5): 172 met, 1 failed, 36 measured only. The 36 are: 24 values of β·(ε_eff−ε), the 6 β=64 cases of Q10 and Q11 that do not meet the hypotheses, and 6 summary quantities (the Q2/Q3 margins, Q6 slack, the quadrature change, β₀, and the deficit range).

## Hypotheses each statement uses, and where they are stated

- I2/I3/I1: β > 0, Haar = normalised surface measure (LEMMA_F §0, TUNNEL §0).
- I4: kernel symmetric and ≥ 0; ψ > 0 measurable, with Fψ ≤ λψ everywhere (§1 I4). The L² / boundedness of ψ is not stated but is automatic (compact space, continuous ψ > 0).
- I6: 0 < δ ≤ 1, z > 0 (§1 I6; the δ ≤ 1 comes from the hypothesis of Mathlib `cos_bound`).
- I7: z > 0; D > 0 is needed and holds for β > 1 (D(1) = 0.039) (§1 I7; Thm 1 assumes β > 1).
- I8: x, y ∈ [0,1].
- I9: unit q, μ > 0, c ≥ 0; the Taylor step needs γ < ½ (so 1−γ/8 ∈ [½,1]) (§1 I9).
- Thm 1: β > 1, s ∈ (0,1], 0 < τ < 1/5, 0 < δ ≤ 1 (§2). With τ = β^{−1/3} this requires β > 125. This is stated in §3(b).
- Corollary: η > 0, s₀ = η/2, s = sin a ∈ [0,1] (§3).

## Failed predicates (kept)

1. Q1 at β=4096 (runs 4 and 5): Z = 2I₁/β against my composite Gauss–Legendre quadrature (16 panels on [0,π]), relative error ≥ 1e-9. **My own defect**: the peak has width ~1/64 and is under-resolved. It is not a defect of the target: the same identity passes at β = 1, 64, 1024, and it is an exact derivation.
2. Runs that crashed (no result file, recorded in the register): run1 (scipy not installed), run2 (NaN from negative trapezoid noise in l_n), run3 (log of an underflowed B). All three are **my own defects**. The predicates were not changed. Run3's printed rows before the crash already agreed with runs 4 and 5.
3. Measurement caveat (my own): the "quad max rel panel-refinement change" of 0.11 at β=4096 is an overestimate. My metric divided by a partial sum. My pointwise log B values agree with the child's converged values to 6.8e-13 at 87 common points.
4. Child: its P4 failed (relative change of B on underflowed numbers). This was the child's own predicate design; it was fixed in its log-form barta2.py (108/108).
5. My child-rerun K9 failed (I ran `python3 -I`, which blocked the child's local import). This was my invocation error. K11, without -I, passed.

## What I did not check

- The §5 rate claim (CLAIMED by the author).
- TUNNEL_THEOREM beyond its use of Lemma F (Lemma K, Agmon (A)/(B), §5–7).
- Lemma R's Perron–Frobenius/invariance argument as a proof. I used it only through two numerical routes that agree: Legendre, and my own radial Nyström operator. Both assume that the top eigenvector is radial.
- Exact β₀ beyond a 10^{1/20} grid, and s on a 0.01 grid only.
- I did not access DLMF; I did not need it.

## Delegated questions and outcomes

- **Child T142** (admitted under T140, released): compute the Barta ratio B(ρ) by 1-D quadrature for β ∈ {64,256,1024,4096}, s ∈ {0.1,0.3,1}, at 9 values of ρ up to 1. Its control was I₀(1) to six decimals. **Graded first: 1.266066, correct.**
  - Result: 108 values of log B (res_log.csv) and a table of −log sup B.
  - My rerun of its barta2.py (K11) gives a byte-identical res_log.csv. Its values agree with my independent quadrature to 6.8e-13 in log B at 87 common points. The child made one stray write outside its directory (/tmp/claude-0/rerun) while rerunning its grandchild.
- **Grandchild T143** (admitted by the child under T142, released): independent recomputation of B(0; β=64, s=0.3). Its control was ∫₀¹x²dx = 0.333333, correct.
  - Returned 0.5576952560. My rerun of gc.py (K10) gives the same value, converged to 1e-14. This matches the child's log B = −0.583942602 (exp = 0.5576953).
- My own task-graph records: child admit event 284 (T142), release event 292.

## Records

- `pcp_os.py verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- The register has 11 checks: K1/K2 Lean, K3 child, K4–K8 chal_F runs 1–5, K9–K11 reruns of the child and grandchild.

## Exact commands to rerun

```
cd /home/user/z4-workers/o1-chalF
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"        # control: 0.272341
$P check --ws pcp --name lean-LemmaF_copy --expect-exit 0 --cwd /home/user/z4-lean -- bash -c "PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/o1-chalF/lean/LemmaF_copy.lean"
$P check --ws pcp --name lean-Tunnel_copy --expect-exit 0 --cwd /home/user/z4-lean -- bash -c "PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/o1-chalF/lean/Tunnel_copy.lean"
$P check --ws pcp --name chal_F-runA --expect-exit 0 --timeout 300 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 chal_F.py runA 64,256,1024   # expect exit 1: Q1 beta=4096 (own quadrature)
$P check --ws pcp --name chal_F-runB --expect-exit 0 --timeout 300 -- env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 chal_F.py runB 4096            # expect exit 1: same
$P check --ws pcp --name child-rerun --expect-exit 0 --cwd child_rerun --timeout 300 -- python3 barta2.py    # remove child_rerun/res_log.csv first (mode "x")
$P check --ws pcp --name grandchild-rerun --expect-exit 0 --cwd child_rerun/gc --timeout 300 -- python3 -I gc.py
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
Results: results/chal_F_run4.json, results/chal_F_run5.json; logs run*.log; notes.md.
