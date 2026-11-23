# r5-chal report: challenge of Z4 S1, S2, S4, S6 (+C5)

Control: control.txt = 0.272341. Programs: powers.py (exit 1, expected 0: P2 and P5 failed, both from my own wrong expectations), powers2.py (exit 0). Results: result_powers.json, result_powers2.json. Child: child/ (see §5).

## 1. Verdict table

| item | verdict | evidence |
|---|---|---|
| S1 power b^-5 (sharp-time variance of smeared B_3^2) | STANDS | sharp cutoff local exponent 5.066 (shift explained by a Λ^4 term, below), Gaussian cutoff 5.015, point split a^-5 exactly; lattice C_b(0)·b^5 = 8.04, 8.09, 8.11 at N=24,48,96 |
| S1 coefficient ∝ ∫f² | STANDS | leading coefficient 2/(75π²)·∫f² for a sharp cutoff; after the derived Λ^4 correction, the residual is under 3% for both widths (Q2) |
| S1 "not removed by renormalisation" (C1 extra) | STANDS, sharpened | point split: C_a = c5 a^-5 + c3 a^-3 + c1 a^-1 + finite. c3 ∝ −∫\|∇f\|², c1 ∝ ∫(Δf)², checked to 4e-5 and 5e-3 (P7). With a sharp momentum cutoff the next term is a NONLOCAL Λ^4·∫\|p\|\|f̂\|², so subleading terms depend on the regulator. Vacuum subtraction does not change anything, because C is already connected |
| S2 C(t) finite for t>0, continuum formula k̂→\|k\| | STANDS | momentum grid and my real-space formula agree: C(0.5) = 1.73853 vs 1.73864 (P4) |
| S2 short-time behaviour (C2) | STANDS (new info) | C(t) ≈ ∫f²/(10π² t⁵) as t→0, ratio 0.99999983 (Q1) |
| S2 large-time behaviour (C2) | STANDS (new info) | C(t) ≈ 2(∫f)²/(π⁴ t⁸) in infinite volume, ratio 0.99996, exponent 7.99996 (P6). This is a power law, so no gap. The spectral density near 0 goes like E^7. If ∫f = 0, the power is faster but still a power |
| S2 "error O(b²)" | NOT CHECKED | measured only: lattice C_b(0.5) errors 36%, 39%, 7% at b = 0.5, 0.25, 0.125. This is pre-asymptotic (UV terms of size b^-5 e^{-ct/b}); no b² regime was reached |
| S4 lowest two-photon atom ≥ 2(2π/ℓ)(1+O(b²)) | STANDS | 729/729 total momenta checked, 0 violations, 19 reach 2·2π/ℓ (P8). On the lattice the atom lies BELOW 2·2π/ℓ by a relative π²b²/(6ℓ²) (P9), so the O(b²) is needed and has negative sign |
| S4 no one-photon or vacuum overlap | STANDS | :B²: acting on Ω = a†a†Ω only (algebra) |
| S4 "C(t) decays no faster than that rate" | DEFECT (missing hypothesis) | true only if f̂ ≠ 0 on one of the 19 lowest total momenta (for example ∫f ≠ 0). Otherwise the lowest occupied atom is higher |
| S4 "any argument from positivity, fixed size, bounded moments alone is wrong" | STANDS as a counterexample; the framing overreaches | see §2 |
| S6(a) Z(b) = const/(g² b⁴) at leading order | STANDS | ½Tr U_p = cos(g b²\|F\|/2) = 1 − g²b⁴\|F\|²/8 + O(b⁶) for SU(2) |
| S6(b) "Z with logarithmic corrections" suffices | DEFECT (incomplete; inference on a textbook basis) | the magnetic density B² alone is not a Lorentz scalar. It is a combination of the scalar F² (renormalised through β(g)/g·F², the trace anomaly; textbook) and T_00 (finite lattice renormalisation; Caracciolo et al. type; textbook). It also mixes with E² (same dimension; my inference). So a 2×2 multiplicative renormalisation is needed, plus identity mixing (b^-4, removed by centering). No gauge-invariant local scalar of dimension < 4 exists (textbook), so there is no other power-divergent mixing |
| S6(c) "variance floor of order 1/g_A, g_A = β²/2" | STANDS | hamiltonian-variance.md l.19 (Var F ≥ v_*), l.61 (v_*^-1 = O(g)); action-curvature.md l.40 (G V(g) ≥ v_*); g = β²/2 at spatial-limit.md l.3, action-curvature.md l.65 |
| S6(c) "scales of order 1/b on the bare trajectory" | DEFECT (misleading summary) | two-sided order 1/b holds only for the zero-momentum coherent sum and only averaged over g ∈ [G,2G] (action-curvature.md l.5, l.65). For a single plaquette A4 gives only an UPPER bound M_*/v_* = O(κ√g) = O(1/b) on the first moment (hamiltonian-variance.md l.61). Also, A4's single-plaquette variance ceiling is O(1/β) (refinement.md l.13: V_p ≤ 8u, g u ≤ 5√g/2), not O(β^-2). A4 is consistent with S6's g⁴ ~ β^-2 but does not confirm it |
| C5 "no sharp-time variance needed and none exists" (free theory) | STANDS | C(0) = ∞ (S1) while C(2τ) < ∞ (S2) |
| C5 using e^{-τH}O(f)Ω for the gap | partly STANDS (inference) | e^{-τH} is injective with dense range, so it maps a dense set to a dense set. A common rate m on a dense set gives E(0,m) = 0. But vectors from ONE field O = F² span only that field's cyclic subspace (in the free theory: C-even, even photon number). A gap shown there is a gap in that sector, not the mass gap. Every gauge-invariant local field would be needed |

Counts (this table): STANDS 13, DEFECT 3, NOT CHECKED 1 (sub-statements counted separately; "partly STANDS" counted as STANDS).
Own predicates: met 9 (P1, P3, P4, P6, P7, P8, P9, Q1, Q2), failed 2 (P2, P5), measured only 2 (M1 lattice; C(t) table). Child P_MC rerun by me: met 1.

## 2. Hypotheses each statement uses, and where they are stated

- S1/S2/S4: free (Gaussian) Maxwell on the Gauss-law subspace, zero modes removed (STATEMENT l.15). Periodic box (l.13). Smooth f of fixed width (l.23). Vacuum-centred O (l.23). Wick's theorem / Gaussian vacuum (l.25). The normalisation k̂/2 (l.19): I rederived it (H = ½∫(E²+B²), [A_i, E_j] = iδ). It is correct, and the lattice map B_3 = θ/(g b²), A_phys = A/(g b) is consistent.
- S4 also uses implicitly: f̂ ≠ 0 at one of the lowest total momenta (NOT stated, hence the DEFECT). The "weak-coupling limit" framing (l.9) is not used by the counterexample. As a counterexample, S4 shows only that positivity + fixed-size observable + bounded moments do not imply a gap. It says nothing about YM: at a fixed physical scale the continuum limit of compact YM is not the free theory (asymptotic freedom; Λ_YM fixed). At fixed physical volume, compact zero modes and torons are removed by hand here ("zero modes removed"), and the non-abelian Gauss law is replaced by an abelian one. "As must be" holds for the benchmark only.
- S6: Hamiltonian Wilson/Kogut–Susskind lattice, bare trajectory κ = 2/(βb), λ = β/b (A4 spatial-limit.md l.3). Leading-order perturbation theory only (STATEMENT l.45: "conjectural").

## 3. Failed predicates (kept)

- P2 (powers.py): C/(Λ⁵∫f²) came out 0.957 (w=1) and 0.938 (w=0.7) of 2/(75π²), against my 3% tolerance. Cause: MY expectation was wrong. A sharp cutoff on both propagators gives a nonlocal Λ⁴ term with relative size −1.25⟨\|p\|⟩/Λ. I derived it afterwards and confirmed it (Q2, ratio 0.97–0.98). This is not a defect of the target.
- P5 (powers.py): C(t)t⁵ / [∫f²/(50π²)] = 5.000. Cause: my arithmetic slip; the correct constant is 1/(10π²) (Q1). Not a defect of the target. (The statement gives no constant.)
- PCP check K1 therefore shows exit 1 against an expected 0. I did not re-label it.

## 4. Not checked

S2's O(b²) rate (pre-asymptotic up to N = 96). S3 and S5 (not in my brief). Lattice checks of S4 beyond the dispersion relation. The literature references in S6(b) were not re-read (no network); they are marked textbook from memory. Whether A4's linked README/controls files (not provided) change the reading of S6(c). Non-Gaussian f and f with ∫f = 0 numerically.

## 5. Delegated question and outcome

Question delegated (child/, its own register child/pcp): for free 3+1 Maxwell, f = exp(-|x|²/2), find the powers and constants of C(t) as t→0 and as t→∞, using a method of the child's choice. The child had to derive the two-point normalisation itself, not take it from the statement. Control question: ∫x²e^{-x} = 2. The child answered 2.000… (child/control.txt).

What came back (child/notes.md, read by me): G(x,t) = (t² + x_3² − x_1² − x_2²)/(π²(r²+t²)³), the same as my independent formula. p0 = 5, A0 = 1/(10√π). p∞ = 8, A∞ = 16/π. With ∫f² = π^{3/2} and (∫f)² = 8π³ these equal my ∫f²/(10π²) and 2(∫f)²/π⁴, so the results agree.

The child's checks: twopoint_check (K1, PASS, by its notes); mc_check (K2), an independent momentum-space Monte Carlo with a fixed seed. **I reran mc_check myself**: t=1 C_MC = 4.97303e-2 ± 8.8e-5 vs quadrature 4.96061e-2 (1.41σ); t=2 1.19688e-3 ± 8.5e-7 vs 1.196594e-3 (0.34σ); PASS. Its quadrature values equal my Ct_table entries (0.0496061, 0.00119659).

The child's corr.py was still running when I closed; the session was over budget. Its numerical power fits are NOT used, so the child verify line is not available. corr.py uses the same position-space method as my powers.py, so it would not have been independent of my check anyway. The independent part is the child's derivation of the constants plus the momentum-space MC. Shared model family: the agreement is not independent review.

## 6. Rerun commands (bash, from C:/Users/donke/z4-workers/r5-chal, PYTHONUTF8=1)

```
python -c "import math;print(f'{-math.log(math.tanh(1)):.6f}')"
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name powers  --expect-exit 0 -- python powers.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py check --ws pcp --name powers2 --expect-exit 0 -- python powers2.py
python C:/Users/donke/pcp-os/PCP_OS_Python/pcp_os.py verify --ws pcp
```
(Each rerun writes a new numbered result file; results are never overwritten.)

PCP verify (last line): `result: PASS (a local fact about these files; it authenticates nobody and says nothing about whether a finding is right)`
