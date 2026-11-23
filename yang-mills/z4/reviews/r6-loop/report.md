# r6-loop report: the Wilson loop on the free benchmark (W1 to W5)

Worker of Director Z4, 23 November 2026. Principal: Kirtus Justus. control.txt = 0.272341.
Register `pcp`: K1 loop_bench (exit 1, expected), K2 rerun_child_continuum (exit 0), K3 compare (exit 1, expected).
`verify --ws pcp`, last line: **result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)**

## Verdict table

| Item | Verdict | Evidence |
|---|---|---|
| Setting: Stokes, W = e^{igΦ} | STANDS | Interior links cancel exactly (algebra in notes.md). Numerically, the link sum equals the plaquette sum to 4e-16. The momentum form with \|F\|² = Π b² sin²(k_iR/2)/sin²(k_ib/2) equals the position sum b⁴ΣD_t(p−p′) to 12 digits at N = 16. |
| W1 | STANDS | BCH algebra (notes.md): ⟨e^X e^Y⟩ = exp(½⟨X²⟩+½⟨Y²⟩+⟨XY⟩), with X = −igΦ, Y = igΦ_E(t), so the cross term is (−ig)(ig)G_b(t) = +g²G_b(t). The conjugate matters: ⟨W e^{−tH} W⟩ = exp(−g²G₀ − g²G_t). Only the W* form is the inner product. |
| W2 perimeter law | STANDS | Fitted c1 = 0.32140 (R = .25) and 0.32116 (R = .125), 0.08% apart. Residuals ≤ 1e-3. Log coefficient c2 ≈ −0.20, present and negative (corners). Local exponent 1.02 to 1.03, so not an area law. |
| W2 correlation → 0 | STANDS | log₁₀ corr at t = 0.05, R = .25: g = 1 goes −1.56 → −34.9 from N = 16 to 256; g = .5 goes −0.77 → −9.35. Strictly decreasing in 4/4 cases. |
| W3 convergence at t > 0 | STANDS (measured, not proved) | Lattice Richardson (N = 128, 256) against the independent continuum sum: rel. 1e-6 to 1.9e-4 for t ∈ {.05, .1, .2}, 6/6. At t = .02 it is 3.6e-3 and 4.2e-3: still approaching, not yet O(b²). |
| W3 ‖e^{−τH}(W/⟨W⟩−1)Ω‖² = ρ_b(2τ), S5 hypotheses | STANDS | Algebra: needs ⟨W⟩ real and HΩ = 0. ρ = Σ g^{2n}Gⁿ/n! is a positive finite sum of exponentials in the box. |
| W3 "uses no sharp-time second moment" | STANDS literally, misleading as worded | It uses the sharp-time one-point function ⟨W⟩ = exp(−g²G_b(0)/2). That carries the divergent self-energy, so the normalization is the multiplicative perimeter renormalization exp(+g²c1·4R/b+…). See L3(a). |
| W4 | STANDS (arithmetic) | (ρ/g² − G)/G lies in [x/2, xeˣ/2] and decreases as g → 0 in 6/6 cases. Example: R = .25, t = .05 gives 0.70, 0.13, 0.031, 0.0077 for g = 1 to 1/8. The claims about the interacting theory are not checked (it says so itself). |
| W5 box rate | DEFECT (wording) | On the lattice the rate is 2N sin(π/N)/ℓ, below 2π/ℓ by π²b²/6. The rate fitted from t = 5→6 matches the lattice value to 9e-7 and misses 2π by 1.0e-4 at N = 128 (predicted). Continuum: 6.2859 at t = 3, approaching 2π. A hypothesis is also missing: the form factor must be nonzero at \|n\| = 1. For a square this holds whenever R/ℓ ∉ ℤ (per-axis zeros at n ∈ (ℓ/R)ℤ: 4, 8 for R = .25; 8 for R = .125). So 2π/ℓ is the rate for both sizes. |
| W5 power law in infinite volume | NOT CHECKED numerically | Derived only: G(t) ≈ R⁴/(π²t⁴) for R ≪ t in infinite volume (∫d³k/(2π)³ k⊥²/(2k) e^{−tk} = 1/(π²t⁴)). |

Counts as met, failed, measured only: loop_bench 40, 16, 4; compare 13, 2, 1; sub-agent (as claimed and rerun by me, byte-identical) 4, 0, 0. Total **57, 18, 5**.

## Hypotheses each statement uses, and where they are stated
- All: free lattice Maxwell, periodic box, zero modes removed, Gauss law (STATEMENT.md, Setting). D_t with normalization k̂/2 (STATEMENT.md review, "stands").
- W1: Φ linear in the oscillators with a c-number commutator, and the vacuum is Gaussian (WILSON_LOOP.md W1, "the vacuum is Gaussian"). HΩ = 0 (implicit, not stated).
- W2: the square has sharp corners. Corners give the log term, which is implicit in "a logarithmic correction at most". Fixed g.
- W3: fixed t > 0 and fixed g. ⟨W⟩ real (implicit, from the Gaussian vacuum). For the S5 hypotheses: finite box and finite lattice, i.e. finite sums (S5 is proved only for finite sums, per the STATEMENT.md review).
- W4: g(b) → 0 along the trajectory (stated).
- W5: a box with ℓ ∉ Rℤ, i.e. a nonzero form factor at the lowest momentum (**not stated**). Lattice dispersion (the O(b²) shift is **not stated**).

## Failed predicates (all kept)
- P2a/P2b/P2c at t = 0.02, both R (6 failures). **My expectation / my range of N**: t·k̂_max < 10 at N = 128, so the O(b²) regime is not reached.
- P2a at t = 0.05, both R (2): non-monotone differences at the coarsest N. **My range of N.**
- P2c at t = 0.05 and 0.1, both R (4): relative change 1.04e-2 to 5.1e-2 against my 1e-2 tolerance. **My tolerance.**
- P5c, 4 failures: rate = 2π to 1e-5. **Defect of the target's wording** (lattice rate 2N sin(π/N)). Predicted in the docstring.
- C2 at t = 0.02, both R (2): Richardson vs continuum 3.6e-3 and 4.2e-3 against 1e-3. **My expectation**, predicted.

## L3 (reasoning, not result)
(a) Is "divide by the mean" positive-time-only? ⟨W⟩ is a one-point function at one time, and here it equals exp(−g²G_b(0)/2), the divergent self-energy. In a theory with a unique vacuum and a gap, or with clustering, |⟨W⟩|² = lim_{t→∞}⟨W* e^{−tH} W⟩, because e^{−tH} → |Ω⟩⟨Ω|. So |⟨W⟩|² is determined by positive-time correlators. In the finite box this works even for the free gapless theory: the spectrum above Ω is discrete with lowest level 2N sin(π/N)/ℓ > 0 (zero modes removed by hand), and G_b(t) → 0. In infinite volume, clustering still holds, but only as a power, G ~ t⁻⁴. The phase of ⟨W⟩ is not determined this way; it is real here by symmetry. The limit is taken at fixed b, and |⟨W⟩|² → 0 as b → 0. So ρ_b is a ratio of two vanishing positive-time quantities whose ratio converges. The normalization is the usual multiplicative perimeter renormalization, and it is obtained from positive-time data only through t → ∞ at each b.
(b) Non-abelian loop: W = tr P exp(i∮A)/d, and the same ratio ⟨W† e^{−tH} W⟩/|⟨W⟩|² − 1. What differs, from textbook knowledge and not checked here: the vacuum is not Gaussian, so W1 has no closed form and there are higher cumulants at order g⁴. The linear perimeter divergence and the corner (cusp) divergences are still multiplicative (Polyakov, Dotsenko–Vergeles, Brandt–Neri–Sato), but the cusp anomalous dimension depends on the coupling. The coupling runs: at fixed physical R the relevant coupling is g(R), not g(b), and confinement gives an area law for large R, which the free benchmark cannot show. The product of loops is not a loop (trace of a product), and there are no gauge-invariant one-photon states. The lowest state reached is a glueball, so W5's "one-photon rate" has no analogue. W4 states this boundary itself.

## What I did not check
- The infinite-volume power law (derived only).
- Any analytic value of c1 = 0.3214.
- The R dependence of c3 (corner log ln(R/b)): rough consistency only.
- t < 0.05 to O(b²) precision.
- All claims about B4, the interacting theory and asymptotic freedom.
- Non-square loops.
- That W3's ratio is the "right" normalization physically.
- Lean was not used.

## Delegated question and outcome
Delegated (L2): G(t) from the continuum mode sum with |k| and F1(q) = 2 sin(qR/2)/q, for R = .25 and .125, t ∈ {.02, .05, .1, .2, .5, 1, 2, 3}, with the truncation shown by M-doubling to relative 1e-6. Control: Σ n e^{−n} = 0.920674. It answered correctly.
What came back: the full table (for example G(0.1) = 0.3221769695 for R = .25 and 0.0748281521 for R = .125), its predicates 4/4 met, and its verify PASS. It reported that writing child/report.md was blocked by the harness, so that file is missing.
What I did with it: I reread continuum.py (formula, octant multiplicities, truncation), reran it in rerun/ through my register (K2), and its output is byte-identical. I then compared it with my lattice values: 13 met and 2 failed, both predicted (t = 0.02).

## Commands to rerun (from C:/Users/donke/z4-workers/r6-loop, PYTHONUTF8=1; move results_*.txt and rerun/results_continuum.txt away first)
```
P=C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py
python $P init pcp --principal principal --principal-name "Kirtus Justus"
python $P check --ws pcp --name loop_bench --expect-exit 1 -- python loop_bench.py
mkdir -p rerun && cp child/continuum.py child/control.txt rerun/
python $P check --ws pcp --name rerun_child_continuum --expect-exit 0 -- bash -c "cd rerun && python continuum.py"
python $P check --ws pcp --name compare --expect-exit 1 -- python compare.py
python $P verify --ws pcp
```
Sub-agent's own (from child/): `python $P check --ws pcp --name continuum --expect-exit 0 -- python continuum.py`, `... --name crosscheck ... -- python crosscheck.py`, `python $P verify --ws pcp`.

Director, worker and sub-agent are one model family; this is not independent review.
