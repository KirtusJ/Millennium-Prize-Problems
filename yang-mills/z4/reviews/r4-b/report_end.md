
### g4 vs. requirements (from the sub-agent; checked by me against the files I read)

| Req. | Disposition | Evidence |
|---|---|---|
| (a) continuum limit on R⁴ | NOT ADDRESSED | There is only a preservation lemma that applies once a limit exists. README §Shared contract item 3 lists convergence as an obligation. |
| (b) RP / OS | ADDRESSED AT FIXED REGULATOR (RP only) | RP on the finite open slab (open-slab.md, wilson-kernel.md; analytic). PARTIAL: Lean-checked closure under limits, conditional on the limit existing. The other OS axioms "remain open" (integral/README §Coordination). |
| (c) Euclidean invariance | NOT ADDRESSED | no statement in the lane |
| (d) nontriviality | NOT ADDRESSED | "positive forms may still give a trivial limit" (integral/README) |
| (e) mass gap, physical units | NOT ADDRESSED | Only a control showing that RP plus clustering does not force a gap: K = 1/(1+s+t) (README §Controls) |
| (f) all compact simple groups | PARTIAL | RP at fixed regulator for any compact second-countable G (analytic); group scope is assigned to C4 |

CLAIMED in either lane: none.

## 4. Hypotheses each statement uses, and where they are stated

- **T1:** three sector form bounds with c² ≤ (u−m)(v−m) and u > m (README.md §"What the regulator must supply"). The spectral theorem is "the analytic interface".
- **T2, T4, T5:** SU(2); spatial mesh fixed; L ≥ 2; a ≤ κ/4; z ≤ 1/384; β_t = κ/a, β_s = aλ (blocked-time/README.md ¶1). The Dobrushin comparison is cited, not formalized (blocked-time/execution.md table).
- **T3:** G compact connected with faithful π; a/κ ≤ h0 and κλ ≤ 1/[120(T+1)], where T and h0 exist but are not explicit (compact-groups.md ¶2). Uses the Li–Yau heat bound.
- **T6:** fixed spatial mesh and finite volume for a → 0. The gap needs 8z below Yarotsky's Theorem 1 threshold, to which the note says "We do not assign a numerical value" (hamiltonian-time/README.md §"A volume-independent gap").
- **T7:** z ≤ 1/384 or z ≥ 36; L ≥ 2 (plaquette.md).
- **T8–T10:** ac ≤ 1/36, a ≤ t/2, c = 6λL³ + 6/κ (joint-cutoff/README.md ¶1; evolution.md ¶1). No gap hypothesis.
- **T11:** A4's common first-moment bound, which comes from another lane (energy-density.md §"A comparison", last para).
- **T12:** L even (spatial-plaquette/README.md ¶1).
- **T13:** tanh β_s and tanh β_t ≤ 1/20; open time slabs (strong-coupling/README.md ¶1).
- **G1–G6:** as in the rows above. child/g4_disposition.md quotes each location.

## 5. Failed predicates

None of my predicates failed (P1 and P2 in count_files.py), and the child's g4-count predicate passed.

The lanes record their own failures:
- **transfer-operator:** rejected mutations; the tilt-4 row 2311/1920 > 1 (blocked-time/execution.md); the R = 4 tilt is infeasible (strong-coupling/README.md). These are limits of the authors' own estimates.
- **g4:** the first draft failed elaboration; a CRLF parser bug; a diagnostic-matcher failure (g4/execution.md; integral/execution.md). These were defects of the tooling, not of the statements.
- **g4, open-slab.md §Adverse:** an audit found that end weights must be gauge invariant. This was a defect of the stated theorem, and the note was corrected.

## 6. Contradictions or incompatible conventions without a stated conversion

No outright contradiction was found. These conventions clash with no stated conversion:

1. **κ has two meanings.**
   - transfer-operator/spatial-plaquette/README.md §"Consequence for a transfer estimate": κ is the *spatial* action coefficient, in the multiplier exp(−κV/2).
   - transfer-operator/hamiltonian-time/README.md ¶1, and the rest of the lane: κ is the electric parameter, with β_t = κ/a and β_s = aλ.
   - Read with the lane's usual κ, the spatial-plaquette b = e^{−κN_p} is misread.
2. **γ has two meanings.**
   - hamiltonian-time/README.md §"A volume-independent gap": γ is the Yarotsky gap constant (gap ≥ 3γ/(8κ)).
   - joint-cutoff/energy-density.md §"Capping": γ = 1/(2κ) is the kinetic coefficient.
   - energy-density gives its own conversion to A4's convention but does not address this clash.
3. **The cross-lane coupling normalization differs.**
   - transfer-operator uses exp(β ReTr U_p/2) for SU(2) (strong-coupling/README.md §1) and ReTr π/dim π (compact-groups.md ¶2).
   - g4 uses β_p c_p ReTr with c_p > 0 never fixed (g4/integral/wilson-kernel.md §Statement; open-slab.md §Splitting).
   - No conversion between the β conventions is given. The sign conventions agree: both use exp(+β ReTr), and g4 states its conversion to exp(−S).
4. **The cross-lane time units differ.**
   - transfer-operator states gaps in physical time units of κ (blocked-time/README.md).
   - g4 uses dimensionless slice labels and never relates them to a or to physical time (g4/integral/README.md §Coordination, B4 bullet).
   - The child also lists clashes inside g4: c_p is never fixed, and the weight form behind β = log 2 is not stated (child/g4_disposition.md §Contradictions).

**Points where the lanes agree:**
- transfer-operator/blocked-time/compact-groups.md §"Open time reflection" says it verifies G4's split-action hypothesis for the open slab. This matches g4/integral/open-slab.md.
- Both lanes warn that observables built from blocked or auxiliary-seed variables must be pulled back from Wilson histories.

## 7. Three statements per lane that the lane's own text marks for review

**transfer-operator:**
1. The time-slice-to-spectrum step: the spectral theorem plus density of centered multipliers in the vacuum complement. README.md §1 calls it "the analytic interface"; strong-coupling/README.md §Verification lists it as analytic.
2. The Dobrushin comparison on the lifted bridge measure, together with the open-time limit. These carry the uniform gap; blocked-time/execution.md lists them as "Analytic steps supplied in the notes".
3. Whether Yarotsky's theorem applies, since its threshold is not quantified (hamiltonian-time/execution.md: "applicability of the external stability theorem … analytic"). The Li–Yau minorization behind the general-group extension is in the same position (compact-groups.md).

**g4** (from the child; I checked these against integral/execution.md and open-slab.md):
1. The matrix-feature expansion and uniform tail bound in wilson-kernel.md, which are "not Lean formalized" (integral/execution.md §Corrections).
2. The open-slab identification. It is analytic, and its first audit already found a missing hypothesis.
3. The pushforward RP identity and the conditional reviews of B4 and D4, which are not replays (cross-lane-review.md; complex/README.md §Connection).

## 8. What I did not check

- Whether any proof is correct. This was out of scope.
- Any Lean file. None is in input/, so all Lean and mutation counts are as the notes report them.
- Any external link: the rendezvous issue, the A4/C4/D4 sources, Yarotsky, Lüscher.
- The full text of the 3 g4 execution logs. I grep-checked them for counts only.
- The Python scripts and replays the notes cite.

## 9. Delegated question and outcome

**Question delegated (rule 7):** apply the same extraction template to the smaller lane, input/g4 (9 files). The child was to answer a control question first (−ln tanh 1), work in child/, and keep its own register at child/pcp.

**What came back:** child/g4_disposition.md, with 6 result rows, a requirements table, conventions, and review targets. Its control value was 0.272341, which is correct.

**My checks of the result:**
- I reran child/count_files.py: exit 0, 9 files.
- I reran the child's register verify: "result: PASS (…)".
- I checked 6 rows against the files, one more than the 5 required: README, cross-lane-review, complex/README, integral/README, wilson-kernel and open-slab. **6 of 6 matched**: statements, regime classes, quotes, and the counts (8+3 thm/def with 1 mutation; 24+9 with 4; 28+3 with 5; C4 arithmetic 4096/32/128/8177/2048 and 46/35×6).

**Differences:** none material. The child classed G1, G3 and G4 as CONDITIONAL, which is the stricter reading, and I kept it.

## 10. Commands to rerun

```sh
cd C:/Users/donke/z4-workers/r4-b
export PYTHONUTF8=1
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name file-count --expect-exit 0 -- python count_files.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
cd child && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name g4-count --expect-exit 0 -- python count_files.py && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```

The register was created with `pcp_os.py init pcp --principal principal --principal-name "Kirtus Justus"`. The method was reported as not pinned, which is expected. count_result.txt is written only if it is absent, so the result file is never overwritten.

Last line of my `pcp_os.py verify --ws pcp`: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
