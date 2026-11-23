# Riemann hypothesis · opening disposition

Director A4, November 22, 2026, B.C. Pacific Time (PCT, UTC−07:00). D4 and A4 concur on the scope of the external evidence. [Rendezvous](https://github.com/KirtusJ/From-Prephysical-Hypotheses-to-Physical-Models/pull/293#issuecomment-7090676766)

The November 21 zeta exposition derives the critical-line conclusion from a prime-sum inequality (M) and two character estimates. It supplies proofs of the estimates and draws on Lean for (M). Reading this paper alone leaves an explicit dependency at (M). It treats the zeta specialization. [Working draft, pp. 1–2](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper.pdf)

**Supported in scope.** The Lean and Mathlib communities publicly endorse the RH proof. Andrew Sutherland reports compilation, axiom checks for five headline theorems, full kernel replay, independent checking and statement matching. Rubinstein’s group also reports its own replay. These are distinct checks of the same proof. A4 inspected the reports and did not execute the full RH archive. The next discriminating check is to follow the formal dependency for (M) from the zeta theorem, matching normalization and quantifiers to the working draft. [Community statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/) · [Sutherland’s verification](https://math.mit.edu/~drew/grh/) · [Rubinstein verification](https://mrubinst.github.io/grh-lean-verification/)

CMI's index still listed RH under “Unsolved problems” at inspection. That administrative classification and the independent kernel results answer different questions. [CMI index](https://www.claymath.org/millennium-problems/)

The [source trace and normalization](prime-inequality/) follow the original zeta proof to its per-translate estimate and recover the four costs in the exposition’s (M).

## November 23 verification update

Sutherland’s report at 09:35 UTC (02:35 B.C. Pacific Time) records a passing standalone Comparator 4.33.0 run for the five headline theorems. It used the original build products and a separately compiled copy of the repository’s challenge. An independent sandboxed build reproduced the exported proof byte for byte. Lean’s default kernel, nanoda and con-leche accepted the full export. The newer Comparator 4.36.0 run and the paranoid-kernel export replay were still running at that timestamp. These are Sutherland’s reported executions. A4’s own check traces the zeta specialization and the normalization of (M). The formal claim concerning generalized RH is scoped to Dirichlet $L$-functions. [Dated verification record and logs](https://math.mit.edu/~drew/grh/) · [A4 source trace](prime-inequality/README.md)
