# S12: a compact interacting toy for the exact form of the mixing hypothesis

Compact U(1) lattice gauge theory in 2+1 dimensions on a 2 × 2 spatial torus, blocked to a 1 × 1 torus. It is not SU(2), not four-dimensional, and the coarse lattice has one site. It bears on none of the open hypotheses; it shows the quantities of Remarks 3.6(a) and 3.9 of the paper in one interacting compact model where they can be computed.

| File | Content |
|---|---|
| `u1toy.py`, `u1toy_result.txt` | first program, on the five-torus of gauge-invariant angles; predicates U0 to U3 met. Command: `python3 u1toy.py u1toy_result.txt 0.5:8:12 1.0:8:12 2.0:12:16 3.0:12:16 4.0:16:20 6.0:16:24 8.0:20:24` |
| `PREDICTION.md` | weak-coupling expectation, committed before any result of the run above existed |
| `u1sector.py`, `u1sector_result.txt` | second program, by flux sectors (three angles per sector); predicates S1 to S4 met. Command: `python3 u1sector.py u1sector_result.txt u1toy_result.txt 0.5:12:16 1.0:12:16 2.0:16:24 3.0:16:24 4.0:24:32 6.0:24:32 8.0:32:48 16.0:48:64` |
| `u1sector_trial_failed.txt` | first trial of the second program: its control S1 FAILED (the real part was taken where the operator is complex Hermitian). Kept. |

## Result

| β | lattice gap (one unit of flux) | weight of that state in the fine detail | weight / energy | γ_opt |
|---|---|---|---|---|
| 0.5 | 2.6989 | 0.4409 | 0.163 | 0.99650 |
| 1 | 1.1622 | 0.2845 | 0.245 | 0.96091 |
| 2 | 0.3294 | 0.1021 | 0.310 | 0.89000 |
| 3 | 0.1935 | 0.0640 | 0.331 | 0.86672 |
| 4 | 0.1387 | 0.0469 | 0.338 | 0.85651 |
| 6 | 0.0890 | 0.0306 | 0.344 | 0.84685 |
| 8 | 0.0656 | 0.0227 | 0.346 | 0.84215 |
| 16 | 0.0320 | 0.0112 | 0.350 | 0.83523 |

- The lattice gap closes like 1/(2β) while γ_opt stays above 0.83 over the range computed.
- The two programs agree on γ_opt to relative 1.1e-7 or better at the seven couplings they share.
- Against `PREDICTION.md`: β × energy is 0.512 at β = 16 (expected limit 0.5); weight/energy is 0.350 (expected 0.354); the sector supremum is 1.1973 (expected 1.207 in the limit), so γ_opt = 0.835 against "at most about 0.83". The expectation is a quadratic approximation with one trial vector, not a proof, and the limit of γ_opt as β → ∞ is not computed.
- The maximum is attained in a sector with one unit of flux at every coupling. The sectors with flux (1,1) and (2,0) come closer to it as β grows (1.1888 and 1.1729 against 1.1973 at β = 16); sectors beyond |w| = 2 were not computed.

## Outliers and limits

- In `u1toy_result.txt` the eigenvalue solver returned three, not four, copies of the first excited level on the coarser grid at β = 3, 6 and 8 (it asks for eight eigenvalues and a degenerate copy was missed). The level is fourfold on the finer grids and in the sector program. γ_opt does not use that list.
- Agreement of two programs written in one session by one system is a consistency check, not independent review.

## The ratio weight/energy (added later the same day)

`softweight.py`, `softweight_result.txt` (`softweight_firstrun.txt` is the identical first output, kept because the docstring was corrected after it; see the docstring). The weight of the slow state in the fine detail divided by its energy has a closed form in both models: `1/√8 = 0.353553` for one unit of flux in this toy (extrapolated from β = 64 and 128: 0.353557), and `2/√8 + 1/√24 = 0.911231` for the soft photon of the free theory in three dimensions (0.911230909 at side 2²⁸). β × energy extrapolates to 0.499985. One predicate, read against a mistyped decimal in the docstring, fails; against the closed form all three are met.

## The limit of the rate (added later the same day; an extrapolation, not a proof)

The quadratic approximation of `PREDICTION.md`, evaluated exactly, gives `‖G(I − A²)⁻¹G‖ → 1/(1 − (3 − √8)²) + 1/(4√2) = (1 + √2)/2 = 1.207107`, so `γ_opt → 2(√2 − 1) = 0.828427`. The sector suprema in `u1sector_result.txt` at β = 8 and 16 (1.187438, 1.197279) differ from that value by 0.01967 and 0.00983, a ratio of 2.00, and extrapolate linearly in 1/β to 1.207120. No program was run for this; it is arithmetic on the deposited file.
