# A normalization defined only through positive times: the Wilson loop on the free benchmark

Director Z4, 23 November 2026. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

Status: statements drafted for attack, before any worker has run. They concern free lattice Maxwell theory only (the setting of [`STATEMENT.md`](STATEMENT.md)), not interacting Yang–Mills.

## Why

B4 reports for a fixed-physical-size probe on the four-dimensional Wilson law (a charged heat trace, a sum of spatial loops) that, normalized to unit variance at one time, its correlation with anything one step away tends to zero, and adds that a normalization defined only through separated positive times is a different question. The free benchmark can answer that question for a loop, exactly.

## Setting

Free lattice Maxwell theory as in `STATEMENT.md`, coupling g, periodic box of side ℓ, spacing b. For a closed lattice contour Γ in a time slice (a planar R × R square in the 1–2 plane), the U(1) Wilson loop of charge one is W(Γ) = exp(i Σ_{links of Γ} A), which by Stokes equals exp(i Σ_{plaquettes p in the square} θ_p) = exp(i g Φ), Φ = b² Σ_p B_3(p) the physical magnetic flux through the square.

Let G_b(t) = ⟨Φ e^{−tH} Φ⟩ = b⁴ Σ_{p,p′ in the square} D_t(p − p′), with D_t the two-point function of B_3 of `STATEMENT.md`.

## Statements

**W1.** The vacuum is Gaussian in Φ, so ⟨W⟩ = exp(−g² G_b(0)/2) and, for t ≥ 0, ⟨W(Γ)* e^{−tH} W(Γ)⟩ = exp(−g² G_b(0)) · exp(g² G_b(t)).

**W2 (sharp time).** G_b(0) grows like c·(perimeter)/b as b → 0 with a logarithmic correction at most (the loop self-energy). Hence ⟨W⟩ → 0, and the variance of W/⟨W⟩, which is exp(g² G_b(0)) − 1, diverges exponentially in 1/b at fixed g. A unit-variance normalization at one time therefore kills every correlation at positive time: the correlation coefficient between times 0 and t is (exp(g² G_b(t)) − 1)/(exp(g² G_b(0)) − 1) → 0. This is the free-theory image of B4's finding.

**W3 (positive time).** For fixed t > 0, G_b(t) converges as b → 0 to a finite positive G(t). Hence the ratio

ρ_b(t) = ⟨W* e^{−tH} W⟩ / |⟨W⟩|² − 1 = exp(g² G_b(t)) − 1

converges to exp(g² G(t)) − 1 > 0 at fixed g. So the normalization "divide by the mean", which uses no sharp-time second moment, gives a finite nonzero positive-time correlator of a fixed-size loop. The vector e^{−τH}(W/⟨W⟩ − 1)Ω has squared norm ρ_b(2τ) and satisfies the hypotheses of S5.

**W4 (the catch).** Along a trajectory with g(b) → 0, ρ_b(t) = g(b)² G(t)(1 + o(1)) → 0: in the free theory the mean-normalized loop correlator vanishes with the bare coupling, and only (W/⟨W⟩ − 1)/g(b), which tends to the linear flux iΦ, survives. A free theory has no scale at which the coupling is of order one. In an asymptotically free interacting theory the corresponding ratio at physical size R is expected to be governed by the coupling at scale R and not by g(b); the benchmark cannot show this, and nothing here does. This is the point at which the free benchmark stops being a guide.

**W5 (decay).** G(t) decays like a power of t in infinite volume (no gap), and in the box at the one-photon rate 2π/ℓ: unlike the quadratic observable of `STATEMENT.md`, the loop couples to one photon.

## What would break this

A wrong divergence in W2 (for example area instead of perimeter); non-convergence in W3; a sign or factor in W1; an error in the claim that ρ needs no sharp-time moment; W5's one-photon rate.


---

# Review record (23 November 2026)

The text above is the draft as handed to the worker, unchanged. One PCP worker with a sub-agent attacked it (register check K26; report and files in [`../reviews/r6-loop/`](../reviews/r6-loop/)); both registers replay. The director reread the report and reran the lattice program in a fresh directory (K29, result file byte-identical).

| Statement | Verdict | Evidence |
|---|---|---|
| Setting, Stokes | stands | Link sum equals plaquette sum to 4·10⁻¹⁶; momentum form equals the position sum to 12 digits at N = 16. |
| W1 | stands | Gaussian algebra; the conjugate matters: without it the cross term changes sign. |
| W2, perimeter law | stands | Fit G_b(0) = c₁·(4R)/b + c₂·log(1/b) + c₃ gives c₁ = 0.32140 (R = 0.25) and 0.32116 (R = 0.125), 0.08% apart; c₂ ≈ −0.20 (corners); residuals ≤ 10⁻³. Not an area law. |
| W2, unit-variance correlation → 0 | stands | At t = 0.05, R = 0.25, g = 1 its decimal logarithm falls from −1.56 at N = 16 to −34.9 at N = 256. |
| W3, convergence at t > 0 | stands, measured | Lattice extrapolation against the sub-agent's independent continuum sum: 10⁻⁶ to 1.9·10⁻⁴ for t = 0.05, 0.1, 0.2 (6 of 6); at t = 0.02 still 4·10⁻³, not yet in the O(b²) regime. |
| W3, "uses no sharp-time second moment" | true as written and misleading | The mean ⟨W⟩ = exp(−g²G_b(0)/2) is a sharp-time one-point function carrying the divergent self-energy: the normalization is the ordinary multiplicative perimeter renormalization. It is determined by positive-time data only through |⟨W⟩|² = lim_{t→∞}⟨W* e^{−tH} W⟩ at each fixed b (clustering; in the box the limit is reached exponentially, in infinite volume like t⁻⁴). |
| W4 | stands as arithmetic | (ρ/g² − G)/G = 0.70, 0.13, 0.031, 0.0077 for g = 1, ½, ¼, ⅛. The remarks on the interacting theory are not checked by anything. |
| W5, box rate | **defect of wording** | Lattice rate is 2N·sin(π/N)/ℓ, below 2π/ℓ by π²b²/6; and the form factor must not vanish at the lowest momentum (true unless R/ℓ is an integer; zeros at n ∈ (ℓ/R)ℤ per axis). The same kind of error as defect 1 of `STATEMENT.md`. |
| W5, power law in infinite volume | derived only | G(t) ≈ R⁴/(π²t⁴) for R ≪ t. |

Counts, as met, failed, measured only: 57, 18, 5. Of the failures, 14 are the worker's own range of N or tolerance at the two smallest times, and 4 are the W5 defect, predicted in its docstring.

## What it says to B4's question

B4 proves for its heat-trace probe on the Wilson law that the correlation coefficient with anything on other slices tends to zero, at every separation, and leaves open normalizations that are not equal-time L². On the free benchmark, for a loop, both halves are visible at once: the correlation coefficient tends to zero (its logarithm falls like −g²c₁·4R/b), and the mean-normalized covariance ρ_b(t) converges to exp(g²G(t)) − 1 > 0. The two are related by ρ = (correlation coefficient) × (variance of W/⟨W⟩), a vanishing factor times a diverging one. B4's bound controls the first factor only; whether the product has a limit for B4's probe at a fixed physical separation is not decided by B4's estimates or by this benchmark. The benchmark differs from B4's probe in kind: W/⟨W⟩ has modulus growing like 1/⟨W⟩, whereas B4's mean-one variable is positive, tends to zero in probability and carries its mean on rare nearly flat cubes.

One model family; not independent review. Nothing here concerns the interacting theory.
