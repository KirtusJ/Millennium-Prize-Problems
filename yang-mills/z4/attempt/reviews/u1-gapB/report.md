# report.md — u1-gapB (task T174), builder for gaps A, B and C in note/tun_lower.tex

Control: `control.txt` = 0.272341 (−ln tanh 1). Lean was READY.

I share a model family with the director and with the writers. My agreement is not independent review.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| S4-alg corner absorption, as written in the original note | DEFECT | It is not quantified ("≫", "≈0", "V large"); no case split is given. |
| S4-alg, new statement under (M_A), δ ≤ m/2, y_β ≤ m/2 | STANDS (PROVED) | Written proof in tun_lower_patched.tex. Lean: corner.lean, 5 theorems, exit 0, standard axioms only. Grid P1–P5 met; the child's N1/N2 met on 10200 cases each. |
| The margin of the corner inequality is positive for all η ∈ (0, 0.4] | STANDS | It is m(η) = min(1−e^{−3η/4}, 1−e^{−1/16})/2 > 0, which is ~3η/8 for small η. A slack of order η is necessary (exact value 1−e^{−η} at x_c = y_c = 0). |
| The old c₁ condition implies (M_A) | STANDS | Analytic argument in the lemma's remark. Numerically M_{c1}² − M_A² ≥ 5.98 on 4005 points (child N3, rerun by me). |
| Lemma tu:L-balls, original proof ("covered by the first case") | DEFECT | Points of a valley ball with a1 just outside [a_−, π−a_−] are not in a first-kind ball. |
| Lemma tu:L-balls, new proof (split by ball type) | STANDS (PROVED) | (I) Theorem H4 applied pointwise on D_{M''}. (II) Prop sub gives g ≥ φ on all of X, and the φ formula holds everywhere. Constants checked by P7. |
| M² at η = 0.4 from the c₁ formula: "14.8" (TUNNEL_LOWER_FULL) | DEFECT | The value is 18.047 (P6). The writer's 18.0 stands. |
| "M² ≈ 3.4/η" (FULL) | DEFECT | The c₁ formula gives η·M² → 4.656. The new (M_A) gives η·M_A² → 3.497. |
| Remark on M: "M² ≥ 2ρ_B²" | DEFECT (already noted by the writer) | It is replaced by M² ≥ 1.5ρ_B² + log 2, which (M_A) implies. |
| Patched note compiles | STANDS | pdflatex exit 0, 0 undefined references, 28 overfull boxes (the original also has 28). |

## 2. Hypotheses each new statement uses, and where they are stated

- **S4-alg (new)** — stated in Lemma tu:L-S4 of tun_lower_patched.tex.
  - η ∈ (0, 0.4], with a_−, r0 = √(η sinh η/4), ℓ = r0/3, θ0 = 1/2 (§ ansatz).
  - (M_A).
  - 0 < λ ≤ 1.
  - (E1)–(E3) at x with δ ≤ m/2 (Prop tu:L-E13, Lemma tu:L-E2; not rechecked by me).
  - y_β ≤ m/2.
  - χ = 1 on [a_−, π/2] and Θ̃ = Θ on [0, π/2] (Lemma ansatz-props).
  - The identity α(S) = 2S√(1+S²), which gives G = e^{−kV/2}.
- **Lemma balls (new)** — stated in Lemma tu:L-balls.
  - β ≥ β₀, β ≥ 4, √β > ρ_B/r0, √β ≥ θ0ρ_B²/(2ℓ log(4/3)), √βΘ(r0) ≥ log 4.
  - M² ≥ 1.5ρ_B² + log 2.
  - Theorem H4 with its constants 8.35 and 9.09 (Cor H4cor; not recomputed by me).
  - Prop tu:L-sub.
  - (infl) of Lemma tu:L-elem.
  - The chain construction of § chainsec.

## 3. Failed predicates

My predicates: none. All P1–P7 are met.

The child's failed runs are kept in child/notes.md:
- `control.py` rerun, exit 1: the child's own expectation (mode "x" refuses to overwrite). Not a target defect.
- `grid1`, exit 1: the child's own bug (np.bool_ is not JSON-serialisable). Not a target defect.
- `grid2`, exit 1: the child's own bug (a KeyError from numpy-2 repr). Not a target defect.

The child's clean run `grid4` exited 0, and my rerun `child_grid_rerun` exited 0.

Counts:
- mine: 7 met, 0 failed, 1 measured only (M1: slacks and the minimal M²);
- Lean: 5 met, 0 failed;
- child: 4 met (N1, N2, N3, G), 0 failed on the target, 3 measured only.

## 4. What I did not check

- (E1)–(E3) themselves, the gap bounds DG₁ and DG₃ (Lemma tu:L-gauss), and the Δh bound (Lemma tu:L-taylor).
- The first-half inputs (tun_upper.tex), which I did not open beyond the header.
- The H4 constants 8.35 and 9.09.
- Lemma L4 and Lemma M4.
- Whether Θ(r0) − Θ(ℓ) > 0 needs anything beyond ℓ < r0. It does not; this is trivial.
- The reductions in Steps 2–3 of S4-alg and the bounds in (d) are by hand, not in Lean. The Lean file covers only the scalar cores.
- The grid checks sample finitely many points; they are evidence, while the proof is the written argument.

## 5. Delegated questions and outcomes

- **Child T177** (admitted under T174; released, event 357).
  - Question: a numerical grid check of N1 (F ≤ 1−m), N2 (strip, F ≤ 1−m/2) and N3 (M_A² ≤ M_{c1}², with a table).
  - Control: c* = ∫₀^π √(4 asinh sin a) da. The child answered 4.605413, which is **correct**; I graded it before reading anything else.
  - Outcome: all three hold on its grid. Its minimum slacks match mine to every printed digit (7.5269e−3 at η = 0.4, 2.3872e−3 at 0.1, 3.7360e−3 at 0.01). I reran its `grid.py` under my register (exit 0, same summary).
- **Grandchild T178** (admitted by the child under T177; the child says it released it).
  - Question: an independent recomputation of M_A² and M_{c1}² at η = 0.4 and 0.01, and of P(s_lo) + e^{−1/16} at η = 0.01.
  - Control: asinh 1 = 0.881374, matched.
  - Outcome: 12.060726, 18.047286, 352.5224, 475.7219, and 0.969457 < 1. These agree with my check_gaps.py values.

## 6. Exact commands to rerun

Result files are opened with mode "x", so delete or rename `results_check_gaps.json` first, or run in a copy.

```
cd /home/user/z4-workers/u1-gapB
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
$P check --ws pcp --name check_gaps --expect-exit 0 -- python3 check_gaps.py
$P check --ws pcp --name child_grid_rerun --cwd child --expect-exit 0 --timeout 600 -- python3 grid.py result_rerun_by_parent.json
$P check --ws pcp --name lean_corner --cwd /home/user/z4-lean --expect-exit 0 --timeout 600 -- bash -c "PATH=\$HOME/.elan/bin:\$PATH lake env lean /home/user/z4-workers/u1-gapB/corner.lean"
$P check --ws pcp --name pdflatex_patched --cwd build --expect-exit 0 -- pdflatex -interaction=nonstopmode -halt-on-error wrap_patched.tex
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

Task graph:
```
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-admit /home/user/z4-work/graph/attempt.jsonl --by principal --label u1-gapB-child --parent T174
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos task-release /home/user/z4-work/graph/attempt.jsonl --by principal --id T177
```

The register holds K1 child-run1 (exit 0), K2 check_gaps (0), K3 child_grid_rerun (0), K4 lean_corner (0) and K5 pdflatex_patched (0).

Last lines of the verify commands:
- `pcp_os.py verify --ws pcp`: "result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)"
- `pcpos verify pcp/register.jsonl`: "A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right."

Deliverables: GAPS.md, note/tun_lower_patched.tex, corner.lean (+ lean_output.txt), check_gaps.py and results_check_gaps.json, build/wrap_patched.pdf, notes.md.
