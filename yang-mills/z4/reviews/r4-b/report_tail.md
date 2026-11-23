## Lane table: transfer-operator vs. the problem requirements

| Req. | Disposition | Evidence (location) |
|---|---|---|
| (a) continuum limit on R⁴ | PARTIAL: only the time cutoff and spatial volume are removed, at a FIXED spatial mesh (blocked-time/README.md; joint-cutoff/README.md). Spatial refinement gives only obstructions | "Isotropic removal … and reconstruction of four-dimensional Yang–Mills theory remain open" (joint-cutoff/README.md, last para); local-limit.md: on κ=βb with β²≤1/384 the gap diverges and only contact terms survive |
| (b) reflection positivity / OS | ADDRESSED AT FIXED REGULATOR | open-slab time reflection gives the split crossing action (compact-groups.md §"Open time reflection"); positive transfer at fixed L (hamiltonian-time/README.md §Transfer). No other OS axiom is addressed |
| (c) Euclidean invariance | NOT ADDRESSED (negative tests only) | rotation-test failure in the uncoupled model (hamiltonian-time/README.md §"An explicit spatial refinement"); "Euclidean covariance … remain open" (local-limit.md) |
| (d) nontriviality | ADDRESSED AT FIXED REGULATOR | plaquette connected correlation ≥ (5/9)e^{−12t/κ} at fixed mesh (plaquette.md; local-limit.md); "A fixed spatial mesh is essential" (plaquette.md last para) |
| (e) mass gap > 0, physical units | ADDRESSED AT FIXED REGULATOR (fixed spatial mesh; uniform in L and a, in physical *time* units κ) | gap ≥ 4log3/(13κ) (blocked-time/README.md); on the tree-level spatial trajectory it diverges as 1/(βb) (local-limit.md); finite-volume floor → 0 as L grows (finite-volume-vacuum.md). README.md: "No continuum mass gap or Millennium solution is claimed here." |
| (f) all compact simple groups | PARTIAL: every compact connected G with a faithful rep, fixed mesh, non-explicit (G,π)-dependent T, h0 (compact-groups.md); Hamiltonian gap via Yarotsky for compact simple G (hamiltonian-time/README.md); explicit constants only for SU(2) | strong-coupling/README.md: "quantifier over compact simple groups remain[s] open" |

No requirement is CLAIMED for the 4D continuum theory anywhere in the lane.
