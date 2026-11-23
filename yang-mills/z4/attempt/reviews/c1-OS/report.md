# Report c1-OS (task T5): Theorem S, the whole chain as one conditional theorem

Worker c1-OS for Director Z4, principal Kirtus Justus. The deliverable is [`THEOREM_S.md`](THEOREM_S.md). Its first line: Theorem S is conditional, with **5 lattice hypotheses (H0 to H4)** plus three separate ones it does not conclude, (E1), (E2) and (G). **For SU(2), 2 of the 5 are proved: H0 (lattice axioms) and H2 = (B).** H1 = (A) is the problem. Control: `control.txt` = 0.272341.

Same model family as the director. This is not independent review.

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| Theorem S, steps 1 to 6 (compactness; E0′; translations; O(4) from W₄ + one irrational rotation; symmetry; RP) | STANDS (as written by me) | THEOREM_S §4. Elementary proofs; step 2 is a sketch with its constants traced. Not challenged by anyone |
| Step 7, OS II reconstruction (E0′ + E1–E3 ⇒ Wightman) | STANDS, CITED-2nd only | Read only in KQR arXiv:2104.02090 §9.2 eq. 9.18. Projecteuclid blocked; OS 1973/1975 not read |
| Step 8, gap ≥ 1 for all n-point vectors | STANDS | The inequality F(t+s) ≤ e^{−s}F(t) is closed under pointwise limits. Proof in §4 |
| Steps 9 to 12 (unique vacuum, hyperboloid, cluster, not empty) | STANDS | §4. Step 11 is a sketch |
| Free-field known-answer test (every hypothesis holds; limit = free field of mass 1, including off-axis points) | STANDS | freefield_S.out: 32 predicates met, 4 failed, all four my own (below). Errors ≤ 2.4·10⁻³ at m = 1/32 on 8 points |
| (E1) in the brief's suggested form ("not a generalized free field") | DEFECT (of the brief's formulation) | :φ²: of the free field has nonzero truncated 4-point functions and so passes it, though the theory is free (§5) |
| Initial choice a = bare mass m | DEFECT of my first draft, corrected | The exact lattice gap is 2 asinh(m/2). Theorem S uses the gap |
| H3 for SU(2), H4 for SU(2) and for 4D Ising | NOT CHECKED | no tool; no rigorous source found |
| OS 1973 axiom numbering and ⁰𝒮₊ definition; Osterwalder–Seiler locator | NOT CHECKED | from memory or search snippets |

Counts for the program predicates: **met 32, failed 4, measured only 0**. The child's run: 5 met (P1, P2, P3, P5, P6), 1 failed (P4, on 2 of 4 points; the child's own tolerance).

## Hypotheses each statement uses, and where they are stated

- **Theorem S:** H0, H1, H2, H3(a, b, c), H4 (THEOREM_S §2).
  - Step 1: H3(b, c).
  - Step 2: H3(b), plus step 1.
  - Step 3: H0, H2, H3(c).
  - Step 4: H0, H3(c), H4.
  - Step 5: none.
  - Step 6: H0, plus step 2.
  - Step 7: E0′ and E1–E3 (from steps 2 to 6).
  - Step 8: H1 with a = m, H3(c).
  - Steps 9 to 11: step 8, plus step 4 for 11.
  - Step 12: H3(a, c).
- **Free-field claims:** RP of the Gaussian (CLAIMED); Green-function bounds G_m(n) ≤ C/|n|² and the gradient bound (CLAIMED, checked numerically); the local CLT for isotropy (CLAIMED).

## Failed predicates (kept)

1. **P0:** G₁(0) = 0.127111840 against 0.1271118504, with tolerance 1e-9. *Mine:* the t-integral is cut at 1e-8 and drops about 1e-8, which only matters at n = 0. The control itself was computed separately and is correct.
2. **P3 t-axis and P3 space-axis:** error exactly 0 at all m, so "strictly decreasing" fails. *Mine:* the point x = e₀ rounds to the normalization point N e₀, so the comparison is degenerate.
3. **P3 (0.3,0.4,0,0):** errors 4.2e-4, 4.8e-3, 1.2e-3, not monotone. *My expectation:* the lattice artefact changes sign; the child saw the same at (1,1,0,0). P4 holds there (1.3e-3).
4. **Child P4:** the m² ratio fell outside [3,5] at two points. *The child's tolerance,* not the target.

## What I did not check

- H1, H3 and H4 for SU(2), and H4 for 4D Ising.
- A proof (as opposed to numerics) that the free lattice two-point function is isotropic in the limit.
- The OS papers themselves (blocked); Glimm–Jaffe (not online).
- Fredenhagen/Ruelle-type cluster theorems (not needed; step 11 is direct).
- The (E2) logarithm exponent.
- No Lean. READY exists, but no Lean result is claimed.
- No challenger has attacked THEOREM_S.md.

## Delegated questions and outcomes

- **Child, task T7** (admitted under T5, label c1-OS-child; released). Its question: the free-field scaling limit with a = m at 4 points (two off-axis), plus the Wick square.
  - Control: G₁(0) in d = 4. My value 0.127112 (0.12711185041). The child answered **0.127112: PASS**, graded first.
  - Outcome: errors 0.2–0.6 % at m = 1/16, decreasing; the rotation check passes.
  - Reread: yes. Rerun: check K3, control, results.json and predicates.txt byte-identical. My program reproduces two of its numbers to 10⁻⁹ (P0b).
- **Grandchild, task T11** (parent T7, admitted and released by the child). Its question: K₁(1)/(4π²) by two methods.
  - Control K₀(1) = 0.4210244382: pass.
  - Returned 1.524648825162e-02, which matches. The child notes that the two methods share the I-series.
- **Source reader** (in-session sub-agent, not a PCP child): reported projecteuclid blocked, and read KQR in full plus 3 abstracts.

## PCP record

- `python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp` → `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- `/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl` → `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
- Checks: K1 child-run1 (exit 0, 145 s), K2 freefield_S (exit 0), K3 child-rerun (exit 0).

## Commands to rerun (from /home/user/z4-workers/c1-OS; outputs use mode "x", so give new names)

```
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P check --ws pcp --name freefield_S_rerun --expect-exit 0 -- taskset -c 0 python3 freefield_S.py freefield_S.rerun.out
mkdir child_rerun2 && cp child/lib.py child/main.py child/control.py child/evalpred.py child_rerun2/
$P check --ws pcp --name child-rerun2 --cwd child_rerun2 --expect-exit 0 --timeout 400 -- bash -c "taskset -c 0 python3 control.py && taskset -c 0 python3 main.py && python3 evalpred.py"
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```

The child itself was run with:

```
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
```

with task-graph commands `pcpos task-admit /home/user/z4-work/graph/attempt.jsonl --by principal --label c1-OS-child --parent T5` (→ T7) and `pcpos task-release … --id T7`.
