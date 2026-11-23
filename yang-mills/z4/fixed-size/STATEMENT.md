# An observable of fixed physical size: statements under test

Director Z4, 23 November 2026. Kirtus Justus, Theoretical Physicist, Port Coquitlam, British Columbia, Canada, directs the work. Prepared with assistance from Claude (Anthropic).

Status of this file: statements drafted for attack, before any worker has run. Nothing here is a result until the review record below it says so. Nothing here is a statement about interacting four-dimensional Yang–Mills theory; S1 to S4 concern a free (Gaussian) lattice theory, S5 is abstract, S6 is a conjectural reading and is marked so.

## Why

The overall disposition found that every positive result in the repository uses the single lattice plaquette at a sharp time, and that its spectral weight sits at energies of order 1/b. The question here is what must replace it. The weak-coupling limit of a lattice gauge theory is, to leading order, a free theory of dim(G) photons; in that free theory everything can be computed, so it is a known-answer benchmark for any proposal.

## Setting: free lattice Maxwell theory in Hamiltonian form

Periodic cubic lattice of side N, spacing b, physical side ℓ = Nb. Real link variables A_i(x), conjugate E_i(x), [A_i(x), E_j(y)] = i δ_ij δ_xy. Plaquette angle θ_ij(x) = A_i(x) + A_j(x+e_i) − A_i(x+e_j) − A_j(x).

H = (g²/2b) Σ E_i(x)² + (1/(2g²b)) Σ_{x, i<j} θ_ij(x)², on the Gauss-law subspace, zero modes removed.

Lattice momenta k ∈ (2π/ℓ)ℤ³ in the Brillouin zone, k̂_i = (2/b) sin(k_i b/2), k̂ = |(k̂_1, k̂_2, k̂_3)|. Each k ≠ 0 carries two transverse oscillators of frequency ω(k) = k̂. The physical magnetic field is B_3(x) = θ_12(x)/(g b²). Its vacuum two-point function at Euclidean time separation t ≥ 0 is

D_t(x − y) = ⟨B_3(x) e^{−tH} B_3(y)⟩ = ℓ⁻³ Σ_{k ≠ 0} e^{ik·(x−y)} · ((k̂_1² + k̂_2²)/k̂²) · (k̂/2) · e^{−t k̂}

(the factor (k̂_1² + k̂_2²)/k̂² is the transverse projector for the 3-component; the normalization k̂/2 is to be rederived by the worker, not assumed).

Observable: for a smooth f of fixed physical width, O_b(f) = b³ Σ_x f(bx) (B_3(x)² − ⟨B_3²⟩). It is the free-theory image of a smeared plaquette action: for a compact group the plaquette character is 1 − const·g²b⁴·B² + higher order.

Correlator: C_b(t) = ⟨O_b(f) e^{−tH} O_b(f)⟩. The vacuum is Gaussian, so by Wick's theorem C_b(t) = 2 b⁶ Σ_{x,y} f(bx) f(by) D_t(x−y)².

## Statements

**S1 (sharp-time divergence).** At t = 0 and fixed f, ℓ: C_b(0) grows like b⁻⁵ as b → 0. Precisely, C_b(0)·b⁵ converges to a positive constant times ∫f². Reason: D_0(0)² ~ b⁻⁸ and the sum over coincident points contributes b⁶·(number of points ~ b⁻³)·b⁻⁸. So the sharp-time smeared action density has no limit as a vector; its variance diverges, and this is not removed by any b-independent normalization of f.

**S2 (positive time converges).** For each fixed t > 0, C_b(t) converges as b → 0 to a finite positive limit C(t), with error O(b²). The limit is given by the same formula with k̂ replaced by |k| and the sum over all k ∈ (2π/ℓ)ℤ³ \ {0}.

**S3 (the regularized vector).** Fix a physical τ > 0 and put v_b = e^{−τH} O_b(f) Ω. Then ‖v_b‖² = C_b(2τ) converges to a positive limit, and the first two spectral moments of v_b, M_1 = −C_b′(2τ) and M_2 = C_b″(2τ), converge too, with M_1/M_0 and M_2/M_0 bounded by constants times 1/τ and 1/τ² uniformly in b. So v_b is an observable-generated vector of fixed physical size whose norm and energy moments stay in a fixed physical window, in a theory where the sharp-time vector does not exist.

**S4 (no gap in the benchmark, as must be).** The spectral measure of v_b is supported on two-photon energies ω(k) + ω(k′) with k + k′ in the support of f̂; in infinite volume it reaches down to zero. In the periodic box its lowest atom is at or above 2·(2π/ℓ)·(1 + O(b²)) and C(t) decays no faster than that rate. The benchmark has no mass gap, and any argument that would give one for v_b from positivity, a fixed-size observable and bounded moments alone is wrong.

**S5 (abstract, to be proved in Lean).** For a finite positive sum of atoms ν = Σ w_i δ_{E_i}, E_i ≥ 0, w_i ≥ 0, and C(t) = Σ w_i e^{−tE_i}, for every τ > 0:
- (a) Σ w_i E_i e^{−2τE_i} ≤ C(τ)/(e τ);
- (b) Σ w_i E_i² e^{−2τE_i} ≤ 4 C(τ)/(e² τ²);
- (c) C((s+t)/2)² ≤ C(s) C(t);
- (d) for E₀ > 0: Σ_{E_i > E₀} w_i e^{−2τE_i} ≤ e^{−τE₀} C(τ), hence the regularized weight in [0, E₀] is at least C(2τ) − e^{−τE₀} C(τ);
- (e) if C(2τ) ≥ v > 0 and C(τ) ≤ V then with E₀ = (1/τ) log(2V/v) the regularized weight in [0, E₀] is at least v/2.
Consequence: for the regularized vector, A4's kind of condition (norm bounded below, energy moments bounded above, weight in a bounded window, all in physical units) follows from a two-sided bound on the positive-time correlator at the two physical times τ and 2τ: v ≤ C_b(2τ) and C_b(τ) ≤ V, uniformly in b. No sharp-time variance is needed and none exists.

**S6 (reading for the interacting theory; conjectural, not a result).** For lattice Yang–Mills the same construction would read: O_b(f) = Z(b)·b³ Σ_x f(bx)·(plaquette action density − its vacuum value), v_b = e^{−τH_b} O_b(f) Ω, with Z(b) = const/(g(b)² b⁴) at leading order and logarithmic corrections beyond it. The existence-and-nontriviality obligation for this one observable is then: v ≤ C_b(2τ) and C_b(τ) ≤ V uniformly along the trajectory. The gap obligation is: C_b(t) ≤ K e^{−m(t−τ)} for t ≥ τ with m > 0 uniform. The free benchmark satisfies the first and fails the second. Consistency checks against the other lanes, at leading order only: the sharp-time plaquette variance of the unnormalized trace should scale like g⁴ ~ β⁻², and its energy scale like 1/b; A4's lane reports a variance floor of order 1/g_A with g_A = β²/2 and scales of order 1/b on the bare trajectory.

## What would break this

A wrong power in S1; non-convergence or a different limit in S2; a b-dependence hidden in the moment bounds of S3; an error in the transverse projector or the normalization of D_t; an S5 inequality with a wrong constant; a misreading of A4's scalings in S6.


---

# Review record (23 November 2026) and the statements as they now stand

The text above is the draft as it was handed to the workers, unchanged. Three PCP workers attacked it (register checks K21, K22, K23), each with one sub-agent and its own register; all six registers replay. Reports and files: [`../reviews/r5-bench/`](../reviews/r5-bench/), [`../reviews/r5-lean/`](../reviews/r5-lean/), [`../reviews/r5-chal/`](../reviews/r5-chal/). The director reread the three reports, recompiled the Lean file (K24, exit 0, standard axioms only, no `sorry` in the source) and reran the benchmark programs in a fresh directory (K25, result files byte-identical).

## Verdicts

| Statement | Verdict | Evidence |
|---|---|---|
| D_t, normalization k̂/2 and projector | stands | Rederived by two workers independently; direct oscillator computation on a 4³ lattice agrees to 10⁻¹³. Notation: the phase needs a factor b when x is an integer site. |
| S1, power b⁻⁵ and coefficient ∝ ∫f² | stands | Lattice ratios per halving 32.31, 32.08, 32.02; fitted exponent −5.002; C_b(0)·b⁵ → 8.110·10⁻³; the ratio between the two widths → 8.005 against 8 for ∫f². Continuum: point splitting gives a⁻⁵ exactly, leading coefficient 2/(75π²)·∫f² for a sharp cutoff. Sharpened: the subleading terms are a⁻³·∫|∇f|², a⁻¹·∫(Δf)² for point splitting and depend on the regulator. |
| S2, convergence at t > 0 | stands, with a missing hypothesis | Lattice at N = 128 against the sub-agent's independent continuum sum: 6 of 6 within tolerance; after Richardson extrapolation 2.8·10⁻⁵ (t = 0.2) and 3.5·10⁻⁴ (t = 0.1). The O(b²) rate is seen only once t·k̂_max ≫ 1: at t = 0.05 the coarsest doubling fails (ratio 1.2), and the challenger's coarser lattices never reached the regime. New: C(t) ≈ ∫f²/(10π²t⁵) as t → 0 and ≈ 2(∫f)²/(π⁴t⁸) as t → ∞ in infinite volume. |
| S3, regularized vector | stands | τM₁/M₀ between 2.6 and 3.2 and τ²M₂/M₀ between 8 and 11.4 for all N, both widths and both τ; change below 1.7% from N = 64 to 128; below the S5 bounds. The bounds' constants depend on τ and on the width through C(τ)/C(2τ) (13 to 33 here), so "constants times 1/τ" is true at fixed f and τ, not uniformly in τ. |
| S4, no gap | stands; two defects of wording | Decay rate at t = 3: 12.5694 against 4π = 12.5664; infinite-volume tail t⁻⁸, spectral density ∝ E⁷ near zero. No one-photon or vacuum overlap. Defects below. |
| S5 (a) to (e) | stands, proved | [`../lean/Z4YM/HeatRegularized.lean`](../lean/Z4YM/HeatRegularized.lean), 13 declarations. The constants 1/(eτ) and 4/(e²τ²) are sharp (one atom at 1/τ, at 2/τ). Unused hypotheses: E ≥ 0 in (a), (c), (d); E₀ > 0 in (d). In (e), v ≤ V and E₀ > 0 follow and need not be assumed. Both mutations of the constants rejected. Added: (f) spectrum in {0} ∪ [m, ∞) gives C(t) − P₀ ≤ e^{−m(t−s)}(C(s) − P₀); (g) an atom in (0, m) with positive weight defeats every bound K·e^{−mt}, with an explicit time. Finite sums only; the measure version is not formalized. |
| S6 (a), Z ∝ 1/(g²b⁴) | stands at leading order | ½Tr U_p = 1 − g²b⁴|B|²/8 + …, three colour components. |
| S6 (b) | **defect** | Below. |
| S6 (c) | **defect** | Below. |

## Defects of the draft, all Z4's

1. **S4, "its lowest atom is at or above 2·(2π/ℓ)·(1 + O(b²))".** On the lattice the lowest two-photon energy is 4N·sin(π/N)/ℓ, below 4π/ℓ by the relative amount π²b²/6. The statement is true only if the O(b²) term may be negative; it should give the value.
2. **S4, "C(t) decays no faster than that rate".** True only if f̂ does not vanish on the lowest total momenta (for example ∫f ≠ 0). Hypothesis missing.
3. **S4, framing.** As a counterexample it shows exactly this: positivity, a fixed-size observable and bounded moments do not imply a gap. "As must be" and "the weak-coupling limit" overreach: at a fixed physical scale the continuum limit of the compact non-abelian theory is not the free theory, and the benchmark removes zero modes by hand and has an abelian Gauss law. The benchmark is a known-answer test for a method, not a model of Yang–Mills.
4. **S6 (b), "Z(b) with logarithmic corrections".** Incomplete. The magnetic density B² alone is not a Lorentz scalar: it is a combination of the scalar F² (renormalized through the trace anomaly) and the energy density T₀₀, and on a Hamiltonian lattice it mixes with E² at the same dimension. A two-by-two multiplicative renormalization is needed, besides the identity mixing removed by centering. There is no gauge-invariant local operator of dimension below four, so no other power-divergent mixing. The challenger marks the first parts textbook from memory (no literature was consulted) and the E² mixing as its own inference.
5. **S6 (c), consistency with A4.** "Variance floor of order 1/g_A" is a fair summary. "Scales of order 1/b" is not: A4 proves a two-sided 1/b scale only for the zero-momentum coherent sum averaged over a coupling window; for one plaquette A4 has only an upper bound of that order. And A4's single-plaquette variance ceiling is of order 1/β, not β⁻², so A4's bounds are compatible with the leading-order g⁴ scaling and do not confirm it.
6. **One field is one sector** (challenger, on the use of the regularized vectors). e^{−τH} has dense range, so regularization costs nothing for D4's dense-family criterion. But vectors generated by one field span only that field's cyclic subspace; a decay rate proved for them is a gap in that sector. The draft did not say this.

## The statements as they now stand

For free lattice Maxwell theory in a periodic box, with f smooth, O_b(f) the centered smeared B₃², and C_b(t) its Euclidean-time correlator:

- **S1′.** C_b(0)·b⁵ → c·∫f² with c > 0. The sharp-time vector has no limit. (Lattice: measured to N = 128. Continuum power: derived.)
- **S2′.** For fixed t > 0, C_b(t) → C(t), finite and positive, given by the continuum mode sum; the error is O(b²) once t/b is large. (Measured against an independent computation; not proved.)
- **S3′.** At fixed f and τ > 0 the vector e^{−τH}O_b(f)Ω has norm and first two energy moments convergent in physical units, bounded through S5 by C_b(τ)/C_b(2τ). (Measured.)
- **S4′.** In the box the lowest energy carried is 4N·sin(π/N)/ℓ → 4π/ℓ when f̂ is nonzero on the lowest total momenta; in infinite volume C(t) ~ t⁻⁸. So: reflection positivity, an observable of fixed physical size, a norm bounded below and energy moments bounded above, all in physical units and uniformly in the cutoff, do not imply a gap. (Shown by this example.)
- **S5.** As drafted, proved for finite sums, with (f) and (g).
- **S6′ (conjectural reading; not a result).** For lattice Yang–Mills the candidate fixed-size vectors are e^{−τH_b}O_b(f)Ω with O_b built from the renormalized scalar and energy densities, a two-by-two renormalization of the magnetic and electric plaquette densities at leading order ∝ 1/(g²b⁴). For such a vector, existence and nontriviality in a fixed physical window reduce by S5 (e) to v ≤ C_b(2τ) and C_b(τ) ≤ V uniformly along the trajectory, and a gap in the sector it generates is, by S5 (f) and (g) for finite sums, the bound C_b(t) − P₀ ≤ e^{−m(t−s)}(C_b(s) − P₀) with m uniform. The mass gap needs this for every gauge-invariant local field. Neither bound is known in four dimensions for any trajectory with b → 0.

## What this is and is not

It is a change of target for the fixed-mesh programme: from the sharp-time plaquette, which the benchmark shows cannot have a continuum limit as a vector even in the free theory (variance ∝ b⁻⁵), to positive-time correlators of a renormalized density, which do. It gives the other lanes' quantities a form that can survive refinement: A4's variance and moment conditions become two values of one correlator; D4's rate criterion applies to the same correlator.

It is not progress on the estimate itself. The two-sided bound on C_b at weak coupling is the whole difficulty, and nothing here bounds it. The free benchmark satisfies the first reduction and fails the gap, as a free theory does.

Counts, as met, failed, measured only. Benchmark programs 56, 4, 17 (two failures are the worker's own range of N at t = 0.05; two are defect 1 above, predicted in its docstring before the run). Challenger 9, 2, 2 (both failures its own expectations: a nonlocal Λ⁴ term with a sharp cutoff; an arithmetic slip in a constant). Formalizer: 13 declarations, one failed intermediate compile; its numerics 4, 0, 0 on 2000 atom sets. The challenger's sub-agent left one program unfinished at the budget; its fits are not used.

Director, workers and sub-agents are one model family; this is not independent review. No literature was consulted for the renormalization statements in defect 4.

---

# Addendum, 23 November 2026: S6′ with the gradient-flowed action density

After the literature was read (`../LITERATURE.md`; Lüscher, arXiv:1006.4518; Lüscher and Weisz, arXiv:1101.0963). Conjectural reading, not a result.

**S6″.** Lattice SU(N), spacing b, coupling trajectory β(b), Wilson flow to a fixed physical flow time t. E_b(t, x) a lattice discretization of the flowed ¼G·G. O_{b,t}(f) = b³Σ_x f(bx)(E_b(t, x) − ⟨E_b(t)⟩) on one time slice; C_{b,t}(τ) its connected Euclidean-time correlator.

- Existence and nontriviality for this observable: 0 < c ≤ t²⟨E_b(t)⟩ ≤ C, and v ≤ C_{b,t}(2τ), C_{b,t}(τ) ≤ V, uniformly as b → 0 along the trajectory. By S5 (e) (`MeasureHeat.M3`) a fixed weight then lies in a fixed physical window.
- A gap in the sector it generates: C_{b,t}(τ) ≤ K·e^(−mτ) for τ ≥ τ₀ with m > 0 uniform in b and in the volume (`MeasureHeat.M4_gap`, `M5_no_bound`).
- Caveats: a four-dimensional flow reaches links at all times, so exact reflection positivity on a slice needs the spatial flow or control of the heat-kernel tails; the mass gap needs every gauge-invariant local field, not one.
- Known: finiteness of all such correlators at positive flow time, order by order in perturbation theory in dimensional regularization, with no renormalization beyond the coupling; t²⟨E⟩ = 3(N²−1)g²/(128π²) at leading order; numerical scaling on the lattice. Not known: any of the bounds above nonperturbatively. Perturbation theory gives power-law decay.
- Free benchmark (worker's program, `../reviews/r10-lit2/`): ⟨B₃²⟩ = 1/(48π²t²) under the spatial flow; the equal-time variance of the smeared flowed B₃² is finite for every t > 0 and tends to (√π/(640π²))·∫f²·t^(−5/2) for smearing width much larger than √t. The sharp-time b⁻⁵ of S1′ becomes (√t)⁻⁵.

S6′ above used the time-evolved plaquette density, which mixes magnetic and electric parts; S6″ replaces it.

---

# Note, 23 November 2026 (second session): S6″ is superseded

S6″ and its caveat cannot both hold: under a flow of the spatial links alone the electric half of ¼G·G is not regularized (wildcard worker, `../reviews/r12-wild/`), and under the four-dimensional flow the flowed algebra is not reflection positive (C4; reproduced in `../reviews/r11-flowchal/`). The text above is kept as written. The statement as it now stands is S6‴ in [`SPATIAL_FLOW.md`](SPATIAL_FLOW.md).
