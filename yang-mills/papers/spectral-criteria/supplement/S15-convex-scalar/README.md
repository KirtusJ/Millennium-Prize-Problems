# S15: a scalar field with a convex interaction

Programs and outputs for the proposition on convex interactions at the end of Appendix E of the paper: for `H = −½Δ + ½⟨φ,Kφ⟩ + V(φ)` with `V` convex and any linear block map `B` with kernel `N`, `I − P ≤ (H − E₀)/λ_N`, `λ_N` the lowest eigenvalue of `K^{1/2}` compressed to `N`, with equality of the best constant for `V = 0`.

| File | What it does |
|---|---|
| `convexscalar.py` | Two sites and three sites on a grid; the best constant for a list of convex `V` and two on-site double wells. Output `convexscalar_result.txt`. Command: `python3 convexscalar.py convexscalar_result.txt` (about ten minutes). |
| `convexscalar_trial1.py`, `convexscalar_trial1_progress.txt` | The first version and its log. It factorised the three-site operator directly and was killed for lack of memory before producing a number for three sites. |
| `convexscalar_lib.py`, `convexscalar2.py` | Follow-up: a double well in the fine direction. Output `convexscalar2_result.txt`. |
| `blockscalar.py` | Block sums of a massless free field in dimensions 1 to 3: `λ_N` per coarse momentum. Output `blockscalar_result.txt`. |

## Outcomes, including the predicates that failed

- **V3 (the statement) met**: in all sixteen convex cases the computed constant is at most `1/λ_N`. For the quartic interaction with coefficient 0.1, 1, 10 it is 0.906, 0.673, 0.378 of `1/λ_N` on two sites and 0.922, 0.706, 0.407 on three.
- **V1 met, V2 failed, and the failure was mine.** V2 stated as a "known answer" that the free constant on three sites is `⟨e,ωe⟩/⟨e,ω²e⟩ = 0.593306`. That is the largest ratio of norm to energy over one-particle states *inside* the fine detail. The best constant in `I − P ≤ κH` is `‖(I−P)H⁻¹(I−P)‖`, which on the same states is `|n|²/⟨n,ωn⟩`, and its supremum is `1/λ_N = 0.612899`. The program computed 0.613060, which agrees with `1/λ_N` to the accuracy of the grid (3.7e-4 between the two grids). So the bound of the proposition is an equality for `V = 0`, for every block map, and the paper says so. On two sites the two expressions coincide, which is why V1 did not show the mistake.
- **V4 failed in one case**: quartic coefficient 10 on three sites changes by 3.0e-3 between the grids of 49 and 61 points, above the 2e-3 allowed. The value is 0.41 of the bound, so the conclusion does not depend on it.
- **X1 not as expected**: the two on-site double wells do not violate the bound (0.78 and 0.28 of it). Their slow motion is a common sign change of both sites, which the block variable `φ₁ + φ₂` sees.
- **Follow-up (`convexscalar2.py`)**: with the double well in the fine direction, `V = λ((φ₁ − φ₂)² − v²)²`, the constant is the inverse tunnelling splitting: 2.50 at (λ, v) = (0.25, 2) and 5845 at (0.5, 2.5), against `1/λ_N = 0.667`. **W2 failed as written** because the third case, (1, 3), has a splitting of 2e-13, below what the program resolves; the first two cases behave as expected.
- **`blockscalar.py`**: B1 to B3 met. `λ_N = 2 sin(π/2r)` exactly, at the edge of the coarse Brillouin zone, in dimensions 1, 2, 3. The quantity printed as `kappa_free` is the one-particle ratio of the mistaken control above; it happens to coincide with `1/λ_N` here because the extremal field is an eigenvector of `ω`.

## The version with a time step (`convexstep.py`): an interrupted run

For the second proposition (the transfer operator `T = e^{−aW/2} e^{aΔ/2} e^{−aW/2}`; `I − A² ≥ γ₀(I − P)` with the free rate `γ₀`). **The run was stopped before it finished and wrote no result file.** What it had printed is kept as `convexstep_interrupted_log.txt`; a complete run in a fresh directory is still owed (`python3 convexstep.py convexstep_result.txt`, several hours for the three-site part on four cores).

What the log contains:
- Two sites, time steps 1 and ½, all cases: the free control D1 is met to eight figures (0.93750000 and 0.76936027); for the seven convex interactions the ratio of the best rate to `γ₀` is between 1.000000 and 1.06 at step 1 and between 1.000000 and 1.25 at step ½ (statement D3, no violation); the double well in the fine direction gives 0.51 and 0.39 (expectation X1, as expected).
- Three sites, time step 1 only: the free control D2 is met to eight figures (0.94807078), and the quartic interaction with coefficient 0.1 gives a ratio 1.0094. The other six interactions at step 1 and all of step ½ were **not computed**.

So D1 is met, D2 is met at one of its two time steps, and D3 is untested for thirteen of its sixteen three-site cases. The paper states exactly this.
