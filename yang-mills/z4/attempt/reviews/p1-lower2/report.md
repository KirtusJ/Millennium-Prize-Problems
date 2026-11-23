# report.md — worker p1-lower2 (T146), brief p1-lower2

Control: control.txt = 0.272341 (−ln tanh 1). Lean READY present. Main write-up: TUNNEL_LOWER2.md. Target limsup (−log m_eo)/√β ≤ c* is **NOT proved**. It is reduced to four inputs, listed below. I share a model family with the director, so my agreement is not independent review.

## 1. Verdict table

| item | verdict | evidence (one line) |
|---|---|---|
| Target limsup ≤ c* for SU(2)² | NOT CHECKED (not reached) | conditional on (E1), (E3), H4 and continuum P' (TUNNEL_LOWER2 §5) |
| §1 tangent decomposition 2 valley + 2 transverse + 2 gauge; y-step is N(0, I/β); flat fixed point at S | STANDS | explicit quaternion linearisation, co-isometry; I5 of LEMMA_F (Lean `fixed_point`, cited) |
| Brief's ansatz: φ = e^{−√βΨ(a₁)}·Gaussian in invariant q = \|u₁×u₂\|²/S², −log(Tφ/φ) ≈ ε(S) − Ψ'²/2 | STANDS (to O(β^{−1/2})) | √β·\|diff\| ≤ 2.1 at 36/36 points (mine); child independent ≤ 2.6; worst \|diff\| 0.127 → 0.059 → 0.032 |
| (E2) upper tilt bound | STANDS (given Lemma K) | Lemma K per link, symmetric kernel |
| (E1), (E3) local Gaussian estimates, uniform o(1) | NOT CHECKED (CLAIMED sketch) | error budget in TUNNEL_LOWER2 §2; numerics support it; v1 run shows the o(1) is ~3θ₀/(2ℓ√β) |
| Lemma S4-alg (cut-off (G−c₁)₊(E−c₂)₊ with tilt gain in a₂) | STANDS given (E1)–(E3) | ring identity Lean `cutoff_identity`/`cutoff_pos`; Q4 52/53 at β ≥ 1024 |
| ‖T_ΩΩ‖ < λ_ee on the tube | STANDS (given Lemma F) | T = B*K₁B and fibre bound |
| (B) applies to the odd state f (brief's question) | STANDS | the proof of (A) uses only Tu = λu, the Schur step for real F, and λ ≥ e^{−η/4}; no positivity is needed |
| Lemma M4: mass of f², g² on corners ∩ {V ≤ K} | STANDS (given (B)) | λ ≤ ∫e^{−V}u² plus (B) in each link |
| H4 Harnack chain g ≥ e^{−C(η+a₋+r₀)√β} | NOT CHECKED (CLAIMED) | (H-a), (H-b) proved; chain geometry (H-c) only sketched |
| Continuum Lemma P' (flows) | NOT CHECKED (MISSING) | same gap TUNNEL_LOWER lists for the 1D continuum |
| Brief's "the tube must allow a₂ to wander; a constant-in-a₂ φ with a cutoff" | DEFECT (as stated) | a plain cut-off in the free a₂ direction fails Lemma C at the a₂ edge (loses half the step mass). A tilt e^{−√βΘ(a₂)} is needed, and its gain e^{\|∇Θ\|²/2} pays for the cut-off (S4-alg). |

Counts of predicates: **met 92, failed 1, measured only 19** (main run v2: Q1 3, Q2 36, Q3 1, Q4 52 met / 1 failed at β ≥ 1024, counted per point; the 19 β = 256 Q4 support points are measured only, 6 of them with R₁ < 1). v1 smoke run kept separately: Q1 3/0, Q2 36/0, Q3 0/1, Q4 36/15. The child's own counts are met 76, failed 0, measured only 36.

## 2. Hypotheses used and where stated

- Lemma F (ε_eff ≥ ε − η uniformly): LEMMA_F.md §3, proved there. I used it for ‖T_ΩΩ‖ and inside (B).
- Lemma K (kernel moment bound): TUNNEL_THEOREM §3. Used for (E2) and in the sketches of (E1) and (E3).
- Inequality (A) and estimate (B): TUNNEL_THEOREM §4. I extended them to f and to the exchanged links (TUNNEL_LOWER2 §3).
- λ_ee ≥ 1 − O(β^{−1/3}): TUNNEL_THEOREM §4 (sketch, and A4 cited there). The λ_eo analogue is my own sketch.
- Lemma C and Lemma P' (discrete): TUNNEL_LOWER §1. P' is used in a continuum form that is not written.
- Kernel e^{β⟨U,U'⟩}/Z and Z = 2I₁/β: LEMMA_F I1, I2.
- Scalar L3 (c*(η) ≤ c* + π√(2η)): TUNNEL_LOWER (Lean there).
- New in TUNNEL_LOWER2 with these tags: (E1) CLAIMED, (E3) CLAIMED, (H-c) CLAIMED, continuum P' MISSING.

## 3. Failed predicates

- v1 smoke run, K1: exit 1 because scipy is missing. Own defect; replaced by quadrature.
- v1 smoke run, Q3: FAILED. The cause was MC noise (SE 2–9%), an own defect. Fixed in v2 with antithetic sampling and more samples; v2 Q3 is MET.
- v1 smoke run, Q4: 15/51 FAILED, all at a₂ ≈ 0. Own expectation: the parameters were ℓ = 0.02, θ₀ = 1, and the Θ-Hessian cost exceeds η at these β. This is not a defect of the target. It does show that the o(1) in (E1) is only small when √β ≫ θ₀/ℓ.
- v2 main run, Q4: 1 FAILED, at β = 1024, a₁ = 0.5, a₂ = 0, y = 0. R₁ = 0.967 ± 0.004. This is own expectation (finite-β Hessian cost plus a positive ~2/√β drift at a₁ = 0.5). The same point gives 1.120 at β = 4096.

## 4. What I did not check

- (E1) and (E3) are not written as proofs with constants. The Gaussian truncation, the curvature and the Θ–y cross terms are only estimated in order of magnitude.
- The geometry of the Harnack chain (H-c), including the region near (1,1) where S → 0.
- The continuum/flow version of Lemma P'.
- The λ_eo ≥ 1 − O(β^{−1/3}) trial argument is a sketch; I did not check the gauge-invariant bump in detail.
- The O(β^{−1/2}) coefficient of diff. Its sign tracks ΔΨ on S³, but its size is about 2/3 of −ΔΨ/2, unexplained.
- The Q4 numerics test only 27 points per β, not a dense tube. Points at the a₁ ends below 0.5 were not tested.
- I did not recheck the proofs of LEMMA_F or Lemma K. I only read them.

## 5. Delegated questions and outcomes

- **Child T147** (admitted under T146; released by me after it finished). Question: MC of −log(Tφ)/φ against pred = ε(S) − ε(sin a₁) at 12 points for β = 256, 1024, 4096. Control: c* to 6 digits. It answered 4.60541, which I graded CORRECT before reading anything else.
  - Outcome: diff = O(β^{−1/2}), with √β·|diff| ≤ 2.6 (1.2–2.3 at a₁ = 0.5, systematic positive; negative at 2.5).
  - Its 7 predicates/case-sets were all MET.
  - I reran its mc.py in child_rerun/ (check K6): the output is bit-identical. Against my independent code, |z| ≤ 2.62 at 36/36 points.
- **Grandchild T148** (admitted by the child under T147, released, per the graph: TASK_ADMITTED and TASK_RELEASED events for T148). Question: sampler moment E cos θ = I₀/I₁ − 2/β at β = 256, with a c* control.
  - It returned 0.99414085 vs exact 0.994146369513 (1.15 SE), MET. It also confirmed the identity I₀/I₁ − 2/β = I₂/I₁ (3.7e−15).
  - My own Q1 gives the same exact value, 0.99414637.

## 6. PCP OS record

- Register pcp/: checks K1 (tube-smoke, exit 1, kept), K2 (tube-smoke2), K3 (child-run1), K4 (lean-cutoff), K5 (tube-main), K6 (child-mc-rerun).
- `$P verify --ws pcp` last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl` last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Lean CutoffAlgebra.lean: exit 0; axioms [propext, Classical.choice, Quot.sound] for all three theorems; no sorry.

## 7. Exact rerun commands (from /home/user/z4-workers/p1-lower2; result files are mode "x", so use a new tag or a fresh copy)

```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
$P check --ws pcp --name tube-main-r --expect-exit 0 -- python3 tube_ratio.py main_r 400000
$P check --ws pcp --name tube-smoke-v1-r --expect-exit 0 -- python3 tube_ratio_v1.py smoke_r 20000   # v1 (scipy already replaced by quadrature)
cd /home/user/z4-lean && PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/p1-lower2/CutoffAlgebra.lean
mkdir rr && cp child/mc.py rr/ && $P check --ws pcp --name child-mc-rerun2 --cwd rr --expect-exit 0 -- python3 mc.py
$P verify --ws pcp ; /home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Note: tube_ratio_v1.py is the v1 code after the scipy patch, which is the code of check K2 (results_smoke.txt). The pre-patch code ran only as K1.
