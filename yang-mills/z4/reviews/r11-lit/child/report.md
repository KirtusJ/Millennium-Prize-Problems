# Q4 literature report (SU(2), Wilson plaquette action)
Control: control.txt = 6 unsolved, Poincaré conjecture solved.

| Quantity | Value | URL | Title | Authors | Year | Locator | How read |
|---|---|---|---|---|---|---|---|
| a√σ, β=2.3 | 0.3690(30) | https://arxiv.org/abs/hep-lat/9208012 | Scaling and Asymptotic Scaling in the SU(2) Gauge Theory | Fingberg, Heller, Karsch | 1992 (NPB392) | Table 3 (compilation of others' data, refs [5,6,21-23]) | FULL TEXT |
| a√σ, β=2.4 | 0.2660(20) | same | same | same | 1992 | Table 3 | FULL TEXT |
| a√σ, β=2.5 | 0.1905(8) | same | same | same | 1992 | Table 3 | FULL TEXT |
| plaquette, β=2.3/2.4/2.5 | NOT FOUND at exactly these β. Nearest, same source, Appendix B Table 8 (listed as 1−<Up>, Up = N⁻¹Tr U_p, equal to ½ Tr U_p for SU(2)): β=2.2986: <Up>=0.60254(1); 2.4265: 0.63648(1); 2.5115: 0.65436(1) | same | same | same | 1992 | Table 8 | FULL TEXT (values derived as 1−x) |
| m(0++)/√σ, continuum | 3.78(7) | https://arxiv.org/abs/hep-lat/0404008 | Glueballs and k-strings in SU(N) gauge theories: calculations with improved operators | Lucini, Teper, Wenger | 2004 | Table 14 (O(a²) extrapolation, eq. 27); Table 15 (3.493(56) at a≈0.24/√σ) is NOT continuum | FULL TEXT |

Not used: nothing FROM MEMORY. No ABSTRACT/SUMMARY-only values.

## Computation (prog/check.py, result prog/result_check.txt, PCP check K1 exit 0)
Predicates fixed in docstring before run. P1 (a√σ decreasing): 6/6 pairs PASS. P2 (<Up> increasing): 6/6 PASS. P3 (ratio of a between adjacent β vs 2-loop): 7.9% and 8.5% deviation, PASS at 20% tolerance (my own expectation, no source). P6 (plaquette tabulated at exact β): 0/3 qualify — failure is a property of the source (different β grid), not a defect of my code. No predicate failed otherwise.

## Sub-agent
Asked: locate continuum SU(2) 0++/√σ in one source with table number; control 7*8 -> grandchild/control.txt = 56 (reread, correct). Returned 3.78(7), Table 14, hep-lat/0404008, full text. I reread the PDF text myself: Table 14 confirmed (not independent of my own read of same paper, only independent locating).

## Not checked
Plaquette at exactly β=2.3, 2.4, 2.5 (needs another source, e.g. Michael–Teper or Athenodorou–Teper 2106.00364 not opened); Athenodorou–Teper 2021 and Bloch et al. not opened; Table 3 values are FHK's compilation, original papers [5,6,21-23] not read; whether 3.78(7) matches the published JHEP version beyond arXiv v1; the 2 numbers' errors-in-quadrature conventions.

## PCP verify (last lines)
- Python: `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
- Rust: `A pass is a fact about these bytes. It authenticates nobody and establishes nothing about whether a finding is right.`
