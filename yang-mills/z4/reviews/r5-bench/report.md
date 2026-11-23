# report.md — r5-bench (builder, free lattice Maxwell benchmark)

Control: control.txt = 0.272341. Same model family as the director, so this is not an independent review.

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| D_t formula (k̂/2 normalization, lattice projector) | STANDS | Rederived in notes.md §Step 2. The plaquette-centre phase e^{i(k1+k2)b/2} cancels in \|.\|². A direct N=4 position-space oscillator computation matches the formula to 1.1e-13 at t=0 and 1.2e-14 at t=0.3 (results_b0_1.txt). Notation only: the phase e^{ik·(x−y)} needs a factor b when x is an integer site. |
| S1 | STANDS | Ratios C_b(0)/C_2b(0) = 32.305, 32.080, 32.020 (R=0.1). The fitted exponent is −5.002. C_b(0)b⁵ → 8.110e-3. The R=0.1/R=0.05 ratio of C_b(0)b⁵ → 8.005, against a ∫f² ratio of 8. |
| S2 | STANDS | At t=0.1 and 0.2 the ratios of successive differences are 4.1–5.8. Lattice N=128 agrees with the sub-agent's continuum value within the derived tolerance in 6/6 cases. After Richardson extrapolation the agreement is 2.8e-5 (t=0.2) and 3.5e-4 (t=0.1). The t=0.05 failure is my own choice of N range (see §3). |
| S3 | STANDS | τM1/M0 ≈ 2.6–3.2 and τ²M2/M0 ≈ 8–11.4 for all N, R and τ. Both stay below the S5(a,b) bounds formed with the measured C(τ)/C(2τ), whose ratio is 13–33. They change by less than 1.7% from N=64 to N=128. |
| S4: no gap, decay rate | STANDS | rate(t=3) = 12.5694 against the lowest lattice two-photon energy 4N sin(π/N) = 12.5651 (N=128) and 4π = 12.5664. rate(0.2) = 28.5, which is 2.27×4π, so it is far from asymptotic. |
| S4 wording: "lowest atom at or above 2·(2π/ℓ)(1+O(b²))" | DEFECT (wording, minor) | The lowest atom is 4N sin(π/N)/ℓ, which is below 4π/ℓ for every N (relative −(πb)²/6: −6.4e-3, −1.6e-3, −4.0e-4, −1.0e-4). The statement holds only if the O(b²) term may be negative, so it should say "= 2(2π/ℓ)(1 − π²b²/6 + …)". The no-gap conclusion is unaffected. |
| S5 | NOT CHECKED | No Lean proof attempted. (a) and (b) are respected numerically in all 32 cases tested, which is consistent with them but proves nothing. |
| S6 | NOT CHECKED | Only the leading-order map was derived (B3). A4's scalings were not checked. |

Counts across all predicates (bench + B0 + compare): **met 56, failed 4, measured only 17**.
- B0: 6 met.
- bench.py: 46 met, 4 failed, 9 measured only.
- compare.py: 6 met, 8 measured only.

## 2. Hypotheses each statement uses, and where they are stated

- **D_t.** Uses the Gauss-law subspace with zero modes removed, an H normal-ordered so that e^{−tH} omits the vacuum energy, and B_3 = θ_12/(g b²). All are in STATEMENT.md under "Setting". The normal ordering is implicit there.
- **S1.** Uses fixed f and ℓ, a Gaussian vacuum (Wick's theorem), and f smooth and nonzero. The pass relies on f being a periodic Gaussian (my choice, B1).
- **S2.** Uses t > 0 fixed and smooth f. The O(b²) claim implicitly also needs N large enough that t·k̂_max ≫ 1. The statement does not say this.
- **S3.** Uses S2 at times τ and 2τ, and S5(a,b) for the bounds.
- **S4.** Uses the periodic box and that f̂ is nonzero at q=0. My Gaussian f̂ has full support, so every two-photon pair contributes.
- **B3.** Uses Wilson/Kogut–Susskind normalization with β=4/g² and a magnetic term (4/(g²b))Σ(1−½trU). It is leading order in g.

## 3. Failed predicates (all kept)

1. **P2 R=0.1 t=0.05.** The difference ratios are 1.21 and 4.08. The first must lie in [2,8].
2. **P2 R=0.05 t=0.05.** The difference ratios are 1.08 and 4.14.
   - Cause of both: at N=16, t·k̂_max ≈ 2.8, so the Brillouin-zone edge is not suppressed. C_b(0.05) is non-monotone in N: 181, 266, 195, 178.
   - This is **my own expectation** (the N range I chose), not a defect of S2. At the finest doubling the ratio is ≈ 4, and C_128 agrees with the continuum value within tolerance.
3. **P4c R=0.1.** The literal S4 bound "lowest atom ≥ 4π/ℓ" is false at every N.
4. **P4c R=0.05.** Same failure.
   - This is a **defect of the target's wording**. It was predicted in the docstring before the run.
5. **Sub-agent's first run (child/results_1.txt).** Its K-convergence tolerance of 1e-10 was not met at t=0.05 and t=0.1. This was the sub-agent's own expectation. It raised K, kept the tolerance, and the next run passed.

## 4. What I did not check

- S5 in Lean.
- Any of S6, including A4's variance floor 1/g_A and the g⁴ ~ β⁻² consistency.
- Any f other than the periodic Gaussian, and any ℓ ≠ 1.
- N = 256.
- C(t) for t > 3, and the weights of individual spectral atoms (I identified the lowest atom only from the mode sum and the decay rate).
- Whether S3's "constants" can be taken independent of τ. The ratio C(τ)/C(2τ) that the bounds use does depend on τ and R: 13–33.
- B2 scaling. I observed C_{R=0.05}(t/2) ≈ 4.09–4.16 × C_{R=0.1}(t). This is close to dimensional R⁻²Φ(t/R) scaling, with corrections that grow with t/ℓ. At equal t the ratios are 8.7, 10.3 and 14.9, which is not a power law. C_b(0)b⁵ scales as ∫f² ∝ R³. I am reporting this, not asserting a law.

## 5. Delegated question and outcome

**Question given to the sub-agent** (child/, with its own register child/pcp): compute the continuum C(t) = 2∫∫ f f D_t² with |k| in place of k̂, summed over (2π)ℤ³\{0} with a spherical cutoff K. Show convergence. Use R=0.1 and R=0.05, and t=0.05, 0.1, 0.2. Also give the rate at t=0.2. The control question was ζ(4), and it answered 1.08232323, which is correct.

**What came back:**

| R | t=0.05 | t=0.1 | t=0.2 |
|---|---|---|---|
| 0.1 | 173.8421037813 | 4.948433874175 | 0.1156056947885 |
| 0.05 | 19.83909156316 | 0.4774571289731 | 0.007740640883549 |

- K-convergence is between 1e-12 and 6e-11.
- Rate at t=0.2: 28.50632 (R=0.1) and 31.96571 (R=0.05).
- Its verify result was PASS.

**My checks:** I read corr.py and reran it (child/results_3.txt). The output is identical. Its method is independent of mine: analytic |f̂|², a spherical |k| cutoff, and an FFT linear convolution with no wrap-around.

**Comparison** (results_compare_1.txt): 6/6 agree within tolerance. C128/C_cont − 1 is +2.5e-2, +6.6e-3 and +2.1e-3 for t = 0.05, 0.1, 0.2. The lattice approaches the continuum from above, at a rate consistent with O(b²).

## B3 (leading order only; this is not a result about the interacting theory)

½tr U_p = cos(|θ|/2) = 1 − (1/8) g² b⁴ Σ_{a=1}^{3} (B^a)² + O(g⁴b⁸B⁴). This uses θ^a_12 = g b² B^a_3 and the 3 = dim SU(2) colour components.

- The constant is **1/8** for the normalized character, or 1/4 for the plain trace tr U.
- At Gaussian order the colours are independent, so C_YM = 3 (g²b⁴/8)² C_b.
- S6's Z(b) = const/(g²b⁴) therefore has const = 8 in magnitude, with a negative sign, at leading order.

## 6. Exact commands to rerun

From C:/Users/donke/z4-workers/r5-bench with `export PYTHONUTF8=1`:

```
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name b0_check --expect-exit 0 -- python b0_check.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name bench --expect-exit 0 -- python bench.py
(cd child && python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name corr --expect-exit 0 -- python corr.py)
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name compare --expect-exit 0 -- python compare.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```

Notes on rerunning:
- Each run writes the next free results_*_k.txt.
- compare.py reads results_bench_1.json and child/results_3.txt.

**Last line of verify:** `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
