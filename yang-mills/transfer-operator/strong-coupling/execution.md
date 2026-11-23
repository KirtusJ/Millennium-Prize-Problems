# Replaying the strong-coupling estimate

The recursive PCP desk recorded a root supervisor, its generation child, and two grandchildren. The incidence worker enumerated oriented faces and generated the spatial and temporal row formulas. The certificate worker booted PCP OS with the denominator 15 supplied as a one-byte job. Its freestanding program searched for a numerator $m$ such that both endpoint rows for $h=m/15$ were at most $449/450$ after normalization. For an input denominator $d$, clearing the two denominators gives $345d+60m\le449d$ and $540d\le314m$. At $d=15$ only $m=26$ passes. The guest emitted the witness, the two inequalities and their Lean proof. The generation worker booted another measured PCP OS kernel to assemble both generated sections with the remaining director-authored source. The root matched the full 10,613 bytes, ran Lean on the host and then checked five altered sources. All four hosted desk entries finished at revision 8. [Recorded read-back](readback.txt) · [Native certificate source](certificate.c) · [Hosted incidence worker](incidence.py)

| Item | Observed value |
|---|---|
| Kernel and OS sources | Pinned public kernel and PCP OS revision from the [initial calibration](../execution.md); both serial measurements matched the loader. |
| Weight-search ELF SHA-256 | `2110fed60680a09cb8ac9aa3e2e4597a8796cec01116b39e6fd15a0176dc325e` |
| Assembly ELF SHA-256 | `1cb649a9954be008a7f74ada3fb1494f1949d7947b85bf221875c655ea59afcd` |
| Assembled Lean SHA-256 | `6d8514adeffd390d35c496a309db6108f07ccbaf01ba1432252762cf83c4c44f` |
| Lean and mathlib | Lean 4.19.0, mathlib `c44e0c8ee63ca166450922a373c7409c5d26b00b`. Fourteen declarations passed. Each used exactly `propext`, `Classical.choice` and `Quot.sound`. |
| Mutations | Substituting unit height and raising the time tilt from three to four independently caused the row proof to fail at line 67. Halving the two-plaquette oscillation constant and reversing the later-moment comparison also failed in their own proofs. Including the optimized tilt endpoint in the strict contraction criterion also failed. |

The open-slab worker checked all rows on spatial sides 2, 3 and 4 with five time slices. The maximum normalized spatial and temporal rows were $449/450$ and $129/130$ in all three cases. At spatial side 2 an interior row can have only 15 distinct neighbors among 18 incidences. On the $3^3$-by-5 torus the naive time tilt raised the maximum spatial row to $1426/75$. For a bulk link in each of four orientations the worker separately varied every one of 18 neighbors between the two central values. Exact sixth roots of unity reproduced all 72 pairs of signed unit staples. The general counting and Gibbs arguments are given in the [mathematical note](README.md).

Run from this directory using the completed output of the [two-sector replay](../execution.md). The runner creates a fresh output directory, keeps both serial logs and all Lean logs, and checks the pinned kernel, assembly ELF and source revisions. Python 3.10 or newer is required.

```sh
(cd "$MATHLIB" && lake exe cache get Mathlib/Algebra/Order/BigOperators/Group/Finset.lean Mathlib/Analysis/SpecificLimits/Basic.lean Mathlib/Data/Real/Pi/Bounds.lean Mathlib/Tactic/Linarith.lean Mathlib/Tactic/Ring.lean)
PYTHONDONTWRITEBYTECODE=1 python3 replay.py "$TRANSFER_RUN" "$PCP" ./strong-coupling-run
```
