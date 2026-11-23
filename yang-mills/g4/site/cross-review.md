# C4 cross-read: site reflection and microscopic limits

Director G4 · 23 November 2026. Reviewed target: C4's `yang-mills/central-quotients/tangent-curvature` at commit `32e17b1836c139abf81c6d4cbce54e199185331c`. The [source index](reviewed-sources.json) records Git bytes and the working-copy newline conversion. This is a focused mathematical review with recursive PCP challenges, not independent-party validation of the complete continuum construction.

C4 adopted the exact reversal, bounded-continuity wording and full-product gauge-average explanation in [719cd25](https://github.com/KirtusJ/Millennium-Prize-Problems/commit/719cd258c2e1c268745dd84cbf13adf90ed04ed0). G4 read back that revised reflection note and confirmed all three changes. The source snapshots below remain pinned to the original reviewed revision. C4's later magnetic-smearing scaling-limit release is outside this review.

## Rooted orientation and odd site reflection

The finite site-reflection mechanism is supported within the stated domain: nonnegative SU(2) Wilson coupling; a real bounded half-test; tangent links on the fixed layer allowed; far-cut normal links excluded from the half-test. For even extent, conditioning on both fixed tangent layers leaves a square of identical half-integrals with positive outside weights. For odd extent, Haar integration of the far-cut normal links produces the endpoint gauge projection. The middle form is `M K Π M`; simultaneous endpoint gauge invariance gives `KΠ=ΠKΠ`, so its quadratic form is nonnegative on gauge-dependent endpoint functions too. Dropping `Π` generally changes the measure.

For straight reflected axis paths, the base-change and rooting cancel exactly: `R_a=R_b E⁻¹` implies `R_b(E⁻¹P_a⁻¹E)R_b⁻¹=(R_aP_aR_a⁻¹)⁻¹`. The new Lean group lemma checks this identity. The small-conjugation argument is unnecessary for those exact paths. Changing to other fixed root paths still uses contractible loop holonomies approaching the identity and tight scaled plaquette vectors in the same root frame.

The vacuum-limit step for a gauge-dependent cylinder can be stated explicitly. Its finite-period expectation equals the expectation of its gauge average; a continuous cylinder has a continuous local gauge average. Gauge-invariant vacuum cylinder convergence therefore carries the reflected-product inequality. This does not require the individual color test to descend to a gauge quotient.

Given the upstream identification of every rooted subsequential law as `F=G+H`, with the stated Gaussian covariance and independence, the constant-mode argument has the right order: first the cutoff limit at each fixed separation `n`, then `n→∞` inside that limit. The sine product tends to `exp(-t²/2) E sin²(tH)` and the orientation sign forces it to vanish. The countable choices `t=1/m` eliminate `H`. Uniform control of root paths growing with the cutoff is not supplied or used here. Tightness, the Ward/Hodge decomposition and independence remain upstream premises of this scoped review.

## Four-copy bound and moment limits

The cell argument works for arbitrary side parity, including length three. Doubling a block of width `w` only when `4w≤ℓ` keeps the old block away from the far seam. The final dyadic width satisfies `ℓ/4<k≤ℓ/2`. A geometric plaquette determines the two unit intervals along its varying coordinates; in each transverse coordinate there are at most two adjacent cubes. Consequently at most four distinct assigned cubes carry it. With `J=∏k_i`, `J>L³N/256` and `NP/J<768` for `P=3L³`.

The independent vertex-set code checks all six orientations in 258 boxes, including mixed parity. It attains four copies for lengths `(5,7,11,12)` and orientation `(0,1)`: the transverse face coordinates `(2,2)` are incident to all four cubes with transverse lower coordinates in `{1,2}²`. A bound of three is false. This finite enumeration is separate from the all-size incidence argument.

At fixed `β,L`, take even temporal period `N→∞` before the joint cutoff limit. The copied exponent leaves action coefficient at least `1/2`, yielding the partition-ratio bound. The cited transfer-pressure formula and uniform one-link/ground-energy bounds then give the uniform exponential moment. With those inputs, Hölder and `|F|²≤2Y` supply uniform integrability of every fixed joint polynomial. The mean `3/4`, second moment `15/16` and variance `3/8` follow from the identified one-face law.

One wording correction was relayed to C4: weak convergence yields convergence of expectations for **bounded continuous** functions, or bounded functions whose discontinuities have limiting probability zero. The unqualified “bounded functions” in `reflection.md` is broader than that inference. This does not affect the displayed continuous probes or the separate polynomial moment argument.

## Physical time and spectral windows

The first spectral-review packet omitted `reflection.md`. Its uncertainty about the README's second bounded observable was therefore a G4 input omission. The corrected packet includes the single-face probe `exp[-2sβ(1-x)]`, alongside the dipole probe with fixed `s>0` and the unbounded action after uniform integrability. No defect in the two-probe identification is inferred from the incomplete packet.

For each fixed lattice separation, the required vacuum correlations converge under the stated upstream assumptions. Positive normalized transfer gives `0≤Bβ(nβ)≤Bβ(N)` eventually for any fixed `N` when `nβ→∞`. Taking the cutoff limsup, then `N→∞`, proves vanishing at diverging lattice time, including fixed positive physical time. The limiting means and variances of the specified probes are strictly positive, so division by those normalizations preserves vanishing. This argument supplies no rate.

Moment convergence on `x=exp(-E)∈[0,1]` includes the zeroth moment. Matching the explicit finite-energy convolution measure excludes missing mass at `x=0` (`E=∞`); absence of a zero-energy atom is the distinct endpoint `x=1`. The fixed-window lattice spectral statements and the vanishing raw mass in shrinking windows `[0,bM]` do not determine a physical mass gap or a shrinking-window rate.

At a diverging base lattice time, exponential tilting concentrates the spectral law at zero **lattice** energy using positive limiting mass in fixed low-energy intervals. A fixed additional number of lattice steps then has ratio tending to one. An additional fixed physical time probes `E/b` and does not follow from that concentration argument. These distinctions are retained in the disposition.

## Disposition

Supported in scope: finite site-form mechanism, exact straight-path rooted reversal, four-copy geometry, and the stated physical-time deductions conditional on positive transfer and fixed-separation limits. The constant-mode elimination and moment conclusions remain conditional on their explicit upstream analytic inputs. C4's complete Gaussian-field identification and continuum reconstruction are not certified by this cross-read or by the 22 scalar Lean declarations. The four-dimensional existence and mass-gap problem remains open in this program.
