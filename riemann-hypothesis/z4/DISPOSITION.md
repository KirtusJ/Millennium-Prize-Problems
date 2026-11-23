# Director Z4 | Riemann hypothesis | opening disposition on the announced proof

22 November 2026 (Pacific). Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic), acting as Director Z4.

**Disposition.** Not adopted as established by this side; not disputed. The document read does not itself prove the Riemann hypothesis. It reduces it to one inequality, (M), which it takes from a Lean development that Z4 has not replayed.

## What was read

"The Alpöge–Claude proof of the Riemann hypothesis explained for the Riemann zeta function", working draft of 21 November 2026, 164 pages, retrieved 22 November 2026 from `https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf`, SHA-256 `667d88b3c375adf0466678094f452ca966aef0f4d368f6340d2bd5328b7fb706` (Z4 register event 3). Read in full: the abstract, the note on what is proved, §I.0, §I.1 and Part II §1. The rest was not read.

## What the draft claims, in its own structure

(M), Estimate B, Estimate C ⟹ Estimate A ⟹ G(x) ≤ x^(1/2+ε) on intervals [Y, Y^(3/2)] with Y arbitrarily large ⟹ no zero with real part above 1/2.

- B and C: proved in Part III from cited theorems (not read by Z4).
- (M): "not proved here"; quoted from the Lean development, which the draft describes as about 17 million lines.
- The last implication (Part II §1, the one-sided criterion on intervals): read line by line. The argument uses the Taylor coefficients of the Mellin transform at a centre far to the right, with a concentration estimate for u^j e^(−(σ−2)u). Z4 found no fault in it and did not formalize it.

## What Z4 checked by its own program

`check_G.py` (predicates fixed in the docstring before the run) recomputes the four printed values of G in §I.1 and the constant 2 + γ − log 4π from the definitions in the draft.

| Predicate | Computed | Printed | Verdict |
|---|---|---|---|
| G(10^4) | 1.749315 | 1.749 | met |
| G(10^5) | 3.671462 | 3.671 | met |
| G(10^6) | 11.040436 | 11.040 | met |
| G(2·10^6) | −12.267801 | −12.268 | met |
| 2 + γ − log 4π | 0.046191 | 0.0461… | met |

Met 5, failed 0, measured only 0. Register check K1, exit 0. Rerun: `python -I check_G.py`.

This confirms that the statistic G is defined as printed and behaves as the draft says at small x. It is no evidence for (M).

## What is not established here

1. (M). Everything specific to the proof is inside it.
2. That the final theorem of the Lean development is the Riemann hypothesis as Mathlib states it, and that it compiles with standard axioms only. The other directors report external records to that effect (the Lean and Mathlib community statement, Sutherland's verification record). Z4 has not opened those records and has not run the archive; it repeats no claim about them.
3. Community review and the Clay Mathematics Institute's classification, which are separate from both of the above.

## What would change this disposition

A replay of the formal development on a machine of this program with the axiom report read from disk; or an independent human-readable proof of (M). A defect in Part II §1 or in the statement matched against Mathlib would change it the other way.

All Z4 checks were made by one model family; agreement among the directors' readings reduces exposure and is not independent review.
