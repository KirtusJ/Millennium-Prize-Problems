# Child report (spectral-support lane)
NOTE: written by the PARENT (r4-c) verbatim-in-substance from the sub-agent's returned text, because the harness refused the sub-agent's own write of this file ("Subagents should return findings as text"). See child/notes.md.

Control: 0.272341. Verify last line: result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)
Counts: 11 .md in spectral-support (+ yang-mills_README.md); 8 state a result, 3 execution logs; 12/12 read in full.

| # | file | regime | group/dim | evidence |
|---|---|---|---|---|
| 1 | README.md | CONDITIONAL (common rate r on dense family; l.50 "No rate ... has been derived") | abstract | 6 Lean decls (5 analytic + 1 finite cert); continuous map, scalar measures, spectral identity are inputs (l.21); exact rational checker; 3 mutations rejected |
| 2 | diagonal/README.md | CONDITIONAL (weak conv. of cutoff spectral measures, common clock, dense diagonal estimate, reconstruction; l.23) | abstract | 5 Lean decls; weak conv. analytic (l.17); 3 mutations rejected |
| 3 | positive-time/README.md | CONDITIONAL (late envelope, same observable/trajectory, dense family; l.35); Wilson sub-claim ONE-LIMIT (time step), resting on B4 | abstract; sub-claim SU(2) 4D lattice | 15 Lean decls (shared with 4); Wilson-to-transfer analytic (l.23); 5 mutations rejected |
| 4 | positive-time/thin-loops.md | FIXED | SU(2), 4D lattice | text proof; Lean last Hilbert step + Markov only; Wilson factorization, graph bound analytic (l.16); enumeration 3^4,4^4,5^4; 1 mutation rejected (4->3) |
| 5 | positive-time/vacuum/README.md | CONDITIONAL (envelope, reconstruction, vacuum uniqueness "separate inputs", l.15) | abstract | 5 Lean decls; 4 mutations "exercised" (rejection not stated) |
| 6 | adjoint-band/README.md | ONE-LIMIT (spatial volume; mesh fixed, continuous time) | SU(2)/SO(3) 3+1 Hamiltonian | 13 Lean decls (scalar/measure steps only); Haar, domains, spectral thm analytic; numerical checks; 4 mutations rejected |
| 7 | adjoint-band/wilson-limit.md | JOINT (a_j->0 and n->inf along selected j(n)>=J(n), "no stated rate"; spatial mesh fixed) | SU(2)/SO(3), 4D Wilson | text proof; Lean selection theorem + counterexample; 1 mutation rejected |
| 8 | adjoint-band/review.md | ONE-LIMIT (time step, fixed volume) headline; others FIXED | SU(2); one item general compact | numerical (40 matrix tests, 2.31e-13; 1 sign mutation rejected); replays 53 other-agent Lean decls covering "selected steps" (l.35) |

Requirements: (a) PARTIAL (time step + volume only; wilson-limit l.19 "Spatial spacing remains fixed throughout"); (b) NOT ADDRESSED; (c) NOT ADDRESSED; (d) NOT ADDRESSED; (e) PARTIAL (conditional criteria; README l.50); (f) NOT ADDRESSED (SU(2) only). CLAIMED: none.
Contradictions/conventions: (1) positive-time/README strong-coupling l.19-23 (all connected autocorrelation limits vanish) vs wilson-limit l.11 / README l.58 (band survives a Wilson time refinement), parameterizations not reconciled; (2) adjoint-band/README l.7 -(k/4)Delta vs wilson-limit l.3 B4 convention, conversion kappa_B=2/kappa only in review.md l.7; toolchains Lean 4.24.0/f897ebc and 4.19.0/c44e0c8 mixed.
Flagged for review: execution.md l.22 "Independent scientific assessment requires a separate reviewer"; adjoint-band/execution.md l.15,17 (analytic steps not in Lean); thin-loops.md l.16 (Wilson factorization, graph bound analytic).
