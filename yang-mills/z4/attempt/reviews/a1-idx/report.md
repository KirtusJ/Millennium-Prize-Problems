# report — worker a1-idx (indexer), Director Z4

Deliverable: `/home/user/z4-workers/a1-idx/INDEX.md`. Control: `control.txt` = 0.272341 (−ln tanh 1).

## Verdict table
| item | verdict | evidence |
|---|---|---|
| INDEX.md covers all 7 director folders and their sub-folders | STANDS | inventory.py H: 7 of 7 folders have README; every sub-folder listed by `find -maxdepth 1` has a row or a grouped row |
| Child control (transfer-operator has 13 sub-folders) | STANDS | my `ls` = 13 before delegating; child/control.txt = 13; inventory.py P1, P2 met |
| Child's B4 rows (16 rows) | STANDS, with two corrections | I reread the B4 README and the openings of spatial-heat-trace, joint-cutoff, strong-coupling, hamiltonian-time and blocked-time; confirmed the girth-shell quote at `girth-shell/README.md:14`. Dropped the child's "L6" tag on spatial-plaquette (not supported by the README) |
| Grandchild's claim that no B4 folder treats β→∞ at a fixed lattice | DEFECT (grandchild) | contradicted by `weak-cavity/README.md` (g↓0 at fixed N cells); the child found this and I agree |
| Inflation: `transfer-operator/blocked-time` title "physical gap" | DEFECT (target, mild) | the gap holds at a fixed spatial mesh with z ≤ 1/384; it is ∝ 1/(βb) per `z4/README.md` audit table |
| Inflation: A4 root README on uniform-band leaves out "small β" | DEFECT (target, mild) | `observable-normalization/uniform-band/README.md:5` says "for small positive β" |
| `z4/OVERALL_DISPOSITION.md` classification "fixed mesh, conditional or control only" | DEFECT (director's summary, incomplete) | interacting Wilson results along b→0 exist (C4 magnetic-smearing, locality; D4 ordinary-loop; B4 spatial-heat-trace; A4 wilson-contact). Its conclusion that there is no interacting continuum result still holds |
| Answer: L3–L7 have no interacting result uniform in the lattice spacing; L2 has only upper bounds or escapes; L1 holds exactly at each cutoff | STANDS (based on reading) | see INDEX.md, last section; I found no file stating otherwise |
| No `sorry` in any .lean file (text grep) | STANDS | inventory.py P4: 0 files (text only, not a compile) |
| Lean files compile with standard axioms | NOT CHECKED | no Lean run. /home/user/z4-lean/READY exists, but I did not use Lean |
| README summaries agree with full statement files | NOT CHECKED (partial) | I read only the opening paragraphs and the "open" lines; full .md bodies were not read |

Counts: verdicts 6 STANDS, 4 DEFECT, 2 NOT CHECKED. Predicates of inventory.py: 4 met (P1–P4), 1 failed (P5), and per-folder file counts measured only. Hypothesis H: 7 of 7 cases qualify.

## Hypotheses each statement uses and where they are stated
These are given per row in INDEX.md ("statement" column: group, dimension, lattice, coupling regime, volume). The recurring hypotheses:
- **Fixed spatial mesh**: B4 hamiltonian-time/blocked-time, A4 Hamiltonian notes, C4 momentum, D4 adjoint-band.
- **Small κλ or small β**: B4 `blocked-time` z ≤ 1/384; `strong-coupling` tanh β ≤ 1/20; A4 `uniform-band`; D4 `finite-readings` λ/κ ≤ √3/512.
- **Explicit fast weak-coupling trajectories**, e.g. β = r¹⁷ or r⁶⁵: C4 magnetic-smearing and lie-curvature, D4 ordinary-loop and electric-slab.
- **b(1+β) → 0 or b²(1+β) → 0**: D4 graph-holonomies, B4 spatial-heat-trace.
- **Abstract**: a convergent regulator sequence or a dense family with a common rate is assumed, not proved (G4 root, D4 root, A4 root).
- **Haar measure and representation are inputs, not constructed**: G4 `wilson/README.md`.

## Failed predicates
- P5 ("every .lean file has `#print axioms`") failed for `central-quotients/Model.lean` (definitions only) and `z4/lean/Z4YM.lean` (an import aggregator). This was my own wrong expectation, not a defect of the target.
- Child: none reported.
- Grandchild: its β-regime statement, kept above as a DEFECT of the grandchild.

## What I did not check
- I compiled no Lean file and reran no program, as the brief says.
- I did not read the full statement .md files; I read the READMEs and the "open / not / remains" lines.
- I did not check numerical constants (except the quoted girth-shell sentence and one Lean declaration count).
- I did not check the external sources (E1/E2, Jofer v4, the assessment PDF).
- I did not verify that the 13 B4 sub-folders contain nothing beyond the child's rows.
- I did not check whether `OVERALL_DISPOSITION.md` predates the later rounds.

## Delegated questions and outcomes
- **Child** (`child/`, Sonnet, register `child/pcp`, my check K1 exit 0, 74 s): index transfer-operator in the same row format; control = number of sub-folders.
  - Control answer 13: correct, graded first.
  - Returned `child/INDEX_B4.md` with 16 rows and 3 inflation notes.
  - My rerun: sub-folder count (13), the girth-shell quote, the `WilsonInfluence.lean` declaration count (20, once `noncomputable`/`abbrev` are counted; a narrower regex gives 19), and the child's registers (`pcp_os verify --ws child/pcp`: PASS; Rust verify: pass line).
- **Grandchild** (`child/grandchild/`): list the B4 files with Lean declarations or "theorem", and the β regime per folder.
  - Control 17·23 = 391: correct.
  - Its declaration counts were reproduced by the child and, for four files, by me.
  - Its claim "no folder treats β→∞ at a fixed lattice" is wrong (`weak-cavity`).

## Rerun commands
```
cd /home/user/z4-workers/a1-idx
python3 -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
P="python3 /home/user/pcp-os/PCP_OS_Python/pcp_os.py"
$P init pcp --principal principal --principal-name "Kirtus Justus"
$P check --ws pcp --name child-run1 --cwd child --timeout 900 -- bash -c "claude -p --model sonnet --allowedTools 'Bash,Read,Write,Edit,Glob,Grep,Agent,Task' < PROMPT.txt"
$P check --ws pcp --name inventory-run1 --expect-exit 0 -- python3 -I inventory.py repo/yang-mills child inventory_result_run1.json
$P verify --ws pcp
/home/user/pcp-os/PCP_OS_Rust/target/release/pcpos verify pcp/register.jsonl
```
The result file is opened with mode "x", so a rerun of inventory.py needs a new output name.

Last line of `$P verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
Last line of `pcpos verify pcp/register.jsonl`: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`

The director, this worker and the child are one model family, so this is not independent review.
