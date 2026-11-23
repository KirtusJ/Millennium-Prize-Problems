# Report r1-asm (task T158): assembling limsup (−log m_eo)/√β ≤ c*

Deliverable: TUNNEL_LOWER_FULL.md. Control: control.txt = 0.272341 (−ln tanh 1).

The assembly is proved in writing, conditional on the unreviewed parts. I share a model family with the director and with every author of the parts, so my agreement is not independent review.

## 1. Verdict table

| item | verdict | one line of evidence |
|---|---|---|
| Overall: linear proof of limsup ≤ c* from the parts | STANDS (conditional on unreviewed parts) | TUNNEL_LOWER_FULL §7; every interface fits after C1–C7; no interface DOES NOT FIT |
| (1) sets: tube K (E13) vs Ω (TUNNEL_LOWER2) | DEFECT, fixed by C1 | E13's numbers use η' = 0.5 > a₋(η = 0.25) = 0.2554, so [a₋, η') is uncovered (asm_check P6 FAILED). The fix is η' := a₋; E13's proof allows any η' > 0 |
| (1) S (PATHS) σ₁-invariance; R_well ⊂ D_M ∪ σ₁D_M | STANDS | On supp φ_L, V < 2M²S/√(1+S²) < 2M² and a₂ < r₀ ≤ π/2 |
| (2) Lemma C hypotheses delivered by S4-alg + (E1)–(E3) | STANDS after C2, C3 | Δ₁ ≤ η/4 leaves A₁ − λ ≥ e^{η/2} − 1 (D ≤ η/4); the max(φ_L, φ_R) form needs S4-alg only for a₁ ≤ π/2 |
| (2) Ψ kink at π − a₋/2; Θ∘a₂ cone point at U₂ = −1 | DEFECT (TUNNEL_LOWER2), fixed by C2, C3 | Lemma K needs a global C² weight. Fix: smooth cut-offs, Ψ' = 0 near π, Θ flat near π |
| (3) normalisation μ from HARNACK; M fixed | STANDS | M = M(η) is chosen before β → ∞; M enters only the β^{1/4} term |
| (3) HARNACK "M² = O(log 1/η)" | DEFECT (harmless) | M² ≈ 3.4/η (asm_check P5: 14.8 … 339 at η = 0.4 … 0.01) |
| (4) factor c* vs 2c* | STANDS (c*) | φ = max(φ_L, φ_R) is the tent, so 2Ψ(π/2) = c*(η) (P4 met 3/3). The monotone reading would give ≈ 9.3. Child 1D: r → c*; my independent onedflux.py agrees to all digits |
| (4) TUNNEL_LOWER2 §4 wording e^{−√βΨ(a₁)} | DEFECT (wording), fixed by C6 | It must be min(Ψ(a₁), Ψ(π−a₁)); §5 already uses 2Ψ(π/2) |
| (4) chain x → σx | Missing in all parts; supplied by C4 | HARNACK phases 0 and 1, then the U₁ subgroup through 1 (length π, V ≡ 0), then the σ₁-mirror. Ball inclusion checked: P3 met 3/3 (ratio ≤ 1.398 ≤ 1.5) |
| (5) ∫_S f² ≥ ½ via M4 | STANDS after C5 | Lemma L4 (trial bound λ_ee, λ_eo → 1) proved here; P1 met 3/3. Its rate is very slow (P2 failed) |
| (6) m_eo ≥ Δ/λ_ee ≥ Δ | STANDS | log x ≥ 1 − 1/x and λ ≤ 1 |
| (7) parameters and order of limits | STANDS | Consistent choice in §6 of the FULL file; P5 met 7/7 |
| Ψ' ≤ √(2(ε+η)) on the transition zone | DEFECT (omitted statement), fixed by C7 | Needed for 2Ψ(π/2) ≤ c*(η) |
| Child output field "delta" | DEFECT (child's, harmless) | child/results_beta256_v2.json "delta" = m = 8.73e−30. My flux Δ = 7.19e−30 = m·λ_e. r is unaffected |

Counts over the 15 rows of the verdict table: STANDS 9 (rows 1, 3, 4, 6, 8, 10, 11, 12, 13; row 10 stands only after C4), DEFECT 6 (rows 2, 5, 7, 9, 14, 15; every one is fixable or harmless), NOT CHECKED 0. The inside of the parts is listed in §4.

## 2. Hypotheses each statement uses, and where they are stated

- **Lemma C.**
  - Uses φ ≥ 0, ‖T_ΩΩ‖ < λ, Tφ ≥ λφ on Ω, and φ ≤ g on Ω^c (TUNNEL_LOWER §1; continuum in PATHS §3(C)).
  - ‖T_ΩΩ‖ < λ comes from Lemma F in its η/2-form (LEMMA_F §3) and λ > e^{−3η/2} (L4, FULL §5).
- **S4-alg** (TUNNEL_LOWER2 §2).
  - Uses (E1), (E2), (E3) with o(1) errors.
  - Uses c₁ ≤ G_min(e^{η/2}−1)e^{−C}/4 and r₀²/sin a₋ ≤ η/4.
  - Uses ℓ < r₀/2 and λ ≤ 1.
- **(E1), (E3)** (E13 §0).
  - (H1) Ψ ∈ C² on a neighbourhood of the tube's a₁-range, with H_Ψ and Λ finite.
  - (H2) Θ as defined, H_Θ ≤ θ₀/ℓ.
  - (H3) x ∈ K, with K's η' > 0 and r₀ + 0.1 ≤ π/2.
- **(E2).** Uses Lemma K (TUNNEL_THEOREM §3) and a global C² weight with bounded Hessian (C2, C3).
- **H4** (HARNACK §3).
  - Tg = λg with λ ≤ 1, g > 0 continuous, and σ₁, σ₂ symmetry.
  - x ∈ D_M, β ≥ max(1, 4ρ²), ρ ≤ ½, a* ≤ π/4.
  - m_B from M4.
- **M4** (TUNNEL_LOWER2 §3). Uses (B) for u ∈ {f, g}, which needs λ_u ≥ e^{−η/4} (L4) and Lemma F.
- **(B)** (TUNNEL_THEOREM §4). Uses Lemma F (η/4), Lemma K, and a C² weight Φ (with the smoothing at π/2).
- **Lemma F** (LEMMA_F §3). Holds for β ≥ β₀(η), for all s ∈ [0, 1].
- **P'c / Corollary B** (PATHS §1, §2.1).
  - (H1)–(H4) of PATHS §0.
  - Paths from every x ∈ S to σx; Q_min > 0 on U; v > 0.
- **L4** (FULL §5). Uses only V ≤ 2β sin²a₁ sin²a₂, the triangle inequality on S³, and positivity of T.

## 3. Failed predicates (all kept)

1. **asm_check P2: FAILED. My own expectation.** I guessed that 1 − L_β < 0.05 at β = 10¹⁶. Measured: L_β = 0.75, with the rate about β^{−1/12}. L4 still gives o(1), which is all the limit needs, but no usable β₀ follows from it.
2. **asm_check P6: FAILED, as expected. A defect of the target's parametrisation.** E13 used η' = 0.5 > a₋ = 0.2554.
3. **Child T160.** All its failures were its own coding bugs: K1 exit 1 (KeyError), a formatting bug, K7 exit 1 (JSON bool), and an empty first control file. All were fixed and rerun. No physics predicate failed.
4. **Grandchild T161.** Its float64 route gave m = 0 at β = 256, so it did not reproduce r. That was the child's expectation failing, not a defect of the target.

## 4. What I did not check

- The internal proofs of E13 §2–§4 (the Taylor remainder and gap bounds), LEMMA_F §2 (Theorem 1), Lemma K, HARNACK §1–§2 (constants 8.35 and 9.09), and PATHS §1. I used their statements and checked only the interfaces.
- The smoothing in (B)'s weight (TUNNEL_THEOREM §4), and Lemma R.
- Any SU(2)² eigenfunction numerically. Every numerical check of g, f and m is 1D.
- The Lean files of the parts. I used no Lean myself (/home/user/z4-lean/READY exists, but no Lean result is claimed).
- β₀(η): it is astronomically large. Lemma F needs about 10¹⁴ at η = 0.2, and E13's Δ₁ is 0.17 at β = 2.7·10⁸. The result is purely asymptotic.
- Measurability of the chain centres in phase 0 is asserted, not written out.

## 5. Delegated questions and outcomes

- **Child: task T160** (admitted under T158, run as child-run1 in my register, released).
  - Question: on the 1D grid model, does −log m/√β approach c* or 2c*? Is the tent subsolution valid at the kink?
  - Control: c* to 6 decimals. Answer 4.605413, graded CORRECT before reading anything else.
  - Outcome:
    - r = 3.936, 4.182, 4.335, 4.432 at β = 64, 256, 1024, 4096, approaching c*.
    - 2q/r = 0.989 … 0.996.
    - Tent: Tφ/(λφ) ≥ 1.37 on {ε ≥ 2η}, and 2.69–3.36 at the kink, in 4 of 4 β.
  - My recheck: I reread its code and outputs and reran via onedflux.py (an independent method: matrix squaring plus the flux identity). r agrees at β = 64 and 256 to all printed digits (Q1, Q2, Q3 met 2/2 each). I found its "delta" field mislabelled (it holds m).
- **Grandchild: task T161** (admitted under T160 and released by the child).
  - Question: an independent recomputation of r at β = 256 after a known-answer control.
  - Outcome: control matched. Its float64 run could not resolve m (λ_e = λ_o to 16 digits), so r was not independently reproduced by the grandchild. My onedflux.py supplies that independent recomputation instead.

## 6. Commands to rerun (from /home/user/z4-workers/r1-asm)

Result files are opened with mode "x", so move the old ones aside first.

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name onedflux-b64 --expect-exit 0 -- python3 onedflux.py 64
$P check --ws pcp --name onedflux-b256 --expect-exit 0 -- python3 onedflux.py 256
$P check --ws pcp --name asm-check-run1 --expect-exit 0 -- python3 asm_check.py
G=/home/user/z4-work/graph/attempt.jsonl; R=/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos
$R task-admit $G --by principal --label r1-asm-child --parent T158
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$R task-release $G --by principal --id T160
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

The child's own rerun commands are in child/report.md.

## 7. PCP OS record

- `$P verify --ws pcp`, last line: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `pcpos verify pcp/register.jsonl`, last line: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Checks recorded: child-run1 (exit 0), onedflux-b64 (K2, exit 0), onedflux-b256 (K3, exit 0), asm-check-run1 (K4, exit 0).
- Predicate counts:
  - asm_check: met 16, failed 2, measured only 2.
  - onedflux: met 6, failed 0, measured only 0.
