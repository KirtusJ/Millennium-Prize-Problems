# g1-toron (T71) report

**Strongest target closed: NONE of T1–T4.**
- What is proved: an exact reformulation (S1), the closed-form potential (S3), splitting and Schur/ground-state reductions (S2, S4, S6), and a kinetic bound (S5) conditional on one cited Bessel inequality.
- What is missing: the gap needs inequality M1, and even the zero-point bound needs M0. Both are stated exactly in TORON_GAP.md §2.
- Control: control.txt = 0.272341.
- Lean: /home/user/z4-lean/READY exists; scalar.lean passes (exit 0; axioms propext, Classical.choice, Quot.sound; no sorry).

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| T1 / T2 / T3 / T4 (gap lower bounds) | NOT CHECKED (not proved) | Each needs M1 (TORON_GAP §2); no step controls a second eigenvalue |
| S1 exact reformulation 1−λ_k = min-max of ⟨g,(1−K+W)g⟩/⟨g,(1+W)g⟩ | STANDS | Two-line substitution f = e^{V/2}g; sidesteps the Golden–Thompson direction |
| S2 λ0 ≤ 1 − min(½, ν0/2) | STANDS | Lean F5 (quotient_split) plus S1 |
| S3 V = 2β sin²θ1 sin²θ2 sin²φ (k = 2) | STANDS | Algebra; P1 max error 8.3e−16 on 2000 random pairs |
| S4 1−K1K2 ≥ ½(1−K1) + ½(1−K2) | STANDS | Lean F1 plus spectral calculus |
| S5 κ_j ≤ exp(−2j(j+1)/(β+2j+½)) | STANDS conditionally (Amos 1974 cited from memory, not read) | Derivation: Lean F2, F3. Child T74: 2200/2200 grid cases met, rerun identical by me |
| S6 ground-state representation ⇒ ν0 ≥ inf[1 − Kφ/φ + V] | STANDS | Standard identity, proof in TORON_GAP S6 |
| S7 −Δ_{S³} + 4λρ² ≥ 4(√λ−1) | STANDS | Jacobi substitution; minimisation in Lean F4 |
| M0 zero-point bound −ln λ0 ≥ cβ^{−1/3} | NOT CHECKED (MISSING) | Reduced to one pointwise inequality, not proved |
| Numerics, two-direction model (su2x2.py) | STANDS as a measurement | m_e·β = 3.28, 3.05, 4.12, 8.66 at β = 2, 4, 8, 16; jmax 5 vs 6 agree to 0.1% |
| Expectation P5 (gap above the free gap at every β) | DEFECT (my expectation) | Failed at β = 2, 4, 8; met at 16 |

**Counts** (met, failed, measured only):
- su2x2.py: P1 1 met; P2 2 met; P3 2 met; P4 4 met; P5 1 met, 3 failed; P6 1 met; measured-only table 1.
- Total: **11 met, 3 failed, 1 measured only.**
- Child T74 (claims A, B, C): 5058 met, 0 failed, 0 measured only (final pass).

## Hypotheses used and where they are stated
- Wilson action, the one-site normalisation, temporal gauge and the averaged temporal link: TORON_GAP §0.
- The Bessel ratio bound of Amos 1974 (ν ≥ 0, x > 0): TORON_GAP S5. It is cited from memory and not read; it is supported only numerically on the grid x ≤ 512, n ≤ 200.
- β ≥ 8 for the corollary of S5: TORON_GAP S5.
- The φ in S6 is positive, continuous, gauge-invariant and center-even: TORON_GAP S6.
- WKB tunnelling scale exp(−c√β) for the center-odd sector: TORON_GAP §4, CLAIMED.
- Numerics: truncation j ≤ 6 and quadrature n = 48 (su2x2.py docstring). Compression eigenvalues are lower bounds on the true ones (Cauchy interlacing); gaps are not bounded either way.

## Failed predicates (kept)
- **P5, β = 2, 4, 8:** m_e = 1.638, 0.763, 0.516 against free gaps 2.012, 1.073, 0.527. This was my own expectation, and it was wrong at strong coupling. It is not a defect of R1, which is asymptotic. P5 holds at β = 16 (0.541 against 0.257).
- **Child:** its first trapezoid pass left 1729 cases undecided, by its own expectation. Its series pass decided all of them. No failures.

## Not checked
- M0 and M1, hence all of T1–T4.
- The three-direction model, numerically or otherwise.
- β > 16 numerically (would need jmax ≳ 8).
- The center-odd sector.
- The Amos inequality itself: not read and not proved, checked on the grid only.
- Simon 1983: not read and not used.
- No literature was fetched in this run.
- The child's check.py (first pass) was not rerun. Only check2.py was rerun, and its output was identical.

## Delegated questions and outcomes
- **Child T74** (admitted under T71, released). Question: check claims A (Amos bounds, ν ≤ 200), B (the κ_j bound of S5, n ≤ 200) and C (its β ≥ n+½ corollary) for x from 0.5 to 512.
  - Control: I_3(4)/I_1(4). My value is 0.341953 and the child answered 0.341953, so I graded it correct before reading anything else.
  - Outcome: A 2211/2211, B 2200/2200, C 647/647 qualifying cases met. Worst log-slack for B is 1.14e−5 at (n = 1, x = 512).
  - I reread check2.py (formulas lines 33, 38, 39 match the claims) and reran it in a scratch copy (register K3). The output was identical.
- **Grandchild T76** (admitted under T74 and released, per the child's report; I did not inspect the graph entry myself). Question: 50-digit recomputation of I_201(8)/I_1(8) = 1.76378e−259 and of the worst cases. They matched, as reported by the child. I did not rerun the grandchild.

## Registers
- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp` → `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl` → `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

## Rerun (from /home/user/z4-workers/g1-toron; result files are mode "x", so use fresh names)
```
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
$P check --ws pcp --name su2x2-run2 --expect-exit 0 --timeout 300 -- python3 prog/su2x2.py results_su2x2_run2.txt
$P check --ws pcp --name lean-scalar-2 --expect-exit 0 --cwd /home/user/z4-lean --timeout 290 -- bash -c 'PATH=$HOME/.elan/bin:$PATH lake env lean /home/user/z4-workers/g1-toron/scalar.lean'
mkdir -p /tmp/claude-0/childrerun2 && cp child/check2.py /tmp/claude-0/childrerun2/
$P check --ws pcp --name child-rerun-check2b --expect-exit 0 --cwd /tmp/claude-0/childrerun2 --timeout 250 -- python3 check2.py
$P check --ws pcp --name child-run2 --cwd child2 --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"   # after: mkdir child2; cp child/PROMPT.txt child2/; pcpos task-admit first
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
