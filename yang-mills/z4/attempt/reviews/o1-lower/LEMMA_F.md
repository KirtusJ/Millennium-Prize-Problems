**Proved (in writing here, not independently reviewed): Lemma F in the η-form of TUNNEL_THEOREM.md §2. For every η > 0 there is β₀(η) such that for all β ≥ β₀ and ALL s ∈ [0,1]: ε_eff = −log‖F_a‖ ≥ 2 asinh(s) − η. Concretely: ε_eff ≥ 0 for all s and β (trivial), and for s ∈ [s₀,1], ε_eff ≥ 2 asinh(s) − log max(M_in, A·M_out) with the explicit M_in, M_out of Theorem 1, which → 0 uniformly on [s₀,1] for each fixed s₀ > 0 (τ = δ = β^{−1/3}). No explicit power rate uniform in s is proved; a (log β/β)^{1/4} rate is CLAIMED (§5, sketch only).**

Worker n1-lemF (task T134). I share a model family with the director; this is not independent review.

## 0. Setting (as in TUNNEL_THEOREM.md §1)

U = (x₀,x₁,x₂,x₃) ∈ S³ ≅ SU(2), Haar = normalised surface measure. ρ² = r = x₁² + x₂², w = (x₁,x₂), R = √(1−r).
k(U,U') = e^{β cos θ(U⁻¹U')}/Z. F = e^{−V/2} K e^{−V/2}, V/2 = βs²r. Put

α = 2s√(1+s²), c = s² + α/2, A = 1 + 2c = 1 + 2s² + 2s√(1+s²).

## 1. Ingredients (each tagged)

**(I1) Kernel in ambient coordinates. PROVED.** For g = U⁻¹U', ½ tr g = Re(Ū U') = ⟨U,U'⟩ (R⁴ inner product), and ½ tr g = cos θ(g). So k(U,U') = e^{β⟨U,U'⟩}/Z, and e^{β⟨U,U'⟩} = e^{β} e^{−(β/2)|U−U'|²} on S³ (the brief's "check!": correct).

**(I2) Z = 2 I₁(β)/β. PROVED** (x₀ has density (2/π) sin²θ dθ, x₀ = cos θ; (1/π)∫₀^π e^{β cos θ} sin²θ dθ = I₁(β)/β by integrating ∫ e^{βcos θ} cos θ by parts). Checked numerically (Q1, β = 1, 64, 1024, rel. err ≤ 2e−12).

**(I3) Coordinates. PROVED.** U = (R cos φ, w, R sin φ), w in the unit disc D. In R⁴ = R²_w × R²_{(x₀,x₃)} with polar (ϱ,φ) in the second factor, the surface measure is δ(√(ϱ²+r) − 1) d²w ϱ dϱ dφ = d²w dφ (the Jacobian ∂_ϱ√(ϱ²+r) = ϱ cancels ϱ). Total 2π·π = 2π², so dU = d²w dφ/(2π²). The brief's "(check: this was used elsewhere)": correct.
Integrating φ': ∫₀^{2π} e^{βRR' cos(φ−φ')} dφ' = 2π I₀(βRR'). Hence for ψ = ψ(r):

 (Fψ)(U) = e^{−βs²r} (1/(πZ)) ∫_D I₀(βRR') e^{βw·w'} e^{−βs²r'} ψ(r') d²w'.

**(I4) Schur/Barta test. PROVED (classical, one line).** F is self-adjoint with a positive kernel. If ψ > 0 and Fψ ≤ λψ pointwise, then for f ∈ L², by Cauchy–Schwarz |Ff(x)|² ≤ (∫F(x,y)ψ(y))(∫F(x,y)|f(y)|²/ψ(y)) ≤ λψ(x)∫F(x,y)|f(y)|²/ψ(y). Integrating in x and using symmetry and Fψ ≤ λψ again gives ‖Ff‖² ≤ λ²‖f‖².

**(I5) Flat fixed point. PROVED, Lean `fixed_point`, `two_arsinh_eq_log`.** α/2 − s² = c/A and log A = 2 asinh s. For ψ = e^{−βαr/2} and every w ∈ R²,
 e^{β(α/2−s²)r} (β/2π) ∫_{R²} e^{−(β/2)|w−w'|² − βc r'} d²w' = 1/A.
(Gaussian integral: the w'-precision is β(1+2c) = βA, the value is (1/A)·exp(βr[α/2 − s² − ½ + 1/(2A)]) and the bracket is 0 by the identity.) As a probability, the normalised integrand in w' is N(w/A, (βA)⁻¹ I₂). This is the brief's oscillator: ε = log A = arccosh(1+2s²) = 2 asinh s.

**(I6) Bessel envelope. PROVED.** For 0 < δ ≤ 1 and z > 0,
 e^{−z} I₀(z) ≤ H̃_δ(z) := min(1, H_δ(z)), H_δ(z) = [2πz(1 − 5δ²/48)]^{−1/2} + e^{−z(1−cos δ)}.
Proof: I₀(z) = (1/π)∫₀^π e^{z cos t}dt ≤ e^z. On [0,δ], 1 − cos t ≥ (t²/2)(1 − 5δ²/48) (Lean `one_sub_cos_ge`, TUNNEL_THEOREM's Lean target, from Mathlib `Real.cos_bound`); extend to [0,∞). On [δ,π], e^{z cos t} ≤ e^{z cos δ}. H̃_δ is decreasing in z. Checked on a grid (Q2).

**(I7) Lower bound on I₁. PROVED.** I₁(z) ≥ e^z (1 − 1/(2z))/√(2πz) − 1/2.
Proof: on [π/2,π] the integrand of (1/π)∫ e^{z cos t} cos t is ≥ −1. On [0,π/2], e^{z cos t} cos t ≥ e^{z(1−t²/2)}(1−t²/2) (both factors' lower bounds are ≥ 0 where 1 − t²/2 ≥ 0; elsewhere the right side is negative). The integrand on [π/2,∞) is negative, so ∫₀^{π/2} ≥ ∫₀^∞ = √(π/2z)(1 − 1/(2z)). Checked (Q3). Hence e^β/I₁(β) ≤ √(2πβ)/D, D = 1 − 1/(2β) − √(2πβ) e^{−β}/2.
(DLMF 10.40.1 gives the exact asymptotics 1 − 3/(8z); NOT fetched, not used.)

**(I8) AM–GM. PROVED, Lean `amgm_pair`.** For x, y ∈ [0,1]: xy ≤ √(xy) ≤ (x+y)/2. With x = 1−r, y = 1−r': (1−r)(1−r') ≤ RR' ≤ 1 − (r+r')/2.

**(I9) Outer exponent. PROVED, Lean `weak_duality`, `quad_step`; checked (Q4).** For unit q ∈ R², p = (R, ρ), μ > 0: p·q − c q₂² ≤ (1−r)/(2μ) + r/(2(μ+2c)) + μ/2. Let g(μ) = that bound − 1 + (c/A)r. Then g(1) = 0 (by A = 1+2c), g'(1) = γ := (r/2)(1 − 1/A²) ∈ [0, ½), g'' = (1−r)/μ³ + r/(μ+2c)³ ≤ 8 on [½,1]. Taylor at μ = 1 − γ/8: g ≤ −γ/8·γ + 4(γ/8)² = −γ²/16. So
 Φ(r) := (c/A) r − 1 + max_{q∈S¹}(p·q − c q₂²) ≤ −(r²/64)(1 − 1/A²)².

## 2. Theorem 1 (master bound). PROVED

For β > 1, s ∈ (0,1], 0 < τ < 1/5, 0 < δ ≤ 1, with ψ = e^{−βαr/2}:

 ‖F_a‖ ≤ (1/A) · max(M_in, A·M_out),
 M_in = (1/D)·{ [(1−τ)(1−4τ)(1−5δ²/48)]^{−1/2} + √(2πβ) e^{−β(1−5τ)(1−cos δ)} + √(2πβ) e^{−βAτ/2} },
 M_out = (β√(2πβ)/(2D)) · exp(−βτ²(1 − 1/A²)²/64).

Proof. By (I4) it suffices to bound B(w) := (Fψ)(w)/ψ(w).
*Interior, r ≤ τ.* By (I3), B(w) = e^{β(α/2−s²)r}(1/(πZ))∫_D I₀(βRR') e^{βw·w'−βcr'} d²w'. By (I6) and (I8), I₀(βRR') ≤ e^{β(1−(r+r')/2)} H̃_δ(β(1−r)(1−r')) (exponential increasing, H̃ decreasing, RR' ≥ (1−r)(1−r')). Since −(r+r')/2 + w·w' = −|w−w'|²/2 and 1/(πZ) = (β/2π)/I₁(β), by (I5)
 B(w) ≤ (1/A) E[G(r, |W'|²) 1_{|W'|<1}], W' ~ N(w/A, (βA)⁻¹ I₂), G(r,r') = (e^β/I₁(β)) H̃_δ(β(1−r)(1−r')).
On {r' ≤ 4τ}: G ≤ (√(2πβ)/D) H_δ(β(1−τ)(1−4τ)), which is ≤ the first two terms of M_in (use (1−τ)(1−4τ) ≥ 1−5τ in the exponential). On {r' > 4τ}: |w/A| ≤ √τ, so |W' − w/A| > √τ, probability exactly e^{−βAτ/2} (2-D Gaussian), and G ≤ e^β/I₁(β) ≤ √(2πβ)/D (H̃ ≤ 1). Sum: B(w) ≤ M_in/A.
*Outer, r > τ.* I₀(z) ≤ e^z. For w' ∈ D, RR' + w·w' ≤ RR' + ρ|w'| = p·q with q = (R', |w'|) unit, and r' = q₂². So by (I5)'s identity α/2 − s² = c/A and (I9), B(w) ≤ (1/(πZ))·π·e^{β(1+Φ(r))} = (βe^β/(2I₁(β))) e^{βΦ(r)} ≤ M_out (as −r²/64·(…)² ≤ −τ²/64·(…)²). ∎

So ε_eff ≥ 2 asinh(s) − log max(M_in, A·M_out). Uniformity in s: M_in does not increase with s (A ≥ 1); M_out·A ≤ (1+2+2√2)·M_out and 1 − 1/A² ≥ 1 − (1+2s₀)^{−2} for s ≥ s₀ since A ≥ 1+2s.

## 3. Corollary (Lemma F, η-form). PROVED

(a) ‖F_a‖ ≤ ‖K‖ ≤ ∫k = 1 (e^{−V/2} ≤ 1; Schur/Young with k ≥ 0, ∫k = 1), so ε_eff ≥ 0 for every s, β. Since asinh(s) ≤ s, for s ≤ η/2: ε_eff ≥ 0 ≥ 2 asinh(s) − η.
(b) For s ∈ [η/2, 1] take τ = δ = β^{−1/3} (τ < 1/5 once β > 125). Then log M_in = O(β^{−1/3}) + O(√β e^{−β^{1/3}/3}) → 0 and log(A·M_out) ≤ log(5.83·β^{3/2}√(2π)/(2D)) − β^{1/3}(1−(1+η)^{−2})²/64 → −∞, both uniformly in s ∈ [η/2,1]. Choose β₀(η) so that both are ≤ η. ∎

β₀ is explicit but huge for small η: the outer term needs β^{1/3}(1−(1+η)^{−2})²/64 ≳ 1.5 log β. E.g. η = 0.2 (s₀ = 0.1): measured (check_lemF run2) the master deficit log max(M_in, A M_out) at s = 0.1 is still 24.9 at β = 10¹²; it drops below η only near β ≈ 10¹⁴ (my estimate, not run). At s = 1 it is 5e−4 at β = 10¹¹. At β ≤ 4096 the master bound is useless (deficit 6.5 to 14 nats). The loss is in the outer region (the crude I₀ ≤ e^z and area·sup bound), not in the true Barta ratio, which is already within 1e−3 of 2 asinh s at β = 4096 for all six s values (below).

## 4. Numerics (check_lemF.py run2; child T138 independently)

Barta ratio B_sup = sup_ρ B by 1-D quadrature (angles integrated exactly), compared with ε = 2 asinh s and the exact ε_eff from the target's eps_eff.py. See results/check_lemF_run2.json and report.md for the table. Summary: −log B_sup ≤ ε_eff in every case (Schur consistency), and −log B_sup − ε = −O(1/β) (β = 4096: −2e−4 to −4e−4 for s ≥ 0.1). So the plain Gaussian ψ already gives Lemma F at these β; what the proof lacks is a sharp *analytic* control of the outer region, not a better test function.

## 5. Rate (CLAIMED, not proved)

Taking τ = s₀ = (C log β/β)^{1/4} and using 1 − 1/A² ≥ 4s/9 (s ≤ 1) makes A·M_out ≤ 1 for s ≥ s₀ when C ≈ 648; the interior gives log M_in ≈ 5τ/2. This would give ε_eff ≥ 2 asinh s − 3(648 log β/β)^{1/4} for all s ∈ [0,1], β ≥ β₁. I have not written the constants out carefully nor checked β₁; tag CLAIMED.

## Step tags

| step | tag |
|---|---|
| I1 kernel = e^{β⟨U,U'⟩}/Z | PROVED |
| I2 Z = 2I₁/β | PROVED, checked |
| I3 Haar = d²w dφ/2π², φ'-integral → I₀ | PROVED |
| I4 Schur/Barta | PROVED (classical) |
| I5 flat fixed point, log A = 2 asinh s | PROVED, Lean |
| I6 I₀ envelope | PROVED; core 1−cos bound Lean (`one_sub_cos_ge` from the director's Tunnel.lean, recompiled by me as Tunnel_copy.lean: exit 0, standard axioms) |
| I7 I₁ lower bound | PROVED, checked |
| I8 AM–GM pair | PROVED, Lean |
| I9 outer exponent | PROVED; scalar cores Lean; inequality checked on grid |
| Theorem 1 | PROVED |
| Lemma F (η-form) | PROVED |
| explicit rate (log β/β)^{1/4} | CLAIMED |
| Lemma R (target's reduction) | used only as a numerical reference (eps_eff.py); my proof does NOT use Lemma R |
